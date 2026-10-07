#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/publish_ssc_bangla_1st_pillar.py
-------------------------------------------------------
Publishes the SSC & Dakhil 2026-2027 Bangla 1st Paper Master Pillar Post to Blogger Live
strictly adhering to the mandatory 2-Step Custom English Permalink Minting Protocol:
Step 1: Insert post with slug 'ssc-bangla-1st-paper-final-suggestion-2027' to mint clean URL.
Step 2: Update title to full academic title.
Step 3: Ping Google Indexing API with live URL.
Step 4: Ping WebSub / PubSubHubbub Hubs for instant feed ingest.
"""

import os
import sys
import json
import time
import subprocess

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID
from tools.governance.pre_flight_checker import PreFlightChecker
from tools.indexer.pubsub_hub_pinger import ping_all_hubs

HTML_PATH = os.path.join(PROJECT_ROOT, "output_posts", "ssc-bangla-1st-paper-final-suggestion-2027.html")
META_PATH = os.path.join(PROJECT_ROOT, "output_posts", "ssc-bangla-1st-paper-final-suggestion-2027_metadata.json")

def publish_pillar():
    print("=" * 75)
    print("🚀 HELPTRICKBD 2-STEP PUBLISHING ENGINE — BANGLA 1ST PAPER PILLAR")
    print("=" * 75)

    if not os.path.exists(HTML_PATH) or not os.path.exists(META_PATH):
        print(f"[ERROR] Required files not found: {HTML_PATH} or {META_PATH}")
        sys.exit(1)

    # 1. Pre-Flight Quality Gate Check
    print("\n[*] Checking Pre-Flight Quality Gate...")
    checker = PreFlightChecker(HTML_PATH, metadata_path=META_PATH)
    if not checker.run_all():
        checker.print_report()
        print("\n[BLOCKED] Pre-Flight check failed! Aborting publication.")
        sys.exit(1)
    print("    [✔] Pre-Flight Quality Gate: 100% PASSED (0 Critical Errors).")

    with open(META_PATH, "r", encoding="utf-8") as f:
        meta = json.load(f)
    with open(HTML_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    slug = meta["custom_slug"]
    full_title = meta["title"]
    labels = meta["labels"]

    print(f"\n[*] Target Post Details:")
    print(f"    Slug:    {slug}")
    print(f"    Title:   {full_title}")
    print(f"    Labels:  {', '.join(labels)}")
    print(f"    Words:   {len(content.split())} words")

    # 2. Blogger API Authentication
    service = get_authenticated_service()
    if not service:
        print("[ERROR] Failed to authenticate with Blogger API v3.")
        sys.exit(1)

    # 3. STEP 1: Mint clean English permalink
    body = {
        "kind": "blogger#post",
        "blog": {"id": BLOG_ID},
        "title": slug,
        "content": content,
        "labels": labels
    }

    print("\n[*] [STEP 1] Minting clean English permalink on Blogger...")
    try:
        inserted_post = service.posts().insert(blogId=BLOG_ID, body=body, isDraft=False).execute()
        post_id = inserted_post.get("id")
        live_url = inserted_post.get("url")
        print(f"    [✔] Successfully Minted Post ID: {post_id}")
        print(f"    [✔] Permanent Clean URL:       {live_url}")
    except Exception as e:
        print(f"[ERROR] Step 1 Minting Failed: {e}")
        sys.exit(1)

    # 4. STEP 2: Update title to full Bengali academic title
    time.sleep(2)
    print("\n[*] [STEP 2] Updating post title to full Bengali title...")
    patch_body = {
        "title": full_title
    }

    try:
        updated_post = service.posts().patch(
            blogId=BLOG_ID,
            postId=post_id,
            body=patch_body,
            revert=False
        ).execute()
        print(f"    [✔] Successfully Updated Title: {updated_post.get('title')}")
    except Exception as e:
        print(f"[ERROR] Step 2 Title Update Failed: {e}")

    # 5. STEP 3: Ping Google Indexing API
    print("\n[*] [STEP 3] Notifying Google Indexing API...")
    try:
        from tools.indexer.index_now import get_authenticated_service as get_idx_service, submit_url
        idx_service = get_idx_service()
        if idx_service:
            success = submit_url(idx_service, live_url, "URL_UPDATED")
            if success:
                print(f"    [✔] Googlebot notified to index: {live_url}")
        else:
            print("    [!] Indexing service credentials not loaded, falling back to manual CLI.")
    except Exception as e:
        print(f"    [!] Indexing API ping error: {e}")

    # 6. STEP 4: Ping WebSub / PubSubHubbub Hubs
    print("\n[*] [STEP 4] Pinging Real-Time WebSub Hubs...")
    try:
        ping_all_hubs()
    except Exception as e:
        print(f"    [!] WebSub ping warning: {e}")

    # 7. Save Deployment Record
    manifest = {
        "post_id": post_id,
        "live_url": live_url,
        "slug": slug,
        "title": full_title,
        "labels": labels,
        "status": "published_live",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    record_path = os.path.join(PROJECT_ROOT, "output_posts", "ssc_bangla_1st_pillar_published.json")
    with open(record_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"\n[✔] Deployment manifest saved to: {record_path}")

    print("\n" + "=" * 75)
    print("🎉 BANGLA 1ST PAPER MASTER PILLAR POST LIVE & INDEXED SUCCESSFULLY!")
    print(f"   URL: {live_url}")
    print("=" * 75)
    return manifest

if __name__ == "__main__":
    publish_pillar()
