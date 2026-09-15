#!/usr/bin/env python3
"""
tools/image_generator/build_user_requested_thumbnails.py
Generates the 3 requested thumbnails using HelpTrickBD official background templates
from 'Thumbnail BG/' and Hind Siliguri typography.
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

TASKS = [
    {
        "title": "সরকারি প্রাথমিক শিক্ষক নিয়োগ ও চাকরির ভাইভা প্রস্তুতি গাইডলাইন",
        "subtitle": "ড্রেস কোড, সাধারণ জিজ্ঞাসা ও আত্মবিশ্বাসী ভাইভা সহায়িকা",
        "category": "Job Study Article",
        "filename": "primary-teacher-viva-guide-banner.png",
        "desc": "Primary Teacher Viva Guide (bg_4.png - Job Prep)"
    },
    {
        "title": "ক্লাউড কম্পিউটিং কি ও এর বাস্তব সুবিধা",
        "subtitle": "IaaS, PaaS ও SaaS মডেলের সহজ ও পূর্ণাঙ্গ ব্যাখ্যা",
        "category": "ICT Guide",
        "filename": "cloud-computing-guide-banner.png",
        "desc": "Cloud Computing Guide (bg_5.png - ICT Guide)"
    },
    {
        "title": "কম্পিউটার ভাইরাস ও সাইবার নিরাপত্তা গাইডলাইন",
        "subtitle": "ম্যালওয়্যার, র‍্যানসমওয়্যার ও ফিশিং থেকে ডাটা সুরক্ষার উপায়",
        "category": "ICT Guide",
        "filename": "computer-virus-cyber-security-banner.png",
        "desc": "Computer Virus Guide (bg_5.png - ICT Guide)"
    },
    {
        "title": "বিসিএস প্রিলিমিনারি ২০০ নম্বরের মানবণ্টন ও বুক লিস্ট",
        "subtitle": "প্রথমবারে পাসের সেরা প্রস্তুতি ও বিষয়ভিত্তিক বই তালিকা",
        "category": "Job Study Article",
        "filename": "bcs-preliminary-marks-booklist-banner.png",
        "desc": "BCS Preliminary Marks & Booklist (bg_4.png - Job Prep)"
    }
]

def main():
    print("=" * 70)
    print("🎨 Generating Official Background Thumbnails...")
    print("=" * 70)

    for item in TASKS:
        print(f"\n[*] Generating: {item['desc']}")
        # 1. Generate via thumbnail_generator into THUMB_DIR
        generate_thumbnail(
            title=item["title"],
            category=item["category"],
            subtitle=item["subtitle"],
            output_filename=item["filename"],
            lang="bn"
        )

        base_name = os.path.splitext(item["filename"])[0]
        png_thumb = os.path.join(THUMB_DIR, item["filename"])
        webp_thumb = os.path.join(THUMB_DIR, f"{base_name}.webp")

        png_post = os.path.join(POSTS_DIR, item["filename"])
        webp_post = os.path.join(POSTS_DIR, f"{base_name}.webp")
        jpg_post = os.path.join(POSTS_DIR, f"{base_name}.jpg")

        # Copy to posts directory
        shutil.copy2(png_thumb, png_post)
        shutil.copy2(png_thumb, jpg_post)

        # Compress to 10-20 KB WebP
        compress_to_target_webp(png_post, webp_post, target_min_kb=10.0, target_max_kb=20.0)
        shutil.copy2(webp_post, webp_thumb)

        size_kb = os.path.getsize(webp_post) / 1024.0
        print(f"    [✔] PNG: {png_post}")
        print(f"    [✔] WebP: {size_kb:.2f} KB ({webp_post})")

    print("\n" + "=" * 70)
    print("🎉 All thumbnails successfully generated and ready for user inspection!")
    print("=" * 70)

if __name__ == "__main__":
    main()
