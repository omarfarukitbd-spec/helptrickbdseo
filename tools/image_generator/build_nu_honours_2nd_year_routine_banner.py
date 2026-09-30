#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/image_generator/build_nu_honours_2nd_year_routine_banner.py
-----------------------------------------------------------------
Generates the official 16:9 featured banner for:
জাতীয় বিশ্ববিদ্যালয় অনার্স ২য় বর্ষ পরীক্ষার রুটিন ২০২৬ (সকল বিভাগ) | NU Honours 2nd Year Exam Routine 2026.
"""

import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.image_generator.build_official_bg_thumbnails import generate_official_bg_banner

BANNER_CONFIG = {
    "filename": "nu_honours_2nd_year_routine_2026.png",
    "category_key": "Education Guide",
    "badge_label": "অনার্স পরীক্ষা ২০২৬ | জাতীয় বিশ্ববিদ্যালয়",
    "custom_tag_text": "সকল বিভাগ • নিয়মিত, অনিয়মিত ও গ্রেড উন্নয়ন",
    "title": "NU Honours 2nd Year Exam Routine 2026",
    "subtitle": "অনার্স ২য় বর্ষ পরীক্ষার পূর্ণাঙ্গ সময়সূচি ও কোড",
    "features": [
        "সকল বিভাগের পূর্ণাঙ্গ রুটিন",
        "ইংরেজি আবশ্যিক পাস শর্টকাট",
        "হিসাব, ব্যবস্থাপনা ও রাষ্ট্রবিজ্ঞান",
        "গ্রেডিং ও প্রমোশন নিয়মাবলী"
    ]
}

def main():
    print("=" * 70)
    print("GENERATING OFFICIAL BANNER FOR NU HONOURS 2ND YEAR ROUTINE 2026...")
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
