#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/backup_audit_fix_targets.py
Safely backs up all posts targeted for the 3 audit fixes into
backups/posts/2026-09-19_audit_fixes_backup/ before making any modifications.
"""

import os
import sys
import json
import time

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID

BACKUP_DIR = os.path.join(PROJECT_ROOT, "backups", "posts", "2026-09-19_audit_fixes_backup")
os.makedirs(BACKUP_DIR, exist_ok=True)

# 1. Thin posts
THIN_PIDS = [
    "5496176856660793475", # রাজনীতিতে নারীর অংশগ্রহণ
    "8548896560937787860", # নারী নির্যাতন
    "6725103459411539325", # রাজা রামমোহন রায়
    "7152628717436788366", # মহাত্মা গান্ধী
    "6126999372993436911"  # লেনিনের জীবনী
]

# 2. Label fix post
LABEL_PIDS = ["4710432391315087780"]

# 3. Byte-0 failed posts
BYTE0_FILE = os.path.join(PROJECT_ROOT, "scratch", "all_byte_0_failed.json")
with open(BYTE0_FILE, "r", encoding="utf-8") as f:
    byte0_items = json.load(f)
BYTE0_PIDS = [item["id"] for item in byte0_items]

ALL_TARGET_PIDS = list(dict.fromkeys(THIN_PIDS + LABEL_PIDS + BYTE0_PIDS))
print(f"Total unique target posts to backup: {len(ALL_TARGET_PIDS)}")

service = get_authenticated_service()
if not service:
    print("[ERROR] Auth failed")
    sys.exit(1)

manifest = []

for idx, pid in enumerate(ALL_TARGET_PIDS, 1):
    try:
        post = service.posts().get(blogId=BLOG_ID, postId=pid, view="ADMIN").execute()
        file_path = os.path.join(BACKUP_DIR, f"{pid}.json")
        with open(file_path, "w", encoding="utf-8") as out:
            json.dump(post, out, ensure_ascii=False, indent=2)
            
        manifest.append({
            "num": idx,
            "id": pid,
            "title": post.get("title"),
            "url": post.get("url"),
            "labels": post.get("labels", []),
            "published": post.get("published"),
            "content_length": len(post.get("content", ""))
        })
        print(f"[{idx}/{len(ALL_TARGET_PIDS)}] Backed up: {post.get('title')[:45]}...")
        time.sleep(1)
    except Exception as e:
        print(f"[ERROR] Failed to backup {pid}: {e}")

manifest_file = os.path.join(BACKUP_DIR, "manifest.json")
with open(manifest_file, "w", encoding="utf-8") as out:
    json.dump(manifest, out, ensure_ascii=False, indent=2)

print(f"\n[OK] Successfully backed up all {len(manifest)} target posts with manifest at: {manifest_file}")
