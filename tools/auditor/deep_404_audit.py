#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/auditor/deep_404_audit.py
--------------------------------
Comprehensive 404 Error Auditor for Helptrickbd.com (WordPress 6.7+)

Audits:
1. XML Sitemaps (post-sitemap, page-sitemap, category-sitemap)
2. All live post URLs (HTTP Status Codes)
3. Core pages (Home, About, Contact, Privacy Policy, Terms, Disclaimer)
4. 301 Redirect integrity for legacy Blogger URLs (.html permalinks)
5. Internal link crawling for broken destinations (404s)

Strictly zero emojis (Rule 12).
"""

import os
import sys
import json
import time
import requests
import xml.etree.ElementTree as ET
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 (HelpTrickBD 404 Auditor/2.0)"
}

SITEMAP_INDEX = "https://www.helptrickbd.com/sitemap_index.xml"
FALLBACK_SITEMAPS = [
    "https://www.helptrickbd.com/post-sitemap.xml",
    "https://www.helptrickbd.com/page-sitemap.xml",
    "https://www.helptrickbd.com/category-sitemap.xml",
    "https://www.helptrickbd.com/wp-sitemap.xml"
]

CORE_PAGES = [
    "https://www.helptrickbd.com/",
    "https://www.helptrickbd.com/about/",
    "https://www.helptrickbd.com/about-us/",
    "https://www.helptrickbd.com/contact/",
    "https://www.helptrickbd.com/contact-us/",
    "https://www.helptrickbd.com/privacy-policy/",
    "https://www.helptrickbd.com/terms-and-conditions/",
    "https://www.helptrickbd.com/disclaimer/"
]


def fetch_sitemap_urls(sitemap_url):
    """Fetches URLs from XML sitemap (handles sitemap index and sub-sitemaps)."""
    urls = []
    try:
        res = requests.get(sitemap_url, headers=HEADERS, timeout=15)
        if res.status_code != 200:
            return urls
        root = ET.fromstring(res.content)
        ns = ""
        if root.tag.startswith("{"):
            ns = root.tag.split("}")[0] + "}"
            
        # Check if sitemap index (contains other sitemaps)
        sub_sitemaps = root.findall(f".//{ns}sitemap/{ns}loc")
        if sub_sitemaps:
            for s in sub_sitemaps:
                sub_url = s.text.strip()
                urls.extend(fetch_sitemap_urls(sub_url))
        else:
            # Regular sitemap containing URLs
            for loc in root.findall(f".//{ns}url/{ns}loc"):
                if loc.text:
                    urls.append(loc.text.strip())
    except Exception as e:
        print(f"[-] Sitemap fetch failed for {sitemap_url}: {e}")
    return list(dict.fromkeys(urls))


def check_url(url, allow_redirects=True):
    """Checks a single URL and returns status, final_url, redirect_count, error."""
    try:
        res = requests.get(url, headers=HEADERS, timeout=12, allow_redirects=allow_redirects)
        return {
            "url": url,
            "status_code": res.status_code,
            "final_url": res.url,
            "redirect_history": [r.status_code for r in res.history],
            "ok": (200 <= res.status_code < 400),
            "is_404": (res.status_code == 404),
            "error": None
        }
    except Exception as e:
        return {
            "url": url,
            "status_code": 0,
            "final_url": url,
            "redirect_history": [],
            "ok": False,
            "is_404": False,
            "error": str(e)
        }


def extract_internal_links(page_url):
    """Fetches a page and extracts all internal links."""
    links = set()
    try:
        res = requests.get(page_url, headers=HEADERS, timeout=12)
        if res.status_code != 200:
            return []
        soup = BeautifulSoup(res.text, "html.parser")
        domain = "helptrickbd.com"
        for a in soup.find_all("a", href=True):
            href = a["href"].strip()
            if not href or href.startswith("#") or href.startswith("mailto:") or href.startswith("tel:"):
                continue
            full_url = urljoin(page_url, href)
            parsed = urlparse(full_url)
            if domain in parsed.netloc:
                clean_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
                if clean_url.endswith("/") or "." not in os.path.basename(clean_url):
                    links.add(clean_url)
    except Exception:
        pass
    return list(links)


def run_audit():
    print("=" * 72)
    print("  HELPTRICKBD 360-DEGREE 404 ERROR AUDITOR")
    print(f"  Target: https://www.helptrickbd.com/")
    print(f"  Start Time: {time.strftime('%Y-%m-%d %I:%M:%S %p')}")
    print("=" * 72)

    # Step 1: Collect URLs from Sitemaps
    print("\n[*] Step 1: Collecting URLs from XML Sitemaps...")
    all_sitemap_urls = fetch_sitemap_urls(SITEMAP_INDEX)
    if not all_sitemap_urls:
        for sm in FALLBACK_SITEMAPS:
            urls = fetch_sitemap_urls(sm)
            all_sitemap_urls.extend(urls)
    all_sitemap_urls = list(dict.fromkeys(all_sitemap_urls))
    print(f"[+] Total URLs found from Sitemaps: {len(all_sitemap_urls)}")

    # Step 2: Load known post URLs from migration_log.json
    print("\n[*] Step 2: Loading posts from migration catalog...")
    mig_path = os.path.join(PROJECT_ROOT, "Helptrickbd Wp", "migration_log.json")
    catalog_urls = []
    legacy_blogger_urls = []
    if os.path.exists(mig_path):
        try:
            with open(mig_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for p in data.get("posts", []):
                    slug = p.get("slug", "").strip()
                    if slug:
                        wp_url = f"https://www.helptrickbd.com/{slug}/"
                        catalog_urls.append(wp_url)
                    
                    old_path = p.get("old_path") or p.get("blogger_path") or ""
                    if old_path:
                        legacy_url = f"https://www.helptrickbd.com{old_path}"
                        legacy_blogger_urls.append((legacy_url, wp_url))
        except Exception as e:
            print(f"[-] Catalog load error: {e}")
    print(f"[+] Total catalog post URLs: {len(catalog_urls)}")

    # Combine all live candidate URLs to test
    target_urls = list(dict.fromkeys(CORE_PAGES + all_sitemap_urls + catalog_urls))
    print(f"[+] Unique URLs queued for 404 HTTP check: {len(target_urls)}")

    # Step 3: Run concurrent HTTP status checks
    print(f"\n[*] Step 3: Scanning {len(target_urls)} URLs for 404 or dead link responses...")
    results = []
    broken_404s = []
    redirect_chain = []
    errors = []

    with ThreadPoolExecutor(max_workers=8) as executor:
        future_map = {executor.submit(check_url, u): u for u in target_urls}
        completed = 0
        for future in as_completed(future_map):
            completed += 1
            res = future.result()
            results.append(res)
            if completed % 20 == 0 or completed == len(target_urls):
                print(f"    Progress: {completed}/{len(target_urls)} ({int(completed/len(target_urls)*100)}%) checked...")

            if res["status_code"] == 404:
                broken_404s.append(res)
            elif res["status_code"] >= 400:
                errors.append(res)
            elif res["redirect_history"]:
                redirect_chain.append(res)

    # Step 4: Test Legacy Blogger URLs for 301 Redirect vs 404
    print("\n[*] Step 4: Testing Legacy Blogger URLs for 301 Redirection integrity...")
    blogger_404s = []
    blogger_success = []
    sample_blogger = legacy_blogger_urls[:15] if legacy_blogger_urls else []
    
    # Also add standard test date-based URLs if none in catalog
    if not sample_blogger:
        for p in catalog_urls[:10]:
            slug = p.strip("/").split("/")[-1]
            fake_old = f"https://www.helptrickbd.com/2026/08/{slug}.html"
            sample_blogger.append((fake_old, p))

    for old_u, expected_new in sample_blogger:
        chk = check_url(old_u, allow_redirects=True)
        if chk["status_code"] == 404:
            blogger_404s.append(chk)
        elif chk["ok"]:
            blogger_success.append(chk)

    # Step 5: Check Internal Links on Key Sample Pages
    print("\n[*] Step 5: Extracting and validating in-content internal links on top 5 posts...")
    internal_sample_posts = [u for u in catalog_urls if u != "https://www.helptrickbd.com/"][:5]
    checked_in_links = set()
    internal_404s = []

    for post_url in internal_sample_posts:
        in_links = extract_internal_links(post_url)
        for link in in_links:
            if link not in checked_in_links:
                checked_in_links.add(link)
                link_chk = check_url(link)
                if link_chk["status_code"] == 404:
                    internal_404s.append({"source_page": post_url, "broken_link": link})

    # Summary Report
    print("\n" + "=" * 72)
    print("  AUDIT SUMMARY RESULTS")
    print("=" * 72)
    print(f"Total Live URLs Audited   : {len(results)}")
    print(f"Total 404 Broken Errors   : {len(broken_404s)}")
    print(f"Other HTTP Errors (>=400) : {len(errors)}")
    print(f"Successful URLs (200 OK)  : {len([r for r in results if r['status_code'] == 200])}")
    print(f"Redirected URLs (301/302) : {len(redirect_chain)}")
    print(f"Blogger Redirect 404s     : {len(blogger_404s)}")
    print(f"In-Page Internal 404s     : {len(internal_404s)}")
    print("-" * 72)

    if broken_404s:
        print("[!] 404 URLs Detected:")
        for b in broken_404s:
            print(f"  • {b['url']} -> HTTP {b['status_code']}")
    else:
        print("[OK] ZERO 404 errors detected across all tested live sitemap & post URLs!")

    if internal_404s:
        print("\n[!] Broken In-Page Internal Links:")
        for item in internal_404s:
            print(f"  • Source: {item['source_page']}")
            print(f"    Dead Link: {item['broken_link']}")

    # Save JSON report
    report_data = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "total_audited": len(results),
        "total_404": len(broken_404s),
        "broken_404_urls": broken_404s,
        "other_errors": errors,
        "redirected_urls": len(redirect_chain),
        "blogger_redirect_404s": blogger_404s,
        "internal_broken_links": internal_404s
    }
    out_file = os.path.join(PROJECT_ROOT, "scratch", "404_audit_report.json")
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(report_data, f, ensure_ascii=False, indent=2)
    print(f"\n[+] Detailed JSON report saved: scratch/404_audit_report.json")
    return report_data


if __name__ == "__main__":
    run_audit()
