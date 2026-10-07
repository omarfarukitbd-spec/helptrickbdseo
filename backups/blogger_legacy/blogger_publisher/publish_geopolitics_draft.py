#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/publish_geopolitics_draft.py
---------------------------------------------------
Publishes the Geopolitics Master Guide as a DRAFT in Blogger,
using the 2-step mint-and-revert protocol to guarantee that the English custom
permalink is permanently locked (Zero generic blog-post_xx.html).

Status in Blogger: DRAFT (Ready for user review before live publishing).
"""

import os
import sys
import json
import time

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID

HTML_PATH = os.path.join(PROJECT_ROOT, "output_posts", "geopolitics_master_guide_2026.html")
META_PATH = os.path.join(PROJECT_ROOT, "output_posts", "geopolitics_master_guide_2026_meta.json")


def main():
    print("=" * 72)
    print("  HELPTRICKBD DRAFT PUBLISHER: GEOPOLITICS MASTER GUIDE")
    print("=" * 72)

    with open(HTML_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    with open(META_PATH, "r", encoding="utf-8") as f:
        meta = json.load(f)

    slug = meta.get("slug", "geopolitics-definition-elements-nature-bangladesh-importance")
    bengali_title = meta.get("title", "")
    labels = meta.get("labels", ["Political Science", "Education Guide", "Job Study Article"])

    service = get_authenticated_service()
    if not service:
        print("[ERROR] Blogger API Authentication failed.")
        return

    print(f"[*] ধাপ ০১: কাস্টম পারমালিঙ্ক মিন্ট করা হচ্ছে...")
    print(f"    স্লাগ: {slug}")

    # Step 1: Mint custom permalink
    mint_body = {
        "kind": "blogger#post",
        "blog": {"id": BLOG_ID},
        "title": slug,
        "content": content,
        "labels": labels
    }

    res_mint = service.posts().insert(blogId=BLOG_ID, body=mint_body, isDraft=False).execute()
    post_id = res_mint.get("id")
    live_url = res_mint.get("url")

    print(f"[OK] পারমালিঙ্ক মিন্ট সফল!")
    print(f"    Post ID: {post_id}")
    print(f"    Permanent URL: {live_url}")

    time.sleep(2)

    # Step 2: Update Title to Bengali Title & Revert to Draft
    print(f"\n[*] ধাপ ০২: মূল বাংলা টাইটেল আপডেট ও ড্রাফটে রূপান্তর...")
    print(f"    বাংলা টাইটেল: {bengali_title}")

    update_body = {
        "title": bengali_title,
        "content": content,
        "labels": labels
    }

    res_update = service.posts().patch(blogId=BLOG_ID, postId=post_id, body=update_body).execute()
    print(f"[OK] বাংলা টাইটেল সফলভাবে আপডেট হয়েছে!")

    time.sleep(1)

    print(f"[*] ড্রাফটে রূপান্তর করা হচ্ছে (revert)...")
    res_revert = service.posts().revert(blogId=BLOG_ID, postId=post_id).execute()
    print(f"[OK] পোস্টটি সফলভাবে BLOGGER DRAFT-এ রাখা হয়েছে!")
    print(f"    স্ট্যাটাস: DRAFT (ইউজার রিভিউয়ের জন্য প্রস্তুত)")
    print("=" * 72)


if __name__ == "__main__":
    main()
