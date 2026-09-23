#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/image_generator/build_ssc_bangla_cq_banners.py
Generates the official 16:9 featured banners for:
1. SSC 2027 Bangla 1st Paper Prose (গদ্যাংশ) Creative Question (CQ) Bank
2. SSC 2027 Bangla 1st Paper Poetry (কবিতাংশ) Creative Question (CQ) Bank
"""

import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.image_generator.build_official_bg_thumbnails import generate_official_bg_banner

PROSE_BANNER_CONFIG = {
    "filename": "ssc_bangla_1st_paper_prose_cq_bank_2027.png",
    "category_key": "Education Guide",
    "badge_label": "SSC 2027 | গদ্যাংশ CQ ব্যাংক",
    "custom_tag_text": "সব উদ্দীপকের ক, খ, গ, ঘ সমাধান",
    "title": "SSC Bangla 1st Paper Prose CQ Bank",
    "subtitle": "এসএসসি ও দাখিল বাংলা ১ম পত্র গদ্যাংশ সকল সৃজনশীল প্রশ্ন ও ৪ স্তরের পূর্ণাঙ্গ মডেল উত্তর",
    "features": ["প্রত্যুপকার ও সুভা CQ", "বই পড়া ও নিমগাছ সমাধান", "আমাদের নতুন গৌরবগাথা", "বোর্ড স্ট্যান্ডার্ড পূর্ণাঙ্গ উত্তর"]
}

POETRY_BANNER_CONFIG = {
    "filename": "ssc_bangla_1st_paper_poetry_cq_bank_2027.png",
    "category_key": "Education Guide",
    "badge_label": "SSC 2027 | কবিতাংশ CQ ব্যাংক",
    "custom_tag_text": "প্রতিটি কবিতার সৃজনশীল সমাধান",
    "title": "SSC Bangla 1st Paper Poetry CQ Bank",
    "subtitle": "এসএসসি ও দাখিল বাংলা ১ম পত্র কবিতাংশ সকল সৃজনশীল উদ্দীপক ও ভাবার্থ বিশ্লেষণ",
    "features": ["বন্দনা ও কপোতাক্ষ নদ", "প্রাণ ও জীবন বিনিময়", "তোমাকে পাওয়ার জন্যে হে স্বাধীনতা", "১০ এ ১০ পাওয়ার মডেল উত্তর"]
}

def main():
    print("=" * 70)
    print("🎨 GENERATING BILINGUAL BANNERS FOR BANGLA 1ST CQ BANKS...")
    print("=" * 70)

    # 1. Prose CQ Banner
    print("\n--- Generating Prose CQ Banner ---")
    prose_webp = generate_official_bg_banner(
        filename=PROSE_BANNER_CONFIG["filename"],
        category_key=PROSE_BANNER_CONFIG["category_key"],
        badge_label=PROSE_BANNER_CONFIG["badge_label"],
        title=PROSE_BANNER_CONFIG["title"],
        subtitle=PROSE_BANNER_CONFIG["subtitle"],
        features=PROSE_BANNER_CONFIG["features"],
        custom_tag_text=PROSE_BANNER_CONFIG["custom_tag_text"]
    )
    if os.path.exists(prose_webp):
        print(f"[✔] Prose CQ Banner Generated: {prose_webp} ({os.path.getsize(prose_webp)/1024:.2f} KB)")

    # 2. Poetry CQ Banner
    print("\n--- Generating Poetry CQ Banner ---")
    poetry_webp = generate_official_bg_banner(
        filename=POETRY_BANNER_CONFIG["filename"],
        category_key=POETRY_BANNER_CONFIG["category_key"],
        badge_label=POETRY_BANNER_CONFIG["badge_label"],
        title=POETRY_BANNER_CONFIG["title"],
        subtitle=POETRY_BANNER_CONFIG["subtitle"],
        features=POETRY_BANNER_CONFIG["features"],
        custom_tag_text=POETRY_BANNER_CONFIG["custom_tag_text"]
    )
    if os.path.exists(poetry_webp):
        print(f"[✔] Poetry CQ Banner Generated: {poetry_webp} ({os.path.getsize(poetry_webp)/1024:.2f} KB)")

if __name__ == "__main__":
    main()
