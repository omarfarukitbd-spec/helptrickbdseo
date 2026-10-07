#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/publish_ssc_2027_silo_series.py
--------------------------------------------------------
Publishes all 5 SSC 2027 English 1st Paper Silo Series posts to Blogger Live.
Follows the mandatory 2-Step Custom English Permalink Minting Protocol.

Silo Posts:
  Part 01: ssc-2027-english-seen-passage-suggestion
  Part 02: ssc-2027-english-unseen-passage-summary-writing
  Part 03: ssc-2027-english-matching-rearrange-rules-solution
  Part 04: ssc-2027-english-poems-stories-question-answer-guide
  Part 05: ssc-2027-english-completing-story-dialogue-suggestion
"""

import os
import sys
import json
import time
import subprocess

# Set stdout/stderr encoding for Windows without wrapping (avoids closed file errors)
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

RAW_POSTS_DIR = os.path.join(PROJECT_ROOT, "scratch", "raw_posts")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output_posts")
os.makedirs(OUTPUT_DIR, exist_ok=True)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID
from tools.governance.pre_flight_checker import PreFlightChecker
from tools.indexer.pubsub_hub_pinger import ping_all_hubs

SILO_POSTS = [
    ("ssc_2027_silo_01_seen_passage", "Part 01: Seen Passage"),
    ("ssc_2027_silo_02_unseen_summary", "Part 02: Unseen Passage & Summary"),
    ("ssc_2027_silo_03_matching_rearrange", "Part 03: Matching & Re-arranging"),
    ("ssc_2027_silo_04_poems_stories", "Part 04: Poems & Stories"),
    ("ssc_2027_silo_05_story_dialogue", "Part 05: Completing Story & Dialogue"),
]


def publish_single_post(service, html_path, meta_path, label):
    """Publishes a single silo post using the 2-Step Permalink Protocol."""
    print(f"\n{'─' * 65}")
    print(f"  Publishing: {label}")
    print(f"{'─' * 65}")

    if not os.path.exists(html_path):
        print(f"  [ERROR] HTML file not found: {html_path}")
        return None
    if not os.path.exists(meta_path):
        print(f"  [ERROR] Meta file not found: {meta_path}")
        return None

    # 1. Pre-Flight Quality Gate
    print("  [*] Running Pre-Flight Quality Gate...")
    checker = PreFlightChecker(html_path, metadata_path=meta_path)
    if not checker.run_all():
        checker.print_report()
        print("  [BLOCKED] Pre-Flight failed! Skipping this post.")
        return None
    print("  [OK] Pre-Flight: PASSED")

    with open(meta_path, "r", encoding="utf-8") as f:
        meta = json.load(f)
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    slug = meta["slug"]
    bengali_title = meta["title"]
    labels = meta["labels"]

    print(f"  [*] Slug:   {slug}")
    print(f"  [*] Words:  {len(content.split())}")

    # 2. STEP 1: Mint clean English permalink (publish with slug as title)
    body = {
        "kind": "blogger#post",
        "blog": {"id": BLOG_ID},
        "title": slug,
        "content": content,
        "labels": labels
    }
    print("  [*] Step 1: Minting English permalink...")
    result = service.posts().insert(blogId=BLOG_ID, body=body, isDraft=False).execute()
    post_id = result.get("id")
    initial_url = result.get("url")
    print(f"  [OK] Minted! Post ID: {post_id}")
    print(f"       URL: {initial_url}")

    time.sleep(3)

    # 3. STEP 2: Update to full Bengali title
    print("  [*] Step 2: Updating to Bengali title...")
    patch_body = {"title": bengali_title}
    updated = service.posts().patch(blogId=BLOG_ID, postId=post_id, body=patch_body).execute()
    final_url = updated.get("url")
    print(f"  [OK] Title updated: {updated.get('title')[:60]}...")
    print(f"       Final URL: {final_url}")

    # 4. Ping Google Indexing API
    print("  [*] Step 3: Google Indexing API ping...")
    try:
        idx_cmd = [
            sys.executable,
            os.path.join(PROJECT_ROOT, "tools", "indexer", "index_now.py"),
            "--url", final_url
        ]
        idx_res = subprocess.run(idx_cmd, capture_output=True, text=True,
                                 cwd=os.path.join(PROJECT_ROOT, "tools", "indexer"))
        print(f"  [OK] Indexing: {idx_res.stdout.strip()[:80]}")
    except Exception as e:
        print(f"  [!] Indexing note: {e}")

    # 5. Record published snapshot
    record = {
        "post_id": post_id,
        "title": updated.get("title"),
        "slug": slug,
        "url": final_url,
        "labels": labels,
        "search_description": meta.get("search_description", ""),
        "published_at": updated.get("published"),
        "updated_at": updated.get("updated")
    }
    record_path = os.path.join(OUTPUT_DIR, f"{slug}_published.json")
    with open(record_path, "w", encoding="utf-8") as f:
        json.dump(record, f, ensure_ascii=False, indent=2)

    # 6. Backup
    backup_dir = os.path.join(PROJECT_ROOT, "backups", "posts", slug, str(int(time.time())))
    os.makedirs(backup_dir, exist_ok=True)
    with open(os.path.join(backup_dir, "post.html"), "w", encoding="utf-8") as f:
        f.write(content)
    with open(os.path.join(backup_dir, "metadata.json"), "w", encoding="utf-8") as f:
        json.dump(record, f, ensure_ascii=False, indent=2)

    print(f"  [OK] Backup: {backup_dir}")
    return record


def main():
    print("=" * 70)
    print("SSC 2027 ENGLISH SILO SERIES — 2-STEP PUBLISHER")
    print("=" * 70)

    # Authenticate once
    print("\n[*] Authenticating with Blogger API v3...")
    service = get_authenticated_service()
    if not service:
        print("[ERROR] Authentication failed!")
        sys.exit(1)
    print("[OK] Authenticated successfully!\n")

    published_posts = []
    failed_posts = []

    for file_prefix, label in SILO_POSTS:
        html_path = os.path.join(RAW_POSTS_DIR, f"{file_prefix}.html")
        meta_path = os.path.join(RAW_POSTS_DIR, f"{file_prefix}.json")

        record = publish_single_post(service, html_path, meta_path, label)
        if record:
            published_posts.append(record)
            print(f"  [DONE] {label} published successfully!")
        else:
            failed_posts.append(label)
            print(f"  [FAIL] {label} could not be published.")

        # Delay between posts to avoid rate limiting
        if file_prefix != SILO_POSTS[-1][0]:
            print("\n  [*] Waiting 5 seconds before next post...")
            time.sleep(5)

    # Final WebSub ping
    print("\n[*] WebSub Hub Ping (all hubs)...")
    try:
        ping_all_hubs()
        print("[OK] WebSub hubs pinged.")
    except Exception as e:
        print(f"[!] WebSub note: {e}")

    # Summary Report
    print("\n" + "=" * 70)
    print("PUBLICATION SUMMARY")
    print("=" * 70)
    print(f"  Published: {len(published_posts)} / {len(SILO_POSTS)} posts")
    for rec in published_posts:
        print(f"  [OK]  {rec['slug']}")
        print(f"        {rec['url']}")
    if failed_posts:
        print(f"\n  Failed: {len(failed_posts)} posts")
        for f in failed_posts:
            print(f"  [FAIL] {f}")
    print("=" * 70)

    return published_posts


if __name__ == "__main__":
    main()
