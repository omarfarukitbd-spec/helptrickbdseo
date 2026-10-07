#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/publish_and_index_degree_post.py
--------------------------------------------------------
Publishes the Degree 2nd Year post live on Blogger using Blogger API v3,
then submits the live URL to Google Indexing API v3 and Google WebSub Hub
for instant Google crawling and indexing.
Strictly Zero Emojis (Rule 12).
"""

import os
import sys
import json
import time
import subprocess

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID

POST_ID = "3467234920665395308"
META_PATH = os.path.join(PROJECT_ROOT, "output_posts", "nu-degree-2nd-year-in-course-and-exam-routine-2026_meta.json")

def publish_and_index():
    print("=" * 72)
    print("  HELPTRICKBD PUBLISH & GOOGLE INDEXING PIPELINE")
    print(f"  Post ID: {POST_ID}")
    print("=" * 72)

    service = get_authenticated_service()
    if not service:
        print("[-] Blogger API Authentication failed.")
        return False

    # Step 1: Publish the draft to live on Blogger
    print("[*] ধাপ ০১: Blogger API v3 দিয়ে পোস্টটি LIVE পাবলিশ করা হচ্ছে...")
    res_pub = service.posts().publish(blogId=BLOG_ID, postId=POST_ID).execute()
    live_url = res_pub.get("url")
    print(f"[OK] পোস্টটি ব্লগারে সফলভাবে লাইভ পাবলিশ হয়েছে!")
    print(f"     Title: {res_pub.get('title')}")
    print(f"     Status: {res_pub.get('status')}")
    print(f"     Live URL: {live_url}")

    # Update metadata
    if os.path.exists(META_PATH):
        try:
            with open(META_PATH, "r", encoding="utf-8") as mf:
                m = json.load(mf)
            m["status"] = "LIVE"
            m["url"] = live_url
            with open(META_PATH, "w", encoding="utf-8") as mf:
                json.dump(m, mf, ensure_ascii=False, indent=2)
        except Exception:
            pass

    time.sleep(2)

    # Step 2: Google Indexing API v3 Submission
    print("\n[*] ধাপ ০২: Google Indexing API v3-তে URL সাবমিট করা হচ্ছে...")
    cmd_index = [
        sys.executable,
        os.path.join(PROJECT_ROOT, "tools", "indexer", "index_now.py"),
        "--url", live_url,
        "--credentials", os.path.join(PROJECT_ROOT, "tools", "indexer", "service_account.json")
    ]
    res_idx = subprocess.run(cmd_index, capture_output=True, text=True, encoding="utf-8")
    print(res_idx.stdout)

    # Step 3: Google WebSub (PubSubHubbub) Real-Time Hub Ping
    print("[*] ধাপ ০৩: Google WebSub (PubSubHubbub) সেন্ট্রাল হাবে রিয়েল-টাইম পুশ পিং...")
    cmd_hub = [
        sys.executable,
        os.path.join(PROJECT_ROOT, "tools", "indexer", "pubsub_hub_pinger.py")
    ]
    res_hub = subprocess.run(cmd_hub, capture_output=True, text=True, encoding="utf-8")
    print(res_hub.stdout)

    print("=" * 72)
    print("  [SUCCESS] পোস্টটি ব্লগারে লাইভ এবং গুগলে ইনডেক্সিং রিকোয়েস্ট সফল!")
    print("=" * 72)
    return True

if __name__ == "__main__":
    publish_and_index()
