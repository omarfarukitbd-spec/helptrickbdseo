#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/image_generator/build_amader_notun_gourabbatha_banner.py
Generates the official 16:9 featured banner for Post 03:
'আমাদের নতুন গৌরবগাথা' (Amader Notun Gourabbatha)
July 2024 Mass Uprising CQ & MCQ Final Guide for SSC & Dakhil 2026-2027.
"""

import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.image_generator.build_official_bg_thumbnails import generate_official_bg_banner

BANNER_CONFIG = {
    "filename": "amader_notun_gourabbatha_cq_mcq_2027.png",
    "category_key": "Education Guide",
    "badge_label": "SSC 2027 | নতুন সিলেবাস",
    "custom_tag_text": "জুলাই গণঅভ্যুত্থান প্রবন্ধ",
    "title": "Amader Notun Gourabbatha CQ & MCQ",
    "subtitle": "আমাদের নতুন গৌরবগাথা — সৃজনশীল প্রশ্ন, অনুধাবন ও বহুনির্বাচনি ফাইনাল গাইড",
    "features": ["জুলাই গণঅভ্যুত্থান ২০২৪", "বোর্ড স্ট্যান্ডার্ড CQ সমাধান", "জ্ঞান ও অনুধাবন ব্যাংক", "১০০% কমন উপযোগী MCQ"]
}

def main():
    print("=" * 70)
    print("🎨 GENERATING BILINGUAL BANNER FOR AMADER NOTUN GOURABBATHA (POST 03)...")
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
