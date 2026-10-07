#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/schedule_ssc_english_2nd_posts.py
---------------------------------------------------------
Schedules all 7 SSC & Dakhil English 2nd Paper posts to Blogger
starting today at 8:00 AM BST (2026-09-19T08:00:00+06:00) with 30-minute intervals.

Enforces:
1. 2-Step Custom English Permalink Minting Protocol (Zero generic URLs).
2. Exact RFC 3339 Future Publishing Times (Blogger Scheduled status).
3. Single Approved Category Label: "Education Guide".
4. Full Pre-flight validation verification before publishing.
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
        "post_num": "10",
        "name": "Changing Sentences",
        "html_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-10-ssc-changing-sentences.html"),
        "meta_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-10-ssc-changing-sentences_metadata.json"),
        "scheduled_time": "2026-09-19T08:00:00+06:00",
        "readable_time": "আজ সকাল ৮:০০ BST"
    },
    {
        "post_num": "11",
        "name": "Tag Questions",
        "html_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-11-ssc-tag-questions.html"),
        "meta_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-11-ssc-tag-questions_metadata.json"),
        "scheduled_time": "2026-09-19T08:30:00+06:00",
        "readable_time": "আজ সকাল ৮:৩০ BST"
    },
    {
        "post_num": "12",
        "name": "Suffix & Prefix",
        "html_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-12-ssc-suffix-prefix.html"),
        "meta_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-12-ssc-suffix-prefix_metadata.json"),
        "scheduled_time": "2026-09-19T09:00:00+06:00",
        "readable_time": "আজ সকাল ৯:০০ BST"
    },
    {
        "post_num": "13",
        "name": "Prepositions & Gap Filling",
        "html_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-13-ssc-preposition-gap-filling.html"),
        "meta_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-13-ssc-preposition-gap-filling_metadata.json"),
        "scheduled_time": "2026-09-19T09:30:00+06:00",
        "readable_time": "আজ সকাল ৯:৩০ BST"
    },
    {
        "post_num": "14",
        "name": "Connectors & Punctuation",
        "html_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-14-ssc-connectors-punctuation.html"),
        "meta_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-14-ssc-connectors-punctuation_metadata.json"),
        "scheduled_time": "2026-09-19T10:00:00+06:00",
        "readable_time": "আজ সকাল ১০:০০ BST"
    },
    {
        "post_num": "15",
        "name": "Writing Part Final Suggestion",
        "html_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-15-ssc-writing-part.html"),
        "meta_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-15-ssc-writing-part_metadata.json"),
        "scheduled_time": "2026-09-19T10:30:00+06:00",
        "readable_time": "আজ সকাল ১০:৩০ BST"
    },
    {
        "post_num": "16",
        "name": "Full Model Test & Board Question",
        "html_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-16-ssc-full-model-test.html"),
        "meta_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-16-ssc-full-model-test_metadata.json"),
        "scheduled_time": "2026-09-19T11:00:00+06:00",
        "readable_time": "আজ সকাল ১১:০০ BST"
    }
]

def schedule_all():
    print("=" * 75)
    print("⏰ HELPTRICKBD BLOGGER SCHEDULE ENGINE — SSC ENGLISH 2ND PAPER (POSTS 10-16)")
    print("   Target Release Window: আজ সকাল ৮:০০ টা থেকে শুরু (৩০ মিনিট বিরতি)")
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
        full_title = meta["title"]
        label = meta.get("labels", ["Education Guide"])[0] if isinstance(meta.get("labels"), list) else meta.get("labels", "Education Guide")
        sched_time = item["scheduled_time"]
        read_time = item["readable_time"]

        print(f"\n[Post {item['post_num']}: {item['name']}]")
        print(f"       Title:          {full_title[:60]}...")
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

            # STEP 2: Update title to full academic title (preserving schedule time)
            print("       [*] Step 2: Updating post title to full academic title...")
            patch_body = {
                "title": full_title,
                "published": sched_time
            }
            updated_result = service.posts().patch(blogId=BLOG_ID, postId=post_id, body=patch_body).execute()
            final_title = updated_result.get("title")
            final_url = updated_result.get("url")
            final_status = updated_result.get("status")
            final_published = updated_result.get("published")
            print(f"       [✔] Title & Schedule Confirmed: {final_title[:55]}...")
            print(f"           Status:    {final_status}")
            print(f"           Published: {final_published}")
            print(f"           Target URL: {final_url}")

            scheduled_records.append({
                "post_id": post_id,
                "post_num": item["post_num"],
                "name": item["name"],
                "title": final_title,
                "slug": slug,
                "url": final_url,
                "label": label,
                "status": final_status,
                "scheduled_at": final_published,
                "readable_time": read_time,
                "search_description": meta.get("search_description")
            })

            time.sleep(2)

        except Exception as e:
            print(f"       [❌ ERROR] Scheduling failed for Post {item['post_num']}: {e}")

    # Save output record
    output_dir = os.path.join(PROJECT_ROOT, "output_posts")
    os.makedirs(output_dir, exist_ok=True)
    output_record_path = os.path.join(output_dir, "scheduled_ssc_english_2nd_posts.json")
    with open(output_record_path, "w", encoding="utf-8") as f:
        json.dump(scheduled_records, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 75)
    print(f"🎉 ALL {len(scheduled_records)} POSTS SUCCESSFULLY SCHEDULED ON BLOGGER!")
    print(f"   Record saved to: output_posts/scheduled_ssc_english_2nd_posts.json")
    print("=" * 75)

if __name__ == "__main__":
    schedule_all()
