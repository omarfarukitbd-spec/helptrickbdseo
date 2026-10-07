#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/wp_auditor/wp_auditor_core.py
------------------------------------
Core 360-Degree WordPress Site Auditor for HelpTrickBD.
Audits published posts, static pages, categories, and image assets.
Zero-Emoji compliance (Rule 12).
"""

import os
import sys
import json
import time

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

from bs4 import BeautifulSoup
from typing import List, Dict, Any, Optional

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.wp_publisher.publisher import WordPressPublisher
from tools.wp_auditor.audit_rules import (
    audit_content_depth,
    audit_image_seo,
    audit_rank_math_seo,
    audit_headings,
    audit_links_and_legacy,
    audit_interactive_elements
)

MANDATORY_LEGAL_PAGES = [
    {"label": "About Us (আমাদের সম্পর্কে)", "patterns": ["about-us", "about"], "primary_slug": "about-us"},
    {"label": "Contact Us (যোগাযোগ)", "patterns": ["contact-us", "contact"], "primary_slug": "contact-us"},
    {"label": "Privacy Policy (গোপনীয়তা নীতি)", "patterns": ["privacy-policy", "privacy"], "primary_slug": "privacy-policy"},
    {"label": "Terms and Conditions (ব্যবহারের শর্তাবলী)", "patterns": ["terms-conditions", "terms-and-conditions", "terms"], "primary_slug": "terms-conditions"},
    {"label": "Disclaimer (দাবিত্যাগ)", "patterns": ["disclaimer"], "primary_slug": "disclaimer"}
]

class WordPressSiteAuditor:
    def __init__(self):
        self.publisher = WordPressPublisher()
        self.client = self.publisher.client
        self.base_url = self.client.base_url

    def fetch_all_categories(self) -> List[Dict[str, Any]]:
        """Fetches all categories to audit category balance."""
        res = self.client.get("categories", params={"per_page": 100})
        if res.status_code == 200:
            return res.json()
        return []

    def fetch_all_pages(self) -> List[Dict[str, Any]]:
        """Fetches all static pages to verify mandatory legal pages."""
        res = self.client.get("pages", params={"per_page": 100})
        if res.status_code == 200:
            return res.json()
        return []

    def fetch_posts(self, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """Fetches published posts via pagination."""
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

            # Check total pages
            total_pages = int(res.headers.get("X-WP-TotalPages", 1))
            if page >= total_pages:
                break
            page += 1
            time.sleep(0.3)

        return posts

    def audit_site(self, limit: Optional[int] = None) -> Dict[str, Any]:
        """Runs full 360-degree site audit."""
        print("=" * 70)
        print("HELPTRICKBD WORDPRESS 360-DEGREE FULL SITE AUDIT")
        print("=" * 70)

        # 1. Audit Categories (AdSense balance)
        print("[*] Fetching and auditing WordPress categories...")
        categories = self.fetch_all_categories()
        category_audit = []
        under_populated_cats = []

        for cat in categories:
            count = cat.get("count", 0)
            name = cat.get("name", "")
            slug = cat.get("slug", "")
            cat_status = "PASS" if count >= 4 else "WARNING"
            if count < 4:
                under_populated_cats.append(f"{name} ({count} posts)")
            category_audit.append({
                "name": name,
                "slug": slug,
                "count": count,
                "status": cat_status
            })

        print(f"    Audited {len(categories)} categories. Under-populated (<4 posts): {len(under_populated_cats)}")

        # 2. Audit Mandatory Legal Pages
        print("[*] Verifying 5 mandatory AdSense legal pages...")
        pages = self.fetch_all_pages()
        page_slugs = {p.get("slug", ""): p for p in pages}
        legal_page_audit = []
        missing_legal_pages = []

        for item in MANDATORY_LEGAL_PAGES:
            label = item["label"]
            patterns = item["patterns"]
            matched_slug = None
            for p_slug in page_slugs.keys():
                for pat in patterns:
                    if pat == p_slug or pat.replace("-", "") in p_slug.replace("-", ""):
                        matched_slug = p_slug
                        break
                if matched_slug:
                    break

            found = matched_slug is not None
            legal_page_audit.append({
                "label": label,
                "slug": matched_slug if found else item["primary_slug"],
                "found": found
            })
            if not found:
                missing_legal_pages.append(label)

        print(f"    Legal pages found: {len(MANDATORY_LEGAL_PAGES) - len(missing_legal_pages)}/{len(MANDATORY_LEGAL_PAGES)}")

        # 3. Audit Posts
        print(f"[*] Fetching published posts from WordPress REST API (limit: {limit or 'ALL'})...")
        posts = self.fetch_posts(limit=limit)
        print(f"    Loaded {len(posts)} posts. Beginning deep HTML & SEO content analysis...")

        post_results = []
        critical_count = 0
        warning_count = 0
        pass_count = 0

        for idx, post in enumerate(posts, 1):
            p_id = post.get("id")
            title = post.get("title", {}).get("rendered", "")
            slug = post.get("slug", "")
            content_html = post.get("content", {}).get("rendered", "")
            edit_url = f"{self.base_url}/wp-admin/post.php?post={p_id}&action=edit"
            live_url = post.get("link", f"{self.base_url}/{slug}/")

            soup = BeautifulSoup(content_html, "html.parser")

            # Run rule audits
            c_depth = audit_content_depth(post, soup)
            img_seo = audit_image_seo(post, soup)
            rm_seo = audit_rank_math_seo(post, soup)
            headings = audit_headings(post, soup)
            links = audit_links_and_legacy(post, soup)
            interactive = audit_interactive_elements(post, soup)

            # Determine overall post verdict
            checks = [c_depth, img_seo, rm_seo, headings, links, interactive]
            has_critical = any(c["status"] == "CRITICAL" for c in checks)
            has_warning = any(c["status"] == "WARNING" for c in checks)

            if has_critical:
                overall_status = "CRITICAL"
                critical_count += 1
            elif has_warning:
                overall_status = "WARNING"
                warning_count += 1
            else:
                overall_status = "PASS"
                pass_count += 1

            post_audit = {
                "id": p_id,
                "title": title,
                "slug": slug,
                "live_url": live_url,
                "edit_url": edit_url,
                "status": overall_status,
                "word_count": c_depth["word_count"],
                "checks": {
                    "content_depth": c_depth,
                    "image_seo": img_seo,
                    "rank_math": rm_seo,
                    "headings": headings,
                    "links": links,
                    "interactive": interactive
                }
            }
            post_results.append(post_audit)
            print(f"    [{idx:03d}/{len(posts):03d}] ID {p_id}: {overall_status} | Words: {c_depth['word_count']} | {title[:40]}...")

        # Summary compilation
        summary = {
            "total_posts_audited": len(posts),
            "posts_pass": pass_count,
            "posts_warning": warning_count,
            "posts_critical": critical_count,
            "total_categories": len(categories),
            "under_populated_categories": under_populated_cats,
            "missing_legal_pages": missing_legal_pages
        }

        full_audit = {
            "summary": summary,
            "legal_pages": legal_page_audit,
            "categories": category_audit,
            "posts": post_results
        }

        return full_audit

    def export_reports(self, audit_data: Dict[str, Any], output_md: str, output_json: str):
        """Exports audit results to Markdown and JSON formats."""
        os.makedirs(os.path.dirname(output_md), exist_ok=True)

        # JSON Export
        with open(output_json, "w", encoding="utf-8") as f:
            json.dump(audit_data, f, ensure_ascii=False, indent=2)

        # Markdown Export
        summary = audit_data["summary"]
        lines = []
        lines.append("# HelpTrickBD WordPress 360-Degree Site Audit Report\n")
        lines.append(f"**Target Site:** {self.base_url}\n")
        lines.append(f"**Audit Scope:** {summary['total_posts_audited']} Published Posts & Core Taxonomies\n")
        lines.append("---\n")

        lines.append("## 1. Executive Summary\n")
        lines.append("| Metric | Result | Target |\n")
        lines.append("| :--- | :--- | :--- |\n")
        lines.append(f"| **Total Posts Audited** | {summary['total_posts_audited']} | 100% of Active Posts |\n")
        lines.append(f"| **Clean Posts (PASS)** | {summary['posts_pass']} | Maximum |\n")
        lines.append(f"| **Posts with Warnings** | {summary['posts_warning']} | Minimize |\n")
        lines.append(f"| **Critical Attention Required** | {summary['posts_critical']} | 0 |\n")
        lines.append(f"| **Missing Legal Pages** | {len(summary['missing_legal_pages'])} | 0 (5/5 required) |\n")
        lines.append(f"| **Under-Populated Categories (<4 posts)** | {len(summary['under_populated_categories'])} | 0 |\n\n")

        # Legal Pages Section
        lines.append("## 2. AdSense Mandatory Legal Pages Audit\n")
        for item in audit_data["legal_pages"]:
            status_tag = "[OK] PUBLISHED" if item["found"] else "[ACTION NEEDED] MISSING"
            lines.append(f"* **{item['label']}**: {status_tag} (slug: `/{item['slug']}/`)\n")
        lines.append("\n")

        # Categories Section
        lines.append("## 3. Category Balance Audit (AdSense Policy)\n")
        if summary["under_populated_categories"]:
            lines.append("The following categories have fewer than 4 published posts and must not be placed in top navigation:\n")
            for cat in summary["under_populated_categories"]:
                lines.append(f"* {cat}\n")
        else:
            lines.append("All active categories have 4 or more published posts. Excellent balance.\n")
        lines.append("\n")

        # Posts Needing Attention
        lines.append("## 4. Post Action Checklist (Ordered by Priority)\n")
        flagged_posts = [p for p in audit_data["posts"] if p["status"] in ("CRITICAL", "WARNING")]

        if not flagged_posts:
            lines.append("All audited posts passed all quality, SEO, and image guidelines.\n")
        else:
            for p in flagged_posts:
                lines.append(f"### Post {p['id']}: [{p['status']}] {p['title']}\n")
                lines.append(f"* **Live URL:** [{p['live_url']}]({p['live_url']})\n")
                lines.append(f"* **WordPress Edit Link:** [Edit in WP-Admin]({p['edit_url']})\n")
                lines.append(f"* **Word Count:** {p['word_count']:,} words\n")
                lines.append("* **Issues Identified:**\n")
                for c_name, c_data in p["checks"].items():
                    if c_data.get("status") in ("CRITICAL", "WARNING"):
                        for msg in c_data.get("messages", []):
                            lines.append(f"  - `{c_name}`: {msg}\n")
                lines.append("\n")

        with open(output_md, "w", encoding="utf-8") as f:
            f.write("".join(lines))

        print(f"\n[OK] Reports generated successfully:")
        print(f"     Markdown Report : {output_md}")
        print(f"     JSON Data Dump  : {output_json}")
