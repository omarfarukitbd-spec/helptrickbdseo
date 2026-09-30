#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/social_broadcaster/broadcast_university_admission.py
----------------------------------------------------------
Broadcasts the newly published Public University Admission Guide 2026
to the official HelpTrickBD Facebook Page and Telegram Channel.
Strictly zero-emoji compliant.
"""

import os
import sys
import json

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

CREDS_PATH = os.path.join(PROJECT_ROOT, "tools", "social_broadcaster", "social_credentials.json")

from tools.social_broadcaster.telegram_publisher import TelegramPublisher
from tools.social_broadcaster.facebook_publisher import FacebookPublisher

POST_TITLE = "পাবলিক বিশ্ববিদ্যালয় ভর্তি যোগ্যতা ২০২৬: বিজ্ঞান, মানবিক ও ব্যবসায় শাখা পূর্ণাঙ্গ গাইড (Public University Admission Guide 2026)"
POST_URL = "https://www.helptrickbd.com/2026/09/public-university-admission-eligibility.html"
HERO_IMAGE = "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/public_university_admission_guide_2026.webp"

# 1. Telegram Copy (Clean HTML, < 900 chars)
TELEGRAM_TEXT = """<b>পাবলিক বিশ্ববিদ্যালয় ভর্তি যোগ্যতা ২০২৬: বিজ্ঞান, মানবিক ও ব্যবসায় শাখা পূর্ণাঙ্গ গাইড</b>

এইচএসসি পরীক্ষা শেষ হওয়ার পর বিশ্ববিদ্যালয়ের ভর্তি পরীক্ষা (Public University Admission 2026) শিক্ষার্থীদের জীবনের সবচেয়ে বড় টার্নিং পয়েন্ট। রেজাল্ট প্রকাশের আগেই সঠিক গাইডলাইন জানা থাকলে ঢাবি, রাবি, চবি, জাবি ও গুচ্ছভুক্ত ২৪টি পাবলিক বিশ্ববিদ্যালয়ে নিজের আসন নিশ্চিত করা সম্ভব।

<b>আর্টিকেলের মূল বিষয়সমূহ:</b>
• বিজ্ঞান, মানবিক ও বাণিজ্য শাখা অনুযায়ী বিষয় নির্বাচন ম্যাট্রিক্স
• শীর্ষ বিশ্ববিদ্যালয়গুলোর জিপিএ যোগ্যতা, আসন ও মানবণ্টন
• রেজাল্টের অপেক্ষার ৬০ দিন কেন ভর্তি প্রস্তুতির গোল্ডেন টাইম
• ভর্তি আবেদন ও পরীক্ষার হলের ৬টি মারাত্মক ফাঁদ
• রেজাল্ট আশানুরূপ না হলে বিকল্প পথ ও ব্যাকআপ প্ল্যান (Plan-B)
• বোর্ড চ্যালেঞ্জ চলাকালীন আবেদন করার সঠিক নিয়ম

#HelpTrickBD #VarsityAdmission #HSC2026 #StudyGuide #EducationBD"""

# 2. Facebook Copy
FACEBOOK_MESSAGE = """পাবলিক বিশ্ববিদ্যালয় ভর্তি যোগ্যতা ২০২৬: বিজ্ঞান, মানবিক ও ব্যবসায় শাখা পূর্ণাঙ্গ গাইড (Public University Admission Guide 2026)

এইচএসসি পরীক্ষা শেষ হওয়ার পর বিশ্ববিদ্যালয়ের ভর্তি পরীক্ষা (Public University Admission 2026) প্রতিটি শিক্ষার্থীর জীবনের সবচেয়ে বড় টার্নিং পয়েন্ট। রেজাল্ট প্রকাশের আগেই সঠিক প্রস্তুতি ও বিষয়ভিত্তিক কৌশল জানা থাকলে ঢাকা বিশ্ববিদ্যালয় (DU), রাজশাহী বিশ্ববিদ্যালয় (RU), চট্টগ্রাম বিশ্ববিদ্যালয় (CU), জাহাঙ্গীরনগর বিশ্ববিদ্যালয় (JU), কৃষি গুচ্ছ ও সাধারণ গুচ্ছের ২৪টি পাবলিক বিশ্ববিদ্যালয়ে নিজের আসন নিশ্চিত করা সম্ভব।

এই পূর্ণাঙ্গ গাইডের মূল বিষয়সমূহ:
- বিজ্ঞান, মানবিক ও ব্যবসায় শাখা অনুযায়ী কোন কোন বিষয়ে আবেদন করা যাবে
- শীর্ষ বিশ্ববিদ্যালয়গুলোর জিপিএ যোগ্যতা, আসন সংখ্যা ও মানবণ্টন
- এইচএসসি রেজাল্টের অপেক্ষার ৬০ দিন কেন ভর্তি যুদ্ধের গোল্ডেন টাইম
- ভর্তি আবেদন ও পরীক্ষার হলের ৬টি মারাত্মক ফাঁদ (যা না জানলে চান্স পেয়েও স্বপ্নভঙ্গ হতে পারে)
- রেজাল্ট আশানুরূপ না হলে বিকল্প পথ ও ব্যাকআপ প্ল্যান (Plan-B: GST & Agri Cluster)
- বোর্ড চ্যালেঞ্জ চলাকালীন বিশ্ববিদ্যালয়ের আবেদনের সঠিক নিয়ম

সম্পূর্ণ আর্টিকেলটি বিস্তারিত পড়তে ভিজিট করুন:
https://www.helptrickbd.com/2026/09/public-university-admission-eligibility.html

#HelpTrickBD #UniversityAdmission2026 #VarsityAdmission #HSC2026 #DUAdmission #StudyGuide #EducationBD"""

def main():
    if not os.path.exists(CREDS_PATH):
        print(f"Error: Credentials not found at {CREDS_PATH}")
        sys.exit(1)

    with open(CREDS_PATH, "r", encoding="utf-8") as f:
        creds = json.load(f)

    results = {}

    # Publish to Telegram
    print("Publishing to Telegram Channel...")
    tg = TelegramPublisher(
        bot_token=creds["telegram"]["bot_token"],
        channel_id=creds["telegram"]["channel_id"]
    )
    tg_res = tg.publish_post(
        text=TELEGRAM_TEXT,
        image_url=HERO_IMAGE,
        button_text="সম্পূর্ণ ভর্তি গাইড পড়ুন",
        button_url=POST_URL
    )
    results["telegram"] = tg_res
    print("Telegram Result:", tg_res)

    # Publish to Facebook
    print("\nPublishing to Facebook Page...")
    fb = FacebookPublisher(
        page_id=creds["facebook"]["page_id"],
        page_access_token=creds["facebook"]["page_access_token"],
        make_webhook_url=creds["facebook"].get("make_webhook_url")
    )
    fb_res = fb.publish_post(
        message=FACEBOOK_MESSAGE,
        link=POST_URL,
        image_url=HERO_IMAGE,
        title=POST_TITLE,
        post_type="link"
    )
    results["facebook"] = fb_res
    print("Facebook Result:", fb_res)

    print("\nSocial Broadcast Complete!")
    return results

if __name__ == "__main__":
    main()
