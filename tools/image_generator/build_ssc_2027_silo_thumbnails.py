#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/image_generator/build_ssc_2027_silo_thumbnails.py
---------------------------------------------------------
Generates the official 16:9 featured banners for the SSC 2027 English 1st Paper
Pillar and Silo Series using the authentic 'Thumbnail BG/bg_3.png' background template.
Enforces Rule 08:
1. Prominent English Title (Latin Alphabet) for English 1st Paper posts.
2. High-impact Bengali Subtitle & Marks context for student CTR.
3. Authentic bg_3.png Education Guide theme with zero dark overlays.
4. 10–20 KB Ultra-WebP Core Web Vitals compression.
5. Dual CDN aliases for seamless backwards-compatibility.
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

SERIES_BANNERS = [
    {
        "filename": "ssc_english_1st_paper_suggestion_2027.png",
        "category_key": "Education Guide",
        "badge_label": "SSC 2027 | English 1st",
        "custom_tag_text": "এসএসসি ও দাখিল পরীক্ষা ২০২৭",
        "title": "SSC English 1st Paper Suggestion 2027",
        "subtitle": "১০০ নম্বরের পূর্ণাঙ্গ ফাইনাল সাজেশন, সিলেবাস ও মানবণ্টন",
        "features": ["Part A: Reading (70)", "Part B: Writing (30)", "সকল বোর্ড সাজেশন", "১০০% প্রস্তুতি"]
    },
    {
        "filename": "ssc_2027_silo_01_seen_passage.png",
        "category_key": "Education Guide",
        "badge_label": "SSC 2027 | English 1st",
        "custom_tag_text": "এসএসসি ও দাখিল পরীক্ষা ২০২৭",
        "title": "SSC 2027 English Seen Passage Suggestion",
        "subtitle": "সিন প্যাসেজ MCQ, প্রশ্নোত্তর ও গ্যাপ ফিলিং — ২২ নম্বরের প্রস্তুতি",
        "features": ["প্রশ্ন ১: MCQ (৭ নম্বর)", "প্রশ্ন ২: Q/A (১০ নম্বর)", "প্রশ্ন ৩: Gap Fill (৫)", "বোর্ড মডেল সমাধান"]
    },
    {
        "filename": "ssc_2027_silo_02_unseen_summary.png",
        "category_key": "Education Guide",
        "badge_label": "SSC 2027 | English 1st",
        "custom_tag_text": "এসএসসি ও দাখিল পরীক্ষা ২০২৭",
        "title": "SSC 2027 English Unseen Passage & Summary",
        "subtitle": "ইনফরমেশন ট্রান্সফার ও সামারি রাইটিং — ১৫ নম্বরের প্রস্তুতি",
        "features": ["প্রশ্ন ৪: Info Transfer (৫)", "প্রশ্ন ৫: Summary (১০)", "১/৩ নিয়মে সামারি", "৪১টি আনসিন তালিকা"],
        "aliases": ["ssc_2027_silo_02_unseen_passage.png"]
    },
    {
        "filename": "ssc_2027_silo_03_matching_rearrange.png",
        "category_key": "Education Guide",
        "badge_label": "SSC 2027 | English 1st",
        "custom_tag_text": "এসএসসি ও দাখিল পরীক্ষা ২০২৭",
        "title": "SSC 2027 English Matching & Rearrange",
        "subtitle": "টেবিল ম্যাচিং ও রি-অ্যারেঞ্জিং অনুচ্ছেদ — ১৩ নম্বরের প্রস্তুতি",
        "features": ["প্রশ্ন ৬: টেবিল ম্যাচিং (৫)", "প্রশ্ন ৭: রি-অ্যারেঞ্জ (৮)", "৩২টি ম্যাচিং টেবিল", "৩৬টি রি-অ্যারেঞ্জ সমাধান"]
    },
    {
        "filename": "ssc_2027_silo_04_poems_stories.png",
        "category_key": "Education Guide",
        "badge_label": "SSC 2027 | English 1st",
        "custom_tag_text": "এসএসসি ও দাখিল পরীক্ষা ২০২৭",
        "title": "SSC 2027 English Poems & Stories Suggestion",
        "subtitle": "কবিতা ও ছোটগল্পের সংক্ষিপ্ত প্রশ্নোত্তর — ১৬ নম্বরের মডেল হ্যান্ডনোট",
        "features": ["প্রশ্ন ৮: কবিতা প্রশ্নোত্তর (৮)", "প্রশ্ন ৯: গল্প প্রশ্নোত্তর (৮)", "৭টি কবিতা বিশ্লেষণ", "৩২টি মডেল প্রশ্নোত্তর"]
    },
    {
        "filename": "ssc_2027_silo_05_story_dialogue.png",
        "category_key": "Education Guide",
        "badge_label": "SSC 2027 | English 1st",
        "custom_tag_text": "এসএসসি ও দাখিল পরীক্ষা ২০২৭",
        "title": "SSC 2027 English Completing Story & Dialogue",
        "subtitle": "কমপ্লিটিং স্টোরি ও ডায়ালগ রাইটিং — ২৫ নম্বরের ফাইনাল সাজেশন",
        "features": ["প্রশ্ন ১০: Story Writing (১৫)", "প্রশ্ন ১১: Dialogue Writing (১০)", "৩৪টি স্টোরি তালিকা", "৩২টি ডায়ালগ সমাধান"],
        "aliases": ["ssc_2027_silo_05_writing.png"]
    }
]

def main():
    print("=" * 70)
    print("🎨 GENERATING 6 BILINGUAL SSC 2027 ENGLISH BANNERS ON bg_3.png...")
    print("=" * 70)

    for idx, item in enumerate(SERIES_BANNERS, 1):
        print(f"\n[{idx}/6] Rendering Banner: {item['title']}")
        print(f"      File:     {item['filename']}")
        print(f"      Subtitle: {item['subtitle']}")

        out_webp = generate_official_bg_banner(
            filename=item["filename"],
            category_key=item["category_key"],
            badge_label=item["badge_label"],
            title=item["title"],
            subtitle=item["subtitle"],
            features=item["features"],
            custom_tag_text=item["custom_tag_text"]
        )

        base = os.path.splitext(item["filename"])[0]
        # Check for aliases and create duplicate webp/png/jpg
        for alias_fn in item.get("aliases", []):
            alias_base = os.path.splitext(alias_fn)[0]
            for ext in [".png", ".webp", ".jpg"]:
                src_p = os.path.join(POSTS_DIR, f"{base}{ext}")
                dst_p = os.path.join(POSTS_DIR, f"{alias_base}{ext}")
                if os.path.exists(src_p):
                    shutil.copy2(src_p, dst_p)
                src_t = os.path.join(THUMBS_DIR, f"{base}{ext}")
                dst_t = os.path.join(THUMBS_DIR, f"{alias_base}{ext}")
                if os.path.exists(src_t):
                    shutil.copy2(src_t, dst_t)
            print(f"      [✔] Created Alias: {alias_fn}")

    # Remove temporary test files if present
    for t_fn in ["test_bilingual_silo_01.webp", "test_bilingual_silo_01.png", "test_bilingual_silo_01.jpg"]:
        t_path = os.path.join(POSTS_DIR, t_fn)
        if os.path.exists(t_path):
            os.remove(t_path)
        t_path_thumb = os.path.join(THUMBS_DIR, t_fn)
        if os.path.exists(t_path_thumb):
            os.remove(t_path_thumb)

    print("\n" + "=" * 70)
    print("🎉 ALL 6 BILINGUAL ENGLISH 1ST PAPER BANNERS GENERATED SUCCESSFULLY!")
    print("=" * 70)

if __name__ == "__main__":
    main()
