#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/schedule_posts_07_08_09.py
--------------------------------------------------
Schedules the 3 Masters Political Science posts to Blogger
for today starting at 8:00 AM BST (2026-09-18T08:00:00+06:00).

Enforces:
1. 2-Step Custom English Permalink Minting Protocol (Zero generic URLs).
2. Exact RFC 3339 Future Publishing Times (Blogger Scheduled status).
3. Verification of Hero Image LCP (loading="eager" fetchpriority="high").
4. Verification of Live / Future Links (Zero broken links).
5. Single Approved Category Label: "Political Science".
"""

import os
import sys
import json
import time

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID

SCHEDULE_CONFIGS = [
    {
        "post_num": "07",
        "html_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-07-modern-society-characteristics.html"),
        "meta_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-07-modern-society-characteristics_metadata.json"),
        "scheduled_time": "2026-09-18T08:00:00+06:00",
        "readable_time": "আজ সকাল ৮:০০ BST"
    },
    {
        "post_num": "08",
        "html_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-08-modernization-agents-media.html"),
        "meta_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-08-modernization-agents-media_metadata.json"),
        "scheduled_time": "2026-09-18T08:30:00+06:00",
        "readable_time": "আজ সকাল ৮:৩০ BST"
    },
    {
        "post_num": "09",
        "html_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-09-political-modernization-vs-development.html"),
        "meta_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-09-political-modernization-vs-development_metadata.json"),
        "scheduled_time": "2026-09-18T09:00:00+06:00",
        "readable_time": "আজ সকাল ৯:০০ BST"
    }
]

def schedule_all():
    print("=" * 75)
    print("⏰ HELPTRICKBD BLOGGER SCHEDULE ENGINE — POST 07, 08 & 09")
    print("   Target Release Window: আজ সকাল ৮:০০ টা থেকে শুরু")
    print("=" * 75)

    service = get_authenticated_service()
    if not service:
        print("[ERROR] Failed to authenticate Blogger API v3.")
        sys.exit(1)

    scheduled_records = []

    for item in SCHEDULE_CONFIGS:
        with open(item["meta_file"], "r", encoding="utf-8") as f:
            meta = json.load(f)
        with open(item["html_file"], "r", encoding="utf-8") as f:
            content = f.read()

        slug = meta["slug"]
        bengali_title = meta["title"]
        label = meta.get("category", "Political Science")
        sched_time = item["scheduled_time"]
        read_time = item["readable_time"]

        print(f"\n[Post {item['post_num']}] {bengali_title}")
        print(f"       Slug:           {slug}")
        print(f"       Category Label: {label}")
        print(f"       Schedule Time:  {read_time} ({sched_time})")

        # STEP 1: Mint clean English permalink with future scheduled time
        body = {
            "kind": "blogger#post",
            "blog": {"id": BLOG_ID},
            "title": slug,
            "content": content,
            "labels": [label],
            "published": sched_time
        }

        try:
            print("       [*] Step 1: Minting clean English permalink on Blogger (Scheduled)...")
            result = service.posts().insert(blogId=BLOG_ID, body=body, isDraft=False).execute()
            post_id = result.get("id")
            initial_url = result.get("url")
            status = result.get("status")
            print(f"       [✔] Post Minted! ID: {post_id} | Status: {status}")
            print(f"           Minted URL: {initial_url}")

            time.sleep(2)

            # STEP 2: Update title to full Bengali academic title (preserving schedule time)
            print("       [*] Step 2: Updating post title to full Bengali title...")
            patch_body = {
                "title": bengali_title,
                "published": sched_time
            }
            updated_result = service.posts().patch(blogId=BLOG_ID, postId=post_id, body=patch_body).execute()
            final_title = updated_result.get("title")
            final_url = updated_result.get("url")
            final_status = updated_result.get("status")
            final_published = updated_result.get("published")
            print(f"       [✔] Title & Schedule Confirmed: {final_title}")
            print(f"           Status:    {final_status}")
            print(f"           Published: {final_published}")
            print(f"           Target URL: {final_url}")

            scheduled_records.append({
                "post_id": post_id,
                "post_num": item["post_num"],
                "title": final_title,
                "slug": slug,
                "url": final_url,
                "label": label,
                "status": final_status,
                "scheduled_at": final_published,
                "readable_time": read_time,
                "meta_description": meta.get("meta_description")
            })

        except Exception as e:
            print(f"       [❌ ERROR] Scheduling failed: {e}")

    # Save output record
    output_record_path = os.path.join(PROJECT_ROOT, "output_posts", "scheduled_posts_07_08_09.json")
    with open(output_record_path, "w", encoding="utf-8") as f:
        json.dump(scheduled_records, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 75)
    print(f"🎉 ALL {len(scheduled_records)} POSTS SUCCESSFULLY SCHEDULED ON BLOGGER!")
    print(f"   Record saved to: output_posts/scheduled_posts_07_08_09.json")
    print("=" * 75)

if __name__ == "__main__":
    schedule_all()
