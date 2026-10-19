#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/image_generator/build_nu_convocation_banner.py
---------------------------------------------------
Generates the official 16:9 featured banner for:
জাতীয় বিশ্ববিদ্যালয় ২য় সমাবর্তন ২০২৭: রেজিস্ট্রেশন ও Best Complete Guide (ফি ও নিয়মাবলী)
"""

import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.image_generator.build_official_bg_thumbnails import generate_official_bg_banner

BANNER_CONFIG = {
    "filename": "nu_2nd_convocation_registration_guide_2027.png",
    "category_key": "Education Guide",
    "badge_label": "জাতীয় বিশ্ববিদ্যালয় ২য় সমাবর্তন ২০২৭ • অফিশিয়াল বিজ্ঞপ্তি",
    "custom_tag_text": "NU 2nd Convocation 2027 • রেজিস্ট্রেশন নির্দেশিকা",
    "title": "NU 2nd Convocation 2027 Guide",
    "subtitle": "জাতীয় বিশ্ববিদ্যালয় ২য় সমাবর্তন রেজিস্ট্রেশন ও ফি",
    "features": [
        "অনার্স, মাস্টার্স ও ডিগ্রি গ্র্যাজুয়েট",
        "অনলাইন আবেদন ও ফি পরিশোধের নিয়ম",
        "প্রয়োজনীয় কাগজপত্র ও সনদ বিতরণ",
        "গাউন ও সমাবর্তন কিট সংগ্রহ"
    ]
}

def main():
    print("=" * 70)
    print("GENERATING OFFICIAL BANNER FOR NU 2ND CONVOCATION 2027...")
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

    print(f"\n[OK] Master Banner Generated: {out_webp}")
    if os.path.exists(out_webp):
        size_kb = os.path.getsize(out_webp) / 1024
        print(f"    Size: {size_kb:.2f} KB (Target: 10-20 KB)")

if __name__ == "__main__":
    main()
