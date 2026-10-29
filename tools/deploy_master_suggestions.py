#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/deploy_master_suggestions.py
----------------------------------
Deploys and synchronizes the two complete master subject suggestions:
1. Audit & Assurance (Post ID 15948):
   - Updates existing live published post with all 288 questions (10 Units).
   - Preserves status: 'publish'.
   - Sets Rank Math 90+ SEO metadata.

2. Advanced Accounting-I (New Post):
   - Uploads 'adv_accounting_1_banner.webp' to WordPress Media Library.
   - Creates dedicated post with all 245 questions (5 Units).
   - Sets status: 'draft' (ready for 1-click user publish).
   - Sets Rank Math 90+ SEO metadata.
"""

import os
import sys
import json

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.wp_publisher.publisher import WordPressPublisher

def deploy_all():
    sys.stdout.reconfigure(encoding='utf-8')
    pub = WordPressPublisher()
    
    # Verify connection
    conn = pub.test_connection()
    if not conn.get("success"):
        print("[ERROR] Failed to connect to WordPress:", conn)
        return False
    print(f"✅ WordPress Connected: User '{conn.get('username')}' (ID: {conn.get('user_id')})")
    
    # -------------------------------------------------------------
    # 1. Update Subject 1: Audit & Assurance (Post ID 15948)
    # -------------------------------------------------------------
    print("\n--- [1/2] Updating Post 1: Audit & Assurance (ID: 15948) ---")
    audit_html_path = os.path.join(PROJECT_ROOT, "scratch", "audit_master_288.html")
    with open(audit_html_path, "r", encoding="utf-8") as f:
        audit_content = f.read()
        
    audit_title = "অনার্স ৩য় বর্ষ নিরীক্ষা ও নিশ্চয়তা সাজেশন 2026: Best Complete Exam Guide"
    audit_focus_kw = "অনার্স ৩য় বর্ষ নিরীক্ষা ও নিশ্চয়তা সাজেশন"
    audit_meta_desc = "অনার্স ৩য় বর্ষ নিরীক্ষা ও নিশ্চয়তা সাজেশন 2026: জাতীয় বিশ্ববিদ্যালয় BBA হিসাববিজ্ঞান বিভাগের ক, খ ও গ বিভাগের ২৮৮টি প্রশ্ন ও উত্তর।"
    
    audit_payload = {
        "title": audit_title,
        "content": audit_content,
        "status": "publish",  # User explicitly published this post!
        "meta": {
            "rank_math_title": audit_title,
            "rank_math_description": audit_meta_desc,
            "rank_math_focus_keyword": f"{audit_focus_kw}, Honours 3rd Year Audit Suggestion",
            "rank_math_robots": "index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large"
        }
    }
    
    res1 = pub.update_post(15948, **audit_payload)
    if res1.get("success"):
        print(f"✅ Post 15948 Updated Successfully!")
        print(f"   URL: {res1.get('url')}")
        print(f"   Status: {res1.get('status')}")
        print(f"   Questions included: 288 (Units 01-10 complete)")
    else:
        print(f"[ERROR] Failed to update Post 15948:", res1)
        return False

    # -------------------------------------------------------------
    # 2. Deploy Subject 2: Advanced Accounting-I
    # -------------------------------------------------------------
    print("\n--- [2/2] Deploying Post 2: Advanced Accounting-I ---")
    adv1_thumb_path = os.path.join(PROJECT_ROOT, "assets", "images", "thumbnails", "adv_accounting_1_banner.webp")
    if not os.path.exists(adv1_thumb_path):
        print(f"[ERROR] Thumbnail not found: {adv1_thumb_path}")
        return False
        
    print(f"Uploading featured image: {adv1_thumb_path}...")
    media_id = pub.upload_featured_image(
        adv1_thumb_path,
        alt_text="অনার্স ৩য় বর্ষ উন্নত হিসাববিজ্ঞান ১ সাজেশন",
        title="অনার্স ৩য় বর্ষ উন্নত হিসাববিজ্ঞান ১ সাজেশন 2026"
    )
    print(f"✅ Featured Media Uploaded! Media ID: {media_id}")
    
    adv1_html_path = os.path.join(PROJECT_ROOT, "scratch", "adv1_master_245.html")
    with open(adv1_html_path, "r", encoding="utf-8") as f:
        adv1_content = f.read()
        
    adv1_title = "অনার্স ৩য় বর্ষ উন্নত হিসাববিজ্ঞান ১ সাজেশন 2026: Best Complete Exam Guide"
    adv1_slug = "honours-3rd-year-advanced-accounting-1-suggestion"
    adv1_focus_kw = "অনার্স ৩য় বর্ষ উন্নত হিসাববিজ্ঞান ১ সাজেশন"
    adv1_meta_desc = "অনার্স ৩য় বর্ষ উন্নত হিসাববিজ্ঞান ১ সাজেশন 2026: জাতীয় বিশ্ববিদ্যালয় BBA হিসাববিজ্ঞান বিভাগের ক, খ ও গ বিভাগের ২৪৫টি প্রশ্নের সমাধান।"
    
    adv1_seo_meta = {
        "title": adv1_title,
        "seo_title": adv1_title,
        "search_desc": adv1_meta_desc,
        "focus_keyword": f"{adv1_focus_kw}, Honours 3rd Year Advanced Accounting 1 Suggestion"
    }
    
    # Check if a post with this slug already exists to prevent duplicate creation
    existing_check = pub.client.get("posts", params={"slug": adv1_slug, "status": "any"})
    if existing_check.status_code == 200 and existing_check.json():
        existing_post = existing_check.json()[0]
        post2_id = existing_post.get("id")
        print(f"Found existing post for slug '{adv1_slug}' (ID: {post2_id}). Updating...")
        res2 = pub.update_post(
            post2_id,
            title=adv1_title,
            content=adv1_content,
            categories=[4, 9],
            featured_media=media_id,
            meta={
                "rank_math_title": adv1_title,
                "rank_math_description": adv1_meta_desc,
                "rank_math_focus_keyword": f"{adv1_focus_kw}, Honours 3rd Year Advanced Accounting 1 Suggestion",
                "rank_math_robots": "index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large"
            }
        )
        post2_url = existing_post.get("link")
        edit_url = f"{pub.client.base_url}/wp-admin/post.php?post={post2_id}&action=edit"
    else:
        print(f"Creating new post for slug '{adv1_slug}'...")
        res2 = pub.create_post(
            title=adv1_title,
            content=adv1_content,
            slug=adv1_slug,
            categories=[4, 9],
            status="draft",
            featured_media_id=media_id,
            seo_meta=adv1_seo_meta
        )
        post2_id = res2.get("id")
        post2_url = res2.get("url")
        edit_url = res2.get("edit_url")
        
    if res2.get("success"):
        print(f"✅ Post 2 Deployed Successfully!")
        print(f"   ID: {post2_id}")
        print(f"   URL: {post2_url}")
        print(f"   Edit URL: {edit_url}")
        print(f"   Status: {res2.get('status', 'draft')}")
        print(f"   Questions included: 245 (Units 01-05 complete)")
    else:
        print(f"[ERROR] Failed to deploy Post 2:", res2)
        return False
        
    return True

if __name__ == "__main__":
    deploy_all()

