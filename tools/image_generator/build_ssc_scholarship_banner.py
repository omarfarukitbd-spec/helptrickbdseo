#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/image_generator/build_ssc_scholarship_banner.py
----------------------------------------------------
Generates the official 16:9 featured banner for:
এসএসসি বৃত্তির রেজাল্ট ২০২৬: মেধা ও সাধারণ বৃত্তি তালিকা ও Best Complete Guide (টাকা পাওয়ার নিয়ম)
"""

import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.image_generator.build_official_bg_thumbnails import generate_official_bg_banner

BANNER_CONFIG = {
    "filename": "ssc_scholarship_result_merit_general_list_2026.png",
    "category_key": "Education Guide",
    "badge_label": "এসএসসি বৃত্তি ২০২৬ • সকল শিক্ষা বোর্ড ও মাউশি",
    "custom_tag_text": "SSC Scholarship Result 2026 • মেধা ও সাধারণ বৃত্তি",
    "title": "SSC Scholarship Result 2026",
    "subtitle": "এসএসসি বৃত্তির রেজাল্ট, তালিকা ও ব্যাংক তথ্য এন্ট্রি",
    "features": [
        "সকল বোর্ডের মেধা ও সাধারণ বৃত্তি তালিকা",
        "মেধাবৃত্তিতে মাসে ৬০০, সাধারণে ৩৫০ টাকা",
        "এককালীন অনুদান ও মেয়াদকাল",
        "MIS সফটওয়্যারে ব্যাংক অ্যাকাউন্ট এন্ট্রি"
    ]
}

def main():
    print("=" * 70)
    print("GENERATING OFFICIAL BANNER FOR SSC SCHOLARSHIP RESULT 2026...")
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

    print(f"\n[OK] Master Banner Generated: {out_webp}")
    if os.path.exists(out_webp):
        size_kb = os.path.getsize(out_webp) / 1024
        print(f"    Size: {size_kb:.2f} KB (Target: 10-20 KB)")

if __name__ == "__main__":
    main()
