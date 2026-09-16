#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/content_optimizer/cleanup_duplicate_tocs.py
-------------------------------------------------
Automated cleanup of duplicate Table of Contents (TOC) across all 13 identified posts:
1. Takes 100% full snapshot backups (post_snapshot.json, content_original.html)
2. Removes the redundant <div class="ht-toc-container"> while preserving the official .htbd-toc-box
3. Live patches each post on Blogger via Blogger API v3
4. Pings Google Indexing API
"""

import os
import sys
import json
import time
import subprocess
from datetime import datetime
from bs4 import BeautifulSoup

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID

TARGET_POST_IDS = [
    "179336939989858201",  # শিল্প জাতীয়করণ
    "5020265416603423827",  # খেলার সাথী
    "1429095227109508205",  # রাজনৈতিক অর্থনীতি
    "8095492964121246778",  # নারীর ক্ষমতায়নে এনজিও
    "5786345583005242847",  # বিদ্যাসাগর
    "3163731179305221308",  # BLRI
    "9216865562894997738",  # সরকার ও রাজনৈতিক দল
    "3465437051897928179",  # কম্পিউটার প্রকারভেদ পার্ট-৪
    "5955879897597266679",  # কম্পিউটার প্রজন্ম পার্ট-৩
    "4287526406029588825",  # কম্পিউটার ইতিহাস পার্ট-২
    "2080353291294038390",  # রাষ্ট্রচিন্তা কাকে বলে
    "4705377665339185450",  # সামাজিক পরিবর্তন ৩১১৯০৩
    "1200879181592128005",  # অলস ও ব্যাকবেঞ্চার
]

def backup_post(post_data):
    post_id = post_data["id"]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    slug = post_data.get("url", "").split("/")[-1].replace(".html", "") or post_id
    backup_dir = os.path.join(PROJECT_ROOT, "backups", "posts", slug, timestamp)
    os.makedirs(backup_dir, exist_ok=True)

    with open(os.path.join(backup_dir, "post_snapshot.json"), "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)

    with open(os.path.join(backup_dir, "content_original.html"), "w", encoding="utf-8") as f:
        f.write(post_data.get("content", ""))

    print(f"      [✔] Backup saved: backups/posts/{slug}/{timestamp}/")
    return backup_dir

def main():
    service = get_authenticated_service()
    if not service:
        print("[!] Failed to authenticate Blogger API v3.")
        return

    print("=" * 70)
    print("🧹 CLEANING UP DUPLICATE TABLE OF CONTENTS ACROSS 13 POSTS")
    print("=" * 70)

    cleaned_count = 0
    for idx, post_id in enumerate(TARGET_POST_IDS, 1):
        try:
            print(f"\n[{idx}/{len(TARGET_POST_IDS)}] Fetching Post ID: {post_id}...")
            post = service.posts().get(blogId=BLOG_ID, postId=post_id).execute()
            title = post.get("title", "")
            url = post.get("url", "")
            content = post.get("content", "")

            print(f"    Title: {title}")
            print(f"    URL:   {url}")

            if "ht-toc-container" not in content:
                print("    [-] ht-toc-container not found in content, skipping.")
                continue

            # 1. Full Backup
            backup_post(post)

            # 2. Parse & Remove duplicate TOC
            soup = BeautifulSoup(content, "html.parser")
            toc_containers = soup.find_all("div", class_="ht-toc-container")
            for tc in toc_containers:
                tc.decompose()

            cleaned_html = str(soup)

            # 3. Patch Blogger
            patch_body = {"content": cleaned_html}
            service.posts().patch(blogId=BLOG_ID, postId=post_id, body=patch_body).execute()
            print("      [✔] Blogger Post updated: ht-toc-container removed, clean TOC preserved.")
            cleaned_count += 1

            # 4. Ping Google Indexing API
            try:
                indexer_cmd = [
                    sys.executable,
                    os.path.join(PROJECT_ROOT, "tools", "indexer", "index_now.py"),
                    "--url", url
                ]
                subprocess.run(indexer_cmd, capture_output=True, text=True, cwd=os.path.join(PROJECT_ROOT, "tools", "indexer"))
                print("      [✔] Google Indexing API pinged.")
            except Exception as e_idx:
                print(f"      [!] Google Indexing Ping error: {e_idx}")

            time.sleep(1.5)
        except Exception as e:
            print(f"    [!] Error processing post {post_id}: {e}")

    print("\n" + "=" * 70)
    print(f"🎉 COMPLETED: Successfully cleaned up duplicate TOC in {cleaned_count} posts!")
    print("=" * 70)

if __name__ == "__main__":
    main()
