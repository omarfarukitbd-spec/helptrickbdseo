#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/publish_nu_social_change_posts.py
--------------------------------------------------------
Publishes the 2 Masters Political Science posts to Blogger live
following the mandatory 2-Step Custom English Permalink Minting Protocol:
Step 1: Insert post with English keyword slug title to mint clean permalink.
Step 2: Immediately update title to full Bengali academic title.
Step 3: Submit live URL to Google Indexing API for rapid indexing.
"""

import os
import sys
import json
import time
import urllib.request
import subprocess

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID

DRAFTS = [
    {
        "html_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-05-transitional-society-characteristics.html"),
        "meta_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-05-transitional-society-characteristics_metadata.json"),
    },
    {
        "html_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-06-traditional-vs-modern-society.html"),
        "meta_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-06-traditional-vs-modern-society_metadata.json"),
    }
]

def publish_selected():
    print("=" * 75)
    print("🚀 HELPTRICKBD 2-STEP PUBLISHING ENGINE — POST 05 & POST 06")
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

        print(f"\n[{idx}/2] Processing: {bengali_title}")
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
                indexer_cmd = [
                    sys.executable,
                    os.path.join(PROJECT_ROOT, "tools", "indexer", "index_now.py"),
                    "--url", final_url
                ]
                idx_res = subprocess.run(indexer_cmd, capture_output=True, text=True, cwd=os.path.join(PROJECT_ROOT, "tools", "indexer"))
                print(f"      [✔] Google Indexing Result: {idx_res.stdout.strip()}")
            except Exception as e_idx:
                print(f"      [!] Warning: Google Indexing Ping failed: {e_idx}")

            # STEP 4: HTTP 200 Check
            try:
                req = urllib.request.Request(final_url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
                with urllib.request.urlopen(req, timeout=10) as resp:
                    print(f"      [✔] HTTP Status: {resp.getcode()} OK")
            except Exception as e_http:
                print(f"      [!] HTTP Verification Notice: {e_http}")

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
    output_report = os.path.join(PROJECT_ROOT, "output_posts", "published_nu_social_change_posts.json")
    os.makedirs(os.path.dirname(output_report), exist_ok=True)
    with open(output_report, "w", encoding="utf-8") as f:
        json.dump(published_records, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 75)
    print(f"🎉 BOTH POSTS PUBLISHED & SUBMITTED TO GOOGLE INDEXING API!")
    print(f"   Summary Report saved to: {output_report}")
    print("=" * 75)
    for rec in published_records:
        print(f"  • {rec['title']}")
        print(f"    URL: {rec['url']}\n")

if __name__ == "__main__":
    publish_selected()
