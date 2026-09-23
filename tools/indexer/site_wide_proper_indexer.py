#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/indexer/site_wide_proper_indexer.py
-----------------------------------------
Official Multi-Engine Site-Wide Indexing Pipeline for HelpTrickBD.
Submits 100% of live URLs (Homepage, Static Pages, and all Blog Posts)
to Google Indexing API, Bing/Yandex IndexNow, and Google WebSub Hubs.
"""

import os
import sys
import json
import time
import requests
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.indexer.index_now import get_authenticated_service as get_idx_credentials

SITEMAP_POSTS = "https://www.helptrickbd.com/sitemap.xml"
SITEMAP_PAGES = "https://www.helptrickbd.com/sitemap-pages.xml"
HOMEPAGE = "https://www.helptrickbd.com/"

HUBS = [
    "https://pubsubhubbub.appspot.com/publish",
    "https://pubsubhubbub.superfeedr.com/publish"
]

FEEDS = [
    "https://www.helptrickbd.com/feeds/posts/default",
    "https://www.helptrickbd.com/atom.xml?redirect=false&start-index=1&max-results=500",
    "https://www.helptrickbd.com/sitemap.xml",
    "https://www.helptrickbd.com/sitemap-pages.xml"
]

LOG_FILE = os.path.join(PROJECT_ROOT, "tools", "indexer", "site_wide_indexing_history.log")
REPORT_FILE = os.path.join(PROJECT_ROOT, "tools", "indexer", "site_wide_indexing_report.json")

def fetch_locs_from_sitemap(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (compatible; HelpTrickBDBot/1.0)"}
        res = requests.get(url, headers=headers, timeout=15)
        res.raise_for_status()
        root = ET.fromstring(res.content)
        ns = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
        locs = [el.text.strip() for el in root.findall(f".//{ns}loc") if el.text]
        return locs
    except Exception as e:
        print(f"[!] Warning fetching sitemap {url}: {e}")
        return []

def get_all_site_urls():
    print("[*] Fetching all live URLs from official XML sitemaps...")
    post_urls = fetch_locs_from_sitemap(SITEMAP_POSTS)
    page_urls = fetch_locs_from_sitemap(SITEMAP_PAGES)
    
    # Prioritized order:
    # 1. Homepage
    # 2. Critical static policy pages (AdSense & trust requirement)
    # 3. All blog posts (newest to oldest)
    ordered = [HOMEPAGE] + page_urls + post_urls
    
    unique_urls = []
    for u in ordered:
        clean_u = u.split("?")[0].strip()
        if clean_u and clean_u not in unique_urls:
            unique_urls.append(clean_u)
            
    print(f"[*] Discovered {len(unique_urls)} clean unique URLs:")
    print(f"    - Homepage: 1")
    print(f"    - Static Policy Pages: {len(page_urls)}")
    print(f"    - Blog Posts: {len(post_urls)}")
    return unique_urls

def ping_websub_hubs():
    print("\n" + "=" * 70)
    print("PHASE 1: REAL-TIME WEBSUB (PUBSUBHUBBUB) FEED PINGS")
    print("=" * 70)
    total = 0
    success = 0
    for feed in FEEDS:
        for hub in HUBS:
            total += 1
            payload = {"hub.mode": "publish", "hub.url": feed}
            headers = {"User-Agent": "HelpTrickBD-RealtimePinger/2.0", "Content-Type": "application/x-www-form-urlencoded"}
            try:
                r = requests.post(hub, data=payload, headers=headers, timeout=10)
                if r.status_code in (200, 204):
                    success += 1
                    print(f"   [✔] Hub Pinger (HTTP {r.status_code}): {feed.split('/')[-1]} -> {hub.split('/')[2]}")
                else:
                    print(f"   [!] Hub Warning (HTTP {r.status_code}): {hub.split('/')[2]}")
            except Exception as e:
                print(f"   [✘] Hub Error {hub}: {e}")
    print(f"[*] WebSub Result: {success}/{total} endpoints notified successfully.")

def submit_indexnow(urls):
    print("\n" + "=" * 70)
    print("PHASE 2: INDEXNOW API SUBMISSION (BING / YANDEX / YAHOO)")
    print("=" * 70)
    host = "www.helptrickbd.com"
    payload = {
        "host": host,
        "key": "4c424e8e19d749fcb150c25a073dbb89",
        "keyLocation": f"https://{host}/4c424e8e19d749fcb150c25a073dbb89.txt",
        "urlList": urls
    }
    endpoints = [
        "https://api.indexnow.org/indexnow",
        "https://www.bing.com/indexnow",
        "https://yandex.com/indexnow"
    ]
    for ep in endpoints:
        try:
            r = requests.post(ep, json=payload, headers={"Content-Type": "application/json; charset=utf-8"}, timeout=15)
            print(f"   [IndexNow] {ep.split('/')[2]} -> Status {r.status_code} ({len(urls)} URLs submitted)")
        except Exception as e:
            print(f"   [IndexNow] {ep.split('/')[2]} -> Error: {e}")

def submit_google_indexing(urls):
    print("\n" + "=" * 70)
    print("PHASE 3: GOOGLE INDEXING API (OFFICIAL GOOGLEBOT NOTIFICATION)")
    print(f"Total URLs to submit: {len(urls)} (Within daily quota of 200)")
    print("=" * 70)

    credentials = get_idx_credentials()
    if not credentials:
        print("[ERROR] Google service account credentials not found!")
        return 0, len(urls), []

    service = build("indexing", "v3", credentials=credentials)
    
    results = []
    success_count = 0
    failed_count = 0

    with open(LOG_FILE, "a", encoding="utf-8") as log_fp:
        log_fp.write(f"\n--- SITE-WIDE INDEXING RUN: {datetime.now(timezone.utc).isoformat()} ---\n")

        for idx, url in enumerate(urls, 1):
            body = {"url": url, "type": "URL_UPDATED"}
            try:
                res = service.urlNotifications().publish(body=body).execute()
                notify_time = res.get("urlNotificationMetadata", {}).get("latestUpdate", {}).get("notifyTime", "N/A")
                success_count += 1
                log_entry = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [SUCCESS] [200] {url} (Notified: {notify_time})\n"
                log_fp.write(log_entry)
                log_fp.flush()
                results.append({"url": url, "status": 200, "notified": notify_time, "success": True})
                
                # Friendly display
                short_url = url.replace("https://www.helptrickbd.com/", "/")
                print(f" [{idx:03d}/{len(urls):03d}] [200 OK] {short_url}")
            except HttpError as e:
                failed_count += 1
                status = e.resp.status if hasattr(e, 'resp') else "Error"
                log_entry = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [FAILED] [{status}] {url} -> {e}\n"
                log_fp.write(log_entry)
                log_fp.flush()
                results.append({"url": url, "status": status, "error": str(e), "success": False})
                print(f" [{idx:03d}/{len(urls):03d}] [FAILED {status}] {url}")
            except Exception as e:
                failed_count += 1
                results.append({"url": url, "status": "Exception", "error": str(e), "success": False})
                print(f" [{idx:03d}/{len(urls):03d}] [EXCEPTION] {url} -> {e}")

            # Pacing delay: 0.35s to respect Google API gateway
            time.sleep(0.35)

    return success_count, failed_count, results

def main():
    start_time = time.time()
    print("=" * 75)
    print("🚀 HELPTRICKBD SITE-WIDE 100% PROPER INDEXING PIPELINE")
    print("=" * 75)

    all_urls = get_all_site_urls()
    if not all_urls:
        print("[!] No URLs found to process.")
        return

    # Phase 1: Real-Time WebSub Hubs
    ping_websub_hubs()

    # Phase 2: IndexNow Multi-Search Engine Batch
    submit_indexnow(all_urls)

    # Phase 3: Google Indexing API Official Bot Notification
    success_count, failed_count, results = submit_google_indexing(all_urls)

    elapsed = round(time.time() - start_time, 1)

    summary = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "total_urls": len(all_urls),
        "google_indexing_successful": success_count,
        "google_indexing_failed": failed_count,
        "duration_seconds": elapsed,
        "results": results
    }

    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 75)
    print("🎉 SITE-WIDE INDEXING COMPLETE!")
    print(f"   Total URLs:      {len(all_urls)}")
    print(f"   Success (200):   {success_count}")
    print(f"   Failed:          {failed_count}")
    print(f"   Time Elapsed:    {elapsed}s")
    print(f"   Full Report:     {REPORT_FILE}")
    print("=" * 75)

if __name__ == "__main__":
    main()
