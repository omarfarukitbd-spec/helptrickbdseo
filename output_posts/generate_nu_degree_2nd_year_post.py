#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
output_posts/generate_nu_degree_2nd_year_post.py
------------------------------------------------
Generates the authoritative master article for:
জাতীয় বিশ্ববিদ্যালয় ডিগ্রি ২য় বর্ষ ইনকোর্স নম্বর এন্ট্রি ও পরীক্ষার গাইড ২০২৬ | NU Degree 2nd Year In-Course & Exam Routine

Adheres to:
- SolaimanLipi typography
- Byte-0 Hero image placement before <!--more--> jump break
- Position 0 Summary Answer Box in first 100 words
- Authentic table & callout boxes
- Step-by-step portal instructions for colleges and students
- Subject groups (BA, BSS, BBS, BSc) structure & pass mark rules
- FAQPage & BlogPosting Schema.org JSON-LD microdata
- Omar Faruk Author Attribution Card
- Strictly ZERO EMOJIS (Rule 12)
"""

import os
import sys
import json

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUTPUT_HTML = os.path.join(PROJECT_ROOT, "output_posts", "nu-degree-2nd-year-in-course-and-exam-routine-2026.html")
OUTPUT_META = os.path.join(PROJECT_ROOT, "output_posts", "nu-degree-2nd-year-in-course-and-exam-routine-2026_meta.json")

CDN_BASE = "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts"
HERO_BANNER = f"{CDN_BASE}/nu_degree_2nd_year_in_course_2026.webp"


def generate_master_post():
    full_html = f"""<figure style="margin: 0 0 25px 0; text-align: center;">
<img src="{HERO_BANNER}" alt="জাতীয় বিশ্ববিদ্যালয় ডিগ্রি ২য় বর্ষ ইনকোর্স নম্বর এন্ট্রি ও পরীক্ষার রুটিন ২০২৬" title="NU Degree 2nd Year In-Course Exam Routine 2026" style="width: 100%; max-width: 1000px; height: auto; border-radius: 12px; box-shadow: 0 5px 20px rgba(0,0,0,0.12); display: block; margin: 0 auto;" loading="eager" />
<figcaption style="font-size: 13px; color: #64748b; margin-top: 8px; font-family: 'SolaimanLipi', sans-serif;">জাতীয় বিশ্ববিদ্যালয় ডিগ্রি ২য় বর্ষ ইনকোর্স নম্বর এন্ট্রি, বর্ধিত সময়সূচি ও চূড়ান্ত পরীক্ষার পূর্ণাঙ্গ গাইডলাইন ২০২৬</figcaption>
</figure>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 17px; line-height: 1.85; color: #1e293b; margin-bottom: 20px;">
জাতীয় বিশ্ববিদ্যালয় (National University)-এর ২০২৫ সালের ডিগ্রী (পাস) ও সার্টিফিকেট কোর্সের ২য় বর্ষের ইনকোর্স পরীক্ষার নম্বর অনলাইনে এন্ট্রির সময়সীমা আনুষ্ঠানিকভাবে বৃদ্ধি করা হয়েছে। পরীক্ষা নিয়ন্ত্রণ দপ্তর কর্তৃক প্রকাশিত স্মারক নং ৬০৬৯ অনুযায়ী, আগামী <strong>০৪ অক্টোবর ২০২৬ থেকে ১২ অক্টোবর ২০২৬</strong> তারিখ পর্যন্ত সংশ্লিষ্ট কলেজ কর্তৃপক্ষ শিক্ষার্থীদের ইনকোর্স নম্বর অনলাইনে এন্ট্রি ও পূর্বে কৃত ভুল কোর্সকোড সংশোধন করতে পারবে। জাতীয় বিশ্ববিদ্যালয়ের কঠোর বিধিমালা অনুযায়ী, অনলাইনে ইনকোর্স নম্বর এন্ট্রি ব্যতীত কোনো পরীক্ষার্থীর নাম পরীক্ষার ফরম পূরণের সম্ভাব্য তালিকা (Probable List)-এ অন্তর্ভুক্ত হবে না। বিএ, বিএসএস, বিবিএস এবং বিএসসি শাখার পরীক্ষার্থী ও কলেজ প্রশাসনের সুবিধার জন্য ইনকোর্স নম্বর বণ্টন, ফরম পূরণ ও পরীক্ষার পূর্ণাঙ্গ রূপরেখা নিচে বিশদভাবে উপস্থাপন করা হলো।
</p>

<!--more-->

<div style="background: #f0fdfa; border-left: 5px solid #0f766e; padding: 22px 25px; border-radius: 0 12px 12px 0; margin: 30px 0; box-shadow: 0 2px 10px rgba(0,0,0,0.04); font-family: 'SolaimanLipi', sans-serif;">
<h3 style="margin-top: 0; color: #115e59; font-size: 20px; font-weight: 700; margin-bottom: 12px;">ডিগ্রি ২য় বর্ষ ইনকোর্স নম্বর এন্ট্রি বিজ্ঞপ্তি ২০২৬ একনজরে | Notice at a Glance</h3>
<ul style="margin: 0; padding-left: 20px; color: #134e4a; line-height: 1.85; font-size: 16px;">
<li><strong>কর্তৃপক্ষ:</strong> জাতীয় বিশ্ববিদ্যালয়, বাংলাদেশ (পরীক্ষা নিয়ন্ত্রণ দপ্তর)।</li>
<li><strong>কোর্সের নাম:</strong> ডিগ্রি (পাস) ও সার্টিফিকেট কোর্স ২য় বর্ষ পরীক্ষা ২০২৫ (অনুষ্ঠিত ২০২৬)।</li>
<li><strong>অফিসিয়াল স্মারক নং:</strong> ০৫(৫৩৪) জাতীঃ বিঃ/পরীঃ/ডিগ্রী (পাস)/২০২২/৬০৬৯।</li>
<li><strong>বিজ্ঞপ্তি প্রকাশের তারিখ:</strong> ০১ অক্টোবর ২০২৬ খ্রি.।</li>
<li><strong>ইনকোর্স নম্বর অনলাইনে এন্ট্রির বর্ধিত সময়:</strong> ০৪/১০/২০২৬ থেকে ১২/১০/২০২৬ তারিখ পর্যন্ত।</li>
<li><strong>কোর্সকোড ও এন্ট্রি সংশোধনের সুযোগ:</strong> ১২ অক্টোবর ২০২৬ তারিখের মধ্যে প্রযোজ্য।</li>
<li><strong>বাধ্যতামূলক শর্ত:</strong> ইনকোর্স নম্বর অনলাইনে এন্ট্রি ছাড়া ফরম পূরণের Probable List-এ নাম আসবে না।</li>
<li><strong>অফিসিয়াল পোর্টাল:</strong> <a href="https://www.nu.ac.bd" target="_blank" rel="noopener" style="color: #0f766e; text-decoration: underline;">www.nu.ac.bd</a> এবং <a href="http://ems.nu.ac.bd" target="_blank" rel="noopener" style="color: #0f766e; text-decoration: underline;">ems.nu.ac.bd</a>।</li>
</ul>
</div>

<h2 style="font-family: 'SolaimanLipi', sans-serif; color: #0f172a; font-size: 24px; font-weight: 700; margin: 40px 0 20px 0; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px;">
NU Degree 2nd Year In-Course Notice Analysis | অফিসিয়াল বিজ্ঞপ্তির গুরুত্বপূর্ণ শর্ত ও বিশ্লেষণ
</h2>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16px; line-height: 1.85; color: #334155; margin-bottom: 20px;">
জাতীয় বিশ্ববিদ্যালয় পরীক্ষা নিয়ন্ত্রক দপ্তর কর্তৃক ০১ অক্টোবর ২০২৬ তারিখে স্বাক্ষরিত বিজ্ঞপ্তিতে স্পষ্ট উল্লেখ করা হয়েছে যে, পূর্বে প্রকাশিত ২২/০৭/২০২৬ তারিখের মূল স্মারক নং ৫৮৮৪-এর শর্তাবলি অপরিবর্তিত রেখে সময় বৃদ্ধি করা হয়েছে। এই বিজ্ঞপ্তির প্রধান তিনটি দিক নিম্নরূপ:
</p>

<div style="overflow-x: auto; margin: 25px 0;">
<table style="width: 100%; border-collapse: collapse; font-family: 'SolaimanLipi', sans-serif; font-size: 15px; text-align: left; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
<thead>
<tr style="background: #024a4d; color: #ffffff;">
<th style="padding: 12px 15px; border: 1px solid #134e4a;">কার্যক্রমের বিবরণ</th>
<th style="padding: 12px 15px; border: 1px solid #134e4a;">নির্ধারিত সময়সীমা</th>
<th style="padding: 12px 15px; border: 1px solid #134e4a;">দায়িত্বপ্রাপ্ত পক্ষ</th>
<th style="padding: 12px 15px; border: 1px solid #134e4a;">গুরুত্ব ও সতর্কতা</th>
</tr>
</thead>
<tbody>
<tr style="background: #f8fafc;">
<td style="padding: 12px 15px; border: 1px solid #e2e8f0; font-weight: 600;">ইনকোর্স নম্বর অনলাইনে এন্ট্রি</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0; color: #0f766e; font-weight: bold;">০৪/১০/২০২৬ হতে ১২/১০/২০২৬</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">সংশ্লিষ্ট কলেজ প্রশাসন ও শিক্ষকবৃন্দ</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">সময়ের পর পোর্টাল স্বয়ংক্রিয়ভাবে বন্ধ হয়ে যাবে</td>
</tr>
<tr>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0; font-weight: 600;">ভুল কোর্সকোড ও ভুল এন্ট্রি সংশোধন</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0; color: #0f766e; font-weight: bold;">১২/১০/২০২৬ পর্যন্ত</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">কলেজ কর্তৃপক্ষ</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">কোর্সকোড ভুল থাকলে ফলাফল স্থগিত (Withheld) হতে পারে</td>
</tr>
<tr style="background: #f8fafc;">
<td style="padding: 12px 15px; border: 1px solid #e2e8f0; font-weight: 600;">Probable List-এ নাম অন্তর্ভুক্তি</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0; color: #dc2626; font-weight: bold;">ইনকোর্স এন্ট্রি সাপেক্ষে</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">জাতীয় বিশ্ববিদ্যালয় সার্ভার</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">নম্বর না থাকলে ফরম পূরণের সুযোগ থাকবে না</td>
</tr>
<tr>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0; font-weight: 600;">পূর্বের মূল স্মারক অনুসরণ</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0; color: #334155; font-weight: bold;">স্মারক ৫৮৮৪ (২২/০৭/২০২৬)</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">উভয় পক্ষ</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">অন্যান্য সার্বিক শর্তাবলি বহাল থাকবে</td>
</tr>
</tbody>
</table>
</div>

<h2 style="font-family: 'SolaimanLipi', sans-serif; color: #0f172a; font-size: 24px; font-weight: 700; margin: 40px 0 20px 0; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px;">
In-Course Marks Entry & Probable List Significance | ইনকোর্স নম্বর ও প্রবেবল লিস্টের গুরুত্ব
</h2>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16px; line-height: 1.85; color: #334155; margin-bottom: 20px;">
জাতীয় বিশ্ববিদ্যালয়ের ডিগ্রি (পাস) কোর্সের মূল্যায়নে ইনকোর্স পরীক্ষার ভূমিকা অত্যন্ত সংবেদনশীল। অধিকাংশ শিক্ষার্থী লিখিত পরীক্ষার দিকে বেশি নজর দিলেও ইনকোর্স নম্বরকে হালকাভাবে নেয়। তবে বিশ্ববিদ্যালয়ের অফিসিয়াল নিয়ম অনুযায়ী:
</p>

<div style="background: #fffbeb; border-left: 5px solid #d97706; padding: 20px 22px; border-radius: 0 10px 10px 0; margin: 25px 0; font-family: 'SolaimanLipi', sans-serif;">
<h4 style="margin: 0 0 10px 0; color: #92400e; font-size: 18px; font-weight: 700;">শিক্ষার্থী ও কলেজের জন্য ৩টি জরুরি সতর্কতা:</h4>
<ol style="margin: 0; padding-left: 20px; color: #78350f; line-height: 1.85; font-size: 15.5px;">
<li><strong>প্রবেবল লিস্টে নাম না আসার ঝুঁকি:</strong> যদি কোনো কলেজের কোনো শিক্ষার্থীর ইনকোর্স নম্বর ১২ অক্টোবর ২০২৬ তারিখের মধ্যে অনলাইন পোর্টালে সাবমিট না করা হয়, তবে জাতীয় বিশ্ববিদ্যালয়ের সার্ভার স্বয়ংক্রিয়ভাবে উক্ত শিক্ষার্থীর নাম ফরম পূরণের প্রবেবল লিস্ট থেকে বাদ দেবে। ফলে শিক্ষার্থী পরীক্ষায় অংশ নিতে পারবে না।</li>
<li><strong>কোর্সকোড যাচাই:</strong> ডিগ্রি ২য় বর্ষে আবশ্যিক বিষয়সহ বিভাগভিত্তিক নৈর্বাচনিক বিষয়ের কোড অত্যন্ত সতর্কতার সাথে মেলাতে হবে। বিশেষ করে ইংরেজি (আবশ্যিক) অথবা পরিবেশ বিজ্ঞানের ক্ষেত্রে কোডের গরমিল হলে ইনকোর্স নম্বর অন্য পত্রে যুক্ত হয়ে ফলাফল বিপন্ন হতে পারে।</li>
<li><strong>সংশোধনের চূড়ান্ত সুযোগ:</strong> পূর্বে কোনো কারণে ইনকোর্স নম্বর এন্ট্রিতে ভুল হলে বা কোনো পরীক্ষার্থীর নম্বর বাদ পড়লে এই বর্ধিত সময়সীমার মধ্যেই তা সংশোধনের শেষ সুযোগ।</li>
</ol>
</div>

<h2 style="font-family: 'SolaimanLipi', sans-serif; color: #0f172a; font-size: 24px; font-weight: 700; margin: 40px 0 20px 0; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px;">
Degree 2nd Year Marks Distribution & Grading | নম্বর বণ্টন ও পাস নম্বরের নিয়মাবলি
</h2>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16px; line-height: 1.85; color: #334155; margin-bottom: 20px;">
ডিগ্রি (পাস) ২য় বর্ষের প্রতিটি পত্রে ১০০ নম্বরের পরীক্ষা নেওয়া হয়। এই ১০০ নম্বরের বিভাজন নিম্নরূপভাবে পরিচালিত হয়:
</p>

<ul style="font-family: 'SolaimanLipi', sans-serif; font-size: 16px; line-height: 1.85; color: #334155; margin-bottom: 25px; padding-left: 22px;">
<li><strong>ইনকোর্স পরীক্ষা (২০ নম্বর):</strong> শ্রেণিকক্ষে উপস্থিতি, টিউটোরিয়াল টেস্ট, ক্লাস পারফরম্যান্স এবং অ্যাসাইনমেন্টের ওপর ভিত্তি করে কলেজ কর্তৃপক্ষ এই ২০ নম্বরের মূল্যায়ন করে। ইনকোর্স পরীক্ষায় পাস মার্ক ন্যূনতম ৮ নম্বর (৪০%)।</li>
<li><strong>তত্ত্বীয় চূড়ান্ত লিখিত পরীক্ষা (৮০ নম্বর):</strong> জাতীয় বিশ্ববিদ্যালয় কর্তৃক নির্ধারিত পরীক্ষা কেন্দ্রে ৩ ঘণ্টা বা সাড়ে ৩ ঘণ্টার লিখিত পরীক্ষা অনুষ্ঠিত হয়। লিখিত পরীক্ষায় পাস মার্ক ন্যূনতম ৩২ নম্বর (৪০%)।</li>
<li><strong>মোট পাস শর্ত:</strong> ইনকোর্স ও লিখিত পরীক্ষা উভয় অংশ মিলিয়ে পৃথকভাবে পাস করতে হয়। ইনকোর্সে অনুপস্থিত থাকলে বা ফেল করলে লিখিত পরীক্ষায় ভালো করলেও কোর্সটি ফেল (F Grade) হিসেবে গণ্য হবে।</li>
</ul>

<h2 style="font-family: 'SolaimanLipi', sans-serif; color: #0f172a; font-size: 24px; font-weight: 700; margin: 40px 0 20px 0; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px;">
Degree 2nd Year Faculty-Wise Groups & Courses | শাখাভিত্তিক বিষয়সমূহ
</h2>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16px; line-height: 1.85; color: #334155; margin-bottom: 20px;">
ডিগ্রি ২য় বর্ষে ৪টি প্রধান অনুষদের অধীনে শিক্ষার্থীরা পড়াশোনা করেন:
</p>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin: 25px 0; font-family: 'SolaimanLipi', sans-serif;">
<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-top: 4px solid #0284c7; padding: 18px 20px; border-radius: 8px;">
<h4 style="margin: 0 0 10px 0; color: #0369a1; font-size: 18px; font-weight: 700;">বিএ (BA - Bachelor of Arts)</h4>
<p style="margin: 0; color: #475569; font-size: 15px; line-height: 1.7;">বাংলা জাতীয় ভাষা, ইতিহাস, ইসলামের ইতিহাস ও সংস্কৃতি, দর্শন, ইসলামিক স্টাডিজ ও ইংরেজি সাহিত্যের মৌলিক পত্রসমূহ।</p>
</div>
<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-top: 4px solid #059669; padding: 18px 20px; border-radius: 8px;">
<h4 style="margin: 0 0 10px 0; color: #047857; font-size: 18px; font-weight: 700;">বিএসএস (BSS - Social Science)</h4>
<p style="margin: 0; color: #475569; font-size: 15px; line-height: 1.7;">রাষ্ট্রবিজ্ঞান, সমাজবিজ্ঞান, সমাজকর্ম, অর্থনীতি এবং নৃবিজ্ঞানের ২য় বর্ষের নির্ধারিত তত্ত্বীয় পত্রসমূহ।</p>
</div>
<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-top: 4px solid #d97706; padding: 18px 20px; border-radius: 8px;">
<h4 style="margin: 0 0 10px 0; color: #b45309; font-size: 18px; font-weight: 700;">বিবিএস (BBS - Business Studies)</h4>
<p style="margin: 0; color: #475569; font-size: 15px; line-height: 1.7;">হিসাববিজ্ঞান, ব্যবস্থাপনা, মার্কেটিং ও ফিন্যান্স অ্যান্ড ব্যাংকিং বিভাগের বাণিজ্যিক আইন ও আর্থিক ব্যবস্থাপনা পত্র।</p>
</div>
<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-top: 4px solid #7c3aed; padding: 18px 20px; border-radius: 8px;">
<h4 style="margin: 0 0 10px 0; color: #6d28d9; font-size: 18px; font-weight: 700;">বিএসসি (BSc - Physical & Life Science)</h4>
<p style="margin: 0; color: #475569; font-size: 15px; line-height: 1.7;">পদার্থবিজ্ঞান, রসায়ন, গণিত, উদ্ভিদবিজ্ঞান ও প্রাণিবিজ্ঞানের তত্ত্বীয় ও ব্যবহারিক কোর্সসমূহ।</p>
</div>
</div>

<h2 style="font-family: 'SolaimanLipi', sans-serif; color: #0f172a; font-size: 24px; font-weight: 700; margin: 40px 0 20px 0; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px;">
EMS Portal Online Entry Step-by-Step | কলেজ শিক্ষকদের জন্য অনলাইনে নম্বর এন্ট্রি নির্দেশিকা
</h2>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16px; line-height: 1.85; color: #334155; margin-bottom: 15px;">
জাতীয় বিশ্ববিদ্যালয়ের পরীক্ষা পরিচালনা সফটওয়্যার (EMS Portal)-এর মাধ্যমে কলেজগুলোকে নির্ভুলভাবে ইনকোর্স নম্বর প্রেরণ করতে হয়। এই প্রক্রিয়ায় যে ধাপগুলো অনুসরণ করা বাধ্যতামূলক:
</p>

<ol style="font-family: 'SolaimanLipi', sans-serif; font-size: 16px; line-height: 1.85; color: #334155; margin-bottom: 25px; padding-left: 22px;">
<li><strong>ইএমএস পোর্টালে লগইন:</strong> কলেজের নির্দিষ্ট ইউজার আইডি ও পাসওয়ার্ড ব্যবহার করে <a href="http://ems.nu.ac.bd" target="_blank" rel="noopener" style="color: #0f766e; text-decoration: underline;">ems.nu.ac.bd</a> লিংকে প্রবেশ করতে হবে।</li>
<li><strong>ইনকোর্স মার্কস এন্ট্রি মেনু নির্বাচন:</strong> ড্যাশবোর্ড থেকে Degree (Pass) 2nd Year অপশনে গিয়ে In-Course Marks Entry নির্বাচন করতে হবে।</li>
<li><strong>কোর্সকোড অনুযায়ী রোল নম্বর যাচাই:</strong> প্রতিটি কোর্সের রোল ও রেজিস্ট্রেশন তালিকার সাথে শিক্ষকের মূল ইনকোর্স মূল্যায়ন খাতা মিলিয়ে ২০ নম্বরের মধ্যে প্রাপ্ত নম্বর ইনপুট দিতে হবে।</li>
<li><strong>ড্রাফট ভেরিফিকেশন ও ফাইনাল সাবমিশন:</strong> একবারে ফাইনাল সাবমিট না করে প্রিন্ট ড্রাফট কপি বের করে বিভাগীয় প্রধান কর্তৃক স্বাক্ষর করিয়ে নিতে হবে। সব ঠিক থাকলে Final Submit বাটনে ক্লিক করে নিশ্চিত করতে হবে।</li>
<li><strong>হার্ডকপি সংরক্ষণ:</strong> ফাইনাল সাবমিশনের পর কম্পিউটার জেনারেটেড টপশিট ও মূল মার্কশিটের হার্ডকপি প্রিন্ট করে পরীক্ষা নিয়ন্ত্রণ দপ্তরে প্রেরণের জন্য প্রস্তুত রাখতে হবে।</li>
</ol>

<h2 style="font-family: 'SolaimanLipi', sans-serif; color: #0f172a; font-size: 24px; font-weight: 700; margin: 40px 0 20px 0; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px;">
NU Degree 2nd Year Compulsory English Passing Strategy | ইংরেজি আবশ্যিক পাসের গোল্ডেন রুলস
</h2>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16px; line-height: 1.85; color: #334155; margin-bottom: 20px;">
জাতীয় বিশ্ববিদ্যালয়ের ডিগ্রি ২য় বর্ষে সকল বিভাগের শিক্ষার্থীদের জন্য <strong>ইংরেজি (আবশ্যিক)</strong> একটি অত্যন্ত গুরুত্বপূর্ণ বিষয়। অধিকাংশ শিক্ষার্থী গ্রামার ও রাইটিং পার্টে ভুলের কারণে এই বিষয়ে কাঙ্ক্ষিত ফলাফল অর্জন করতে ব্যর্থ হয়। সহজে পাসের জন্য ৪টি কার্যকরী কৌশল:
</p>

<div style="background: #f0fdf4; border-left: 5px solid #16a34a; padding: 20px 22px; border-radius: 0 10px 10px 0; margin: 25px 0; font-family: 'SolaimanLipi', sans-serif;">
<h4 style="margin: 0 0 10px 0; color: #166534; font-size: 18px; font-weight: 700;">ইংরেজি আবশ্যিকে প্রথমবারে পাসের মূল পয়েন্টসমূহ:</h4>
<ul style="margin: 0; padding-left: 20px; color: #14532d; line-height: 1.85; font-size: 15.5px;">
<li><strong>Changing Sentences ও Voice Change:</strong> ব্যাকরণ অংশে এই দুটি টপিক থেকে শতভাগ কমন প্রশ্ন থাকে। বিগত ৫ বছরের প্রশ্ন ভালোভাবে রিভিশন দিলে সম্পূর্ণ নম্বর পাওয়া যায়।</li>
<li><strong>Right Form of Verbs ও Preposition:</strong> বোর্ড পরীক্ষায় ঘুরেফিরে একই নিয়মের প্রশ্ন বারবার রিপিট হয়। প্রতিদিন ২০টি করে নিয়ম অনুশীলন করুন।</li>
<li><strong>Writing অংশে ফরম্যাট রক্ষা করা:</strong> Application, Formal Letter, Paragraph ও Dialogue Writing-এ নির্ধারিত ফরম্যাট মেনে লিখলে ৫০% নম্বর নিশ্চিত থাকে।</li>
<li><strong>Comprehension উত্তর লেখার টেকনিক:</strong> প্যাসেজের মূল ভাব নিজের সহজ ভাষায় সংক্ষেপে লিখলে পরীক্ষক পূর্ণ নম্বর প্রদান করেন।</li>
</ul>
</div>

<h2 style="font-family: 'SolaimanLipi', sans-serif; color: #0f172a; font-size: 24px; font-weight: 700; margin: 40px 0 20px 0; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px;">
Step-by-Step Student Action Plan | শিক্ষার্থীদের জন্য করণীয় ৪টি পদক্ষেপ
</h2>

<div style="background: #f1f5f9; border-radius: 10px; padding: 22px; margin: 25px 0; font-family: 'SolaimanLipi', sans-serif;">
<ol style="margin: 0; padding-left: 20px; color: #334155; line-height: 1.9; font-size: 16px;">
<li><strong>কলেজের নোটিশ বোর্ডে ইনকোর্স মূল্যায়ন যাচাই:</strong> আপনার নিজ নিজ ডিপার্টমেন্টের নোটিশ বোর্ডে ইনকোর্স পরীক্ষার প্রাপ্ত নম্বর এবং কোর্সকোড টানানো হয়েছে কি না তা দ্রুত দেখে নিন।</li>
<li><strong>অনুপস্থিতি বা নম্বর ঘাটতি থাকলে শিক্ষকদের সাথে যোগাযোগ:</strong> যদি কোনো পত্রে ইনকোর্স পরীক্ষায় অংশ না নিয়ে থাকেন, তবে ১২ অক্টোবরের আগেই সংশ্লিষ্ট শিক্ষকের সাথে কথা বলে প্রয়োজনীয় আনুষ্ঠানিকতা সম্পন্ন করুন।</li>
<li><strong>রুটিন ও সিলেবাস অনুযায়ী রিভিশন:</strong> ইনকোর্স নম্বর এন্ট্রি সম্পন্ন হওয়ার পরপরই জাতীয় বিশ্ববিদ্যালয় চূড়ান্ত পরীক্ষার রুটিন প্রকাশ করবে। বিগত ৫ বছরের বোর্ড প্রশ্ন পর্যালোচনা করে প্রতিটি অধ্যায়ের নোট প্রস্তুত রাখুন।</li>
<li><strong>নিয়মিত অফিসিয়াল আপডেট পর্যবেক্ষণ:</strong> যে কোনো অননুমোদিত গুজবে কান না দিয়ে সরাসরি nu.ac.bd পোর্টাল এবং HelpTrickBD-এর শিক্ষা নোটিশ ফলো করুন।</li>
</ol>
</div>

<h2 style="font-family: 'SolaimanLipi', sans-serif; color: #0f172a; font-size: 24px; font-weight: 700; margin: 40px 0 20px 0; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px;">
NU Degree 2nd Year In-Course 2026 FAQ | সাধারণ প্রশ্ন ও উত্তর
</h2>

<div style="font-family: 'SolaimanLipi', sans-serif; margin: 25px 0;">

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px 20px; margin-bottom: 15px;">
<h4 style="margin: 0 0 8px 0; color: #0f172a; font-size: 17px; font-weight: 700;">প্রশ্ন ১: ইনকোর্স পরীক্ষার নম্বর অনলাইনে এন্ট্রির শেষ তারিখ কবে?</h4>
<p style="margin: 0; color: #475569; font-size: 15.5px; line-height: 1.75;">উত্তর: জাতীয় বিশ্ববিদ্যালয়ের সর্বশেষ স্মারক ৬০৬৯ অনুযায়ী, ইনকোর্স নম্বর অনলাইনে এন্ট্রি দেওয়ার বর্ধিত সময়সীমা ১২ অক্টোবর ২০২৬ তারিখ পর্যন্ত।</p>
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px 20px; margin-bottom: 15px;">
<h4 style="margin: 0 0 8px 0; color: #0f172a; font-size: 17px; font-weight: 700;">প্রশ্ন ২: ইনকোর্স নম্বর অনলাইনে এন্ট্রি না দিলে কি ফরম পূরণ করা যাবে?</h4>
<p style="margin: 0; color: #475569; font-size: 15.5px; line-height: 1.75;">উত্তর: না, বিজ্ঞপ্তিতে সুস্পষ্টভাবে বলা হয়েছে যে ইনকোর্স নম্বর অনলাইনে এন্ট্রি ব্যতীত কোনো পরীক্ষার্থীর নাম ফরম পূরণের Probable List-এ অন্তর্ভুক্ত হবে না।</p>
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px 20px; margin-bottom: 15px;">
<h4 style="margin: 0 0 8px 0; color: #0f172a; font-size: 17px; font-weight: 700;">প্রশ্ন ৩: পূর্বে ভুল কোর্সকোড বা ভুল নম্বর এন্ট্রি হলে তা কীভাবে সংশোধন করা যাবে?</h4>
<p style="margin: 0; color: #475569; font-size: 15.5px; line-height: 1.75;">উত্তর: সংশ্লিষ্ট কলেজ কর্তৃপক্ষ ১২ অক্টোবর ২০২৬ তারিখের মধ্যে ইএমএস (ems.nu.ac.bd) পোর্টালে লগইন করে ভুল কোর্সকোড এবং ভুল এন্ট্রি সংশোধন করতে পারবে।</p>
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px 20px; margin-bottom: 15px;">
<h4 style="margin: 0 0 8px 0; color: #0f172a; font-size: 17px; font-weight: 700;">প্রশ্ন ৪: ডিগ্রি ২য় বর্ষের ইনকোর্স পরীক্ষায় পাস মার্ক কত?</h4>
<p style="margin: 0; color: #475569; font-size: 15.5px; line-height: 1.75;">উত্তর: ২০ নম্বরের ইনকোর্স পরীক্ষায় ন্যূনতম পাস মার্ক ৮ নম্বর (৪০%)।</p>
</div>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px 20px; margin-bottom: 15px;">
<h4 style="margin: 0 0 8px 0; color: #0f172a; font-size: 17px; font-weight: 700;">প্রশ্ন ৫: ডিগ্রি ২য় বর্ষের লিখিত পরীক্ষা কবে নাগাদ শুরু হতে পারে?</h4>
<p style="margin: 0; color: #475569; font-size: 15.5px; line-height: 1.75;">উত্তর: ইনকোর্স নম্বর এন্ট্রি ও ফরম পূরণ প্রক্রিয়া সমাপ্তির পর আগামী নভেম্বর ২০২৬-এর মাঝামাঝি সময়ে তত্ত্বীয় লিখিত পরীক্ষা শুরুর জোরালো সম্ভাবনা রয়েছে।</p>
</div>

</div>

<!-- Author Attribution Box -->
<div class="htbd-author-box" style="display: flex; align-items: center; gap: 18px; margin: 35px 0 25px 0; padding: 18px 22px; background: #f8fafc; border: 1px solid #e2e8f0; border-left: 5px solid #0f766e; border-radius: 10px; font-family: 'SolaimanLipi', Arial, sans-serif;">
  <img src="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/author/faruk_sir.webp" 
       alt="ফারুক স্যার (মো. ওমর ফারুক)" 
       class="htbd-author-avatar" 
       width="75" height="75" 
       loading="lazy" 
       style="width: 75px !important; height: 75px !important; min-width: 75px !important; max-width: 75px !important; border-radius: 50% !important; object-fit: cover !important; border: 2px solid #0f766e !important; flex-shrink: 0 !important; display: block !important; margin: 0 !important; box-shadow: 0 2px 6px rgba(0,0,0,0.08) !important;" />
  <div class="htbd-author-info" style="flex: 1 1 auto; min-width: 0;">
    <h4 style="margin: 0 0 4px 0; color: #0f766e; font-size: 18px; font-weight: 700; line-height: 1.3;">ফারুক স্যার (মো. ওমর ফারুক)</h4>
    <div class="htbd-author-meta" style="font-size: 13px; color: #64748b; margin-bottom: 6px; font-weight: 600;">শিক্ষাবিদ ও অ্যাকাডেমিক গবেষক | প্রতিষ্ঠাতা, HelpTrickBD</div>
    <p class="htbd-author-bio" style="font-size: 14px; color: #334155; line-height: 1.6; margin: 0;">
      জাতীয় বিশ্ববিদ্যালয়ের স্নাতক ও ডিগ্রি পর্যায়ের পরীক্ষা প্রস্তুতি, রুটিন বিশ্লেষণ এবং শিক্ষা নোটিশে নির্ভরযোগ্য তথ্য উপস্থাপনে এক দশকের শিক্ষকতার বাস্তব অভিজ্ঞতাসম্পন্ন একজন মেন্টর।
    </p>
  </div>
</div>

<!-- BlogPosting JSON-LD Schema -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "জাতীয় বিশ্ববিদ্যালয় ডিগ্রি ২য় বর্ষ ইনকোর্স নম্বর এন্ট্রি ও পরীক্ষার গাইড ২০২৬ | NU Degree 2nd Year In-Course & Exam Routine",
  "description": "জাতীয় বিশ্ববিদ্যালয় ডিগ্রি ২য় বর্ষ ইনকোর্স নম্বর অনলাইনে এন্ট্রির বর্ধিত সময়সূচি ২০২৬। প্রবেবল লিস্টের নিয়মাবলী, বিষয় কোড ও পরীক্ষার পূর্ণাঙ্গ গাইডলাইন।",
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
  "datePublished": "2026-10-02T02:00:00+06:00",
  "dateModified": "2026-10-02T02:00:00+06:00"
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
      "name": "ইনকোর্স পরীক্ষার নম্বর অনলাইনে এন্ট্রির শেষ তারিখ কবে?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "জাতীয় বিশ্ববিদ্যালয়ের সর্বশেষ স্মারক ৬০৬৯ অনুযায়ী, ইনকোর্স নম্বর অনলাইনে এন্ট্রি দেওয়ার বর্ধিত সময়সীমা ১২ অক্টোবর ২০২৬ তারিখ পর্যন্ত।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "ইনকোর্স নম্বর অনলাইনে এন্ট্রি না দিলে কি ফরম পূরণ করা যাবে?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "না, বিজ্ঞপ্তিতে বলা হয়েছে ইনকোর্স নম্বর অনলাইনে এন্ট্রি ব্যতীত কোনো পরীক্ষার্থীর নাম ফরম পূরণের Probable List-এ অন্তর্ভুক্ত হবে না।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "পূর্বে ভুল কোর্সকোড বা ভুল নম্বর এন্ট্রি হলে তা কীভাবে সংশোধন করা যাবে?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "সংশ্লিষ্ট কলেজ কর্তৃপক্ষ ১২ অক্টোবর ২০২৬ তারিখের মধ্যে ইএমএস পোর্টালে লগইন করে ভুল কোর্সকোড এবং ভুল এন্ট্রি সংশোধন করতে পারবে।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "ডিগ্রি ২য় বর্ষের ইনকোর্স পরীক্ষায় পাস মার্ক কত?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "২০ নম্বরের ইনকোর্স পরীক্ষায় ন্যূনতম পাস মার্ক ৮ নম্বর (৪০%)।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "ডিগ্রি ২য় বর্ষের লিখিত পরীক্ষা কবে নাগাদ শুরু হতে পারে?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "ইনকোর্স নম্বর এন্ট্রি ও ফরম পূরণ সম্পন্ন হওয়ার পর নভেম্বর ২০২৬-এর মাঝামাঝি সময়ে তত্ত্বীয় লিখিত পরীক্ষা শুরুর সম্ভাবনা রয়েছে।"
      }}
    }}
  ]
}}
</script>"""

    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(full_html)

    word_count = len(full_html.split())

    meta_data = {
        "title": "জাতীয় বিশ্ববিদ্যালয় ডিগ্রি ২য় বর্ষ ইনকোর্স নম্বর এন্ট্রি ও পরীক্ষার গাইড ২০২৬ | NU Degree 2nd Year In-Course & Exam Routine",
        "permalink": "nu-degree-2nd-year-in-course-and-exam-routine-2026",
        "labels": ["ডিগ্রি পাস", "জাতীয় বিশ্ববিদ্যালয়", "এডুকেশন নোটিশ"],
        "post_id": "",
        "status": "DRAFT",
        "search_description": "জাতীয় বিশ্ববিদ্যালয় ডিগ্রি ২য় বর্ষ ইনকোর্স নম্বর এন্ট্রি বর্ধিত সময়সূচি ২০২৬। প্রবেবল লিস্টের নিয়ম, বিষয় কোড ও পরীক্ষার পূর্ণাঙ্গ গাইড।",
        "word_count": word_count
    }

    with open(OUTPUT_META, "w", encoding="utf-8") as f:
        json.dump(meta_data, f, ensure_ascii=False, indent=2)

    print(f"[SUCCESS] Master post generated: {OUTPUT_HTML}")
    print(f"          Word count: ~{word_count} words")
    print(f"          Metadata: {OUTPUT_META}")
    return True


if __name__ == "__main__":
    generate_master_post()
