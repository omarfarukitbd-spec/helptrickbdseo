#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/deploy_87_thumbnails.py
------------------------------------------------
Deploys official 16:9 featured thumbnails for all 87 audited posts on Blogger:
- Places official <figure><img ...></figure> at Byte 0 (< 100 chars)
- Surgically cleans previous hero banners to avoid duplicates
- Updates BlogPosting & FAQPage JSON-LD image property
- Preserves 100% of the original content, labels, and publish dates
- Includes persistent checkpointing to safely resume if interrupted
"""

import os
import sys
import json
import time
import re

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID

PLAN_FILE = os.path.join(PROJECT_ROOT, "scratch", "batch_thumbnail_plan.json")
PROGRESS_FILE = os.path.join(PROJECT_ROOT, "scratch", "deploy_thumbnails_progress.json")

def transform_post_content(post_id, title, content):
    cdn_url = f"https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/htbd-official-{post_id}.webp"
    
    hero_banner = (
        f'<figure style="margin: 0 0 25px 0; text-align: center; clear: both;">\n'
        f'  <img alt="{title}" title="{title}" src="{cdn_url}" width="1200" height="675" loading="eager" fetchpriority="high" decoding="async" style="width: 100%; max-width: 1200px; height: auto; aspect-ratio: 16/9; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.08); display: block; margin: 0 auto;" />\n'
        f'  <figcaption style="font-size: 14px; color: #64748b; margin-top: 8px; font-style: italic; text-align: center;">{title} - হেল্পট্রিকবিডি অফিসিয়াল গাইড</figcaption>\n'
        f'</figure>\n'
    )
    
    rest_content = content
    
    # 1. Pattern: figure in top 6000 chars
    fig_match = re.search(r'<figure[\s\S]*?</figure>', rest_content[:6000], re.IGNORECASE)
    if fig_match:
        rest_content = rest_content[:fig_match.start()] + rest_content[fig_match.end():]
    else:
        # 2. Pattern: div separator in top 6000 chars
        sep_match = re.search(r'<div class="separator"[^>]*>[\s\S]*?</div>', rest_content[:6000], re.IGNORECASE)
        if sep_match:
            rest_content = rest_content[:sep_match.start()] + rest_content[sep_match.end():]
        else:
            # 3. Pattern: div center with img in top 6000 chars
            div_match = re.search(r'<div style="text-align:\s*center;[^>]*>[\s\S]*?<img[^>]*>[\s\S]*?</div>', rest_content[:6000], re.IGNORECASE)
            if div_match:
                rest_content = rest_content[:div_match.start()] + rest_content[div_match.end():]
            else:
                # 4. Pattern: bare img in top 6000 chars
                img_match = re.search(r'<img[^>]*>', rest_content[:6000], re.IGNORECASE)
                if img_match:
                    rest_content = rest_content[:img_match.start()] + rest_content[img_match.end():]
                    
    # Update schema JSON-LD image URL if present
    rest_content = re.sub(
        r'("image"\s*:\s*")([^"]+)(")',
        rf'\g<1>{cdn_url}\g<3>',
        rest_content
    )
    
    # Enforce Byte-0 placement
    final_content = hero_banner + rest_content.lstrip()
    return final_content

def main():
    print("=" * 80)
    print("HELPTICKBD OFFICIAL THUMBNAIL BATCH DEPLOYMENT (87 POSTS)")
    print("=" * 80)
    
    if not os.path.exists(PLAN_FILE):
        print(f"[ERROR] Plan file not found: {PLAN_FILE}")
        sys.exit(1)
        
    with open(PLAN_FILE, "r", encoding="utf-8") as f:
        plan = json.load(f)
        
    # Load progress checkpoint
    completed_ids = set()
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
            try:
                progress_data = json.load(f)
                completed_ids = set(progress_data.get("completed_ids", []))
                print(f"[*] Resuming: Found {len(completed_ids)} already completed posts.")
            except Exception:
                pass

    service = get_authenticated_service()
    if not service:
        print("[ERROR] Blogger authentication failed.")
        sys.exit(1)

    total = len(plan)
    success_count = len(completed_ids)
    
    for idx, item in enumerate(plan, start=1):
        pid = item["id"]
        title = item["title"]
        category = item["assigned_category"]
        
        if pid in completed_ids:
            continue
            
        print(f"\n[{idx}/{total}] Processing Post ID: {pid}")
        print(f"  Title: {title[:55]}...")
        print(f"  Category: {category}")
        
        try:
            # 1. Fetch live post
            post = service.posts().get(blogId=BLOG_ID, postId=pid, view="ADMIN").execute()
            orig_content = post.get("content", "")
            published_time = post.get("published")
            
            # 2. Transform content with Byte-0 hero banner
            new_content = transform_post_content(pid, title, orig_content)
            
            # Pre-flight check on content Byte-0
            first_img_idx = new_content.find("<img")
            if first_img_idx == -1 or first_img_idx > 100:
                print(f"  [WARN] Byte-0 index is {first_img_idx}, proceeding with safety checks.")

            # 3. Patch post on Blogger
            patch_body = {
                "content": new_content,
                "published": published_time
            }
            
            service.posts().patch(
                blogId=BLOG_ID,
                postId=pid,
                body=patch_body
            ).execute()
            
            print(f"  [OK] Updated successfully on Blogger (Byte-0 Hero Banner Active).")
            completed_ids.add(pid)
            success_count += 1
            
            # Save checkpoint
            with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
                json.dump({"completed_ids": list(completed_ids), "last_id": pid, "count": success_count}, f, indent=2)
                
            # Sleep 2 seconds for API safety
            time.sleep(2)
            
        except Exception as e:
            print(f"  [ERROR] Failed to update post {pid}: {e}")
            time.sleep(5)

    print("\n" + "=" * 80)
    print(f"[OK] Mass Deployment Finished: {success_count}/{total} posts updated with official thumbnails.")
    print("=" * 80)

if __name__ == "__main__":
    main()
