#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/image_generator/build_nu_digitization_banner.py
------------------------------------------------------
Generates the official 16:9 featured banner for:
জাতীয় বিশ্ববিদ্যালয়ের পরীক্ষা ডিজিটালাইজেশন ও একিউএ গ্লোবাল চুক্তি ২০২৬
"""

import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.image_generator.build_official_bg_thumbnails import generate_official_bg_banner

BANNER_CONFIG = {
    "filename": "nu_exam_digitization_aqa_global_mou_2026.png",
    "category_key": "Education Guide",
    "badge_label": "জাতীয় বিশ্ববিদ্যালয় • পরীক্ষা সংস্কার ২০২৬",
    "custom_tag_text": "NU & AQA Global MoU • আন্তর্জাতিক মূল্যায়ন রূপরেখা",
    "title": "NU Exam Digitization & AQA Global MoU",
    "subtitle": "পরীক্ষা ডিজিটালাইজেশন ও একিউএ গ্লোবাল ঐতিহাসিক চুক্তি",
    "features": [
        "পরীক্ষা ও মূল্যায়ন সম্পূর্ণ ডিজিটাল",
        "অক্সফোর্ড একিউএ স্বীকৃতি",
        "মানবিক ভুল ও সেশনজট নিরসন",
        "আন্তর্জাতিক সনদের গ্রহণযোগ্যতা"
    ]
}

def main():
    print("=" * 70)
    print("GENERATING OFFICIAL BANNER FOR NU EXAM DIGITIZATION & AQA GLOBAL...")
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
