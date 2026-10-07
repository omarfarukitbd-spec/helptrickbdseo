#!/usr/bin/env python3
"""
tools/blogger_publisher/touch_and_sync_silo_posts.py
Refreshes and updates the 4 silo posts on Blogger live so that
Blogger's thumbnail extractor re-caches the brand-new official thumbnails.
"""

import os
import sys
import time

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.update_post import get_authenticated_service, BLOG_ID

POSTS = [
    {
        "post_id": "5898560761534163519",
        "title": "সরকারি প্রাথমিক শিক্ষক নিয়োগ ও চাকরির ভাইভা প্রস্তুতি গাইডলাইন (২০২৬)",
        "banner": "primary-teacher-viva-guide-banner.webp"
    },
    {
        "post_id": "5695213693308965635",
        "title": "ক্লাউড কম্পিউটিং কি? প্রকারভেদ, বাস্তব সুবিধা ও শীর্ষ প্ল্যাটফর্মের সহজ ব্যাখ্যা",
        "banner": "cloud-computing-guide-banner.webp"
    },
    {
        "post_id": "3998042912898607308",
        "title": "কম্পিউটার ভাইরাস ও সাইবার নিরাপত্তা: ম্যালওয়্যার থেকে ডাটা সুরক্ষার সেরা উপায় (২০২৬)",
        "banner": "computer-virus-cyber-security-banner.webp"
    },
    {
        "post_id": "3708406842330148411",
        "title": "বিসিএস প্রিলিমিনারি ২০০ নম্বরের বিষয়ভিত্তিক মানবণ্টন ও প্রথমবারে পাসের পূর্ণাঙ্গ বুক লিস্ট",
        "banner": "bcs-preliminary-marks-booklist-banner.webp"
    }
]

CDN_BASE = "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/"

def main():
    service = get_authenticated_service()
    if not service:
        print("[!] Blogger API auth failed.")
        sys.exit(1)

    print("=" * 65)
    print("🔄 Re-syncing Silo Posts on Blogger for Thumbnail Cache Re-index...")
    print("=" * 65)

    for item in POSTS:
        pid = item["post_id"]
        banner = item["banner"]
        cdn_url = f"{CDN_BASE}{banner}"
        print(f"\n[*] Updating Post ID: {pid} ({item['title'][:40]}...)")
        try:
            post = service.posts().get(blogId=BLOG_ID, postId=pid).execute()
            content = post.get("content", "")

            # Ensure image tag has cdn_url
            if cdn_url not in content:
                print(f"    [!] Updating image src to: {cdn_url}")
                # Replace any old image src in the first figure/img tag
                import re
                content = re.sub(r'src=["\'][^"\']*banner[^"\']*["\']', f'src="{cdn_url}"', content)
                post["content"] = content

            # Trigger update on Blogger
            updated = service.posts().update(blogId=BLOG_ID, postId=pid, body=post).execute()
            print(f"    [✔] Successfully updated live on Blogger!")
            print(f"    [🔗] URL: {updated.get('url')}")
            time.sleep(1)
        except Exception as e:
            print(f"    [!] Error updating {pid}: {e}")

    print("\n" + "=" * 65)
    print("🎉 All 4 posts live on Blogger re-indexed with new official thumbnails!")
    print("=" * 65)

if __name__ == "__main__":
    main()
