#!/usr/bin/env python3
"""
SEO & AdSense Readiness Auditor for HelpTrickBD (www.helptrickbd.com)
Crawls sitemaps and pages, checking 404s, thin content, headings, meta tags,
schema markup, and AdSense approval red flags.

Usage:
    python audit_site.py
    python audit_site.py --sitemap https://www.helptrickbd.com/sitemap.xml --pages-sitemap https://www.helptrickbd.com/sitemap-pages.xml
"""

import argparse
import json
import os
import re
import sys
import time
import xml.etree.ElementTree as ET
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
    print("\n[!] Missing required libraries. Please install:")
    print("    pip install requests beautifulsoup4\n")
    sys.exit(1)

DEFAULT_SITEMAP = "https://www.helptrickbd.com/sitemap.xml"
DEFAULT_PAGES_SITEMAP = "https://www.helptrickbd.com/sitemap-pages.xml"
OUTPUT_MD = "audit_report.md"
OUTPUT_JSON = "audit_report.json"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) HelpTrickBDOptimizer/1.0"
}


def fetch_sitemap_urls(sitemap_url):
    """Fetches URLs from XML sitemap."""
    try:
        res = requests.get(sitemap_url, headers=HEADERS, timeout=12)
        if res.status_code != 200:
            return []
        root = ET.fromstring(res.content)
        ns = ""
        if root.tag.startswith("{"):
            ns = root.tag.split("}")[0] + "}"
        return [elem.text.strip() for elem in root.findall(f".//{ns}loc") if elem.text]
    except Exception as e:
        print(f"[!] Error fetching sitemap {sitemap_url}: {e}")
        return []


def audit_page(url, is_static_page=False):
    """Analyzes a single page for SEO and AdSense issues."""
    result = {
        "url": url,
        "status_code": 0,
        "is_static_page": is_static_page,
        "title": "",
        "title_length": 0,
        "meta_description": "",
        "meta_desc_length": 0,
        "canonical": "",
        "h1_count": 0,
        "h1_tags": [],
        "h2_count": 0,
        "word_count": 0,
        "images_total": 0,
        "images_missing_alt": 0,
        "has_article_schema": False,
        "has_website_schema": False,
        "flags": []
    }

    try:
        res = requests.get(url, headers=HEADERS, timeout=12)
        result["status_code"] = res.status_code

        if res.status_code != 200:
            result["flags"].append(f"HTTP_{res.status_code}")
            return result

        soup = BeautifulSoup(res.text, "html.parser")

        # 1. Title
        title_tag = soup.find("title")
        if title_tag and title_tag.string:
            result["title"] = title_tag.string.strip()
            result["title_length"] = len(result["title"])
            if "aaaa" in result["title"].lower():
                result["flags"].append("TEST_JUNK_PAGE")
        else:
            result["flags"].append("MISSING_TITLE")

        # 2. Meta Description
        meta_desc = soup.find("meta", attrs={"name": "description"})
        if meta_desc and meta_desc.get("content"):
            result["meta_description"] = meta_desc["content"].strip()
            result["meta_desc_length"] = len(result["meta_description"])
            if result["meta_desc_length"] < 60:
                result["flags"].append("SHORT_META_DESCRIPTION")
        else:
            result["flags"].append("MISSING_META_DESCRIPTION")

        # 3. Canonical
        canonical_tag = soup.find("link", attrs={"rel": "canonical"})
        if canonical_tag:
            result["canonical"] = canonical_tag.get("href", "")

        # 4. Headings
        h1s = [h.get_text().strip() for h in soup.find_all("h1") if h.get_text().strip()]
        result["h1_count"] = len(h1s)
        result["h1_tags"] = h1s[:2]
        if result["h1_count"] == 0:
            result["flags"].append("MISSING_H1")
        elif result["h1_count"] > 1:
            result["flags"].append("MULTIPLE_H1")

        h2s = [h.get_text().strip() for h in soup.find_all("h2") if h.get_text().strip()]
        result["h2_count"] = len(h2s)
        if not is_static_page and result["h2_count"] == 0:
            result["flags"].append("MISSING_H2")

        # 5. Content Word Count
        # Extract main post body
        post_body = soup.find("div", class_=re.compile(r"post-body|entry-content", re.I))
        if post_body:
            text = post_body.get_text(separator=" ", strip=True)
        else:
            # fallback to whole body
            body = soup.find("body")
            text = body.get_text(separator=" ", strip=True) if body else ""

        words = [w for w in text.split() if len(w) > 1]
        result["word_count"] = len(words)

        if not is_static_page:
            if result["word_count"] < 400:
                result["flags"].append("THIN_CONTENT_CRITICAL (<400 words)")
            elif result["word_count"] < 800:
                result["flags"].append("LOW_WORD_COUNT (<800 words)")

        # 6. Images & Alt text
        images = soup.find_all("img")
        result["images_total"] = len(images)
        missing_alt = 0
        for img in images:
            alt = img.get("alt", "")
            if not alt or not alt.strip():
                missing_alt += 1
        result["images_missing_alt"] = missing_alt
        if missing_alt > 0 and result["images_total"] > 0:
            result["flags"].append(f"MISSING_ALT_TAGS ({missing_alt}/{result['images_total']})")

        # 7. Schema Markup
        for script in soup.find_all("script", type="application/ld+json"):
            content = script.string or ""
            if "Article" in content or "BlogPosting" in content:
                result["has_article_schema"] = True
            if "WebSite" in content:
                result["has_website_schema"] = True

        if not is_static_page and not result["has_article_schema"]:
            result["flags"].append("MISSING_ARTICLE_SCHEMA")

        # Check slug for test junk
        if "/p/aaaa" in url or "test" in url:
            result["flags"].append("TEST_JUNK_PAGE")

    except Exception as e:
        result["status_code"] = 500
        result["flags"].append(f"CRAWL_ERROR: {str(e)}")

    return result


def generate_reports(results):
    """Generates JSON and formatted Markdown reports."""
    total_pages = len(results)
    successful = [r for r in results if r["status_code"] == 200]
    errors = [r for r in results if r["status_code"] != 200]
    junk_pages = [r for r in results if "TEST_JUNK_PAGE" in r["flags"]]
    thin_content = [r for r in results if any("THIN_CONTENT" in f for f in r["flags"])]
    missing_schema = [r for r in results if "MISSING_ARTICLE_SCHEMA" in r["flags"]]
    missing_h1 = [r for r in results if "MISSING_H1" in r["flags"] or "MULTIPLE_H1" in r["flags"]]

    # Calculate AdSense Readiness Score (0 - 100)
    score = 100
    if errors:
        score -= min(len(errors) * 5, 25)
    if junk_pages:
        score -= 20  # Having test/junk page is a huge penalty
    if thin_content:
        score -= min(len(thin_content) * 3, 20)
    if missing_schema:
        score -= 10
    score = max(score, 10)

    # Save JSON
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    # Save Markdown
    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write(f"# 📊 HelpTrickBD SEO & AdSense Audit Report\n\n")
        f.write(f"**Target Site:** `https://www.helptrickbd.com`  \n")
        f.write(f"**Audit Date:** {time.strftime('%Y-%m-%d %H:%M:%S')}  \n")
        f.write(f"**AdSense Readiness Score:** **`{score}/100`**  \n\n")

        f.write("## 🚨 Executive Summary & Critical Flags\n\n")
        if junk_pages:
            f.write(f"> [!CAUTION]\n> **Junk/Test Pages Detected:** Found {len(junk_pages)} incomplete test page(s) in sitemap (e.g. `{junk_pages[0]['url']}`). **Google AdSense immediately rejects sites with test/placeholder pages** as 'Under Construction' or 'Low Value Content'. These MUST be deleted from Blogger immediately!\n\n")
        if thin_content:
            f.write(f"> [!WARNING]\n> **Thin Content Alert:** {len(thin_content)} posts have fewer than 400 words. AdSense requires comprehensive, original content (minimum 800–1,200 words per post).\n\n")
        if missing_schema:
            f.write(f"> [!IMPORTANT]\n> **Missing Article Schema:** {len(missing_schema)} posts lack JSON-LD `BlogPosting`/`Article` schema markup. Currently, the theme only outputs basic `WebSite` schema, preventing Google from understanding article authors, dates, and rich snippets.\n\n")

        f.write("## 📈 Metrics Overview\n\n")
        f.write(f"| Metric | Value | Status |\n")
        f.write(f"| :--- | :--- | :--- |\n")
        f.write(f"| **Total Pages Crawled** | {total_pages} | Info |\n")
        f.write(f"| **HTTP 200 OK** | {len(successful)} | {'✅ Good' if len(successful) == total_pages else '⚠️ Fix Errors'} |\n")
        f.write(f"| **HTTP 404 / Errors** | {len(errors)} | {'✅ 0' if not errors else '❌ Critical'} |\n")
        f.write(f"| **Junk / Placeholder Pages** | {len(junk_pages)} | {'✅ Clean' if not junk_pages else '❌ Must Delete'} |\n")
        f.write(f"| **Thin Content (<400 words)** | {len(thin_content)} | {'✅ 0' if not thin_content else '⚠️ Expand'} |\n")
        f.write(f"| **Heading Hierarchy Issues** | {len(missing_h1)} | {'✅ Good' if not missing_h1 else '⚠️ Optimize'} |\n\n")

        f.write("## 📋 Detailed Page Issues\n\n")
        f.write("| URL | Status | Word Count | Issues / Flags |\n")
        f.write("| :--- | :---: | :---: | :--- |\n")
        for r in results:
            if r["flags"]:
                flags_str = ", ".join(r["flags"][:3])
                f.write(f"| [{r['url'].split('/')[-1]}]({r['url']}) | {r['status_code']} | {r['word_count']} | `{flags_str}` |\n")

        f.write("\n\n## 🛠️ Step-by-Step Action Items for 100% AdSense Approval\n\n")
        f.write("1. **Delete Test Pages in Blogger:** Delete `/p/aaaa_11.html` and any placeholder pages from Blogger > Pages.\n")
        f.write("2. **Expand Thin Posts:** Update articles with low word counts to at least 800+ words with step-by-step points and relevant headings.\n")
        f.write("3. **Inject Article Schema into Blogger Theme:** Paste the JSON-LD snippet provided in `templates/technical_seo/theme_schema_and_meta.xml` into your Theme XML `<head>`.\n")
        f.write("4. **Add Mandatory AdSense Pages:** Ensure the 5 legal pages in `templates/legal_pages/` are published and linked in the footer.\n")
        f.write("5. **Trigger Google Indexing:** Use `python tools/indexer/index_now.py` to get all updated posts crawled and re-indexed.\n")

    print(f"\n[OK] Audit Complete! Reports saved to:")
    print(f"    - {OUTPUT_MD}")
    print(f"    - {OUTPUT_JSON}")


def main():
    parser = argparse.ArgumentParser(description="SEO & AdSense Auditor for HelpTrickBD")
    parser.add_argument("--sitemap", default=DEFAULT_SITEMAP, help="URL of posts sitemap")
    parser.add_argument("--pages-sitemap", default=DEFAULT_PAGES_SITEMAP, help="URL of static pages sitemap")
    parser.add_argument("--limit", type=int, default=0, help="Limit number of pages to audit (0 = all)")
    args = parser.parse_args()

    print(f"\n{'='*60}")
    print("  HelpTrickBD SEO & AdSense Readiness Auditor")
    print(f"{'='*60}\n")

    post_urls = fetch_sitemap_urls(args.sitemap)
    page_urls = fetch_sitemap_urls(args.pages_sitemap)

    all_targets = [(u, False) for u in post_urls] + [(u, True) for u in page_urls]

    if args.limit > 0:
        all_targets = all_targets[:args.limit]

    print(f"[*] Found {len(post_urls)} posts and {len(page_urls)} static pages.")
    print(f"[*] Total URLs to audit: {len(all_targets)}\n")

    results = []
    for idx, (url, is_page) in enumerate(all_targets, 1):
        print(f"[{idx}/{len(all_targets)}] Auditing: {url.split('/')[-1] or url}")
        res = audit_page(url, is_static_page=is_page)
        results.append(res)
        time.sleep(0.3)

    generate_reports(results)


if __name__ == "__main__":
    main()
