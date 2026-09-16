#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/image_generator/build_nu_social_change_thumbnails.py
----------------------------------------------------------
Generates the 5 official 16:9 banners for the Masters Political Science posts
(Paper Code: 311103 - Social Change & Political Development) using the authentic
'Thumbnail BG/bg_2.png' background template.
"""

import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

from tools.image_generator.build_official_bg_thumbnails import generate_official_bg_banner

POSTS = [
    {
        "filename": "transitional-society-characteristics-banner.png",
        "category_key": "Political Science",
        "badge_label": "মাস্টার্স রাষ্ট্রবিজ্ঞান",
        "title": "পরিবর্তনশীল সমাজের বৈশিষ্ট্যসমূহ",
        "subtitle": "সামাজিক পরিবর্তন ও রাজনৈতিক উন্নয়ন — মাস্টার্স শেষ পর্ব হ্যান্ডনোট",
        "features": ["তাত্ত্বিক সংজ্ঞা", "১০টি মূল বৈশিষ্ট্য", "উন্নয়নশীল দেশের সংকট", "মডেল প্রশ্নোত্তর ২০২৬"]
    },
    {
        "filename": "traditional-vs-modern-society-banner.png",
        "category_key": "Political Science",
        "badge_label": "মাস্টার্স রাষ্ট্রবিজ্ঞান",
        "title": "সনাতন সমাজ ও আধুনিক সমাজের পার্থক্য",
        "subtitle": "সামাজিক পরিবর্তনের গতিধারা ও তুলনামূলক সমাজতাত্ত্বিক বিশ্লেষণ",
        "features": ["মৌলিক ধারণা", "১২টি বিষয়ের তুলনামূলক ছক", "সমাজতাত্ত্বিক গুরুত্ব", "পরীক্ষা প্রস্তুতি নোট"]
    },
    {
        "filename": "modern-society-characteristics-banner.png",
        "category_key": "Political Science",
        "badge_label": "মাস্টার্স রাষ্ট্রবিজ্ঞান",
        "title": "আধুনিক সমাজের বৈশিষ্ট্যসমূহ ও স্বরূপ",
        "subtitle": "শিল্পায়ন, বিজ্ঞানমনস্কতা ও গণতান্ত্রিক কাঠামোর তাত্ত্বিক পর্যালোচনা",
        "features": ["আধুনিক সমাজের রূপরেখা", "১২টি প্রধান বৈশিষ্ট্য", "সমসাময়িক সংকট", "বিশ্লেষণধর্মী প্রশ্নোত্তর"]
    },
    {
        "filename": "modernization-agents-media-banner.png",
        "category_key": "Political Science",
        "badge_label": "মাস্টার্স রাষ্ট্রবিজ্ঞান",
        "title": "আধুনিকীকরণ কী ও এর প্রধান বাহনসমূহ",
        "subtitle": "সামাজিক ও রাজনৈতিক আধুনিকায়নে বিভিন্ন প্রাতিষ্ঠানিক মাধ্যমের ভূমিকা",
        "features": ["তাত্ত্বিক সংজ্ঞা", "৯টি প্রধান বাহন বা মাধ্যম", "উন্নয়নশীল দেশের বাস্তবতা", "মডেল হ্যান্ডনোট"]
    },
    {
        "filename": "political-modernization-vs-development-banner.png",
        "category_key": "Political Science",
        "badge_label": "মাস্টার্স রাষ্ট্রবিজ্ঞান",
        "title": "রাজনৈতিক আধুনিকীকরণ ও উন্নয়নের পার্থক্য",
        "subtitle": "রাষ্ট্রবিজ্ঞান তাত্ত্বিক বিতর্ক ও ১৪টি বিষয়ের প্রামাণ্য তুলনামূলক ছক",
        "features": ["ধারণাগত পার্থক্য", "১৪টি বিষয়ের তুলনামূলক টেবিল", "হান্টিংটনের অবক্ষয় তত্ত্ব", "মাস্টার্স মডেল উত্তর"]
    }
]

def main():
    print("=" * 75)
    print("🎨 Generating 5 Official Political Science Banners on bg_2.png...")
    print("=" * 75)
    
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
    print("\n" + "=" * 75)
    print("✅ All 5 Official Political Science Banners Generated Successfully!")
    print("=" * 75)

if __name__ == "__main__":
    main()
