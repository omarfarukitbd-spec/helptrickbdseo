#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
output_posts/generate_nu_honours_promotion_post.py
---------------------------------------------------
Generates the authoritative master article for:
জাতীয় বিশ্ববিদ্যালয় অনার্স ২য় বর্ষ পরীক্ষার গাইড ও ৩য় বর্ষে প্রমোশনের নিয়মাবলী ২০২৬
NU Honours 2nd Year Exam Guidelines, Pass Marks & Promotion Rules to 3rd Year.

Conforms to:
- Rule 01 (Content Standards: 1,500+ words, SolaimanLipi, Faruk Sir E-E-A-T card, Dual Schemas).
- Rule 02 (Asset Standards: 16:9 WebP banner).
- Rule 12 (Strictly Zero Emojis).
- Byte-0 Hero Placement & <!--more--> jump break.
"""

import os
import sys
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUTPUT_HTML = os.path.join(PROJECT_ROOT, "output_posts", "nu-honours-2nd-year-exam-guide-and-promotion-rules-2026.html")
OUTPUT_META = os.path.join(PROJECT_ROOT, "output_posts", "nu-honours-2nd-year-exam-guide-and-promotion-rules-2026_meta.json")

HERO_BANNER = "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/nu_honours_2nd_year_promotion_rules_2026.webp"

def generate_post_html():
    return f"""<figure style="margin: 0 0 25px 0; text-align: center;">
<img src="{HERO_BANNER}" alt="জাতীয় বিশ্ববিদ্যালয় অনার্স ২য় বর্ষ পরীক্ষার গাইড ও প্রমোশনের নিয়মাবলী ২০২৬" title="NU Honours 2nd Year Exam Guidelines and Promotion Rules 2026" width="1200" height="675" style="max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); display: block; margin: 0 auto;" loading="eager" />
<figcaption style="font-family: 'SolaimanLipi', Arial, sans-serif; font-size: 14px; color: #64748b; margin-top: 10px; font-weight: 500;">
ছবি: জাতীয় বিশ্ববিদ্যালয় অনার্স ২য় বর্ষ পরীক্ষা ও ৩য় বর্ষে প্রমোশনের অফিসিয়াল নীতিমালা রূপরেখা
</figcaption>
</figure>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 17px; line-height: 1.85; color: #1e293b; margin-bottom: 20px;">
জাতীয় বিশ্ববিদ্যালয়ের অনার্স ২য় বর্ষের চূড়ান্ত পরীক্ষা সারা দেশে অত্যন্ত গুরুত্বের সাথে অনুষ্ঠিত হচ্ছে। ডিগ্রি অর্জনের চার বছর মেয়াদি স্নাতক যাত্রায় ২য় বর্ষ হলো একটি অত্যন্ত সংবেদনশীল পর্যায়। কারণ ১ম বর্ষের ধাক্কা কাটিয়ে উঠে ২য় বর্ষে ভালো সিজিপিএ (CGPA) ধরে রাখা এবং ৩য় বর্ষে নিরাপদে উত্তীর্ণ হওয়া প্রতিটি শিক্ষার্থীর জন্য অপরিহার্য। তবে অনেক শিক্ষার্থীই জাতীয় বিশ্ববিদ্যালয়ের অফিসিয়াল প্রমোশন নীতিমালা, ন্যূনতম পাস মার্ক, ইনকোর্স ও ব্যবহারিক নম্বরের প্রভাব এবং নন-ক্রেডিট ইংরেজি আবশ্যিক বিষয়ের শর্তাবলি পরিষ্কারভাবে না জানার কারণে নানা রকম দুশ্চিন্তায় পড়েন। নিচে জাতীয় বিশ্ববিদ্যালয়ের অফিসিয়াল রেগুলেশন অনুযায়ী অনার্স ২য় বর্ষের পরীক্ষা গাইড, গ্রেডিং পদ্ধতি এবং ৩য় বর্ষে প্রমোশনের চূড়ান্ত নিয়মাবলী বিস্তারিত তুলে ধরা হলো।
</p>

<!-- Quick Overview Callout Box -->
<div style="background: #eff6ff; border-left: 5px solid #2563eb; border-radius: 8px; padding: 20px 24px; margin: 25px 0; font-family: 'SolaimanLipi', sans-serif;">
<h3 style="margin: 0 0 10px 0; color: #1e3a8a; font-size: 19px; font-weight: 700;">৩য় বর্ষে প্রমোশনের গোল্ডেন রুলস একনজরে | Quick Promotion Summary</h3>
<p style="margin: 0; color: #1e293b; font-size: 16px; line-height: 1.85;">
অনার্স ২য় বর্ষ থেকে ৩য় বর্ষে উন্নীত হতে হলে শিক্ষার্থীকে দুটি মৌলিক শর্ত পূরণ করতে হবে: <strong>১. সকল বিষয়ের মধ্যে কমপক্ষে ৩টি প্রধান তাত্ত্বিক কোর্সে ন্যূনতম 'D' গ্রেড (৪০% নম্বর) পেয়ে পাস করতে হবে।</strong> এবং <strong>২. সার্বিকভাবে সর্বনিম্ন সিজিপিএ ২.০০ (CGPA 2.00) অর্জন করতে হবে।</strong> এছাড়া নন-ক্রেডিট আবশ্যিক ইংরেজিতে ফেল করলেও প্রমোশন হবে, তবে ডিগ্রি শেষ করার আগে অবশ্যই পাস করতে হবে।
</p>
<div style="margin-top: 12px; font-size: 14.5px; color: #1d4ed8; font-weight: 600;">
অফিসিয়াল তথ্যসূত্র: জাতীয় বিশ্ববিদ্যালয় পরীক্ষা নিয়ন্ত্রণ দপ্তর ও স্নাতক (সম্মান) রেগুলেশন অনুযায়ী প্রস্তুতকৃত
</div>
</div>

<!--more-->

<h2 style="font-family: 'SolaimanLipi', sans-serif; color: #0c2340; font-size: 24px; font-weight: 700; margin: 40px 0 18px 0; border-left: 5px solid #1e3a8a; padding-left: 14px;">
৩য় বর্ষে প্রমোশন পাওয়ার অফিসিয়াল নীতিমালা ও শর্তাবলী | Promotion Rules to 3rd Year
</h2>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16.5px; line-height: 1.85; color: #334155; margin-bottom: 20px;">
জাতীয় বিশ্ববিদ্যালয়ের স্নাতক (সম্মান) পরীক্ষার প্রমোশন নীতিমালা অত্যন্ত সুনির্দিষ্ট। জাতীয় বিশ্ববিদ্যালয়ের পরীক্ষা অধ্যাদেশ অনুযায়ী একজন শিক্ষার্থীকে পরবর্তী বর্ষে উত্তীর্ণ হতে হলে নিচের শর্তগুলো সতর্কতার সাথে পূরণ করতে হয়:
</p>

<div style="overflow-x: auto; margin: 25px 0;">
<table style="width: 100%; border-collapse: collapse; font-family: 'SolaimanLipi', sans-serif; font-size: 15.5px; text-align: left; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
<thead>
<tr style="background: #0c2340; color: #ffffff;">
<th style="padding: 14px 16px; border: 1px solid #1e3a8a;">শর্তের নাম</th>
<th style="padding: 14px 16px; border: 1px solid #1e3a8a;">অফিসিয়াল প্রয়োজনীয়তা</th>
<th style="padding: 14px 16px; border: 1px solid #1e3a8a;">ব্যাখ্যা ও শিক্ষার্থীর করণীয়</th>
</tr>
</thead>
<tbody>
<tr style="background: #f8fafc;">
<td style="padding: 12px 16px; border: 1px solid #e2e8f0; font-weight: 700; color: #0f172a;">১. ন্যূনতম পাস কোর্স</td>
<td style="padding: 12px 16px; border: 1px solid #e2e8f0; font-weight: bold; color: #16a34a;">কমপক্ষে ৩টি তাত্ত্বিক কোর্সে পাস</td>
<td style="padding: 12px 16px; border: 1px solid #e2e8f0;">যেসব বিষয়ে ক্রেডিট রয়েছে, তার মধ্যে অন্তত ৩টিতে 'D' গ্রেড (৪০ বা তদূর্ধ্ব নম্বর) পেতে হবে।</td>
</tr>
<tr>
<td style="padding: 12px 16px; border: 1px solid #e2e8f0; font-weight: 700; color: #0f172a;">২. ন্যূনতম সিজিপিএ (CGPA)</td>
<td style="padding: 12px 16px; border: 1px solid #e2e8f0; font-weight: bold; color: #16a34a;">সর্বনিম্ন ২.০০ (CGPA 2.00)</td>
<td style="padding: 12px 16px; border: 1px solid #e2e8f0;">সব ক্রেডিট কোর্সের গ্রেড পয়েন্ট গড় ২.০০ বা তার বেশি হতে হবে।</td>
</tr>
<tr style="background: #f8fafc;">
<td style="padding: 12px 16px; border: 1px solid #e2e8f0; font-weight: 700; color: #0f172a;">৩. এফ (F) গ্রেড সংক্রান্ত শর্ত</td>
<td style="padding: 12px 16px; border: 1px solid #e2e8f0; color: #dc2626; font-weight: bold;">F গ্রেড থাকলেও প্রমোশন সম্ভব</td>
<td style="padding: 12px 16px; border: 1px solid #e2e8f0;">যদি ৩টি বিষয়ে পাস ও CGPA ২.০০ থাকে, তবে F পেলেও ৩য় বর্ষে ওঠা যাবে। তবে পরবর্তী শিক্ষাবর্ষে ওই কোর্সে মানোন্নয়ন পরীক্ষা দিয়ে পাস করতে হবে।</td>
</tr>
<tr>
<td style="padding: 12px 16px; border: 1px solid #e2e8f0; font-weight: 700; color: #0f172a;">৪. নট-প্রমোটেড (Not Promoted) অবস্থা</td>
<td style="padding: 12px 16px; border: 1px solid #e2e8f0; color: #b91c1c; font-weight: bold;">৩টির কম পাস অথবা CGPA ২.০০ এর নিচে</td>
<td style="padding: 12px 16px; border: 1px solid #e2e8f0;">কোনো শিক্ষার্থী যদি ২টি বা তার কম বিষয়ে পাস করে, কিংবা ৩টিতে পাস করেও মোট CGPA ২.০০ এর নিচে থাকে, তবে সে নট-প্রমোটেড হবে এবং একই বর্ষে অনিয়মিত হিসেবে পরীক্ষা দিতে হবে।</td>
</tr>
<tr style="background: #f0fdf4;">
<td style="padding: 12px 16px; border: 1px solid #e2e8f0; font-weight: 700; color: #166534;">৫. ইংরেজি আবশ্যিক (Non-Credit)</td>
<td style="padding: 12px 16px; border: 1px solid #e2e8f0; font-weight: bold; color: #166534;">ন্যূনতম ৩৩ পেয়ে পাস করতে হবে</td>
<td style="padding: 12px 16px; border: 1px solid #e2e8f0;">এতে ফেল করলে ৩য় বর্ষে প্রমোশন আটকাবে না, তবে ডিগ্রি সমাপ্তির আগেই পাস করা বাধ্যতামূলক।</td>
</tr>
</tbody>
</table>
</div>

<h2 style="font-family: 'SolaimanLipi', sans-serif; color: #0c2340; font-size: 24px; font-weight: 700; margin: 40px 0 18px 0; border-left: 5px solid #1e3a8a; padding-left: 14px;">
ইংরেজি আবশ্যিক (English Compulsory — বিষয়কোড: 221109) পাসের গোল্ডেন গাইড
</h2>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16.5px; line-height: 1.85; color: #334155; margin-bottom: 20px;">
অনার্স ২য় বর্ষে সকল বিভাগের (ব্যবসায় শিক্ষা, কলা, সমাজবিজ্ঞান ও বিজ্ঞান অনুষদ) শিক্ষার্থীদের জন্য ১০০ নম্বরের ইংরেজি আবশ্যিক পরীক্ষা নেওয়া হয়। এটি একটি <strong>নন-ক্রেডিট (Non-Credit)</strong> বিষয়। এই বিষয়টির বিশেষত্ব এবং পাসের কৌশলগুলো নিচে তুলে ধরা হলো:
</p>

<div style="background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 10px; padding: 22px 26px; margin: 25px 0; font-family: 'SolaimanLipi', sans-serif;">
<h3 style="margin-top: 0; color: #9d174d; font-size: 20px; font-weight: 700; margin-bottom: 12px;">আবশ্যিক ইংরেজি বিষয়ে শিক্ষার্থীদের বহুল বিভ্রান্তি নিরসন</h3>
<ul style="margin: 0; padding-left: 20px; color: #831843; line-height: 1.9; font-size: 16px;">
<li><strong>নম্বর কি সিজিপিএ-তে যুক্ত হয়?</strong> না। এই বিষয়ে প্রাপ্ত নম্বর মোট জিপিএ বা সিজিপিএ-তে যুক্ত হয় না। তাই এতে ৮০ পেলেও যেমন সিজিপিএ বাড়বে না, তেমনি ৪০ পেলেও সিজিপিএ কমবে না।</li>
<li><strong>পাস নম্বর কত?</strong> ১০০ নম্বরের লিখিত পরীক্ষায় ন্যূনতম ৩৩ নম্বর পেলেই পাস হিসেবে গণ্য হবে।</li>
<li><strong>ফেল করলে কি ৩য় বর্ষে ওঠা যাবে?</strong> হ্যাঁ, অন্যান্য শর্ত পূরণ থাকলে আপনি ৩য় বর্ষে ভর্তি হতে পারবেন। তবে সার্টিফিকেট পেতে হলে ৪র্থ বর্ষ শেষ হওয়ার পূর্বে যেকোনো সেশনে পরীক্ষা দিয়ে পাস করতেই হবে।</li>
<li><strong>সহজে পাসের টেকনিক:</strong> গ্রামার অংশে রাইট ফর্ম অফ ভার্বস, ডব্লিউএইচ কোশ্চেনস, রি-অ্যারেঞ্জ এবং রাইটিং অংশে অ্যাপ্লিকেশন, প্যারাগ্রাফ ও নোটিসের ফরম্যাট ঠিক রেখে লিখলে অনায়াসেই ৫০-৬০ নম্বর তোলা সম্ভব।</li>
</ul>
</div>

<h2 style="font-family: 'SolaimanLipi', sans-serif; color: #0c2340; font-size: 24px; font-weight: 700; margin: 40px 0 18px 0; border-left: 5px solid #1e3a8a; padding-left: 14px;">
জাতীয় বিশ্ববিদ্যালয় গ্রেডিং স্কেল ও পয়েন্ট হিসাব করার সহজ ছক | NU Grading Scale
</h2>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16.5px; line-height: 1.85; color: #334155; margin-bottom: 20px;">
জাতীয় বিশ্ববিদ্যালয়ের ডিগ্রি ও অনার্স পর্যায়ে গ্রেডিং পদ্ধতি ইউজিসির সমন্বিত ইউনিফর্ম স্কেল অনুযায়ী নির্ধারিত। তত্ত্বীয় লিখিত পরীক্ষা (৮০ নম্বর) এবং ইনকোর্স/উপস্থিতি (২০ নম্বর) সমন্বয়ে মোট ১০০ নম্বরের ওপর গ্রেড পয়েন্ট নির্ধারিত হয়:
</p>

<div style="overflow-x: auto; margin: 25px 0;">
<table style="width: 100%; border-collapse: collapse; font-family: 'SolaimanLipi', sans-serif; font-size: 15px; text-align: center; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px;">
<thead>
<tr style="background: #0f172a; color: #ffffff;">
<th style="padding: 12px 14px; border: 1px solid #334155;">নম্বর সীমা (Marks Range)</th>
<th style="padding: 12px 14px; border: 1px solid #334155;">লেটার গ্রেড (Letter Grade)</th>
<th style="padding: 12px 14px; border: 1px solid #334155;">গ্রেড পয়েন্ট (Grade Point - GP)</th>
<th style="padding: 12px 14px; border: 1px solid #334155;">গুণগত মান ও পারফরম্যান্স</th>
</tr>
</thead>
<tbody>
<tr style="background: #f0fdf4;">
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; font-weight: bold;">৮০% বা তদূর্ধ্ব</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; font-weight: bold; color: #15803d;">A+ (এ প্লাস)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; font-weight: bold; color: #15803d;">৪.০০ (4.00)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; color: #15803d;">অসাধারণ (Outstanding)</td>
</tr>
<tr>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; font-weight: 600;">৭৫% থেকে ৭৯%</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; font-weight: 600; color: #0284c7;">A (এ)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; font-weight: 600; color: #0284c7;">৩.৭৫ (3.75)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0;">খুবই উত্তম (Excellent)</td>
</tr>
<tr style="background: #f8fafc;">
<td style="padding: 10px 14px; border: 1px solid #e2e8f0;">৭০% থেকে ৭৪%</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; color: #0369a1;">A- (এ মাইনাস)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; color: #0369a1;">৩.৫০ (3.50)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0;">উত্তম (Very Good)</td>
</tr>
<tr>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0;">৬৫% থেকে ৬৯%</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; color: #2563eb;">B+ (বি প্লাস)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; color: #2563eb;">৩.২৫ (3.25)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0;">ভালো (Good)</td>
</tr>
<tr style="background: #f8fafc;">
<td style="padding: 10px 14px; border: 1px solid #e2e8f0;">৬০% থেকে ৬৪%</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; color: #0891b2;">B (বি)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; color: #0891b2;">৩.০০ (3.00)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0;">সন্তোষজনক (Satisfactory)</td>
</tr>
<tr>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0;">৫৫% থেকে ৫৯%</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; color: #d97706;">B- (বি মাইনাস)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; color: #d97706;">২.৭৫ (2.75)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0;">চলনসই (Above Average)</td>
</tr>
<tr style="background: #f8fafc;">
<td style="padding: 10px 14px; border: 1px solid #e2e8f0;">৫০% থেকে ৫৪%</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; color: #b45309;">C+ (সি প্লাস)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; color: #b45309;">২.৫০ (2.50)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0;">গড়পড়তা (Average)</td>
</tr>
<tr>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0;">৪৫% থেকে ৪৯%</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; color: #c2410c;">C (সি)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; color: #c2410c;">২.২৫ (2.25)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0;">প্রান্তিক গড় (Below Average)</td>
</tr>
<tr style="background: #fefce8;">
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; font-weight: 600;">৪০% থেকে ৪৪%</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; font-weight: 600; color: #ca8a04;">D (ডি)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; font-weight: 600; color: #ca8a04;">২.০০ (2.00)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0;">পাস গ্রেড (Pass)</td>
</tr>
<tr style="background: #fef2f2;">
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; font-weight: bold; color: #b91c1c;">৪০% এর কম (০ – ৩৯)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; font-weight: bold; color: #b91c1c;">F (এফ)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; font-weight: bold; color: #b91c1c;">০.০০ (0.00)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; color: #b91c1c;">অকৃতকার্য (Fail)</td>
</tr>
</tbody>
</table>
</div>

<h2 style="font-family: 'SolaimanLipi', sans-serif; color: #0c2340; font-size: 24px; font-weight: 700; margin: 40px 0 18px 0; border-left: 5px solid #1e3a8a; padding-left: 14px;">
গ্রেড উন্নয়ন (Improvement) পরীক্ষা দেওয়ার নিয়মাবলী | Improvement Guidelines
</h2>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16.5px; line-height: 1.85; color: #334155; margin-bottom: 20px;">
অনার্স ২য় বর্ষে কাঙ্ক্ষিত ফলাফল অর্জন করতে না পারলে বা কোনো বিষয়ে আশানুরূপ গ্রেড না আসলে জাতীয় বিশ্ববিদ্যালয় শিক্ষার্থীদের জন্য মানোন্নয়নের সুযোগ দেয়:
</p>

<ul style="font-family: 'SolaimanLipi', sans-serif; font-size: 16px; line-height: 1.9; color: #334155; margin-bottom: 25px; padding-left: 22px;">
<li><strong>কোন কোন গ্রেডে ইমপ্রুভমেন্ট দেওয়া যায়?</strong> কোনো বিষয়ে যদি আপনার ফলাফল <strong>C, D অথবা F</strong> গ্রেড আসে, কেবল সেই বিষয়গুলোতেই আপনি পরবর্তী শিক্ষাবর্ষের নিয়মিত শিক্ষার্থীদের সাথে মানোন্নয়ন পরীক্ষা দিতে পারবেন। B বা তার ওপরের গ্রেডে ইমপ্রুভমেন্ট দেওয়া যায় না।</li>
<li><strong>সর্বোচ্চ কত গ্রেড পাওয়া সম্ভব?</strong> গ্রেড উন্নয়ন পরীক্ষায় অংশ নিয়ে আপনি যত ভালো নম্বরই পান না কেন, জাতীয় বিশ্ববিদ্যালয়ের নিয়ম অনুযায়ী আপনার অর্জিত সর্বোচ্চ গ্রেড হবে <strong>B+ (বি প্লাস / ৩.২৫ গ্রেড পয়েন্ট)</strong>।</li>
<li><strong>যদি পূর্বের চেয়ে কম নম্বর আসে?</strong> ইমপ্রুভমেন্ট পরীক্ষায় যদি পূর্ববর্তী নম্বরের চেয়ে কম নম্বর আসে, তবে বিশ্ববিদ্যালয় কর্তৃপক্ষ আপনার দুটি ফলের মধ্যে যেটি সর্বোচ্চ, সেটিই চূড়ান্তভাবে সংরক্ষণ করবে। অর্থাৎ এতে আগের ভালো গ্রেড হারানোর কোনো ঝুঁকি থাকে না।</li>
</ul>

<h2 style="font-family: 'SolaimanLipi', sans-serif; color: #0c2340; font-size: 24px; font-weight: 700; margin: 40px 0 18px 0; border-left: 5px solid #1e3a8a; padding-left: 14px;">
পরীক্ষার হলের ৪ ঘণ্টার সময় ব্যবস্থাপনা ও খাতা উপস্থাপনা | Exam Hall Strategy
</h2>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16.5px; line-height: 1.85; color: #334155; margin-bottom: 20px;">
অনার্স ২য় বর্ষের ৮০ নম্বরের তত্ত্বীয় পরীক্ষার জন্য ৪ ঘণ্টা সময় বরাদ্দ থাকে। দীর্ঘ এই সময়ে যথাযথ পরিকল্পনা মেনে না লিখলে অনেকেরই শেষ মুহূর্তে সময় সংকট তৈরি হয়:
</p>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 22px 26px; margin: 25px 0; font-family: 'SolaimanLipi', sans-serif;">
<h3 style="margin-top: 0; color: #1e3a8a; font-size: 20px; font-weight: 700; margin-bottom: 12px;">৩টি বিভাগের সময় ও উত্তর বণ্টনের আদর্শ ফর্মুলা</h3>
<ul style="margin: 0; padding-left: 20px; color: #334155; line-height: 1.9; font-size: 15.5px;">
<li><strong>ক-বিভাগ (অতি সংক্ষিপ্ত প্রশ্ন — ১০ নম্বর):</strong> ১২টি প্রশ্ন থেকে ১০টি প্রশ্নের উত্তর দিতে হবে (১০ × ১ = ১০)। এর জন্য সর্বোচ্চ <strong>২০ মিনিট</strong> সময় বরাদ্দ রাখুন। এক বা দুই লাইনে টু-দ্য-পয়েন্ট উত্তর লিখুন।</li>
<li><strong>খ-বিভাগ (সংক্ষিপ্ত প্রশ্ন — ২০ নম্বর):</strong> ৮টি প্রশ্ন থেকে যেকোনো ৫টি প্রশ্নের উত্তর দিতে হবে (৫ × ৪ = ২০)। প্রতিটি প্রশ্নের জন্য গড়ে <strong>১২ থেকে ১৫ মিনিট</strong> ব্যয় করুন (মোট ৬০–৭৫ মিনিট)। পয়েন্টভিত্তিক পরিষ্কার উত্তর উপস্থাপন করুন।</li>
<li><strong>গ-বিভাগ (রচনামূলক বা বর্ণনামূলক প্রশ্ন — ৫০ নম্বর):</strong> ৮টি বড় প্রশ্ন থেকে যেকোনো ৫টি প্রশ্নের উত্তর দিতে হবে (৫ × ১০ = ৫০)। এটিই আপনার জিপিএ নির্ধারণ করবে। প্রতিটি উত্তরের জন্য <strong>২৫ থেকে ২৮ মিনিট</strong> সময় রাখুন (মোট ১২৫–১৪০ মিনিট)। প্রাসঙ্গিক সাব-হেডিং, উক্তি ও চিত্র ব্যবহার করুন।</li>
<li><strong>রিভিশন ও ওএমআর চেক:</strong> পরীক্ষার শেষ <strong>১৫ মিনিট</strong> অবশ্যই অতিরিক্ত পৃষ্ঠা নম্বর মেলানো, মার্জিন ঠিক রাখা এবং ওএমআর শিটের রোল ও রেজিস্ট্রেশন নম্বর পুনর্যাচাইয়ের জন্য সংরক্ষণ করুন।</li>
</ul>
</div>

<h2 style="font-family: 'SolaimanLipi', sans-serif; color: #0c2340; font-size: 24px; font-weight: 700; margin: 40px 0 18px 0; border-left: 5px solid #1e3a8a; padding-left: 14px;">
সকল বিভাগের রুটিন ও অফিসিয়াল তথ্যসূত্র | Routine & Official Portal
</h2>

<div style="background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 10px; padding: 22px 26px; margin: 25px 0; font-family: 'SolaimanLipi', sans-serif;">
<div style="font-weight: 700; color: #0f172a; font-size: 17px; margin-bottom: 12px;">
অনার্স ২য় বর্ষের জরুরি লিংক ও অফিসিয়াল পোর্টাল:
</div>
<ul style="margin: 0; padding-left: 20px; line-height: 2.0; font-size: 15.5px; color: #1e293b;">
<li style="margin-bottom: 8px;">
<strong>অনার্স ২য় বর্ষ পরীক্ষার পূর্ণাঙ্গ রুটিন ও বিষয়কোড কার্ড:</strong><br/>
<a href="https://www.helptrickbd.com/2026/10/nu-honours-2nd-year-exam-routine-2026.html" style="color: #1e40af; text-decoration: underline; font-weight: 700;">সকল বিভাগের বিষয়ভিত্তিক রুটিন ও কোড দেখতে এখানে ক্লিক করুন [Helptrickbd Live Guide]</a>
</li>
<li style="margin-bottom: 8px;">
<strong>জাতীয় বিশ্ববিদ্যালয় কেন্দ্রীয় ওয়েবসাইট নোটিশ বোর্ড:</strong><br/>
<a href="https://www.nu.ac.bd/" target="_blank" rel="noopener noreferrer" style="color: #1e40af; text-decoration: underline; font-weight: 600;">nu.ac.bd (অফিসিয়াল নোটিশ বোর্ড ও কেন্দ্র তালিকা)</a>
</li>
<li>
<strong>পরীক্ষা ডিজিটালাইজেশন বিষয়ক হালনাগাদ প্রজ্ঞাপন:</strong> আমাদের প্রকাশিত <a href="https://www.helptrickbd.com/2026/10/nu-exam-digitization-aqa-global-mou-2026.html" style="color: #1e40af; text-decoration: underline; font-weight: 600;">জাতীয় বিশ্ববিদ্যালয়ের পরীক্ষা ডিজিটালাইজেশন ও একিউএ গ্লোবাল চুক্তি গাইড</a> বিস্তারিত পড়ে নিতে পারেন।
</li>
</ul>
</div>

<h2 style="font-family: 'SolaimanLipi', sans-serif; color: #0c2340; font-size: 24px; font-weight: 700; margin: 40px 0 18px 0; border-left: 5px solid #1e3a8a; padding-left: 14px;">
শিক্ষার্থীদের সর্বাধিক জিজ্ঞাসিত প্রশ্ন ও উত্তর (FAQ) | Frequently Asked Questions
</h2>

<details style="margin: 14px 0; padding: 16px 20px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; font-family: 'SolaimanLipi', Arial, sans-serif; cursor: pointer; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
<summary style="font-weight: 700; color: #1e3a8a; font-size: 17px; outline: none;">
প্রশ্ন ১: অনার্স ২য় বর্ষে ৩টি বিষয়ে পাস করলে কিন্তু CGPA ২.০০ এর নিচে আসলে কি প্রমোশন হবে?
</summary>
<div style="margin-top: 12px; padding-top: 10px; border-top: 1px dashed #cbd5e1; color: #334155; font-size: 15.5px; line-height: 1.8;">
উত্তর: না। প্রমোশন পাওয়ার জন্য দুটি শর্তই একসাথে পূরণ হতে হবে—কমপক্ষে ৩টি কোর্সে পাস এবং মোট CGPA ন্যূনতম ২.০০। যদি CGPA ১.৯৯ ও আসে, তবে ফলাফল 'নট-প্রমোটেড' (Not Promoted) হিসেবে আসবে এবং শিক্ষার্থী ৩য় বর্ষে ভর্তি হতে পারবে না।
</div>
</details>

<details style="margin: 14px 0; padding: 16px 20px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; font-family: 'SolaimanLipi', Arial, sans-serif; cursor: pointer; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
<summary style="font-weight: 700; color: #1e3a8a; font-size: 17px; outline: none;">
প্রশ্ন ২: একটি বিষয়ে এফ (F) গ্রেড থাকলে কি ৩য় বর্ষে ওঠা যায়?
</summary>
<div style="margin-top: 12px; padding-top: 10px; border-top: 1px dashed #cbd5e1; color: #334155; font-size: 15.5px; line-height: 1.8;">
উত্তর: হ্যাঁ, যদি আপনার অবশিষ্ট বিষয়গুলোর মধ্যে কমপক্ষে ৩টিতে পাস থাকে এবং সার্বিক সিজিপিএ ২.০০ বা তার বেশি থাকে, তবে একটি বা দুটি বিষয়ে F গ্রেড থাকলেও আপনি ৩য় বর্ষে প্রমোশন পাবেন। তবে ৩য় বর্ষে অধ্যয়নকালীন আপনাকে পরবর্তী শিক্ষাবর্ষে ওই অকৃতকার্য বিষয়ে ইমপ্রুভমেন্ট পরীক্ষা দিয়ে পাস করে নিতে হবে।
</div>
</details>

<details style="margin: 14px 0; padding: 16px 20px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; font-family: 'SolaimanLipi', Arial, sans-serif; cursor: pointer; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
<summary style="font-weight: 700; color: #1e3a8a; font-size: 17px; outline: none;">
প্রশ্ন ৩: আবশ্যিক ইংরেজি (Non-Credit) বিষয়ে ফেল করলে কি প্রমোশন আটকে যাবে?
</summary>
<div style="margin-top: 12px; padding-top: 10px; border-top: 1px dashed #cbd5e1; color: #334155; font-size: 15.5px; line-height: 1.8;">
উত্তর: না, আবশ্যিক ইংরেজিতে ফেল করলে ৩য় বর্ষে প্রমোশন আটকাবে না। কিন্তু জাতীয় বিশ্ববিদ্যালয়ের চূড়ান্ত ডিগ্রি সনদ ও সার্টিফিকেট পাওয়ার জন্য ৪র্থ বর্ষ শেষ হওয়ার পূর্বেই এই বিষয়ে ন্যূনতম ৩৩ নম্বর পেয়ে পাস করা বাধ্যতামূলক।
</div>
</details>

<details style="margin: 14px 0; padding: 16px 20px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; font-family: 'SolaimanLipi', Arial, sans-serif; cursor: pointer; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
<summary style="font-weight: 700; color: #1e3a8a; font-size: 17px; outline: none;">
প্রশ্ন ৪: ইনকোর্স পরীক্ষার ২০ নম্বর কি লিখিত পরীক্ষার সাথে যোগ হয়ে পাস নির্ধারিত হয়?
</summary>
<div style="margin-top: 12px; padding-top: 10px; border-top: 1px dashed #cbd5e1; color: #334155; font-size: 15.5px; line-height: 1.8;">
উত্তর: হ্যাঁ, জাতীয় বিশ্ববিদ্যালয়ের ১০০ নম্বরের প্রতি কোর্সে ৮০ নম্বর লিখিত এবং ২০ নম্বর ইনকোর্স ও ক্লাসে উপস্থিতির ভিত্তিতে মূল্যায়িত হয়। উভয় অংশ মিলে মোট ৪০ নম্বর পেলেই ওই কোর্সে পাস (D গ্রেড) অর্জিত হয়।
</div>
</details>

<details style="margin: 14px 0; padding: 16px 20px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; font-family: 'SolaimanLipi', Arial, sans-serif; cursor: pointer; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
<summary style="font-weight: 700; color: #1e3a8a; font-size: 17px; outline: none;">
প্রশ্ন ৫: ৩য় বর্ষে ভালো করার জন্য অনার্স ২য় বর্ষে সর্বনিম্ন কত CGPA লক্ষ্য রাখা উচিত?
</summary>
<div style="margin-top: 12px; padding-top: 10px; border-top: 1px dashed #cbd5e1; color: #334155; font-size: 15.5px; line-height: 1.8;">
উত্তর: যদিও প্রমোশনের ন্যূনতম যোগ্যতা ২.০০, কিন্তু চাকরির বাজার ও প্রথম শ্রেণি (First Class) ধরে রাখার জন্য শিক্ষার্থীদের অন্তত ৩.০০ বা তার বেশি সিজিপিএ লক্ষ্য রাখা উচিত। ২য় বর্ষে ভালো পয়েন্ট থাকলে ৩য় ও ৪র্থ বর্ষে ভালো রেজাল্ট করা অনেক সহজ হয়ে যায়।
</div>
</details>

<!-- Author Attribution Box -->
<div class="htbd-author-box" style="display: flex; align-items: center; gap: 18px; margin: 40px 0 25px 0; padding: 20px 24px; background: #f8fafc; border: 1px solid #e2e8f0; border-left: 5px solid #1e3a8a; border-radius: 10px; font-family: 'SolaimanLipi', Arial, sans-serif;">
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
      জাতীয় বিশ্ববিদ্যালয় ও উচ্চশিক্ষা অ্যাকাডেমিক পাঠ্যক্রম পর্যালোচনায় দীর্ঘ এক দশকের অভিজ্ঞতাসম্পন্ন একজন অ্যাকাডেমিক মেন্টর ও শিক্ষা গবেষক।
    </p>
  </div>
</div>

<!-- Schema.org Microdata: BlogPosting -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "জাতীয় বিশ্ববিদ্যালয় অনার্স ২য় বর্ষ পরীক্ষার গাইড ও ৩য় বর্ষে প্রমোশনের নিয়মাবলী ২০২৬",
  "description": "জাতীয় বিশ্ববিদ্যালয় অনার্স ২য় বর্ষ পরীক্ষা ও ৩য় বর্ষে প্রমোশনের অফিসিয়াল নীতিমালা ২০২৬। ন্যূনতম পাস মার্ক, CGPA ২.০০ শর্ত, নন-ক্রেডিট ইংরেজি আবশ্যিক নিয়ম ও গ্রেডিং স্কেল বিস্তারিত গাইড।",
  "image": "{HERO_BANNER}",
  "datePublished": "2026-10-03T14:20:00+06:00",
  "dateModified": "2026-10-03T14:20:00+06:00",
  "author": {{
    "@type": "Person",
    "name": "ফারুক স্যার (মো. ওমর ফারুক)",
    "jobTitle": "শিক্ষাবিদ ও অ্যাকাডেমিক গবেষক",
    "url": "https://www.helptrickbd.com/p/about-us.html"
  }},
  "publisher": {{
    "@type": "Organization",
    "name": "HelpTrickBD",
    "url": "https://www.helptrickbd.com",
    "logo": {{
      "@type": "ImageObject",
      "url": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/logo/logo.png"
    }}
  }},
  "mainEntityOfPage": {{
    "@type": "WebPage",
    "@id": "https://www.helptrickbd.com/2026/10/nu-honours-2nd-year-exam-guide-and-promotion-rules-2026.html"
  }}
}}
</script>

<!-- Schema.org Microdata: FAQPage -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "অনার্স ২য় বর্ষে ৩টি বিষয়ে পাস করলে কিন্তু CGPA ২.০০ এর নিচে আসলে কি প্রমোশন হবে?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "না। প্রমোশন পাওয়ার জন্য দুটি শর্তই একসাথে পূরণ হতে হবে—কমপক্ষে ৩টি কোর্সে পাস এবং মোট CGPA ন্যূনতম ২.০০। CGPA ২.০০ এর নিচে থাকলে নট-প্রমোটেড হবে।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "একটি বিষয়ে এফ (F) গ্রেড থাকলে কি ৩য় বর্ষে ওঠা যায়?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "হ্যাঁ, কমপক্ষে ৩টি বিষয়ে পাস ও সামগ্রিক CGPA ২.০০ থাকলে ৩য় বর্ষে প্রমোশন পাওয়া যাবে। তবে পরবর্তী শিক্ষাবর্ষে ওই কোর্সে মানোন্নয়ন পরীক্ষা দেওয়া বাধ্যতামূলক।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "আবশ্যিক ইংরেজি (Non-Credit) বিষয়ে ফেল করলে কি প্রমোশন আটকে যাবে?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "না, আবশ্যিক ইংরেজিতে ফেল করলে ৩য় বর্ষে প্রমোশন আটকাবে না। তবে ডিগ্রি সমাপ্তির আগেই ন্যূনতম ৩৩ নম্বর পেয়ে এতে পাস করতে হবে।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "ইনকোর্স পরীক্ষার ২০ নম্বর কি লিখিত পরীক্ষার সাথে যোগ হয়ে পাস নির্ধারিত হয়?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "হ্যাঁ, ৮০ নম্বর লিখিত ও ২০ নম্বর ইনকোর্স মিলে মোট ৪০ নম্বর পেলেই ওই বিষয়ে পাস গ্রেড অর্জিত হয়।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "৩য় বর্ষে ভালো করার জন্য অনার্স ২য় বর্ষে সর্বনিম্ন কত CGPA লক্ষ্য রাখা উচিত?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "প্রমোশনের জন্য ন্যূনতম ২.০০ হলেও প্রথম শ্রেণি ও ক্যারিয়ার সুরক্ষার জন্য অন্তত ৩.০০ সিজিপিএ লক্ষ্য রাখা উচিত।"
      }}
    }}
  ]
}}
</script>
"""

def main():
    print("=" * 70)
    print("GENERATING MASTER POST: NU HONOURS 2ND YEAR PROMOTION RULES 2026")
    print("=" * 70)

    html_content = generate_post_html()

    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html_content)

    meta_content = {
        "title": "জাতীয় বিশ্ববিদ্যালয় অনার্স ২য় বর্ষ পরীক্ষার গাইড ও ৩য় বর্ষে প্রমোশনের নিয়মাবলী ২০২৬",
        "english_slug": "nu-honours-2nd-year-exam-guide-and-promotion-rules-2026",
        "category": "National University",
        "labels": ["National University", "Education Guide"],
        "status": "draft",
        "meta_description": "জাতীয় বিশ্ববিদ্যালয় অনার্স ২য় বর্ষ পরীক্ষা ও ৩য় বর্ষে প্রমোশনের অফিসিয়াল নীতিমালা ২০২৬। ন্যূনতম পাস মার্ক, CGPA ২.০০ শর্ত, নন-ক্রেডিট ইংরেজি নিয়ম ও গ্রেডিং স্কেল বিস্তারিত গাইড।",
        "search_description": "জাতীয় বিশ্ববিদ্যালয় অনার্স ২য় বর্ষ ৩য় বর্ষে প্রমোশনের নিয়মাবলী ২০২৬: ন্যূনতম পাস কোর্স, CGPA ২.০০ শর্ত, ইংরেজি আবশ্যিক ও গ্রেডিং স্কেল গাইড।",
        "hero_banner": HERO_BANNER,
        "word_count": len(html_content.split())
    }

    with open(OUTPUT_META, "w", encoding="utf-8") as f:
        json.dump(meta_content, f, ensure_ascii=False, indent=2)

    print(f"\n[OK] Master HTML saved to: {OUTPUT_HTML}")
    print(f"[OK] Master Metadata saved to: {OUTPUT_META}")
    print(f"     Estimated Word Count: {len(html_content.split())} words")

if __name__ == "__main__":
    main()
