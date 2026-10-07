#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/publish_nu_cgpa_page_live.py
------------------------------------------------------
Makes the existing NU CGPA Calculator draft page LIVE on Blogger.
Page ID: 6328665612127487727
URL: https://www.helptrickbd.com/p/nu-cgpa-calculator.html
"""

import os
import sys
import json

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID

PAGE_ID       = "6328665612127487727"
HTML_PATH     = os.path.join(PROJECT_ROOT, "output_pages", "nu-cgpa-calculator.html")
META_PATH     = os.path.join(PROJECT_ROOT, "output_pages", "nu-cgpa-calculator_meta.json")
LIVE_URL      = "https://www.helptrickbd.com/p/nu-cgpa-calculator.html"

def main():
    print("=" * 70)
    print("  NU CGPA CALCULATOR: DRAFT → LIVE PUBLISHER")
    print("=" * 70)

    # Load latest content
    with open(HTML_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    with open(META_PATH, "r", encoding="utf-8") as f:
        meta = json.load(f)

    bengali_title = meta.get("title", "জাতীয় বিশ্ববিদ্যালয় সিজিপিএ ক্যালকুলেটর ও গ্রেডিং গাইড ২০২৬")

    service = get_authenticated_service()
    if not service:
        print("[ERROR] Blogger API Authentication failed.")
        return False

    print(f"[*] Page ID   : {PAGE_ID}")
    print(f"[*] Target URL: {LIVE_URL}")
    print(f"[*] Publishing LIVE now...")

    # Publish the page (isDraft=False makes it LIVE)
    try:
        res = service.pages().publish(blogId=BLOG_ID, pageId=PAGE_ID).execute()
        status = res.get("status", "unknown")
        url    = res.get("url", LIVE_URL)
        print(f"\n[SUCCESS] Page is now LIVE!")
        print(f"    Status : {status}")
        print(f"    URL    : {url}")
        print(f"    Title  : {res.get('title', bengali_title)}")
    except Exception as e:
        # If publish endpoint not available, try patch with isDraft=False
        print(f"[!] publish() failed ({e}), trying patch with isDraft=False...")
        body = {
            "title"  : bengali_title,
            "content": content,
            "status" : "LIVE"
        }
        res = service.pages().patch(
            blogId=BLOG_ID, pageId=PAGE_ID,
            body=body, publish=True
        ).execute()
        status = res.get("status", "unknown")
        url    = res.get("url", LIVE_URL)
        print(f"\n[SUCCESS] Page status updated to LIVE!")
        print(f"    Status : {status}")
        print(f"    URL    : {url}")

    # Update meta
    meta["status"] = "live"
    meta["url"]    = url
    with open(META_PATH, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    print("=" * 70)
    return True

if __name__ == "__main__":
    main()
