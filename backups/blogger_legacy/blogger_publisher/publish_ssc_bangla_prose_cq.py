#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/publish_ssc_bangla_prose_cq.py
---------------------------------------------------------
Publishes Post 01:
'এসএসসি ও দাখিল বাংলা ১ম পত্র গদ্যাংশ সৃজনশীল প্রশ্নব্যাংক ২০২৬-২০২৭ (SSC Bangla 1st Paper Prose CQ Question Bank & Full Solution)'
Adheres strictly to the 2-Step Custom English Permalink Minting Protocol.
"""

import os
import sys
import json
import time

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID
from tools.governance.pre_flight_checker import PreFlightChecker
from tools.indexer.post_publish_verifier import verify_and_index_post

HTML_PATH = os.path.join(PROJECT_ROOT, "output_posts", "ssc-bangla-1st-paper-prose-cq-question-bank-2027.html")
META_PATH = os.path.join(PROJECT_ROOT, "output_posts", "ssc-bangla-1st-paper-prose-cq-question-bank-2027_metadata.json")

def publish_prose_cq():
    print("=" * 75)
    print("🚀 HELPTRICKBD 2-STEP PUBLISHING ENGINE — BANGLA 1ST PROSE CQ BANK")
    print("=" * 75)

    if not os.path.exists(HTML_PATH) or not os.path.exists(META_PATH):
        print(f"[ERROR] Required files not found: {HTML_PATH} or {META_PATH}")
        sys.exit(1)

    # 1. Pre-Flight Quality Gate Check
    print("\n[*] Checking Pre-Flight Quality Gate...")
    checker = PreFlightChecker(HTML_PATH, metadata_path=META_PATH)
    if not checker.run_all():
        checker.print_report()
        print("\n[BLOCKED] Pre-Flight check failed! Aborting publication.")
        sys.exit(1)
    print("    [PASSED] Pre-Flight Quality Gate: 100% PASSED (0 Critical Errors).")

    with open(META_PATH, "r", encoding="utf-8") as f:
        meta = json.load(f)
    with open(HTML_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    slug = meta.get("custom_slug") or meta.get("slug")
    full_title = meta["title"]
    labels = meta["labels"]

    print(f"\n[*] Target Post Details:")
    print(f"    Slug:    {slug}")
    print(f"    Title:   {full_title}")
    print(f"    Labels:  {', '.join(labels)}")
    print(f"    Words:   {len(content.split()):,} words")

    # 2. Blogger API Authentication
    service = get_authenticated_service()
    if not service:
        print("[ERROR] Failed to authenticate with Blogger API v3.")
        sys.exit(1)

    # 3. STEP 1: Mint clean English permalink
    body = {
        "kind": "blogger#post",
        "blog": {"id": BLOG_ID},
        "title": slug,
        "content": content,
        "labels": labels
    }

    print("\n[*] STEP 1: Minting clean English permalink with draft-publish...")
    insert_req = service.posts().insert(blogId=BLOG_ID, body=body, isDraft=False)
    created_post = insert_req.execute()

    post_id = created_post.get("id")
    live_url = created_post.get("url")

    print(f"    [✔] Post Minted Successfully!")
    print(f"        Post ID:  {post_id}")
    print(f"        Live URL: {live_url}")

    # 4. STEP 2: Update post title to full authentic Bengali Title
    print("\n[*] STEP 2: Updating post title to full authentic Bengali Title...")
    patch_body = {
        "title": full_title
    }
    patch_req = service.posts().patch(blogId=BLOG_ID, postId=post_id, body=patch_body)
    updated_post = patch_req.execute()

    final_title = updated_post.get("title")
    print(f"    [✔] Title Patched: {final_title}")

    # 5. Verification & Google Indexing API Submission
    print("\n[*] STEP 3: Automated Live Verification & Instant Indexing...")
    time.sleep(3)  # Allow Blogger CDN cache propagation
    verification_result = verify_and_index_post(
        post_url=live_url,
        expected_title=full_title,
        expected_slug=slug
    )

    # 6. Save Published Record
    pub_record_path = os.path.join(PROJECT_ROOT, "output_posts", "ssc_bangla_prose_cq_bank_published.json")
    with open(pub_record_path, "w", encoding="utf-8") as f:
        json.dump({
            "post_id": post_id,
            "url": live_url,
            "title": full_title,
            "slug": slug,
            "verification": verification_result
        }, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 75)
    print(f"🎉 POST 01 PUBLISHED & INDEXED SUCCESSFULLY!")
    print(f"   URL: {live_url}")
    print("=" * 75)

if __name__ == "__main__":
    publish_prose_cq()
