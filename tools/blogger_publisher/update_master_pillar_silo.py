#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/update_master_pillar_silo.py
Updates Master Pillar post (Post 01) on Blogger with the comprehensive Silo Cluster Navigation Hub.
"""

import os
import sys
import json

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID
from tools.governance.pre_flight_checker import PreFlightChecker
from tools.indexer.pubsub_hub_pinger import ping_all_hubs
from tools.indexer.index_now import get_authenticated_service as get_idx_credentials, submit_url
from googleapiclient.discovery import build

HTML_PATH = os.path.join(PROJECT_ROOT, "output_posts", "ssc-bangla-1st-paper-final-suggestion-2027.html")
META_PATH = os.path.join(PROJECT_ROOT, "output_posts", "ssc-bangla-1st-paper-final-suggestion-2027_metadata.json")
POST_ID = "6904395060145150353"

def update_pillar():
    print("=" * 75)
    print("UPDATING MASTER PILLAR (POST 01) WITH 8-POST SILO CLUSTER HUB")
    print("=" * 75)

    checker = PreFlightChecker(HTML_PATH, metadata_path=META_PATH)
    if not checker.run_all():
        checker.print_report()
        print("\n[BLOCKED] Pre-Flight check failed! Aborting update.")
        sys.exit(1)
    print("    [PASSED] Pre-Flight Quality Gate: 100% PASSED.")

    with open(HTML_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    service = get_authenticated_service()
    if not service:
        print("[ERROR] Failed to authenticate with Blogger API v3.")
        sys.exit(1)

    patch_body = {
        "content": content
    }

    print("\n[*] Patching Master Pillar post on Blogger...")
    updated = service.posts().patch(blogId=BLOG_ID, postId=POST_ID, body=patch_body).execute()
    print(f"    [OK] Post ID: {updated.get('id')}")
    print(f"    [OK] Live URL: {updated.get('url')}")
    print(f"    [OK] Title: {updated.get('title')}")

    # Ping Google Indexing API
    print("\n[*] Pinging Google Indexing API...")
    try:
        idx_creds = get_idx_credentials()
        if idx_creds:
            idx_service = build("indexing", "v3", credentials=idx_creds)
            submit_url(idx_service, updated.get("url"), "URL_UPDATED")
            print(f"    [OK] Googlebot notified to re-crawl: {updated.get('url')}")
    except Exception as e:
        print(f"    [NOTE] Indexing call notice: {e}")

    # Ping WebSub
    print("\n[*] Pinging WebSub Hubs...")
    try:
        ping_all_hubs()
    except Exception as e:
        print(f"    [WARNING] WebSub error: {e}")

    print("\n" + "=" * 75)
    print("MASTER PILLAR UPDATED & CROSS-LINKED SUCCESSFULLY!")
    print(f"   URL: {updated.get('url')}")
    print("=" * 75)

if __name__ == "__main__":
    update_pillar()
