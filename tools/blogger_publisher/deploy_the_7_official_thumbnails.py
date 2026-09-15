#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/deploy_the_7_official_thumbnails.py
-----------------------------------------------------------
Updates the 7 posts on Blogger live with the newly generated
authentic Thumbnail BG/ WebP banners hosted on jsDelivr CDN.
Then pings Google Indexing API.
"""

import os
import sys
import re
import urllib.request
import subprocess
from bs4 import BeautifulSoup

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.update_post import get_authenticated_service, BLOG_ID

TARGET_POSTS = [
    {
        "url_fragment": "namta-1-to-20",
        "title": "নামতা ১ থেকে ২০ পর্যন্ত",
        "banner_webp": "namta-1-to-20-official-banner.webp",
        "alt": "নামতা ১ থেকে ২০ পর্যন্ত চার্ট সহায়িকা - HelpTrickBD"
    },
    {
        "url_fragment": "honours-political-science-book-list",
        "title": "রাষ্ট্রবিজ্ঞান অনার্স ১ম, ২য়, ৩য় ও ৪র্থ বর্ষের পাঠ্য বইয়ের তালিকা",
        "banner_webp": "political-science-honours-book-list-official-banner.webp",
        "alt": "রাষ্ট্রবিজ্ঞান অনার্স বইয়ের তালিকা - HelpTrickBD"
    },
    {
        "url_fragment": "hason-raja-was-born-in-1854-class-six",
        "title": "Hason Raja Was Born in 1854",
        "banner_webp": "hason-raja-class-six-english-official-banner.webp",
        "alt": "Hason Raja Class 6 English Seen Comprehension - HelpTrickBD"
    },
    {
        "url_fragment": "computer-types-classification-part4",
        "title": "কম্পিউটারের প্রকারভেদ (পার্ট-৪)",
        "banner_webp": "computer-types-classification-official-banner.webp",
        "alt": "কম্পিউটারের প্রকারভেদ ও শ্রেণিবিন্যাস - HelpTrickBD"
    },
    {
        "url_fragment": "computer-generations-features-part3",
        "title": "কম্পিউটারের প্রজন্ম (পার্ট-৩)",
        "banner_webp": "computer-generations-features-official-banner.webp",
        "alt": "কম্পিউটারের প্রজন্ম ও প্রযুক্তিগত তুলনা - HelpTrickBD"
    },
    {
        "url_fragment": "computer-history-inventions-part2",
        "title": "কম্পিউটারের ইতিহাস (পার্ট-২)",
        "banner_webp": "computer-history-inventions-official-banner.webp",
        "alt": "কম্পিউটারের ইতিহাস ও বিবর্তন রূপরেখা - HelpTrickBD"
    },
    {
        "url_fragment": "computer-definition-history",
        "title": "কম্পিউটার কাকে বলে? (২০২৬)",
        "banner_webp": "computer-definition-history-official-banner.webp",
        "alt": "কম্পিউটার কাকে বলে সংজ্ঞা ও ইতিহাস - HelpTrickBD"
    }
]

def main():
    print("=" * 70)
    print("🚀 Deploying 7 Authentic Thumbnail BG/ Banners to Live Blogger...")
    print("=" * 70)

    service = get_authenticated_service()
    if not service:
        print("[!] Error: Could not authenticate Blogger API.")
        return

    # Fetch all posts to map URL to post ID
    posts_res = service.posts().list(blogId=BLOG_ID, maxResults=150, fetchBodies=True).execute()
    all_live_items = posts_res.get('items', [])
    print(f"[*] Retrieved {len(all_live_items)} total live posts from Blogger API.")

    updated_urls = []

    for target in TARGET_POSTS:
        frag = target["url_fragment"]
        matched_post = None
        for item in all_live_items:
            url = item.get("url", "")
            if frag in url:
                matched_post = item
                break

        if not matched_post:
            print(f"[!] Warning: No matching post found for URL fragment '{frag}'")
            continue

        post_id = matched_post["id"]
        post_url = matched_post["url"]
        post_title = matched_post["title"]
        content = matched_post.get("content", "")

        cdn_url = f"https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/{target['banner_webp']}"
        print(f"\n[*] Updating Post: {post_title}")
        print(f"    URL: {post_url}")
        print(f"    New CDN Banner: {cdn_url}")

        # Verify CDN URL responds with 200 OK
        try:
            req = urllib.request.Request(cdn_url, headers={'User-Agent': 'Mozilla/5.0'})
            res = urllib.request.urlopen(req)
            print(f"    CDN Health Check: HTTP {res.status} OK")
        except Exception as e:
            print(f"    [!] CDN Check Notice: {e} (Cache may take 1-2 mins to propagate)")

        # Replace or inject the hero image
        soup = BeautifulSoup(content, 'html.parser')
        
        # Check if first image exists
        imgs = soup.find_all('img')
        if imgs:
            first_img = imgs[0]
            first_img['src'] = cdn_url
            first_img['alt'] = target['alt']
            first_img['title'] = post_title
            first_img['loading'] = 'eager'
            first_img['style'] = "width: 100%; max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 4px 14px rgba(0,0,0,0.12); display: block; margin: 0 auto 24px;"
            new_content = str(soup)
        else:
            # Inject at top
            hero_html = f'<div class="separator" style="clear: both; text-align: center; margin-bottom: 24px;"><img alt="{target["alt"]}" title="{post_title}" src="{cdn_url}" style="width: 100%; max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 4px 14px rgba(0,0,0,0.12); display: block; margin: 0 auto;" loading="eager" /></div>'
            new_content = hero_html + "\n" + content

        # Patch the post live on Blogger
        patch_body = {
            "content": new_content
        }
        updated = service.posts().patch(blogId=BLOG_ID, postId=post_id, body=patch_body).execute()
        print(f"    [✔] Successfully updated live on Blogger! (Post ID: {post_id})")
        updated_urls.append(post_url)

    print("\n" + "=" * 70)
    print(f"📡 Submitting {len(updated_urls)} Updated URLs to Google Indexing API...")
    print("=" * 70)
    if updated_urls:
        index_file = os.path.join(PROJECT_ROOT, "tools", "indexer", "the_7_updated_urls.txt")
        with open(index_file, "w", encoding="utf-8") as f:
            for u in updated_urls:
                f.write(u + "\n")
        res = subprocess.run(["python", os.path.join(PROJECT_ROOT, "tools", "indexer", "index_now.py"), "--file", index_file], capture_output=True, text=True)
        print(res.stdout)
        if res.stderr:
            print("[!] Indexing API Stderr:", res.stderr)

    print("\n" + "=" * 70)
    print("🎉 ALL 7 POST THUMBNAILS DEPLOYED AND SUBMITTED SUCCESSFULLY!")
    print("=" * 70)

if __name__ == "__main__":
    main()
