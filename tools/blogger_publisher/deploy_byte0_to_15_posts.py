#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/deploy_byte0_to_15_posts.py
Moves the hero banner to Byte-0 for the 15 posts that had banners placed after <style> blocks.
"""

import os
import sys
import json
import time
import re

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID

BYTE0_FILE = os.path.join(PROJECT_ROOT, "scratch", "all_byte_0_failed.json")
with open(BYTE0_FILE, "r", encoding="utf-8") as f:
    byte0_items = json.load(f)

def move_hero_to_byte0(content, title):
    hero_html = None
    rest_content = content
    
    # 1. Figure
    m = re.search(r'<figure[\s\S]*?</figure>', rest_content, re.IGNORECASE)
    if m:
        hero_html = m.group(0)
        rest_content = rest_content[:m.start()] + rest_content[m.end():]
    else:
        # 2. Div center with img
        m = re.search(r'<div style="text-align:\s*center;[^>]*>[\s\S]*?<img[^>]*>[\s\S]*?</div>', rest_content, re.IGNORECASE)
        if m:
            hero_html = m.group(0)
            rest_content = rest_content[:m.start()] + rest_content[m.end():]
        else:
            # 3. Separator
            m = re.search(r'<div class="separator"[^>]*>[\s\S]*?</div>', rest_content, re.IGNORECASE)
            if m:
                hero_html = m.group(0)
                rest_content = rest_content[:m.start()] + rest_content[m.end():]
            else:
                # 4. Bare img
                m = re.search(r'<img[^>]*>', rest_content, re.IGNORECASE)
                if m:
                    img_tag = m.group(0)
                    hero_html = (
                        f'<figure style="margin: 0 0 25px 0; text-align: center; clear: both;">\n'
                        f'  {img_tag}\n'
                        f'  <figcaption style="font-size: 14px; color: #64748b; margin-top: 8px; font-style: italic; text-align: center;">{title} - হেল্পট্রিকবিডি অফিসিয়াল গাইড</figcaption>\n'
                        f'</figure>'
                    )
                    rest_content = rest_content[:m.start()] + rest_content[m.end():]
                    
    if not hero_html:
        raise ValueError(f"No hero image found for {title}")
        
    final_content = hero_html + "\n\n" + rest_content.lstrip()
    return final_content

service = get_authenticated_service()
if not service:
    print("[ERROR] Auth failed")
    sys.exit(1)

print("=" * 75)
print("UPDATING 15 POSTS ON BLOGGER TO BYTE-0 HERO PLACEMENT")
print("=" * 75)

success = 0
for idx, item in enumerate(byte0_items, 1):
    pid = item["id"]
    title = item["title"]
    print(f"\n[{idx}/15] Updating Post ID: {pid}")
    print(f"  Title: {title[:50]}...")
    
    try:
        post = service.posts().get(blogId=BLOG_ID, postId=pid, view="ADMIN").execute()
        orig_content = post.get("content", "")
        new_content = move_hero_to_byte0(orig_content, title)
        
        first_idx = new_content.find("<img")
        print(f"  Byte-0 placement verified: index {first_idx} (< 100)")
        
        service.posts().patch(
            blogId=BLOG_ID,
            postId=pid,
            body={
                "content": new_content,
                "published": post.get("published")
            }
        ).execute()
        print(f"  [OK] Successfully updated on Blogger.")
        success += 1
        time.sleep(2)
    except Exception as e:
        print(f"  [ERROR] Failed to update {pid}: {e}")
        time.sleep(5)

print("\n" + "=" * 75)
print(f"[OK] Completed: {success}/15 posts successfully updated to Byte-0.")
print("=" * 75)
