#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/consolidate_sparse_labels.py
----------------------------------------------------
Consolidates the 4 sparse labels (< 4 posts) across 5 posts into established
thematic pillars (mainly 'Education Guide') to comply with Rule 04
(Label Taxonomy Governance) and Google AdSense Under Construction policies.
Backs up all posts before modifying (Rule 07).
Strictly Zero Emojis (Rule 12).
"""

import os
import sys
import json
import time

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID

BACKUP_DIR = os.path.join(PROJECT_ROOT, "backups", "posts", "2026-10-05_label_consolidation_backup")
os.makedirs(BACKUP_DIR, exist_ok=True)

TARGET_POST_UPDATES = {
    # 1. NU Honours Promotion Guide
    "7901118775212196810": {
        "title": "জাতীয় বিশ্ববিদ্যালয় অনার্স ২য় বর্ষ পরীক্ষার গাইড ও ৩য় বর্ষে প্রমোশনের নিয়মাবলী ২০২৬",
        "new_labels": ["Education Guide"]
    },
    # 2. NU Exam Digitization AQA Global
    "7338193345529576604": {
        "title": "জাতীয় বিশ্ববিদ্যালয়ের পরীক্ষা ডিজিটালাইজেশন ও একিউএ গ্লোবাল চুক্তি: পরীক্ষা ও মূল্যায়নে ঐতিহাসিক পরিবর্তন",
        "new_labels": ["Education Guide"]
    },
    # 3. NU Degree 2nd Year In-Course & Exam Routine
    "3467234920665395308": {
        "title": "জাতীয় বিশ্ববিদ্যালয় ডিগ্রি ২য় বর্ষ ইনকোর্স নম্বর এন্ট্রি ও পরীক্ষার গাইড ২০২৬ | NU Degree 2nd Year In-Course & Exam Routine",
        "new_labels": ["Education Guide"]
    },
    # 4. NU Honours 2nd Year Exam Routine
    "1085826635177863206": {
        "title": "জাতীয় বিশ্ববিদ্যালয় অনার্স ২য় বর্ষ পরীক্ষার রুটিন ২০২৬ (সকল বিভাগ) | NU Honours 2nd Year Exam Routine & Subject Code",
        "new_labels": ["Education Guide"]
    },
    # 5. Public University Admission Guide
    "3461036492670206540": {
        "title": "পাবলিক বিশ্ববিদ্যালয় ভর্তি যোগ্যতা ২০২৬: বিজ্ঞান, মানবিক ও ব্যবসায় শাখা পূর্ণাঙ্গ গাইড (Public University Admission Guide 2026)",
        "new_labels": ["Education", "Education Guide"]
    }
}

def consolidate_labels():
    service = get_authenticated_service()
    if not service:
        print("[ERROR] Auth failed.")
        return False
        
    print("=" * 60)
    print("STEP 1: BACKING UP TARGET POSTS (Rule 07)")
    print("=" * 60)
    manifest = []
    for pid, data in TARGET_POST_UPDATES.items():
        post = service.posts().get(blogId=BLOG_ID, postId=pid, view="ADMIN").execute()
        fpath = os.path.join(BACKUP_DIR, f"{pid}.json")
        with open(fpath, "w", encoding="utf-8") as out:
            json.dump(post, out, ensure_ascii=False, indent=2)
            
        manifest.append({
            "id": pid,
            "title": post.get("title"),
            "old_labels": post.get("labels", []),
            "new_labels": data["new_labels"],
            "url": post.get("url")
        })
        print(f"[BACKUP OK] {pid} | Current labels: {post.get('labels', [])}")
        
    with open(os.path.join(BACKUP_DIR, "manifest.json"), "w", encoding="utf-8") as mf:
        json.dump(manifest, mf, ensure_ascii=False, indent=2)
        
    print("\n" + "=" * 60)
    print("STEP 2: UPDATING LABELS ON LIVE BLOGGER")
    print("=" * 60)
    
    for pid, data in TARGET_POST_UPDATES.items():
        post = service.posts().get(blogId=BLOG_ID, postId=pid, view="ADMIN").execute()
        old_labels = post.get("labels", [])
        post["labels"] = data["new_labels"]
        
        updated_post = service.posts().update(
            blogId=BLOG_ID,
            postId=pid,
            body=post
        ).execute()
        
        print(f"[UPDATED] {pid}")
        print(f"  Title: {updated_post.get('title')[:60]}...")
        print(f"  Old Labels: {old_labels}")
        print(f"  New Labels: {updated_post.get('labels')}")
        print("-" * 50)
        time.sleep(1)
        
    print("\n" + "=" * 60)
    print("ALL 5 POST LABELS SUCCESSFULLY CONSOLIDATED ON BLOGGER!")
    print("=" * 60)
    return True

if __name__ == "__main__":
    consolidate_labels()
