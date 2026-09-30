#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/update_nu_honours_routine_draft.py
----------------------------------------------------------
Updates the existing Blogger DRAFT post (Post ID: 1085826635177863206)
with the comprehensive 18-department routine guide.
Ensures status remains DRAFT.
"""

import os
import sys
import json

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID

HTML_PATH = os.path.join(PROJECT_ROOT, "output_posts", "nu-honours-2nd-year-exam-routine-2026.html")
META_PATH = os.path.join(PROJECT_ROOT, "output_posts", "nu-honours-2nd-year-exam-routine-2026_meta.json")
POST_ID = "1085826635177863206"


def update_draft():
    print("=" * 72)
    print("  HELPTRICKBD DRAFT UPDATER: NU HONOURS 2ND YEAR ROUTINE 2026")
    print("=" * 72)

    with open(HTML_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    with open(META_PATH, "r", encoding="utf-8") as f:
        meta = json.load(f)

    bengali_title = meta.get("title", "")
    labels = meta.get("labels", ["জাতীয় বিশ্ববিদ্যালয়", "অনার্স রুটিন", "এডুকেশন নোটিশ"])

    service = get_authenticated_service()
    if not service:
        print("[ERROR] Authentication failed.")
        return False

    update_body = {
        "title": bengali_title,
        "content": content,
        "labels": labels
    }

    print(f"[*] Patching Post ID: {POST_ID}...")
    res = service.posts().patch(blogId=BLOG_ID, postId=POST_ID, body=update_body).execute()

    print("[SUCCESS] Blogger Draft successfully updated!")
    print(f"          Post ID: {res.get('id')}")
    print(f"          Title: {res.get('title')}")
    print(f"          Status: {res.get('status')}")
    print(f"          Permanent URL: {res.get('url')}")
    print("=" * 72)
    return True


if __name__ == "__main__":
    update_draft()
