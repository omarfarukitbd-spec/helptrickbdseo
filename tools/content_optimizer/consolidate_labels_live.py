#!/usr/bin/env python3
"""
HelpTrickBD Label Consolidation Engine
Surgically consolidates 43 fragmented micro-labels into 5 clean, powerhouse parent categories
via Blogger API v3 without modifying article content, titles, or URLs.

Target 5 Categories:
1. Political Science (~54 posts)
2. Islamic Article (~14 posts)
3. Education Guide (~14 posts)
4. Job Study Article (5 posts)
5. ICT Guide (4 posts)
"""

import json
import os
import sys
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from blogger_publisher.update_post import get_authenticated_service, BLOG_ID

# Label Taxonomy Mapping
POLITICAL_SCIENCE_LABELS = {
    'Political Science', 'মাস্টার্স রাষ্ট্রবিজ্ঞান', 'Honours 2nd Year', 'Honours 4th year', 'Masters',
    'বাংলাদেশ সরকার ও রাজনীতি', 'বাংলাদেশ সংবিধান', 'বাংলাদেশ বিষয়াবলি', 'বাংলাদেশ ও মুক্তিযুদ্ধ',
    'বাংলাদেশ অর্থনীতি', 'অর্থনীতি ও শাসন', 'শিল্প ও বাণিজ্য', 'ইতিহাস ও সমাজ সংস্কার',
    'রাষ্ট্রবিজ্ঞান', 'সমাজবিজ্ঞান', 'সমাজকর্ম', 'ভূগোল ও পরিবেশ', 'শিশু বিকাশ ও মনস্তত্ত্ব'
}

ISLAMIC_LABELS = {
    'Islamic Article', 'ক্বাসিদা ও নাত', 'ইসলামিক সাহিত্য', 'সালাত ও সালাম',
    'দুরুদ শরীফ', 'যিকির ও তাসবীহ', 'সুফি সাহিত্য', 'মিলাদ শরীফ'
}

ICT_LABELS = {
    'ICT Guide', 'কম্পিউটার ও তথ্যপ্রযুক্তি'
}

EDU_LABELS = {
    'Education Guide', 'Education News', 'Notice', 'Alim', 'এসএসসি পরীক্ষা',
    'সার্টিফিকেট সংশোধন', 'Primary Math', 'মৌলিক গণিত', 'Class 6 English & Bangla',
    'বাংলা সাহিত্য', 'বাংলা ব্যাকরণ', 'Motivational Speech', 'News', 'কৃষি ও প্রাণিসম্পদ'
}

def map_labels(current_labels):
    new_labels = set()
    for l in current_labels:
        if l in POLITICAL_SCIENCE_LABELS:
            new_labels.add('Political Science')
        elif l in ISLAMIC_LABELS:
            new_labels.add('Islamic Article')
        elif l in ICT_LABELS:
            new_labels.add('ICT Guide')
        elif l == 'Job Study Article':
            new_labels.add('Job Study Article')
        elif l in EDU_LABELS:
            new_labels.add('Education Guide')
        else:
            # Default fallback if unknown
            new_labels.add('Education Guide')
            
    if not new_labels:
        new_labels.add('Political Science')
        
    return sorted(list(new_labels))


def run_consolidation():
    print("=" * 70)
    print("🚀 HelpTrickBD Label Consolidation Starting...")
    print("=" * 70)
    
    service = get_authenticated_service()
    if not service:
        print("[!] Failed to authenticate with Blogger API")
        return
        
    res = service.posts().list(blogId=BLOG_ID, maxResults=150).execute()
    posts = res.get('items', [])
    print(f"[*] Retrieved {len(posts)} posts from Blogger API\n")
    
    updated_count = 0
    skipped_count = 0
    
    for idx, p in enumerate(posts, start=1):
        post_id = p.get('id')
        title = p.get('title')
        current_labels = p.get('labels', [])
        new_labels = map_labels(current_labels)
        
        # Check if change is needed
        if sorted(current_labels) == sorted(new_labels):
            skipped_count += 1
            continue
            
        print(f"[{idx}/{len(posts)}] Updating: {title[:45]}...")
        print(f"    Old Labels: {current_labels}")
        print(f"    New Labels: {new_labels}")
        
        try:
            # Patch ONLY the labels
            service.posts().patch(
                blogId=BLOG_ID,
                postId=post_id,
                body={'labels': new_labels}
            ).execute()
            updated_count += 1
            time.sleep(0.4)  # Respect Blogger rate limits
        except Exception as e:
            print(f"    [!] Error updating post {post_id}: {e}")
            time.sleep(1)
            
    print("\n" + "=" * 70)
    print(f"🎉 [COMPLETED] Label Consolidation Finished Successfully!")
    print(f"  Total Posts Checked: {len(posts)}")
    print(f"  Posts Updated:       {updated_count}")
    print(f"  Posts Already Clean: {skipped_count}")
    print("=" * 70)

if __name__ == '__main__':
    run_consolidation()
