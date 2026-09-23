#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/image_generator/build_ssc_bangla_poetry_mcq_banner.py
Generates the official 16:9 featured banner for:
SSC 2027 Bangla 1st Paper Poetry (পদ্যাংশ) 242-MCQ Bank.
"""

import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.image_generator.build_official_bg_thumbnails import generate_official_bg_banner

BANNER_CONFIG = {
    "filename": "ssc_bangla_1st_paper_poetry_mcq_bank_2027.png",
    "category_key": "Education Guide",
    "badge_label": "SSC 2027 | পদ্যাংশ MCQ ব্যাংক",
    "custom_tag_text": "২৪২টি অধ্যায়ভিত্তিক বহুনির্বাচনি",
    "title": "SSC Bangla 1st Paper Poetry MCQ Bank",
    "subtitle": "এসএসসি ও দাখিল বাংলা ১ম পত্র কবিতাংশ ২৪২টি বহুনির্বাচনি প্রশ্ন ও ছন্দ বিশ্লেষণ",
    "features": ["কপোতাক্ষ নদ ও বঙ্গবাণী", "রানার ও পল্লিজননী", "সেইদিন এই মাঠ", "ক্লিক-টু-রিভিল ড্রপডাউন"]
}

def main():
    print("=" * 70)
    print("🎨 GENERATING BILINGUAL BANNER FOR BANGLA 1ST POETRY MCQ BANK...")
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
