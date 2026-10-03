#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
output_posts/generate_class_6_to_9_annual_exam_post.py
------------------------------------------------------
Generates the authoritative master article for:
৬ষ্ঠ, ৭ম, ৮ম ও ৯ম শ্রেণির বার্ষিক পরীক্ষার মানবণ্টন ও পূর্ণাঙ্গ প্রস্তুতি গাইড ২০২৬ | Class 6 to 9 Annual Exam Marks Distribution

Complies with:
- SolaimanLipi typography
- Byte-0 Hero image placement before <!--more--> jump break
- Position 0 Summary Answer Box in first 100 words (AEO/GEO optimized)
- 30% Continuous Assessment + 70% Summative Exam Official Structure
- Table-first data grids for Classes 6, 7, 8, 9
- GPA 5.0 Calculation Matrix
- 5 Contextual Internal Links to Live Helptrickbd Posts
- Official Sources (NCTB nctb.gov.bd & DSHE dshe.gov.bd) Grounding
- Interactive <details><summary> FAQ Accordion
- Universal Faruk Sir Author Attribution Card
- Valid JSON-LD BlogPosting & FAQPage Schema
- Strictly ZERO EMOJIS (Rule 12)
"""

import os
import sys
import json

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUTPUT_HTML = os.path.join(PROJECT_ROOT, "output_posts", "class-6-to-9-annual-exam-marks-distribution-2026.html")
OUTPUT_META = os.path.join(PROJECT_ROOT, "output_posts", "class-6-to-9-annual-exam-marks-distribution-2026_meta.json")

CDN_BASE = "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts"
HERO_BANNER = f"{CDN_BASE}/class_6_to_9_annual_exam_marks_distribution_2026.webp"

def generate_master_post():
    full_html = f"""<figure style="margin: 0 0 25px 0; text-align: center;">
<img src="{HERO_BANNER}" alt="৬ষ্ঠ ৭ম ৮ম ও ৯ম শ্রেণির বার্ষিক পরীক্ষার মানবণ্টন ও প্রস্তুতি গাইড ২০২৬" title="Class 6 to 9 Annual Exam Marks Distribution 2026" width="1200" height="675" style="width: 100%; max-width: 1000px; height: auto; border-radius: 12px; box-shadow: 0 5px 20px rgba(0,0,0,0.12); display: block; margin: 0 auto;" loading="eager" fetchpriority="high" decoding="async" />
<figcaption style="font-size: 13.5px; color: #64748b; margin-top: 8px; font-family: 'SolaimanLipi', sans-serif;">৬ষ্ঠ, ৭ম, ৮ম ও ৯ম শ্রেণির বার্ষিক পরীক্ষার বিষয়ভিত্তিক নম্বর বিভাজন, গ্রেডিং স্কেল ও পূর্ণাঙ্গ প্রস্তুতি নির্দেশিকা ২০২৬</figcaption>
</figure>

<div class="htbd-overview-box" style="background: #f8fafd; border: 1px solid #dbeafe; border-left: 5px solid #0c2340; border-radius: 8px; padding: 20px 24px; margin-bottom: 24px; font-family: 'SolaimanLipi', Arial, sans-serif; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
<p style="margin: 0; font-size: 17px; line-height: 1.85; color: #1e293b;">
<strong>সারসংক্ষেপ উত্তর:</strong> জাতীয় শিক্ষাক্রম ও পাঠ্যপুস্তক বোর্ড (NCTB) এবং মাধ্যমিক ও উচ্চশিক্ষা অধিদপ্তর (মাউশি)-এর সর্বশেষ প্রজ্ঞাপন অনুযায়ী ২০২৬ শিক্ষাবর্ষে ৬ষ্ঠ, ৭ম, ৮ম ও ৯ম শ্রেণির বার্ষিক পরীক্ষা মোট <strong>১০০ নম্বরের</strong> ভিত্তিতে অনুষ্ঠিত হচ্ছে। এর মধ্যে <strong>৩০ শতাংশ (৩০ নম্বর)</strong> শিক্ষাবর্ষ জুড়ে ধারাবাহিক 'শিখনকালীন মূল্যায়ন' এবং বাকি <strong>৭০ শতাংশ (৭০ নম্বর)</strong> বছরের শেষে চূড়ান্ত 'বার্ষিক লিখিত পরীক্ষা (সামষ্টিক মূল্যায়ন)'-র মাধ্যমে নির্ধারিত হবে। পূর্বের ত্রিভুজ-বৃত্তের পরিবর্তে প্রতিটি বিষয়ে ১০০ নম্বরের ওপর ভিত্তি করে সনাতন ও সর্বজনীন জিপিএ ৫.০ (GPA 5.0) স্কেলে শিক্ষার্থীদের মেধা গ্রেড প্রকাশ করা হবে।
</p>
</div>

<!--more-->

<div style="display: inline-block; background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 6px; padding: 8px 18px; font-size: 14px; color: #166534; margin: 10px 0 25px 0; font-weight: 600; font-family: 'SolaimanLipi', sans-serif;">
অফিসিয়াল তথ্যসূত্র: জাতীয় শিক্ষাক্রম ও পাঠ্যপুস্তক বোর্ড (NCTB) ও মাধ্যমিক ও উচ্চশিক্ষা অধিদপ্তর (মাউশি) সার্কুলার অনুযায়ী যাচাইকৃত
</div>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 17px; line-height: 1.85; color: #334155; margin-bottom: 22px;">
মাধ্যমিক পর্যায়ের শিক্ষার্থীদের জন্য শিক্ষাবর্ষ সমাপনী বার্ষিক পরীক্ষা একটি অত্যন্ত গুরুত্বপূর্ণ ধাপ। বিশেষ করে ৬ষ্ঠ থেকে ৯ম শ্রেণির শিক্ষার্থীদের পরবর্তী শ্রেণিতে উত্তীর্ণ হওয়া এবং বোর্ড পরীক্ষার পূর্বপ্রস্তুতি গড়ে তোলার ক্ষেত্রে এই পরীক্ষার ফলাফল সরাসরি ভূমিকা রাখে। শিক্ষা মন্ত্রণালয়ের সাম্প্রতিক নির্দেশনায় মূল্যায়ন পদ্ধতিতে যুগান্তকারী স্বচ্ছতা আনা হয়েছে। জটিল পারদর্শিতার সূচকের (PI) বদলে স্পষ্ট নম্বর প্রদান ও গ্রেডিং পদ্ধতি চালু করায় শিক্ষার্থী, শিক্ষক ও অভিভাবক সকলের জন্যই মূল্যায়নের চিত্র এখন অত্যন্ত সুস্পষ্ট। নিচে ৬ষ্ঠ থেকে ৯ম শ্রেণির বিষয়ভিত্তিক মানবণ্টন, পরীক্ষার সময়সূচি এবং জিপিএ ৫ পাওয়ার সেরা কৌশল বিস্তারিত আলোচনা করা হলো।
</p>

<h2 style="font-family: 'SolaimanLipi', sans-serif; color: #0c2340; font-size: 24px; font-weight: 700; margin: 40px 0 18px 0; border-left: 5px solid #1e3a8a; padding-left: 14px;">
শিক্ষা মন্ত্রণালয় ও মাউশির মূল্যায়ন নীতি ২০২৬ একনজরে | Examination Framework
</h2>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16.5px; line-height: 1.85; color: #334155; margin-bottom: 20px;">
মাউশি কর্তৃক নির্ধারিত মূল্যায়ন কাঠামো মূলত দুটি স্বতন্ত্র অংশের সমন্বয়ে গঠিত। প্রতিটি শিক্ষার্থীকে উভয় অংশে যথাযথ দায়িত্বশীলতার সাথে অংশগ্রহণ করতে হয়:
</p>

<div style="overflow-x: auto; margin: 25px 0;">
<table style="width: 100%; border-collapse: collapse; font-family: 'SolaimanLipi', sans-serif; font-size: 15.5px; text-align: left; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
<thead>
<tr style="background: #0c2340; color: #ffffff;">
<th style="padding: 14px 16px; border: 1px solid #1e3a8a;">মূল্যায়নের ধরন</th>
<th style="padding: 14px 16px; border: 1px solid #1e3a8a;">বরাদ্দকৃত নম্বর</th>
<th style="padding: 14px 16px; border: 1px solid #1e3a8a;">মূল্যায়নের উপাদানসমূহ</th>
<th style="padding: 14px 16px; border: 1px solid #1e3a8a;">মূল্যায়নকারী কর্তৃপক্ষ</th>
</tr>
</thead>
<tbody>
<tr style="background: #f8fafc;">
<td style="padding: 12px 16px; border: 1px solid #e2e8f0; font-weight: 700; color: #0f172a;">১. শিখনকালীন মূল্যায়ন</td>
<td style="padding: 12px 16px; border: 1px solid #e2e8f0; font-weight: bold; color: #0284c7;">৩০ নম্বর (৩০%)</td>
<td style="padding: 12px 16px; border: 1px solid #e2e8f0;">শ্রেণিকক্ষের অ্যাসাইনমেন্ট, একক ও দলীয় কাজ, ব্যবহারিক কাজ, কুইজ ও ক্লাসে উপস্থিতি</td>
<td style="padding: 12px 16px; border: 1px solid #e2e8f0;">শ্রেণি শিক্ষক ও সংশ্লিষ্ট বিষয় শিক্ষক</td>
</tr>
<tr>
<td style="padding: 12px 16px; border: 1px solid #e2e8f0; font-weight: 700; color: #0f172a;">২. বার্ষিক সামষ্টিক পরীক্ষা</td>
<td style="padding: 12px 16px; border: 1px solid #e2e8f0; font-weight: bold; color: #16a34a;">৭০ নম্বর (৭০%)</td>
<td style="padding: 12px 16px; border: 1px solid #e2e8f0;">এনসিটিবি সংক্ষিপ্ত সিলেবাসের ওপর ৩ ঘণ্টার চূড়ান্ত লিখিত পরীক্ষা (সৃজনশীল ও নৈর্ব্যক্তিক)</td>
<td style="padding: 12px 16px; border: 1px solid #e2e8f0;">বিদ্যালয় পরীক্ষা পরিচালনা কমিটি</td>
</tr>
<tr style="background: #f0fdf4;">
<td style="padding: 12px 16px; border: 1px solid #e2e8f0; font-weight: 700; color: #166534;">সর্বমোট চূড়ান্ত মূল্যায়ন</td>
<td style="padding: 12px 16px; border: 1px solid #e2e8f0; font-weight: bold; color: #166534;">১০০ নম্বর (১০০%)</td>
<td style="padding: 12px 16px; border: 1px solid #e2e8f0;" colspan="2">উভয় অংশের সমন্বয়ে জিপিএ (GPA) গ্রেডিং স্কেলে ফলাফল প্রস্তুত</td>
</tr>
</tbody>
</table>
</div>

<h2 style="font-family: 'SolaimanLipi', sans-serif; color: #0c2340; font-size: 24px; font-weight: 700; margin: 40px 0 18px 0; border-left: 5px solid #1e3a8a; padding-left: 14px;">
৬ষ্ঠ ও ৭ম শ্রেণির বিষয়ভিত্তিক চূড়ান্ত মানবণ্টন ছক | Class 6 & 7 Marks Breakdown
</h2>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16.5px; line-height: 1.85; color: #334155; margin-bottom: 20px;">
৬ষ্ঠ ও ৭ম শ্রেণির পাঠ্যক্রমে প্রতিটি বিষয়ের লিখিত অংশে বিষয়ভিত্তিক প্রায়োগিক দক্ষতা যাচাইয়ের ওপর গুরুত্ব দেওয়া হয়েছে। বার্ষিক লিখিত পরীক্ষার ৭০ নম্বরের বণ্টন কাঠামো নিচে তুলে ধরা হলো:
</p>

<div style="overflow-x: auto; margin: 25px 0;">
<table style="width: 100%; border-collapse: collapse; font-family: 'SolaimanLipi', sans-serif; font-size: 15px; text-align: left; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px;">
<thead>
<tr style="background: #1e3a8a; color: #ffffff;">
<th style="padding: 12px 15px; border: 1px solid #2563eb;">বিষয়</th>
<th style="padding: 12px 15px; border: 1px solid #2563eb;">লিখিত পরীক্ষা (৭০ নম্বর)</th>
<th style="padding: 12px 15px; border: 1px solid #2563eb;">শিখনকালীন (৩০ নম্বর)</th>
<th style="padding: 12px 15px; border: 1px solid #2563eb;">বিশেষ দিক ও প্রশ্নোত্তর ধরন</th>
</tr>
</thead>
<tbody>
<tr style="background: #f8fafc;">
<td style="padding: 12px 15px; border: 1px solid #e2e8f0; font-weight: 700;">বাংলা (১ম ও ২য় পত্র)</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">সৃজনশীল ৪০ + নৈর্ব্যক্তিক ১৫ + ব্যাকরণ ও নির্মিতি ১৫</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">শ্রবণ ও কথন দক্ষতা, খাতা ও উপস্থাপনা ৩০</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">গদ্য ও কবিতা থেকে ৪টি সৃজনশীল প্রশ্ন, শব্দার্থ ও <a href="https://www.helptrickbd.com/2025/12/bangla-bagdhara-collection-with-meaning.html" style="color: #2563eb; text-decoration: underline;" title="বাংলা বাগধারা সংকলন">বাংলা ব্যাকরণ ও বাগধারা</a></td>
</tr>
<tr>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0; font-weight: 700;">ইংরেজি (English)</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">Reading 30 + Grammar 25 + Writing 15</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">Speaking, Listening ও Class Assignment ৩০</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">Seen/Unseen Passage, Gap Filling ও <a href="https://www.helptrickbd.com/2026/09/ssc-english-2nd-paper-right-form-of.html" style="color: #2563eb; text-decoration: underline;" title="Right Form of Verbs নিয়ম">Right Form of Verbs</a> প্রস্তুতি</td>
</tr>
<tr style="background: #f8fafc;">
<td style="padding: 12px 15px; border: 1px solid #e2e8f0; font-weight: 700;">গণিত (Mathematics)</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">সৃজনশীল ৫০ + সংক্ষিপ্ত ও নৈর্ব্যক্তিক ২০</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">ব্যবহারিক পরিমাপ, সমস্যা সমাধান ও খাতা ৩০</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">পাটিগণিত, বীজগণিতীয় রাশি ও ব্যবহারিক জ্যামিতি অঙ্কন</td>
</tr>
<tr>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0; font-weight: 700;">বিজ্ঞান (অনুসন্ধানী ও অনুশীলন)</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">সৃজনশীল ৪০ + সংক্ষিপ্ত ১৫ + নৈর্ব্যক্তিক ১৫</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">পরীক্ষণ, বৈজ্ঞানিক অনুসন্ধান ও প্রজেক্ট ৩০</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">জীববিজ্ঞান, পদার্থবিজ্ঞান ও পরিবেশ বিজ্ঞানের মূল ভিত্তি</td>
</tr>
<tr style="background: #f8fafc;">
<td style="padding: 12px 15px; border: 1px solid #e2e8f0; font-weight: 700;">ইতিহাস ও সামাজিক বিজ্ঞান</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">সৃজনশীল ৫০ + সংক্ষিপ্ত ও নৈর্ব্যক্তিক ২০</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">সামাজিক সমীক্ষা, পোস্টার পেপার ও প্রতিবেদন ৩০</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">প্রাচীন বাংলা, মুক্তিযুদ্ধ ও নাগরিক অধিকার বিশ্লেষণ</td>
</tr>
<tr>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0; font-weight: 700;">ডিজিটাল প্রযুক্তি (আইসিটি)</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">তাত্ত্বিক লিখিত ৩৫ + ব্যবহারিক ৩৫</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">কম্পিউটার ল্যাব কার্যক্রম ও প্রজেক্ট ৩০</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">সাইবার নিরাপত্তা, অফিস সফটওয়্যার ও অনলাইন শিখন</td>
</tr>
<tr style="background: #f8fafc;">
<td style="padding: 12px 15px; border: 1px solid #e2e8f0; font-weight: 700;">ধর্ম ও নৈতিক শিক্ষা</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">সৃজনশীল ৫০ + নৈর্ব্যক্তিক ২০</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">নৈতিক আচরণ ও ব্যবহারিক অনুশাসন ৩০</td>
<td style="padding: 12px 15px; border: 1px solid #e2e8f0;">কুরআন-হাদিস/ধর্মগ্রন্থের বাণী ও দৈনন্দিন শিষ্টাচার</td>
</tr>
</tbody>
</table>
</div>

<h2 style="font-family: 'SolaimanLipi', sans-serif; color: #0c2340; font-size: 24px; font-weight: 700; margin: 40px 0 18px 0; border-left: 5px solid #1e3a8a; padding-left: 14px;">
৮ম ও ৯ম শ্রেণির বোর্ডমুখী পূর্ণাঙ্গ মানবণ্টন ও সৃজনশীল কাঠামো | Class 8 & 9 Blueprint
</h2>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16.5px; line-height: 1.85; color: #334155; margin-bottom: 20px;">
৮ম ও ৯ম শ্রেণি মাধ্যমিক স্তরের অত্যন্ত সংবেদনশীল ধাপ। এই দুই শ্রেণির বার্ষিক পরীক্ষা সরাসরি এসএসসি ও সমমানের বোর্ড পরীক্ষার হুবহু আদলে পরিচালিত হয়। বোর্ডের নিয়মে সৃজনশীল প্রশ্ন (CQ) ও বহুনির্বাচনি প্রশ্ন (MCQ)-এর স্পষ্ট বিভাজন নিচে বিস্তারিত তুলে ধরা হলো:
</p>

<div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 10px; padding: 22px 26px; margin: 25px 0; font-family: 'SolaimanLipi', sans-serif;">
<h3 style="margin-top: 0; color: #1e3a8a; font-size: 20px; font-weight: 700; margin-bottom: 12px;">৮ম ও ৯ম শ্রেণির ১০০ নম্বরের বিষয়সমূহের আদর্শ বণ্টন (বাংলা, গণিত ও সমাজ)</h3>
<ul style="margin: 0; padding-left: 20px; color: #1e293b; line-height: 1.9; font-size: 16px;">
<li><strong>সৃজনশীল লিখিত অংশ (CQ):</strong> মোট ৭০ নম্বর। মোট ১১টি সৃজনশীল প্রশ্ন থাকবে, যার মধ্য থেকে যেকোনো ৭টি প্রশ্নের উত্তর দিতে হবে (৭ × ১০ = ৭০ নম্বর)। সময়: ২ ঘণ্টা ৩০ মিনিট। শিক্ষার্থীকে গদ্য, কবিতা ও উপন্যাস/নাটক থেকে নির্ধারিত শর্ত মেনে প্রশ্ন বাছাই করতে হবে।</li>
<li><strong>বহুনির্বাচনি অংশ (MCQ):</strong> মোট ৩০ নম্বর। ৩০টি প্রশ্ন থাকবে এবং প্রতিটি প্রশ্নের মান ১ নম্বর। কোনো নেগেটিভ মার্কিং নেই। সময়: ৩০ মিনিট। বিস্তারিত অনুশীলনের জন্য আমাদের <a href="https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-model-test.html" style="color: #2563eb; text-decoration: underline; font-weight: 600;" title="এসএসসি বাংলা ১ম পত্র মডেল টেস্ট">এসএসসি বাংলা মডেল টেস্ট ও প্রশ্নব্যাংক</a> অনুসরণ করতে পারেন।</li>
<li><strong>মোট সময়:</strong> ৩ ঘণ্টা (প্রথমে ৩০ মিনিটে নৈর্ব্যক্তিক ও পরে ২ ঘণ্টা ৩০ মিনিটে সৃজনশীল পরীক্ষা অনুষ্ঠিত হবে)।</li>
</ul>
</div>

<div style="background: #fefce8; border: 1px solid #fef08a; border-radius: 10px; padding: 22px 26px; margin: 25px 0; font-family: 'SolaimanLipi', sans-serif;">
<h3 style="margin-top: 0; color: #854d0e; font-size: 20px; font-weight: 700; margin-bottom: 12px;">৯ম শ্রেণির বিজ্ঞান শাখার বিশেষ বিষয়সমূহ (পদার্থবিজ্ঞান, রসায়ন ও জীববিজ্ঞান)</h3>
<p style="margin: 0 0 10px 0; color: #713f12; line-height: 1.85; font-size: 16px;">
বিজ্ঞান বিভাগের ব্যবহারিকযুক্ত বিষয়গুলোর ক্ষেত্রে মাউশির বোর্ড স্ট্যান্ডার্ড অনুযায়ী নম্বর বিন্যাস নির্ধারিত:
</p>
<ul style="margin: 0; padding-left: 20px; color: #713f12; line-height: 1.85; font-size: 15.5px;">
<li><strong>সৃজনশীল প্রশ্ন (CQ):</strong> ৫০ নম্বর (৮টি প্রশ্নের মধ্যে যেকোনো ৫টি প্রশ্নের উত্তর দিতে হবে, ৫ × ১০ = ৫০)।</li>
<li><strong>বহুনির্বাচনি প্রশ্ন (MCQ):</strong> ২৫ নম্বর (২৫টি প্রশ্নের সবগুলোর উত্তর দিতে হবে, ২৫ × ১ = ২৫)।</li>
<li><strong>ব্যবহারিক পরীক্ষা (Practical):</strong> ২৫ নম্বর (ল্যাব এক্সপেরিমেন্ট ১৫ + মৌখিক ৫ + ব্যবহারিক নোটবুক ৫)।</li>
</ul>
</div>

<div style="background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 10px; padding: 22px 26px; margin: 25px 0; font-family: 'SolaimanLipi', sans-serif;">
<h3 style="margin-top: 0; color: #9d174d; font-size: 20px; font-weight: 700; margin-bottom: 12px;">ইংরেজি ১ম ও ২য় পত্রের ১০০ নম্বরের স্পেশাল বিভাজন</h3>
<p style="margin: 0 0 10px 0; color: #831843; line-height: 1.85; font-size: 16px;">
ইংরেজি বিষয়ে পূর্ণাঙ্গ ১০০ নম্বরের লিখিত পরীক্ষা অনুষ্ঠিত হয়:
</p>
<ul style="margin: 0; padding-left: 20px; color: #831843; line-height: 1.85; font-size: 15.5px;">
<li><strong>Part A: Reading Test (৫০ নম্বর):</strong> Seen Passage 1 (MCQ & Answering Questions - 15 marks), Seen Passage 2 (Gap Filling without clues - 5 marks), Information Transfer & Summary Writing (15 marks), Matching sentences (5 marks), Rearranging sentences (10 marks)।</li>
<li><strong>Part B: Grammar Items (৩০ নম্বর):</strong> Cloze test with/without clues, Substitution table, Changing sentences (Voice, Degree, Affirmative to Negative), Suffix & Prefix, Tag questions এবং Sentence connectors। পূর্ণাঙ্গ প্রস্তুতির জন্য <a href="https://www.helptrickbd.com/2026/09/ssc-english-2nd-paper-final-suggestion.html" style="color: #9d174d; text-decoration: underline; font-weight: 600;" title="এসএসসি ইংরেজি ফাইনাল সাজেশন">এসএসসি ইংরেজি ২য় পত্র ফাইনাল সাজেশন</a> সহায়ক হবে।</li>
<li><strong>Part C: Guided Writing (২০ নম্বর):</strong> Paragraph writing, Completing a story, Informal letter/Email এবং Dialogue writing।</li>
</ul>
</div>

<h2 style="font-family: 'SolaimanLipi', sans-serif; color: #0c2340; font-size: 24px; font-weight: 700; margin: 40px 0 18px 0; border-left: 5px solid #1e3a8a; padding-left: 14px;">
ফলাফল নির্ধারণ ও গ্রেডিং স্কেল (GPA 5.0 ক্যালকুলেশন মেথড) | Grading System
</h2>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16.5px; line-height: 1.85; color: #334155; margin-bottom: 20px;">
বার্ষিক পরীক্ষার ৭০ নম্বর এবং শিখনকালীন মূল্যায়নের ৩০ নম্বর একত্রিত করে প্রাপ্ত মোট ১০০ নম্বরের ভিত্তিতে সরকারি গ্রেডিং স্কেল কার্যকর হয়। প্রতিটি গ্রেডের সীমা ও পয়েন্ট নিচে সুস্পষ্টভাবে প্রদর্শিত হলো:
</p>

<div style="overflow-x: auto; margin: 25px 0;">
<table style="width: 100%; border-collapse: collapse; font-family: 'SolaimanLipi', sans-serif; font-size: 15px; text-align: center; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px;">
<thead>
<tr style="background: #0c2340; color: #ffffff;">
<th style="padding: 12px 14px; border: 1px solid #1e3a8a;">নম্বর সীমা (Marks Range)</th>
<th style="padding: 12px 14px; border: 1px solid #1e3a8a;">অক্ষর গ্রেড (Letter Grade)</th>
<th style="padding: 12px 14px; border: 1px solid #1e3a8a;">গ্রেড পয়েন্ট (Grade Point - GP)</th>
<th style="padding: 12px 14px; border: 1px solid #1e3a8a;">মূল্যায়নের মন্তব্য</th>
</tr>
</thead>
<tbody>
<tr style="background: #f0fdf4;">
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; font-weight: bold;">৮০ – ১০০</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; font-weight: bold; color: #15803d;">A+ (এ প্লাস)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; font-weight: bold; color: #15803d;">৫.০০ (5.00)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; color: #15803d;">অসামান্য (Outstanding)</td>
</tr>
<tr>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; font-weight: 600;">৭০ – ৭৯</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; font-weight: 600; color: #0284c7;">A (এ)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; font-weight: 600; color: #0284c7;">৪.০০ (4.00)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0;">খুব ভালো (Very Good)</td>
</tr>
<tr style="background: #f8fafc;">
<td style="padding: 10px 14px; border: 1px solid #e2e8f0;">৬০ – ৬৯</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; color: #0369a1;">A- (এ মাইনাস)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; color: #0369a1;">৩.৫০ (3.50)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0;">ভালো (Good)</td>
</tr>
<tr>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0;">৫০ – ৫৯</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; color: #d97706;">B (বি)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; color: #d97706;">৩.০০ (3.00)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0;">সন্তোষজনক (Satisfactory)</td>
</tr>
<tr style="background: #f8fafc;">
<td style="padding: 10px 14px; border: 1px solid #e2e8f0;">৪০ – ৪৯</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; color: #b45309;">C (সি)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; color: #b45309;">২.০০ (2.00)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0;">উন্নতি প্রয়োজন (Passable)</td>
</tr>
<tr>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0;">৩৩ – ৩৯</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; color: #dc2626;">D (ডি)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; color: #dc2626;">১.০০ (1.00)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0;">প্রান্তিক পাস (Marginal Pass)</td>
</tr>
<tr style="background: #fef2f2;">
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; font-weight: bold; color: #b91c1c;">০ – ৩২</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; font-weight: bold; color: #b91c1c;">F (এফ)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; font-weight: bold; color: #b91c1c;">০.০০ (0.00)</td>
<td style="padding: 10px 14px; border: 1px solid #e2e8f0; color: #b91c1c;">অকৃতকার্য (Failed)</td>
</tr>
</tbody>
</table>
</div>

<h2 style="font-family: 'SolaimanLipi', sans-serif; color: #0c2340; font-size: 24px; font-weight: 700; margin: 40px 0 18px 0; border-left: 5px solid #1e3a8a; padding-left: 14px;">
বার্ষিক পরীক্ষায় এ প্লাস (A+) পাওয়ার কৌশল ও ৩ ঘণ্টার টাইম ম্যানেজমেন্ট | Exam Strategy
</h2>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16.5px; line-height: 1.85; color: #334155; margin-bottom: 20px;">
পরীক্ষার হলে শুধু পড়া থাকলেই ভালো ফল পাওয়া যায় না; সময়ের সঠিক সদ্ব্যবহার করা অত্যন্ত জরুরি। অনেক শিক্ষার্থী সব প্রশ্নের উত্তর জানা সত্ত্বেও সময় ব্যবস্থাপনার অভাবে শেষ প্রশ্নগুলো অপূর্ণ রেখে আসে। ৩ ঘণ্টার পরীক্ষাকে নিচের টাইম বাজেটে ভাগ করে নেওয়া বুদ্ধিমানের কাজ হবে:
</p>

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 22px; margin: 25px 0; font-family: 'SolaimanLipi', sans-serif;">
<h3 style="margin-top: 0; color: #0f172a; font-size: 19px; font-weight: 700; margin-bottom: 15px;">৩ ঘণ্টার নিখুঁত সময় বণ্টন চার্ট (Time Budgeting Formula)</h3>
<ul style="margin: 0; padding-left: 20px; line-height: 1.9; font-size: 16px; color: #334155;">
<li><strong>প্রথম ৩০ মিনিট (নৈর্ব্যক্তিক পরীক্ষা):</strong> প্রশ্ন পাওয়ার পর মনোযোগ দিয়ে বৃত্ত ভরাট করুন। নিশ্চিত উত্তরগুলো আগে দাগিয়ে নিন; অস্পষ্ট প্রশ্ন নিয়ে অযথা সময় নষ্ট করবেন না।</li>
<li><strong>পরবর্তী ৫ মিনিট (প্রশ্ন নির্বাচন ও পরিকল্পনা):</strong> সৃজনশীল প্রশ্নপত্র হাতে পাওয়ার পর দ্রুত চোখ বুলিয়ে যে ৭টি প্রশ্নের ক, খ, গ, ঘ চারটি অংশই আপনার সবচেয়ে ভালো জানা আছে, সেগুলো চিহ্নিত করুন।</li>
<li><strong>প্রতিটি সৃজনশীল প্রশ্নের জন্য ২১ মিনিট:</strong>
  <br />• <em>(ক) জ্ঞানমূলক প্রশ্ন (১ নম্বর):</em> সর্বোচ্চ ১ থেকে দেড় মিনিট (সরাসরি ১-২ বাক্যে উত্তর)।
  <br />• <em>(খ) অনুধাবনমূলক প্রশ্ন (২ নম্বর):</em> ৩ থেকে ৪ মিনিট (দুটি প্যারায় স্পষ্ট ব্যাখ্যা)।
  <br />• <em>(গ) প্রয়োগমূলক প্রশ্ন (৩ নম্বর):</em> ৬ থেকে ৭ মিনিট (উদ্দীপক ও পাঠ্যবইয়ের মেলবন্ধন)।
  <br />• <em>(ঘ) উচ্চতর দক্ষতামূলক প্রশ্ন (৪ নম্বর):</em> ৮ থেকে ৯ মিনিট (তুলনামূলক মূল্যায়ন ও নিজস্ব সিদ্ধান্ত)।
</li>
<li><strong>শেষ ১০ মিনিট (খাতা রিভিশন ও চেক):</strong> খাতার মার্জিন, রোল নম্বর, প্রশ্নের ক্রমিক নম্বর ও অতিরিক্ত পৃষ্ঠা (লুজ শিট)-এর নম্বর সঠিকভাবে যুক্ত করা হয়েছে কি না তা মিলিয়ে দেখুন। পরীক্ষার হলের নিখুঁত নিয়ম জানতে আমাদের <a href="https://www.helptrickbd.com/2025/04/important-instructions-for-ssc-candidates.html" style="color: #2563eb; text-decoration: underline;" title="পরীক্ষার্থীদের জন্য জরুরি নির্দেশনা">পরীক্ষার্থীদের জন্য জরুরি নির্দেশনা</a> গাইডটি পড়তে পারেন।</li>
</ul>
</div>

<h2 style="font-family: 'SolaimanLipi', sans-serif; color: #0c2340; font-size: 24px; font-weight: 700; margin: 40px 0 18px 0; border-left: 5px solid #1e3a8a; padding-left: 14px;">
শিক্ষার্থীদের যে ৫টি মারাত্মক ভুল পরিহার করতে হবে | Avoidable Mistakes
</h2>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16.5px; line-height: 1.85; color: #334155; margin-bottom: 20px;">
অভিজ্ঞ শিক্ষকদের খাতা মূল্যায়নের অভিজ্ঞতা অনুযায়ী, শিক্ষার্থীরা প্রায়শই নিচের ভুলগুলোর কারণে কাঙ্ক্ষিত নম্বর থেকে বঞ্চিত হয়:
</p>

<ol style="font-family: 'SolaimanLipi', sans-serif; font-size: 16px; line-height: 1.9; color: #334155; margin-bottom: 25px; padding-left: 22px;">
<li><strong>শিখনকালীন মূল্যায়নের খাতা যথাসময়ে জমা না দেওয়া:</strong> অনেকে লিখিত পরীক্ষার প্রস্তুতিতে ব্যস্ত হয়ে শিখনকালীন ৩০ নম্বরের প্রজেক্ট বা খাতা জমা দিতে অবহেলা করে। অথচ এই ৩০ নম্বর চূড়ান্ত জিপিএ ৫ অর্জনের সবচেয়ে সহজ ভিত্তি।</li>
<li><strong>জ্ঞানমূলক ও অনুধাবনে অপ্রয়োজনীয় বড় উত্তর লেখা:</strong> ১ নম্বরের জ্ঞানমূলক প্রশ্নে আধা পৃষ্ঠা লিখলেও পরীক্ষক ১ নম্বরের বেশি দেবেন না; বরং এতে সময় নষ্ট হয়ে ৪ নম্বরের প্রশ্নের উত্তর ছোট হয়ে যায়।</li>
<li><strong>উদ্দীপকের হুবহু লাইন তুলে দেওয়া:</strong> সৃজনশীল প্রশ্নের প্রয়োগ ও উচ্চতর দক্ষতায় উদ্দীপকের কথা হুবহু না লিখে পাঠ্যবইয়ের তত্ত্বের আলোকে নিজের ভাষায় বিশ্লেষণ উপস্থাপন করতে হবে।</li>
<li><strong>জ্যামিতিতে পেন্সিলের বদলে কলম ব্যবহার:</strong> গণিত পরীক্ষায় উপপাদ্য বা সম্পাদ্যের চিত্র সবসময় শার্প পেন্সিল ও স্কেল দিয়ে পরিচ্ছন্নভাবে আঁকতে হবে।</li>
<li><strong>নেতিবাচক ও কাটাকাটিপূর্ণ উপস্থাপনা:</strong> খাতায় বারবার কাটাকাটি করলে পরীক্ষকের মনস্তাত্ত্বিক বিরক্তি তৈরি হয়। কোনো শব্দ ভুল হলে একটি মাত্র সরল দাগ দিয়ে কেটে পাশে শুদ্ধ শব্দটি লিখুন।</li>
</ol>

<h2 style="font-family: 'SolaimanLipi', sans-serif; color: #0c2340; font-size: 24px; font-weight: 700; margin: 40px 0 18px 0; border-left: 5px solid #1e3a8a; padding-left: 14px;">
অফিসিয়াল তথ্যসূত্র ও পোর্টাল নির্দেশিকা | Official References
</h2>

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 10px; padding: 22px 25px; margin: 25px 0; font-family: 'SolaimanLipi', sans-serif;">
<p style="margin: 0 0 16px 0; font-size: 16px; line-height: 1.8; color: #1e293b;">
এই আর্টিকেলে উপস্থাপিত সকল মানবণ্টন ও মূল্যায়ন কাঠামো শিক্ষা মন্ত্রণালয়, এনসিটিবি ও মাউশির অফিসিয়াল প্রজ্ঞাপন দ্বারা অনুমোদিত। পরিপত্র যাচাই ও বিস্তারিত জানতে সরাসরি সরকারি পোর্টালের নোটিশ সেকশনগুলো নিচে দেওয়া হলো:
</p>
<ul style="margin: 0; padding-left: 20px; line-height: 2.1; font-size: 15.5px; color: #0f172a;">
<li style="margin-bottom: 8px;"><strong>মাধ্যমিক ও উচ্চশিক্ষা অধিদপ্তর (মাউশি) অফিসিয়াল নোটিশ বোর্ড:</strong> <a href="https://www.dshe.gov.bd/site/notices" target="_blank" rel="noopener noreferrer" style="color: #1e40af; text-decoration: underline; font-weight: 600;">dshe.gov.bd/site/notices</a> (সংশোধিত মূল্যায়ন নির্দেশনা ও বিষয়-কাঠামো নোটিশ)</li>
<li style="margin-bottom: 8px;"><strong>জাতীয় শিক্ষাক্রম ও পাঠ্যপুস্তক বোর্ড (NCTB) পরিপত্র শাখা:</strong> <a href="http://www.nctb.gov.bd/site/notices" target="_blank" rel="noopener noreferrer" style="color: #1e40af; text-decoration: underline; font-weight: 600;">nctb.gov.bd/site/notices</a> (বার্ষিক সামষ্টিক মূল্যায়ন ও মানবণ্টন নির্দেশিকা)</li>
<li style="margin-bottom: 8px;"><strong>শিক্ষা মন্ত্রণালয় (মাধ্যমিক ও উচ্চ শিক্ষা বিভাগ):</strong> <a href="https://shed.gov.bd/site/notices" target="_blank" rel="noopener noreferrer" style="color: #1e40af; text-decoration: underline; font-weight: 600;">shed.gov.bd/site/notices</a> (পরীক্ষা ও পাঠ্যসূচি সংক্রান্ত সরকারি প্রজ্ঞাপন)</li>
<li><strong>বিদ্যালয়ের নিজস্ব নোটিশ বোর্ড:</strong> নিজ নিজ বিদ্যালয়ের প্রধান শিক্ষক ও শ্রেণি শিক্ষক কর্তৃক নোটিশ বোর্ডে টাঙানো ব্যবহারিক ও বার্ষিক পরীক্ষার চূড়ান্ত রুটিন।</li>
</ul>
</div>

<h2 style="font-family: 'SolaimanLipi', sans-serif; color: #0c2340; font-size: 24px; font-weight: 700; margin: 40px 0 18px 0; border-left: 5px solid #1e3a8a; padding-left: 14px;">
সর্বাধিক জিজ্ঞাসিত প্রশ্নোত্তর (FAQ) | Frequently Asked Questions
</h2>

<details style="margin: 14px 0; padding: 16px 20px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; font-family: 'SolaimanLipi', Arial, sans-serif; cursor: pointer; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
<summary style="font-weight: 700; color: #1e3a8a; font-size: 17px; outline: none;">
প্রশ্ন ১: ২০২৬ সালের বার্ষিক পরীক্ষায় কি কোনো বিষয়ে ফেল করলে পরবর্তী ক্লাসে ওঠা যাবে?
</summary>
<div style="margin-top: 12px; padding-top: 10px; border-top: 1px dashed #cbd5e1; color: #334155; font-size: 15.5px; line-height: 1.8;">
উত্তর: সরকারি বিধিমালা অনুযায়ী বাধ্যতামূলক বিষয়গুলোতে পাস নম্বর (ন্যূনতম ৩৩ বা 'D' গ্রেড) অর্জন করা আবশ্যক। কোনো শিক্ষার্থী এক বা একাধিক বিষয়ে অকৃতকার্য হলে বিদ্যালয় একাডেমিক কাউন্সিলের নিয়ম অনুযায়ী সিদ্ধান্ত গৃহীত হয়। তবে সাধারণ নীতি অনুযায়ী পরবর্তী ক্লাসে উত্তীর্ণ হতে হলে সব আবশ্যিক বিষয়ে পাস করতে হবে।
</div>
</details>

<details style="margin: 14px 0; padding: 16px 20px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; font-family: 'SolaimanLipi', Arial, sans-serif; cursor: pointer; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
<summary style="font-weight: 700; color: #1e3a8a; font-size: 17px; outline: none;">
প্রশ্ন ২: শিখনকালীন ৩০ নম্বরের খাতা ও অ্যাসাইনমেন্ট কবে জমা দিতে হবে?
</summary>
<div style="margin-top: 12px; padding-top: 10px; border-top: 1px dashed #cbd5e1; color: #334155; font-size: 15.5px; line-height: 1.8;">
উত্তর: বার্ষিক লিখিত পরীক্ষা শুরু হওয়ার অন্তত ৭ থেকে ১০ দিন পূর্বেই শ্রেণি শিক্ষকের নিকট শিখনকালীন মূল্যায়নের যাবতীয় অ্যাসাইনমেন্ট, প্রজেক্ট ফাইল ও ব্যবহারিক নোটবুক জমা দিয়ে মূল্যায়ন সম্পন্ন করতে হয়।
</div>
</details>

<details style="margin: 14px 0; padding: 16px 20px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; font-family: 'SolaimanLipi', Arial, sans-serif; cursor: pointer; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
<summary style="font-weight: 700; color: #1e3a8a; font-size: 17px; outline: none;">
প্রশ্ন ৩: বার্ষিক পরীক্ষা কি পুরো পাঠ্যবইয়ের ওপর অনুষ্ঠিত হবে নাকি সংক্ষিপ্ত সিলেবাসে?
</summary>
<div style="margin-top: 12px; padding-top: 10px; border-top: 1px dashed #cbd5e1; color: #334155; font-size: 15.5px; line-height: 1.8;">
উত্তর: এনসিটিবি ও মাউশির নির্দেশনা অনুযায়ী বার্ষিক পরীক্ষা সাধারণত বছরের দ্বিতীয় অর্ধে (জুলাই থেকে নভেম্বর পর্যন্ত) পঠিত সংক্ষিপ্ত পাঠ্যসূচি বা অধ্যায়গুলোর ওপর বেশি গুরুত্ব দিয়ে অনুষ্ঠিত হয়। তবে মৌলিক দক্ষতার কিছু টপিক প্রথম অধ্যায়ের সাথে সম্পর্কিত থাকতে পারে।
</div>
</details>

<details style="margin: 14px 0; padding: 16px 20px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; font-family: 'SolaimanLipi', Arial, sans-serif; cursor: pointer; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
<summary style="font-weight: 700; color: #1e3a8a; font-size: 17px; outline: none;">
প্রশ্ন ৪: সৃজনশীল ও বহুনির্বাচনি (MCQ) অংশে কি আলাদা আলাদা পাস করতে হবে?
</summary>
<div style="margin-top: 12px; padding-top: 10px; border-top: 1px dashed #cbd5e1; color: #334155; font-size: 15.5px; line-height: 1.8;">
উত্তর: হ্যাঁ, ৮ম ও ৯ম শ্রেণির ক্ষেত্রে বোর্ড পরীক্ষা কাঠামোর অনুরূপ লিখিত (সৃজনশীল) ও বহুনির্বাচনি (MCQ) উভয় অংশে পৃথকভাবে পাস নম্বর (৩৩%) অর্জন করা বাধ্যতামূলক।
</div>
</details>

<details style="margin: 14px 0; padding: 16px 20px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; font-family: 'SolaimanLipi', Arial, sans-serif; cursor: pointer; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
<summary style="font-weight: 700; color: #1e3a8a; font-size: 17px; outline: none;">
প্রশ্ন ৫: ২০২৬ সালের মাধ্যমিক পর্যায়ের বার্ষিক পরীক্ষার সময়সূচি বা রুটিন কবে প্রকাশ করা হবে?
</summary>
<div style="margin-top: 12px; padding-top: 10px; border-top: 1px dashed #cbd5e1; color: #334155; font-size: 15.5px; line-height: 1.8;">
উত্তর: মাউশির একাডেমিক ক্যালেন্ডার অনুযায়ী বার্ষিক পরীক্ষা সাধারণত নভেম্বর মাসের শেষ সপ্তাহ থেকে শুরু হয়ে ডিসেম্বরের দ্বিতীয় সপ্তাহের মধ্যে সমাপ্ত হয়। বিদ্যালয়গুলো অক্টোবর মাসের শেষ দিকে পূর্ণাঙ্গ সময়সূচি প্রকাশ করবে।
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
      মাধ্যমিক, উচ্চমাধ্যমিক ও উচ্চতর অ্যাকাডেমিক পাঠ্যক্রম পর্যালোচনায় দীর্ঘ এক দশকের অভিজ্ঞতাসম্পন্ন একজন অ্যাকাডেমিক মেন্টর ও শিক্ষা গবেষক।
    </p>
  </div>
</div>

<!-- Schema.org Microdata: BlogPosting -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "৬ষ্ঠ, ৭ম, ৮ম ও ৯ম শ্রেণির বার্ষিক পরীক্ষার মানবণ্টন ও পূর্ণাঙ্গ প্রস্তুতি গাইড ২০২৬",
  "description": "২০২৬ শিক্ষাবর্ষের ৬ষ্ঠ, ৭ম, ৮ম ও ৯ম শ্রেণির বার্ষিক পরীক্ষার মাউশি নির্দেশিত নতুন মানবণ্টন, ৭০% সামষ্টিক ও ৩০% শিখনকালীন মূল্যায়ন পদ্ধতি এবং পরীক্ষায় এ প্লাস (A+) পাওয়ার বিষয়ভিত্তিক পূর্ণাঙ্গ প্রস্তুতি গাইড।",
  "image": "{HERO_BANNER}",
  "datePublished": "2026-10-03T12:40:00+06:00",
  "dateModified": "2026-10-03T12:40:00+06:00",
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
    "@id": "https://www.helptrickbd.com/2026/10/class-6-to-9-annual-exam-marks-distribution-2026.html"
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
      "name": "২০২৬ সালের বার্ষিক পরীক্ষায় কি কোনো বিষয়ে ফেল করলে পরবর্তী ক্লাসে ওঠা যাবে?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "সরকারি বিধিমালা অনুযায়ী বাধ্যতামূলক বিষয়গুলোতে পাস নম্বর (ন্যূনতম ৩৩ বা 'D' গ্রেড) অর্জন করা আবশ্যক। অকৃতকার্য হলে বিদ্যালয় অ্যাকাডেমিক কাউন্সিলের সিদ্ধান্ত অনুযায়ী ব্যবস্থা গ্রহণ করা হয়।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "শিখনকালীন ৩০ নম্বরের খাতা ও অ্যাসাইনমেন্ট কবে জমা দিতে হবে?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "বার্ষিক লিখিত পরীক্ষা শুরু হওয়ার অন্তত ৭ থেকে ১০ দিন পূর্বেই শ্রেণি শিক্ষকের নিকট শিখনকালীন মূল্যায়নের যাবতীয় অ্যাসাইনমেন্ট ও ব্যবহারিক ফাইল জমা দিতে হবে।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "বার্ষিক পরীক্ষা কি পুরো পাঠ্যবইয়ের ওপর অনুষ্ঠিত হবে নাকি সংক্ষিপ্ত সিলেবাসে?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "এনসিটিবি ও মাউশির নির্দেশনা অনুযায়ী বার্ষিক পরীক্ষা সাধারণত বছরের দ্বিতীয় অর্ধে পঠিত পাঠ্যসূচি ও অধ্যায়গুলোর ওপর বেশি গুরুত্ব দিয়ে অনুষ্ঠিত হয়।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "সৃজনশীল ও বহুনির্বাচনি (MCQ) অংশে কি আলাদা আলাদা পাস করতে হবে?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "হ্যাঁ, ৮ম ও ৯ম শ্রেণির ক্ষেত্রে বোর্ড পরীক্ষা কাঠামোর অনুরূপ লিখিত (সৃজনশীল) ও বহুনির্বাচনি (MCQ) উভয় অংশে পৃথকভাবে পাস নম্বর (৩৩%) অর্জন করা বাধ্যতামূলক।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "২০২৬ সালের মাধ্যমিক পর্যায়ের বার্ষিক পরীক্ষার সময়সূচি বা রুটিন কবে প্রকাশ করা হবে?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "বার্ষিক পরীক্ষা সাধারণত নভেম্বর মাসের শেষ সপ্তাহ থেকে শুরু হয়ে ডিসেম্বরের দ্বিতীয় সপ্তাহের মধ্যে সমাপ্ত হয়। বিদ্যালয়গুলো অক্টোবর মাসের শেষ দিকে পূর্ণাঙ্গ সময়সূচি প্রকাশ করে থাকে।"
      }}
    }}
  ]
}}
</script>
"""
    return full_html

def main():
    print("=" * 70)
    print("GENERATING MASTER ARTICLE: CLASS 6-9 ANNUAL EXAM MARKS DISTRIBUTION 2026")
    print("=" * 70)

    html_content = generate_master_post()

    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html_content)

    meta_content = {
        "title": "৬ষ্ঠ, ৭ম, ৮ম ও ৯ম শ্রেণির বার্ষিক পরীক্ষার মানবণ্টন ও পূর্ণাঙ্গ প্রস্তুতি গাইড ২০২৬",
        "english_slug": "class-6-to-9-annual-exam-marks-distribution-2026",
        "category": "Education Guide",
        "labels": ["Education Guide", "Education"],
        "status": "draft",
        "meta_description": "২০২৬ শিক্ষাবর্ষের ৬ষ্ঠ, ৭ম, ৮ম ও ৯ম শ্রেণির বার্ষিক পরীক্ষার মাউশি নির্দেশিত নতুন মানবণ্টন, ৭০% সামষ্টিক ও ৩০% শিখনকালীন মূল্যায়ন পদ্ধতি এবং পরীক্ষায় এ প্লাস (A+) পাওয়ার বিষয়ভিত্তিক পূর্ণাঙ্গ প্রস্তুতি গাইড।",
        "search_description": "৬ষ্ঠ, ৭ম, ৮ম ও ৯ম শ্রেণির বার্ষিক পরীক্ষার মানবণ্টন ২০২৬: মাউশি নির্দেশিত ৭০% সামষ্টিক ও ৩০% শিখনকালীন মূল্যায়ন এবং এ প্লাস পাওয়ার প্রস্তুতি গাইড।",
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
