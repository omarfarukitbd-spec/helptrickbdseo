#!/usr/bin/env python3
"""
tools/image_generator/regenerate_silo_thumbnails.py
Regenerates the 4 new post thumbnails using HelpTrickBD's official
Thumbnail BG/ templates, Hind Siliguri typography, and 10–20 KB WebP compressor.
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

ITEMS_TO_GENERATE = [
    {
        "title": "সরকারি প্রাথমিক শিক্ষক নিয়োগ ও ভাইভা প্রস্তুতি গাইড",
        "subtitle": "ড্রেস কোড, সাধারণ জিজ্ঞাসা ও আত্মবিশ্বাসী ভাইভা সহায়িকা",
        "category": "Job Study Article",
        "filename": "primary-teacher-viva-guide-banner.png"
    },
    {
        "title": "বিসিএস প্রিলিমিনারি ২০০ নম্বরের মানবণ্টন ও বুক লিস্ট",
        "subtitle": "প্রথমবারে পাসের সেরা প্রস্তুতি ও বিষয়ভিত্তিক বই তালিকা",
        "category": "Job Study Article",
        "filename": "bcs-preliminary-marks-booklist-banner.png"
    },
    {
        "title": "কম্পিউটার ভাইরাস ও সাইবার নিরাপত্তা: ডাটা সুরক্ষার উপায়",
        "subtitle": "ম্যালওয়্যার, র‍্যানসমওয়্যার ও ফিশিং থেকে সুরক্ষার পূর্ণাঙ্গ গাইড",
        "category": "ICT Guide",
        "filename": "computer-virus-cyber-security-banner.png"
    },
    {
        "title": "ক্লাউড কম্পিউটিং কি? প্রকারভেদ ও শীর্ষ প্ল্যাটফর্ম",
        "subtitle": "IaaS, PaaS, SaaS ও আধুনিক ক্লাউড সার্ভিসের সহজ ব্যাখ্যা",
        "category": "ICT Guide",
        "filename": "cloud-computing-guide-banner.png"
    }
]

def main():
    print("=" * 70)
    print("🎨 Regenerating Official Category Thumbnails for 4 Silo Posts...")
    print("=" * 70)

    for item in ITEMS_TO_GENERATE:
        print(f"\n[*] Generating: {item['title']} ({item['category']})")
        # 1. Generate via official thumbnail_generator (saved in THUMB_DIR)
        raw_webp = generate_thumbnail(
            title=item["title"],
            category=item["category"],
            subtitle=item["subtitle"],
            output_filename=item["filename"],
            lang="bn"
        )

        base_name = os.path.splitext(item["filename"])[0]
        png_src = os.path.join(THUMB_DIR, item["filename"])
        webp_src = os.path.join(THUMB_DIR, f"{base_name}.webp")

        # Copy to assets/images/posts/
        png_dst = os.path.join(POSTS_DIR, item["filename"])
        webp_dst = os.path.join(POSTS_DIR, f"{base_name}.webp")
        jpg_dst = os.path.join(POSTS_DIR, f"{base_name}.jpg")

        shutil.copy2(png_src, png_dst)
        shutil.copy2(webp_src, webp_dst)
        # also save jpg for compatibility if needed
        shutil.copy2(png_src, jpg_dst)

        # Compress specifically in posts dir to ensure 10-20 KB
        compress_to_target_webp(png_dst, webp_dst, target_min_kb=10.0, target_max_kb=20.0)

        webp_size = os.path.getsize(webp_dst) / 1024.0
        print(f"    [✔] Saved in posts: {item['filename']}")
        print(f"    [✔] WebP Size: {webp_size:.2f} KB ({webp_dst})")

    print("\n" + "=" * 70)
    print("🎉 All 4 thumbnails successfully regenerated with Official Brand Templates!")
    print("=" * 70)

if __name__ == "__main__":
    main()
