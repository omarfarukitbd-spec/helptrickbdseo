#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/deploy_adv_accounting_pair.py
-----------------------------------
Synchronizes the 2 Advanced Accounting-I posts directly to WordPress REST API:
Post 1 (ID 15997): 7 Units, 320 Questions + Master PDF Link
Post 2 (New ID): 6 Board Years (2019-2024), 168 Questions + Board PDF Link
"""

import os
import sys
import json

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.wp_publisher.publisher import WordPressPublisher

def deploy_pair():
    sys.stdout.reconfigure(encoding='utf-8')
    pub = WordPressPublisher()
    
    conn = pub.test_connection()
    if not conn.get("success"):
        print("[ERROR] Failed to connect to WordPress:", conn)
        return False
    print(f"✅ WordPress Connected: User '{conn.get('username')}' (ID: {conn.get('user_id')})")
    
    # ------------------------------------------------------------------
    # 1. Update Post 1: Chapter-wise Suggestion (Post ID 15997)
    # ------------------------------------------------------------------
    print("\n--- [1/2] Updating Post 1: Chapter Suggestion (ID: 15997) ---")
    p1_html_path = os.path.join(PROJECT_ROOT, "scratch", "adv1_suggestion_320.html")
    with open(p1_html_path, "r", encoding="utf-8") as f:
        p1_content = f.read()
        
    p1_title = "অনার্স ৩য় বর্ষ উন্নত হিসাববিজ্ঞান ১ সাজেশন 2026: Best Complete Exam Guide"
    p1_slug = "honours-3rd-year-advanced-accounting-1-suggestion"
    p1_focus_kw = "অনার্স ৩য় বর্ষ উন্নত হিসাববিজ্ঞান ১ সাজেশন"
    p1_meta_desc = "অনার্স ৩য় বর্ষ উন্নত হিসাববিজ্ঞান ১ সাজেশন 2026: জাতীয় বিশ্ববিদ্যালয় BBA ৩য় বর্ষ হিসাববিজ্ঞানের ৭টি অধ্যায়ের ৩২০টি প্রশ্ন ও গাণিতিক সমাধান।"
    
    res1 = pub.update_post(
        15997,
        title=p1_title,
        content=p1_content,
        categories=[4, 9],
        featured_media=15996,
        meta={
            "rank_math_title": p1_title,
            "rank_math_description": p1_meta_desc,
            "rank_math_focus_keyword": f"{p1_focus_kw}, Honours 3rd Year Advanced Accounting 1 Suggestion",
            "rank_math_robots": "index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large"
        }
    )
    if res1.get("success"):
        print(f"✅ Post 1 Updated Successfully!")
        print(f"   ID: 15997")
        print(f"   Slug: {p1_slug}")
        print(f"   Status: draft")
        print(f"   Questions included: 320 (Units 01-07 complete + Master PDF Link)")
    else:
        print(f"[ERROR] Failed to update Post 1:", res1)
        return False

    # ------------------------------------------------------------------
    # 2. Deploy Post 2: Board Questions 2019-2024
    # ------------------------------------------------------------------
    print("\n--- [2/2] Deploying Post 2: Board Questions 2019-2024 ---")
    p2_html_path = os.path.join(PROJECT_ROOT, "scratch", "adv1_board_168.html")
    with open(p2_html_path, "r", encoding="utf-8") as f:
        p2_content = f.read()
        
    p2_title = "উন্নত হিসাববিজ্ঞান ১ বিগত বছরের বোর্ড প্রশ্ন সমাধান (2019-2024): Best Solution Guide"
    p2_slug = "honours-3rd-year-advanced-accounting-1-board-questions"
    p2_focus_kw = "উন্নত হিসাববিজ্ঞান ১ বিগত বছরের বোর্ড প্রশ্ন"
    p2_meta_desc = "উন্নত হিসাববিজ্ঞান ১ বিগত বছরের বোর্ড প্রশ্ন সমাধান (2019-2024): জাতীয় বিশ্ববিদ্যালয় BBA অনার্স ৩য় বর্ষের ১৬৮টি প্রশ্ন ও গাণিতিক সমাধান।"
    
    existing_check = pub.client.get("posts", params={"slug": p2_slug, "status": "any"})
    if existing_check.status_code == 200 and existing_check.json():
        existing_post = existing_check.json()[0]
        p2_id = existing_post.get("id")
        print(f"Found existing post for slug '{p2_slug}' (ID: {p2_id}). Updating...")
        res2 = pub.update_post(
            p2_id,
            title=p2_title,
            content=p2_content,
            categories=[4, 9],
            featured_media=16004,
            meta={
                "rank_math_title": p2_title,
                "rank_math_description": p2_meta_desc,
                "rank_math_focus_keyword": f"{p2_focus_kw}, Advanced Accounting 1 Board Questions",
                "rank_math_robots": "index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large"
            }
        )
        p2_url = existing_post.get("link")
        edit_url = f"{pub.client.base_url}/wp-admin/post.php?post={p2_id}&action=edit"
    else:
        print(f"Creating new post for slug '{p2_slug}'...")
        res2 = pub.create_post(
            title=p2_title,
            content=p2_content,
            slug=p2_slug,
            categories=[4, 9],
            status="draft",
            featured_media_id=16004,
            seo_meta={
                "title": p2_title,
                "seo_title": p2_title,
                "search_desc": p2_meta_desc,
                "focus_keyword": f"{p2_focus_kw}, Advanced Accounting 1 Board Questions"
            }
        )
        p2_id = res2.get("id")
        p2_url = res2.get("url")
        edit_url = res2.get("edit_url")
        
    if res2.get("success"):
        print(f"✅ Post 2 Deployed Successfully!")
        print(f"   ID: {p2_id}")
        print(f"   URL: {p2_url}")
        print(f"   Edit URL: {edit_url}")
        print(f"   Status: draft")
        print(f"   Questions included: 168 (Years 2019-2024 complete + Board PDF Link)")
        return True
    else:
        print(f"[ERROR] Failed to deploy Post 2:", res2)
        return False

if __name__ == "__main__":
    deploy_pair()
