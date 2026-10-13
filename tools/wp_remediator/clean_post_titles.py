#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/wp_remediator/clean_post_titles.py
---------------------------------------
Removes all spam repetitions of 'Best Complete Guide' and dangling dashes/separators
from all published WordPress post titles and Rank Math SEO titles.
Saves pre-modification backup of every post before applying.
"""

import os
import sys
import re
import html
import json
import time
import argparse
from typing import Dict, Any, List

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

from tools.wp_publisher.publisher import WordPressPublisher

BACKUP_DIR = os.path.join(PROJECT_ROOT, "backups", "title_clean_backups")
MIGRATION_LOG_PATH = os.path.join(PROJECT_ROOT, "Helptrickbd Wp", "migration_log.json")

def sanitize_title(title: str) -> str:
    """
    Cleans all 'Best Complete Guide' spam, entity encodings, and punctuation stacking.
    """
    if not title:
        return ""
    
    # 1. Decode HTML entities (e.g. &#8211; -> –, &#038; -> &)
    t = html.unescape(title)
    
    # 2. Iteratively strip any variation of 'Best Complete Guide' (case-insensitive)
    spam_pattern = r'[\s\u2013\u2014\-–—|:]*\bBest Complete Guide\b[\s\d]*'
    while re.search(r'\bBest Complete Guide\b', t, flags=re.IGNORECASE):
        t = re.sub(spam_pattern, '', t, flags=re.IGNORECASE)
    
    # 3. Clean any trailing separators
    t = re.sub(r'[\s\u2013\u2014\-–—|:]+$', '', t)
    
    # 4. Clean any leading separators
    t = re.sub(r'^[\s\u2013\u2014\-–—|:]+', '', t)
    
    # 5. Fix double / triple colons (e.g. "বিষয়: বিষয়:")
    t = re.sub(r':\s*:', ':', t)
    
    # 6. Fix multiple hyphens/dashes
    t = re.sub(r'[-–—\s]+[-–—]', ' - ', t)
    
    # 7. Normalize whitespace
    t = re.sub(r'\s+', ' ', t).strip()
    
    return t

class TitleCleaner:
    def __init__(self, dry_run: bool = True, restore_original: bool = False):
        self.dry_run = dry_run
        self.restore_original = restore_original
        self.publisher = WordPressPublisher()
        self.client = self.publisher.client
        self.migration_posts_by_slug = {}
        self._load_migration_data()
        os.makedirs(BACKUP_DIR, exist_ok=True)

    def _load_migration_data(self):
        if os.path.exists(MIGRATION_LOG_PATH):
            try:
                with open(MIGRATION_LOG_PATH, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    for p in data.get("posts", []):
                        slug_norm = p.get("slug", "").strip().lower().rstrip(".")
                        self.migration_posts_by_slug[slug_norm] = p
            except Exception as e:
                print(f"[WARN] Could not load migration log: {e}")

    def fetch_all_posts(self) -> List[Dict[str, Any]]:
        posts = []
        page = 1
        per_page = 100
        while True:
            res = self.client.get("posts", params={"per_page": per_page, "page": page, "status": "publish"})
            if res.status_code != 200:
                break
            batch = res.json()
            if not batch:
                break
            posts.extend(batch)
            total_pages = int(res.headers.get("X-WP-TotalPages", 1))
            if page >= total_pages:
                break
            page += 1
            time.sleep(0.2)
        return posts

    def process_post(self, post: Dict[str, Any]) -> Dict[str, Any]:
        post_id = post.get("id")
        slug = post.get("slug", "")
        slug_norm = slug.strip().lower().rstrip(".")
        curr_rendered = post.get("title", {}).get("rendered", "")
        curr_meta = post.get("meta", {}) or {}
        curr_rm_title = curr_meta.get("rank_math_title", "")
        
        # Pre-modification backup
        backup_file = os.path.join(BACKUP_DIR, f"post_{post_id}_title_backup.json")
        with open(backup_file, "w", encoding="utf-8") as f:
            json.dump({
                "id": post_id,
                "slug": slug,
                "title_rendered": curr_rendered,
                "rank_math_title": curr_rm_title,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }, f, ensure_ascii=False, indent=2)

        mig_data = self.migration_posts_by_slug.get(slug_norm)
        
        if self.restore_original and mig_data:
            target_wp_title = mig_data.get("title", "").strip()
            focus_kw = mig_data.get("focus_keyword", "").strip()
            # If Rank Math title is wanted, keep natural title with focus kw
            target_rm_title = target_wp_title
        else:
            target_wp_title = sanitize_title(curr_rendered)
            target_rm_title = sanitize_title(curr_rm_title) if curr_rm_title else target_wp_title

        needs_update = (target_wp_title != html.unescape(curr_rendered)) or (target_rm_title != html.unescape(curr_rm_title))

        applied = False
        if needs_update and not self.dry_run:
            payload = {
                "title": target_wp_title,
                "meta": {
                    "rank_math_title": target_rm_title
                }
            }
            res = self.client.post(f"posts/{post_id}", json=payload)
            if res.status_code == 200:
                applied = True
            else:
                print(f"[ERROR] Failed to update post {post_id}: {res.status_code}")

        return {
            "id": post_id,
            "slug": slug,
            "old_title": curr_rendered,
            "new_title": target_wp_title,
            "old_rm": curr_rm_title,
            "new_rm": target_rm_title,
            "changed": needs_update,
            "applied": applied
        }

    def run(self):
        posts = self.fetch_all_posts()
        print(f"[INFO] Fetched {len(posts)} published posts. Dry-run: {self.dry_run}, Restore Original: {self.restore_original}")
        
        summary = []
        changed_count = 0
        for p in posts:
            res = self.process_post(p)
            summary.append(res)
            if res["changed"]:
                changed_count += 1
                status = "APPLIED" if res["applied"] else ("DRY-RUN SIMULATED" if self.dry_run else "FAILED")
                print(f"[{status}] ID {res['id']} ({res['slug']}):")
                print(f"  OLD: {res['old_title']}")
                print(f"  NEW: {res['new_title']}\n")

        report_file = os.path.join(PROJECT_ROOT, "reports", "title_cleanup_report.json")
        with open(report_file, "w", encoding="utf-8") as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)

        print(f"\n[DONE] Processed {len(posts)} posts. {changed_count} needed title cleanup.")
        print(f"[REPORT] Detailed report saved to: {report_file}")
        return summary

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean repeated Best Complete Guide from WP titles")
    parser.add_argument("--apply", action="store_true", help="Apply updates to live WordPress site")
    parser.add_argument("--restore-original", action="store_true", help="Restore clean original titles from migration log")
    args = parser.parse_args()

    cleaner = TitleCleaner(dry_run=not args.apply, restore_original=args.restore_original)
    cleaner.run()
