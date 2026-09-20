#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/deploy_4_ready_posts.py
------------------------------------------------
Deploys and updates the 4 ready posts on Helptrickbd:
- Post 1: New post -> 2-Step Minting Protocol (Slug: federal-government-features-and-functions)
- Post 2: Live post (ID: 3708406842330148411) -> Pre-edit backup + Update
- Post 3: Live post (ID: 3998042912898607308) -> Pre-edit backup + Update
- Post 4: Live post (ID: 5898560761534163519) -> Pre-edit backup + Update

Followed by Google Indexing API ping and WebSub Hub pinger.
"""

import os
import sys
import json
import time
import subprocess

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID
from tools.backup_manager.post_backup_manager import create_post_backup

service = get_authenticated_service()
if not service:
    print("[ERROR] Failed to authenticate Blogger API v3.")
    sys.exit(1)

results = []

# ==============================================================================
# 1. POST 1: যুক্তরাষ্ট্রীয় সরকার (NEW POST - 2-STEP MINTING PROTOCOL)
# ==============================================================================
print("\n" + "="*75)
print("1. DEPLOYING POST 1: যুক্তরাষ্ট্রীয় সরকারের বৈশিষ্ট্য ও কার্যাবলী (NEW POST)")
print("="*75)

post1_html_path = os.path.join(PROJECT_ROOT, "output_posts", "যকতরষটরয-সরকরর-বশষটয-ও-করযবল.html")
with open(post1_html_path, "r", encoding="utf-8") as f:
    post1_content = f.read()

post1_slug = "federal-government-features-and-functions"
post1_title = "যুক্তরাষ্ট্রীয় সরকারের বৈশিষ্ট্য ও কার্যাবলী: সংজ্ঞা, তুলনামূলক ছক ও পূর্ণাঙ্গ হ্যান্ডনোট (২০২৬)"
post1_labels = ["Political Science"]

print(f"Step 1: Minting clean English permalink with title: '{post1_slug}'...")
mint_body = {
    "kind": "blogger#post",
    "blog": {"id": BLOG_ID},
    "title": post1_slug,
    "content": post1_content,
    "labels": post1_labels
}
minted_post = service.posts().insert(blogId=BLOG_ID, body=mint_body, isDraft=False).execute()
post1_id = minted_post.get("id")
post1_url = minted_post.get("url")
print(f"   Minted Post ID: {post1_id}")
print(f"   Minted URL:     {post1_url}")

print(f"Step 2: Patching title to full Bengali title: '{post1_title}'...")
patch_body = {"title": post1_title}
updated_post1 = service.posts().patch(blogId=BLOG_ID, postId=post1_id, body=patch_body).execute()
print(f"   Final Title:    {updated_post1.get('title')}")
print(f"   Confirmed URL:  {updated_post1.get('url')}")

results.append({
    "post_id": post1_id,
    "action": "new_minted",
    "title": post1_title,
    "url": post1_url,
    "labels": post1_labels
})


# ==============================================================================
# 2. POST 2: বিসিএস প্রিলিমিনারি মানবণ্টন (EXISTING LIVE POST)
# ==============================================================================
print("\n" + "="*75)
print("2. UPDATING POST 2: বিসিএস প্রিলিমিনারি ২০০ নম্বরের মানবণ্টন ও বুক লিস্ট")
print("="*75)

post2_id = "3708406842330148411"
post2_html_path = os.path.join(PROJECT_ROOT, "output_posts", "new_silo_posts", "bcs-preliminary-marks-distribution-booklist.html")
with open(post2_html_path, "r", encoding="utf-8") as f:
    post2_content = f.read()

post2_title = "বিসিএস প্রিলিমিনারি ২০০ নম্বরের বিষয়ভিত্তিক মানবণ্টন ও প্রথমবারে পাসের পূর্ণাঙ্গ বুক লিস্ট"

print(f"Step 1: Fetching current live post for backup (ID: {post2_id})...")
orig_post2 = service.posts().get(blogId=BLOG_ID, postId=post2_id, view="ADMIN").execute()
backup_dir2 = create_post_backup(orig_post2, reason="pre_enrichment_update_4434_words")
print(f"   Pre-edit backup secured in: {backup_dir2}")

print(f"Step 2: Updating post content (4,434 words) and title...")
update_body2 = {
    "title": post2_title,
    "content": post2_content,
    "labels": orig_post2.get("labels", ["Job Study Article"])
}
updated_post2 = service.posts().patch(blogId=BLOG_ID, postId=post2_id, body=update_body2).execute()
print(f"   Updated Title: {updated_post2.get('title')}")
print(f"   Live URL:      {updated_post2.get('url')}")
print(f"   Labels:        {updated_post2.get('labels')}")

results.append({
    "post_id": post2_id,
    "action": "updated_live",
    "title": post2_title,
    "url": updated_post2.get("url"),
    "labels": updated_post2.get("labels")
})


# ==============================================================================
# 3. POST 3: কম্পিউটার ভাইরাস ও সাইবার নিরাপত্তা (EXISTING LIVE POST)
# ==============================================================================
print("\n" + "="*75)
print("3. UPDATING POST 3: কম্পিউটার ভাইরাস ও সাইবার নিরাপত্তা (২০২৬)")
print("="*75)

post3_id = "3998042912898607308"
post3_html_path = os.path.join(PROJECT_ROOT, "output_posts", "new_silo_posts", "computer-virus-and-cyber-security-guide-2026.html")
with open(post3_html_path, "r", encoding="utf-8") as f:
    post3_content = f.read()

post3_title = "কম্পিউটার ভাইরাস ও সাইবার নিরাপত্তা: ম্যালওয়্যার থেকে ডাটা সুরক্ষার সেরা উপায় (২০২৬)"

print(f"Step 1: Fetching current live post for backup (ID: {post3_id})...")
orig_post3 = service.posts().get(blogId=BLOG_ID, postId=post3_id, view="ADMIN").execute()
backup_dir3 = create_post_backup(orig_post3, reason="pre_enrichment_update_3807_words")
print(f"   Pre-edit backup secured in: {backup_dir3}")

print(f"Step 2: Updating post content (3,807 words) and title...")
update_body3 = {
    "title": post3_title,
    "content": post3_content,
    "labels": orig_post3.get("labels", ["ICT Guide"])
}
updated_post3 = service.posts().patch(blogId=BLOG_ID, postId=post3_id, body=update_body3).execute()
print(f"   Updated Title: {updated_post3.get('title')}")
print(f"   Live URL:      {updated_post3.get('url')}")
print(f"   Labels:        {updated_post3.get('labels')}")

results.append({
    "post_id": post3_id,
    "action": "updated_live",
    "title": post3_title,
    "url": updated_post3.get("url"),
    "labels": updated_post3.get("labels")
})


# ==============================================================================
# 4. POST 4: প্রাথমিক শিক্ষক নিয়োগ ও ভাইভা (EXISTING LIVE POST)
# ==============================================================================
print("\n" + "="*75)
print("4. UPDATING POST 4: সরকারি প্রাথমিক শিক্ষক নিয়োগ ও ভাইভা প্রস্তুতি")
print("="*75)

post4_id = "5898560761534163519"
post4_html_path = os.path.join(PROJECT_ROOT, "output_posts", "new_silo_posts", "primary-teacher-job-viva-preparation-guideline.html")
with open(post4_html_path, "r", encoding="utf-8") as f:
    post4_content = f.read()

post4_title = "সরকারি প্রাথমিক শিক্ষক নিয়োগ ও চাকরির ভাইভা প্রস্তুতি গাইডলাইন (২০২৬)"

print(f"Step 1: Fetching current live post for backup (ID: {post4_id})...")
orig_post4 = service.posts().get(blogId=BLOG_ID, postId=post4_id, view="ADMIN").execute()
backup_dir4 = create_post_backup(orig_post4, reason="pre_enrichment_update_4505_words")
print(f"   Pre-edit backup secured in: {backup_dir4}")

print(f"Step 2: Updating post content (4,505 words) and title...")
update_body4 = {
    "title": post4_title,
    "content": post4_content,
    "labels": orig_post4.get("labels", ["Job Study Article"])
}
updated_post4 = service.posts().patch(blogId=BLOG_ID, postId=post4_id, body=update_body4).execute()
print(f"   Updated Title: {updated_post4.get('title')}")
print(f"   Live URL:      {updated_post4.get('url')}")
print(f"   Labels:        {updated_post4.get('labels')}")

results.append({
    "post_id": post4_id,
    "action": "updated_live",
    "title": post4_title,
    "url": updated_post4.get("url"),
    "labels": updated_post4.get("labels")
})

# Save deployment manifest
manifest_path = os.path.join(PROJECT_ROOT, "output_posts", "deployed_4_posts_manifest.json")
with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print(f"\nSaved deployment record: {manifest_path}")

# ==============================================================================
# 5. GOOGLE INDEXING API & WEBSUB HUB PINGING
# ==============================================================================
print("\n" + "="*75)
print("5. SUBMITTING URLS TO GOOGLE INDEXING API & WEBSUB HUB")
print("="*75)

indexer_script = os.path.join(PROJECT_ROOT, "tools", "indexer", "index_now.py")
for r in results:
    url = r["url"]
    print(f"Submitting to Google Indexing API: {url}...")
    try:
        cmd = [sys.executable, indexer_script, "--url", url]
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        print(f"   Result: {res.stdout.strip()[:100]}")
    except Exception as e:
        print(f"   Indexing warning: {e}")

hub_pinger_script = os.path.join(PROJECT_ROOT, "tools", "indexer", "pubsub_hub_pinger.py")
print("\nPinging Google PubSubHubbub (WebSub) Real-Time Hubs...")
try:
    cmd_hub = [sys.executable, hub_pinger_script]
    res_hub = subprocess.run(cmd_hub, capture_output=True, text=True, timeout=30)
    print(res_hub.stdout.strip())
except Exception as e:
    print(f"WebSub Pinger warning: {e}")

print("\n" + "="*75)
print("ALL 4 POSTS DEPLOYED & INDEXING PINGS COMPLETED SUCCESSFULLY!")
print("="*75)
