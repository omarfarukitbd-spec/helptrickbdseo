#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/image_generator/build_ssc_bangla_1st_banner.py
Generates the official 16:9 featured banner for SSC & Dakhil Bangla 1st Paper Final Suggestion 2027
using the authentic 'Thumbnail BG/bg_3.png' template.
"""

import os
import sys
import shutil

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.image_generator.build_official_bg_thumbnails import generate_official_bg_banner

POSTS_DIR = os.path.join(PROJECT_ROOT, "assets", "images", "posts")
THUMBS_DIR = os.path.join(PROJECT_ROOT, "assets", "images", "thumbnails")

BANNER_CONFIG = {
    "filename": "ssc_bangla_1st_paper_final_suggestion_2027.png",
    "category_key": "Education Guide",
    "badge_label": "SSC 2027 | বাংলা ১ম পত্র",
    "custom_tag_text": "এসএসসি ও দাখিল পরীক্ষা ২০২৭",
    "title": "SSC Bangla 1st Paper Suggestion 2027",
    "subtitle": "১০০ নম্বরের সম্পূর্ণ সিলেবাস, নতুন মানবণ্টন ও অধ্যায়ভিত্তিক সুপার সাজেশন",
    "features": ["সৃজনশীল প্রশ্ন (৫০)", "বহুনির্বাচনি MCQ (৩০)", "সংক্ষিপ্ত প্রশ্ন (২০)", "১০০% কমন উপযোগী"]
}

def main():
    print("=" * 70)
    print("🎨 GENERATING BILINGUAL BANNER FOR SSC BANGLA 1ST PAPER 2027...")
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
