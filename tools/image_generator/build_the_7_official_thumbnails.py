#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/image_generator/build_the_7_official_thumbnails.py
--------------------------------------------------------
Generates 100% authentic, beautiful, light-background banners for the 7 posts
using tools.image_generator.thumbnail_generator (the official template engine
matching Cloud Computing and Computer Virus banners).
"""

import os
import sys
import shutil

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.image_generator.thumbnail_generator import generate_thumbnail
from tools.image_optimizer.webp_compressor import compress_to_target_webp

POSTS_DIR = os.path.join(PROJECT_ROOT, "assets", "images", "posts")
THUMB_DIR = os.path.join(PROJECT_ROOT, "assets", "images", "thumbnails")
os.makedirs(POSTS_DIR, exist_ok=True)
os.makedirs(THUMB_DIR, exist_ok=True)

POSTS_TO_BUILD = [
    {
        "slug": "namta-1-to-20",
        "post_id": "1802936717529328214",
        "url": "https://www.helptrickbd.com/2025/01/namta-1-to-20.html",
        "title": "নামতা ১ থেকে ২০ পর্যন্ত: বাংলা ও ইংরেজিতে সহজে মুখস্থ করার চার্ট",
        "subtitle": "গুণনীয়কের সহজ নিয়ম ও শিশুদের জন্য আদর্শ নামতা চার্ট সহায়িকা",
        "category": "Education Guide",
        "lang": "bn",
        "filename": "namta-1-to-20-official-banner.png"
    },
    {
        "slug": "honours-political-science-book-list",
        "post_id": "4563456345634563456", # will search or match
        "url": "https://www.helptrickbd.com/2025/01/honours-political-science-book-list.html",
        "title": "রাষ্ট্রবিজ্ঞান অনার্স ১ম, ২য়, ৩য় ও ৪র্থ বর্ষের পাঠ্য বইয়ের তালিকা",
        "subtitle": "সকল বর্ষের বিষয়ভিত্তিক পূর্ণাঙ্গ বুক লিস্ট ও বিষয় কোড সহায়িকা",
        "category": "Political Science",
        "lang": "bn",
        "filename": "political-science-honours-book-list-official-banner.png"
    },
    {
        "slug": "hason-raja-was-born-in-1854-class-six",
        "post_id": "7891234567891234567",
        "url": "https://www.helptrickbd.com/2025/01/hason-raja-was-born-in-1854-class-six.html",
        "title": "Hason Raja Was Born in 1854 | Class 6 English Seen Comprehension",
        "subtitle": "Textbook Passage, Bengali Meaning & Model Question Solutions",
        "category": "Fallback / School",
        "lang": "en",
        "filename": "hason-raja-class-six-english-official-banner.png"
    },
    {
        "slug": "computer-types-classification-part4",
        "post_id": "",
        "url": "https://www.helptrickbd.com/2025/12/computer-types-classification-part4.html",
        "title": "কম্পিউটারের প্রকারভেদ: অ্যানালগ, ডিজিটাল, হাইব্রিড ও সুপার কম্পিউটার",
        "subtitle": "কাজের প্রকৃতি ও আকারভেদে কম্পিউটারের সম্পূর্ণ আধুনিক শ্রেণিবিন্যাস",
        "category": "ICT Guide",
        "lang": "bn",
        "filename": "computer-types-classification-official-banner.png"
    },
    {
        "slug": "computer-generations-features-part3",
        "post_id": "",
        "url": "https://www.helptrickbd.com/2025/12/computer-generations-features-part3.html",
        "title": "কম্পিউটারের প্রজন্ম: ১ম থেকে ৫ম প্রজন্মের প্রযুক্তিগত তুলনা ও বৈশিষ্ট্য",
        "subtitle": "ভ্যাকুয়াম টিউব থেকে মাইক্রোপ্রসেসর ও কৃত্রিম বুদ্ধিমত্তার বিবর্তন",
        "category": "ICT Guide",
        "lang": "bn",
        "filename": "computer-generations-features-official-banner.png"
    },
    {
        "slug": "computer-history-inventions-part2",
        "post_id": "",
        "url": "https://www.helptrickbd.com/2025/12/computer-history-inventions-part2.html",
        "title": "কম্পিউটারের ইতিহাস: এবাকাস থেকে ইন্টিগ্রেটেড সার্কিট পর্যন্ত পূর্ণাঙ্গ রূপরেখা",
        "subtitle": "প্যাসকেলাইন, চার্লস ব্যাবেজের ইঞ্জিন ও ট্রানজিস্টরের বৈপ্লবিক আবিষ্কার",
        "category": "ICT Guide",
        "lang": "bn",
        "filename": "computer-history-inventions-official-banner.png"
    },
    {
        "slug": "computer-definition-history",
        "post_id": "",
        "url": "https://www.helptrickbd.com/2025/12/computer-definition-history.html",
        "title": "কম্পিউটার কাকে বলে? কম্পিউটারের সংজ্ঞা, ইতিহাস, বৈশিষ্ট্য ও প্রজন্ম",
        "subtitle": "এবাকাস থেকে আধুনিক সুপার কম্পিউটার ও কৃত্রিম বুদ্ধিমত্তার সহজ পাঠ",
        "category": "ICT Guide",
        "lang": "bn",
        "filename": "computer-definition-history-official-banner.png"
    }
]

def main():
    print("=" * 70)
    print("🎨 Generating 7 Official HelpTrickBD Category Banners...")
    print("=" * 70)

    for item in POSTS_TO_BUILD:
        print(f"\n[*] Generating: {item['title']}")
        print(f"    Category: {item['category']} | Lang: {item['lang']}")
        
        # Generate thumbnail via official thumbnail_generator.py
        raw_webp = generate_thumbnail(
            title=item["title"],
            category=item["category"],
            subtitle=item["subtitle"],
            output_filename=item["filename"],
            lang=item["lang"]
        )

        base_name = os.path.splitext(item["filename"])[0]
        png_src = os.path.join(THUMB_DIR, item["filename"])
        webp_src = os.path.join(THUMB_DIR, f"{base_name}.webp")

        png_dst = os.path.join(POSTS_DIR, item["filename"])
        webp_dst = os.path.join(POSTS_DIR, f"{base_name}.webp")

        shutil.copy2(png_src, png_dst)
        shutil.copy2(webp_src, webp_dst)

        # Optimize/compress to 10-20 KB
        compress_to_target_webp(png_dst, webp_dst, target_min_kb=10.0, target_max_kb=20.0)

        webp_size = os.path.getsize(webp_dst) / 1024.0
        print(f"    [✔] Success: {base_name}.webp ({webp_size:.2f} KB)")

    print("\n" + "=" * 70)
    print("🎉 All 7 official banners successfully generated!")
    print("=" * 70)

if __name__ == "__main__":
    main()
