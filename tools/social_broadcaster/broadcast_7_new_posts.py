#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/social_broadcaster/broadcast_7_new_posts.py
-------------------------------------------------
Broadcasts the 7 newest published posts on HelpTrickBD to Facebook Page
(via Make.com verified gateway) and Telegram Channel (via Telegram Bot API).
Strictly zero-emoji compliant (Rule 12).
"""

import os
import sys
import time
import json
from datetime import datetime

# Enforce UTF-8 on Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(MODULE_DIR, "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.social_broadcaster.telegram_publisher import TelegramPublisher
from tools.social_broadcaster.facebook_publisher import FacebookPublisher

CREDS_FILE = os.path.join(MODULE_DIR, "social_credentials.json")
AUDIT_DATA_FILE = os.path.join(PROJECT_ROOT, "output_posts", "social_audit_data.json")
MASTER_MD_FILE = os.path.join(PROJECT_ROOT, "output_posts", "social_unposted_messages_master.md")

NEW_POSTS = [
    {
        "url": "https://www.helptrickbd.com/2026/10/nu-honours-2nd-year-exam-guide-and.html",
        "title": "জাতীয় বিশ্ববিদ্যালয় অনার্স ২য় বর্ষ পরীক্ষার গাইড ও ৩য় বর্ষে প্রমোশনের নিয়মাবলী ২০২৬",
        "category": "Education Guide",
        "hero_image": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/nu_honours_2nd_year_promotion_rules_2026.webp",
        "button_text": "প্রমোশনের নিয়ম ও গাইডলাইন পড়ুন",
        "telegram": (
            "<b>জাতীয় বিশ্ববিদ্যালয় অনার্স ২য় বর্ষ পরীক্ষার গাইড ও ৩য় বর্ষে প্রমোশনের নিয়মাবলী ২০২৬</b>\n\n"
            "অনার্স ২য় বর্ষের চূড়ান্ত পরীক্ষা শিক্ষার্থীদের স্নাতক জীবনের অত্যন্ত গুরুত্বপূর্ণ ধাপ। ৩য় বর্ষে নিশ্চিত প্রমোশনের জন্য সুনির্দিষ্ট নীতিমালা জানা থাকা আবশ্যক।\n\n"
            "<b>এই গাইডে যা যা থাকছে:</b>\n"
            "• ৩য় বর্ষে প্রমোশন পেতে ন্যূনতম কয়টি তাত্ত্বিক কোর্সে পাস (কমপক্ষে D গ্রেড) বাধ্যতামূলক\n"
            "• সর্বনিম্ন জিপিএ (GPA 2.00) ও ক্রেডিট অর্জনের সুনির্দিষ্ট নিয়মাবলী\n"
            "• কোনো কোর্সে F গ্রেড পেলে প্রমোশন নাকি ইমপ্রুভমেন্টের সুযোগ\n"
            "• ইংরেজি আবশ্যিক পাসের শর্ত ও জিপিএ গণনায় প্রভাব\n\n"
            "<b>» সম্পূর্ণ প্রমোশন রুলস ও স্টাডি গাইডলাইন পড়তে ভিজিট করুন:</b>\n"
            "<a href=\"https://www.helptrickbd.com/2026/10/nu-honours-2nd-year-exam-guide-and.html\"><b>https://www.helptrickbd.com/2026/10/nu-honours-2nd-year-exam-guide-and.html</b></a>\n\n"
            "#NationalUniversity #NUHonours #Honours2ndYear #NUPromotionRules #HelpTrickBD"
        ),
        "facebook": (
            "জাতীয় বিশ্ববিদ্যালয় অনার্স ২য় বর্ষ পরীক্ষার গাইড ও ৩য় বর্ষে প্রমোশনের নিয়মাবলী ২০২৬\n\n"
            "অনার্স ২য় বর্ষের চূড়ান্ত পরীক্ষা শিক্ষার্থীদের চার বছর মেয়াদি স্নাতক যাত্রার অন্যতম গুরুত্বপূর্ণ পর্ব। ৩য় বর্ষে প্রমোশন নিশ্চিত করতে জাতীয় বিশ্ববিদ্যালয়ের সুনির্দিষ্ট প্রমোশন নীতিমালা জানা প্রতিটি শিক্ষার্থীর জন্য অপরিহার্য।\n\n"
            "এই পূর্ণাঙ্গ গাইডের মূল বিষয়সমূহ:\n"
            "- ৩য় বর্ষে প্রমোশন পাওয়ার জন্য ন্যূনতম কয়টি কোর্সে পাস (কমপক্ষে D গ্রেড) বাধ্যতামূলক\n"
            "- সর্বনিম্ন জিপিএ (GPA 2.00) ও ক্রেডিট অর্জনের সুনির্দিষ্ট নিয়মাবলী\n"
            "- কোনো বিষয়ে F গ্রেড থাকলে প্রমোশন নাকি ইমপ্রুভমেন্টের শর্তাবলী\n"
            "- ইংরেজি আবশ্যিক (নন-ক্রেডিট) বিষয়ে পাসের নিয়ম ও গুরুত্ব\n"
            "- পরীক্ষার হলে সময় বণ্টনের কার্যকরী কৌশল\n\n"
            "তোমার বন্ধুদের সচেতন করতে এবং নিজে উপকৃত হতে পোস্টটি শেয়ার করে টাইমলাইনে সংরক্ষণ করে রাখো।\n\n"
            "সম্পূর্ণ প্রমোশন রুলস ও প্রস্তুতি গাইড পড়তে ভিজিট করুন:\n"
            "https://www.helptrickbd.com/2026/10/nu-honours-2nd-year-exam-guide-and.html\n\n"
            "#NationalUniversity #NUHonours #Honours2ndYear #NUPromotionRules #HelpTrickBD #StudyGuide"
        )
    },
    {
        "url": "https://www.helptrickbd.com/2026/10/nu-exam-digitization-aqa-global-mou-2026.html",
        "title": "জাতীয় বিশ্ববিদ্যালয়ের পরীক্ষা ডিজিটালাইজেশন ও একিউএ গ্লোবাল চুক্তি: পরীক্ষা ও মূল্যায়নে ঐতিহাসিক পরিবর্তন",
        "category": "Education Guide",
        "hero_image": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/nu_exam_digitization_aqa_global_mou_2026.webp",
        "button_text": "সম্পূর্ণ চুক্তি ও সংস্কার বিশ্লেষণ পড়ুন",
        "telegram": (
            "<b>জাতীয় বিশ্ববিদ্যালয়ের পরীক্ষা ডিজিটালাইজেশন ও একিউএ গ্লোবাল চুক্তি: পরীক্ষা ও মূল্যায়নে ঐতিহাসিক পরিবর্তন</b>\n\n"
            "জাতীয় বিশ্ববিদ্যালয়ের পরীক্ষা পরিচালনা, খাতা মূল্যায়ন এবং দ্রুত ফল প্রকাশে যুক্তরাজ্যের একিউএ (AQA) গ্লোবালের সাথে ঐতিহাসিক সমঝোতা স্মারক স্বাক্ষরিত হয়েছে।\n\n"
            "<b>এই চুক্তির মূল সংস্কারসমূহ:</b>\n"
            "• ওএমআর (OMR) ও ডিজিটাল স্ক্রিপ্ট মূল্যায়নের নতুন রূপরেখা\n"
            "• পরীক্ষার ফল প্রকাশে দীর্ঘসূত্রতা ও সেশনজট নিরসনে অটোমেশন\n"
            "• আন্তর্জাতিক মানে জাতীয় বিশ্ববিদ্যালয়ের সনদের গ্রহণযোগ্যতা বৃদ্ধি\n"
            "• ডিজিটাল পরীক্ষা ব্যবস্থার ইতিবাচক প্রভাব ও ভবিষ্যৎ সম্ভাবনা\n\n"
            "<b>» চুক্তির রূপরেখা ও বিস্তারিত বিশ্লেষণ পড়তে ভিজিট করুন:</b>\n"
            "<a href=\"https://www.helptrickbd.com/2026/10/nu-exam-digitization-aqa-global-mou-2026.html\"><b>https://www.helptrickbd.com/2026/10/nu-exam-digitization-aqa-global-mou-2026.html</b></a>\n\n"
            "#NationalUniversity #NUNews #Digitization #AQAGlobal #HelpTrickBD"
        ),
        "facebook": (
            "জাতীয় বিশ্ববিদ্যালয়ের পরীক্ষা ডিজিটালাইজেশন ও একিউএ গ্লোবাল চুক্তি: পরীক্ষা ও মূল্যায়নে ঐতিহাসিক পরিবর্তন\n\n"
            "বাংলাদেশের উচ্চশিক্ষা ব্যবস্থার ইতিহাসে একটি যুগান্তকারী মাইলফলক স্থাপিত হয়েছে। জাতীয় বিশ্ববিদ্যালয়ের বিশাল পরীক্ষা পরিচালনা, খাতা মূল্যায়ন এবং ফলাফল প্রক্রিয়াকরণে আন্তর্জাতিক আধুনিক প্রযুক্তির সমন্বয় ঘটাতে যুক্তরাজ্যের একিউএ (AQA) গ্লোবালের সাথে ঐতিহাসিক সমঝোতা স্মারক স্বাক্ষরিত হয়েছে।\n\n"
            "এই ঐতিহাসিক চুক্তির ফলে কী কী পরিবর্তন আসছে:\n"
            "- ওএমআর (OMR) শিট ও ডিজিটাল পদ্ধতিতে উত্তরপত্র মূল্যায়নের নতুন রূপরেখা\n"
            "- পরীক্ষার রেজাল্ট প্রকাশে দীর্ঘসূত্রতা ও সেশনজট স্থায়ীভাবে দূর করার উদ্যোগ\n"
            "- আন্তর্জাতিক অঙ্গনে জাতীয় বিশ্ববিদ্যালয়ের সার্টিফিকেট ও ডিগ্রির গ্রহণযোগ্যতা বৃদ্ধি\n"
            "- শিক্ষার্থীদের পরীক্ষা ফি ও ট্র্যাকিং সহজতর করার আধুনিক অনলাইন সেবা\n\n"
            "জাতীয় বিশ্ববিদ্যালয়ের সকল শিক্ষার্থী ও শিক্ষকদের জন্য এটি একটি অত্যন্ত গুরুত্বপূর্ণ আপডেট। পোস্টটি শেয়ার করে সবাইকে জানার সুযোগ করে দিন।\n\n"
            "সম্পূর্ণ বিশ্লেষণ ও চুক্তির বিস্তারিত জানতে ভিজিট করুন:\n"
            "https://www.helptrickbd.com/2026/10/nu-exam-digitization-aqa-global-mou-2026.html\n\n"
            "#NationalUniversity #NUNews #Digitization #AQAGlobal #HigherEducation #HelpTrickBD"
        )
    },
    {
        "url": "https://www.helptrickbd.com/2026/10/class-6-to-9-annual-exam-marks-distribution-2026.html",
        "title": "৬ষ্ঠ, ৭ম, ৮ম ও ৯ম শ্রেণির বার্ষিক পরীক্ষার মানবণ্টন ও পূর্ণাঙ্গ প্রস্তুতি গাইড ২০২৬",
        "category": "Education Guide",
        "hero_image": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/class_6_to_9_annual_exam_marks_distribution_2026.webp",
        "button_text": "সম্পূর্ণ মানবণ্টন ও গাইড পড়ুন",
        "telegram": (
            "<b>৬ষ্ঠ, ৭ম, ৮ম ও ৯ম শ্রেণির বার্ষিক পরীক্ষার মানবণ্টন ও পূর্ণাঙ্গ প্রস্তুতি গাইড ২০২৬</b>\n\n"
            "জাতীয় শিক্ষাক্রম ও পাঠ্যপুস্তক বোর্ড (NCTB) এবং মাধ্যমিক ও উচ্চশিক্ষা অধিদপ্তর (মাউশি)-এর সর্বশেষ প্রজ্ঞাপন অনুযায়ী ৬ষ্ঠ থেকে ৯ম শ্রেণির বার্ষিক পরীক্ষার কাঠামো ও মানবণ্টন প্রকাশ করা হয়েছে।\n\n"
            "<b>এই গাইডে যা যা থাকছে:</b>\n"
            "• শ্রেণিভিত্তিক ও বিষয়ভিত্তিক ১০০ নম্বরের লিখিত ও নৈর্ব্যক্তিক মানবণ্টন\n"
            "• বাংলা, ইংরেজি, গণিত ও বিজ্ঞান বিষয়ের কাঠামোবদ্ধ নম্বর বিভাজন\n"
            "• পরীক্ষার খাতায় সর্বোচ্চ নম্বর তোলার বিশেষ উপস্থাপনা কৌশল\n"
            "• শেষ মুহূর্তের কার্যকরী প্রস্তুতি ও রিভিশন রুটিন\n\n"
            "<b>» সম্পূর্ণ মানবণ্টন ও স্টাডি গাইডলাইন পড়তে ভিজিট করুন:</b>\n"
            "<a href=\"https://www.helptrickbd.com/2026/10/class-6-to-9-annual-exam-marks-distribution-2026.html\"><b>https://www.helptrickbd.com/2026/10/class-6-to-9-annual-exam-marks-distribution-2026.html</b></a>\n\n"
            "#AnnualExam2026 #Class6to9 #MarksDistribution #NCTB #HelpTrickBD"
        ),
        "facebook": (
            "৬ষ্ঠ, ৭ম, ৮ম ও ৯ম শ্রেণির বার্ষিক পরীক্ষার মানবণ্টন ও পূর্ণাঙ্গ প্রস্তুতি গাইড ২০২৬\n\n"
            "জাতীয় শিক্ষাক্রম ও পাঠ্যপুস্তক বোর্ড (NCTB) এবং মাধ্যমিক ও উচ্চশিক্ষা অধিদপ্তর (মাউশি)-এর সর্বশেষ নির্দেশনা অনুযায়ী ৬ষ্ঠ থেকে ৯ম শ্রেণির বার্ষিক পরীক্ষার পূর্ণাঙ্গ মানবণ্টন ও সিলেবাস কাঠামো কার্যকর করা হয়েছে।\n\n"
            "এই পূর্ণাঙ্গ গাইডের মূল বিষয়সমূহ:\n"
            "- শ্রেণিভিত্তিক ও বিষয়ভিত্তিক ১০০ নম্বরের লিখিত ও নৈর্ব্যক্তিক মানবণ্টন রূপরেখা\n"
            "- বাংলা ১ম ও ২য় পত্র, ইংরেজি, গণিত এবং বিজ্ঞান বিষয়ের অধ্যায়ভিত্তিক নম্বর বিভাজন\n"
            "- সৃজনশীল ও বর্ণনামূলক প্রশ্নের সময় ব্যবস্থাপনা কৌশল\n"
            "- বার্ষিক পরীক্ষার খাতায় কাটাকাটি ছাড়া সর্বোচ্চ নম্বর পাওয়ার সহজ টিপস\n"
            "- অভিভাবকদের জন্য শিক্ষার্থীদের রিভিশন তত্ত্বাবধানের বিশেষ পরামর্শ\n\n"
            "অভিভাবক ও শিক্ষার্থীদের সুবিধার্থে পোস্টটি এখনই শেয়ার করে টাইমলাইনে সংরক্ষণ করুন।\n\n"
            "সম্পূর্ণ মানবণ্টন ও প্রস্তুতি গাইড পড়তে ভিজিট করুন:\n"
            "https://www.helptrickbd.com/2026/10/class-6-to-9-annual-exam-marks-distribution-2026.html\n\n"
            "#AnnualExam2026 #Class6to9 #MarksDistribution #NCTB #SchoolExam #HelpTrickBD"
        )
    },
    {
        "url": "https://www.helptrickbd.com/2026/10/nu-degree-2nd-year-in-course-and-exam.html",
        "title": "জাতীয় বিশ্ববিদ্যালয় ডিগ্রি ২য় বর্ষ ইনকোর্স নম্বর এন্ট্রি ও পরীক্ষার গাইড ২০২৬ | NU Degree 2nd Year In-Course & Exam Routine",
        "category": "Education Guide",
        "hero_image": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/nu_degree_2nd_year_in_course_2026.webp",
        "button_text": "ইনকোর্স ও পরীক্ষার গাইড পড়ুন",
        "telegram": (
            "<b>জাতীয় বিশ্ববিদ্যালয় ডিগ্রি ২য় বর্ষ ইনকোর্স নম্বর এন্ট্রি ও পরীক্ষার গাইড ২০২৬</b>\n\n"
            "জাতীয় বিশ্ববিদ্যালয়ের ডিগ্রি (পাস) ২য় বর্ষের ইনকোর্স পরীক্ষার নম্বর অনলাইনে এন্ট্রি ও চূড়ান্ত পরীক্ষা সংক্রান্ত অত্যন্ত গুরুত্বপূর্ণ নোটিশ ও গাইডলাইন প্রকাশিত হয়েছে।\n\n"
            "<b>এই গাইডে যা যা থাকছে:</b>\n"
            "• ডিগ্রি ২য় বর্ষ ইনকোর্স নম্বর এন্ট্রির বর্ধিত সময়সূচি ও কলেজ নির্দেশনা\n"
            "• ইনকোর্সে অনুপস্থিত থাকলে মূল রেজাল্টে কী প্রভাব পড়বে\n"
            "• ডিগ্রি ২য় বর্ষের চূড়ান্ত পরীক্ষার প্রস্তুতি ও পাস মার্কস কৌশল\n"
            "• পরীক্ষার হলের জন্য জাতীয় বিশ্ববিদ্যালয়ের কঠোর নিয়মাবলী\n\n"
            "<b>» সম্পূর্ণ নোটিশ ও ইনকোর্স গাইডলাইন বিস্তারিত পড়তে ভিজিট করুন:</b>\n"
            "<a href=\"https://www.helptrickbd.com/2026/10/nu-degree-2nd-year-in-course-and-exam.html\"><b>https://www.helptrickbd.com/2026/10/nu-degree-2nd-year-in-course-and-exam.html</b></a>\n\n"
            "#NationalUniversity #NUDegree #Degree2ndYear #InCourseExam #HelpTrickBD"
        ),
        "facebook": (
            "জাতীয় বিশ্ববিদ্যালয় ডিগ্রি ২য় বর্ষ ইনকোর্স নম্বর এন্ট্রি ও পরীক্ষার গাইড ২০২৬ | NU Degree 2nd Year In-Course & Exam Routine\n\n"
            "জাতীয় বিশ্ববিদ্যালয়ের ডিগ্রি (পাস) ও সার্টিফিকেট কোর্সের ২য় বর্ষের ইনকোর্স পরীক্ষার নম্বর অনলাইনে এন্ট্রি এবং চূড়ান্ত পরীক্ষার প্রস্তুতি নিয়ে গুরুত্বপূর্ণ নির্দেশনা জারি করা হয়েছে।\n\n"
            "এই নির্দেশিকায় যা যা থাকছে:\n"
            "- ইনকোর্স নম্বর অনলাইনে প্রেরণের বর্ধিত সময়সূচি ও কলেজ প্রশাসনের দায়িত্ব\n"
            "- ইনকোর্স পরীক্ষায় অংশ না নিলে প্রমোশন ও রেজাল্টে যে জটিলতা সৃষ্টি হতে পারে\n"
            "- ডিগ্রি ২য় বর্ষ পরীক্ষার পূর্ণাঙ্গ মানবণ্টন ও পাস মার্কসের নিয়মাবলী\n"
            "- শেষ মুহূর্তে ভালো ফলাফল অর্জনের জন্য কার্যকরী প্রস্তুতি রুটিন\n\n"
            "ডিগ্রি ২য় বর্ষের সকল সহপাঠীদের সাথে তথ্যটি শেয়ার করে জানিয়ে দিন।\n\n"
            "সম্পূর্ণ গাইডলাইন পড়তে ক্লিক করুন:\n"
            "https://www.helptrickbd.com/2026/10/nu-degree-2nd-year-in-course-and-exam.html\n\n"
            "#NationalUniversity #NUDegree #Degree2ndYear #InCourseExam #NUNotice #HelpTrickBD"
        )
    },
    {
        "url": "https://www.helptrickbd.com/2026/10/nu-honours-2nd-year-exam-routine-2026.html",
        "title": "জাতীয় বিশ্ববিদ্যালয় অনার্স ২য় বর্ষ পরীক্ষার রুটিন ২০২৬ (সকল বিভাগ) | NU Honours 2nd Year Exam Routine & Subject Code",
        "category": "Education Guide",
        "hero_image": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/nu_honours_2nd_year_routine_2026.webp",
        "button_text": "সম্পূর্ণ রুটিন ও বিষয়কোড দেখুন",
        "telegram": (
            "<b>জাতীয় বিশ্ববিদ্যালয় অনার্স ২য় বর্ষ পরীক্ষার রুটিন ২০২৬ (সকল বিভাগ) | বিষয়কোড ও সময়সূচি</b>\n\n"
            "জাতীয় বিশ্ববিদ্যালয়ের অনার্স ২য় বর্ষের সংশোধিত চূড়ান্ত পরীক্ষার রুটিন প্রকাশিত হয়েছে। বিএ, বিএসএস, বিবিএ ও বিএসসি সকল বিভাগের পরীক্ষার্থীদের জন্য জরুরি আপডেট।\n\n"
            "<b>এই গাইডে যা যা থাকছে:</b>\n"
            "• সকল বিভাগের পূর্ণাঙ্গ সংশোধিত পরীক্ষার সময়সূচি ও বিষয়কোড\n"
            "• প্রতিদিনের পরীক্ষা শুরু ও সমাপ্তির সঠিক সময়\n"
            "• আবশ্যিক ইংরেজি পরীক্ষায় নিশ্চিত পাসের শর্টকাট কৌশল\n"
            "• পরীক্ষার হলে নিষিদ্ধ সামগ্রী ও রেজিস্ট্রেশন কার্ড সংক্রান্ত নির্দেশনা\n\n"
            "<b>» সম্পূর্ণ রুটিন ও বিভাগভিত্তিক বিষয়কোড দেখতে ভিজিট করুন:</b>\n"
            "<a href=\"https://www.helptrickbd.com/2026/10/nu-honours-2nd-year-exam-routine-2026.html\"><b>https://www.helptrickbd.com/2026/10/nu-honours-2nd-year-exam-routine-2026.html</b></a>\n\n"
            "#NationalUniversity #Honours2ndYear #ExamRoutine2026 #SubjectCode #HelpTrickBD"
        ),
        "facebook": (
            "জাতীয় বিশ্ববিদ্যালয় অনার্স ২য় বর্ষ পরীক্ষার রুটিন ২০২৬ (সকল বিভাগ) | NU Honours 2nd Year Exam Routine & Subject Code\n\n"
            "জাতীয় বিশ্ববিদ্যালয়ের অনার্স ২য় বর্ষের সংশোধিত চূড়ান্ত পরীক্ষার সময়সূচি ও বিষয়ভিত্তিক কোড আনুষ্ঠানিকভাবে প্রকাশিত হয়েছে। বিএ, বিএসএস, বিবিএ এবং বিএসসি সকল বিভাগের পরীক্ষার্থীদের সময়মতো রুটিন সংগ্রহ করা প্রয়োজন।\n\n"
            "এই পূর্ণাঙ্গ গাইডে যা যা থাকছে:\n"
            "- সকল বিভাগের সমন্বিত পরীক্ষার সময়সূচি ও বিষয়কোড চার্ট\n"
            "- আবশ্যিক ইংরেজি নন-ক্রেডিট পরীক্ষায় সহজেই পাস করার টেকনিক\n"
            "- পরীক্ষার হলে প্রবেশপত্র ও রেজিস্ট্রেশন কার্ড সংরক্ষণের নিয়ম\n"
            "- পরীক্ষার দিনগুলোতে শেষ মুহূর্তের রিভিশন ও মানসিক প্রস্তুতির টিপস\n\n"
            "পরীক্ষার্থী বন্ধুদের সাথে রুটিনটি শেয়ার করে প্রস্তুত থাকতে সহায়তা করুন।\n\n"
            "সম্পূর্ণ রুটিন ও বিষয়কোড বিস্তারিত জানতে ক্লিক করুন:\n"
            "https://www.helptrickbd.com/2026/10/nu-honours-2nd-year-exam-routine-2026.html\n\n"
            "#NationalUniversity #Honours2ndYear #ExamRoutine2026 #SubjectCode #NUExam #HelpTrickBD"
        )
    },
    {
        "url": "https://www.helptrickbd.com/2026/09/geopolitics-definition-elements-nature.html",
        "title": "ভূরাজনীতি কাকে বলে? সংজ্ঞা, উপাদান, প্রকৃতি, রাজনৈতিক ভূগোলের সাথে পার্থক্য এবং বাংলাদেশের ভূরাজনীতি",
        "category": "Political Science",
        "hero_image": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/geopolitics-bangladesh-political-science-notes.webp",
        "button_text": "সম্পূর্ণ ভূরাজনীতি হ্যান্ডনোট পড়ুন",
        "telegram": (
            "<b>ভূরাজনীতি কাকে বলে? সংজ্ঞা, উপাদান, প্রকৃতি এবং বাংলাদেশের ভূরাজনীতি</b>\n\n"
            "আন্তর্জাতিক সম্পর্ক ও রাষ্ট্রবিজ্ঞানে ভূরাজনীতি (Geopolitics) একটি অত্যন্ত মৌলিক প্রত্যয়। ভৌগোলিক অবস্থানের ভিত্তিতে পররাষ্ট্রনীতি প্রণয়ন ও জাতীয় স্বার্থ রক্ষা এর মূল বিষয়।\n\n"
            "<b>এই হ্যান্ডনোটে যা যা থাকছে:</b>\n"
            "• ভূরাজনীতির প্রামাণ্য সংজ্ঞা ও তাত্ত্বিক ভিত্তি (ম্যাকিন্ডার ও কিয়েলেন)\n"
            "• রাজনৈতিক ভূগোল ও ভূরাজনীতির মধ্যকার সুস্পষ্ট পার্থক্যের ছক\n"
            "• ভূরাজনীতির মৌলিক উপাদানসমূহ (অবস্থান, আয়তন ও প্রাকৃতিক সম্পদ)\n"
            "• বঙ্গোপসাগর কেন্দ্রিক কৌশলগত দ্বন্দ্ব ও বাংলাদেশের ভূরাজনৈতিক গুরুত্ব\n"
            "• বিসিএস লিখিত ও বিশ্ববিদ্যালয় পরীক্ষার জন্য মডেল প্রশ্নোত্তর\n\n"
            "<b>» সম্পূর্ণ স্টাডি হ্যান্ডনোট বিস্তারিত পড়তে ভিজিট করুন:</b>\n"
            "<a href=\"https://www.helptrickbd.com/2026/09/geopolitics-definition-elements-nature.html\"><b>https://www.helptrickbd.com/2026/09/geopolitics-definition-elements-nature.html</b></a>\n\n"
            "#PoliticalScience #Geopolitics #InternationalRelations #BCSPreparation #HelpTrickBD"
        ),
        "facebook": (
            "ভূরাজনীতি কাকে বলে? সংজ্ঞা, উপাদান, প্রকৃতি, রাজনৈতিক ভূগোলের সাথে পার্থক্য এবং বাংলাদেশের ভূরাজনীতি\n\n"
            "আন্তর্জাতিক সম্পর্ক ও রাষ্ট্রবিজ্ঞানের অত্যন্ত গুরুত্বপূর্ণ একটি প্রত্যয় হলো ভূরাজনীতি (Geopolitics)। ভৌগোলিক অবস্থানের ভিত্তিতে একটি রাষ্ট্র কীভাবে তার জাতীয় নিরাপত্তা, পররাষ্ট্রনীতি এবং আন্তর্জাতিক প্রভাব বিস্তার করে, তা বিশ্লেষণে ভূরাজনীতি অতুলনীয় ভূমিকা রাখে।\n\n"
            "এই পূর্ণাঙ্গ হ্যান্ডনোটে যা যা বিস্তারিত আলোচনা করা হয়েছে:\n"
            "- ভূরাজনীতির প্রামাণ্য সংজ্ঞা ও মৌলিক তাত্ত্বিক বিকাশ (ম্যাকিন্ডার ও কিয়েলেনের তত্ত্ব)\n"
            "- রাজনৈতিক ভূগোল (Political Geography) এবং ভূরাজনীতির মধ্যে মূল পার্থক্যের তুলনামূলক ছক\n"
            "- ভূরাজনীতির প্রধান উপাদান: অবস্থান, ভূখণ্ড, জনসংখ্যা ও প্রাকৃতিক সম্পদ\n"
            "- বঙ্গোপসাগর কেন্দ্রিক বৈশ্বিক ক্ষমতার দ্বন্দ্ব এবং বাংলাদেশের ভূকৌশলগত গুরুত্ব\n"
            "- বিশ্ববিদ্যালয় ও বিসিএস লিখিত পরীক্ষার জন্য সম্পূর্ণ মডেল প্রশ্নের উত্তর কাঠামো\n\n"
            "রাষ্ট্রবিজ্ঞান শিক্ষার্থী ও বিসিএস প্রত্যাশী বন্ধুদের জন্য এটি একটি অবশ্য পাঠ্য হ্যান্ডনোট। টাইমলাইনে শেয়ার করে রাখুন।\n\n"
            "সম্পূর্ণ হ্যান্ডনোটটি পড়তে ভিজিট করুন:\n"
            "https://www.helptrickbd.com/2026/09/geopolitics-definition-elements-nature.html\n\n"
            "#PoliticalScience #Geopolitics #InternationalRelations #BCSPreparation #NUHonours #HelpTrickBD"
        )
    },
    {
        "url": "https://www.helptrickbd.com/2026/09/public-university-admission-eligibility.html",
        "title": "পাবলিক বিশ্ববিদ্যালয় ভর্তি যোগ্যতা ২০২৬: বিজ্ঞান, মানবিক ও ব্যবসায় শাখা পূর্ণাঙ্গ গাইড (Public University Admission Guide 2026)",
        "category": "Education Guide",
        "hero_image": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/public_university_admission_guide_2026.webp",
        "button_text": "সম্পূর্ণ ভর্তি গাইড পড়ুন",
        "telegram": (
            "<b>পাবলিক বিশ্ববিদ্যালয় ভর্তি যোগ্যতা ২০২৬: বিজ্ঞান, মানবিক ও ব্যবসায় শাখা পূর্ণাঙ্গ গাইড</b>\n\n"
            "এইচএসসি পরীক্ষার পর বিশ্ববিদ্যালয়ে ভর্তি পরীক্ষা প্রতিটি শিক্ষার্থীর জীবনের অন্যতম বড় টার্নিং পয়েন্ট। রেজাল্ট প্রকাশের পূর্বেই সঠিক প্রস্তুতি ও যোগ্যতা জানা থাকলে কাঙ্ক্ষিত বিশ্ববিদ্যালয়ে আসন নিশ্চিত করা সহজ হয়।\n\n"
            "<b>এই গাইডে যা যা থাকছে:</b>\n"
            "• বিজ্ঞান, মানবিক ও ব্যবসায় শাখা অনুযায়ী বিষয় নির্বাচন ম্যাট্রিক্স\n"
            "• ঢাবি, রাবি, চবি, জাবি ও গুচ্ছভুক্ত ২৪টি বিশ্ববিদ্যালয়ের জিপিএ যোগ্যতা\n"
            "• ভর্তি আবেদন ও পরীক্ষার হলের ৬টি মারাত্মক ফাঁদ এড়ানোর কৌশল\n"
            "• রেজাল্ট আশানুরূপ না হলে বিকল্প পথ ও ব্যাকআপ প্ল্যান (Plan-B)\n"
            "• বোর্ড চ্যালেঞ্জ চলাকালীন আবেদন প্রক্রিয়ার সঠিক নিয়মাবলী\n\n"
            "<b>» সম্পূর্ণ পাবলিক বিশ্ববিদ্যালয় ভর্তি গাইড পড়তে ভিজিট করুন:</b>\n"
            "<a href=\"https://www.helptrickbd.com/2026/09/public-university-admission-eligibility.html\"><b>https://www.helptrickbd.com/2026/09/public-university-admission-eligibility.html</b></a>\n\n"
            "#UniversityAdmission2026 #VarsityAdmission #HSC2026 #HelpTrickBD #StudyGuide"
        ),
        "facebook": (
            "পাবলিক বিশ্ববিদ্যালয় ভর্তি যোগ্যতা ২০২৬: বিজ্ঞান, মানবিক ও ব্যবসায় শাখা পূর্ণাঙ্গ গাইড (Public University Admission Guide 2026)\n\n"
            "এইচএসসি পরীক্ষা শেষ হওয়ার পর বিশ্ববিদ্যালয়ের ভর্তি পরীক্ষা (Public University Admission 2026) প্রতিটি শিক্ষার্থীর জীবনের সবচেয়ে বড় টার্নিং পয়েন্ট। রেজাল্ট প্রকাশের আগেই সঠিক প্রস্তুতি ও বিষয়ভিত্তিক কৌশল জানা থাকলে ঢাকা বিশ্ববিদ্যালয় (DU), রাজশাহী বিশ্ববিদ্যালয় (RU), চট্টগ্রাম বিশ্ববিদ্যালয় (CU), জাহাঙ্গীরনগর বিশ্ববিদ্যালয় (JU), কৃষি গুচ্ছ ও সাধারণ গুচ্ছের ২৪টি পাবলিক বিশ্ববিদ্যালয়ে নিজের আসন নিশ্চিত করা সম্ভব।\n\n"
            "এই পূর্ণাঙ্গ গাইডের মূল বিষয়সমূহ:\n"
            "- বিজ্ঞান, মানবিক ও ব্যবসায় শাখা অনুযায়ী কোন কোন বিষয়ে আবেদন করা যাবে\n"
            "- শীর্ষ বিশ্ববিদ্যালয়গুলোর জিপিএ যোগ্যতা, আসন সংখ্যা ও মানবণ্টন\n"
            "- এইচএসসি রেজাল্টের অপেক্ষার ৬০ দিন কেন ভর্তি যুদ্ধের গোল্ডেন টাইম\n"
            "- ভর্তি আবেদন ও পরীক্ষার হলের ৬টি মারাত্মক ফাঁদ (যা না জানলে চান্স পেয়েও স্বপ্নভঙ্গ হতে পারে)\n"
            "- রেজাল্ট আশানুরূপ না হলে বিকল্প পথ ও ব্যাকআপ প্ল্যান (Plan-B: GST & Agri Cluster)\n"
            "- বোর্ড চ্যালেঞ্জ চলাকালীন বিশ্ববিদ্যালয়ের আবেদনের সঠিক নিয়ম\n\n"
            "ভর্তি যুদ্ধে অংশগ্রহণকারী সকল ভাই-বোনদের জন্য পোস্টটি অত্যন্ত মূল্যবান। শেয়ার করে টাইমলাইনে সংরক্ষণ করুন।\n\n"
            "সম্পূর্ণ আর্টিকেলটি বিস্তারিত পড়তে ভিজিট করুন:\n"
            "https://www.helptrickbd.com/2026/09/public-university-admission-eligibility.html\n\n"
            "#HelpTrickBD #UniversityAdmission2026 #VarsityAdmission #HSC2026 #DUAdmission #StudyGuide #EducationBD"
        )
    }
]

def main():
    print("=" * 65)
    print("হেল্পট্রিকবিডি ৭টি নতুন পোস্ট সোশ্যাল ব্রডকাস্ট ইঞ্জিন")
    print("=" * 65)

    if not os.path.exists(CREDS_FILE):
        print("ত্রুটি: সোশ্যাল ক্রেডেনশিয়াল ফাইল পাওয়া যায়নি।")
        sys.exit(1)

    with open(CREDS_FILE, "r", encoding="utf-8") as f:
        creds = json.load(f)

    # Load audit data
    if os.path.exists(AUDIT_DATA_FILE):
        with open(AUDIT_DATA_FILE, "r", encoding="utf-8") as f:
            audit_data = json.load(f)
    else:
        audit_data = []

    existing_urls = {r.get("url") for r in audit_data if r.get("url")}

    # Initialize publishers
    tg_pub = TelegramPublisher(
        bot_token=creds["telegram"]["bot_token"],
        channel_id=creds["telegram"]["channel_id"]
    )
    fb_pub = FacebookPublisher(
        page_id=creds["facebook"]["page_id"],
        page_access_token=creds["facebook"]["page_access_token"],
        make_webhook_url=creds["facebook"].get("make_webhook_url")
    )

    # Test connections
    print("সংযোগ পরীক্ষা করা হচ্ছে...")
    tg_test = tg_pub.test_connection()
    print("টেলিগ্রাম সংযোগ:", tg_test.get("message"))
    fb_test = fb_pub.test_connection()
    print("ফেসবুক সংযোগ:", fb_test.get("message"))

    if not tg_test.get("success") or not fb_test.get("success"):
        print("ত্রুটি: সংযোগ পরীক্ষায় সমস্যা হয়েছে। ব্রডকাস্ট স্থগিত করা হলো।")
        sys.exit(1)

    total_posts = len(NEW_POSTS)
    print(f"\nমোট নতুন ব্রডকাস্ট পোস্ট: {total_posts}টি")
    print("ব্রডকাস্ট প্রক্রিয়া শুরু হচ্ছে...\n")

    results = []

    for i, post in enumerate(NEW_POSTS, 1):
        print(f"[{i}/{total_posts}] পোস্ট ব্রডকাস্ট হচ্ছে: {post['title']}")
        print(f"  ইউআরএল: {post['url']}")
        print(f"  ইমেজ: {post['hero_image']}")

        record = {
            "url": post["url"],
            "title": post["title"],
            "category": post["category"],
            "hero_image": post["hero_image"],
            "posted_facebook": False,
            "posted_telegram": False,
            "copy": {
                "button_text": post["button_text"],
                "telegram": post["telegram"],
                "facebook": post["facebook"]
            }
        }

        # 1. Publish to Facebook
        fb_res = fb_pub.publish_post(
            message=post["facebook"],
            link=post["url"],
            image_url=post["hero_image"],
            post_type="link",
            title=post["title"]
        )
        if fb_res.get("success"):
            record["posted_facebook"] = True
            record["facebook_result"] = fb_res.get("message", "পাবলিশ সম্পন্ন")
            record["facebook_timestamp"] = datetime.now().isoformat()
            print(f"  [ফেসবুক]: {fb_res.get('message')}")
        else:
            print(f"  [ফেসবুক ব্যর্থ]: {fb_res.get('message')}")

        # 2. Publish to Telegram
        tg_res = tg_pub.publish_post(
            text=post["telegram"],
            image_url=post["hero_image"],
            button_text=post["button_text"],
            button_url=post["url"]
        )
        if tg_res.get("success"):
            record["posted_telegram"] = True
            record["telegram_msg_id"] = tg_res.get("message_id")
            record["telegram_result"] = tg_res.get("message", "পাবলিশ সম্পন্ন")
            record["telegram_timestamp"] = datetime.now().isoformat()
            print(f"  [টেলিগ্রাম]: {tg_res.get('message')}")
        else:
            print(f"  [টেলিগ্রাম ব্যর্থ]: {tg_res.get('message')}")

        # Append to audit data
        if post["url"] in existing_urls:
            for idx, existing in enumerate(audit_data):
                if existing.get("url") == post["url"]:
                    audit_data[idx] = record
                    break
        else:
            audit_data.append(record)
            existing_urls.add(post["url"])

        # Immediate save
        with open(AUDIT_DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(audit_data, f, ensure_ascii=False, indent=2)

        results.append({
            "title": post["title"],
            "url": post["url"],
            "facebook": record["posted_facebook"],
            "telegram": record["posted_telegram"]
        })

        print("-" * 50)

        # Anti-spam delay between posts
        if i < total_posts:
            delay_sec = 12
            print(f"পরবর্তী পোস্টের জন্য {delay_sec} সেকেন্ড অপেক্ষা করা হচ্ছে (Anti-Spam Delay)...")
            time.sleep(delay_sec)

    print("\n" + "=" * 65)
    print("ব্রডকাস্ট সম্পন্ন সারসংক্ষেপ")
    print("=" * 65)
    for r in results:
        fb_status = "সফল" if r["facebook"] else "ব্যর্থ"
        tg_status = "সফল" if r["telegram"] else "ব্যর্থ"
        print(f"পোস্ট: {r['title'][:45]}...")
        print(f"  ফেসবুক: {fb_status} | টেলিগ্রাম: {tg_status}")

if __name__ == "__main__":
    main()
