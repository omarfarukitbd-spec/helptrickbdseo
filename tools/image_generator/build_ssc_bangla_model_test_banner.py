#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/image_generator/build_ssc_bangla_model_test_banner.py
Generates the official 16:9 featured banner for:
SSC বাংলা ১ম পত্র ১০০ নম্বরের পূর্ণাঙ্গ মডেল টেস্ট ও সমাধান ২০২৬-২০২৭.
"""

import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.image_generator.build_official_bg_thumbnails import generate_official_bg_banner

BANNER_CONFIG = {
    "filename": "ssc_bangla_1st_paper_model_test_2027.png",
    "category_key": "Islamic Article",
    "badge_label": "SSC 2027 | ১০০ নম্বরের পূর্ণাঙ্গ টেস্ট",
    "custom_tag_text": "বোর্ড স্ট্যান্ডার্ড মডেল প্রশ্ন ও সমাধান",
    "title": "SSC 2027 Bangla 1st 100-Mark Model Test",
    "subtitle": "বোর্ড স্ট্যান্ডার্ড CQ, MCQ ও সংক্ষিপ্ত প্রশ্ন ২০২৭",
    "features": ["১০০ নম্বরের পূর্ণাঙ্গ টেস্ট", "৩০ বহুনির্বাচনি ও উত্তরমালা", "৫০ নম্বরের সৃজনশীল", "২০ নম্বরের সংক্ষিপ্ত প্রশ্ন"]
}

def main():
    print("=" * 70)
    print("GENERATING BILINGUAL BANNER FOR BANGLA 1ST 100-MARK MODEL TEST...")
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
