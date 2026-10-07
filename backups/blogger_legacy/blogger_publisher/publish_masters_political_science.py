#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/publish_masters_political_science.py
-----------------------------------------------------------
Publishes the 4 Masters Political Science posts to Blogger live
following the mandatory 2-Step Custom English Permalink Minting Protocol:
Step 1: Insert post with English keyword slug title to mint clean permalink.
Step 2: Immediately update title to full Bengali academic title.
Step 3: Submit live URL to Google Indexing API for rapid indexing.
"""

import os
import sys
import json
import time

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID

DRAFTS = [
    {
        "html_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-01-political-violence-bangladesh.html"),
        "meta_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-01-political-violence-bangladesh_metadata.json"),
    },
    {
        "html_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-02-un-membership-bangladesh.html"),
        "meta_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-02-un-membership-bangladesh_metadata.json"),
    },
    {
        "html_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-03-secularism-vs-islamic-values.html"),
        "meta_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-03-secularism-vs-islamic-values_metadata.json"),
    },
    {
        "html_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-04-caretaker-government-bangladesh.html"),
        "meta_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-04-caretaker-government-bangladesh_metadata.json"),
    }
]

def publish_all():
    print("=" * 75)
    print("🚀 HELPTRICKBD 2-STEP PUBLISHING ENGINE — MASTERS POLITICAL SCIENCE")
    print("=" * 75)

    service = get_authenticated_service()
    if not service:
        print("[ERROR] Failed to authenticate Blogger API v3.")
        sys.exit(1)

    published_records = []

    for idx, item in enumerate(DRAFTS, 1):
        with open(item["meta_file"], "r", encoding="utf-8") as f:
            meta = json.load(f)
        with open(item["html_file"], "r", encoding="utf-8") as f:
            content = f.read()

        slug = meta["slug"]
        bengali_title = meta["title"]
        label = meta["category"]  # "Political Science"

        print(f"\n[{idx}/4] Processing: {bengali_title}")
        print(f"      Slug (Step 1 Permalink Mint): {slug}")
        print(f"      Label:                        {label}")

        # STEP 1: Mint clean English permalink
        body = {
            "kind": "blogger#post",
            "blog": {"id": BLOG_ID},
            "title": slug,
            "content": content,
            "labels": [label]
        }

        try:
            print("      [*] Step 1: Minting clean English permalink on Blogger...")
            result = service.posts().insert(blogId=BLOG_ID, body=body, isDraft=False).execute()
            post_id = result.get("id")
            initial_url = result.get("url")
            print(f"      [✔] Post Minted! ID: {post_id}")
            print(f"          Minted URL: {initial_url}")

            time.sleep(2)

            # STEP 2: Update title to full Bengali academic title
            print("      [*] Step 2: Updating post title to full Bengali academic title...")
            patch_body = {
                "title": bengali_title
            }
            updated_result = service.posts().patch(blogId=BLOG_ID, postId=post_id, body=patch_body).execute()
            final_title = updated_result.get("title")
            final_url = updated_result.get("url")
            print(f"      [✔] Title Updated: {final_title}")
            print(f"          Final Live URL: {final_url}")

            # STEP 3: Ping Google Indexing API
            print("      [*] Step 3: Submitting URL to Google Indexing API...")
            try:
                import subprocess
                indexer_cmd = [
                    sys.executable,
                    os.path.join(PROJECT_ROOT, "tools", "indexer", "index_now.py"),
                    "--url", final_url
                ]
                idx_res = subprocess.run(indexer_cmd, capture_output=True, text=True, cwd=os.path.join(PROJECT_ROOT, "tools", "indexer"))
                print(f"      [✔] Google Indexing Result: {idx_res.stdout.strip()}")
            except Exception as e_idx:
                print(f"      [!] Warning: Google Indexing Ping failed: {e_idx}")

            published_records.append({
                "post_id": post_id,
                "title": final_title,
                "slug": slug,
                "url": final_url,
                "label": label,
                "published_at": updated_result.get("published")
            })

            time.sleep(2)

        except Exception as e:
            print(f"      [!] ERROR during publishing: {e}")
            raise e

    # Save summary report
    output_report = os.path.join(PROJECT_ROOT, "output_posts", "published_masters_posts.json")
    os.makedirs(os.path.dirname(output_report), exist_ok=True)
    with open(output_report, "w", encoding="utf-8") as f:
        json.dump(published_records, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 75)
    print(f"🎉 ALL 4 POSTS PUBLISHED & SUBMITTED TO GOOGLE INDEXING API!")
    print(f"   Summary Report saved to: {output_report}")
    print("=" * 75)
    for rec in published_records:
        print(f"  • {rec['title']}")
        print(f"    URL: {rec['url']}\n")

if __name__ == "__main__":
    publish_all()
