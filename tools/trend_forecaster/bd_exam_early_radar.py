#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/trend_forecaster/bd_exam_early_radar.py
---------------------------------------------
Helptrickbd Master Bangladesh 360-Degree Academic & Career Radar.

Covers:
- Tier 1: Primary Education (Class 1 to 5, Primary Scholarship, Annual Exam)
- Tier 2: Secondary & School (Class 6 to 9 Annual Assessment, Class 10/SSC/Dakhil/Vocational)
- Tier 3: Higher Secondary (Class 11-12, HSC/Alim, Polytechnic Diploma BTEB)
- Tier 4: Tertiary & Universities (NU Honours 1st-4th Year, Masters Final, Degree Pass, 7 Colleges)
- Tier 5: University Admission Tests (DU, Medical, BUET, GST Cluster, Agricultural Cluster)
- Tier 6: Competitive Job Exams (BCS Preliminary/Written, Primary Assistant Teacher, NTRCA, Banks, Govt Jobs)

Calculates the 30-45 Day SEO Golden Window for every single educational tier so Helptrickbd
ranks #1 on Google 1-2 months ahead of competitors.

Zero-emoji compliance (Rule 12).
"""

import os
import sys
import json
import argparse
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUTPUT_REPORT = os.path.join(PROJECT_ROOT, "bd_exam_seo_radar_report.md")
LIVE_POSTS_PATH = os.path.join(PROJECT_ROOT, "scratch", "all_112_live_posts.json")

# Master 360-Degree Bangladesh Education & Career Lifecycle Database
BD_COMPREHENSIVE_RADAR_CALENDAR = [
    # =========================================================================
    # TIER 1: PRIMARY EDUCATION (CLASS 1 - 5)
    # =========================================================================
    {
        "tier": "Tier 1: Primary (শ্রেণি ১ - ৫)",
        "exam_name": "প্রাথমিক বৃত্তি পরীক্ষা ও ট্যালেন্টপুল মেধা তালিকা (Class 5)",
        "category": "Education Guide / Primary",
        "exam_window": "ডিসেম্বর শেষ সপ্তাহ",
        "target_month": 12,
        "lead_time_days": 45,
        "search_volume": "বিশাল (14x)",
        "target_keywords": [
            "প্রাথমিক বৃত্তি পরীক্ষার রুটিন ২০২৬",
            "প্রাইমারি বৃত্তি সাজেশন বাংলা গণিত ইংরেজি",
            "বৃত্তি পরীক্ষার মানবণ্টন ও ফি",
            "প্রাথমিক বৃত্তি প্রশ্ন ব্যাংক ও সমাধান"
        ],
        "content_blueprint": "৫ম শ্রেণির শিক্ষার্থীদের জন্য বাংলা, ইংরেজি, গণিত ও বিজ্ঞান বিষয়ের ১০০ নম্বরের পূর্ণাঙ্গ মডেল টেস্ট, মানবণ্টন ও ট্যালেন্টপুল বৃত্তির কৌশল।"
    },
    {
        "tier": "Tier 1: Primary (শ্রেণি ১ - ৫)",
        "exam_name": "Class 1 থেকে Class 5 বার্ষিক পরীক্ষা ও প্রান্তিক মূল্যায়ন",
        "category": "Education Guide / School",
        "exam_window": "নভেম্বর - ডিসেম্বর",
        "target_month": 11,
        "lead_time_days": 35,
        "search_volume": "উচ্চ (9x)",
        "target_keywords": [
            "প্রাথমিক বিদ্যালয় বার্ষিক পরীক্ষার রুটিন",
            "১ম থেকে ৫ম শ্রেণি বার্ষিক পরীক্ষার প্রশ্ন",
            "প্রান্তিক মূল্যায়ন প্রশ্ন ও সমাধান ২০২৬",
            "প্রাথমিক গণিত ও ইংরেজি হ্যান্ডনোট"
        ],
        "content_blueprint": "প্রথম থেকে পঞ্চম শ্রেণির বার্ষিক পরীক্ষার সময়সূচি, চূড়ান্ত নমুনা প্রশ্নপত্র এবং সহজে এ প্লাস পাওয়ার সমাধান নোট।"
    },
    {
        "tier": "Tier 1: Primary (শ্রেণি ১ - ৫)",
        "exam_name": "নতুন শিক্ষাবর্ষের প্রাথমিক বিদ্যালয়ে ভর্তি ও বই উৎসব (Class 1-5)",
        "category": "Education Guide / Primary",
        "exam_window": "ডিসেম্বর - জানুয়ারি",
        "target_month": 12,
        "lead_time_days": 30,
        "search_volume": "মাঝারি (7x)",
        "target_keywords": [
            "সরকারি প্রাথমিক বিদ্যালয়ে ভর্তি নিয়ম",
            "বই উৎসব ২০২৬ তারিখ",
            "১ম শ্রেণিতে লটারি ভর্তি আবেদন",
            "প্রাথমিক শিক্ষা অধিদপ্তরের ভর্তি নির্দেশিকা"
        ],
        "content_blueprint": "সরকারি প্রাথমিক বিদ্যালয়ে অনলাইন লটারি আবেদন পদ্ধতি, প্রয়োজনীয় ডকুমেন্টস এবং ১ জানুয়ারির বিনামূল্যে বই উৎসবের বিবরণ।"
    },

    # =========================================================================
    # TIER 2: JUNIOR & SECONDARY (CLASS 6 - 10 & SSC / DAKHIL)
    # =========================================================================
    {
        "tier": "Tier 2: Secondary (শ্রেণি ৬ - ১০ ও এসএসসি)",
        "exam_name": "Class 6 থেকে Class 9 বার্ষিক মূল্যায়ন ও ফাইনাল পরীক্ষা",
        "category": "School / Class 6-9",
        "exam_window": "নভেম্বর - ডিসেম্বর",
        "target_month": 11,
        "lead_time_days": 35,
        "search_volume": "অত্যধিক উচ্চ (13x)",
        "target_keywords": [
            "৬ষ্ঠ ৭ম ৮ম ৯ম শ্রেণি বার্ষিক পরীক্ষার রুটিন",
            "নতুন কারিকুলাম বার্ষিক সামষ্টিক মূল্যায়ন ২০২৬",
            "ক্লাস ৭ ইংরেজি বার্ষিক পরীক্ষার প্রশ্ন",
            "ক্লাস ৮ গণিত বার্ষিক সাজেশন",
            "ক্লাস ৯ বাংলা ১ম পত্র হ্যান্ডনোট"
        ],
        "content_blueprint": "৬ষ্ঠ, ৭ম, ৮ম ও ৯ম শ্রেণির শিক্ষার্থীদের জন্য নতুন শিক্ষাক্রম ও প্রচলিত পদ্ধতির বার্ষিক পরীক্ষার মানবণ্টন, নমুনা অ্যাসাইনমেন্ট ও সুপার শর্ট সাজেশন।"
    },
    {
        "tier": "Tier 2: Secondary (শ্রেণি ৬ - ১০ ও এসএসসি)",
        "exam_name": "এসএসসি, দাখিল ও ভোকেশনাল নির্বাচনী (টেস্ট) পরীক্ষা",
        "category": "School / SSC",
        "exam_window": "অক্টোবর - নভেম্বর",
        "target_month": 11,
        "lead_time_days": 30,
        "search_volume": "বিশাল (16x)",
        "target_keywords": [
            "এসএসসি টেস্ট পরীক্ষার প্রশ্ন ২০২৬",
            "এসএসসি বাংলা ১ম পত্র টেস্ট সাজেশন",
            "ssc english 2nd paper model test",
            "দাখিল নির্বাচনী পরীক্ষার প্রশ্ন ব্যাংক",
            "ভোকেশনাল টেস্ট পরীক্ষার রুটিন"
        ],
        "content_blueprint": "এসএসসি, দাখিল ও ভোকেশনাল পরীক্ষার্থীদের জন্য নির্বাচনী পরীক্ষার বাংলা, ইংরেজি ও সাধারণ বিজ্ঞান বিষয়ের ১০০% কমন টেস্ট সাজেশন ও মডেল টেস্ট।"
    },
    {
        "tier": "Tier 2: Secondary (শ্রেণি ৬ - ১০ ও এসএসসি)",
        "exam_name": "এসএসসি ও দাখিল বোর্ড পরীক্ষা ২০২৭/২০২৬ চূড়ান্ত প্রস্তুতি",
        "category": "School / SSC",
        "exam_window": "ফেব্রুয়ারি - মার্চ",
        "target_month": 2,
        "lead_time_days": 90,
        "search_volume": "সর্বোচ্চ (20x)",
        "target_keywords": [
            "ssc exam routine 2027",
            "এসএসসি বাংলা সাজেশন ২০২৭",
            "ssc english 1st paper suggestion 2027",
            "এসএসসি গণিত সৃজনশীল সমাধান",
            "এসএসসি পদার্থ ও রসায়ন ১০০% কমন"
        ],
        "content_blueprint": "এসএসসি বোর্ড পরীক্ষার সকল বিষয়ের অধ্যায়ভিত্তিক সুপার সাজেশন, বোর্ড পরীক্ষার প্রশ্নপত্র সমাধান এবং এ প্লাস নিশ্চিত করার স্পেশাল টিপস।"
    },
    {
        "tier": "Tier 2: Secondary (শ্রেণি ৬ - ১০ ও এসএসসি)",
        "exam_name": "এসএসসি ফলাফল ও একাদশ শ্রেণিতে কলেজ ভর্তি (XI Admission)",
        "category": "College / Admission",
        "exam_window": "মে - জুলাই",
        "target_month": 5,
        "lead_time_days": 45,
        "search_volume": "সর্বোচ্চ (18x)",
        "target_keywords": [
            "ssc result mark sheet download",
            "বোর্ড চ্যালেঞ্জ আবেদন নিয়ম",
            "একাদশ শ্রেণিতে কলেজ চয়েস নিয়ম",
            "সেরা সরকারি কলেজের জিপিএ তালিকা"
        ],
        "content_blueprint": "এসএসসি পরীক্ষার রেজাল্ট প্রকাশের পর পুনঃনিরীক্ষণ আবেদন, মার্কশিট ডাউনলোড এবং নটর ডেম কলেজসহ সেরা সরকারি কলেজে ভর্তির পূর্ণাঙ্গ গাইড।"
    },

    # =========================================================================
    # TIER 3: HIGHER SECONDARY (HSC / ALIM / BTEB DIPLOMA)
    # =========================================================================
    {
        "tier": "Tier 3: Higher Secondary (এইচএসসি, আলিম ও ডিপ্লোমা)",
        "exam_name": "দ্বাদশ শ্রেণি নির্বাচনী (HSC Test Exam) পরীক্ষা",
        "category": "College / HSC",
        "exam_window": "ডিসেম্বর - জানুয়ারি",
        "target_month": 12,
        "lead_time_days": 40,
        "search_volume": "উচ্চ (11x)",
        "target_keywords": [
            "এইচএসসি টেস্ট পরীক্ষার রুটিন",
            "এইচএসসি টেস্ট পরীক্ষার বাংলা সাজেশন",
            "hsc english test exam model questions",
            "এইচএসসি আইসিটি নির্বাচনী সাজেশন"
        ],
        "content_blueprint": "এইচএসসি ও আলিম পরীক্ষার্থীদের টেস্ট পরীক্ষার জন্য বাংলা ১ম, ইংরেজি ২য় পত্র এবং তথ্য ও যোগাযোগ প্রযুক্তির (ICT) স্পেশাল মডেল টেস্ট।"
    },
    {
        "tier": "Tier 3: Higher Secondary (এইচএসসি, আলিম ও ডিপ্লোমা)",
        "exam_name": "এইচএসসি ও আলিম বোর্ড ফাইনাল পরীক্ষা",
        "category": "College / HSC",
        "exam_window": "এপ্রিল - জুন",
        "target_month": 4,
        "lead_time_days": 90,
        "search_volume": "সর্বোচ্চ (19x)",
        "target_keywords": [
            "এইচএসসি পরীক্ষার রুটিন ২০২৬",
            "এইচএসসি বাংলা ১ম পত্র সাজেশন",
            "এইচএসসি আইসিটি হ্যান্ডনোট ও বহুনির্বাচনী",
            "এইচএসসি পৌরনীতি ও সুশাসন"
        ],
        "content_blueprint": "এইচএসসি মানবিক, বিজ্ঞান ও ব্যবসায় শিক্ষা শাখার সকল বিষয়ের বোর্ড স্ট্যান্ডার্ড ফাইনাল হ্যান্ডনোট ও প্রশ্ন সমাধান।"
    },
    {
        "tier": "Tier 3: Higher Secondary (এইচএসসি, আলিম ও ডিপ্লোমা)",
        "exam_name": "কারিগরি শিক্ষা বোর্ড (BTEB) পলিটেকনিক ডিপ্লোমা ইন ইঞ্জিনিয়ারিং পরীক্ষা",
        "category": "Technical / BTEB",
        "exam_window": "জুন ও ডিসেম্বর",
        "target_month": 12,
        "lead_time_days": 35,
        "search_volume": "উচ্চ (8x)",
        "target_keywords": [
            "কারিগরি শিক্ষা বোর্ড ডিপ্লোমা রুটিন",
            "পলিটেকনিক সেমিস্টার ফাইনাল সাজেশন",
            "ডিপ্লোমা ইন ইঞ্জিনিয়ারিং প্রশ্ন ব্যাংক",
            "বিটিইবি নোটিশ রেজাল্ট"
        ],
        "content_blueprint": "পলিটেকনিক শিক্ষার্থীদের ১ম থেকে ৮ম সেমিস্টার ফাইনাল পরীক্ষার রুটিন, ফরম পূরণ নির্দেশিকা এবং ডিপার্টমেন্টাল বিষয়ের হ্যান্ডনোট।"
    },

    # =========================================================================
    # TIER 4: TERTIARY & HIGHER EDUCATION (NU HONOURS, MASTERS, DEGREE, 7 COLLEGES - ALL DISCIPLINES)
    # =========================================================================
    {
        "tier": "Tier 4: Tertiary (অনার্স, মাস্টার্স, ডিগ্রি ও ৭ কলেজ)",
        "exam_name": "জাতীয় বিশ্ববিদ্যালয় অনার্স ২য় বর্ষ পরীক্ষা (সকল বিভাগ ও ইংরেজি আবশ্যিক)",
        "category": "Honours / All Subjects (NU)",
        "exam_window": "নভেম্বর - ডিসেম্বর",
        "target_month": 11,
        "lead_time_days": 40,
        "search_volume": "অত্যধিক উচ্চ (15x)",
        "target_keywords": [
            "অনার্স ২য় বর্ষ রুটিন ২০২৬",
            "অনার্স ২য় বর্ষ ইংরেজি আবশ্যিক শর্টকাট",
            "অনার্স ২য় বর্ষ হিসাববিজ্ঞান সাজেশন",
            "অনার্স ২য় বর্ষ ব্যবস্থাপনা সাজেশন",
            "অনার্স ২য় বর্ষ সমাজবিজ্ঞান হ্যান্ডনোট",
            "অনার্স ২য় বর্ষ অর্থনীতি সাজেশন",
            "অনার্স ২য় বর্ষ বাংলা ও ইংরেজি হ্যান্ডনোট"
        ],
        "content_blueprint": "জাতীয় বিশ্ববিদ্যালয়ের অনার্স ২য় বর্ষের রুটিন ও ফরম পূরণ নির্দেশিকা, বাধ্যতামূলক ইংরেজি আবশ্যিক বিষয়ের ১০০% পাস ট্রিকস এবং হিসাববিজ্ঞান, ব্যবস্থাপনা, সমাজবিজ্ঞান, অর্থনীতি, বাংলা ও রাষ্ট্রবিজ্ঞান বিভাগের সুপার শর্ট সাজেশন।"
    },
    {
        "tier": "Tier 4: Tertiary (অনার্স, মাস্টার্স, ডিগ্রি ও ৭ কলেজ)",
        "exam_name": "জাতীয় বিশ্ববিদ্যালয় মাস্টার্স শেষ পর্ব পরীক্ষা (সকল বিভাগ)",
        "category": "Masters / All Subjects (NU)",
        "exam_window": "অক্টোবর - নভেম্বর",
        "target_month": 11,
        "lead_time_days": 35,
        "search_volume": "উচ্চ (12x)",
        "target_keywords": [
            "মাস্টার্স শেষ পর্ব পরীক্ষার রুটিন ২০২৬",
            "মাস্টার্স ফাইনাল ভূরাজনীতি ও বাংলাদেশ ৩১১৯১৩",
            "মাস্টার্স সমাজবিজ্ঞান ফাইনাল সাজেশন",
            "মাস্টার্স হিসাববিজ্ঞান ফাইনাল হ্যান্ডনোট",
            "মাস্টার্স ব্যবস্থাপনা ফাইনাল সাজেশন",
            "মাস্টার্স অর্থনীতি শেষ পর্ব সাজেশন",
            "মাস্টার্স বাংলা ও ইংরেজি সাহিত্যের হ্যান্ডনোট"
        ],
        "content_blueprint": "মাস্টার্স ফাইনাল পরীক্ষার সকল বিভাগের পূর্ণাঙ্গ ক, খ ও গ বিভাগের প্রশ্ন সমাধান—সমাজবিজ্ঞান, হিসাববিজ্ঞান, ব্যবস্থাপনা, অর্থনীতি, সমাজকর্ম, বাংলা, ইংরেজি এবং রাষ্ট্রবিজ্ঞান।"
    },
    {
        "tier": "Tier 4: Tertiary (অনার্স, মাস্টার্স, ডিগ্রি ও ৭ কলেজ)",
        "exam_name": "জাতীয় বিশ্ববিদ্যালয় অনার্স ১ম বর্ষ পরীক্ষা ও স্বাধীন বাংলাদেশের অভ্যুদয়ের ইতিহাস (সকল বিভাগ)",
        "category": "Honours / Compulsory & Major",
        "exam_window": "মে - জুলাই",
        "target_month": 5,
        "lead_time_days": 60,
        "search_volume": "বিশাল (16x)",
        "target_keywords": [
            "স্বাধীন বাংলাদেশের অভ্যুদয়ের ইতিহাস ১০০% কমন সাজেশন",
            "অনার্স ১ম বর্ষ পরীক্ষার রুটিন ২০২৬",
            "অনার্স ১ম বর্ষ হিসাববিজ্ঞান নীতিমালা",
            "অনার্স ১ম বর্ষ সমাজবিজ্ঞান পরিচিতি",
            "অনার্স ১ম বর্ষ মাইক্রো ইকোনমিক্স অর্থনীতি",
            "অনার্স ১ম বর্ষ বুক লিস্ট সকল বিভাগ"
        ],
        "content_blueprint": "জাতীয় বিশ্ববিদ্যালয়ের সকল অনুষদের (কলা, সামাজিক বিজ্ঞান, ব্যবসায় শিক্ষা ও বিজ্ঞান) শিক্ষার্থীদের জন্য বাধ্যতামূলক 'স্বাধীন বাংলাদেশের অভ্যুদয়ের ইতিহাস' হ্যান্ডনোট এবং বিভাগভিত্তিক ১ম বর্ষের সম্পূর্ণ সাজেশন ও বুক লিস্ট।"
    },
    {
        "tier": "Tier 4: Tertiary (অনার্স, মাস্টার্স, ডিগ্রি ও ৭ কলেজ)",
        "exam_name": "জাতীয় বিশ্ববিদ্যালয় অনার্স ৩য় ও ৪র্থ বর্ষ ফাইনাল পরীক্ষা (সকল বিভাগ)",
        "category": "Honours / Advanced Subjects",
        "exam_window": "মার্চ - জুলাই",
        "target_month": 4,
        "lead_time_days": 60,
        "search_volume": "উচ্চ (12x)",
        "target_keywords": [
            "অনার্স ৩য় বর্ষ ফাইনাল পরীক্ষার রুটিন",
            "অনার্স ৪র্থ বর্ষ ফাইনাল সাজেশন ২০২৬",
            "অনার্স ৪র্থ বর্ষ হিসাববিজ্ঞান অডিট অ্যান্ড ট্যাক্সেশন",
            "অনার্স ৪র্থ বর্ষ থিসিস প্রজেক্ট লেখার নিয়ম",
            "অনার্স ৩য় বর্ষ ও ৪র্থ বর্ষের ফলাফল"
        ],
        "content_blueprint": "অনার্স ৩য় ও ৪র্থ বর্ষের মেজর বিষয়সমূহের অ্যাডভান্সড অধ্যায়ভিত্তিক সাজেশন, অডিট ও ফাইন্যান্সিয়াল ম্যানেজমেন্ট, সোশ্যাল রিসার্চ মেথডোলজি এবং থিসিস বা টার্ম পেপার লেখার সঠিক নিয়ম।"
    },
    {
        "tier": "Tier 4: Tertiary (অনার্স, মাস্টার্স, ডিগ্রি ও ৭ কলেজ)",
        "exam_name": "জাতীয় বিশ্ববিদ্যালয় ডিগ্রি পাস ১ম, ২য় ও ৩য় বর্ষ পরীক্ষা (বিএ, বিএসএস, বিবিএস, বিএসসি)",
        "category": "Degree / Pass Course (NU)",
        "exam_window": "সেপ্টেম্বর - নভেম্বর",
        "target_month": 10,
        "lead_time_days": 30,
        "search_volume": "উচ্চ (11x)",
        "target_keywords": [
            "জাতীয় বিশ্ববিদ্যালয় ডিগ্রি পরীক্ষার পরিবর্তিত রুটিন ২০২৬",
            "ডিগ্রি ৩য় বর্ষ রাষ্ট্রবিজ্ঞান ও সমাজবিজ্ঞান সাজেশন",
            "ডিগ্রি ১ম বর্ষ স্বাধীন বাংলাদেশের অভ্যুদয়ের ইতিহাস",
            "ডিগ্রি ২য় বর্ষ বাংলা ও ইংরেজি আবশ্যিক শর্টকাট",
            "ডিগ্রি পাস কোর্সের সকল বিষয়ের সুপার সাজেশন"
        ],
        "content_blueprint": "ডিগ্রি পাস কোর্সের বিএ, বিএসএস, বিবিএস ও বিএসসি শাখার সকল বর্ষের পরীক্ষার রুটিন, সেন্টার লিস্ট এবং স্বাধীন বাংলাদেশের অভ্যুদয় ও আবশ্যিক ইংরেজি/বাংলা বিষয়ের সহজে পাস করার চূড়ান্ত ট্রিকস।"
    },
    {
        "tier": "Tier 4: Tertiary (অনার্স, মাস্টার্স, ডিগ্রি ও ৭ কলেজ)",
        "exam_name": "ঢাকা বিশ্ববিদ্যালয় অধিভুক্ত সরকারি ৭ কলেজ অনার্স ও মাস্টার্স পরীক্ষা (সকল বিভাগ)",
        "category": "7 Colleges / DU (All Disciplines)",
        "exam_window": "নভেম্বর - জানুয়ারি",
        "target_month": 12,
        "lead_time_days": 40,
        "search_volume": "উচ্চ (11x)",
        "target_keywords": [
            "ঢাকা বিশ্ববিদ্যালয় ৭ কলেজ পরীক্ষার রুটিন ২০২৬",
            "৭ কলেজ অনার্স হিসাববিজ্ঞান ও ফিন্যান্স সাজেশন",
            "৭ কলেজ ইংরেজি ডিপার্টমেন্ট হ্যান্ডনোট",
            "সরকারি সাত কলেজ সমাজবিজ্ঞান ও অর্থনীতি নোট",
            "৭ কলেজ মাস্টার্স পরীক্ষার ফলাফল ও সিট প্ল্যান"
        ],
        "content_blueprint": "ঢাবি অধিভুক্ত ঢাকা কলেজ, ইডেন মহিলা কলেজ, কবি নজরুল, শহীদ সোহরাওয়ার্দী, বেগম বদরুন্নেসা, মিরপুর বাঙলা কলেজ ও তিতুমীর কলেজের সকল বিষয়ের অনার্স ও মাস্টার্স সেমিস্টার রুটিন, ইনকোর্স প্রশ্ন ও সিলেবাস সমাধান।"
    },

    # =========================================================================
    # TIER 5: UNIVERSITY ADMISSION TESTS (PUBLIC UNIVERSITIES)
    # =========================================================================
    {
        "tier": "Tier 5: University Admission (বিশ্ববিদ্যালয় ভর্তি)",
        "exam_name": "ঢাকা বিশ্ববিদ্যালয় (ঢাবি) ভর্তি পরীক্ষা (ক, খ, গ ইউনিট)",
        "category": "University Admission / DU",
        "exam_window": "জানুয়ারি - ফেব্রুয়ারি",
        "target_month": 1,
        "lead_time_days": 60,
        "search_volume": "সর্বোচ্চ (19x)",
        "target_keywords": [
            "ঢাকা বিশ্ববিদ্যালয় ভর্তি আবেদন ২০২৬",
            "ঢাবি খ ইউনিট কলা ও সামাজিক বিজ্ঞান প্রস্তুতি",
            "ঢাবি ক ইউনিট বিজ্ঞান কাটমার্কস",
            "ঢাবি ভর্তি পরীক্ষার মানবণ্টন ও নেগেটিভ মার্কিং"
        ],
        "content_blueprint": "ঢাকা বিশ্ববিদ্যালয়ের কলা, বিজ্ঞান ও ব্যবসায় অনুষদের বিগত ১০ বছরের প্রশ্ন সমাধান, রিটেন পার্ট ট্রিকস এবং কাটমার্কস অ্যানালাইসিস।"
    },
    {
        "tier": "Tier 5: University Admission (বিশ্ববিদ্যালয় ভর্তি)",
        "exam_name": "মেডিকেল (MBBS) ও ডেন্টাল (BDS) ভর্তি পরীক্ষা",
        "category": "Medical Admission",
        "exam_window": "জানুয়ারি - ফেব্রুয়ারি",
        "target_month": 1,
        "lead_time_days": 60,
        "search_volume": "সর্বোচ্চ (18x)",
        "target_keywords": [
            "মেডিকেল ভর্তি পরীক্ষা আবেদন যোগ্যতা ২০২৬",
            "এমবিবিএস ভর্তি পরীক্ষার তারিখ ও সিলেবাস",
            "মেডিকেল প্রশ্ন ব্যাংক সমাধান",
            "মেডিকেল ভর্তি কাটমার্কস ও জেলা কোটা"
        ],
        "content_blueprint": "মেডিকেল ভর্তি পরীক্ষার ১০০ নম্বরের এমসিকিউ মানবণ্টন, জিকে ও ইংরেজির স্পেশাল শর্টকাট নোট এবং সরকারি মেডিকেলের আসন সংখ্যা।"
    },
    {
        "tier": "Tier 5: University Admission (বিশ্ববিদ্যালয় ভর্তি)",
        "exam_name": "বুয়েট ও ইঞ্জিনিয়ারিং গুচ্ছ (চুয়েট, কুয়েট, রুয়েট) ভর্তি পরীক্ষা",
        "category": "Engineering Admission",
        "exam_window": "ফেব্রুয়ারি - মার্চ",
        "target_month": 2,
        "lead_time_days": 70,
        "search_volume": "উচ্চ (14x)",
        "target_keywords": [
            "বুয়েট প্রাক-নির্বাচনী ও মূল লিখিত পরীক্ষা তারিখ",
            "ইঞ্জিনিয়ারিং গুচ্ছ ভর্তি সার্কুলার ২০২৬",
            "বুয়েট ভর্তি প্রস্তুতি ফিজিক্স কেমিস্ট্রি ম্যাথ",
            "ইঞ্জিনিয়ারিং কাটমার্কস"
        ],
        "content_blueprint": "বুয়েট ও ইঞ্জিনিয়ারিং গুচ্ছের প্রিলি ও মূল লিখিত পরীক্ষার প্রস্তুতি পরিকল্পনা, ফর্মুলা শিট এবং আবেদন যোগ্যতা।"
    },
    {
        "tier": "Tier 5: University Admission (বিশ্ববিদ্যালয় ভর্তি)",
        "exam_name": "জিএসটি (GST) সাধারণ ও বিজ্ঞান প্রযুক্তি গুচ্ছ বিশ্ববিদ্যালয় ভর্তি",
        "category": "University Admission / GST",
        "exam_window": "মার্চ - মে",
        "target_month": 4,
        "lead_time_days": 75,
        "search_volume": "বিশাল (16x)",
        "target_keywords": [
            "গুচ্ছ ভর্তি সার্কুলার ২০২৬",
            "জিএসটি ভর্তি পরীক্ষার আবেদন নিয়ম",
            "গুচ্ছ কাটমার্কস ও সাবজেক্ট চয়েস লিস্ট",
            "২৪টি সাধারণ ও বিজ্ঞান প্রযুক্তি বিশ্ববিদ্যালয় আসন"
        ],
        "content_blueprint": "জিএসটি গুচ্ছভুক্ত ২৪টি পাবলিক বিশ্ববিদ্যালয়ের এ, বি ও সি ইউনিটের আবেদন যোগ্যতা, কাটমার্কস হিসাব এবং ভর্তি নিশ্চিতকরণের নিয়ম।"
    },

    # =========================================================================
    # TIER 6: COMPETITIVE JOB EXAMS (BCS & GOVT JOBS)
    # =========================================================================
    {
        "tier": "Tier 6: Competitive Jobs (বিসিএস ও সরকারি চাকরি)",
        "exam_name": "৪৭তম ও ৪৮তম বিসিএস প্রিলিমিনারি ও লিখিত পরীক্ষা",
        "category": "Job Study / BCS",
        "exam_window": "নভেম্বর - ফেব্রুয়ারি সার্কুলার, মার্চ - মে প্রিলি",
        "target_month": 12,
        "lead_time_days": 60,
        "search_volume": "দীর্ঘস্থায়ী বিশাল (17x)",
        "target_keywords": [
            "৪৭তম বিসিএস সার্কুলার ২০২৬",
            "বিসিএস প্রিলিমিনারি ২০০ নম্বরের মানবণ্টন",
            "বিসিএস প্রস্তুতি সেরা বুক লিস্ট",
            "বিসিএস ক্যাডার চয়েস লিস্ট সাজানোর নিয়ম",
            "বিসিএস আন্তর্জাতিক ও বাংলাদেশ বিষয়াবলী"
        ],
        "content_blueprint": "বিসিএস প্রিলিমিনারির ২০০ নম্বরের সুনির্দিষ্ট বিষয়ভিত্তিক মানবণ্টন, পড়ার সঠিক রুটিন এবং প্রথমবারই প্রিলিমিনারি ক্র্যাক করার স্ট্র্যাটেজি।"
    },
    {
        "tier": "Tier 6: Competitive Jobs (বিসিএস ও সরকারি চাকরি)",
        "exam_name": "প্রাথমিক সহকারী শিক্ষক নিয়োগ পরীক্ষা (প্রাইমারি শিক্ষক)",
        "category": "Job Study / Primary",
        "exam_window": "নভেম্বর - জানুয়ারি",
        "target_month": 12,
        "lead_time_days": 45,
        "search_volume": "বিশাল (15x)",
        "target_keywords": [
            "প্রাথমিক শিক্ষক নিয়োগ পরীক্ষার তারিখ",
            "প্রাইমারি শিক্ষক নিয়োগ সাজেশন ও মানবণ্টন",
            "প্রাইমারি বিগত ১০ বছরের প্রশ্ন সমাধান",
            "প্রাইমারি শিক্ষক নিয়োগ ভাইভা প্রস্তুতি"
        ],
        "content_blueprint": "প্রাথমিক সহকারী শিক্ষক নিয়োগের ৮০ নম্বরের লিখিত পরীক্ষা ও ২০ নম্বরের ভাইভা প্রস্তুতি, গণিত ও ইংরেজির শর্টকাট টেকনিক।"
    },
    {
        "tier": "Tier 6: Competitive Jobs (বিসিএস ও সরকারি চাকরি)",
        "exam_name": "এনটিআরসিএ (NTRCA) বেসরকারি শিক্ষক নিবন্ধন প্রিলিমিনারি ও লিখিত",
        "category": "Job Study / NTRCA",
        "exam_window": "জানুয়ারি - মার্চ",
        "target_month": 2,
        "lead_time_days": 60,
        "search_volume": "উচ্চ (13x)",
        "target_keywords": [
            "১৯তম শিক্ষক নিবন্ধন সার্কুলার",
            "এনটিআরসিএ প্রিলিমিনারি ১০০ নম্বরের পাস মার্কস",
            "শিক্ষক নিবন্ধন স্কুল ও কলেজ পর্যায় সাজেশন",
            "NTRCA লিখিত পরীক্ষার সিলেবাস"
        ],
        "content_blueprint": "এনটিআরসিএ শিক্ষক নিবন্ধনের স্কুল, স্কুল-২ ও কলেজ পর্যায়ের প্রিলিমিনারি পরীক্ষার সিলেবাস, পাস মার্কস অর্জন ও লিখিত বিষয়ের নোট।"
    },
    {
        "tier": "Tier 6: Competitive Jobs (বিসিএস ও সরকারি চাকরি)",
        "exam_name": "সমন্বিত সরকারি ৯ ব্যাংক অফিসার ও সিনিয়র অফিসার নিয়োগ পরীক্ষা",
        "category": "Job Study / Bank",
        "exam_window": "ডিসেম্বর - মার্চ",
        "target_month": 1,
        "lead_time_days": 50,
        "search_volume": "উচ্চ (12x)",
        "target_keywords": [
            "সমন্বিত ব্যাংক নিয়োগ পরীক্ষার তারিখ",
            "বাংলাদেশ ব্যাংক অফিসার ক্যাশ প্রিলি প্রস্তুতি",
            "কম্বাইন্ড ব্যাংক ম্যাথ ও ইংলিশ শর্টকাট",
            "ব্যাংক লিখিত অনুবাদ ও ফোকাস রাইটিং"
        ],
        "content_blueprint": "বাংলাদেশ ব্যাংকের ব্যাংকার্স সিলেকশন কমিটির অধীনে সমন্বিত ব্যাংক অফিসার নিয়োগের ১০০ নম্বরের প্রিলিমিনারি ও ২০০ নম্বরের লিখিত পরীক্ষার গাইডলাইন।"
    }
]

ALL_TIER_NEWS_QUERIES = [
    # Primary
    "প্রাথমিক বৃত্তি পরীক্ষা",
    "প্রাথমিক বার্ষিক পরীক্ষা",
    # Secondary
    "৬ষ্ঠ ৭ম ৮ম ৯ম বার্ষিক পরীক্ষা",
    "এসএসসি পরীক্ষা ২০২৬",
    "দাখিল পরীক্ষা রুটিন",
    # Higher Secondary
    "এইচএসসি পরীক্ষা রুটিন ২০২৬",
    "কারিগরি শিক্ষা বোর্ড ডিপ্লোমা",
    # University
    "জাতীয় বিশ্ববিদ্যালয় নোটিশ",
    "অনার্স দ্বিতীয় বর্ষের পরীক্ষার রুটিন",
    "মাস্টার্স শেষ পর্ব পরীক্ষা",
    "ঢাকা বিশ্ববিদ্যালয় ৭ কলেজ রুটিন",
    # Admissions
    "বিশ্ববিদ্যালয় ভর্তি সার্কুলার ২০২৬",
    "মেডিকেল ভর্তি পরীক্ষা ২০২৬",
    "বুয়েট ভর্তি পরীক্ষা",
    "গুচ্ছ ভর্তি পরীক্ষা",
    # Jobs
    "বিসিএস সার্কুলার পরীক্ষা",
    "প্রাথমিক শিক্ষক নিয়োগ পরীক্ষা",
    "শিক্ষক নিবন্ধন NTRCA নোটিশ",
    "ব্যাংক নিয়োগ পরীক্ষা রুটিন"
]


def fetch_all_tier_live_notices() -> list[dict]:
    """Fetches real-time educational notices and news across all tiers from Google News BD RSS."""
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    live_notices = []
    seen_titles = set()

    for q in ALL_TIER_NEWS_QUERIES:
        url = f"https://news.google.com/rss/search?q={urllib.parse.quote(q)}&hl=bn&gl=BD&ceid=BD:bn"
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=6) as resp:
                root = ET.fromstring(resp.read())
                items = root.findall("./channel/item")
                for item in items[:2]:
                    title_elem = item.find("title")
                    pub_elem = item.find("pubDate")
                    link_elem = item.find("link")
                    if title_elem is not None and title_elem.text:
                        title = title_elem.text.strip()
                        if title not in seen_titles:
                            seen_titles.add(title)
                            live_notices.append({
                                "source": f"জাতীয় শিক্ষাবার্তা ও গুগল নিউজ ({q})",
                                "portal_url": "https://news.google.com/",
                                "title": title,
                                "pub_date": pub_elem.text.strip() if pub_elem is not None else "",
                                "link": link_elem.text.strip() if link_elem is not None else "",
                                "pdf_url": "",
                                "query": q
                            })
        except Exception:
            pass

    return live_notices[:15]


def load_live_posts_titles() -> list[str]:
    """Loads existing live post titles from Helptrickbd repository."""
    if not os.path.exists(LIVE_POSTS_PATH):
        return []
    try:
        with open(LIVE_POSTS_PATH, "r", encoding="utf-8") as f:
            posts = json.load(f)
            return [p.get("title", "") for p in posts]
    except Exception:
        return []


def evaluate_360_degree_radar(current_month: int, filter_tier: str = None) -> list[dict]:
    """Evaluates all educational tiers and ranks by 30-45 day SEO golden window urgency."""
    radar_results = []
    live_titles = load_live_posts_titles()

    for item in BD_COMPREHENSIVE_RADAR_CALENDAR:
        if filter_tier and filter_tier.lower() not in item["tier"].lower():
            continue

        target_m = item["target_month"]
        diff_months = (target_m - current_month) % 12

        if diff_months == 0:
            status = "URGENT (গোল্ডেন উইন্ডো — চলতি মাসে পরীক্ষা/সার্কুলার)"
            urgency_score = 1
            reason = "পরীক্ষা বা সার্কুলার ১ মাসের ভেতরেই। গুগলে প্রথম পাতায় র‍্যাংক পাওয়ার জন্য এখনই পোস্ট করার মোক্ষম সময়।"
        elif diff_months == 1:
            status = "IDEAL TIMING (আদর্শ গোল্ডেন উইন্ডো — পরবর্তী ৩০ দিনের টার্গেট)"
            urgency_score = 2
            reason = "পরীক্ষার ৩০-৬০ দিন পূর্বে পোস্ট করলে পরীক্ষার দিন সার্চ ভলিউম বাড়ামাত্র গুগল ১ নম্বর পজিশন দিয়ে দেবে।"
        elif diff_months == 2:
            status = "EARLY PREPARATION (আগাম প্রস্তুতি — পরবর্তী ৬০ দিনের সুযোগ)"
            urgency_score = 3
            reason = "৬০-৯০ দিন পূর্বে ব্যাকলিংক, পিলার পোস্ট ও ইন্টারনাল লিংকের স্ট্রাকচার রেডি করার সময়।"
        else:
            status = "LONG-TERM / OFF-SEASON (পরবর্তী মৌসুমের জন্য সংরক্ষিত)"
            urgency_score = 4
            reason = "পরীক্ষা বা সেশনের সময় হতে এখনো ৩ মাসের বেশি বাকি।"

        # Check coverage in live posts
        has_coverage = False
        matching_titles = []
        for kw in item["target_keywords"]:
            for t in live_titles:
                first_word = kw.split()[0]
                if first_word.lower() in t.lower():
                    has_coverage = True
                    matching_titles.append(t)
                    break
            if has_coverage:
                break

        radar_results.append({
            "tier": item["tier"],
            "exam_name": item["exam_name"],
            "category": item["category"],
            "exam_window": item["exam_window"],
            "status": status,
            "urgency_score": urgency_score,
            "reason": reason,
            "search_volume": item["search_volume"],
            "target_keywords": item["target_keywords"],
            "content_blueprint": item["content_blueprint"],
            "has_coverage": has_coverage,
            "matching_titles": matching_titles[:2]
        })

    radar_results.sort(key=lambda x: x["urgency_score"])
    return radar_results


def generate_360_master_report(radar_results: list[dict], live_notices: list[dict], current_date: datetime) -> str:
    """Generates an all-inclusive master radar markdown report."""
    lines = []
    lines.append("# বাংলাদেশ ৩৬০-ডিগ্রি অল-ক্লাস ও ক্যারিয়ার এসইও রাডার রিপোর্ট")
    lines.append(f"**তারিখ:** {current_date.strftime('%Y-%m-%d')} | **চলতি মাস:** {current_date.strftime('%B %Y')}")
    lines.append("**কভারেজ:** ক্লাস ১ থেকে মাস্টার্স, বিশ্ববিদ্যালয় ভর্তি, বিসিএস ও সকল সরকারি চাকরি পরীক্ষা।\n")

    lines.append("## ১. এসইও গোল্ডেন উইন্ডোর মূল নীতি (কেন ১-২ মাস আগেই পোস্ট করতে হয়?)")
    lines.append("- **গুগল ট্রাস্ট ইনকিউবেশন পিরিয়ড:** গুগলে একটি আর্টিকেলের কোয়ালিটি যাচাই, ক্রলিং এবং সার্চ ইম্প্রেশন তৈরি হতে ন্যূনতম ২১ থেকে ৩০ দিন সময় লাগে।")
    lines.append("- **দেরিতে পোস্ট করার চরম ব্যর্থতা:** পরীক্ষার ২-৩ দিন আগে পোস্ট করলে সেই পোস্ট কখনো ১ নম্বরে র‍্যাংক পায় না; ট্রাফিক চলে যায় পুরনো প্রতিযোগীদের সাইটে।")
    lines.append("- **আর্লি-মুভার স্ট্র্যাটেজি:** পরীক্ষার ৩০ থেকে ৪৫ দিন পূর্বে পোস্ট পাবলিশ করে রাখলে পরীক্ষার দিন যখন লক্ষ লক্ষ পরীক্ষার্থী অনলাইনে সার্চ করে, তখন আমাদের পোস্ট স্বয়ংক্রিয়ভাবে গুগলের ১ নম্বরে চলে আসে।\n")

    lines.append("## ২. চলতি মাসের তাৎক্ষণিক গোল্ডেন উইন্ডো তালিকা (Urgent Action Items)")
    lines.append("| ধাপ | পরীক্ষার নাম | পরীক্ষার সময়কাল | সার্চ ভলিউম | আমাদের সাইটে আছে কি? | অ্যাকশন প্ল্যান |")
    lines.append("| :--- | :--- | :--- | :--- | :--- | :--- |")

    for r in radar_results:
        if r["urgency_score"] <= 2:
            cov = "হ্যাঁ (আপডেট)" if r["has_coverage"] else "না (জরুরি নতুন পোস্ট)"
            lines.append(f"| **{r['tier'].split(':')[0]}** | **{r['exam_name']}** | {r['exam_window']} | {r['search_volume']} | `{cov}` | {r['content_blueprint'][:65]}... |")

    lines.append("\n## ৩. স্তরভিত্তিক বিস্তারিত কনটেন্ট গাইডলাইন ও টার্গেট কি-ওয়ার্ডস\n")
    current_tier = ""
    for r in radar_results:
        if r["urgency_score"] <= 3:
            if r["tier"] != current_tier:
                current_tier = r["tier"]
                lines.append(f"### {current_tier}\n")

            lines.append(f"#### {r['exam_name']}")
            lines.append(f"- **স্ট্যাটাস:** {r['status']}")
            lines.append(f"- **সম্ভাব্য সময়কাল:** {r['exam_window']}")
            lines.append(f"- **কেন এখনই লিখতে হবে:** {r['reason']}")
            lines.append(f"- **টার্গেট কি-ওয়ার্ডস:** `{', '.join(r['target_keywords'])}`")
            lines.append(f"- **কনটেন্ট ব্লুপ্রিন্ট:** {r['content_blueprint']}")
            if r["has_coverage"]:
                lines.append(f"- **সাইটে বিদ্যমান সংশ্লিষ্ট পোস্ট:** {r['matching_titles']}")
            else:
                lines.append("- **কনটেন্ট গ্যাপ:** সাইটে এই বিষয়ের ওপর এখনও কোনো পূর্ণাঙ্গ পোস্ট নেই। দ্রুত পোস্ট লেখা প্রয়োজন।")
            lines.append("")

    if live_notices:
        lines.append("## ৪. লাইভ এডুকেশন বোর্ড ও এক্সাম নোটিশ ট্র্যাকার (আজকের সর্বশেষ সংবাদ)")
        lines.append("গুগল নিউজ ও বাংলাদেশ শিক্ষা পোর্টাল থেকে রিয়েল-টাইমে সংগৃহীত নোটিশ:")
        for idx, n in enumerate(live_notices, 1):
            lines.append(f"{idx}. **{n['title']}** (প্রকাশকাল: {n['pub_date'][:16]})")
        lines.append("")

    lines.append("## ৫. হেল্পট্রিকবিডির জন্য অগ্রাধিকারভিত্তিক সাপ্তাহিক পাবলিশিং রোডম্যাপ")
    lines.append("1. **জাতীয় বিশ্ববিদ্যালয় (অনার্স ২য় বর্ষ ও মাস্টার্স):** অনার্স ২য় বর্ষ পরীক্ষার রুটিন, ফরম পূরণ গাইড ও রাষ্ট্রবিজ্ঞান হ্যান্ডনোট (নভেম্বর পরীক্ষার প্রস্তুতি)।")
    lines.append("2. **মাধ্যমিক ও স্কুল (এসএসসি ও ক্লাস ৬-৯):** এসএসসি টেস্ট পরীক্ষার বাংলা ও ইংরেজি মডেল টেস্ট এবং ৬ষ্ঠ-৯ম শ্রেণির বার্ষিক পরীক্ষার সুপার সাজেশন।")
    lines.append("3. **বিশ্ববিদ্যালয় ভর্তি (ঢাবি, মেডিকেল, গুচ্ছ):** সকল পাবলিক বিশ্ববিদ্যালয়ের সার্কুলার, ইউনিটভিত্তিক যোগ্যতা ও বিগত বছরের কাটমার্কস।")
    lines.append("4. **চাকরি ও বিসিএস:** ৪৭তম বিসিএস প্রিলিমিনারি ২০০ নম্বরের মানবণ্টন এবং প্রাথমিক সহকারী শিক্ষক নিয়োগ পরীক্ষার বিগত ১০ বছরের প্রশ্ন ব্যাংক।")
    lines.append("5. **প্রাথমিক শিক্ষা (Class 1-5):** ৫ম শ্রেণির প্রাথমিক বৃত্তি পরীক্ষার ১০০ নম্বরের চূড়ান্ত মডেল টেস্ট ও বার্ষিক পরীক্ষার রুটিন।")

    report_text = "\n".join(lines)
    with open(OUTPUT_REPORT, "w", encoding="utf-8") as f:
        f.write(report_text)
    return report_text


def main():
    parser = argparse.ArgumentParser(description="Master 360-Degree Bangladesh Exam Early-Warning & SEO Radar Engine")
    parser.add_argument("--month", type=int, help="Target month (1-12, default: current month)")
    parser.add_argument("--tier", type=str, help="Filter by tier (e.g. primary, school, college, honours, admission, bcs)")
    args = parser.parse_args()

    now = datetime.now()
    cur_month = args.month if args.month else now.month

    print("=" * 72)
    print("  HELPTRICKBD 360-DEGREE BANGLADESH EXAM & CAREER RADAR ENGINE")
    print("=" * 72)
    print(f"[*] চলতি তারিখ: {now.strftime('%Y-%m-%d')} (মাস: {cur_month})")

    print("[*] ক্লাস ১ থেকে মাস্টার্স, বিসিএস ও চাকরির লাইভ নোটিশ ট্র্যাক করা হচ্ছে...")
    live_notices = fetch_all_tier_live_notices()
    print(f"[OK] {len(live_notices)}টি লাইভ নোটিশ সফলভাবে সংগ্রহ করা হয়েছে।")

    print("[*] ৩৬০-ডিগ্রি অল-ক্লাস এসইও গোল্ডেন উইন্ডো ক্যালকুলেশন সম্পন্ন হচ্ছে...")
    radar_results = evaluate_360_degree_radar(cur_month, filter_tier=args.tier)

    urgent_count = sum(1 for r in radar_results if r["urgency_score"] <= 2)
    print(f"[OK] মোট {urgent_count}টি পরীক্ষা বর্তমানে ৩০-৪৫ দিনের এসইও গোল্ডেন উইন্ডোতে রয়েছে।")

    print(f"[*] রিপোর্ট তৈরি ও সেভ করা হচ্ছে: {OUTPUT_REPORT}")
    generate_360_master_report(radar_results, live_notices, now)
    print("[SUCCESS] ৩৬০-ডিগ্রি এক্সাম রাডার রিপোর্ট সফলভাবে জেনারেট হয়েছে!")
    print("=" * 72)


if __name__ == "__main__":
    main()
