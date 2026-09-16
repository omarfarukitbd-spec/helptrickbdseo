#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/image_generator/build_ssc_2027_silo_thumbnails.py
---------------------------------------------------------
Generates the 5 official 16:9 featured banners for SSC 2027 English 1st Paper
Silo Series using the authentic 'Thumbnail BG/bg_3.png' background template.
Enforces:
1. Pure authentic canvas without dark overlays.
2. Chromium HarfBuzz text-shaping engine for 100% flawless Bengali conjuncts.
3. 10–20 KB Ultra-WebP Core Web Vitals compression.
"""

import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.image_generator.build_official_bg_thumbnails import generate_official_bg_banner

SILO_BANNERS = [
    {
        "filename": "ssc_2027_silo_01_seen_passage.png",
        "category_key": "Education Guide",
        "badge_label": "এসএসসি ২০২৭",
        "custom_tag_text": "এসএসসি ও দাখিল ২০২৭",
        "title": "এসএসসি ২০২৭ ইংরেজি ১ম পত্র সিন প্যাসেজ সাজেশন",
        "subtitle": "MCQ, প্রশ্নোত্তর ও গ্যাপ ফিলিং — ২২ নম্বরের পূর্ণাঙ্গ প্রস্তুতি গাইড",
        "features": ["প্রশ্ন ১: MCQ (৭ নম্বর)", "প্রশ্ন ২: Q/A (১০ নম্বর)", "প্রশ্ন ৩: Gap Fill (৫)", "মডেল সমাধান"]
    },
    {
        "filename": "ssc_2027_silo_02_unseen_summary.png",
        "category_key": "Education Guide",
        "badge_label": "এসএসসি ২০২৭",
        "custom_tag_text": "এসএসসি ও দাখিল ২০২৭",
        "title": "এসএসসি ২০২৭ ইংরেজি ১ম পত্র আনসিন প্যাসেজ ও সামারি",
        "subtitle": "ইনফরমেশন ট্রান্সফার ও সামারি রাইটিং — ১৫ নম্বরের শতভাগ কমন কৌশল",
        "features": ["প্রশ্ন ৪: Info Transfer (৫)", "প্রশ্ন ৫: Summary (১০)", "১/৩ নিয়মে সামারি", "টপ প্র্যাকটিস প্যাসেজ"]
    },
    {
        "filename": "ssc_2027_silo_03_matching_rearrange.png",
        "category_key": "Education Guide",
        "badge_label": "এসএসসি ২০২৭",
        "custom_tag_text": "এসএসসি ও দাখিল ২০২৭",
        "title": "এসএসসি ২০২৭ ইংরেজি ১ম পত্র ম্যাচিং টেবিল ও রি-অ্যারেঞ্জ",
        "subtitle": "Sentence Matching ও Rearranging — ১২ নম্বরের ফুল মার্কস ট্রিকস ও রুলস",
        "features": ["প্রশ্ন ৬: টেবিল ম্যাচিং (৫)", "প্রশ্ন ৭: রি-অ্যারেঞ্জ (৭)", "কালানুক্রমিক ট্রিকস", "বোর্ড সলিউশন ২০২৭"]
    },
    {
        "filename": "ssc_2027_silo_04_poems_stories.png",
        "category_key": "Education Guide",
        "badge_label": "এসএসসি ২০২৭",
        "custom_tag_text": "এসএসসি ও দাখিল ২০২৭",
        "title": "এসএসসি ২০২৭ ইংরেজি কবিতা ও গল্প প্রশ্নোত্তর গাইড",
        "subtitle": "EFT পাঠ্যবইয়ের গুরুত্বপূর্ণ কবিতা ও গল্পের পূর্ণাঙ্গ প্রশ্ন ও মডেল উত্তর",
        "features": ["প্রশ্ন ৮-৯ স্পেশাল গাইড", "গুরুত্বপূর্ণ কবিতা তালিকা", "গল্পভিত্তিক মডেল Q/A", "A+ হ্যান্ডনোট"]
    },
    {
        "filename": "ssc_2027_silo_05_story_dialogue.png",
        "category_key": "Education Guide",
        "badge_label": "এসএসসি ২০২৭",
        "custom_tag_text": "এসএসসি ও দাখিল ২০২৭",
        "title": "এসএসসি ২০২৭ ইংরেজি রাইটিং পার্ট: Story ও Dialogue",
        "subtitle": "Completing Story ও Dialogue Writing — ২৫ নম্বরের ফাইনাল সাজেশন",
        "features": ["প্রশ্ন ১০: Completing Story", "প্রশ্ন ১১: Dialogue Writing", "টাইটেল ও মোরাল ট্রিকস", "টপ কমন সাজেশন ২০২৭"]
    }
]

def main():
    print("=" * 70)
    print("🎨 GENERATING 5 OFFICIAL SSC 2027 SILO BANNERS ON bg_3.png...")
    print("=" * 70)

    generated = []
    for idx, item in enumerate(SILO_BANNERS, 1):
        print(f"\n[{idx}/5] Rendering Banner: {item['title']}")
        print(f"      File:     {item['filename']}")
        print(f"      Category: {item['category_key']} (bg_3.png)")

        out_webp = generate_official_bg_banner(
            filename=item["filename"],
            category_key=item["category_key"],
            badge_label=item["badge_label"],
            title=item["title"],
            subtitle=item["subtitle"],
            features=item["features"],
            custom_tag_text=item["custom_tag_text"]
        )
        generated.append(out_webp)

    print("\n" + "=" * 70)
    print("🎉 ALL 5 OFFICIAL SILO BANNERS GENERATED AND OPTIMIZED TO WEBP (10-20 KB)!")
    print("=" * 70)

if __name__ == "__main__":
    main()
