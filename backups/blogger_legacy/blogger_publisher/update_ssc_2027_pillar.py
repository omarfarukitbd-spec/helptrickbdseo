#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/update_ssc_2027_pillar.py
--------------------------------------------------
Updates the live SSC 2027 English 1st Paper Pillar post on Blogger (Post ID: 5652005814898036993)
with the new, responsive, academic design matching the golden reference:
secularism-vs-islamic-values-in.html
"""

import os
import sys
import json
import time

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID
from tools.governance.pre_flight_checker import PreFlightChecker
from tools.indexer.pubsub_hub_pinger import ping_all_hubs
from tools.backup_manager.post_backup_manager import create_post_backup

POST_ID = "5652005814898036993"
HTML_PATH = os.path.join(PROJECT_ROOT, "scratch", "raw_posts", "ssc_2027_english_1st_paper_pillar.html")
META_PATH = os.path.join(PROJECT_ROOT, "scratch", "raw_posts", "ssc_2027_english_1st_paper_pillar.json")

def update_live_post():
    print("=" * 75)
    print("🚀 HELPTRICKBD LIVE POST REDESIGN & UPDATE ENGINE")
    print("=" * 75)

    if not os.path.exists(HTML_PATH) or not os.path.exists(META_PATH):
        print(f"[ERROR] Files not found: {HTML_PATH} or {META_PATH}")
        sys.exit(1)

    # 1. Pre-Flight Check
    print("\n[*] Running Pre-Flight Quality Gatekeeper...")
    checker = PreFlightChecker(HTML_PATH, metadata_path=META_PATH)
    if not checker.run_all():
        checker.print_report()
        print("\n[BLOCKED] Pre-Flight Gatekeeper failed. Aborting update.")
        sys.exit(1)
    print("    [✔] Pre-Flight Check: PASSED (0 Errors).")

    with open(META_PATH, "r", encoding="utf-8") as f:
        meta = json.load(f)
    with open(HTML_PATH, "r", encoding="utf-8") as f:
        new_content = f.read()

    # 2. Authenticate
    service = get_authenticated_service()
    if not service:
        print("[ERROR] Could not authenticate with Blogger API v3.")
        sys.exit(1)

    # 3. Retrieve live post & create backup (Rule 07 & 15)
    print(f"\n[*] Fetching live post (Post ID: {POST_ID}) for safety backup...")
    live_post = service.posts().get(blogId=BLOG_ID, postId=POST_ID).execute()
    try:
        backup_res = create_post_backup(live_post, reason="pre_redesign_backup")
        print(f"    [✔] Pre-edit backup secured: {backup_res.get('backup_dir')}")
    except Exception as e_bak:
        print(f"    [!] Warning: Backup manager note: {e_bak}")

    # 4. Patch Post with New Content & Preserved Title/Labels
    print("\n[*] Updating post with responsive, premium academic styling...")
    patch_body = {
        "title": meta["title"],
        "content": new_content,
        "labels": meta["labels"]
    }

    updated_post = service.posts().patch(blogId=BLOG_ID, postId=POST_ID, body=patch_body).execute()
    final_url = updated_post.get("url")
    print(f"    [✔] Post Updated Successfully!")
    print(f"        Title:    {updated_post.get('title')}")
    print(f"        Live URL: {final_url}")
    print(f"        Updated:  {updated_post.get('updated')}")

    # 5. Ping Google Indexing API
    print("\n[*] Pinging Google Indexing API...")
    try:
        import subprocess
        indexer_cmd = [
            sys.executable,
            os.path.join(PROJECT_ROOT, "tools", "indexer", "index_now.py"),
            "--url", final_url
        ]
        idx_res = subprocess.run(indexer_cmd, capture_output=True, text=True, cwd=os.path.join(PROJECT_ROOT, "tools", "indexer"))
        print(f"    [✔] Indexing API: {idx_res.stdout.strip()}")
    except Exception as e_idx:
        print(f"    [!] Indexing Ping note: {e_idx}")

    # 6. Ping WebSub Hubs
    print("\n[*] Pinging WebSub Hubs...")
    try:
        ping_all_hubs()
    except Exception as e_hub:
        print(f"    [!] WebSub Hub ping note: {e_hub}")

    # 7. Update published snapshot
    snapshot_path = os.path.join(PROJECT_ROOT, "output_posts", f"{meta['slug']}_published.json")
    snapshot_data = {
        "post_id": POST_ID,
        "title": updated_post.get("title"),
        "slug": meta["slug"],
        "url": final_url,
        "labels": meta["labels"],
        "search_description": meta.get("search_description", ""),
        "updated_at": updated_post.get("updated")
    }
    with open(snapshot_path, "w", encoding="utf-8") as f:
        json.dump(snapshot_data, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 75)
    print("🎉 SSC 2027 PILLAR POST REDESIGNED & UPDATED LIVE SUCCESSFULLY!")
    print(f"   URL: {final_url}")
    print("=" * 75)

if __name__ == "__main__":
    update_live_post()
