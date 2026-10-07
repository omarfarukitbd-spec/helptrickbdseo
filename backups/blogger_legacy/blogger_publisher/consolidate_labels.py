#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/consolidate_labels.py
---------------------------------------------
Consolidates Blogger's fragmented 28+ labels into the 5 Official Core Pillars:
1. Political Science
2. Education Guide
3. Islamic Article
4. Job Study Article
5. ICT Guide

Eliminates single-post micro-labels, solves AdSense category imbalance,
and restores clean navigation to the website.
"""

import os
import sys
import io
import argparse

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.update_post import get_authenticated_service, BLOG_ID

# Official 5 Pillars
APPROVED_PILLARS = {
    "Political Science",
    "Education Guide",
    "Islamic Article",
    "Job Study Article",
    "ICT Guide"
}

# Mapping table from fragmented micro-labels to Core Pillars
LABEL_MAPPING = {
    # ICT / Tech
    "কম্পিউটার ও তথ্যপ্রযুক্তি": "ICT Guide",
    "কম্পিউটার শিক্ষা": "ICT Guide",
    "তথ্য ও যোগাযোগ প্রযুক্তি": "ICT Guide",
    "ICT Guide": "ICT Guide",
    
    # Jobs & Career
    "চাকরি প্রস্তুতি": "Job Study Article",
    "বিসিএস প্রস্তুতি": "Job Study Article",
    "ক্যারিয়ার গাইড": "Job Study Article",
    "Job Study Article": "Job Study Article",
    
    # Education
    "Education Guide": "Education Guide",
    "Class 6": "Education Guide",
    "Honours 4th year": "Education Guide",
    "সার্টিফিকেট সংশোধন": "Education Guide",
    "Motivational Speech": "Education Guide",
    "শিশু বিকাশ ও মনস্তত্ত্ব": "Education Guide",
    "কৃষি ও প্রাণিসম্পদ": "Education Guide",
    "বাংলা সাহিত্য": "Education Guide",
    
    # Islamic
    "Islamic Article": "Islamic Article",
    
    # Political Science & Academic
    "Political Science": "Political Science",
    "মাস্টার্স রাষ্ট্রবিজ্ঞান": "Political Science",
    "Masters": "Political Science",
    "বাংলাদেশ অর্থনীতি": "Political Science",
    "বাংলাদেশ বিষয়াবলি": "Political Science",
    "বাংলাদেশ সরকার ও রাজনীতি": "Political Science",
    "অর্থনীতি ও শাসন": "Political Science",
    "সমাজবিজ্ঞান": "Political Science",
    "সমাজকর্ম": "Political Science",
    "ইতিহাস ও সমাজ সংস্কার": "Political Science",
    "শিল্প ও বাণিজ্য": "Political Science",
}

def map_post_labels(current_labels, title=""):
    """Maps arbitrary labels to one or two core pillars."""
    new_labels = set()
    for l in current_labels:
        l_clean = l.strip()
        if l_clean in LABEL_MAPPING:
            new_labels.add(LABEL_MAPPING[l_clean])
            
    # Fallback to title keywords if empty
    if not new_labels:
        t_low = title.lower()
        if any(w in t_low for w in ["রাষ্ট্র", "রাজনীতি", "সরকার", "সার্বভৌম", "political", "masters"]):
            new_labels.add("Political Science")
        elif any(w in t_low for w in ["কম্পিউটার", "ক্লাউড", "ভাইরাস", "আইসিটি", "ict", "computer"]):
            new_labels.add("ICT Guide")
        elif any(w in t_low for w in ["চাকরি", "বিসিএস", "ভাইভা", "শিক্ষক নিয়োগ", "viva", "bcs"]):
            new_labels.add("Job Study Article")
        elif any(w in t_low for w in ["ক্বাসিদা", "ইসলাম", "দুরুদ", "আল্লাহ", "সালাত", "qasida", "islamic"]):
            new_labels.add("Islamic Article")
        else:
            new_labels.add("Education Guide")
            
    # Return sorted list of approved pillars
    return sorted([l for l in new_labels if l in APPROVED_PILLARS])

def run_consolidation(apply_changes=False):
    service = get_authenticated_service()
    if not service:
        print("Failed to authenticate with Blogger API.")
        return

    print("=" * 75)
    print("🏷️  HELPTRICKBD LABEL CONSOLIDATION ENGINE")
    print(f"Mode: {'APPLYING LIVE CHANGES' if apply_changes else 'DRY RUN (PREVIEW ONLY)'}")
    print("=" * 75)

    posts_res = service.posts().list(blogId=BLOG_ID, maxResults=100, fetchBodies=False).execute()
    posts = posts_res.get("items", [])
    print(f"Fetched {len(posts)} total published posts from Blogger.\n")

    updated_count = 0
    post_plan = []

    for p in posts:
        pid = p["id"]
        title = p["title"]
        curr_labels = p.get("labels", [])
        new_labels = map_post_labels(curr_labels, title)

        if set(curr_labels) != set(new_labels):
            updated_count += 1
            post_plan.append({
                "id": pid,
                "title": title,
                "old": curr_labels,
                "new": new_labels
            })
            print(f"[*] {title[:55]}...")
            print(f"    OLD: {curr_labels}")
            print(f"    NEW: {new_labels}\n")

    print("-" * 75)
    print(f"Total posts requiring label update: {updated_count} out of {len(posts)}")
    print("-" * 75)

    if apply_changes:
        print(f"\nApplying updates to {len(post_plan)} posts on Blogger live...")
        for idx, item in enumerate(post_plan, 1):
            try:
                service.posts().patch(
                    blogId=BLOG_ID,
                    postId=item["id"],
                    body={"labels": item["new"]}
                ).execute()
                print(f"  [{idx}/{len(post_plan)}] Updated: {item['title'][:45]} -> {item['new']}")
            except Exception as e:
                print(f"  [ERROR] Failed to update {item['id']}: {e}", file=sys.stderr)

        print("\n" + "=" * 75)
        print("🎉 ALL POST LABELS CONSOLIDATED SUCCESSFULLY ON BLOGGER!")
        print("=" * 75)
    else:
        print("\nDry-run complete. Run with --apply to push updates to Blogger.")

def main():
    parser = argparse.ArgumentParser(description="Consolidate Blogger Labels into 5 Core Pillars")
    parser.add_argument("--apply", action="store_true", help="Apply updates to live Blogger posts")
    args = parser.parse_args()
    run_consolidation(apply_changes=args.apply)

if __name__ == "__main__":
    main()
