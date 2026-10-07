#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/update_post_live.py
Updates a live post on Blogger with new HTML content, title, and labels,
then pings Google Indexing API and WebSub Hubs.
"""

import os
import sys
import json
import argparse

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID
from tools.governance.pre_flight_checker import PreFlightChecker
from tools.indexer.pubsub_hub_pinger import ping_all_hubs
from tools.indexer.index_now import get_authenticated_service as get_idx_service, submit_url

def update_live_post(html_path, meta_path):
    print("=" * 70)
    print("🔄 HELPTRICKBD LIVE POST UPDATE & SYNC ENGINE")
    print("=" * 70)

    # 1. Pre-flight check
    checker = PreFlightChecker(html_path, metadata_path=meta_path)
    if not checker.run_all():
        checker.print_report()
        print("\n[BLOCKED] Pre-Flight check failed! Aborting update.")
        sys.exit(1)
    print("    [✔] Pre-Flight Quality Gate: 100% PASSED.")

    with open(meta_path, "r", encoding="utf-8") as f:
        meta = json.load(f)
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    post_id = meta.get("post_id")
    title = meta.get("title")
    labels = meta.get("labels")
    live_url = meta.get("live_url")

    print(f"[*] Updating Post ID: {post_id}")
    print(f"    Title:    {title}")
    print(f"    Live URL: {live_url}")
    print(f"    Words:    {len(content.split())} words")

    service = get_authenticated_service()
    if not service:
        print("[ERROR] Failed to authenticate Blogger API.")
        sys.exit(1)

    patch_body = {
        "title": title,
        "content": content,
        "labels": labels
    }

    try:
        updated = service.posts().patch(
            blogId=BLOG_ID,
            postId=post_id,
            body=patch_body,
            revert=False
        ).execute()
        print(f"\n[✔] Successfully updated live post on Blogger! ID: {updated.get('id')}")
    except Exception as e:
        print(f"[ERROR] Update failed: {e}")
        sys.exit(1)

    # 2. Ping Google Indexing API
    print("\n[*] Pinging Google Indexing API...")
    try:
        idx_service = get_idx_service()
        if idx_service and live_url:
            submit_url(idx_service, live_url, "URL_UPDATED")
            print(f"    [✔] Google Indexing API notified: {live_url}")
    except Exception as e:
        print(f"    [!] Indexing API ping warning: {e}")

    # 3. Ping WebSub
    print("\n[*] Pinging WebSub Hubs...")
    try:
        ping_all_hubs()
    except Exception as e:
        print(f"    [!] WebSub ping warning: {e}")

    print("\n" + "=" * 70)
    print(f"🎉 POST {post_id} UPDATED & SYNCED LIVE SUCCESSFULLY!")
    print(f"   URL: {live_url}")
    print("=" * 70)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("html", help="Path to HTML file")
    parser.add_argument("meta", help="Path to JSON metadata file")
    args = parser.parse_args()

    update_live_post(args.html, args.meta)
