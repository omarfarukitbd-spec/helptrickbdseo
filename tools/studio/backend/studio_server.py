#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/studio/backend/studio_server.py
--------------------------------------------------------------
HelpTrickBD Autonomous Publishing Studio — Local HTTP Server & API.

Zero-dependency local server using Python's built-in http.server.
Runs on http://localhost:8501
"""

import os
import sys
import json
import time
import urllib.parse
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.studio.backend.studio_engine import (
    parse_pdf_text,
    generate_studio_blueprint,
    render_official_thumbnail_card
)
from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID
from tools.indexer.pubsub_hub_pinger import ping_all_hubs
from tools.backup_manager.post_backup_manager import create_post_backup
from tools.governance.pre_flight_checker import PreFlightChecker

FRONTEND_DIR = os.path.join(PROJECT_ROOT, "tools", "studio", "frontend")
SCRATCH_DIR = os.path.join(PROJECT_ROOT, "scratch", "studio_uploads")
os.makedirs(SCRATCH_DIR, exist_ok=True)

class StudioHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=FRONTEND_DIR, **kwargs)

    def _set_cors(self, content_type="application/json"):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Content-Type", content_type)

    def do_OPTIONS(self):
        self.send_response(200)
        self._set_cors()
        self.end_headers()

    def do_GET(self):
        url = urllib.parse.urlparse(self.path)

        if url.path == "/api/status":
            self.send_response(200)
            self._set_cors()
            self.end_headers()
            status = {
                "status": "ONLINE",
                "blog_id": BLOG_ID,
                "token_exists": os.path.exists(os.path.join(PROJECT_ROOT, "tools", "blogger_publisher", "blogger_token.json")),
                "indexing_service_account": os.path.exists(os.path.join(PROJECT_ROOT, "service_account.json")),
                "thumbnail_templates": [f for f in os.listdir(os.path.join(PROJECT_ROOT, "Thumbnail BG")) if f.endswith(".png")],
                "port": 8501
            }
            self.wfile.write(json.dumps(status).encode("utf-8"))
            return

        if url.path.startswith("/assets/images/"):
            # Serve local assets for thumbnail preview
            rel_path = url.path.lstrip("/")
            file_path = os.path.join(PROJECT_ROOT, rel_path)
            if os.path.exists(file_path):
                self.send_response(200)
                content_type = "image/webp" if file_path.endswith(".webp") else "image/png"
                self.send_header("Content-Type", content_type)
                self.end_headers()
                with open(file_path, "rb") as f:
                    self.wfile.write(f.read())
                return

        return super().do_GET()

    def do_POST(self):
        url = urllib.parse.urlparse(self.path)
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length) if content_length > 0 else b""

        # 1. Upload & Parse PDF
        if url.path == "/api/upload-pdf":
            try:
                # Handle raw bytes upload
                pdf_path = os.path.join(SCRATCH_DIR, f"upload_{int(time.time())}.pdf")
                with open(pdf_path, "wb") as f:
                    f.write(body)

                res = parse_pdf_text(pdf_path)
                self.send_response(200)
                self._set_cors()
                self.end_headers()
                self.wfile.write(json.dumps({
                    "success": True,
                    "pages": res.get("pages", 0),
                    "word_count": res.get("word_count", 0),
                    "char_count": res.get("char_count", 0),
                    "preview_snippet": res.get("text", "")[:1200]
                }).encode("utf-8"))
            except Exception as e:
                self.send_response(500)
                self._set_cors()
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": str(e)}).encode("utf-8"))
            return

        # 2. Generate Adaptive Silo Blueprint
        if url.path == "/api/generate-blueprint":
            try:
                data = json.loads(body.decode("utf-8"))
                title = data.get("title", "এসএসসি ও দাখিল প্রস্তুতি গাইড")
                category = data.get("category", "Education")
                raw_text = data.get("text", "")

                blueprint = generate_studio_blueprint(title, category, raw_text)
                self.send_response(200)
                self._set_cors()
                self.end_headers()
                self.wfile.write(json.dumps({"success": True, "blueprint": blueprint}).encode("utf-8"))
            except Exception as e:
                self.send_response(500)
                self._set_cors()
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": str(e)}).encode("utf-8"))
            return

        # 3. Generate Official 16:9 Thumbnail
        if url.path == "/api/render-thumbnail":
            try:
                data = json.loads(body.decode("utf-8"))
                title = data.get("title", "সাজেশন ও মানবণ্টন")
                subtitle = data.get("subtitle", "HelpTrickBD | helptrickbd.com")
                category = data.get("category", "EDUCATION")
                bg_image = data.get("bg_image", "bg_3.png")
                slug = data.get("slug", "post-thumb")

                output_path = os.path.join(PROJECT_ROOT, "assets", "images", "posts", f"{slug}.webp")
                success = render_official_thumbnail_card(title, subtitle, category, bg_image, output_path)

                web_url = f"/assets/images/posts/{slug}.webp"
                self.send_response(200)
                self._set_cors()
                self.end_headers()
                self.wfile.write(json.dumps({"success": success, "url": web_url}).encode("utf-8"))
            except Exception as e:
                self.send_response(500)
                self._set_cors()
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": str(e)}).encode("utf-8"))
            return

        # 4. Live Blogger Publish
        if url.path == "/api/publish-live":
            try:
                data = json.loads(body.decode("utf-8"))
                title = data.get("title")
                content = data.get("content")
                labels = data.get("labels", ["Education"])
                is_draft = data.get("is_draft", False)

                service = get_authenticated_service()
                if not service:
                    raise Exception("Blogger authentication failed.")

                body_payload = {
                    "title": title,
                    "content": content,
                    "labels": labels
                }

                # Direct publish via Blogger API
                new_post = service.posts().insert(
                    blogId=BLOG_ID,
                    body=body_payload,
                    isDraft=is_draft
                ).execute()

                post_url = new_post.get("url", "")
                post_id = new_post.get("id", "")

                # Ping Indexing if live
                if not is_draft and post_url:
                    try:
                        cmd = [sys.executable, os.path.join(PROJECT_ROOT, "tools", "indexer", "index_now.py"), "--url", post_url]
                        subprocess.run(cmd, capture_output=True, text=True, cwd=os.path.join(PROJECT_ROOT, "tools", "indexer"))
                        ping_all_hubs()
                    except Exception as e_idx:
                        print(f"[!] Indexing ping note: {e_idx}")

                self.send_response(200)
                self._set_cors()
                self.end_headers()
                self.wfile.write(json.dumps({
                    "success": True,
                    "post_id": post_id,
                    "url": post_url,
                    "is_draft": is_draft
                }).encode("utf-8"))
            except Exception as e:
                self.send_response(500)
                self._set_cors()
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": str(e)}).encode("utf-8"))
            return

        self.send_response(404)
        self.end_headers()

def run_server(port=8501):
    server_address = ("127.0.0.1", port)
    httpd = HTTPServer(server_address, StudioHandler)
    print("=" * 70)
    print(f"🚀 HELPTRICKBD AUTONOMOUS STUDIO BACKEND ONLINE: http://localhost:{port}")
    print("   Zero external dependencies. Press Ctrl+C to stop.")
    print("=" * 70)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[!] Studio server shutting down.")
        httpd.server_close()

if __name__ == "__main__":
    if "--test" in sys.argv:
        print("[✔] Server module syntax and imports verified.")
        sys.exit(0)
    port = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 8501
    run_server(port)
