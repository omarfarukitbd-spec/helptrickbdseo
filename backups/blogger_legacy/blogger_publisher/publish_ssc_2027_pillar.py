#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/publish_ssc_2027_pillar.py
--------------------------------------------------
Publishes the SSC 2027 English 1st Paper Pillar Hub Post to Blogger Live
following the mandatory 2-Step Custom English Permalink Minting Protocol:
Step 1: Insert post with English slug 'ssc-english-1st-paper-suggestion-2027' to mint clean permanent URL.
Step 2: Update title to full Bengali academic title:
        'এসএসসি ২০২৭ ইংরেজি ১ম পত্র চূড়ান্ত সাজেশন ও মানবণ্টন (১০০ নম্বর পূর্ণাঙ্গ প্রস্তুতি ও পিডিএফ)'.
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

HTML_PATH = os.path.join(PROJECT_ROOT, "scratch", "raw_posts", "ssc_2027_english_1st_paper_pillar.html")
META_PATH = os.path.join(PROJECT_ROOT, "scratch", "raw_posts", "ssc_2027_english_1st_paper_pillar.json")

def publish_pillar():
    print("=" * 75)
    print("🚀 HELPTRICKBD 2-STEP PUBLISHING ENGINE — SSC 2027 ENGLISH PILLAR")
    print("=" * 75)

    if not os.path.exists(HTML_PATH) or not os.path.exists(META_PATH):
        print(f"[ERROR] Required files not found: {HTML_PATH} or {META_PATH}")
        sys.exit(1)

    # 1. Pre-Flight Check Gate
    print("\n[*] Checking Pre-Flight Quality Gate...")
    checker = PreFlightChecker(HTML_PATH, metadata_path=META_PATH)
    if not checker.run_all():
        checker.print_report()
        print("\n[BLOCKED] Pre-Flight check failed! Aborting publication.")
        sys.exit(1)
    print("    [✔] Pre-Flight Quality Gate: 100% PASSED (0 Errors).")

    with open(META_PATH, "r", encoding="utf-8") as f:
        meta = json.load(f)
    with open(HTML_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    slug = meta["slug"]
    bengali_title = meta["title"]
    labels = meta["labels"]

    print(f"\n[*] Target Post Details:")
    print(f"    Slug:    {slug}")
    print(f"    Title:   {bengali_title}")
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

    print("\n[*] Step 1: Minting clean English permalink on Blogger...")
    result = service.posts().insert(blogId=BLOG_ID, body=body, isDraft=False).execute()
    post_id = result.get("id")
    initial_url = result.get("url")
    print(f"    [✔] Post Minted Successfully! Post ID: {post_id}")
    print(f"        Initial Minted URL: {initial_url}")

    time.sleep(2)

    # 4. STEP 2: Update title to full Bengali title
    print("\n[*] Step 2: Updating post title to full Bengali academic title...")
    patch_body = {
        "title": bengali_title
    }
    updated_result = service.posts().patch(blogId=BLOG_ID, postId=post_id, body=patch_body).execute()
    final_title = updated_result.get("title")
    final_url = updated_result.get("url")
    print(f"    [✔] Bengali Title Applied: {final_title}")
    print(f"    [✔] Final Live URL:        {final_url}")

    # 5. STEP 3: Submit to Google Indexing API
    print("\n[*] Step 3: Submitting live URL to Google Indexing API...")
    try:
        indexer_cmd = [
            sys.executable,
            os.path.join(PROJECT_ROOT, "tools", "indexer", "index_now.py"),
            "--url", final_url
        ]
        idx_res = subprocess.run(indexer_cmd, capture_output=True, text=True, cwd=os.path.join(PROJECT_ROOT, "tools", "indexer"))
        print(f"    [✔] Google Indexing Response: {idx_res.stdout.strip()}")
    except Exception as e_idx:
        print(f"    [!] Warning: Google Indexing submission failed: {e_idx}")

    # 6. STEP 4: Ping WebSub / PubSubHubbub Hubs
    print("\n[*] Step 4: Real-Time WebSub (PubSubHubbub) Hub Ping...")
    try:
        ping_all_hubs()
    except Exception as e_hub:
        print(f"    [!] Warning: WebSub hub ping failed: {e_hub}")

    # 7. Record Post Snapshot & Backup
    published_record = {
        "post_id": post_id,
        "title": final_title,
        "slug": slug,
        "url": final_url,
        "labels": labels,
        "search_description": meta.get("search_description", ""),
        "published_at": updated_result.get("published"),
        "updated_at": updated_result.get("updated")
    }

    record_path = os.path.join(PROJECT_ROOT, "output_posts", f"{slug}_published.json")
    os.makedirs(os.path.dirname(record_path), exist_ok=True)
    with open(record_path, "w", encoding="utf-8") as f:
        json.dump(published_record, f, ensure_ascii=False, indent=2)

    backup_dir = os.path.join(PROJECT_ROOT, "backups", "posts", slug, str(int(time.time())))
    os.makedirs(backup_dir, exist_ok=True)
    with open(os.path.join(backup_dir, "post.html"), "w", encoding="utf-8") as f:
        f.write(content)
    with open(os.path.join(backup_dir, "metadata.json"), "w", encoding="utf-8") as f:
        json.dump(published_record, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 75)
    print("🎉 SSC 2027 ENGLISH 1ST PAPER PILLAR HUB POST PUBLISHED SUCCESSFULLY!")
    print(f"   Live URL: {final_url}")
    print(f"   Post ID:  {post_id}")
    print(f"   Record:   {record_path}")
    print("=" * 75)

    return published_record

if __name__ == "__main__":
    publish_pillar()
