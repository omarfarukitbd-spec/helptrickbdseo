#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/one_click_auth_and_publish.py
-----------------------------------------------------
Robust 1-Click Authenticator & Auto-Draft Publisher for HelpTrickBD.
1. Listens on http://localhost:8080
2. Captures Google OAuth callback and saves `blogger_token.json`
3. Automatically executes 2-step mint-and-revert draft publication
   for `nu-honours-2nd-year-exam-routine-2026.html`.
"""

import os
import sys
import json
import time
import wsgiref.simple_server
from google_auth_oauthlib.flow import InstalledAppFlow, _WSGIRequestHandler, _RedirectWSGIApp

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

SCOPES = ["https://www.googleapis.com/auth/blogger"]
CREDENTIALS_FILE = os.path.join(os.path.dirname(__file__), "client_secrets.json")
TOKEN_FILE = os.path.join(os.path.dirname(__file__), "blogger_token.json")
LINK_FILE = os.path.join(os.path.dirname(__file__), "login_link.txt")
HTML_PATH = os.path.join(PROJECT_ROOT, "output_posts", "nu-honours-2nd-year-exam-routine-2026.html")
META_PATH = os.path.join(PROJECT_ROOT, "output_posts", "nu-honours-2nd-year-exam-routine-2026_meta.json")


def main():
    print("=" * 72, flush=True)
    print("  HELPTRICKBD 1-CLICK AUTH & DRAFT PUBLISHER", flush=True)
    print("=" * 72, flush=True)

    flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
    wsgi_app = _RedirectWSGIApp("অভিনন্দন! গুগল অনুমোদন সম্পন্ন হয়েছে এবং পোস্টটি ব্লগারে ড্রাফট হিসেবে জমা হচ্ছে। আপনি এই ট্যাবটি বন্ধ করতে পারেন।")

    local_server = wsgiref.simple_server.make_server(
        "localhost", 8080, wsgi_app, handler_class=_WSGIRequestHandler
    )
    flow.redirect_uri = "http://localhost:8080/"

    auth_url, _ = flow.authorization_url(access_type="offline", prompt="consent")

    with open(LINK_FILE, "w", encoding="utf-8") as lf:
        lf.write(auth_url)

    print("\n" + "=" * 72, flush=True)
    print("  LINK GENERATED (Open in browser):", flush=True)
    print(auth_url, flush=True)
    print("=" * 72 + "\n", flush=True)
    print("[*] Server listening on http://localhost:8080/ ...", flush=True)

    while wsgi_app.last_request_uri is None:
        local_server.handle_request()

    authorization_response = wsgi_app.last_request_uri.replace("http:", "https:")
    flow.fetch_token(authorization_response=authorization_response)
    creds = flow.credentials

    with open(TOKEN_FILE, "w", encoding="utf-8") as token_file:
        token_file.write(creds.to_json())

    print("\n[OK] blogger_token.json সফলভাবে সেভ হয়েছে!", flush=True)

    # Now immediately publish draft
    print("\n[*] ব্লগারে ২-ধাপ পারমালিঙ্ক মিন্টিং ও ড্রাফট তৈরি শুরু হচ্ছে...", flush=True)
    from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID
    service = get_authenticated_service()

    with open(HTML_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    with open(META_PATH, "r", encoding="utf-8") as f:
        meta = json.load(f)

    slug = meta.get("english_slug", "nu-honours-2nd-year-exam-routine-2026")
    bengali_title = meta.get("title", "")
    labels = meta.get("labels", ["Education Guide", "Education"])

    print(f"[*] ধাপ ০১: ইংরেজি পারমালিঙ্ক মিন্ট করা হচ্ছে (slug: {slug})...", flush=True)
    mint_body = {
        "kind": "blogger#post",
        "blog": {"id": BLOG_ID},
        "title": slug,
        "content": content,
        "labels": labels
    }

    res_mint = service.posts().insert(blogId=BLOG_ID, body=mint_body, isDraft=False).execute()
    post_id = res_mint.get("id")
    live_url = res_mint.get("url")

    print(f"[OK] পারমালিঙ্ক তৈরি সফল! URL: {live_url}", flush=True)
    time.sleep(2)

    print(f"[*] ধাপ ০২: মূল বাংলা টাইটেল আপডেট ও ড্রাফটে রূপান্তর...", flush=True)
    update_body = {
        "title": bengali_title,
        "content": content,
        "labels": labels
    }
    service.posts().patch(blogId=BLOG_ID, postId=post_id, body=update_body).execute()
    time.sleep(1)

    service.posts().revert(blogId=BLOG_ID, postId=post_id).execute()
    print("\n" + "=" * 72, flush=True)
    print("  [SUCCESS] পোস্টটি ব্লগারে ড্রাফট হিসেবে সফলভাবে জমা হয়েছে!", flush=True)
    print(f"  Post ID: {post_id}", flush=True)
    print(f"  Permalink URL: {live_url}", flush=True)
    print("=" * 72 + "\n", flush=True)


if __name__ == "__main__":
    main()
    main()
