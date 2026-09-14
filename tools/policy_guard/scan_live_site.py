#!/usr/bin/env python3
"""
HelpTrickBD Live Site AdSense Policy Auditor
Scans all 78 published posts on https://www.helptrickbd.com
to detect any hidden AdSense policy violations, restricted keywords,
copyright piracy triggers, exam leak phrases, or thin content.

Usage:
    python scan_live_site.py
"""

import concurrent.futures
import json
import os
import re
import sys
import time
from urllib.parse import urlparse

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("[!] Missing requests or bs4. Run: pip install requests beautifulsoup4")
    sys.exit(1)

from policy_scanner import scan_content_for_policy_violations

CACHE_FILE = os.path.join(os.path.dirname(__file__), "..", "internal_linker", "site_articles_index.json")
REPORT_MD = os.path.join(os.path.dirname(__file__), "..", "..", "audit_adsense_policy_live.md")
REPORT_JSON = os.path.join(os.path.dirname(__file__), "..", "..", "audit_adsense_policy_live.json")


def fetch_and_scan_post(post_info):
    url = post_info["url"]
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) HelpTrickBD Policy Auditor/2.0"}
    try:
        res = requests.get(url, headers=headers, timeout=12)
        if res.status_code != 200:
            return {
                "url": url,
                "title": post_info.get("title", ""),
                "status_code": res.status_code,
                "error": f"HTTP {res.status_code}",
                "is_clean": False,
                "violations": [],
                "word_count": 0
            }

        soup = BeautifulSoup(res.text, "html.parser")
        post_body = soup.find("div", class_=re.compile(r"post-body|entry-content", re.I))
        if post_body:
            body_text = post_body.get_text(separator=" ", strip=True)
        else:
            body_text = soup.get_text(separator=" ", strip=True)

        is_clean, violations, word_count = scan_content_for_policy_violations(body_text)

        title = soup.find("title").get_text().strip() if soup.find("title") else post_info.get("title", "")

        return {
            "url": url,
            "title": title,
            "status_code": 200,
            "error": None,
            "is_clean": is_clean,
            "violations": violations,
            "word_count": word_count
        }

    except Exception as e:
        return {
            "url": url,
            "title": post_info.get("title", ""),
            "status_code": 0,
            "error": str(e),
            "is_clean": False,
            "violations": [],
            "word_count": 0
        }


def main():
    print("\n" + "="*70)
    print("  🛡️ Scanning All 78 Published Posts on HelpTrickBD for Policy Violations")
    print("="*70 + "\n")

    if not os.path.exists(CACHE_FILE):
        print(f"[!] Cache file not found at: {CACHE_FILE}")
        return

    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        posts = json.load(f)

    total_posts = len(posts)
    print(f"[*] Loaded {total_posts} published articles to scan.\n")

    results = []
    # Use concurrent threads for fast scanning
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        future_to_post = {executor.submit(fetch_and_scan_post, p): p for p in posts}
        count = 0
        for future in concurrent.futures.as_completed(future_to_post):
            count += 1
            data = future.result()
            results.append(data)
            status_symbol = "✅" if data["is_clean"] and not data["violations"] else ("🚨" if not data["is_clean"] else "⚠️")
            print(f"[{count:02d}/{total_posts}] {status_symbol} {data['title'][:45]}... ({data['word_count']} words)")

    # Analyze findings
    clean_posts = [r for r in results if r["is_clean"] and not r["violations"]]
    critical_posts = [r for r in results if not r["is_clean"]]
    warning_posts = [r for r in results if r["is_clean"] and r["violations"]]

    print("\n" + "="*70)
    print("  📊 AUDIT SUMMARY FOR 78 LIVE POSTS")
    print(f"  • Total Posts Audited:       {total_posts}")
    print(f"  • 100% Policy Safe Posts:    {len(clean_posts)}")
    print(f"  • Critical Violation Posts:  {len(critical_posts)}")
    print(f"  • Warning / Thin Posts:      {len(warning_posts)}")
    print("="*70 + "\n")

    # Save to JSON
    with open(REPORT_JSON, "w", encoding="utf-8") as f:
        json.dump({
            "total_posts": total_posts,
            "clean_count": len(clean_posts),
            "critical_count": len(critical_posts),
            "warning_count": len(warning_posts),
            "critical_posts": critical_posts,
            "warning_posts": warning_posts
        }, f, indent=2, ensure_ascii=False)

    # Generate Markdown Report
    with open(REPORT_MD, "w", encoding="utf-8") as f:
        f.write("# HelpTrickBD 78 Live Posts AdSense Policy Audit Report\n\n")
        f.write(f"- **Total Posts Scanned:** {total_posts}\n")
        f.write(f"- **100% Policy Safe:** {len(clean_posts)}\n")
        f.write(f"- **Critical Policy Violations:** {len(critical_posts)}\n")
        f.write(f"- **Warnings (Thin content / questionable terms):** {len(warning_posts)}\n\n")

        if critical_posts:
            f.write("## 🚨 Critical Policy Violations Found\n\n")
            for idx, cp in enumerate(critical_posts, 1):
                f.write(f"### {idx}. [{cp['title']}]({cp['url']})\n")
                f.write(f"- **Word Count:** {cp['word_count']} words\n")
                for v in cp["violations"]:
                    f.write(f"- **Category:** `{v['category']}` ({v['severity']})\n")
                    f.write(f"  - {v['description']}\n")
                    for term, snip in v["matches"]:
                        f.write(f"  - **Term:** `{term}` | **Context:** `...{snip.strip()}...`\n")
                f.write("\n")

        if warning_posts:
            f.write("## ⚠️ Warnings & Thin Content\n\n")
            for idx, wp in enumerate(warning_posts, 1):
                f.write(f"### {idx}. [{wp['title']}]({wp['url']})\n")
                f.write(f"- **Word Count:** {wp['word_count']} words\n")
                for v in wp["violations"]:
                    f.write(f"- **Warning:** {v['description']}\n")
                f.write("\n")

    print(f"[OK] Audit reports saved to:")
    print(f"     Markdown: {REPORT_MD}")
    print(f"     JSON:     {REPORT_JSON}\n")


if __name__ == "__main__":
    main()
