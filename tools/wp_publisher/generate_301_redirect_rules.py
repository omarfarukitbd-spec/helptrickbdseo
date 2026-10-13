#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/wp_publisher/generate_301_redirect_rules.py
-------------------------------------------------
Generates comprehensive 301 redirection rules from legacy Blogger URLs
to modern clean WordPress URLs (/%postname%/).

Outputs:
1. archive/legacy_blogger/blogger_to_wp_301_redirects_htaccess.txt (Apache .htaccess)
2. archive/legacy_blogger/blogger_to_wp_301_redirects_nginx.conf (Nginx)
3. archive/legacy_blogger/blogger_to_wp_301_redirects_cloudflare.csv (Cloudflare / Bulk CSV)
"""

import os
import sys
import json
import csv
from datetime import datetime

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
MIGRATION_LOG = os.path.join(PROJECT_ROOT, "Helptrickbd Wp", "migration_log.json")
ARCHIVE_DIR = os.path.join(PROJECT_ROOT, "archive", "legacy_blogger")

def main():
    if not os.path.exists(MIGRATION_LOG):
        print(f"[-] Migration log not found: {MIGRATION_LOG}")
        return

    os.makedirs(ARCHIVE_DIR, exist_ok=True)

    with open(MIGRATION_LOG, "r", encoding="utf-8") as f:
        data = json.load(f)

    posts = data.get("posts", [])
    print(f"[*] Processing {len(posts)} posts for 301 redirection rules...")

    htaccess_lines = [
        "# =====================================================================",
        "# HelpTrickBD 301 Permanent Redirections (Blogger -> WordPress 6.7+)",
        f"# Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "# =====================================================================",
        "<IfModule mod_rewrite.c>",
        "RewriteEngine On",
        "",
        "# 1. Universal Regex Fallback Rule for all standard date-slug Blogger URLs",
        "RewriteRule ^[0-9]{4}/[0-9]{2}/([^/]+)\\.html$ https://www.helptrickbd.com/$1/ [R=301,L]",
        "",
        "# 2. Explicit Post-by-Post 301 Mappings",
    ]

    nginx_lines = [
        "# =====================================================================",
        "# HelpTrickBD Nginx 301 Redirection Block",
        f"# Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "# =====================================================================",
        "rewrite ^/[0-9]{4}/[0-9]{2}/([^/]+)\\.html$ https://www.helptrickbd.com/$1/ permanent;",
        "",
    ]

    csv_rows = [["Source URL", "Target URL", "Status Code"]]

    for p in posts:
        slug = p.get("slug", "")
        date_str = p.get("date", "")
        if not slug:
            continue

        year = "2026"
        month = "10"
        if date_str:
            try:
                dt = datetime.strptime(date_str[:10], "%Y-%m-%d")
                year = f"{dt.year:04d}"
                month = f"{dt.month:02d}"
            except Exception:
                pass

        old_path = f"/{year}/{month}/{slug}.html"
        new_url = f"https://www.helptrickbd.com/{slug}/"

        htaccess_lines.append(f"Redirect 301 {old_path} {new_url}")
        nginx_lines.append(f"location = {old_path} {{ return 301 {new_url}; }}")
        csv_rows.append([f"https://www.helptrickbd.com{old_path}", new_url, "301"])

    htaccess_lines.append("</IfModule>\n")

    # Write htaccess
    htaccess_file = os.path.join(ARCHIVE_DIR, "blogger_to_wp_301_redirects_htaccess.txt")
    with open(htaccess_file, "w", encoding="utf-8") as f:
        f.write("\n".join(htaccess_lines))

    # Write nginx
    nginx_file = os.path.join(ARCHIVE_DIR, "blogger_to_wp_301_redirects_nginx.conf")
    with open(nginx_file, "w", encoding="utf-8") as f:
        f.write("\n".join(nginx_lines))

    # Write csv
    csv_file = os.path.join(ARCHIVE_DIR, "blogger_to_wp_301_redirects_cloudflare.csv")
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(csv_rows)

    print(f"[OK] Generated .htaccess rules: {htaccess_file}")
    print(f"[OK] Generated Nginx rules: {nginx_file}")
    print(f"[OK] Generated Cloudflare CSV: {csv_file}")
    print(f"[SUCCESS] 301 Redirection suite complete ({len(posts)} posts mapped).")

if __name__ == "__main__":
    main()
