#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/image_generator/build_pdf_posts_thumbnails.py
---------------------------------------------------
Generates the 4 official 16:9 banners for the Masters Political Science posts
using the authentic 'Thumbnail BG/bg_2.png' background template.
"""

import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

from tools.image_generator.build_official_bg_thumbnails import generate_official_bg_banner

POSTS = [
    {
        "filename": "political-violence-bangladesh-banner.png",
        "category_key": "Political Science",
        "badge_label": "মাস্টার্স রাষ্ট্রবিজ্ঞান",
        "title": "বাংলাদেশে রাজনৈতিক সহিংসতার কারণ ও প্রতিকার",
        "subtitle": "জাতীয় বিশ্ববিদ্যালয় মাস্টার্স শেষ পর্ব রাষ্ট্রবিজ্ঞান স্পেশাল হ্যান্ডনোট",
        "features": ["সহিংসতার ঐতিহাসিক কারণ", "প্রকৃতি ও রূপরেখা", "উত্তরণের উপায়", "মডেল প্রশ্নোত্তর ২০২৬"]
    },
    {
        "filename": "bangladesh-un-membership-1972-banner.png",
        "category_key": "Political Science",
        "badge_label": "মাস্টার্স রাষ্ট্রবিজ্ঞান",
        "title": "জাতিসংঘ সদস্যপদ লাভে বাংলাদেশের বাধাসমূহ",
        "subtitle": "১৯৭২ সালের আন্তর্জাতিক কূটনৈতিক সংকট ও নিরাপত্তা পরিষদের ভেটো রাজনীতি",
        "features": ["১৯৭২-এর পটভূমি", "চীনের ভেটো বিতর্ক", "কূটনৈতিক তৎপরতা", "পরীক্ষা সহায়ক নোট"]
    },
    {
        "filename": "secularism-vs-islamic-values-banner.png",
        "category_key": "Political Science",
        "badge_label": "মাস্টার্স রাষ্ট্রবিজ্ঞান",
        "title": "ধর্মনিরপেক্ষতা বনাম ইসলামি মূল্যবোধ",
        "subtitle": "স্বাধীন বাংলাদেশের রাজনীতিতে আদর্শিক দ্বন্দ্ব ও সাংবিধানিক বিবর্তন",
        "features": ["তাত্ত্বিক সংজ্ঞা", "সাংবিধানিক প্রেক্ষাপট", "দ্বন্দ্বের ঐতিহাসিক কারণ", "ভারসাম্যপূর্ণ সমাধান"]
    },
    {
        "filename": "caretaker-government-free-fair-election-banner.png",
        "category_key": "Political Science",
        "badge_label": "মাস্টার্স রাষ্ট্রবিজ্ঞান",
        "title": "তত্ত্বাবধায়ক সরকার ও অবাধ সুষ্ঠু নির্বাচনের পূর্বশর্ত",
        "subtitle": "বাংলাদেশের গণতান্ত্রিক রূপান্তর, সাংবিধানিক বিতর্ক ও গ্রহণযোগ্য নির্বাচনের শর্ত",
        "features": ["উৎপত্তি ও ত্রয়োদশ সংশোধনী", "নির্বাচনী সংকট", "সুষ্ঠু নির্বাচনের শর্ত", "বিশ্লেষণধর্মী হ্যান্ডনোট"]
    }
]

def main():
    print("=" * 70)
    print("🎨 Generating 4 Official Political Science Banners on bg_2.png...")
    print("=" * 70)
    
    for p in POSTS:
        print(f"\n[*] Processing: {p['title']}")
        generate_official_bg_banner(
            filename=p["filename"],
            category_key=p["category_key"],
            badge_label=p["badge_label"],
            title=p["title"],
            subtitle=p["subtitle"],
            features=p["features"]
        )
    print("\n" + "=" * 70)
    print("✅ All 4 Official Political Science Banners Generated Successfully!")
    print("=" * 70)

if __name__ == "__main__":
    main()
