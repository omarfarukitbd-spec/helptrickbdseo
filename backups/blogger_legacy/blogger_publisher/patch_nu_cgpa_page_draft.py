#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/patch_nu_cgpa_page_draft.py
----------------------------------------------------
Updates the content of the NU CGPA Calculator Page (Draft) in Blogger.
"""

import os
import sys
import json

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID

PAGE_ID = "6328665612127487727"
HTML_PATH = os.path.join(PROJECT_ROOT, "output_pages", "nu-cgpa-calculator.html")
META_PATH = os.path.join(PROJECT_ROOT, "output_pages", "nu-cgpa-calculator_meta.json")

def main():
    service = get_authenticated_service()
    if not service:
        print("[ERROR] Auth failed")
        return False

    with open(HTML_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    with open(META_PATH, "r", encoding="utf-8") as f:
        meta = json.load(f)

    bengali_title = meta.get("title", "জাতীয় বিশ্ববিদ্যালয় সিজিপিএ ক্যালকুলেটর ও গ্রেডিং গাইড ২০২৬")

    print(f"[*] Patching Draft Page ID: {PAGE_ID} ...")
    body = {
        "title": bengali_title,
        "content": content
    }

    res = service.pages().patch(blogId=BLOG_ID, pageId=PAGE_ID, body=body).execute()
    print("[SUCCESS] Page updated successfully!")
    print(f"    Page ID: {res.get('id')}")
    print(f"    Title: {res.get('title')}")
    print(f"    Status: {res.get('status')}")
    print(f"    URL: {res.get('url')}")

    meta["page_id"] = PAGE_ID
    meta["url"] = res.get("url")
    with open(META_PATH, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    return True

if __name__ == "__main__":
    main()
