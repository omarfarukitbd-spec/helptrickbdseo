#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/wp_remediator/fix_post_15924_rank_math.py
----------------------------------------------
Fixes Rank Math SEO score for Post 15924:
- Aligns Focus Keyword with SEO Title (resolves "Focus Keyword does not appear in the SEO title")
- Adds English secondary keyword matching permalink slug
- Satisfies Title Readability (Number '2026', Power Word 'Complete Guide', Sentiment 'Best')
- Aligns First 10% content, H2 subheading, and Image Alt text
"""

import os
import sys
import json
import re
import requests

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CONFIG_PATH = os.path.join(PROJECT_ROOT, "tools", "wp_publisher", "config.json")

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    cfg = json.load(f)

auth = (cfg["wp_user"], cfg["wp_app_password"])
base_url = cfg["wp_url"].rstrip("/")

post_id = 15924

# 1. Fetch current post
res = requests.get(f"{base_url}/wp-json/wp/v2/posts/{post_id}?context=edit", auth=auth)
if res.status_code != 200:
    print(f"[ERROR] Failed to fetch post {post_id}: {res.status_code}")
    sys.exit(1)

post = res.json()
content = post["content"]["raw"]

primary_kw = "৮ম শ্রেণির জুনিয়র বৃত্তি পরীক্ষার রুটিন 2026"
secondary_kw = "class 8 junior scholarship exam routine 2026"
full_focus_kw = f"{primary_kw}, {secondary_kw}"

new_title = "৮ম শ্রেণির জুনিয়র বৃত্তি পরীক্ষার রুটিন 2026: পরীক্ষার মানবণ্টন ও Best Complete Guide (সুপার সাজেশন)"
new_desc = "৮ম শ্রেণির জুনিয়র বৃত্তি পরীক্ষার রুটিন 2026 ও সময়সূচি প্রকাশিত। ২০ ডিসেম্বর শুরু পরীক্ষার মানবণ্টন, বিষয়ভিত্তিক সিলেবাস ও অফিসিয়াল নির্দেশিকা।"

# 2. In-content updates
# A. First paragraph (first 10%)
content = content.replace(
    "৮ম শ্রেণির জুনিয়র বৃত্তি পরীক্ষা ২০২৬",
    primary_kw
)

# B. Section 2 Heading (H2)
content = content.replace(
    "২. ৮ম শ্রেণির জুনিয়র বৃত্তি পরীক্ষার রুটিন ও সময়সূচি",
    f"২. {primary_kw} ও সময়সূচি"
)

# C. Image alt
content = re.sub(
    r'alt="[^"]*"',
    f'alt="{primary_kw} ও মানবণ্টন গাইড"',
    content,
    count=1
)

# D. Image title
content = re.sub(
    r'title="[^"]*"',
    f'title="{primary_kw}"',
    content,
    count=1
)

# 3. Payload
payload = {
    "title": new_title,
    "content": content,
    "meta": {
        "rank_math_title": new_title,
        "rank_math_description": new_desc,
        "rank_math_focus_keyword": full_focus_kw,
        "rank_math_robots": "index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large",
        "rank_math_canonical_url": ""
    }
}

update_res = requests.post(f"{base_url}/wp-json/wp/v2/posts/{post_id}", json=payload, auth=auth)
if update_res.status_code == 200:
    print("[SUCCESS] Post 15924 updated successfully!")
    updated_data = update_res.json()
    print("New Title:", updated_data.get("title", {}).get("raw"))
    print("New Focus KW:", updated_data.get("meta", {}).get("rank_math_focus_keyword"))
    print("New SEO Title:", updated_data.get("meta", {}).get("rank_math_title"))
else:
    print(f"[ERROR] Failed to update post: {update_res.status_code} - {update_res.text[:200]}")
