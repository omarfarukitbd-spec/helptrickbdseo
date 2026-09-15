#!/usr/bin/env python3
"""
tools/content_optimizer/fix_silo_image_urls.py
Fixes broken banner image URLs on the 4 newly published posts by pointing them
to the high-speed jsDelivr GitHub CDN.
"""

import os
import sys
import re
import urllib.request

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.update_post import get_authenticated_service, BLOG_ID

POSTS_TO_FIX = [
    {
        "post_id": "3998042912898607308",
        "title": "কম্পিউটার ভাইরাস ও সাইবার নিরাপত্তা: ম্যালওয়্যার থেকে ডাটা সুরক্ষার সেরা উপায় (২০২৬)",
        "expected_image": "computer-virus-cyber-security-banner.webp",
        "url": "https://www.helptrickbd.com/2026/09/computer-virus-cyber-security-guide-2026.html"
    },
    {
        "post_id": "5695213693308965635",
        "title": "ক্লাউড কম্পিউটিং কি? প্রকারভেদ, বাস্তব সুবিধা ও শীর্ষ প্ল্যাটফর্মের সহজ ব্যাখ্যা",
        "expected_image": "cloud-computing-guide-banner.webp",
        "url": "https://www.helptrickbd.com/2026/09/cloud-computing-types-benefits-guide.html"
    },
    {
        "post_id": "3708406842330148411",
        "title": "বিসিএস প্রিলিমিনারি ২০০ নম্বরের বিষয়ভিত্তিক মানবণ্টন ও প্রথমবারে পাসের পূর্ণাঙ্গ বুক লিস্ট",
        "expected_image": "bcs-preliminary-marks-booklist-banner.webp",
        "url": "https://www.helptrickbd.com/2026/09/bcs-preliminary-marks-distribution_01436475916.html"
    },
    {
        "post_id": "5898560761534163519",
        "title": "সরকারি প্রাথমিক শিক্ষক নিয়োগ ও চাকরির ভাইভা প্রস্তুতি গাইডলাইন (২০২৬)",
        "expected_image": "primary-teacher-viva-guide-banner.webp",
        "url": "https://www.helptrickbd.com/2026/09/primary-teacher-job-viva-preparation.html"
    }
]

CDN_BASE = "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/"

def run_fix():
    service = get_authenticated_service()
    if not service:
        print("[!] Blogger authentication failed.")
        return False

    print("=======================================================")
    print("  Fixing Broken Silo Post Image URLs on Blogger Live")
    print("=======================================================\n")

    for item in POSTS_TO_FIX:
        post_id = item["post_id"]
        print(f"[*] Checking Post ID: {post_id} ({item['title']})")
        try:
            post = service.posts().get(blogId=BLOG_ID, postId=post_id).execute()
            content = post.get("content", "")

            # Check if broken image url exists in content
            cdn_url = f"{CDN_BASE}{item['expected_image']}"
            
            # Replace https://www.helptrickbd.com/images/... with CDN URL
            old_pattern = r'https://www\.helptrickbd\.com/images/[a-zA-Z0-9_\-\.]+'
            if re.search(old_pattern, content):
                new_content = re.sub(old_pattern, cdn_url, content)
                post["content"] = new_content
                updated = service.posts().update(blogId=BLOG_ID, postId=post_id, body=post).execute()
                print(f"    [SUCCESS] Updated image URL to:\n      {cdn_url}")
                print(f"    [Status] Live URL: {updated.get('url')}")
            else:
                # Check if cdn_url is already present
                if cdn_url in content:
                    print(f"    [ALREADY OK] CDN URL is already present in content.")
                else:
                    print(f"    [WARN] Pattern not found. First 200 chars: {content[:200]}")

        except Exception as e:
            print(f"    [ERROR] Failed to update post {post_id}: {e}")

    # Also fix local HTML files in output_posts/new_silo_posts/
    output_dir = os.path.join(PROJECT_ROOT, "output_posts", "new_silo_posts")
    if os.path.exists(output_dir):
        print("\n[*] Updating local HTML files in output_posts/new_silo_posts/...")
        for fname in os.listdir(output_dir):
            if fname.endswith(".html"):
                fpath = os.path.join(output_dir, fname)
                with open(fpath, "r", encoding="utf-8") as f:
                    html = f.read()
                fixed_html = re.sub(r'https://www\.helptrickbd\.com/images/', CDN_BASE, html)
                if fixed_html != html:
                    with open(fpath, "w", encoding="utf-8") as f:
                        f.write(fixed_html)
                    print(f"    [Fixed Local HTML] {fname}")

    print("\n[✔] Image repair process completed successfully!")
    return True

if __name__ == "__main__":
    run_fix()
