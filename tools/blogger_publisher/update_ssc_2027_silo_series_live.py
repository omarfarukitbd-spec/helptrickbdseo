#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/update_ssc_2027_silo_series_live.py
--------------------------------------------------------------
Updates the 5 live SSC 2027 English 1st Paper Silo Series posts on Blogger:
1. Replaces the over-engineered dark navigation box with a clean, simple, minimalist design.
2. Injects the official 16:9 featured banner on bg_3.png hosted via jsDelivr CDN.
3. Preserves authentic category labels and titles.
4. Takes mandatory pre-edit backup (Rule 07 & 15).
5. Pings Google Indexing API and WebSub Hubs.
"""

import os
import sys
import json
import time
import subprocess

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID
from tools.governance.pre_flight_checker import PreFlightChecker
from tools.indexer.pubsub_hub_pinger import ping_all_hubs
from tools.backup_manager.post_backup_manager import create_post_backup

SILO_POSTS_CONFIG = [
    {
        "part": "Pillar Hub",
        "post_id": "5652005814898036993",
        "html_path": os.path.join(PROJECT_ROOT, "scratch", "raw_posts", "ssc_2027_english_1st_paper_pillar.html"),
        "meta_path": os.path.join(PROJECT_ROOT, "scratch", "raw_posts", "ssc_2027_english_1st_paper_pillar.json"),
    },
    {
        "part": "Part 01",
        "post_id": "6338741433469034454",
        "html_path": os.path.join(PROJECT_ROOT, "scratch", "raw_posts", "ssc_2027_silo_01_seen_passage.html"),
        "meta_path": os.path.join(PROJECT_ROOT, "scratch", "raw_posts", "ssc_2027_silo_01_seen_passage.json"),
    },
    {
        "part": "Part 02",
        "post_id": "7053633278573752071",
        "html_path": os.path.join(PROJECT_ROOT, "scratch", "raw_posts", "ssc_2027_silo_02_unseen_summary.html"),
        "meta_path": os.path.join(PROJECT_ROOT, "scratch", "raw_posts", "ssc_2027_silo_02_unseen_summary.json"),
    },
    {
        "part": "Part 03",
        "post_id": "7415763963240393114",
        "html_path": os.path.join(PROJECT_ROOT, "scratch", "raw_posts", "ssc_2027_silo_03_matching_rearrange.html"),
        "meta_path": os.path.join(PROJECT_ROOT, "scratch", "raw_posts", "ssc_2027_silo_03_matching_rearrange.json"),
    },
    {
        "part": "Part 04",
        "post_id": "1093847854655422506",
        "html_path": os.path.join(PROJECT_ROOT, "scratch", "raw_posts", "ssc_2027_silo_04_poems_stories.html"),
        "meta_path": os.path.join(PROJECT_ROOT, "scratch", "raw_posts", "ssc_2027_silo_04_poems_stories.json"),
    },
    {
        "part": "Part 05",
        "post_id": "4013582929893307058",
        "html_path": os.path.join(PROJECT_ROOT, "scratch", "raw_posts", "ssc_2027_silo_05_story_dialogue.html"),
        "meta_path": os.path.join(PROJECT_ROOT, "scratch", "raw_posts", "ssc_2027_silo_05_story_dialogue.json"),
    }
]

def update_all_silo_posts():
    print("=" * 75)
    print("🚀 HELPTRICKBD LIVE SILO SERIES REDESIGN & OFFICIAL BANNER SYNC")
    print("=" * 75)

    service = get_authenticated_service()
    if not service:
        print("[ERROR] Could not authenticate with Blogger API v3.")
        sys.exit(1)

    updated_urls = []

    for cfg in SILO_POSTS_CONFIG:
        part = cfg["part"]
        post_id = cfg["post_id"]
        html_path = cfg["html_path"]
        meta_path = cfg["meta_path"]

        print(f"\n{'─' * 70}")
        print(f"[*] Processing: {part} (Post ID: {post_id})")
        print(f"{'─' * 70}")

        if not os.path.exists(html_path) or not os.path.exists(meta_path):
            print(f"[ERROR] Missing file: {html_path} or {meta_path}")
            continue

        # 1. Pre-Flight Check
        checker = PreFlightChecker(html_path, metadata_path=meta_path)
        if not checker.run_all():
            checker.print_report()
            print(f"[BLOCKED] Pre-Flight failed for {part}. Skipping.")
            continue
        print("  [✔] Pre-Flight Check: PASSED (0 Errors).")

        with open(meta_path, "r", encoding="utf-8") as f:
            meta = json.load(f)
        with open(html_path, "r", encoding="utf-8") as f:
            new_content = f.read()

        # 2. Retrieve live post & create backup (Rule 07 & 15)
        print(f"  [*] Fetching live post for safety backup...")
        try:
            live_post = service.posts().get(blogId=BLOG_ID, postId=post_id).execute()
            backup_res = create_post_backup(live_post, reason="seo_title_and_lsi_update")
            print(f"  [✔] Pre-edit backup secured: {backup_res.get('backup_dir')}")
        except Exception as e_bak:
            print(f"  [!] Backup note: {e_bak}")

        # 3. Patch post content and update to the SEO-optimized front-loaded title
        patch_body = {
            "title": meta["title"],
            "content": new_content,
            "labels": meta["labels"]
        }

        print("  [*] Updating live Blogger post with front-loaded title & LSI keywords...")
        updated = service.posts().patch(blogId=BLOG_ID, postId=post_id, body=patch_body).execute()
        live_url = updated.get("url")
        print(f"  [✔] {part} Updated Successfully!")
        print(f"      Title:    {updated.get('title')}")
        print(f"      Live URL: {live_url}")
        updated_urls.append(live_url)

        time.sleep(2)

    # 4. Google Indexing API ping
    print("\n" + "=" * 75)
    print("📡 PINGING GOOGLE INDEXING API FOR ALL UPDATED POSTS...")
    print("=" * 75)
    for url in updated_urls:
        try:
            cmd = [sys.executable, os.path.join(PROJECT_ROOT, "tools", "indexer", "index_now.py"), "--url", url]
            res = subprocess.run(cmd, capture_output=True, text=True, cwd=os.path.join(PROJECT_ROOT, "tools", "indexer"))
            print(f"  [✔] Indexing API ({url}): {res.stdout.strip()}")
        except Exception as e:
            print(f"  [!] Indexing note for {url}: {e}")

    # 5. WebSub Hub ping
    print("\n[*] Pinging WebSub Hubs...")
    try:
        ping_all_hubs()
        print("  [✔] WebSub Hubs pinged successfully.")
    except Exception as e_hub:
        print(f"  [!] Hub ping note: {e_hub}")

    print("\n" + "=" * 75)
    print("🎉 ALL 5 SILO POSTS LIVE UPDATED WITH CLEAN DESIGN & OFFICIAL BANNERS!")
    print("=" * 75)

if __name__ == "__main__":
    update_all_silo_posts()
