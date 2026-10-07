#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/republish_ssc_silo_02_03_04.py
-------------------------------------------------------
Re-publishes only the 3 failed silo posts (02, 03, 04) after enrichment.
"""

import os, sys, json, time, subprocess

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

FAILED_POSTS = [
    ("ssc_2027_silo_02_unseen_summary", "Part 02: Unseen Passage & Summary"),
    ("ssc_2027_silo_03_matching_rearrange", "Part 03: Matching & Re-arranging"),
    ("ssc_2027_silo_04_poems_stories", "Part 04: Poems & Stories"),
]


def publish_post(service, html_path, meta_path, label):
    print(f"\n{'─' * 60}")
    print(f"  {label}")
    print(f"{'─' * 60}")

    print("  [*] Pre-Flight Check...")
    checker = PreFlightChecker(html_path, metadata_path=meta_path)
    if not checker.run_all():
        checker.print_report()
        print("  [BLOCKED] Pre-Flight failed.")
        return None
    print("  [OK] Pre-Flight: PASSED")

    with open(meta_path, 'r', encoding='utf-8') as f:
        meta = json.load(f)
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    slug = meta["slug"]
    bengali_title = meta["title"]
    labels = meta["labels"]

    # Step 1: Mint permalink with slug as title
    body = {"kind": "blogger#post", "blog": {"id": BLOG_ID},
            "title": slug, "content": content, "labels": labels}
    print(f"  [*] Step 1: Minting — {slug}")
    result = service.posts().insert(blogId=BLOG_ID, body=body, isDraft=False).execute()
    post_id = result.get("id")
    initial_url = result.get("url")
    print(f"  [OK] Post ID: {post_id}")
    print(f"       URL:     {initial_url}")
    time.sleep(3)

    # Step 2: Update to Bengali title
    print("  [*] Step 2: Applying Bengali title...")
    updated = service.posts().patch(blogId=BLOG_ID, postId=post_id,
                                    body={"title": bengali_title}).execute()
    final_url = updated.get("url")
    print(f"  [OK] Final URL: {final_url}")

    # Step 3: Indexing API
    try:
        idx_cmd = [sys.executable, os.path.join(PROJECT_ROOT, "tools", "indexer", "index_now.py"), "--url", final_url]
        idx_res = subprocess.run(idx_cmd, capture_output=True, text=True, cwd=os.path.join(PROJECT_ROOT, "tools", "indexer"))
        print(f"  [OK] Indexed: {idx_res.stdout.strip()[:60]}")
    except Exception as e:
        print(f"  [!] Index note: {e}")

    # Backup
    record = {"post_id": post_id, "title": updated.get("title"), "slug": slug,
              "url": final_url, "labels": labels,
              "search_description": meta.get("search_description", ""),
              "published_at": updated.get("published")}
    backup_dir = os.path.join(PROJECT_ROOT, "backups", "posts", slug, str(int(time.time())))
    os.makedirs(backup_dir, exist_ok=True)
    with open(os.path.join(backup_dir, "post.html"), 'w', encoding='utf-8') as f:
        f.write(content)
    with open(os.path.join(backup_dir, "metadata.json"), 'w', encoding='utf-8') as f:
        json.dump(record, f, ensure_ascii=False, indent=2)
    with open(os.path.join(OUTPUT_DIR, f"{slug}_published.json"), 'w', encoding='utf-8') as f:
        json.dump(record, f, ensure_ascii=False, indent=2)

    print(f"  [DONE] Published successfully!")
    return record


def main():
    print("=" * 65)
    print("SSC 2027 SILO SERIES — RE-PUBLISH FAILED POSTS (02, 03, 04)")
    print("=" * 65)

    service = get_authenticated_service()
    if not service:
        print("[ERROR] Auth failed!")
        sys.exit(1)
    print("[OK] Authenticated.\n")

    published = []
    failed = []

    for file_prefix, label in FAILED_POSTS:
        html_path = os.path.join(RAW_POSTS_DIR, f"{file_prefix}.html")
        meta_path = os.path.join(RAW_POSTS_DIR, f"{file_prefix}.json")
        record = publish_post(service, html_path, meta_path, label)
        if record:
            published.append(record)
        else:
            failed.append(label)
        if file_prefix != FAILED_POSTS[-1][0]:
            print("\n  [*] Waiting 5s...")
            time.sleep(5)

    # Final WebSub ping
    print("\n[*] WebSub Hub Ping...")
    try:
        ping_all_hubs()
        print("[OK] Hubs pinged.")
    except Exception as e:
        print(f"[!] WebSub note: {e}")

    print("\n" + "=" * 65)
    print(f"RESULT: {len(published)}/{len(FAILED_POSTS)} posts published")
    for rec in published:
        print(f"  [OK]  {rec['slug']}")
        print(f"        {rec['url']}")
    for f in failed:
        print(f"  [FAIL] {f}")
    print("=" * 65)


if __name__ == "__main__":
    main()
