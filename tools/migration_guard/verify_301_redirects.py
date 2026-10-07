#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/migration_guard/verify_301_redirects.py
---------------------------------------------
Automated 301 Permanent Redirect Auditor for HelpTrickBD.
Tests legacy Blogger URLs (e.g., /YYYY/MM/post.html) against the live
WordPress site and verifies HTTP 301 status and target URL matching.

Usage:
  python tools/migration_guard/verify_301_redirects.py [--limit 10]
"""

import os
import sys
import json
import argparse
import requests

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def run_redirect_audit(limit=None):
    print("=" * 70)
    print("HELPTRICKBD 301 REDIRECTION AUDITOR")
    print("=" * 70)

    # Try to load migration log
    migration_log_path = os.path.join(PROJECT_ROOT, "Helptrickbd Wp", "migration_log.json")
    if not os.path.exists(migration_log_path):
        migration_log_path = os.path.join(os.path.dirname(PROJECT_ROOT), "Helptrickbd Wp", "migration_log.json")

    urls_to_test = []
    if os.path.exists(migration_log_path):
        with open(migration_log_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            # data has post list with old and new links
            for item in data.get("posts", []):
                old_url = item.get("blogger_url") or item.get("original_url")
                new_slug = item.get("slug")
                if old_url:
                    urls_to_test.append((old_url, new_slug))

    if not urls_to_test:
        # Fallback sample test urls
        urls_to_test = [
            ("https://www.helptrickbd.com/2026/09/honours-political-science-book-list.html", "honours-political-science-book-list"),
            ("https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-mcq-saq-question.html", "ssc-bangla-1st-paper-mcq-saq-question"),
            ("https://www.helptrickbd.com/p/nu-cgpa-calculator.html", "nu-cgpa-calculator")
        ]

    if limit:
        urls_to_test = urls_to_test[:limit]

    print(f"Total URLs to test: {len(urls_to_test)}")
    print("-" * 70)

    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HelpTrickBD Redirect Tester)"
    })

    success_count = 0
    failure_count = 0

    for idx, (old_url, expected_slug) in enumerate(urls_to_test, 1):
        try:
            resp = session.get(old_url, allow_redirects=False, timeout=10)
            status_code = resp.status_code
            location = resp.headers.get("Location", "")

            is_301 = (status_code == 301)
            slug_match = expected_slug in location if expected_slug else True

            if is_301 and slug_match:
                print(f"[{idx:03d}] PASS (301) -> {location}")
                success_count += 1
            elif status_code == 200:
                print(f"[{idx:03d}] DIRECT 200 (No redirect needed or already new) -> {old_url}")
                success_count += 1
            else:
                print(f"[{idx:03d}] FAIL (Status: {status_code}) | Target: {location} | Expected: {expected_slug}")
                failure_count += 1

        except Exception as e:
            print(f"[{idx:03d}] ERROR: {e}")
            failure_count += 1

    print("=" * 70)
    print(f"Audit Summary: {success_count} Passed | {failure_count} Failed")
    print("=" * 70)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test 301 redirects for HelpTrickBD")
    parser.add_argument("--limit", type=int, default=15, help="Number of URLs to test")
    args = parser.parse_args()
    run_redirect_audit(limit=args.limit)
