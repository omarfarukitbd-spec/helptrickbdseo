#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/publish_ssc_bangla_prose_part3.py
Publishes Prose Part 3 to Blogger Live with 2-Step Custom Permalink Minting.
"""

import os
import sys
import json
import time

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

HTML_PATH = os.path.join(PROJECT_ROOT, "output_posts", "ssc-bangla-1st-paper-prose-cq-part-3.html")
META_PATH = os.path.join(PROJECT_ROOT, "output_posts", "ssc-bangla-1st-paper-prose-cq-part-3_metadata.json")

def publish_prose_part3():
    print("=" * 75)
    print("HELPTRICKBD 2-STEP PUBLISHING ENGINE — BANGLA 1ST PROSE CQ PART 3")
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

    slug = meta.get("custom_slug", meta.get("slug"))
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
    created = service.posts().insert(blogId=BLOG_ID, body=body, isDraft=False).execute()
    post_id = created.get("id")
    clean_url = created.get("url")
    print(f"    [OK] Post ID: {post_id}")
    print(f"    [OK] Clean URL: {clean_url}")

    # Brief delay to allow Blogger DB permalink finalization
    time.sleep(2)

    # 2. Step 2: Update to full Bengali title
    print("\n[*] [STEP 2] Updating post title to full Bengali title...")
    update_body = {
        "title": full_title
    }
    updated = service.posts().patch(blogId=BLOG_ID, postId=post_id, body=update_body).execute()
    print(f"    [OK] Updated Title: {updated.get('title')}")

    # 3. Step 3: Google Indexing API
    print("\n[*] [STEP 3] Pinging Google Indexing API...")
    try:
        idx_creds = get_idx_credentials()
        if idx_creds:
            idx_service = build("indexing", "v3", credentials=idx_creds)
            submit_url(idx_service, clean_url, "URL_UPDATED")
            print(f"    [OK] Googlebot notified to index: {clean_url}")
    except Exception as e:
        print(f"    [NOTE] Indexing call notice: {e}")

    # 4. Step 4: WebSub Hub Pinging
    print("\n[*] [STEP 4] Pinging WebSub Hubs...")
    try:
        ping_all_hubs()
    except Exception as e:
        print(f"    [WARNING] WebSub ping encountered error: {e}")

    # Save manifest
    manifest_path = os.path.join(PROJECT_ROOT, "output_posts", "ssc_bangla_prose_part3_published.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump({
            "post_id": post_id,
            "url": clean_url,
            "title": full_title,
            "slug": slug,
            "labels": labels,
            "published_at": updated.get("published"),
            "updated_at": updated.get("updated")
        }, f, ensure_ascii=False, indent=2)
    print(f"\n[OK] Manifest saved to: {manifest_path}")

    print("\n" + "=" * 75)
    print(f"BANGLA 1ST PROSE PART 3 POST LIVE SUCCESSFULLY!")
    print(f"   URL: {clean_url}")
    print("=" * 75)

if __name__ == "__main__":
    publish_prose_part3()
