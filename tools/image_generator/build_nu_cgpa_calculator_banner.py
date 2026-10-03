#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/image_generator/build_nu_cgpa_calculator_banner.py
---------------------------------------------------------
Generates the official 16:9 featured banner for:
জাতীয় বিশ্ববিদ্যালয় সিজিপিএ ক্যালকুলেটর ও গ্রেডিং গাইড ২০২৬
"""

import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.image_generator.build_official_bg_thumbnails import generate_official_bg_banner

BANNER_CONFIG = {
    "filename": "nu_cgpa_calculator_honours_degree_masters_2026.png",
    "category_key": "National University",
    "badge_label": "জাতীয় বিশ্ববিদ্যালয় • একাডেমিক টুল ২০২৬",
    "custom_tag_text": "NU CGPA Calculator • Honours • Degree • Masters",
    "title": "NU CGPA Calculator & Honours Grade Guide",
    "subtitle": "জাতীয় বিশ্ববিদ্যালয় সিজিপিএ ক্যালকুলেটর ও গ্রেডিং গাইড",
    "features": [
        "ইয়ার-ওয়াইজ ও সাবজেক্ট-ভিত্তিক হিসাব",
        "টার্গেট ৩.০০ ও ফার্স্ট ক্লাস প্ল্যানার",
        "ডিপার্টমেন্ট সিলেবাস ও ক্রেডিট অটো-লোড",
        "মানোন্নয়ন (Improvement) সিমুলেটর"
    ]
}

def main():
    print("=" * 70)
    print("GENERATING OFFICIAL BANNER FOR NU CGPA CALCULATOR 2026...")
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
