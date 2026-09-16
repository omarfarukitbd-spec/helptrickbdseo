#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/image_generator/build_user_requested_10_thumbnails.py
-----------------------------------------------------------
Generates the 10 official, 16:9 featured banners for the 10 posts identified
from the user's uploaded screenshots, strictly using the authentic 'Thumbnail BG/'
templates (bg_2.png for Political Science, bg_3.png for Education Guide).
Enforces:
- Exact Bengali typography via HindSiliguri-Bold.ttf and Chromium HarfBuzz
- 10-20 KB Ultra-WebP Core Web Vitals compression
- Sync to assets/images/posts/ and assets/images/thumbnails/
"""

import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.image_generator.build_official_bg_thumbnails import generate_official_bg_banner

POSTS_TO_BUILD = [
    {
        "filename": "bangladesh-industry-nationalization-history-official-banner.png",
        "category_key": "Political Science",
        "badge_label": "মাস্টার্স রাষ্ট্রবিজ্ঞান",
        "title": "বাংলাদেশে শিল্প জাতীয়করণের ইতিহাস",
        "subtitle": "পটভূমি, সমস্যা, সংকট ও অর্থনীতির ওপর বাস্তব প্রভাব (২০২৬)",
        "features": ["ঐতিহাসিক পটভূমি", "১৯৭২ সালের শিল্প নীতি", "জাতীয়করণের সমস্যা", "মাস্টার্স মডেল উত্তর"]
    },
    {
        "filename": "state-society-women-movement-official-banner.png",
        "category_key": "Political Science",
        "badge_label": "মাস্টার্স রাষ্ট্রবিজ্ঞান",
        "title": "রাষ্ট্র, সমাজ ও নারী: আন্দোলনের প্রেক্ষাপট",
        "subtitle": "অধিকার ও অস্তিত্ব রক্ষার লড়াই — নারী ক্ষমতায়নের রূপরেখা (২০২৬)",
        "features": ["আন্দোলনের ইতিহাস", "সাংবিধানিক অধিকার", "পিতৃতান্ত্রিক বাধা", "বিশ্লেষণমূলক হ্যান্ডনোট"]
    },
    {
        "filename": "child-socialization-peers-friends-official-banner.png",
        "category_key": "Political Science",
        "badge_label": "সমাজবিজ্ঞান ও শিক্ষা",
        "title": "শিশুর সামাজিকীকরণে খেলার সাথী ও বন্ধু",
        "subtitle": "ব্যক্তিত্ব বিকাশ, সামাজিক মূল্যবোধ ও সহপাঠীদের ভূমিকা (২০২৬)",
        "features": ["সামাজিকীকরণ ধারণা", "সঙ্গী দলের মনস্তত্ত্ব", "পারিবারিক প্রভাব", "পরীক্ষা প্রস্তুতি গাইড"]
    },
    {
        "filename": "population-change-causes-factors-official-banner.png",
        "category_key": "Political Science",
        "badge_label": "মাস্টার্স রাষ্ট্রবিজ্ঞান",
        "title": "জনসংখ্যা পরিবর্তনের কারণ ও নিয়ামকসমূহ",
        "subtitle": "জনমিতিক রূপান্তর, আর্থ-সামাজিক প্রভাব ও ভবিষ্যৎ চ্যালেঞ্জ (২০২৬)",
        "features": ["পরিবর্তনের কারণ", "প্রধান নিয়ামকসমূহ", "উন্নয়নশীল দেশের সংকট", "মডেল প্রশ্নোত্তর"]
    },
    {
        "filename": "what-is-political-economy-definition-official-banner.png",
        "category_key": "Political Science",
        "badge_label": "মাস্টার্স রাষ্ট্রবিজ্ঞান",
        "title": "রাজনৈতিক অর্থনীতি কাকে বলে?",
        "subtitle": "সংজ্ঞা, পরিধি, বিষয়বস্তু ও আধুনিক তাত্ত্বিক কাঠামো (২০২৬)",
        "features": ["তাত্ত্বিক সংজ্ঞা", "বিষয়বস্তু ও পরিধি", "চিরায়ত মতবাদ", "মাস্টার্স পরীক্ষার হ্যান্ডনোট"]
    },
    {
        "filename": "women-reserved-seats-parliament-official-banner.png",
        "category_key": "Political Science",
        "badge_label": "মাস্টার্স রাষ্ট্রবিজ্ঞান",
        "title": "সংসদে নারীদের সংরক্ষিত আসন ও পটভূমি",
        "subtitle": "সাংবিধানিক বিবর্তন, গুরুত্ব ও প্রতিনিধিত্বের বাস্তবতা (২০২৬)",
        "features": ["সাংবিধানিক ধারা", "সংরক্ষিত আসনের বিবর্তন", "বাস্তব চ্যালেঞ্জ", "পূর্ণাঙ্গ স্পেশাল নোট"]
    },
    {
        "filename": "womens-decade-goals-objectives-official-banner.png",
        "category_key": "Political Science",
        "badge_label": "মাস্টার্স রাষ্ট্রবিজ্ঞান",
        "title": "নারী দশকের লক্ষ্য, উদ্দেশ্য ও পটভূমি",
        "subtitle": "জাতিসংঘের বিশ্ব নারী দশক ও বৈশ্বিক নারী অধিকারের বিস্তার",
        "features": ["ঐতিহাসিক পটভূমি", "জাতিসংঘের ঘোষণা", "মূল লক্ষ্য ও উদ্দেশ্য", "পরীক্ষা সহায়ক হ্যান্ডনোট"]
    },
    {
        "filename": "what-is-patriarchy-definition-official-banner.png",
        "category_key": "Political Science",
        "badge_label": "মাস্টার্স রাষ্ট্রবিজ্ঞান",
        "title": "পুরুষতন্ত্র কাকে বলে? সমাজতাত্ত্বিক স্বরূপ",
        "subtitle": "সংজ্ঞা, উৎপত্তি, পিতৃতান্ত্রিক কাঠামো ও সামাজিক প্রভাব (২০২৬)",
        "features": ["সমাজতাত্ত্বিক সংজ্ঞা", "উৎপত্তির ইতিহাস", "নারীর অবস্থান", "মাস্টার্স স্পেশাল হ্যান্ডনোট"]
    },
    {
        "filename": "blri-bangladesh-livestock-research-official-banner.png",
        "category_key": "Education Guide",
        "badge_label": "শিক্ষা ও সাধারণ জ্ঞান",
        "title": "বাংলাদেশ প্রাণিসম্পদ গবেষণা ইনস্টিটিউট (BLRI)",
        "subtitle": "কার্যক্রম, উদ্ভাবন ও জাতীয় অর্থনীতিতে ভূমিকা (২০২৬)",
        "features": ["বিএলআরআই পটভূমি", "গবেষণা ও উদ্ভাবন", "অর্থনৈতিক অবদান", "পরীক্ষা সহায়ক সহায়িকা"]
    },
    {
        "filename": "government-political-parties-relationship-official-banner.png",
        "category_key": "Political Science",
        "badge_label": "মাস্টার্স রাষ্ট্রবিজ্ঞান",
        "title": "সরকার ও রাজনৈতিক দল: ধারণা ও সম্পর্ক",
        "subtitle": "পারস্পরিক মিথস্ক্রিয়া ও বাংলাদেশে গণতান্ত্রিক চর্চার বাস্তবতা (২০২৬)",
        "features": ["মৌলিক ধারণা", "পারস্পরিক সম্পর্ক", "গণতান্ত্রিক সংস্কৃতি", "বিশ্লেষণমূলক উত্তর"]
    }
]

def main():
    print("=" * 70)
    print("🎨 GENERATING 10 OFFICIAL BANNERS VIA CHROMIUM HARFBUZZ ENGINE")
    print("=" * 70)

    generated = []
    for idx, item in enumerate(POSTS_TO_BUILD, 1):
        print(f"\n[{idx}/10] Rendering Banner: {item['title']}")
        print(f"      File:     {item['filename']}")
        print(f"      Category: {item['category_key']}")

        out_webp = generate_official_bg_banner(
            filename=item["filename"],
            category_key=item["category_key"],
            badge_label=item["badge_label"],
            title=item["title"],
            subtitle=item["subtitle"],
            features=item["features"]
        )
        generated.append(out_webp)

    print("\n" + "=" * 70)
    print(f"🎉 ALL 10 OFFICIAL BANNERS GENERATED AND OPTIMIZED TO WEBP (10-20 KB)!")
    print("=" * 70)
    for p in generated:
        size_kb = os.path.getsize(p) / 1024.0
        print(f"  • {os.path.basename(p)} ({size_kb:.1f} KB)")

if __name__ == "__main__":
    main()
