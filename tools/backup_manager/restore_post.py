#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/backup_manager/restore_post.py
------------------------------------
Restores a previously backed up post to Blogger.
Reinstates the exact original HTML content, title, and labels.
"""

import os
import sys
import json
import argparse

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.update_post import get_authenticated_service, BLOG_ID
from tools.backup_manager.post_backup_manager import BACKUP_ROOT, list_all_backups


def restore_from_directory(backup_dir, publish_live=False):
    """Restore post from a specific backup directory."""
    if not os.path.exists(backup_dir):
        print(f"[!] Backup directory not found: {backup_dir}")
        return False

    html_file = os.path.join(backup_dir, "original_content.html")
    meta_file = os.path.join(backup_dir, "metadata.json")

    if not os.path.exists(html_file) or not os.path.exists(meta_file):
        print("[!] Corrupted backup: missing original_content.html or metadata.json")
        return False

    with open(meta_file, "r", encoding="utf-8") as f:
        meta = json.load(f)

    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()

    post_id = meta.get("post_id")
    title = meta.get("title")
    labels = meta.get("labels", [])
    url = meta.get("url")

    print("\n" + "=" * 70)
    print("🔄 POST RESTORATION PREVIEW")
    print("=" * 70)
    print(f"  • Post ID:      {post_id}")
    print(f"  • Title:        {title}")
    print(f"  • Labels:       {labels}")
    print(f"  • Live URL:     {url}")
    print(f"  • Content Size: {len(content)} characters")
    print(f"  • Backup Dir:   {backup_dir}")
    print("=" * 70)

    if not publish_live:
        print("\n[INFO] Dry-run mode. Add `--publish` to execute live restore to Blogger.")
        return True

    print("\n[*] Restoring post on Blogger...")
    service = get_authenticated_service()
    if not service:
        print("[!] Error: Could not authenticate with Blogger API.")
        return False

    try:
        body = {
            "title": title,
            "content": content,
            "labels": labels
        }
        res = service.posts().patch(blogId=BLOG_ID, postId=post_id, body=body).execute()
        print("\n" + "=" * 70)
        print("🎉 [RESTORED] পোস্টটি সফলভাবে পূর্বাবস্থায় ফিরিয়ে আনা হয়েছে!")
        print(f"  Title:    {res.get('title')}")
        print(f"  URL:      {res.get('url')}")
        print(f"  Labels:   {res.get('labels')}")
        print(f"  Updated:  {res.get('updated')}")
        print("=" * 70 + "\n")
        return True
    except Exception as e:
        print(f"[!] Restoration Error: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="HelpTrickBD Post Restoration Tool")
    parser.add_argument("--slug", help="Slug of the post to restore (e.g. honours-political-science-book-list)")
    parser.add_argument("--dir", help="Direct path to backup directory")
    parser.add_argument("--publish", action="store_true", help="Publish directly to live Blogger")
    parser.add_argument("--list", action="store_true", help="List all available backups")

    args = parser.parse_args()

    if args.list:
        backups = list_all_backups()
        print("\n" + "=" * 70)
        print("📁 AVAILABLE POST BACKUPS")
        print("=" * 70)
        for b in backups:
            print(f"• Slug:      {b.get('slug')}")
            print(f"  Title:     {b.get('title')}")
            print(f"  Labels:    {b.get('labels')}")
            print(f"  Timestamp: {b.get('backup_timestamp')}")
            print(f"  Path:      {b.get('dir_path')}\n")
        return

    target_dir = args.dir
    if not target_dir and args.slug:
        # Default to latest
        latest_dir = os.path.join(BACKUP_ROOT, args.slug, "latest")
        if os.path.exists(latest_dir):
            target_dir = latest_dir
        else:
            print(f"[!] No 'latest' backup found for slug: {args.slug}")
            return

    if not target_dir:
        print("[!] Please provide --slug or --dir to specify which backup to restore.")
        return

    restore_from_directory(target_dir, publish_live=args.publish)


if __name__ == "__main__":
    main()
