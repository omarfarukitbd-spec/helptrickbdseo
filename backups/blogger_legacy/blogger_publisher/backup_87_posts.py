#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/backup_87_posts.py
-----------------------------------------
Backs up all 87 posts from scratch/batch_thumbnail_plan.json
prior to thumbnail deployment, strictly adhering to Rule 07.
"""

import os
import sys
import json
import time

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID

BACKUP_DIR = os.path.join(PROJECT_ROOT, "backups", "posts", "2026-09-19_mass_thumbnail_backup")
os.makedirs(BACKUP_DIR, exist_ok=True)

with open(os.path.join(PROJECT_ROOT, "scratch", "batch_thumbnail_plan.json"), "r", encoding="utf-8") as f:
    plan = json.load(f)

print(f"Starting backup for {len(plan)} posts to: {BACKUP_DIR}")

service = get_authenticated_service()

manifest = []
success_count = 0

for idx, item in enumerate(plan, start=1):
    pid = item["id"]
    title = item["title"]
    backup_file = os.path.join(BACKUP_DIR, f"{pid}.json")
    
    try:
        post_data = service.posts().get(blogId=BLOG_ID, postId=pid).execute()
        with open(backup_file, "w", encoding="utf-8") as f:
            json.dump(post_data, f, ensure_ascii=False, indent=2)
            
        manifest.append({
            "num": idx,
            "id": pid,
            "title": title,
            "url": post_data.get("url"),
            "labels": post_data.get("labels", []),
            "backup_file": f"{pid}.json",
            "content_length": len(post_data.get("content", ""))
        })
        success_count += 1
        if idx % 10 == 0 or idx == len(plan):
            print(f"Backed up {idx}/{len(plan)} posts...")
    except Exception as e:
        print(f"Error backing up post {pid} ({title[:30]}): {e}")

manifest_file = os.path.join(BACKUP_DIR, "manifest.json")
with open(manifest_file, "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print(f"\n[OK] Backup completed successfully! {success_count}/{len(plan)} posts archived in {BACKUP_DIR}")
