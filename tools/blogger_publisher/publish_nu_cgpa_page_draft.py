#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/publish_nu_cgpa_page_draft.py
------------------------------------------------------
Publishes the National University (NU) CGPA Calculator Master Tool
as a DRAFT Static Page in Blogger using the 2-step minting protocol
to guarantee that the URL is locked at:
https://www.helptrickbd.com/p/nu-cgpa-calculator.html

Status in Blogger: DRAFT (Zero live publishing without explicit user permission).
"""

import os
import sys
import json
import time

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID

HTML_PATH = os.path.join(PROJECT_ROOT, "output_pages", "nu-cgpa-calculator.html")
META_PATH = os.path.join(PROJECT_ROOT, "output_pages", "nu-cgpa-calculator_meta.json")

def main():
    print("=" * 72)
    print("  HELPTRICKBD DRAFT PAGE PUBLISHER: NU CGPA CALCULATOR 2026")
    print("=" * 72)

    if not os.path.exists(HTML_PATH) or not os.path.exists(META_PATH):
        print(f"[ERROR] Missing files: {HTML_PATH} or {META_PATH}")
        return False

    with open(HTML_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    with open(META_PATH, "r", encoding="utf-8") as f:
        meta = json.load(f)

    slug = meta.get("english_slug", "nu-cgpa-calculator")
    bengali_title = meta.get("title", "জাতীয় বিশ্ববিদ্যালয় সিজিপিএ ক্যালকুলেটর ও গ্রেডিং গাইড ২০২৬")

    service = get_authenticated_service()
    if not service:
        print("[ERROR] Blogger API Authentication failed.")
        return False

    print(f"[*] ধাপ ০১: পেজ কাস্টম পারমালিঙ্ক মিন্ট করা হচ্ছে...")
    print(f"    স্লাগ: {slug}")

    # Step 1: Insert page as draft with slug as title to mint /p/nu-cgpa-calculator.html
    page_body = {
        "kind": "blogger#page",
        "blog": {"id": BLOG_ID},
        "title": slug,
        "content": content
    }

    res_mint = service.pages().insert(blogId=BLOG_ID, body=page_body, isDraft=True).execute()
    page_id = res_mint.get("id")
    page_url = res_mint.get("url")

    print(f"[OK] পেজ পারমালিঙ্ক মিন্ট সফল!")
    print(f"    Page ID: {page_id}")
    print(f"    Permanent URL: {page_url}")

    time.sleep(2)

    # Step 2: Update title to full Bengali title
    print(f"\n[*] ধাপ ০২: মূল বাংলা টাইটেল আপডেট...")
    print(f"    বাংলা টাইটেল: {bengali_title}")

    update_body = {
        "title": bengali_title,
        "content": content
    }

    res_update = service.pages().patch(blogId=BLOG_ID, pageId=page_id, body=update_body).execute()
    print(f"[OK] বাংলা টাইটেল সফলভাবে আপডেট হয়েছে!")
    print(f"    স্ট্যাটাস: DRAFT (ইউজার রিভিউয়ের জন্য প্রস্তুত)")
    print(f"    স্থায়ী পেজ ইউআরএল: {page_url}")

    # Update metadata
    meta["page_id"] = page_id
    meta["url"] = page_url
    meta["status"] = "draft"

    with open(META_PATH, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    print(f"[OK] মেটাডাটা ফাইল আপডেট সম্পন্ন: {META_PATH}")
    print("=" * 72)
    return True

if __name__ == "__main__":
    main()
