#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/image_generator/build_ssc_bangla_poetry_banner.py
Generates the official 16:9 featured banner for Post 04:
SSC 2027 Bangla 1st Paper Poetry CQ & Theme Suggestions using 'Thumbnail BG/bg_3.png'.
"""

import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.image_generator.build_official_bg_thumbnails import generate_official_bg_banner

BANNER_CONFIG = {
    "filename": "ssc_bangla_1st_paper_poetry_cq_2027.png",
    "category_key": "Education Guide",
    "badge_label": "SSC 2027 | বাংলা কবিতাংশ",
    "custom_tag_text": "কবিতাংশ সৃজনশীল ও ভাবার্থ",
    "title": "SSC 2027 Bangla 1st Poetry CQ Guide",
    "subtitle": "কবিতাংশ সৃজনশীল প্রশ্ন ও উত্তর — কপোতাক্ষ নদ, বন্দনা ও স্বাধীনতা",
    "features": ["কপোতাক্ষ নদ ও বন্দনা", "তোমাকে পাওয়ার জন্যে স্বাধীনতা", "জীবন বিনিময় ও বঙ্গবাণী", "বোর্ড মডেল CQ সমাধান"]
}

def main():
    print("=" * 70)
    print("🎨 GENERATING BILINGUAL BANNER FOR BANGLA 1ST POETRY CQ (POST 04)...")
    print("=" * 70)

    out_webp = generate_official_bg_banner(
        filename=BANNER_CONFIG["filename"],
        category_key=BANNER_CONFIG["category_key"],
        badge_label=BANNER_CONFIG["badge_label"],
        title=BANNER_CONFIG["title"],
        subtitle=BANNER_CONFIG["subtitle"],
        features=BANNER_CONFIG["features"],
        custom_tag_text=BANNER_CONFIG["custom_tag_text"]
    )

    print(f"\n[✔] Master Banner Generated: {out_webp}")
    if os.path.exists(out_webp):
        size_kb = os.path.getsize(out_webp) / 1024
        print(f"    Size: {size_kb:.2f} KB (Target: 10-20 KB)")

if __name__ == "__main__":
    main()
