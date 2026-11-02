#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/upload_adv1_year_banners.py
---------------------------------
Uploads the 6 year banners (2019-2024) to the WordPress Media Library.
Saves the resulting Media IDs and URLs to scratch/adv1_year_media.json.
"""

import os
import sys
import json
import requests

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CONFIG_PATH = os.path.join(PROJECT_ROOT, "tools", "wp_publisher", "config.json")
OUTPUT_JSON = os.path.join(PROJECT_ROOT, "scratch", "adv1_year_media.json")
THUMBS_DIR = os.path.join(PROJECT_ROOT, "assets", "images", "thumbnails")

with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
    cfg = json.load(f)

auth = (cfg['wp_user'], cfg['wp_app_password'])
base_url = cfg['wp_url'].rstrip('/')

YEARS = ["2024", "2023", "2022", "2021", "2020", "2019"]
YEAR_BN_MAP = {
    "2024": "২০২৪",
    "2023": "২০২৩",
    "2022": "২০২২",
    "2021": "২০২১",
    "2020": "২০২০",
    "2019": "২০১৯"
}

results = {}

for yr in YEARS:
    yr_bn = YEAR_BN_MAP[yr]
    filename = f"adv_accounting_1_board_{yr}.webp"
    file_path = os.path.join(THUMBS_DIR, filename)
    
    if not os.path.exists(file_path):
        print(f"[ERROR] File not found: {file_path}")
        continue
        
    with open(file_path, 'rb') as f:
        img_data = f.read()
        
    headers = {
        'Content-Type': 'image/webp',
        'Content-Disposition': f'attachment; filename="{filename}"'
    }
    
    title_text = f"প্রশ্নব্যাংক {yr_bn}: উন্নত হিসাববিজ্ঞান ১"
    alt_text = f"প্রশ্নব্যাংক {yr_bn}: উন্নত হিসাববিজ্ঞান ১ (Advanced Accounting 1 Solution {yr})"
    
    print(f"[*] Uploading {filename} ({len(img_data)} bytes)...")
    res = requests.post(f"{base_url}/wp-json/wp/v2/media", data=img_data, headers=headers, auth=auth)
    
    if res.status_code == 201:
        media = res.json()
        mid = media['id']
        murl = media['source_url']
        print(f"    [SUCCESS] Media ID: {mid}, URL: {murl}")
        
        # Update alt text and title
        meta_payload = {
            'title': title_text,
            'alt_text': alt_text,
            'description': f"জাতীয় বিশ্ববিদ্যালয় BBA অনার্স ৩য় বর্ষ {title_text} | HelpTrickBD"
        }
        requests.post(f"{base_url}/wp-json/wp/v2/media/{mid}", json=meta_payload, auth=auth)
        
        results[yr] = {
            'year_en': yr,
            'year_bn': yr_bn,
            'media_id': mid,
            'source_url': murl,
            'alt_text': alt_text,
            'title_text': title_text
        }
    else:
        print(f"    [FAIL] HTTP {res.status_code}: {res.text[:150]}")

os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\n[DONE] Saved media metadata for {len(results)} banners to {OUTPUT_JSON}")

