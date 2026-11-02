#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/deploy_adv1_individual_years.py
-------------------------------------
Synchronizes the 6 dedicated year posts (2019 to 2024) to WordPress REST API:
- Categories: [4, 9, 127] (Education Guide, National University, NU Question Bank)
- Status: draft
- Featured Media: Dedicated WebP banners with NU Logo & PDF Badge
- Rank Math: 100% optimized focus keywords and schema metadata
"""

import os
import sys
import json
import requests

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.wp_publisher.publisher import WordPressPublisher

YEARS = ["2024", "2023", "2022", "2021", "2020", "2019"]

def deploy_all_years():
    pub = WordPressPublisher()
    conn = pub.test_connection()
    if not conn.get("success"):
        print("[ERROR] Failed to connect to WordPress:", conn)
        return False
        
    print(f"✅ WordPress Connected: User '{conn.get('username')}' (ID: {conn.get('user_id')})")
    
    deployed_records = {}
    
    for yr in YEARS:
        html_path = os.path.join(PROJECT_ROOT, "scratch", f"adv1_board_{yr}.html")
        meta_path = os.path.join(PROJECT_ROOT, "scratch", f"adv1_board_{yr}_meta.json")
        
        with open(html_path, "r", encoding="utf-8") as f:
            content = f.read()
        with open(meta_path, "r", encoding="utf-8") as f:
            meta = json.load(f)
            
        title = meta['title']
        slug = meta['custom_url']
        focus_kw = meta['rank_math_focus_keyword']
        desc = meta['meta_description']
        featured_media = meta['featured_media_id']
        
        print(f"\n--- Deploying Post for Year {yr} ({slug}) ---")
        
        existing_check = pub.client.get("posts", params={"slug": slug, "status": "any"})
        if existing_check.status_code == 200 and existing_check.json():
            post_obj = existing_check.json()[0]
            pid = post_obj.get("id")
            print(f"    Found existing post ID {pid}. Updating...")
            res = pub.update_post(
                pid,
                title=title,
                content=content,
                categories=[4, 9, 127],
                featured_media=featured_media,
                meta={
                    "rank_math_title": title,
                    "rank_math_description": desc,
                    "rank_math_focus_keyword": focus_kw,
                    "rank_math_robots": "index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large"
                }
            )
            post_url = post_obj.get("link")
        else:
            print(f"    Creating new post for slug '{slug}'...")
            res = pub.create_post(
                title=title,
                content=content,
                slug=slug,
                categories=[4, 9, 127],
                status="draft",
                featured_media_id=featured_media,
                seo_meta={
                    "title": title,
                    "seo_title": title,
                    "search_desc": desc,
                    "focus_keyword": focus_kw
                }
            )
            pid = res.get("id")
            post_url = res.get("url")
            
        if res.get("success"):
            print(f"    ✅ Success! ID: {pid}, Slug: {slug}")
            deployed_records[yr] = {
                "year": yr,
                "post_id": pid,
                "slug": slug,
                "title": title,
                "url": f"https://www.helptrickbd.com/{slug}/",
                "preview_url": f"https://www.helptrickbd.com/?p={pid}",
                "status": "draft"
            }
        else:
            print(f"    [FAIL] Could not deploy year {yr}:", res)
            
    summary_path = os.path.join(PROJECT_ROOT, "scratch", "adv1_deployed_years.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(deployed_records, f, ensure_ascii=False, indent=2)
        
    print(f"\n[DONE] Deployed {len(deployed_records)}/{len(YEARS)} posts successfully!")
    return deployed_records

if __name__ == "__main__":
    deploy_all_years()
