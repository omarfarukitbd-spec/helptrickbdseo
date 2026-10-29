#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/deploy_cost_suggestion.py
-------------------------------
Deploys the complete master suggestion for:
Subject: উৎপাদন ব্যয় হিসাববিজ্ঞান (Cost Accounting - Course Code: 232505)
Total Questions: 312 (Units 01-06 complete)
"""

import os
import sys
import json

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.wp_publisher.publisher import WordPressPublisher

def deploy_cost_post():
    sys.stdout.reconfigure(encoding='utf-8')
    pub = WordPressPublisher()
    
    # 1. Test Connection
    conn = pub.test_connection()
    if not conn.get("success"):
        print("[ERROR] Failed to connect to WordPress:", conn)
        return False
    print(f"✅ WordPress Connected: User '{conn.get('username')}' (ID: {conn.get('user_id')})")
    
    # 2. Upload Featured Image
    thumb_path = os.path.join(PROJECT_ROOT, "assets", "images", "thumbnails", "cost_accounting_banner.webp")
    if not os.path.exists(thumb_path):
        print(f"[ERROR] Thumbnail not found: {thumb_path}")
        return False
        
    print(f"Uploading featured image: {thumb_path}...")
    media_id = pub.upload_featured_image(
        thumb_path,
        alt_text="অনার্স ৩য় বর্ষ উৎপাদন ব্যয় হিসাববিজ্ঞান সাজেশন",
        title="অনার্স ৩য় বর্ষ উৎপাদন ব্যয় হিসাববিজ্ঞান সাজেশন 2026"
    )
    print(f"✅ Featured Media Uploaded! Media ID: {media_id}")
    
    # 3. Read Compiled HTML
    html_path = os.path.join(PROJECT_ROOT, "scratch", "cost_master_312.html")
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    title = "অনার্স ৩য় বর্ষ উৎপাদন ব্যয় হিসাববিজ্ঞান সাজেশন 2026: Best Complete Exam Guide"
    slug = "honours-3rd-year-cost-accounting-suggestion"
    focus_kw = "অনার্স ৩য় বর্ষ উৎপাদন ব্যয় হিসাববিজ্ঞান সাজেশন"
    meta_desc = "অনার্স ৩য় বর্ষ উৎপাদন ব্যয় হিসাববিজ্ঞান সাজেশন 2026: জাতীয় বিশ্ববিদ্যালয় BBA ৩য় বর্ষ হিসাববিজ্ঞানের ক, খ ও গ বিভাগের ৩১২টি প্রশ্ন ও অংকের সমাধান।"
    
    seo_meta = {
        "title": title,
        "seo_title": title,
        "search_desc": meta_desc,
        "focus_keyword": f"{focus_kw}, Honours 3rd Year Cost Accounting Suggestion"
    }
    
    # 4. Check for existing post or create
    existing_check = pub.client.get("posts", params={"slug": slug, "status": "any"})
    if existing_check.status_code == 200 and existing_check.json():
        existing_post = existing_check.json()[0]
        post_id = existing_post.get("id")
        print(f"Found existing post for slug '{slug}' (ID: {post_id}). Updating...")
        res = pub.update_post(
            post_id,
            title=title,
            content=content,
            categories=[4, 9],
            featured_media=media_id,
            meta={
                "rank_math_title": title,
                "rank_math_description": meta_desc,
                "rank_math_focus_keyword": f"{focus_kw}, Honours 3rd Year Cost Accounting Suggestion",
                "rank_math_robots": "index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large"
            }
        )
        post_url = existing_post.get("link")
        edit_url = f"{pub.client.base_url}/wp-admin/post.php?post={post_id}&action=edit"
    else:
        print(f"Creating new post for slug '{slug}'...")
        res = pub.create_post(
            title=title,
            content=content,
            slug=slug,
            categories=[4, 9],
            status="draft",
            featured_media_id=media_id,
            seo_meta=seo_meta
        )
        post_id = res.get("id")
        post_url = res.get("url")
        edit_url = res.get("edit_url")
        
    if res.get("success"):
        print(f"✅ Cost Accounting Post Deployed Successfully!")
        print(f"   ID: {post_id}")
        print(f"   URL: {post_url}")
        print(f"   Edit URL: {edit_url}")
        print(f"   Status: {res.get('status', 'draft')}")
        print(f"   Questions included: 312 (Units 01-06 complete)")
        return True
    else:
        print(f"[ERROR] Failed to deploy Cost Accounting Post:", res)
        return False

if __name__ == "__main__":
    deploy_cost_post()
