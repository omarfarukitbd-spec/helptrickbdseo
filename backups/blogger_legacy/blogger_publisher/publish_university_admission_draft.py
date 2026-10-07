#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/publish_university_admission_draft.py
-------------------------------------------------------------
Publishes the Public University Admission Guide 2026 as a DRAFT in Blogger,
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

HTML_PATH = os.path.join(PROJECT_ROOT, "output_posts", "public_university_admission_guide_2026.html")
META_PATH = os.path.join(PROJECT_ROOT, "output_posts", "public_university_admission_guide_2026_meta.json")


def main():
    print("=" * 72)
    print("  HELPTRICKBD DRAFT PUBLISHER: UNIVERSITY ADMISSION GUIDE 2026")
    print("=" * 72)

    with open(HTML_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    with open(META_PATH, "r", encoding="utf-8") as f:
        meta = json.load(f)

    slug = meta.get("slug", "public-university-admission-eligibility-guide-2026")
    bengali_title = meta.get("title", "")
    labels = meta.get("labels", ["Education", "Education Guide", "Study Guide"])

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
    post_url = res_mint.get("url")
    print(f"    [✔] পারমালিঙ্ক স্থায়ীভাবে মিন্ট হয়েছে: {post_url}")
    print(f"    [✔] পোস্ট আইডি: {post_id}")

    time.sleep(1.5)

    # Step 2: Update with authentic Bengali title
    print(f"\n[*] ধাপ ০২: খাঁটি বাংলা টাইটেল আপডেট করা হচ্ছে...")
    print(f"    টাইটেল: {bengali_title}")
    update_body = {
        "title": bengali_title,
        "content": content,
        "labels": labels
    }
    service.posts().patch(blogId=BLOG_ID, postId=post_id, body=update_body).execute()
    print("    [✔] টাইটেল সফলভাবে আপডেট হয়েছে।")

    time.sleep(1.5)

    # Step 3: Revert post to DRAFT for user review
    print(f"\n[*] ধাপ ০৩: পোস্টটি ড্রাফট (Draft) অবস্থায় রূপান্তর করা হচ্ছে...")
    res_revert = service.posts().revert(blogId=BLOG_ID, postId=post_id).execute()
    status = res_revert.get("status")
    print(f"    [✔] পোস্টের বর্তমান স্ট্যাটাস: {status} (ড্রাফট)")

    # Save to local record
    meta["post_id"] = post_id
    meta["status"] = status
    meta["minted_url"] = post_url
    meta["admin_edit_url"] = f"https://www.blogger.com/blog/post/edit/{BLOG_ID}/{post_id}"

    with open(META_PATH, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 72)
    print("  ড্রাফট সম্পন্ন রিপোর্ট")
    print("=" * 72)
    print(f"পোস্ট আইডি:       {post_id}")
    print(f"স্ট্যাটাস:          {status} (ড্রাফট)")
    print(f"স্থায়ী পারমালিঙ্ক:   {post_url}")
    print(f"এডমিন রিভিউ লিংক: {meta['admin_edit_url']}")
    print("=" * 72)


if __name__ == "__main__":
    main()
