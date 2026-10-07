#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/backup_and_sanitize_policy_posts.py
-----------------------------------------------------------
Backs up and sanitizes the 5 sensitive political science / sociology posts
on Blogger live according to Rule 07 (Backup) and Google AdSense Family-Safe
academic language policies.
Strictly Zero Emojis (Rule 12).
"""

import os
import sys
import json
import re
import time

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID

BACKUP_DIR = os.path.join(PROJECT_ROOT, "backups", "posts", "2026-10-05_policy_sanitization_backup")
os.makedirs(BACKUP_DIR, exist_ok=True)

TARGET_POST_IDS = [
    "8316268127112895155",  # নারী আন্দোলন ও অধিকার
    "3995402116153520",     # পুরুষতন্ত্র কাকে বলে
    "8548896560937787860",  # নারী নির্যাতন কী
    "6485913933681271646",  # ইমাম গাজ্জালির রাজনৈতিক দর্শন
    "2080353291294038390",  # রাষ্ট্রচিন্তা কাকে বলে (ডুপ্লিকেট প্যারাগ্রাফ ফিক্স)
]

def backup_posts(service):
    print("=" * 60)
    print("STEP 1: BACKING UP TARGET POSTS (Rule 07)")
    print("=" * 60)
    manifest = []
    posts_data = {}
    for pid in TARGET_POST_IDS:
        post = service.posts().get(blogId=BLOG_ID, postId=pid, view="ADMIN").execute()
        file_path = os.path.join(BACKUP_DIR, f"{pid}.json")
        with open(file_path, "w", encoding="utf-8") as out:
            json.dump(post, out, ensure_ascii=False, indent=2)
        
        info = {
            "id": pid,
            "title": post.get("title"),
            "url": post.get("url"),
            "labels": post.get("labels", []),
            "backup_file": file_path,
            "content_length": len(post.get("content", ""))
        }
        manifest.append(info)
        posts_data[pid] = post
        print(f"[BACKUP OK] {pid} | {info['title']}")
        
    manifest_path = os.path.join(BACKUP_DIR, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as mf:
        json.dump(manifest, mf, ensure_ascii=False, indent=2)
    print(f"Manifest written to: {manifest_path}\n")
    return posts_data

if __name__ == "__main__":
    service = get_authenticated_service()
    if not service:
        print("[ERROR] Auth failed.")
        sys.exit(1)
    backup_posts(service)
