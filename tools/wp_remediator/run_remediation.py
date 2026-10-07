#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/wp_remediator/run_remediation.py
--------------------------------------
Master CLI Runner for HelpTrickBD WordPress Remediation Suite.
Option A: Legacy internal links (.html) cleaner.
Option B: Featured image linker and Rank Math SEO metadata generator.
Zero-Emoji compliance (Rule 12).
"""

import os
import sys
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
from tools.wp_remediator.link_cleaner import InternalLinkCleaner
from tools.wp_remediator.seo_meta_remediator import SeoMetaRemediator
from tools.wp_remediator.featured_image_linker import FeaturedImageLinker

BACKUP_DIR = os.path.join(PROJECT_ROOT, "backups", "remediation_backups")
REPORT_PATH = os.path.join(PROJECT_ROOT, "reports", "remediation_summary.json")

class WordPressRemediator:
    def __init__(self, dry_run: bool = True):
        self.dry_run = dry_run
        self.publisher = WordPressPublisher()
        self.client = self.publisher.client
        self.link_cleaner = InternalLinkCleaner()
        self.seo_remediator = SeoMetaRemediator()
        self.image_linker = FeaturedImageLinker(self.publisher)
        os.makedirs(BACKUP_DIR, exist_ok=True)

    def fetch_published_posts(self, limit: int = None, post_id: int = None) -> List[Dict[str, Any]]:
        """Fetches posts from WordPress REST API."""
        if post_id:
            res = self.client.get(f"posts/{post_id}")
            if res.status_code == 200:
                return [res.json()]
            print(f"[ERROR] Post ID {post_id} not found ({res.status_code})")
            return []

        posts = []
        page = 1
        per_page = 50

        while True:
            params = {"per_page": per_page, "page": page, "status": "publish"}
            res = self.client.get("posts", params=params)
            if res.status_code != 200:
                break

            batch = res.json()
            if not batch:
                break

            posts.extend(batch)
            if limit and len(posts) >= limit:
                posts = posts[:limit]
                break

            total_pages = int(res.headers.get("X-WP-TotalPages", 1))
            if page >= total_pages:
                break
            page += 1
            time.sleep(0.2)

        return posts

    def save_post_backup(self, post: Dict[str, Any]):
        """Saves pre-update backup of the post (Rule 07)."""
        post_id = post.get("id")
        backup_file = os.path.join(BACKUP_DIR, f"post_{post_id}_backup.json")
        with open(backup_file, "w", encoding="utf-8") as f:
            json.dump({
                "id": post_id,
                "title": post.get("title", {}).get("rendered", ""),
                "slug": post.get("slug", ""),
                "content": post.get("content", {}).get("rendered", ""),
                "featured_media": post.get("featured_media", 0),
                "meta": post.get("meta", {}),
                "backed_up_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            }, f, ensure_ascii=False, indent=2)

    def remediate_post(
        self,
        post: Dict[str, Any],
        fix_links: bool = True,
        fix_seo_meta: bool = True,
        fix_featured_images: bool = True
    ) -> Dict[str, Any]:
        """Runs remediation checks and applies fixes if not in dry-run mode."""
        post_id = post.get("id")
        title = post.get("title", {}).get("rendered", "")
        raw_content = post.get("content", {}).get("rendered", "")
        current_featured = post.get("featured_media", 0)
        
        result = {
            "id": post_id,
            "title": title[:50],
            "slug": post.get("slug", ""),
            "changes_detected": False,
            "links_rewritten": 0,
            "seo_meta_updated": False,
            "featured_image_set": False,
            "actions": []
        }

        update_payload = {}

        # 1. Option A: Clean Internal Links
        if fix_links:
            new_content, count_changed, link_changes = self.link_cleaner.clean_content(raw_content)
            if count_changed > 0:
                result["changes_detected"] = True
                result["links_rewritten"] = count_changed
                result["actions"].append(f"Rewrote {count_changed} legacy internal links to clean URLs")
                update_payload["content"] = new_content

        # 2. Option B: Rank Math SEO Meta
        if fix_seo_meta:
            rm_meta = self.seo_remediator.build_rank_math_meta(post)
            # Check if meta is already populated
            existing_meta = post.get("meta", {})
            curr_desc = existing_meta.get("rank_math_description", "")
            curr_kw = existing_meta.get("rank_math_focus_keyword", "")

            if not curr_desc or not curr_kw:
                result["changes_detected"] = True
                result["seo_meta_updated"] = True
                result["actions"].append(f"Injected Rank Math Focus KW: '{rm_meta['rank_math_focus_keyword']}' and Meta Description")
                update_payload["meta"] = rm_meta

        # 3. Option B: Featured Image Linking
        if fix_featured_images and current_featured == 0:
            hero_info = self.image_linker.extract_hero_image_info(raw_content)
            if hero_info:
                local_img = self.image_linker.resolve_local_image_path(hero_info)
                if local_img:
                    result["actions"].append(f"Found hero image: {os.path.basename(local_img)}")
                    if not self.dry_run:
                        media_id = self.image_linker.get_or_upload_media(
                            local_path=local_img,
                            alt_text=hero_info.get("alt") or title,
                            title=hero_info.get("title") or title
                        )
                        if media_id:
                            update_payload["featured_media"] = media_id
                            result["changes_detected"] = True
                            result["featured_image_set"] = True
                            result["actions"].append(f"Bound media ID {media_id} as featured_media")
                    else:
                        result["changes_detected"] = True
                        result["featured_image_set"] = True
                        result["actions"].append("[DRY-RUN] Will upload/bind hero image as featured_media")

        # 4. Apply updates via REST API if not dry-run
        if not self.dry_run and result["changes_detected"] and update_payload:
            self.save_post_backup(post)
            res = self.client.post(f"posts/{post_id}", json=update_payload)
            if res.status_code == 200:
                result["applied"] = True
                result["status"] = "SUCCESS"
            else:
                result["applied"] = False
                result["status"] = f"ERROR ({res.status_code})"
                result["error"] = res.text
        else:
            result["applied"] = False
            result["status"] = "PREVIEW (DRY-RUN)" if self.dry_run else "SKIPPED (NO CHANGES)"

        return result

    def run(
        self,
        fix_links: bool = True,
        fix_seo_meta: bool = True,
        fix_featured_images: bool = True,
        limit: int = None,
        post_id: int = None
    ) -> Dict[str, Any]:
        """Main execution flow."""
        mode_label = "DRY-RUN PREVIEW (No Changes Applied)" if self.dry_run else "LIVE REMEDIATION (Applying Changes)"
        print("=" * 70)
        print(f"HELPTRICKBD WORDPRESS REMEDIATION SUITE")
        print(f"MODE: {mode_label}")
        print("=" * 70)

        posts = self.fetch_published_posts(limit=limit, post_id=post_id)
        print(f"[*] Loaded {len(posts)} posts for processing...")

        results = []
        total_links_rewritten = 0
        total_meta_updated = 0
        total_images_set = 0

        for i, post in enumerate(posts, 1):
            p_id = post.get("id")
            title = post.get("title", {}).get("rendered", "")[:40]
            res = self.remediate_post(
                post=post,
                fix_links=fix_links,
                fix_seo_meta=fix_seo_meta,
                fix_featured_images=fix_featured_images
            )
            results.append(res)

            total_links_rewritten += res["links_rewritten"]
            if res["seo_meta_updated"]:
                total_meta_updated += 1
            if res["featured_image_set"]:
                total_images_set += 1

            status_str = res["status"]
            actions_summary = "; ".join(res["actions"]) if res["actions"] else "None"
            print(f"    [{i:03d}/{len(posts):03d}] ID {p_id}: {status_str} | {actions_summary[:70]}")
            time.sleep(0.1)

        summary = {
            "mode": "dry_run" if self.dry_run else "live_applied",
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "total_processed": len(posts),
            "total_links_rewritten": total_links_rewritten,
            "total_seo_meta_updated": total_meta_updated,
            "total_featured_images_set": total_images_set,
            "results": results
        }

        os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
        with open(REPORT_PATH, "w", encoding="utf-8") as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)

        # Generate MySQL scripts for direct phpMyAdmin / Adminer 1-click execution
        sql_meta_path = os.path.join(PROJECT_ROOT, "reports", "inject_rank_math_meta.sql")
        with open(sql_meta_path, "w", encoding="utf-8") as f_sql:
            f_sql.write("-- HelpTrickBD - Rank Math SEO Postmeta Batch Injector\n")
            f_sql.write("-- Generated by tools/wp_remediator/\nSTART TRANSACTION;\n\n")
            for post in posts:
                p_id = post.get("id")
                meta = self.seo_remediator.build_rank_math_meta(post)
                kw = meta["rank_math_focus_keyword"].replace("'", "''")
                desc = meta["rank_math_description"].replace("'", "''")
                title = "%title% %sep% %sitename%"
                f_sql.write(f"-- Post ID {p_id}\n")
                f_sql.write(f"DELETE FROM wp_postmeta WHERE post_id = {p_id} AND meta_key IN ('rank_math_focus_keyword', 'rank_math_description', 'rank_math_title');\n")
                f_sql.write(f"INSERT INTO wp_postmeta (post_id, meta_key, meta_value) VALUES ({p_id}, 'rank_math_focus_keyword', '{kw}');\n")
                f_sql.write(f"INSERT INTO wp_postmeta (post_id, meta_key, meta_value) VALUES ({p_id}, 'rank_math_description', '{desc}');\n")
                f_sql.write(f"INSERT INTO wp_postmeta (post_id, meta_key, meta_value) VALUES ({p_id}, 'rank_math_title', '{title}');\n\n")
        # Generate MySQL script for legacy links
        sql_links_path = os.path.join(PROJECT_ROOT, "reports", "rewrite_legacy_links.sql")
        with open(sql_links_path, "w", encoding="utf-8") as f_links:
            f_links.write("-- HelpTrickBD - Legacy Internal Links Rewriter\n")
            f_links.write("-- Generated by tools/wp_remediator/\nSTART TRANSACTION;\n\n")
            # Write alias replacements
            for old_s, new_s in self.link_cleaner.slug_map.items():
                if old_s != new_s:
                    f_links.write(f"UPDATE wp_posts SET post_content = REPLACE(post_content, '/{old_s}.html', '/{new_s}/') WHERE post_content LIKE '%/{old_s}.html%';\n")
                    f_links.write(f"UPDATE wp_posts SET post_content = REPLACE(post_content, 'helptrickbd.com/p/{old_s}.html', 'helptrickbd.com/{new_s}/') WHERE post_content LIKE '%helptrickbd.com/p/{old_s}.html%';\n")
            f_links.write("\n-- Regex replacement for standard YYYY/MM/slug.html and /p/slug.html\n")
            f_links.write("UPDATE wp_posts SET post_content = REGEXP_REPLACE(post_content, 'https?://(www\\\\.)?helptrickbd\\\\.com/(p/|[0-9]{4}/[0-9]{2}/)?([a-zA-Z0-9_-]+)\\\\.html', 'https://www.helptrickbd.com/\\\\3/') WHERE post_content REGEXP 'helptrickbd\\\\.com/(p/|[0-9]{4}/[0-9]{2}/)?[a-zA-Z0-9_-]+\\\\.html';\n")
            f_links.write("COMMIT;\n")

        print("-" * 70)
        print(f"[SUMMARY] Total Posts Checked     : {len(posts)}")
        print(f"          Total Links Rewritten    : {total_links_rewritten}")
        print(f"          Posts with SEO Meta Set  : {total_meta_updated}")
        print(f"          Posts with Featured Img  : {total_images_set}")
        print(f"          Report Saved to          : {REPORT_PATH}")
        print(f"          SQL Batch Script         : {sql_meta_path}")
        print("=" * 70)

        return summary


def main():
    parser = argparse.ArgumentParser(description="HelpTrickBD WordPress Remediation Suite")
    parser.add_argument("--apply", action="store_true", help="Apply changes to live database (Default is dry-run)")
    parser.add_argument("--dry-run", action="store_true", help="Preview mode only (Default)")
    parser.add_argument("--links", action="store_true", help="Remediate legacy internal links only (Option A)")
    parser.add_argument("--seo-meta", action="store_true", help="Remediate Rank Math SEO metadata only (Option B)")
    parser.add_argument("--featured-images", action="store_true", help="Remediate featured images only (Option B)")
    parser.add_argument("--all", action="store_true", help="Remediate all: links, SEO meta, and featured images")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of posts to process")
    parser.add_argument("--post-id", type=int, default=None, help="Process single post by ID")

    args = parser.parse_args()

    # Determine execution mode
    is_live = args.apply and not args.dry_run

    # Determine actions
    if args.all or (not args.links and not args.seo_meta and not args.featured_images):
        fix_links = True
        fix_seo_meta = True
        fix_featured_images = True
    else:
        fix_links = args.links
        fix_seo_meta = args.seo_meta
        fix_featured_images = args.featured_images

    remediator = WordPressRemediator(dry_run=not is_live)
    remediator.run(
        fix_links=fix_links,
        fix_seo_meta=fix_seo_meta,
        fix_featured_images=fix_featured_images,
        limit=args.limit,
        post_id=args.post_id
    )

if __name__ == "__main__":
    main()
