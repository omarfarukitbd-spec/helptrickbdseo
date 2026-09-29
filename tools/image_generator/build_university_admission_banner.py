#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/image_generator/build_university_admission_banner.py
----------------------------------------------------------
Generates the official 16:9 featured banner for:
পাবলিক বিশ্ববিদ্যালয় ভর্তি তথ্য ২০২৬: যোগ্যতা, ইউনিট ও বিষয়ভিত্তিক পূর্ণাঙ্গ গাইড.
"""

import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.image_generator.build_official_bg_thumbnails import generate_official_bg_banner

BANNER_CONFIG = {
    "filename": "public_university_admission_guide_2026.png",
    "category_key": "Education Guide",
    "badge_label": "ভর্তি নির্দেশিকা ২০২৬ | পাবলিক বিশ্ববিদ্যালয়",
    "custom_tag_text": "বিজ্ঞান, মানবিক ও বাণিজ্য শাখার মাস্টার ডিরেক্টরি",
    "title": "Public University Admission Guide 2026",
    "subtitle": "পাবলিক বিশ্ববিদ্যালয় ভর্তি তথ্য ও যোগ্যতা ২০২৬",
    "features": [
        "বিজ্ঞান, মানবিক ও বাণিজ্য",
        "ঢাবি, চবি, রাবি, জাবি ও গুচ্ছ",
        "বিভাগ পরিবর্তন ও বিষয় চয়েস",
        "সেকেন্ড টাইম ও সিট সংখ্যা"
    ]
}

def main():
    print("=" * 70)
    print("GENERATING OFFICIAL BANNER FOR PUBLIC UNIVERSITY ADMISSION GUIDE...")
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
