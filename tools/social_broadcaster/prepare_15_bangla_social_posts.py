#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/social_broadcaster/prepare_15_bangla_social_posts.py
-----------------------------------------------------------
Crafts 100% human-feel, high-reach, zero-AI social copies for the 15 unposted
SSC & Dakhil Bangla 1st Paper posts and syncs them into social_audit_data.json.
Strictly zero-emoji compliant (Rule 12).
"""

import os
import sys
import json
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
AUDIT_DATA_FILE = os.path.join(PROJECT_ROOT, "output_posts", "social_audit_data.json")

# Master dictionary of 15 handcrafted human copies (Zero AI Cliché, High Reach, Organic Engagement)
COPIES = [
    {
        "id": "6904395060145150353",
        "title": "SSC & Dakhil Bangla 1st Paper Final Suggestion 2026-2027 with Answers | ১০০ নম্বরের সম্পূর্ণ সিলেবাস, নতুন মানবণ্টন ও অধ্যায়ভিত্তিক সৃজনশীল-MCQ সুপার গাইড",
        "url": "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-final-suggestion.html",
        "hero_image": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/ssc_bangla_1st_paper_final_suggestion_2027.webp",
        "hook": "এসএসসি ও দাখিল বাংলা ১ম পত্রে এ প্লাস (A+) মিস হওয়ার প্রধান কারণ হলো সাজেশনের নামে বাজারে থাকা আজেবাজে হাজারটা প্রশ্ন পড়ে সময় নষ্ট করা।",
        "core_value": "বোর্ড পরীক্ষার সংশোধিত নতুন মানবণ্টন অনুযায়ী গদ্য ও পদ্যের নিশ্চিত কমনযোগ্য অধ্যায়, ১০০ নম্বরের পূর্ণাঙ্গ ব্লু-প্রিন্ট এবং সৃজনশীলে ফুল মার্কস তোলার গোপন টেকনিক নিয়ে তৈরি করা হয়েছে এই মাস্টার সাজেশন।",
        "points": [
            "গদ্য ও পদ্যের নিশ্চিত কমন অধ্যায়ভিত্তিক সুপার শর্ট সাজেশন",
            "সৃজনশীল প্রশ্নের চার স্তরের (জ্ঞান, অনুধাবন, প্রয়োগ ও উচ্চতর দক্ষতা) নম্বর তোলার নিয়ম",
            "৩০ নম্বরের বহুনির্বাচনি (MCQ) নির্ভুল করার স্পেশাল টিপস",
            "বোর্ড পরীক্ষার খাতা মূল্যায়নের গোপন ক্রাইটেরিয়া ও সময় বণ্টন চার্ট"
        ],
        "engagement": "তোমার কোন অধ্যায়ে প্রস্তুতি এখনও দুর্বল? কমেন্টে জানাও — প্রয়োজনীয় নোট শেয়ার করে দেওয়া হবে।",
        "share_prompt": "পরীক্ষার আগ মুহূর্তে দ্রুত রিভিশনের সুবিধার্থে পোস্টটি এখনই নিজের টাইমলাইনে সেভ বা বন্ধুদের সাথে শেয়ার করে রাখো।"
    },
    {
        "id": "8942718904689778868",
        "title": "এসএসসি ও দাখিল বাংলা ১ম পত্র গদ্যাংশ সৃজনশীল প্রশ্নব্যাংক ২০২৬-২০২৭ (SSC Bangla 1st Paper Prose CQ Question Bank & Full Solution)",
        "url": "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-prose-cq-question.html",
        "hook": "সৃজনশীল প্রশ্নের 'প্রয়োগ' ও 'উচ্চতর দক্ষতা' অংশে চারে চার পাওয়া মুখস্থ বিদ্যার কাজ নয় — আসল চাবিকাঠি হলো উদ্দীপকের সাথে পাঠ্যবইয়ের মেলবন্ধন তৈরি করা।",
        "core_value": "গদ্যাংশের শীর্ষ ১৩টি বোর্ড স্ট্যান্ডার্ড উদ্দীপক নিয়ে প্রস্তুত করা হয়েছে এই পূর্ণাঙ্গ প্রশ্নব্যাংক। যেখানে প্রতিটি প্রশ্নের ক, খ, গ এবং ঘ স্তরের শতভাগ নির্ভুল ও মানসম্মত উত্তর সাজিয়ে দেওয়া হয়েছে।",
        "points": [
            "শীর্ষ ১৩টি বোর্ড স্ট্যান্ডার্ড উদ্দীপক ও নিখুঁত ৪ স্তরের মডেল উত্তর",
            "সুভা, বই পড়া, মানুষ মুহম্মদ (স.), নিমগাছ ও শিক্ষা ও মনুষ্যত্ব থেকে কমন প্রশ্ন",
            "জ্ঞান ও অনুধাবন অংশে টু-দ্য-পয়েন্ট নম্বর নিশ্চিত করার কৌশল",
            "উচ্চতর দক্ষতায় উদ্দীপক ও মূলভাবের তুলনামূলক প্যারাগ্রাফ লেখার আর্ট"
        ],
        "engagement": "গদ্যাংশের কোন গল্পটি তোমার সবচেয়ে কঠিন লাগে? কমেন্টে জানাও।",
        "share_prompt": "সৃজনশীল লেখার ভয় কাটাতে এবং পূর্ণাঙ্গ নোট সংগ্রহে রাখতে পোস্টটি টাইমলাইনে শেয়ার করে রাখো।"
    },
    {
        "id": "7156437687099332664",
        "title": "এসএসসি ও দাখিল বাংলা ১ম পত্র কবিতাংশ সৃজনশীল প্রশ্নব্যাংক ২০২৬-২০২৭ (SSC Bangla 1st Paper Poetry CQ Question Bank & Full Solution)",
        "url": "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-poetry-cq-question.html",
        "hook": "কবিতার রূপক অর্থ ও অন্তর্নিহিত ভাবার্থ সঠিকভাবে ধরতে না পারলে সৃজনশীলে ভালো নম্বর তোলা অসম্ভব।",
        "core_value": "কবিতাংশের গুরুত্বপূর্ণ ১০টি উদ্দীপকের পূর্ণাঙ্গ সমাধান নিয়ে তৈরি এই প্রশ্নব্যাংক। প্রতিটি কবিতার মূল সুর, ভাবার্থ এবং বোর্ড স্ট্যান্ডার্ড প্রশ্নের নির্ভুল উত্তর এখন এক পেজেই প্রস্তুত।",
        "points": [
            "বোর্ড পরীক্ষার সেরা ১০টি কবিতাংশ উদ্দীপক ও ৪ স্তরের পূর্ণাঙ্গ উত্তর",
            "কপোতাক্ষ নদ, বন্দনা, প্রাণ, জীবন বিনিময় ও উমর ফারুক কবিতার মডেল CQ",
            "সেইদিন এই মাঠ, বৃষ্টি, স্বাধীনতা ও বোশেখ কবিতার গভীর বিশ্লেষণ",
            "অনুধাবন ও প্রয়োগ স্তরের ব্যাখ্যায় বোর্ড পরীক্ষকদের পছন্দের প্রেজেন্টেশন"
        ],
        "engagement": "কোন কবিতার ভাবার্থ বুঝতে তোমার বেশি সমস্যা হয়? কমেন্টে জানাও।",
        "share_prompt": "কবিতাংশের শতভাগ প্রস্তুতি এক জায়গায় পেতে পোস্টটি এখনই নিজের কাছে সেভ করে রাখো।"
    },
    {
        "id": "6518640368121583889",
        "title": "এসএসসি বাংলা ১ম পত্র গদ্যাংশ বহুনির্বাচনি প্রশ্নব্যাংক ২০২৬-২০২৭ (SSC Bangla 1st Paper Prose MCQ Suggestion with Answers)",
        "url": "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-prose-mcq-question.html",
        "hook": "বাংলা ১ম পত্রে জিপিএ ফাইভ নিশ্চিত করার সবচেয়ে সহজ কিন্তু ঝুঁকিপূর্ণ জায়গা হলো MCQ — এখানে ১ নম্বর ভুল মানেই সোজা এ গ্রেড!",
        "core_value": "গদ্যাংশের প্রতিটি অধ্যায়ের লাইন-বাই-লাইন বিশ্লেষণ করে বিগত ১০ বছরের বোর্ড প্রশ্ন এবং শীর্ষ স্কুলের টেস্ট পেপার থেকে বাছাই করা সেরা বহুনির্বাচনি প্রশ্নব্যাংক।",
        "points": [
            "অধ্যায়ভিত্তিক সাধারণ বহুনির্বাচনি, বহুপদী সমাপ্তিসূচক ও অভিন্ন তথ্যভিত্তিক MCQ",
            "লেখক পরিচিতি, প্রকাশকাল ও মূলভাব থেকে নিশ্চিত কমন আসার মতো প্রশ্ন",
            "কনফিউজিং অপশন দ্রুত এলিমিনেট করে সঠিক উত্তর বের করার টেকনিক",
            "নিখুঁত উত্তরমালা সহ সেলফ-টেস্ট নেওয়ার সেরা ম্যাটেরিয়াল"
        ],
        "engagement": "গদ্যাংশের MCQ-তে তুমি ৩০-এ কত পাওয়ার টার্গেট করছো? কমেন্টে জানাও।",
        "share_prompt": "প্রতিদিন ৫ মিনিট রিভিশন দেওয়ার জন্য পোস্টটি নিজের টাইমলাইনে সেভ করে রাখো।"
    },
    {
        "id": "5688552421964671574",
        "title": "এসএসসি বাংলা ১ম পত্র কবিতাংশ বহুনির্বাচনি প্রশ্নব্যাংক ২০২৬-২০২৭ (SSC Bangla 1st Paper Poetry MCQ Suggestion with Answers)",
        "url": "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-poetry-mcq.html",
        "hook": "কবিতার চরণ বা পঙক্তি তুলে দিয়ে যখন MCQ আসে, তখনই শিক্ষার্থীরা সবচেয়ে বেশি ভুল করে। এই ফাঁদ থেকে বাঁচার উপায় কী?",
        "core_value": "কবিতাংশের গুরুত্বপূর্ণ চরণ, শব্দার্থ, টীকা এবং কবির মানসিকতা ও ব্যাকগ্রাউন্ড থেকে বাছাই করা ১০০% বোর্ড স্ট্যান্ডার্ড বহুনির্বাচনি প্রশ্নব্যাংক তৈরি করা হয়েছে।",
        "points": [
            "কবিতার গুরুত্বপূর্ণ পঙক্তি ও শব্দার্থভিত্তিক বহুনির্বাচনি প্রশ্ন",
            "বহুপদী সমাপ্তিসূচক (i, ii ও iii) প্রশ্ন সমাধানের বিশেষ নিয়ম",
            "বিগত বছরের বোর্ড পরীক্ষায় বারবার আসা টপ রিপিটেড MCQ কালেকশন",
            "যেকোনো বোর্ডে শতভাগ কমন পাওয়ার মতো প্রামাণ্য উত্তরমালা"
        ],
        "engagement": "কোন কবিতার চরণ মনে রাখা তোমার কাছে সবচেয়ে কঠিন মনে হয়? কমেন্টে জানাও।",
        "share_prompt": "পরীক্ষার আগে দ্রুত চোখ বুলিয়ে নেওয়ার জন্য বন্ধুদের সাথে শেয়ার করে সংগ্রহে রাখো।"
    },
    {
        "id": "5165737254267940811",
        "title": "SSC বাংলা ১ম পত্র সংক্ষিপ্ত প্রশ্নব্যাংক ২০২৬-২০২৭ (২০ নম্বর নিশ্চিত) | গদ্য ও পদ্যের সেরা ১০০টি অনুধাবনমূলক প্রশ্ন ও উত্তর (20-Mark SAQ Bank)",
        "url": "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-short-question.html",
        "hook": "সৃজনশীল প্রশ্নের 'খ' নম্বরের অনুধাবন অংশে অনেকেই পুরো ১ পৃষ্ঠা লিখেও মাত্র ১ পায়! কেন এমন হয় জানো?",
        "core_value": "অনুধাবন প্রশ্নের নিয়ম হলো ২টি সুস্পষ্ট প্যারা — ১ম প্যারায় সরাসরি জ্ঞান এবং ২য় প্যারায় প্রেক্ষাপট ব্যাখ্যা। গদ্য ও পদ্যের সেরা ১০০টি অনুধাবন প্রশ্নের এই আদর্শ কাঠামোতেই সাজানো হয়েছে সম্পূর্ণ প্রশ্নব্যাংক।",
        "points": [
            "গদ্য ও পদ্য থেকে বাছাই করা সেরা ১০০টি অনুধাবনমূলক প্রশ্ন ও টু-দ্য-পয়েন্ট উত্তর",
            "২ প্যারার নিখুঁত কাঠামোতে পূর্ণ ২ নম্বর পাওয়ার প্রামাণ্য পদ্ধতি",
            "বোর্ড পরীক্ষায় বারবার আসা বহুল চর্চিত অনুধাবন প্রশ্নগুলোর ব্যাখ্যা",
            "কম সময়ে সর্বোচ্চ রিভিশন দেওয়ার মতো সহজে পড়ার উপযোগী উপস্থাপনা"
        ],
        "engagement": "অনুধাবন প্রশ্নে ফুল মার্কস পেতে তোমার কী কৌশল? কমেন্টে আমাদের জানাও।",
        "share_prompt": "সৃজনশীলে নিশ্চিত ২০ নম্বর পকেটে ভরতে পোস্টটি নিজের কাছে সেভ করে রাখো।"
    },
    {
        "id": "4514455172913539953",
        "title": "SSC বাংলা ১ম পত্র ১০০ নম্বরের পূর্ণাঙ্গ মডেল টেস্ট ও সমাধান ২০২৬-২০২৭ | বোর্ড স্ট্যান্ডার্ড CQ, MCQ ও সংক্ষিপ্ত প্রশ্ন (100 Marks Full Model Test Paper)",
        "url": "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-model-test.html",
        "hook": "পড়া তো অনেক হলো, কিন্তু আড়াই ঘণ্টায় খাতার ৭টি সৃজনশীল আর ৩০টি MCQ শেষ করার আসল পরীক্ষা দিয়েছো কি?",
        "core_value": "বোর্ড পরীক্ষার হুবহু প্রশ্নকাঠামো ও নতুন মানবণ্টন অনুসরণ করে তৈরি করা হয়েছে এই ১০০ নম্বরের পূর্ণাঙ্গ মডেল টেস্ট পেপার। সময় ধরে পরীক্ষা দিয়ে নিজের অবস্থান যাচাইয়ের সেরা মাধ্যম।",
        "points": [
            "বোর্ড পরীক্ষার আসল ফরম্যাটে ১০০ নম্বরের স্ট্যান্ডার্ড প্রশ্নপত্র",
            "গদ্যাংশ, কবিতাংশ ও সহপাঠের সুষম নম্বর বণ্টনে সৃজনশীল সেট",
            "৩০ নম্বরের মানসম্মত MCQ সেট ও তার নির্ভুল সমাধান",
            "সময় ব্যবস্থাপনার রিয়েল-টাইম এক্সাম স্ট্র্যাটেজি"
        ],
        "engagement": "মডেল টেস্টটি ঘড়ি ধরে পরীক্ষা দিয়ে কত পাচ্ছো কমেন্টে জানাও।",
        "share_prompt": "পরীক্ষার আসল অনুভূতি পেতে এবং নিজেকে যাচাই করতে সহপাঠীদের সাথে শেয়ার করো।"
    },
    {
        "id": "7287843811300052440",
        "title": "আমাদের নতুন গৌরবগাথা সৃজনশীল প্রশ্ন ও উত্তর ২০২৬-২০২৭ | জুলাই ২০২৪ গণঅভ্যুত্থান প্রবন্ধের সম্পূর্ণ বহুনির্বাচনি ও অনুধাবনমূলক সুপার সাজেশন (SSC ও দাখিল বাংলা ১ম পত্র)",
        "url": "https://www.helptrickbd.com/2026/09/amader-notun-gourabbatha-cq-mcq.html",
        "hook": "নতুন পাঠ্যবইয়ে অন্তর্ভুক্ত জুলাই ২০২৪ গণঅভ্যুত্থান নিয়ে রচিত প্রবন্ধ 'আমাদের নতুন গৌরবগাথা' থেকে আসন্ন পরীক্ষায় প্রশ্ন আসার সম্ভাবনা শতভাগ!",
        "core_value": "নতুন এই প্রবন্ধের মূল ভাবার্থ, ঐতিহাসিক প্রেক্ষাপট, সম্ভাব্য সৃজনশীল উদ্দীপক, অনুধাবনমূলক প্রশ্ন ও বহুনির্বাচনির এক অনন্য পূর্ণাঙ্গ গাইডলাইন।",
        "points": [
            "নতুন পাঠ্যভুক্ত প্রবন্ধের লাইনভিত্তিক ভাবার্থ ও পটভূমি বিশ্লেষণ",
            "জুলাই গণঅভ্যুত্থান ও তরুণ সমাজের আত্মত্যাগের ওপর বোর্ড স্ট্যান্ডার্ড উদ্দীপক",
            "গুরুত্বপূর্ণ জ্ঞান ও অনুধাবনমূলক প্রশ্নোত্তর কালেকশন",
            "পরীক্ষায় কমন পাওয়ার মতো সম্ভাব্য বহুনির্বাচনি (MCQ) সেট"
        ],
        "engagement": "নতুন এই প্রবন্ধটি কি তোমার পড়া শেষ হয়েছে? কমেন্টে মতামত জানাও।",
        "share_prompt": "নতুন টপিকের সেরা প্রস্তুতি সবার আগে নিশ্চিত করতে পোস্টটি টাইমলাইনে শেয়ার রাখো।"
    },
    {
        "id": "4356373537694150476",
        "title": "SSC বাংলা ১ম পত্র গদ্যাংশ পর্ব-১ সৃজনশীল প্রশ্ন ও উত্তর ২০২৬-২০২৭ | প্রত্যুপকার, সুভা, বই পড়া ও নিরীহ বাঙালি CQ Solution",
        "url": "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-prose-cq.html",
        "hook": "প্রত্যুপকার, সুভা, বই পড়া ও নিরীহ বাঙালি — এই ৪টি অধ্যায় থেকে প্রতি বছর বোর্ডে ন্যূনতম ২টি সৃজনশীল প্রশ্ন নিশ্চিত থাকে!",
        "core_value": "গদ্যাংশের ১ম পর্বের এই চারটি বহুল গুরুত্বপূর্ণ অধ্যায়ের সেরা উদ্দীপক ও ৪ স্তরের পূর্ণাঙ্গ মডেল উত্তর নিয়ে সাজানো হয়েছে বিশেষ স্টাডি নোট।",
        "points": [
            "সুভা ও প্রত্যুপকার অধ্যায়ের সংবেদনশীল উদ্দীপক ও নিখুঁত উত্তর",
            "বই পড়া ও নিরীহ বাঙালি প্রবন্ধের দার্শনিক ভাবার্থ ভিত্তিক CQ",
            "জ্ঞান, অনুধাবন, প্রয়োগ ও উচ্চতর দক্ষতার নম্বর পাওয়ার কাঠামো",
            "বোর্ড পরীক্ষকদের মূল্যায়নের মূল দিকনির্দেশনা"
        ],
        "engagement": "এই চারটির মধ্যে কোন অধ্যায়ের সৃজনশীল তোমার কাছে সহজ মনে হয়? কমেন্টে জানাও।",
        "share_prompt": "৪টি গুরুত্বপূর্ণ অধ্যায়ের পূর্ণাঙ্গ প্রস্তুতি নিশ্চিত করতে পোস্টটি শেয়ার করে রাখো।"
    },
    {
        "id": "8676318542398082119",
        "title": "SSC বাংলা ১ম পত্র গদ্যাংশ পর্ব-২ সৃজনশীল প্রশ্ন ও উত্তর ২০২৬-২০২৭ | মানুষ মুহম্মদ (স.), নিমগাছ, উপেক্ষিত শক্তি ও শিক্ষা ও মনুষ্যত্ব CQ",
        "url": "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-prose-cq-part-2.html",
        "hook": "মানুষ মুহম্মদ (স.), নিমগাছ, উপেক্ষিত শক্তির উদ্বোধন এবং শিক্ষা ও মনুষ্যত্ব — মানবতা ও মূল্যবোধের এই ৪টি অধ্যায় ছাড়া বোর্ডের প্রশ্ন হয় না!",
        "core_value": "গদ্যাংশের ২য় পর্বের এই শীর্ষ অধ্যায়গুলোর বাস্তবসম্মত উদ্দীপক ও স্ট্যান্ডার্ড ৪ স্তরের উত্তরপত্র নিয়ে এই স্টাডি গাইড প্রস্তুত করা হয়েছে।",
        "points": [
            "নিমগাছ গল্পের রূপক অর্থ ও প্রতীকী উদ্দীপক বিশ্লেষণ",
            "শিক্ষা ও মনুষ্যত্ব প্রবন্ধের জীবসত্তা ও মানবসত্তার তুলনামূলক CQ",
            "মানুষ মুহম্মদ (স.) ও উপেক্ষিত শক্তির মানবিক মূল্যবোধের মডেল উত্তর",
            "পরীক্ষার খাতায় সর্বোচ্চ নম্বর অর্জনের স্মার্ট প্রেজেন্টেশন"
        ],
        "engagement": "নিমগাছ গল্পের শেষ লাইনটির গভীর ভাবার্থ কি বুঝতে পেরেছো? কমেন্টে জানাও।",
        "share_prompt": "মূল্যবান এই ৪টি অধ্যায়ের নোট সংগ্রহে রাখতে এখনই পোস্টটি টাইমলাইনে সেভ করো।"
    },
    {
        "id": "6925279533940643847",
        "title": "SSC বাংলা ১ম পত্র গদ্যাংশ পর্ব-৩ সৃজনশীল প্রশ্ন ও উত্তর ২০২৬-২০২৭ | প্রবাস বন্ধু, মমতাদি, একুশের গল্প ও নতুন গৌরবগাথা CQ",
        "url": "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-prose-cq-part-3.html",
        "hook": "প্রবাস বন্ধু, মমতাদি, একুশের গল্প এবং নতুন গৌরবগাথা — গল্পগুলোর বিষয়বস্তু বৈচিত্র্যময় হওয়ায় সৃজনশীলে একটু সচেতনভাবেই উত্তর সাজাতে হয়।",
        "core_value": "গদ্যাংশের ৩য় পর্বের এই আকর্ষণীয় অধ্যায়গুলোর প্রামাণ্য উদ্দীপক ও নির্ভুল উত্তরমালার পূর্ণাঙ্গ সংকলন।",
        "points": [
            "প্রবাস বন্ধু ও মমতাদি গল্পের মানবিক সম্পর্কের গভীর বিশ্লেষণ",
            "একুশের গল্প ও ভাষা আন্দোলনের ঐতিহাসিক প্রেক্ষাপট ভিত্তিক CQ",
            "নতুন গৌরবগাথা প্রবন্ধের সমকালীন উদ্দীপক সমাধান",
            "উচ্চতর দক্ষতায় সময় বাঁচিয়ে ফুল মার্কস তোলার লেখার ট্রিকস"
        ],
        "engagement": "মমতাদি গল্পে তোমার সবচেয়ে প্রিয় অংশ কোনটি? কমেন্টে জানাও।",
        "share_prompt": "পরীক্ষার শেষ মুহূর্তের চূড়ান্ত রিভিশনের জন্য পোস্টটি বন্ধুদের সাথে শেয়ার করো।"
    },
    {
        "id": "6383095457170141697",
        "title": "SSC বাংলা ১ম পত্র কবিতাংশ পর্ব-১ সৃজনশীল প্রশ্ন ও উত্তর ২০২৬-২০২৭ | বন্দনা, কপোতাক্ষ নদ, প্রাণ, জীবন বিনিময় ও উমর ফারুক CQ",
        "url": "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-poetry-cq-part-1.html",
        "hook": "কপোতাক্ষ নদ, বন্দনা, প্রাণ, জীবন বিনিময় ও উমর ফারুক — দেশপ্রেম ও মানবতার এই ৫টি কালজয়ী কবিতা থেকে প্রতি বছর নিশ্চিত প্রশ্ন থাকে!",
        "core_value": "কবিতাংশের ১ম পর্বের গুরুত্বপূর্ণ পাঁচটি কবিতার উদ্দীপক, কবির মনের ভাব ও ৪ স্তরের আদর্শ সৃজনশীল সমাধান নিয়ে সাজানো হয়েছে এই পোস্ট।",
        "points": [
            "কপোতাক্ষ নদ কবিতার চতুর্দশপদী রূপ ও স্মৃতিকাতরতার উদ্দীপক",
            "জীবন বিনিময় ও উমর ফারুক কবিতার আত্মত্যাগ ও সাম্যের মডেল CQ",
            "প্রাণ ও বন্দনা কবিতার মূলভাব ও সৃজনশীল প্রশ্নের সমাধান",
            "ক ও খ নম্বরের নির্ভুল উত্তর লেখার সহজ টেকনিক"
        ],
        "engagement": "কপোতাক্ষ নদ কবিতার মূল সুর তুমি কীভাবে মনে রাখো? কমেন্টে শেয়ার করো।",
        "share_prompt": "কবিতাংশের গুরুত্বপূর্ণ এই অধ্যায়গুলোর প্রস্তুতি পাকা করতে পোস্টটি সেভ করে রাখো।"
    },
    {
        "id": "5928495229348422345",
        "title": "SSC বাংলা ১ম পত্র কবিতাংশ পর্ব-২ সৃজনশীল প্রশ্ন ও উত্তর ২০২৬-২০২৭ | সেইদিন এই মাঠ, বৃষ্টি, আগন্তুক নই, স্বাধীনতা ও বোশেখ CQ",
        "url": "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-poetry-cq-part-2.html",
        "hook": "সেইদিন এই মাঠ, বৃষ্টি, আমি কোনো আগন্তুক নই, তোমাকে পাওয়ার জন্যে হে স্বাধীনতা ও বোশেখ — আধুনিক কবিতার ভাবার্থ বোঝা তুলনামূলকভাবে বেশি স্পর্শকাতর।",
        "core_value": "কবিতাংশের ২য় পর্বের এই শীর্ষ ৫টি আধুনিক কবিতার রূপক অর্থ ও উদ্দীপক সমাধানের ১০০% মানসম্মত পূর্ণাঙ্গ স্টাডি নোট।",
        "points": [
            "সেইদিন এই মাঠ কবিতার প্রকৃতির চিরন্তনতা বনাম মানুষের নশ্বরতা বিশ্লেষণ",
            "তোমাকে পাওয়ার জন্যে হে স্বাধীনতা কবিতার মুক্তিযুদ্ধের রূপক উদ্দীপক",
            "আমি কোনো আগন্তুক নই ও বোশেখ কবিতার দেশজ অনুভূতির মডেল উত্তর",
            "গ ও ঘ নম্বরে চার চারে চার নিশ্চিত করার প্রামাণ্য কাঠামো"
        ],
        "engagement": "আধুনিক কবিতার সৃজনশীল সমাধান তোমার কেমন লাগে? কমেন্টে জানাও।",
        "share_prompt": "পরীক্ষার হলে যাতে বিভ্রান্ত না হতে হয়, পোস্টটি নিজের প্রোফাইলে সেভ করে রাখো।"
    },
    {
        "id": "6065716687095219706",
        "title": "SSC ও দাখিল বাংলা ১ম পত্র কবিতাংশ সৃজনশীল ও ভাবার্থ সমাধান ২০২৬-২০২৭ | কপোতাক্ষ নদ, বন্দনা, তোমাকে পাওয়ার জন্যে হে স্বাধীনতা ও জীবন বিনিময়",
        "url": "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-poetry-cq.html",
        "hook": "কবিতার পঙক্তির অন্তর্নিহিত দর্শন যদি বুঝতে পারো, তবে সৃজনশীল প্রশ্নের উত্তর লেখা তোমার কাছে সবচেয়ে সহজ মনে হবে।",
        "core_value": "কবিতাংশের শীর্ষ চারটি কবিতার সম্পূর্ণ ভাবার্থ, ব্যাখ্যা এবং বিগত বোর্ড পরীক্ষার প্রশ্ন বিশ্লেষণের সমন্বয়ে তৈরি স্পেশাল স্টাডি গাইড।",
        "points": [
            "৪টি মূল কবিতার লাইনভিত্তিক শাব্দিক ও ভাবার্থ বিশ্লেষণ",
            "বোর্ড পরীক্ষার সেরা সৃজনশীল উদ্দীপকের মডেল কাঠামো",
            "অনুধাবন অংশে ২ নম্বরের জন্য সুনির্দিষ্ট প্যারাগ্রাফ প্রেজেন্টেশন",
            "জ্ঞানমূলক প্রশ্নের দ্রুত মনে রাখার স্পেশাল নোটস"
        ],
        "engagement": "কবিতাংশের কোন প্রশ্নটিতে তোমার নম্বর বেশি কাটা যায়? কমেন্টে জানাও।",
        "share_prompt": "কবিতার পূর্ণাঙ্গ সমাধান হাতের কাছে রাখতে পোস্টটি সহপাঠীদের সাথে শেয়ার করো।"
    },
    {
        "id": "4807143611644528582",
        "title": "SSC ও দাখিল বাংলা ১ম পত্র ৩০ নম্বরের বহুনির্বাচনি (MCQ) ও সংক্ষিপ্ত প্রশ্নব্যাংক (SAQ) ২০২৬-২০২৭ | গদ্যাংশ ও কবিতাংশের শীর্ষ কমন প্রশ্ন সমাধান",
        "url": "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-mcq-saq-question.html",
        "hook": "৩০ নম্বরের MCQ আর ২০ নম্বরের সংক্ষিপ্ত প্রশ্ন (SAQ) — এই ৫০ নম্বরই তোমার বাংলা ১ম পত্রের গ্রেড নির্ধারণ করে দেয়!",
        "core_value": "গদ্যাংশ ও কবিতাংশ থেকে বাছাই করা সেরা ৫০ নম্বরের কমনযোগ্য প্রশ্নব্যাংক। সময় নষ্ট না করে সরাসরি পরীক্ষায় আসার মতো প্রশ্নগুলোর সমন্বিত সংকলন।",
        "points": [
            "৩০ নম্বরের নিশ্চিত বহুনির্বাচনি (MCQ) বোর্ড স্ট্যান্ডার্ড মডেল সেট",
            "২০ নম্বরের অনুধাবনমূলক সংক্ষিপ্ত প্রশ্নব্যাংক ও নির্ভুল উত্তরমালা",
            "গদ্য ও পদ্যের অধ্যায়ভিত্তিক সর্বোচ্চ সম্ভাব্য গুরুত্বপূর্ণ প্রশ্নসমূহ",
            "পরীক্ষার হলে সঠিক উত্তর চেনার শর্টকাট টেকনিক ও টিপস"
        ],
        "engagement": "৫০ নম্বরের অবজেক্টিভ অংশে তোমার টার্গেট কত? কমেন্টে জানাও।",
        "share_prompt": "৫০ নম্বর নিশ্চিত করতে এবং বন্ধুদের সাহায্য করতে পোস্টটি এখনই শেয়ার করে রাখো।"
    }
]

def format_telegram(copy_data):
    bullets = "\n".join([f"• {p}" for p in copy_data["points"]])
    text = (
        f"<b>{copy_data['title']}</b>\n\n"
        f"{copy_data['hook']}\n\n"
        f"{copy_data['core_value']}\n\n"
        f"<b>বিশেষ আকর্ষণ ও যা যা থাকছে:</b>\n"
        f"{bullets}\n\n"
        f"<b>» সম্পূর্ণ স্টাডি গাইড ও মডেল প্রশ্নোত্তর বিস্তারিত পড়তে ভিজিট করুন:</b>\n\n"
        f"<a href=\"{copy_data['url']}\"><b>{copy_data['url']}</b></a>\n\n"
        f"#SSC2027 #Bangla1stPaper #SSCExam #HelpTrickBD #StudyTips #Dakhil2027"
    )
    return text

def format_facebook(copy_data):
    bullets = "\n".join([f"- {p}" for p in copy_data["points"]])
    text = (
        f"{copy_data['hook']}\n\n"
        f"{copy_data['core_value']}\n\n"
        f"এই বিশেষ গাইডে যা যা থাকছে:\n"
        f"{bullets}\n\n"
        f"{copy_data['engagement']}\n\n"
        f"{copy_data['share_prompt']}\n\n"
        f"সম্পূর্ণ গাইডটি পড়তে নিচের লিংকে ক্লিক করুন:\n"
        f"{copy_data['url']}\n\n"
        f"#SSC2027 #Bangla1stPaper #SSCExam #HelpTrickBD #StudyTips #Dakhil2027"
    )
    return text

def format_whatsapp(copy_data):
    bullets = "\n".join([f"• {p}" for p in copy_data["points"]])
    text = (
        f"*{copy_data['title']}*\n\n"
        f"{copy_data['hook']}\n\n"
        f"{copy_data['core_value']}\n\n"
        f"*এই গাইডের বিশেষ দিকসমূহ:*\n"
        f"{bullets}\n\n"
        f"_{copy_data['engagement']}_\n\n"
        f"*সম্পূর্ণ গাইডটি পড়তে ভিজিট করুন:*\n"
        f"{copy_data['url']}\n\n"
        f"#SSC2027 #Bangla1stPaper #SSCExam #HelpTrickBD"
    )
    return text

IMAGE_MAP = {
    "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-final-suggestion.html": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/ssc_bangla_1st_paper_final_suggestion_2027.webp",
    "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-prose-cq-question.html": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/ssc_bangla_1st_paper_prose_cq_bank_2027.webp",
    "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-poetry-cq-question.html": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/ssc_bangla_1st_paper_poetry_cq_bank_2027.webp",
    "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-prose-mcq-question.html": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/ssc_bangla_1st_paper_prose_mcq_bank_2027.webp",
    "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-poetry-mcq.html": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/ssc_bangla_1st_paper_poetry_mcq_bank_2027.webp",
    "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-short-question.html": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/ssc_bangla_1st_paper_saq_bank_2027.webp",
    "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-model-test.html": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/ssc_bangla_1st_paper_model_test_2027.webp",
    "https://www.helptrickbd.com/2026/09/amader-notun-gourabbatha-cq-mcq.html": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/amader_notun_gourabbatha_cq_mcq_2027.webp",
    "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-prose-cq.html": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/ssc_bangla_1st_paper_prose_cq_2027.webp",
    "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-prose-cq-part-2.html": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/ssc_bangla_1st_paper_prose_part2_2027.webp",
    "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-prose-cq-part-3.html": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/ssc_bangla_1st_paper_prose_part3_2027.webp",
    "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-poetry-cq-part-1.html": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/ssc_bangla_1st_paper_poetry_part1_2027.webp",
    "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-poetry-cq-part-2.html": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/ssc_bangla_1st_paper_poetry_part2_2027.webp",
    "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-poetry-cq.html": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/ssc_bangla_1st_paper_poetry_cq_2027.webp",
    "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-mcq-saq-question.html": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/ssc_bangla_1st_paper_mcq_saq_2027.webp"
}

def main():
    if not os.path.exists(AUDIT_DATA_FILE):
        print(f"Error: {AUDIT_DATA_FILE} not found!")
        return

    with open(AUDIT_DATA_FILE, "r", encoding="utf-8") as f:
        social_data = json.load(f)

    existing_urls = {r.get("url") for r in social_data if r.get("url")}
    added_count = 0

    for c in COPIES:
        url = c["url"]
        if url in existing_urls:
            continue

        hero_img = IMAGE_MAP.get(url, c.get("hero_image", ""))
        tg_copy = format_telegram(c)
        fb_copy = format_facebook(c)
        wa_copy = format_whatsapp(c)

        new_record = {
            "id": c["id"],
            "title": c["title"],
            "url": url,
            "category": "এসএসসি ও দাখিল স্টাডি গাইড",
            "labels": ["SSC Suggestion 2027", "Bangla 1st Paper", "Education Guide"],
            "hero_image": hero_img,
            "posted_facebook": False,
            "posted_telegram": False,
            "posted_whatsapp": False,
            "copy": {
                "title": c["title"],
                "post_url": url,
                "hero_image": hero_img,
                "archetype": "academic",
                "intro_summary": c["core_value"],
                "highlights": c["points"],
                "button_text": "সম্পূর্ণ গাইড ও মডেল প্রশ্ন পড়ুন",
                "telegram": tg_copy,
                "facebook": fb_copy,
                "whatsapp": wa_copy,
                "hashtags": ["#SSC2027", "#Bangla1stPaper", "#SSCExam", "#HelpTrickBD", "#StudyTips"]
            }
        }
        # Insert at the beginning so that oldest-first reversal in broadcast engine works cleanly
        social_data.insert(0, new_record)
        added_count += 1

    with open(AUDIT_DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(social_data, f, ensure_ascii=False, indent=2)

    print(f"Successfully prepared and injected {added_count} new human-feel social posts into {AUDIT_DATA_FILE}!")

if __name__ == "__main__":
    main()
