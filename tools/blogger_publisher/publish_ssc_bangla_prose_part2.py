#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/publish_ssc_bangla_prose_part2.py
Publishes Prose Part 2 to Blogger Live with 2-Step Custom Permalink Minting.
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
from tools.indexer.index_now import get_authenticated_service as get_idx_service, submit_url

HTML_PATH = os.path.join(PROJECT_ROOT, "output_posts", "ssc-bangla-1st-paper-prose-cq-part-2.html")
META_PATH = os.path.join(PROJECT_ROOT, "output_posts", "ssc-bangla-1st-paper-prose-cq-part-2_metadata.json")

def publish_prose_part2():
    print("=" * 75)
    print("HEL訊TRICKBD 2-STEP PUBLISHING ENGINE — BANGLA 1ST PROSE CQ PART 2")
    print("=" * 75)

    checker = PreFlightChecker(HTML_PATH, metadata_path=META_PATH)
    if not checker.run_all():
        checker.print_report()
        print("\n[BLOCKED] Pre-Flight check failed! Aborting publication.")
        sys.exit(1)
    print("    [PASSED] Pre-Flight Quality Gate: 100% PASSED.")

    with open(META_PATH, "r", encoding="utf-8") as f:
        meta = json.load(f)
    with open(HTML_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    slug = meta["custom_slug"]
    full_title = meta["title"]
    labels = meta["labels"]

    service = get_authenticated_service()
    if not service:
        print("[ERROR] Failed to authenticate with Blogger API v3.")
        sys.exit(1)

    # 1. Step 1: Mint slug
    body = {
        "kind": "blogger#post",
        "blog": {"id": BLOG_ID},
        "title": slug,
        "content": content,
        "labels": labels
    }

    print("\n[*] [STEP 1] Minting clean English permalink on Blogger...")
    try:
        inserted = service.posts().insert(blogId=BLOG_ID, body=body, isDraft=False).execute()
        post_id = inserted.get("id")
        live_url = inserted.get("url")
        print(f"    [OK] Post ID: {post_id}")
        print(f"    [OK] Clean URL: {live_url}")
    except Exception as e:
        print(f"[ERROR] Step 1 failed: {e}")
        sys.exit(1)

    # 2. Step 2: Update title
    time.sleep(2)
    print("\n[*] [STEP 2] Updating post title to full Bengali title...")
    try:
        updated = service.posts().patch(
            blogId=BLOG_ID,
            postId=post_id,
            body={"title": full_title},
            revert=False
        ).execute()
        print(f"    [OK] Updated Title: {updated.get('title')}")
    except Exception as e:
        print(f"[ERROR] Step 2 failed: {e}")

    # 3. Step 3: Ping Google Indexing API
    print("\n[*] [STEP 3] Pinging Google Indexing API...")
    try:
        idx_service = get_idx_service()
        if idx_service:
            submit_url(idx_service, live_url, "URL_UPDATED")
            print(f"    [OK] Googlebot notified to index: {live_url}")
    except Exception as e:
        print(f"    [!] Indexing API ping warning: {e}")

    # 4. Step 4: WebSub pinger
    print("\n[*] [STEP 4] Pinging WebSub Hubs...")
    try:
        ping_all_hubs()
    except Exception as e:
        print(f"    [!] WebSub ping warning: {e}")

    # 5. Manifest record
    manifest = {
        "post_id": post_id,
        "live_url": live_url,
        "slug": slug,
        "title": full_title,
        "labels": labels,
        "status": "published_live",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    rec_path = os.path.join(PROJECT_ROOT, "output_posts", "ssc_bangla_prose_part2_published.json")
    with open(rec_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print(f"\n[OK] Manifest saved to: {rec_path}")

    print("\n" + "=" * 75)
    print("BANGLA 1ST PROSE PART 2 POST LIVE SUCCESSFULLY!")
    print(f"   URL: {live_url}")
    print("=" * 75)
    return manifest

if __name__ == "__main__":
    publish_prose_part2()
