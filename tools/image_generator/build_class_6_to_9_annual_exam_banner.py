#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/image_generator/build_class_6_to_9_annual_exam_banner.py
--------------------------------------------------------------
Generates the official 16:9 featured banner for:
৬ষ্ঠ, ৭ম, ৮ম ও ৯ম শ্রেণির বার্ষিক পরীক্ষার মানবণ্টন ও পূর্ণাঙ্গ প্রস্তুতি গাইড ২০২৬
"""

import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.image_generator.build_official_bg_thumbnails import generate_official_bg_banner

BANNER_CONFIG = {
    "filename": "class_6_to_9_annual_exam_marks_distribution_2026.png",
    "category_key": "Education Guide",
    "badge_label": "বার্ষিক পরীক্ষা ২০২৬ | মাউশি ও এনসিটিবি",
    "custom_tag_text": "৬ষ্ঠ, ৭ম, ৮ম ও ৯ম শ্রেণি • চূড়ান্ত মূল্যায়ন নির্দেশিকা",
    "title": "বার্ষিক পরীক্ষার নতুন মানবণ্টন ও প্রস্তুতি গাইড",
    "subtitle": "৭০% সামষ্টিক লিখিত পরীক্ষা ও ৩০% শিখনকালীন মূল্যায়ন রূপরেখা",
    "features": [
        "৬ষ্ঠ ও ৭ম বিষয়ভিত্তিক ছক",
        "৮ম ও ৯ম সৃজনশীল কাঠামো",
        "জিপিএ (GPA) গ্রেডিং স্কেল",
        "পরীক্ষায় A+ পাওয়ার কৌশল"
    ]
}

def main():
    print("=" * 70)
    print("GENERATING OFFICIAL BANNER FOR CLASS 6-9 ANNUAL EXAM 2026...")
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
