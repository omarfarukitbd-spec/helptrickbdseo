#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
output_posts/generate_nu_honours_2nd_year_routine_post.py
----------------------------------------------------------
Generates the authoritative master article for:
জাতীয় বিশ্ববিদ্যালয় অনার্স ২য় বর্ষ পরীক্ষার রুটিন ২০২৬ (সকল বিভাগ) | NU Honours 2nd Year Exam Routine & Subject Code.

Features:
- Comprehensive coverage of ALL 18 major departments across 4 faculties.
- English search keyword first in headings, followed by Bengali (Rule 08/User Instruction).
- Subject-specific alt and title tags on every routine card figure.
- Byte-0 Hero banner before <!--more--> tag.
- Position-0 Quick Summary Box.
- Compulsory English (Code: 221109) passing guidelines & subject codes.
- Schema.org BlogPosting & FAQPage JSON-LD microdata.
- Strictly ZERO EMOJIS!
"""

import os
import sys
import json

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUTPUT_HTML = os.path.join(PROJECT_ROOT, "output_posts", "nu-honours-2nd-year-exam-routine-2026.html")
OUTPUT_META = os.path.join(PROJECT_ROOT, "output_posts", "nu-honours-2nd-year-exam-routine-2026_meta.json")

CDN_BASE = "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts"

HERO_BANNER = f"{CDN_BASE}/nu_honours_2nd_year_routine_2026.webp"

DEPT_DATA = [
    # Business Studies
    {
        "slug": "management",
        "en_name": "Management",
        "bn_name": "ব্যবস্থাপনা",
        "faculty": "ব্যবসায় শিক্ষা অনুষদ",
        "h2_heading": "NU Honours 2nd Year Management Exam Routine 2026 | অনার্স ২য় বর্ষ ব্যবস্থাপনা বিভাগের পরীক্ষার রুটিন ও বিষয়কোড",
        "img_alt": "NU Honours 2nd Year Management Exam Routine 2026 Subject Code Routine Card",
        "img_title": "NU Honours 2nd Year Management Routine 2026 National University",
        "fig_caption": "ব্যবস্থাপনা বিভাগ: অনার্স ২য় বর্ষ পরীক্ষার বিষয়ভিত্তিক রুটিন ও বিষয়কোড ২০২৬",
        "papers": [
            ("২৮/০৯/২০২৬ (সোমবার)", "221109", "English (Compulsory) — Non-Credit", "আবশ্যিক পাস বিষয়"),
            ("০১/১০/২০২৬ (বৃহস্পতিবার)", "222601", "Human Resource Management", "তত্ত্বীয় মূল পত্র"),
            ("০৭/১০/২০২৬ (বুধবার)", "222603", "Business Communication (In English)", "লিখিত পত্র"),
            ("১২/১০/২০২৬ (সোমবার)", "222605", "Business Mathematics", "গাণিতিক পত্র"),
            ("১৯/১০/২০২৬ (সোমবার)", "222607", "Principles of Finance", "তত্ত্বীয় ও গাণিতিক"),
            ("২৬/১০/২০২৬ (সোমবার)", "222609", "Legal Aspects of Business", "বাণিজ্যিক আইন"),
        ]
    },
    {
        "slug": "accounting",
        "en_name": "Accounting",
        "bn_name": "হিসাববিজ্ঞান",
        "faculty": "ব্যবসায় শিক্ষা অনুষদ",
        "h2_heading": "NU Honours 2nd Year Accounting Exam Routine 2026 | অনার্স ২য় বর্ষ হিসাববিজ্ঞান পরীক্ষার রুটিন ও বিষয়কোড",
        "img_alt": "NU Honours 2nd Year Accounting Exam Routine 2026 Subject Code Routine Card",
        "img_title": "NU Honours 2nd Year Accounting Routine 2026 National University",
        "fig_caption": "হিসাববিজ্ঞান বিভাগ: অনার্স ২য় বর্ষ পরীক্ষার বিষয়ভিত্তিক রুটিন ও বিষয়কোড ২০২৬",
        "papers": [
            ("২৮/০৯/২০২৬ (সোমবার)", "221109", "English (Compulsory) — Non-Credit", "আবশ্যিক পাস বিষয়"),
            ("০১/১০/২০২৬ (বৃহস্পতিবার)", "222501", "Advanced Accounting-I", "প্রধান হিসাববিজ্ঞান পত্র"),
            ("০৭/১০/২০২৬ (বুধবার)", "222503", "Business Communication and Report Writing", "ইংরেজি ও প্রতিবেদন"),
            ("১২/১০/২০২৬ (সোমবার)", "222505", "Business Mathematics", "বাণিজ্যিক গণিত"),
            ("১৯/১০/২০২৬ (সোমবার)", "222507", "Taxation in Bangladesh", "আয়কর ও ভ্যাট আইন"),
            ("২৬/১০/২০২৬ (সোমবার)", "222509", "Principles of Finance", "আর্থিক ব্যবস্থাপনা মূলনীতি"),
        ]
    },
    {
        "slug": "marketing",
        "en_name": "Marketing",
        "bn_name": "মার্কেটিং",
        "faculty": "ব্যবসায় শিক্ষা অনুষদ",
        "h2_heading": "NU Honours 2nd Year Marketing Exam Routine 2026 | অনার্স ২য় বর্ষ মার্কেটিং পরীক্ষার রুটিন ও বিষয়কোড",
        "img_alt": "NU Honours 2nd Year Marketing Exam Routine 2026 Subject Code Routine Card",
        "img_title": "NU Honours 2nd Year Marketing Routine 2026 National University",
        "fig_caption": "মার্কেটিং বিভাগ: অনার্স ২য় বর্ষ পরীক্ষার বিষয়ভিত্তিক রুটিন ও বিষয়কোড ২০২৬",
        "papers": [
            ("২৮/০৯/২০২৬ (সোমবার)", "221109", "English (Compulsory) — Non-Credit", "আবশ্যিক পাস বিষয়"),
            ("০১/১০/২০২৬ (বৃহস্পতিবার)", "222301", "Consumer Behavior", "ভোক্তা আচরণ তত্ত্ব"),
            ("০৭/১০/২০২৬ (বুধবার)", "222303", "Principles of Finance", "আর্থিক মূলনীতি"),
            ("১২/১০/২০২৬ (সোমবার)", "222305", "Business Communication (In English)", "বাণিজ্যিক যোগাযোগ"),
            ("১৯/১০/২০২৬ (সোমবার)", "222307", "Business Statistics", "পরিসংখ্যান পত্র"),
            ("২৬/১০/২০২৬ (সোমবার)", "222309", "Macro Economics", "সামষ্টিক অর্থনীতি"),
        ]
    },
    {
        "slug": "finance",
        "en_name": "Finance & Banking",
        "bn_name": "ফিন্যান্স ও ব্যাংকিং",
        "faculty": "ব্যবসায় শিক্ষা অনুষদ",
        "h2_heading": "NU Honours 2nd Year Finance Exam Routine 2026 | অনার্স ২য় বর্ষ ফিন্যান্স ও ব্যাংকিং পরীক্ষার রুটিন ও বিষয়কোড",
        "img_alt": "NU Honours 2nd Year Finance and Banking Exam Routine 2026 Subject Code Routine Card",
        "img_title": "NU Honours 2nd Year Finance Routine 2026 National University",
        "fig_caption": "ফিন্যান্স ও ব্যাংকিং বিভাগ: অনার্স ২য় বর্ষ পরীক্ষার বিষয়ভিত্তিক রুটিন ও বিষয়কোড ২০২৬",
        "papers": [
            ("২৮/০৯/২০২৬ (সোমবার)", "221109", "English (Compulsory) — Non-Credit", "আবশ্যিক পাস বিষয়"),
            ("০১/১০/২০২৬ (বৃহস্পতিবার)", "222401", "Commercial Banking", "বাণিজ্যিক ব্যাংকিং মূলনীতি"),
            ("০৭/১০/২০২৬ (বুধবার)", "222403", "Financial Management", "আর্থিক ব্যবস্থাপনা পত্র"),
            ("১২/১০/২০২৬ (সোমবার)", "222405", "Business Communication", "বাণিজ্যিক যোগাযোগ"),
            ("১৯/১০/২০২৬ (সোমবার)", "222407", "Business Mathematics", "বাণিজ্যিক গণিত"),
            ("২৬/১০/২০২৬ (সোমবার)", "222409", "Auditing", "নিরীক্ষা শাস্ত্র"),
        ]
    },

    # Social Science
    {
        "slug": "political_science",
        "en_name": "Political Science",
        "bn_name": "রাষ্ট্রবিজ্ঞান",
        "faculty": "সামাজিক বিজ্ঞান অনুষদ",
        "h2_heading": "NU Honours 2nd Year Political Science Exam Routine 2026 | অনার্স ২য় বর্ষ রাষ্ট্রবিজ্ঞান পরীক্ষার রুটিন ও বিষয়কোড",
        "img_alt": "NU Honours 2nd Year Political Science Exam Routine 2026 Subject Code Routine Card",
        "img_title": "NU Honours 2nd Year Political Science Routine 2026 National University",
        "fig_caption": "রাষ্ট্রবিজ্ঞান বিভাগ: অনার্স ২য় বর্ষ পরীক্ষার বিষয়ভিত্তিক রুটিন ও বিষয়কোড ২০২৬",
        "papers": [
            ("২৮/০৯/২০২৬ (সোমবার)", "221109", "English (Compulsory) — Non-Credit", "আবশ্যিক পাস বিষয়"),
            ("০১/১০/২০২৬ (বৃহস্পতিবার)", "221901", "বৃটিশ ভারতের রাজনৈতিক ও সাংবিধানিক উন্নয়ন (১৭৫৭-১৯৪৭)", "ঐতিহাসিক সাংবিধানিক পত্র"),
            ("০৭/১০/২০২৬ (বুধবার)", "221903", "রাজনৈতিক সমাজবিজ্ঞান (Political Sociology)", "তত্ত্বীয় মূল পত্র"),
            ("১২/১০/২০২৬ (সোমবার)", "221905", "পূর্ব এশিয়ার সরকার ও রাজনীতি (চীন ও জাপান)", "আন্তর্জাতিক রাজনীতি"),
            ("১৯/১০/২০২৬ (সোমবার)", "221907", "দক্ষিণ এশিয়ার সরকার ও রাজনীতি (ভারত, পাকিস্তান ও শ্রীলঙ্কা)", "আঞ্চলিক সরকার ও রাজনীতি"),
        ]
    },
    {
        "slug": "sociology",
        "en_name": "Sociology",
        "bn_name": "সমাজবিজ্ঞান",
        "faculty": "সামাজিক বিজ্ঞান অনুষদ",
        "h2_heading": "NU Honours 2nd Year Sociology Exam Routine 2026 | অনার্স ২য় বর্ষ সমাজবিজ্ঞান পরীক্ষার রুটিন ও বিষয়কোড",
        "img_alt": "NU Honours 2nd Year Sociology Exam Routine 2026 Subject Code Routine Card",
        "img_title": "NU Honours 2nd Year Sociology Routine 2026 National University",
        "fig_caption": "সমাজবিজ্ঞান বিভাগ: অনার্স ২য় বর্ষ পরীক্ষার বিষয়ভিত্তিক রুটিন ও বিষয়কোড ২০২৬",
        "papers": [
            ("২৮/০৯/২০২৬ (সোমবার)", "221109", "English (Compulsory) — Non-Credit", "আবশ্যিক পাস বিষয়"),
            ("০১/১০/২০২৬ (বৃহস্পতিবার)", "222001", "Classical Sociological Theory", "চিরায়ত সমাজতাত্ত্বিক তত্ত্ব"),
            ("০৭/১০/২০২৬ (বুধবার)", "222003", "Social Structure of Bangladesh", "বাংলাদেশের সমাজ কাঠামো"),
            ("১২/১০/২০২৬ (সোমবার)", "222005", "Bangladesh Society and Culture", "বাংলাদেশের সমাজ ও সংস্কৃতি"),
            ("১৯/১০/২০২৬ (সোমবার)", "222007", "Social Psychology", "সামাজিক মনোবিজ্ঞান"),
        ]
    },
    {
        "slug": "social_work",
        "en_name": "Social Work",
        "bn_name": "সমাজকর্ম",
        "faculty": "সামাজিক বিজ্ঞান অনুষদ",
        "h2_heading": "NU Honours 2nd Year Social Work Exam Routine 2026 | অনার্স ২য় বর্ষ সমাজকর্ম পরীক্ষার রুটিন ও বিষয়কোড",
        "img_alt": "NU Honours 2nd Year Social Work Exam Routine 2026 Subject Code Routine Card",
        "img_title": "NU Honours 2nd Year Social Work Routine 2026 National University",
        "fig_caption": "সমাজকর্ম বিভাগ: অনার্স ২য় বর্ষ পরীক্ষার বিষয়ভিত্তিক রুটিন ও বিষয়কোড ২০২৬",
        "papers": [
            ("২৮/০৯/২০২৬ (সোমবার)", "221109", "English (Compulsory) — Non-Credit", "আবশ্যিক পাস বিষয়"),
            ("০১/১০/২০২৬ (বৃহস্পতিবার)", "222101", "Human Rights and Social Justice", "মানবাধিকার ও সামাজিক ন্যায়বিচার"),
            ("০৭/১০/২০২৬ (বুধবার)", "222103", "Social Problems of Bangladesh", "বাংলাদেশের সামাজিক সমস্যাবলি"),
            ("১২/১০/২০২৬ (সোমবার)", "222105", "Social Policy and Planning", "সামাজিক নীতি ও পরিকল্পনা"),
            ("১৯/১০/২০২৬ (সোমবার)", "222107", "Social Research and Statistics", "সমাজ গবেষণা ও পরিসংখ্যান"),
        ]
    },
    {
        "slug": "economics",
        "en_name": "Economics",
        "bn_name": "অর্থনীতি",
        "faculty": "সামাজিক বিজ্ঞান অনুষদ",
        "h2_heading": "NU Honours 2nd Year Economics Exam Routine 2026 | অনার্স ২য় বর্ষ অর্থনীতি পরীক্ষার রুটিন ও বিষয়কোড",
        "img_alt": "NU Honours 2nd Year Economics Exam Routine 2026 Subject Code Routine Card",
        "img_title": "NU Honours 2nd Year Economics Routine 2026 National University",
        "fig_caption": "অর্থনীতি বিভাগ: অনার্স ২য় বর্ষ পরীক্ষার বিষয়ভিত্তিক রুটিন ও বিষয়কোড ২০২৬",
        "papers": [
            ("২৮/০৯/২০২৬ (সোমবার)", "221109", "English (Compulsory) — Non-Credit", "আবশ্যিক পাস বিষয়"),
            ("০১/১০/২০২৬ (বৃহস্পতিবার)", "222201", "Intermediate Microeconomics", "মধ্যবর্তী ব্যাষ্টিক অর্থনীতি"),
            ("০৭/১০/২০২৬ (বুধবার)", "222203", "Mathematical Economics", "গাণিতিক অর্থনীতি"),
            ("১২/১০/২০২৬ (সোমবার)", "222205", "Basic Econometrics", "মৌলিক ইকোনোমেট্রিক্স"),
            ("১৯/১০/২০২৬ (সোমবার)", "222207", "Agricultural Economics", "কৃষি অর্থনীতি"),
        ]
    },

    # Arts
    {
        "slug": "bangla",
        "en_name": "Bangla",
        "bn_name": "বাংলা",
        "faculty": "কলা অনুষদ",
        "h2_heading": "NU Honours 2nd Year Bangla Exam Routine 2026 | অনার্স ২য় বর্ষ বাংলা বিভাগের পরীক্ষার রুটিন ও বিষয়কোড",
        "img_alt": "NU Honours 2nd Year Bangla Exam Routine 2026 Subject Code Routine Card",
        "img_title": "NU Honours 2nd Year Bangla Routine 2026 National University",
        "fig_caption": "বাংলা বিভাগ: অনার্স ২য় বর্ষ পরীক্ষার বিষয়ভিত্তিক রুটিন ও বিষয়কোড ২০২৬",
        "papers": [
            ("২৮/০৯/২০২৬ (সোমবার)", "221109", "ইংরেজি (আবশ্যিক) — নন ক্রেডিট", "আবশ্যিক পাস বিষয়"),
            ("০১/১০/২০২৬ (বৃহস্পতিবার)", "221001", "বাংলা সাহিত্যের ইতিহাস-১ (প্রাচীন ও মধ্যযুগ)", "সাহিত্য ইতিহাস পত্র"),
            ("০৭/১০/২০২৬ (বুধবার)", "221003", "মধ্যযুগের কবিতা (শ্রীকৃষ্ণকীর্তন ও মঙ্গলকাব্য)", "মধ্যযুগীয় কাব্য সাহিত্য"),
            ("১২/১০/২০২৬ (সোমবার)", "221005", "বাংলা কবিতা-২ (আধুনিক যুগ)", "আধুনিক কবিতা পত্র"),
            ("১৯/১০/২০২৬ (সোমবার)", "221007", "বাংলা নাটক-১ (প্রারম্ভিক ও আধুনিক নাটক)", "নাট্য সাহিত্য বিশ্লেষণ"),
        ]
    },
    {
        "slug": "english",
        "en_name": "English",
        "bn_name": "ইংরেজি",
        "faculty": "কলা অনুষদ",
        "h2_heading": "NU Honours 2nd Year English Exam Routine 2026 | অনার্স ২য় বর্ষ ইংরেজি বিভাগের পরীক্ষার রুটিন ও বিষয়কোড",
        "img_alt": "NU Honours 2nd Year English Department Exam Routine 2026 Subject Code Routine Card",
        "img_title": "NU Honours 2nd Year English Routine 2026 National University",
        "fig_caption": "ইংরেজি বিভাগ: অনার্স ২য় বর্ষ পরীক্ষার বিষয়ভিত্তিক রুটিন ও বিষয়কোড ২০২৬",
        "papers": [
            ("২৮/০৯/২০২৬ (সোমবার)", "221109", "English (Compulsory) — Non-Credit", "আবশ্যিক পাস বিষয়"),
            ("০১/১০/২০২৬ (বৃহস্পতিবার)", "221101", "Introduction to Drama", "নাট্য সাহিত্যের পরিচিতি"),
            ("০৭/১০/২০২৬ (বুধবার)", "221103", "Romantic Poetry", "রোমান্টিক কাব্য সাহিত্য"),
            ("১২/১০/২০২৬ (সোমবার)", "221105", "Advanced Reading and Writing", "উন্নত পঠন ও লিখন দক্ষতা"),
            ("১৯/১০/২০২৬ (সোমবার)", "221107", "History of English Literature", "ইংরেজি সাহিত্যের ইতিহাস"),
        ]
    },
    {
        "slug": "islamic_history",
        "en_name": "Islamic History & Culture",
        "bn_name": "ইসলামের ইতিহাস ও সংস্কৃতি",
        "faculty": "কলা অনুষদ",
        "h2_heading": "NU Honours 2nd Year Islamic History Exam Routine 2026 | অনার্স ২য় বর্ষ ইসলামের ইতিহাস ও সংস্কৃতি রুটিন",
        "img_alt": "NU Honours 2nd Year Islamic History and Culture Exam Routine 2026 Subject Code Routine Card",
        "img_title": "NU Honours 2nd Year Islamic History Routine 2026 National University",
        "fig_caption": "ইসলামের ইতিহাস বিভাগ: অনার্স ২য় বর্ষ পরীক্ষার বিষয়ভিত্তিক রুটিন ও বিষয়কোড ২০২৬",
        "papers": [
            ("২৮/০৯/২০২৬ (সোমবার)", "221109", "ইংরেজি (আবশ্যিক) — নন ক্রেডিট", "আবশ্যিক পাস বিষয়"),
            ("০১/১০/২০২৬ (বৃহস্পতিবার)", "221601", "আব্বাসীয় খিলাফত (৭৫০-১২৫৮ খ্রি.)", "আব্বাসীয় ইতিহাস পত্র"),
            ("০৭/১০/২০২৬ (বুধবার)", "221603", "ভারতে মুসলিম শাসন (১২০৬-১৫২৬ খ্রি.)", "দিল্লি সালতানাত ও ভারত"),
            ("১২/১০/২০২৬ (সোমবার)", "221605", "মুসলিম দর্শন ও সংস্কৃতির ইতিহাস", "সাংস্কৃতিক উন্নয়ন পত্র"),
            ("১৯/১০/২০২৬ (সোমবার)", "221607", "আধুনিক মধ্যপ্রাচ্যের ইতিহাস", "মধ্যপ্রাচ্য রাজনৈতিক বিকাশ"),
        ]
    },
    {
        "slug": "history",
        "en_name": "History",
        "bn_name": "ইতিহাস",
        "faculty": "কলা অনুষদ",
        "h2_heading": "NU Honours 2nd Year History Exam Routine 2026 | অনার্স ২য় বর্ষ ইতিহাস বিভাগের পরীক্ষার রুটিন ও বিষয়কোড",
        "img_alt": "NU Honours 2nd Year History Exam Routine 2026 Subject Code Routine Card",
        "img_title": "NU Honours 2nd Year History Routine 2026 National University",
        "fig_caption": "ইতিহাস বিভাগ: অনার্স ২য় বর্ষ পরীক্ষার বিষয়ভিত্তিক রুটিন ও বিষয়কোড ২০২৬",
        "papers": [
            ("২৮/০৯/২০২৬ (সোমবার)", "221109", "ইংরেজি (আবশ্যিক) — নন ক্রেডিট", "আবশ্যিক পাস বিষয়"),
            ("০১/১০/২০২৬ (বৃহস্পতিবার)", "221501", "প্রাচীন বাংলার ইতিহাস (১২০৪ খ্রি. পর্যন্ত)", "বাংলার প্রারম্ভিক ইতিহাস"),
            ("০৭/১০/২০২৬ (বুধবার)", "221503", "দিল্লির সালতানাতের ইতিহাস", "সুলতানি শাসনামল"),
            ("১২/১০/২০২৬ (সোমবার)", "221505", "মধ্যযুগীয় ইউরোপের ইতিহাস", "ইউরোপীয় মধ্যযুগীয় ইতিহাস"),
            ("১৯/১০/২০২৬ (সোমবার)", "221507", "আমেরিকার ইতিহাস", "মার্কিন যুক্তরাষ্ট্র রাজনৈতিক বিকাশ"),
        ]
    },
    {
        "slug": "philosophy",
        "en_name": "Philosophy",
        "bn_name": "দর্শন",
        "faculty": "কলা অনুষদ",
        "h2_heading": "NU Honours 2nd Year Philosophy Exam Routine 2026 | অনার্স ২য় বর্ষ দর্শন বিভাগের পরীক্ষার রুটিন ও বিষয়কোড",
        "img_alt": "NU Honours 2nd Year Philosophy Exam Routine 2026 Subject Code Routine Card",
        "img_title": "NU Honours 2nd Year Philosophy Routine 2026 National University",
        "fig_caption": "দর্শন বিভাগ: অনার্স ২য় বর্ষ পরীক্ষার বিষয়ভিত্তিক রুটিন ও বিষয়কোড ২০২৬",
        "papers": [
            ("২৮/০৯/২০২৬ (সোমবার)", "221109", "ইংরেজি (আবশ্যিক) — নন ক্রেডিট", "আবশ্যিক পাস বিষয়"),
            ("০১/১০/২০২৬ (বৃহস্পতিবার)", "221701", "সাধারণ নীতিবিদ্যা (General Ethics)", "নৈতিক তত্ত্ব ও ব্যবহারিক দর্শন"),
            ("০৭/১০/২০২৬ (বুধবার)", "221703", "মুসলিম দর্শন (Muslim Philosophy)", "মুসলিম দার্শনিকদের চিন্তা ধারা"),
            ("১২/১০/২০২৬ (সোমবার)", "221705", "ভারতীয় দর্শন (Indian Philosophy)", "প্রাচ্য দর্শন ধারা"),
            ("১৯/১০/২০২৬ (সোমবার)", "221707", "আধুনিক ইউরোপীয় দর্শন", "পাশ্চাত্য আধুনিক দর্শন"),
        ]
    },

    # Science
    {
        "slug": "mathematics",
        "en_name": "Mathematics",
        "bn_name": "গণিত",
        "faculty": "বিজ্ঞান অনুষদ",
        "h2_heading": "NU Honours 2nd Year Mathematics Exam Routine 2026 | অনার্স ২য় বর্ষ গণিত বিভাগের পরীক্ষার রুটিন ও বিষয়কোড",
        "img_alt": "NU Honours 2nd Year Mathematics Exam Routine 2026 Subject Code Routine Card",
        "img_title": "NU Honours 2nd Year Mathematics Routine 2026 National University",
        "fig_caption": "গণিত বিভাগ: অনার্স ২য় বর্ষ পরীক্ষার বিষয়ভিত্তিক রুটিন ও বিষয়কোড ২০২৬",
        "papers": [
            ("২৮/০৯/২০২৬ (সোমবার)", "221109", "English (Compulsory) — Non-Credit", "আবশ্যিক পাস বিষয়"),
            ("০১/১০/২০২৬ (বৃহস্পতিবার)", "223701", "Calculus-II", "ক্যালকুলাস-২ তত্ত্বীয় পত্র"),
            ("০৭/১০/২০২৬ (বুধবার)", "223703", "Ordinary Differential Equations", "ডিফারেনশিয়াল ইকুয়েশন"),
            ("১২/১০/২০২৬ (সোমবার)", "223705", "Fortran Programming", "কম্পিউটার প্রোগ্রামিং"),
            ("১৯/১০/২০২৬ (সোমবার)", "223707", "Linear Algebra", "লিনিয়ার অ্যালজেবরা"),
        ]
    },
    {
        "slug": "physics",
        "en_name": "Physics",
        "bn_name": "পদার্থবিজ্ঞান",
        "faculty": "বিজ্ঞান অনুষদ",
        "h2_heading": "NU Honours 2nd Year Physics Exam Routine 2026 | অনার্স ২য় বর্ষ পদার্থবিজ্ঞান পরীক্ষার রুটিন ও বিষয়কোড",
        "img_alt": "NU Honours 2nd Year Physics Exam Routine 2026 Subject Code Routine Card",
        "img_title": "NU Honours 2nd Year Physics Routine 2026 National University",
        "fig_caption": "পদার্থবিজ্ঞান বিভাগ: অনার্স ২য় বর্ষ পরীক্ষার বিষয়ভিত্তিক রুটিন ও বিষয়কোড ২০২৬",
        "papers": [
            ("২৮/০৯/২০২৬ (সোমবার)", "221109", "English (Compulsory) — Non-Credit", "আবশ্যিক পাস বিষয়"),
            ("০১/১০/২০২৬ (বৃহস্পতিবার)", "222701", "Electricity and Magnetism", "তড়িৎ ও চুম্বক তত্ত্ব"),
            ("০৭/১০/২০২৬ (বুধবার)", "222703", "Thermal Physics", "তাপীয় পদার্থবিজ্ঞান"),
            ("১২/১০/২০২৬ (সোমবার)", "222705", "Optics", "আলোকবিজ্ঞান পত্র"),
            ("১৯/১০/২০২৬ (সোমবার)", "222707", "Mathematical Physics", "গাণিতিক পদার্থবিজ্ঞান"),
        ]
    },
    {
        "slug": "chemistry",
        "en_name": "Chemistry",
        "bn_name": "রসায়ন",
        "faculty": "বিজ্ঞান অনুষদ",
        "h2_heading": "NU Honours 2nd Year Chemistry Exam Routine 2026 | অনার্স ২য় বর্ষ রসায়ন বিভাগের পরীক্ষার রুটিন ও বিষয়কোড",
        "img_alt": "NU Honours 2nd Year Chemistry Exam Routine 2026 Subject Code Routine Card",
        "img_title": "NU Honours 2nd Year Chemistry Routine 2026 National University",
        "fig_caption": "রসায়ন বিভাগ: অনার্স ২য় বর্ষ পরীক্ষার বিষয়ভিত্তিক রুটিন ও বিষয়কোড ২০২৬",
        "papers": [
            ("২৮/০৯/২০২৬ (সোমবার)", "221109", "English (Compulsory) — Non-Credit", "আবশ্যিক পাস বিষয়"),
            ("০১/১০/২০২৬ (বৃহস্পতিবার)", "222801", "Physical Chemistry-II", "ভৌত রসায়ন-২"),
            ("০৭/১০/২০২৬ (বুধবার)", "222803", "Organic Chemistry-II", "জৈব রসায়ন-২"),
            ("১২/১০/২০২৬ (সোমবার)", "222805", "Inorganic Chemistry-II", "অজৈব রসায়ন-২"),
            ("১৯/১০/২০২৬ (সোমবার)", "222807", "Environmental Chemistry", "পরিবেশ রসায়ন"),
        ]
    },
    {
        "slug": "zoology",
        "en_name": "Zoology",
        "bn_name": "প্রাণিবিজ্ঞান",
        "faculty": "বিজ্ঞান অনুষদ",
        "h2_heading": "NU Honours 2nd Year Zoology Exam Routine 2026 | অনার্স ২য় বর্ষ প্রাণিবিজ্ঞান পরীক্ষার রুটিন ও বিষয়কোড",
        "img_alt": "NU Honours 2nd Year Zoology Exam Routine 2026 Subject Code Routine Card",
        "img_title": "NU Honours 2nd Year Zoology Routine 2026 National University",
        "fig_caption": "প্রাণিবিজ্ঞান বিভাগ: অনার্স ২য় বর্ষ পরীক্ষার বিষয়ভিত্তিক রুটিন ও বিষয়কোড ২০২৬",
        "papers": [
            ("২৮/০৯/২০২৬ (সোমবার)", "221109", "English (Compulsory) — Non-Credit", "আবশ্যিক পাস বিষয়"),
            ("০১/১০/২০২৬ (বৃহস্পতিবার)", "223101", "Animal Diversity-II (Chordata)", "প্রাণীবৈচিত্র্য-২ (কর্ডাটা)"),
            ("০৭/১০/২০২৬ (বুধবার)", "223103", "Comparative Anatomy of Vertebrates", "মেরুদণ্ডী প্রাণীর তুলনামূলক শারীরস্থান"),
            ("১২/১০/২০২৬ (সোমবার)", "223105", "Environmental Biology", "পরিবেশ জীববিজ্ঞান"),
            ("১৯/১০/২০২৬ (সোমবার)", "223107", "Genetics and Molecular Biology", "জিনতত্ত্ব ও আণবিক জীববিজ্ঞান"),
        ]
    },
    {
        "slug": "botany",
        "en_name": "Botany",
        "bn_name": "উদ্ভিদবিজ্ঞান",
        "faculty": "বিজ্ঞান অনুষদ",
        "h2_heading": "NU Honours 2nd Year Botany Exam Routine 2026 | অনার্স ২য় বর্ষ উদ্ভিদবিজ্ঞান পরীক্ষার রুটিন ও বিষয়কোড",
        "img_alt": "NU Honours 2nd Year Botany Exam Routine 2026 Subject Code Routine Card",
        "img_title": "NU Honours 2nd Year Botany Routine 2026 National University",
        "fig_caption": "উদ্ভিদবিজ্ঞান বিভাগ: অনার্স ২য় বর্ষ পরীক্ষার বিষয়ভিত্তিক রুটিন ও বিষয়কোড ২০২৬",
        "papers": [
            ("২৮/০৯/২০২৬ (সোমবার)", "221109", "English (Compulsory) — Non-Credit", "আবশ্যিক পাস বিষয়"),
            ("০১/১০/২০২৬ (বৃহস্পতিবার)", "223001", "Pteridophyta and Gymnosperms", "টেরিডোফাইটা ও ব্যক্তবীজী উদ্ভিদ"),
            ("০৭/১০/২০২৬ (বুধবার)", "223003", "Plant Anatomy and Embryology", "উদ্ভিদ শারীরস্থান ও ভ্রূণবিদ্যা"),
            ("১২/১০/২০২৬ (সোমবার)", "223005", "Plant Ecology and Phytogeography", "উদ্ভিদ বাস্তুবিদ্যা ও উদ্ভিদ ভূগোল"),
            ("১৯/১০/২০২৬ (সোমবার)", "223007", "Plant Pathology and Protection", "উদ্ভিদ রোগতত্ত্ব ও উদ্ভিদ সংরক্ষণ"),
        ]
    },
]


def build_department_sections():
    sections = []
    for dept in DEPT_DATA:
        slug = dept["slug"]
        card_url = f"{CDN_BASE}/nu_honours_2nd_year_fb_routine_{slug}.webp"

        rows_html = []
        for day, code, title, note in dept["papers"]:
            rows_html.append(f"""<tr>
  <td style="padding: 10px 14px; border: 1px solid #e2e8f0; font-weight: 600; color: #0f172a;">{day}</td>
  <td style="padding: 10px 14px; border: 1px solid #e2e8f0; font-family: Arial, sans-serif; font-weight: bold; color: #1e40af;">{code}</td>
  <td style="padding: 10px 14px; border: 1px solid #e2e8f0; font-weight: 600; color: #1e293b;">{title}</td>
  <td style="padding: 10px 14px; border: 1px solid #e2e8f0; color: #64748b;">{note}</td>
</tr>""")
        table_rows_str = "\n".join(rows_html)

        sec = f"""<h2 style="font-family: 'SolaimanLipi', sans-serif; color: #0f172a; font-size: 23px; font-weight: 700; margin: 45px 0 16px 0; border-bottom: 2px solid #0284c7; padding-bottom: 8px;">
{dept['h2_heading']}
</h2>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16px; line-height: 1.85; color: #334155; margin-bottom: 20px;">
জাতীয় বিশ্ববিদ্যালয়ের {dept['faculty']}-এর অন্তর্ভুক্ত <strong>{dept['bn_name']} বিভাগ ({dept['en_name']})</strong>-এর শিক্ষার্থীদের অনার্স ২য় বর্ষ পরীক্ষার পূর্ণাঙ্গ সময়সূচি ও প্রতিটি পত্রের অফিসিয়াল বিষয়কোড নিচে সংযুক্ত করা হলো। প্রতিটি বিষয়ের তত্ত্বীয় পরীক্ষা প্রতিদিন দুপুর ০১:০০ টা থেকে শুরু হবে।
</p>

<figure style="margin: 25px 0; text-align: center;">
<img src="{card_url}" alt="{dept['img_alt']}" title="{dept['img_title']}" style="width: 100%; max-width: 720px; height: auto; border-radius: 12px; box-shadow: 0 8px 24px rgba(0,0,0,0.12); border: 1px solid #cbd5e1; display: block; margin: 0 auto;" loading="lazy" />
<figcaption style="font-size: 13.5px; color: #64748b; margin-top: 10px; font-family: 'SolaimanLipi', sans-serif; font-weight: 600;">{dept['fig_caption']}</figcaption>
</figure>

<div style="overflow-x: auto; margin: 20px 0 35px 0;">
<table style="width: 100%; border-collapse: collapse; font-family: 'SolaimanLipi', sans-serif; font-size: 15px; text-align: left; background: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px;">
<thead>
<tr style="background: #1e293b; color: #ffffff;">
  <th style="padding: 11px 14px; border: 1px solid #334155; width: 28%;">পরীক্ষার তারিখ ও বার</th>
  <th style="padding: 11px 14px; border: 1px solid #334155; width: 16%;">বিষয় কোড</th>
  <th style="padding: 11px 14px; border: 1px solid #334155; width: 36%;">পত্রের নাম ও বিবরণ</th>
  <th style="padding: 11px 14px; border: 1px solid #334155; width: 20%;">মন্তব্য</th>
</tr>
</thead>
<tbody>
{table_rows_str}
</tbody>
</table>
</div>"""
        sections.append(sec)

    return "\n\n".join(sections)


def generate_master_post():
    dept_content = build_department_sections()

    full_html = f"""<figure style="margin: 0 0 25px 0; text-align: center;">
<img src="{HERO_BANNER}" alt="জাতীয় বিশ্ববিদ্যালয় অনার্স ২য় বর্ষ পরীক্ষার রুটিন ২০২৬ সময়সূচি ও বিষয়কোড" title="NU Honours 2nd Year Exam Routine 2026" style="width: 100%; max-width: 1000px; height: auto; border-radius: 12px; box-shadow: 0 5px 20px rgba(0,0,0,0.12); display: block; margin: 0 auto;" loading="eager" />
<figcaption style="font-size: 13px; color: #64748b; margin-top: 8px; font-family: 'SolaimanLipi', sans-serif;">জাতীয় বিশ্ববিদ্যালয় অনার্স ২য় বর্ষ পরীক্ষা ২০২৬: পূর্ণাঙ্গ সময়সূচি, ইংরেজি আবশ্যিক পাস শর্টকাট ও বিভাগভিত্তিক বিষয়কোড</figcaption>
</figure>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 17px; line-height: 1.85; color: #1e293b; margin-bottom: 20px;">
জাতীয় বিশ্ববিদ্যালয় (National University)-এর ২০২৫ সালের অনার্স ২য় বর্ষের চূড়ান্ত পরীক্ষার সময়সূচি ও সংশোধিত রুটিন আনুষ্ঠানিকভাবে কার্যকর হয়েছে। নিয়মিত শিক্ষাবর্ষ (২০২২-২০২৩), অনিয়মিত ও গ্রেড উন্নয়ন (২০২১-২০২২ ও ২০২০-২০২১) শিক্ষাবর্ষের পরীক্ষার্থীদের জন্য এই পরীক্ষা অত্যন্ত গুরুত্বপূর্ণ। বিশেষ করে অনার্স ২য় বর্ষের সকল শাখার শিক্ষার্থীদের জন্য বাধ্যতামূলক <strong>ইংরেজি আবশ্যিক (Compulsory English - বিষয় কোড: 221109)</strong> বিষয়ে পাস করার গোল্ডেন নিয়মাবলি এবং কলা, সামাজিক বিজ্ঞান, ব্যবসায় শিক্ষা ও বিজ্ঞান অনুষদের প্রতিটি বিভাগের বিষয়ভিত্তিক কোড মিলিয়ে পরীক্ষার পূর্ণাঙ্গ প্রস্তুতি নিশ্চিত করতে এই নির্দেশিকাটি সাজানো হয়েছে।
</p>

<!--more-->

<div style="background: #f8fafc; border-left: 5px solid #0284c7; padding: 22px 25px; border-radius: 0 12px 12px 0; margin: 30px 0; box-shadow: 0 2px 10px rgba(0,0,0,0.04); font-family: 'SolaimanLipi', sans-serif;">
<h3 style="margin-top: 0; color: #0369a1; font-size: 20px; font-weight: 700; margin-bottom: 12px;">অনার্স ২য় বর্ষ পরীক্ষার সময়সূচি ২০২৬ একনজরে | NU Honours 2nd Year Routine at a Glance</h3>
<ul style="margin: 0; padding-left: 20px; color: #334155; line-height: 1.85; font-size: 16px;">
<li><strong>বিশ্ববিদ্যালয়ের নাম:</strong> জাতীয় বিশ্ববিদ্যালয়, বাংলাদেশ (National University, Bangladesh)।</li>
<li><strong>পরীক্ষার নাম:</strong> অনার্স ২য় বর্ষ পরীক্ষা ২০২৫ (অনুষ্ঠিত ২০২৬)।</li>
<li><strong>পরীক্ষা শুরু:</strong> ২৮ সেপ্টেম্বর ২০২৬ (সোমবার)।</li>
<li><strong>তত্ত্বীয় পরীক্ষা শেষ:</strong> ২৩ নভেম্বর ২০২৬ (সোমবার)।</li>
<li><strong>পরীক্ষা শুরুর সময়:</strong> প্রতিদিন দুপুর ০১:০০ টা (প্রশ্নপত্রে উল্লেখিত সময় অনুযায়ী)।</li>
<li><strong>প্রথম পরীক্ষা (আবশ্যিক):</strong> ইংরেজি আবশ্যিক — নন-ক্রেডিট (বিষয় কোড: 221109)।</li>
<li><strong>প্রবেশপত্র সংগ্রহ:</strong> নিজ নিজ কলেজের অধ্যক্ষের কার্যালয় থেকে পরীক্ষা শুরুর ৩ দিন পূর্বে।</li>
<li><strong>অফিসিয়াল সোর্স পোর্টাল:</strong> <a href="https://www.nu.ac.bd" target="_blank" rel="noopener" style="color: #0284c7; text-decoration: underline;">nu.ac.bd</a>।</li>
</ul>
</div>

<h2 style="font-family: 'SolaimanLipi', sans-serif; color: #0f172a; font-size: 24px; font-weight: 700; margin: 40px 0 20px 0; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px;">
NU Honours 2nd Year Exam Routine 2026 Overview | অনার্স ২য় বর্ষ পরীক্ষার কেন্দ্রীয় সময়সূচি
</h2>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16px; line-height: 1.85; color: #334155; margin-bottom: 20px;">
জাতীয় বিশ্ববিদ্যালয় কর্তৃক ঘোষিত তারিখ অনুযায়ী প্রতিটি বিষয়ের পরীক্ষা সুনির্দিষ্ট দিনে অনুষ্ঠিত হচ্ছে। সকল অনুষদের কেন্দ্রীয় পরীক্ষার দিনভিত্তিক রূপরেখা নিচে দেওয়া হলো:
</p>

<div style="overflow-x: auto; margin: 25px 0;">
<table style="width: 100%; border-collapse: collapse; font-family: 'SolaimanLipi', sans-serif; font-size: 15px; text-align: left; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
<thead>
<tr style="background: #0f172a; color: #ffffff;">
<th style="padding: 12px 15px; border: 1px solid #334155;">পরীক্ষার তারিখ ও বার</th>
<th style="padding: 12px 15px; border: 1px solid #334155;">বিষয় কোড</th>
<th style="padding: 12px 15px; border: 1px solid #334155;">পত্রের নাম ও বিষয়</th>
<th style="padding: 12px 15px; border: 1px solid #334155;">অনুষদ / শাখা</th>
</tr>
</thead>
<tbody>
<tr style="background: #f8fafc;">
<td style="padding: 12px 15px; border: 1px solid #e2e8f0; font-weight: 600;">২৮/০৯/২০২৬ (সোমবার)</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0; color: #0284c7; font-weight: bold;">221109</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">English (Compulsory) — Non-Credit</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">সকল শাখা (কলা, সামাজিক বিজ্ঞান, বাণিজ্য, বিজ্ঞান)</td>
</tr>
<tr>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0; font-weight: 600;">০১/১০/২০২৬ (বৃহস্পতিবার)</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0; color: #0284c7; font-weight: bold;">বিভাগীয় ১ম পত্র</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">Advanced Accounting-I / HRM / Calculus-II / বাংলা সাহিত্যের ইতিহাস-১ / বৃটিশ ভারত</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">সকল বিভাগের প্রথম মেজর কোর্স</td>
</tr>
<tr style="background: #f8fafc;">
<td style="padding: 12px 15px; border: 1px solid #e2e8f0; font-weight: 600;">০৭/১০/২০২৬ (বুধবার)</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0; color: #0284c7; font-weight: bold;">বিভাগীয় ২য় পত্র</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">Business Communication / ODE / মধ্যযুগের কবিতা / Political Sociology / Consumer Behavior</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">সকল বিভাগের দ্বিতীয় মেজর কোর্স</td>
</tr>
<tr>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0; font-weight: 600;">১২/১০/২০২৬ (সোমবার)</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0; color: #0284c7; font-weight: bold;">বিভাগীয় ৩য় পত্র</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">Business Mathematics / Fortran / বাংলা কবিতা-২ / পূর্ব এশিয়ার সরকার / Basic Econometrics</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">সকল বিভাগের তৃতীয় মেজর কোর্স</td>
</tr>
<tr style="background: #f8fafc;">
<td style="padding: 12px 15px; border: 1px solid #e2e8f0; font-weight: 600;">১৯/১০/২০২৬ (সোমবার)</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0; color: #0284c7; font-weight: bold;">বিভাগীয় ৪র্থ পত্র</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">Principles of Finance / Linear Algebra / বাংলা নাটক-১ / দক্ষিণ এশিয়ার সরকার / Social Psychology</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">সকল বিভাগের চতুর্থ মেজর কোর্স</td>
</tr>
<tr>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0; font-weight: 600;">২৬/১০/২০২৬ (সোমবার)</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0; color: #0284c7; font-weight: bold;">বিভাগীয় ৫ম পত্র</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">Legal Aspects of Business / Taxation in BD / Macro Economics / Auditing</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">ব্যবসায় শিক্ষা অনুষদের অতিরিক্ত মেজর পেপার</td>
</tr>
</tbody>
</table>
</div>

<h2 style="font-family: 'SolaimanLipi', sans-serif; color: #0f172a; font-size: 24px; font-weight: 700; margin: 40px 0 20px 0; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px;">
NU Honours 2nd Year Compulsory English Passing Strategy | ইংরেজি আবশ্যিক পাসের গোল্ডেন রুলস
</h2>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16px; line-height: 1.85; color: #334155; margin-bottom: 20px;">
জাতীয় বিশ্ববিদ্যালয়ের অনার্স ২য় বর্ষে সর্বাধিক শিক্ষার্থী যে বিষয়ে অকৃতকার্য হয় বা মানোন্নয়ন পরীক্ষা দিতে বাধ্য হয়, তা হলো <strong>English (Compulsory - বিষয় কোড: 221109)</strong>। এটি একটি নন-ক্রেডিট কোর্স হলেও অনার্স ডিগ্রি সনদ পাওয়ার জন্য এই বিষয়ে পাস করা ১০০% বাধ্যতামূলক।
</p>

<div style="background: #eff6ff; border-left: 5px solid #2563eb; padding: 20px 22px; border-radius: 0 10px 10px 0; margin: 25px 0; font-family: 'SolaimanLipi', sans-serif;">
<h4 style="margin: 0 0 10px 0; color: #1e40af; font-size: 18px; font-weight: 700;">ইংরেজি আবশ্যিকে প্রথম সুযোগেই পাস করার ৪টি কৌশল:</h4>
<ol style="margin: 0; padding-left: 20px; color: #1e3a8a; line-height: 1.85; font-size: 15.5px;">
<li><strong>Grammar পার্টে সর্বোচ্চ জোর দেওয়া:</strong> গ্রামার অংশে ৪৫ নম্বরের মধ্যে সহজেই ৩৫+ তোলা সম্ভব। বিশেষ করে Changing Sentences, Tag Questions, Suffix and Prefix, Appropriate Prepositions, Right Form of Verbs ও Sentence Connectors নিয়মিত অনুশীলন করুন।</li>
<li><strong>Writing পার্টে ফরম্যাট মুখস্থ রাখা:</strong> Formal Letter, Application, Notice, Poster, Report Writing এবং Paragraph-এর স্ট্যান্ডার্ড স্ট্রাকচার আয়ত্ত করলে নম্বর কাটা যায় না।</li>
<li><strong>Reading Comprehension আগে সমাধান করা:</strong> প্যাসেজ পড়ে সরাসরি মূল পয়েন্টগুলো খাতায় সংক্ষেপে লিখুন। অযথা প্যাসেজের হুবহু লাইন কপি করবেন না।</li>
<li><strong>নন-ক্রেডিট হওয়ায় টার্গেট পাস মার্ক নিশ্চিত করা:</strong> ১০০ নম্বরের পরীক্ষায় পাস মার্ক ৩৩। তবে নিরাপদ থাকার জন্য টার্গেট ৫০+ নম্বরের প্রস্তুতি নেওয়া শ্রেয়।</li>
</ol>
</div>

<!-- All 18 Department Sections -->
{dept_content}

<h2 style="font-family: 'SolaimanLipi', sans-serif; color: #0f172a; font-size: 24px; font-weight: 700; margin: 40px 0 20px 0; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px;">
NU Honours 2nd Year Examination Rules & Hall Instructions | পরীক্ষার্থীদের জন্য পরীক্ষার হলের নিয়মাবলি
</h2>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16px; line-height: 1.85; color: #334155; margin-bottom: 15px;">
পরীক্ষা কেন্দ্রে যেকোনো অপ্রীতিকর পরিস্থিতি ও বহিষ্কার এড়াতে জাতীয় বিশ্ববিদ্যালয় পরীক্ষা নিয়ন্ত্রণ দপ্তর কর্তৃক নির্ধারিত নিয়মাবলি কঠোরভাবে অনুসরণ করতে হবে:
</p>

<ul style="font-family: 'SolaimanLipi', sans-serif; font-size: 16px; line-height: 1.85; color: #334155; margin-bottom: 25px; padding-left: 22px;">
<li><strong>প্রবেশপত্র ও রেজিস্ট্রেশন কার্ড:</strong> পরীক্ষার হলে অবশ্যই মূল প্রবেশপত্র (Admit Card) এবং মূল রেজিস্ট্রেশন কার্ড সঙ্গে রাখতে হবে। সত্যায়িত ফটোকপি সাধারণ ক্ষেত্রে গ্রহণযোগ্য নয়।</li>
<li><strong>পরীক্ষাকেন্দ্রে উপস্থিতির সময়:</strong> পরীক্ষা শুরুর অন্তত ৩০ মিনিট পূর্বে নিজ নিজ নির্ধারিত আসনে প্রবেশ করতে হবে। ওএমআর শিট বিতরণের পর রোল ও রেজিস্ট্রেশন নম্বর সতর্কতার সাথে পূরণ করতে হবে।</li>
<li><strong>মোবাইল ও ইলেকট্রনিক ডিভাইস নিষিদ্ধ:</strong> পরীক্ষা কক্ষে যেকোনো ধরনের মোবাইল ফোন, স্মার্টওয়াচ, ব্লুটুথ ডিভাইস বা ডিজিটাল ক্যালকুলেটর (অননুমোদিত) বহন সম্পূর্ণ বেআইনি এবং সরাসরি বহিষ্কারযোগ্য অপরাধ।</li>
<li><strong>স্বাক্ষর নিশ্চিতকরণ:</strong> প্রতিদিনের পরীক্ষায় উপস্থিতি তালিকায় (Attendance Sheet) আপনার নির্ধারিত স্বাক্ষরের ঘরে স্বাক্ষর করেছেন কি না তা নিশ্চিত করুন।</li>
<li><strong>ব্যবহারিক ও মৌখিক পরীক্ষা:</strong> তত্ত্বীয় পরীক্ষা সমাপ্তির পর নিজ নিজ বিভাগীয় নোটিশ বোর্ড থেকে ব্যবহারিক (Practical) এবং মৌখিক (Viva-Voce) পরীক্ষার সময়সূচি সংগ্রহ করতে হবে।</li>
</ul>

<h2 style="font-family: 'SolaimanLipi', sans-serif; color: #0f172a; font-size: 24px; font-weight: 700; margin: 40px 0 20px 0; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px;">
NU Honours 2nd Year Routine 2026 FAQ | সাধারণ প্রশ্ন ও উত্তর
</h2>

<div style="font-family: 'SolaimanLipi', sans-serif; margin: 25px 0;">

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px 20px; margin-bottom: 15px;">
<h4 style="margin: 0 0 8px 0; color: #0f172a; font-size: 17px; font-weight: 700;">প্রশ্ন ১: অনার্স ২য় বর্ষ পরীক্ষা প্রতিদিন কখন শুরু হয়?</h4>
<p style="margin: 0; color: #475569; font-size: 15.5px; line-height: 1.75;">উত্তর: জাতীয় বিশ্ববিদ্যালয়ের অফিসিয়াল রুটিন অনুযায়ী পরীক্ষা প্রতিদিন দুপুর ০১:০০ টা থেকে শুরু হয়। তবে প্রশ্নপত্রে উল্লেখিত নির্ধারিত সময়সীমা পর্যন্ত পরীক্ষা চলে।</p>
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px 20px; margin-bottom: 15px;">
<h4 style="margin: 0 0 8px 0; color: #0f172a; font-size: 17px; font-weight: 700;">প্রশ্ন ২: ইংরেজি আবশ্যিক (221109) পরীক্ষায় পাস মার্ক কত এবং এটি কি জিপিএ-তে যুক্ত হয়?</h4>
<p style="margin: 0; color: #475569; font-size: 15.5px; line-height: 1.75;">উত্তর: ইংরেজি আবশ্যিক বিষয়ে পাস মার্ক ৩৩। এটি একটি নন-ক্রেডিট কোর্স, তাই এতে প্রাপ্ত নম্বর মূল জিপিএ বা সিজিপিএ-তে যোগ হয় না; তবে ডিগ্রি অর্জনের জন্য এই বিষয়ে পাস করা বাধ্যতামূলক।</p>
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px 20px; margin-bottom: 15px;">
<h4 style="margin: 0 0 8px 0; color: #0f172a; font-size: 17px; font-weight: 700;">প্রশ্ন ৩: কোনো কারণে পরীক্ষার রুটিন পরিবর্তন হলে কীভাবে জানা যাবে?</h4>
<p style="margin: 0; color: #475569; font-size: 15.5px; line-height: 1.75;">উত্তর: কোনো অনিবার্য কারণে তারিখ পরিবর্তন হলে জাতীয় বিশ্ববিদ্যালয়ের অফিসিয়াল ওয়েবসাইট (nu.ac.bd)-এ সংশোধিত নোটিশ প্রকাশ করা হয়। নিয়মিত নোটিশ বোর্ড পর্যবেক্ষণ করার পরামর্শ দেওয়া হলো।</p>
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px 20px; margin-bottom: 15px;">
<h4 style="margin: 0 0 8px 0; color: #0f172a; font-size: 17px; font-weight: 700;">প্রশ্ন ৪: অনার্স ২য় বর্ষের ব্যবহারিক পরীক্ষা কখন অনুষ্ঠিত হবে?</h4>
<p style="margin: 0; color: #475569; font-size: 15.5px; line-height: 1.75;">উত্তর: তত্ত্বীয় পরীক্ষা সমাপ্ত হওয়ার পর বিশ্ববিদ্যালয় থেকে ব্যবহারিক পরীক্ষার কেন্দ্রীয় সময়সীমা ঘোষণা করা হয় এবং কলেজ কর্তৃপক্ষ নিজ সুবিধাজনক সময়ে ব্যবহারিক পরীক্ষার আয়োজন করে।</p>
</div>

</div>

<!-- Author Attribution Box -->
<div class="htbd-author-box" style="display: flex; align-items: center; gap: 18px; margin: 35px 0 25px 0; padding: 18px 22px; background: #f8fafc; border: 1px solid #e2e8f0; border-left: 5px solid #1e3a8a; border-radius: 10px; font-family: 'SolaimanLipi', Arial, sans-serif;">
  <img src="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/author/faruk_sir.webp" 
       alt="ফারুক স্যার (মো. ওমর ফারুক)" 
       class="htbd-author-avatar" 
       width="75" height="75" 
       loading="lazy" 
       style="width: 75px !important; height: 75px !important; min-width: 75px !important; max-width: 75px !important; border-radius: 50% !important; object-fit: cover !important; border: 2px solid #2563eb !important; flex-shrink: 0 !important; display: block !important; margin: 0 !important; box-shadow: 0 2px 6px rgba(0,0,0,0.08) !important;" />
  <div class="htbd-author-info" style="flex: 1 1 auto; min-width: 0;">
    <h4 style="margin: 0 0 4px 0; color: #1e3a8a; font-size: 18px; font-weight: 700; line-height: 1.3;">ফারুক স্যার (মো. ওমর ফারুক)</h4>
    <div class="htbd-author-meta" style="font-size: 13px; color: #64748b; margin-bottom: 6px; font-weight: 600;">শিক্ষাবিদ ও অ্যাকাডেমিক গবেষক | প্রতিষ্ঠাতা, HelpTrickBD</div>
    <p class="htbd-author-bio" style="font-size: 14px; color: #334155; line-height: 1.6; margin: 0;">
      অ্যাকাডেমিক পাঠ্যক্রম এবং জাতীয় বিশ্ববিদ্যালয়ের স্নাতক পর্যায়ের পরীক্ষা প্রস্তুতি ও সাজেশন প্রণয়নে এক দশকের বাস্তব শিক্ষকতার অভিজ্ঞতাসম্পন্ন একজন অ্যাকাডেমিক মেন্টর।
    </p>
  </div>
</div>

<!-- BlogPosting JSON-LD Schema -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "জাতীয় বিশ্ববিদ্যালয় অনার্স ২য় বর্ষ পরীক্ষার রুটিন ২০২৬ (সকল বিভাগ) | NU Honours 2nd Year Exam Routine & Subject Code",
  "description": "জাতীয় বিশ্ববিদ্যালয় অনার্স ২য় বর্ষ পরীক্ষার পূর্ণাঙ্গ সময়সূচি ২০২৬। কলা, সামাজিক বিজ্ঞান, ব্যবসায় শিক্ষা ও বিজ্ঞান অনুষদের সকল বিভাগের রুটিন কার্ড, বিষয় কোড ও ইংরেজি আবশ্যিক পাস ট্রিকস।",
  "image": "{HERO_BANNER}",
  "author": {{
    "@type": "Person",
    "name": "ফারুক স্যার (মো. ওমর ফারুক)"
  }},
  "publisher": {{
    "@type": "Organization",
    "name": "HelpTrickBD",
    "logo": {{
      "@type": "ImageObject",
      "url": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/logo/helptrickbd_logo.png"
    }}
  }},
  "datePublished": "2026-10-01T02:00:00+06:00",
  "dateModified": "2026-10-01T02:00:00+06:00"
}}
</script>

<!-- FAQPage JSON-LD Schema -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "অনার্স ২য় বর্ষ পরীক্ষা প্রতিদিন কখন শুরু হয়?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "জাতীয় বিশ্ববিদ্যালয়ের অফিসিয়াল রুটিন অনুযায়ী পরীক্ষা প্রতিদিন দুপুর ০১:০০ টা থেকে শুরু হয়।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "ইংরেজি আবশ্যিক (221109) পরীক্ষায় পাস মার্ক কত?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "ইংরেজি আবশ্যিক বিষয়ে পাস মার্ক ৩৩। এটি একটি নন-ক্রেডিট কোর্স হলেও পাস করা বাধ্যতামূলক।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "কোনো কারণে পরীক্ষার রুটিন পরিবর্তন হলে কীভাবে জানা যাবে?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "জাতীয় বিশ্ববিদ্যালয়ের অফিসিয়াল ওয়েবসাইট nu.ac.bd-এ সংশোধিত নোটিশ প্রকাশ করা হয়।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "অনার্স ২য় বর্ষের ব্যবহারিক পরীক্ষা কখন অনুষ্ঠিত হবে?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "তত্ত্বীয় পরীক্ষা সমাপ্ত হওয়ার পর বিশ্ববিদ্যালয় থেকে ব্যবহারিক পরীক্ষার কেন্দ্রীয় সময়সূচি ঘোষণা করা হয়।"
      }}
    }}
  ]
}}
</script>"""

    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(full_html)

    meta_data = {
        "title": "জাতীয় বিশ্ববিদ্যালয় অনার্স ২য় বর্ষ পরীক্ষার রুটিন ২০২৬ (সকল বিভাগ) | NU Honours 2nd Year Exam Routine & Subject Code",
        "permalink": "nu-honours-2nd-year-exam-routine-2026",
        "labels": ["জাতীয় বিশ্ববিদ্যালয়", "অনার্স রুটিন", "এডুকেশন নোটিশ"],
        "post_id": "1085826635177863206",
        "status": "DRAFT",
        "search_description": "জাতীয় বিশ্ববিদ্যালয় অনার্স ২য় বর্ষ পরীক্ষার পূর্ণাঙ্গ সময়সূচি ২০২৬। সকল বিভাগের রুটিন কার্ড, বিষয় কোড ও ইংরেজি আবশ্যিক পাস ট্রিকস।",
        "word_count": len(full_html.split())
    }

    with open(OUTPUT_META, "w", encoding="utf-8") as f:
        json.dump(meta_data, f, ensure_ascii=False, indent=2)

    word_count = len(full_html.split())
    print(f"[SUCCESS] Master post generated: {OUTPUT_HTML}")
    print(f"          Word count: ~{word_count} words")
    print(f"          Metadata: {OUTPUT_META}")
    return True


if __name__ == "__main__":
    generate_master_post()
