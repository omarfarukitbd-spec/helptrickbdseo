#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/fix_hero_image_position.py
--------------------------------------------------
Moves the Hero <figure>...</figure> (or first <img> block) to the very top
of the post HTML (byte 0) so that Blogger's thumbnail extractor (which scans
only the first 8 KB) instantly detects the <img> tag and generates the post thumbnail,
preventing the initial letter fallback ([S]).
"""

import os
import sys
import re
import json

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID

def reorder_html_hero_top(html_content):
    """
    Moves <figure>...</figure> containing the hero <img> to the very top.
    """
    fig_match = re.search(r'(<figure[^>]*>.*?</figure>)', html_content, re.DOTALL | re.IGNORECASE)
    if not fig_match:
        # Check if there is an <img before any figure
        img_match = re.search(r'(<img[^>]+>)', html_content, re.IGNORECASE)
        if not img_match:
            return html_content
        # Move img to top
        img_block = img_match.group(1)
        remaining = html_content[:img_match.start()] + html_content[img_match.end():]
        return img_block + '\n\n' + remaining.strip()
    
    fig_block = fig_match.group(1)
    # Check if figure is already at the beginning (within first 150 chars)
    if html_content.strip().startswith(fig_block.strip()):
        return html_content
    
    remaining = html_content[:fig_match.start()] + html_content[fig_match.end():]
    return fig_block + '\n\n' + remaining.strip()

def main():
    service = get_authenticated_service()
    
    # 1. Update scheduled posts
    print("--- Fetching SCHEDULED posts ---")
    sched_posts = service.posts().list(blogId=BLOG_ID, status=['SCHEDULED'], maxResults=20).execute()
    for p in sched_posts.get('items', []):
        post_id = p['id']
        title = p['title']
        content = p.get('content', '')
        first_img = content.find('<img')
        print(f"Scheduled Post: {title[:40]} | img at: {first_img}")
        
        if first_img > 1000:
            new_content = reorder_html_hero_top(content)
            new_first_img = new_content.find('<img')
            print(f"  -> Reordered! New img at: {new_first_img}")
            p['content'] = new_content
            service.posts().patch(blogId=BLOG_ID, postId=post_id, body=p).execute()
            print(f"  -> Successfully updated post on Blogger!")

    # 2. Check LIVE posts with first_img > 8000
    print("\n--- Checking LIVE posts for image position > 8000 ---")
    live_posts = service.posts().list(blogId=BLOG_ID, status=['LIVE'], maxResults=20).execute()
    for p in live_posts.get('items', []):
        post_id = p['id']
        title = p['title']
        content = p.get('content', '')
        first_img = content.find('<img')
        if first_img > 7500:
            print(f"Live Post with late image: {title[:40]} | img at: {first_img}")
            new_content = reorder_html_hero_top(content)
            new_first_img = new_content.find('<img')
            print(f"  -> Reordered! New img at: {new_first_img}")
            p['content'] = new_content
            service.posts().patch(blogId=BLOG_ID, postId=post_id, body=p).execute()
            print(f"  -> Successfully updated post on Blogger!")

if __name__ == '__main__':
    main()
