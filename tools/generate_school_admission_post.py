#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/generate_school_admission_post.py
-----------------------------------------
Generates the comprehensive, high-ranking, 100/100 Rank Math SEO compliant article:
স্কুল ভর্তি লটারি ও লিখিত পরীক্ষা ২০২৭: ১ম শ্রেণিতে লটারি, ২য়-৯ম শ্রেণিতে লিখিত পরীক্ষার মানবণ্টন ও Best Complete Guide (gsa.teletalk.com.bd)
"""

import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output_posts")
os.makedirs(OUTPUT_DIR, exist_ok=True)

primary_kw = "স্কুল ভর্তি লটারি ২০২৭"
secondary_kw = "school admission lottery exam guide 2027"
full_focus_kw = f"{primary_kw}, {secondary_kw}"

title = "স্কুল ভর্তি লটারি ২০২৭: ১ম শ্রেণিতে লটারি, ২য়-৯ম শ্রেণিতে লিখিত পরীক্ষার মানবণ্টন ও Best Complete Guide (gsa.teletalk.com.bd)"
slug = "school-admission-lottery-exam-guide-2027"
meta_desc = "স্কুল ভর্তি লটারি ২০২৭ নীতিমালা জারি। ১ম শ্রেণিতে ডিজিটাল লটারি, ২য়-৯ম শ্রেণিতে লিখিত পরীক্ষার মানবণ্টন ও gsa.teletalk.com.bd আবেদন নির্দেশিকা।"

banner_cdn = "https://www.helptrickbd.com/wp-content/uploads/2026/10/school_admission_lottery_exam_guide_2027.webp"
banner_local = os.path.join(PROJECT_ROOT, "assets", "images", "posts", "school_admission_lottery_exam_guide_2027.webp")

html_content = f"""<figure style="margin: 0 0 25px 0; text-align: center;">
<img src="{banner_cdn}" alt="{primary_kw} ১ম শ্রেণি লটারি ও ২য়-৯ম শ্রেণি লিখিত পরীক্ষার মানবণ্টন" title="{primary_kw}" style="width: 100%; max-width: 1000px; height: auto; border-radius: 12px; box-shadow: 0 5px 20px rgba(0,0,0,0.12); display: block; margin: 0 auto;" loading="eager" />
<figcaption style="font-size: 13px; color: #64748b; margin-top: 8px; font-family: 'SolaimanLipi', sans-serif;">{primary_kw} এর নীতিমালা, ১ম শ্রেণির ডিজিটাল লটারি, ২য়-৯ম শ্রেণির লিখিত পরীক্ষার মানবণ্টন ও gsa.teletalk.com.bd আবেদন নির্দেশিকা</figcaption>
</figure>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 17.5px; line-height: 1.85; color: #1e293b; margin-bottom: 16px;">
দেশের সকল সরকারি ও বেসরকারি মাধ্যমিক বিদ্যালয়ে ২০২৭ শিক্ষাবর্ষে শিক্ষার্থী ভর্তির লক্ষ্যে বহুল প্রতীক্ষিত <strong>{primary_kw}</strong> এবং ভর্তি নীতিমালা আনুষ্ঠানিকভাবে জারি করেছে শিক্ষা মন্ত্রণালয় ও মাধ্যমিক ও উচ্চশিক্ষা অধিদপ্তর (DSHE)। দীর্ঘ কয়েক বছর যাবত ১ম থেকে ৯ম শ্রেণি পর্যন্ত শতভাগ ডিজিটাল লটারির মাধ্যমে শিক্ষার্থী ভর্তি করা হলেও এবারের নীতিমালায় এসেছে এক ঐতিহাসিক ও যুগান্তকারী পরিবর্তন।
</p>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 17px; line-height: 1.85; color: #334155; margin-bottom: 20px;">
নতুন নীতিমালা অনুযায়ী, প্রথম শ্রেণিতে কেন্দ্রীয় ডিজিটাল লটারি পদ্ধতি বহাল থাকলেও দ্বিতীয় থেকে নবম শ্রেণির শূন্য আসনে লটারি বাতিল করে সরাসরি লিখিত ভর্তি পরীক্ষা পুনরায় চালু করার ঐতিহাসিক সিদ্ধান্ত গ্রহণ করা হয়েছে। টেলিটকের সেন্ট্রালাইজড অনলাইন পোর্টাল <strong>gsa.teletalk.com.bd</strong>-এর মাধ্যমে সারাদেশের সরকারি ও বেসরকারি স্কুলগুলোতে একযোগে এই ভর্তি কার্যক্রম পরিচালিত হবে। নিচে <strong>{primary_kw}</strong> এর আবেদন ও পরীক্ষার পূর্ণাঙ্গ Best Complete Guide বিস্তারিতভাবে তুলে ধরা হলো।
</p>

<!--more-->

<!-- Highlights At a Glance Box -->
<div style="background: #f0fdfa; border-left: 5px solid #0f766e; padding: 22px 25px; border-radius: 0 12px 12px 0; margin: 30px 0; box-shadow: 0 2px 10px rgba(0,0,0,0.04); font-family: 'SolaimanLipi', sans-serif;">
<h3 style="margin-top: 0; color: #115e59; font-size: 20px; font-weight: 700; margin-bottom: 12px;">{primary_kw} একনজরে | Highlights at a Glance</h3>
<ul style="margin: 0; padding-left: 20px; color: #134e4a; line-height: 1.85; font-size: 16px;">
<li><strong>নীতিমালা প্রণয়নকারী কর্তৃপক্ষ:</strong> মাধ্যমিক ও উচ্চশিক্ষা বিভাগ, শিক্ষা মন্ত্রণালয় (<a href="https://shed.gov.bd/" target="_blank" rel="noopener noreferrer" style="color: #0f766e; text-decoration: underline; font-weight: bold;">SHED</a>) এবং মাধ্যমিক ও উচ্চশিক্ষা অধিদপ্তর (<a href="http://www.dshe.gov.bd/" target="_blank" rel="noopener noreferrer" style="color: #0f766e; text-decoration: underline; font-weight: bold;">DSHE</a>)।</li>
<li><strong>ভর্তি কার্যক্রমের আওতা:</strong> দেশের সকল মহানগরী, জেলা সদর ও উপজেলা পর্যায়ের সরকারি এবং বেসরকারি মাধ্যমিক বিদ্যালয়।</li>
<li><strong>১ম শ্রেণির নির্বাচন পদ্ধতি:</strong> ১০০% কেন্দ্রীয় ডিজিটাল লটারি (কোনো ভর্তি পরীক্ষা নেওয়া হবে না)।</li>
<li><strong>২য় থেকে ৯ম শ্রেণির নির্বাচন পদ্ধতি:</strong> মেধাভিত্তিক লিখিত ভর্তি পরীক্ষা (লটারি পদ্ধতি বাতিল)।</li>
<li><strong>লিখিত পরীক্ষার মানবণ্টন:</strong> ২য়-৫ম শ্রেণি ৫০ নম্বর (১ ঘণ্টা); ৬ষ্ঠ-৯ম শ্রেণি ১০০ নম্বর (২ ঘণ্টা)।</li>
<li><strong>অনলাইন আবেদন পোর্টাল:</strong> টেলিটকের অফিসিয়াল সেন্ট্রাল ওয়েবসাইট <a href="https://gsa.teletalk.com.bd/" target="_blank" rel="noopener noreferrer" style="color: #0f766e; text-decoration: underline; font-weight: bold;">gsa.teletalk.com.bd</a>।</li>
<li><strong>স্কুল পছন্দক্রমের সংখ্যা:</strong> একজন শিক্ষার্থী অনলাইনে আবেদনের সময় সর্বোচ্চ ৫টি বিদ্যালয় পছন্দক্রম (Choice List) দিতে পারবে।</li>
<li><strong>১ম শ্রেণির বয়সসীমা:</strong> ১ জানুয়ারি ২০২৭ তারিখে সর্বনিম্ন ৫ বছর এবং সর্বোচ্চ ৭ বছর (৬+ বছর নিশ্চিত করতে হবে)।</li>
<li><strong>প্রাসঙ্গিক গাইডলাইন:</strong> আমাদের ওয়েবসাইটের <a href="https://www.helptrickbd.com/primary-scholarship-exam-routine-2026/" style="color: #0f766e; text-decoration: underline; font-weight: bold;">প্রাথমিক বৃত্তি পরীক্ষার রুটিন ও গাইড</a>, <a href="https://www.helptrickbd.com/class-8-junior-scholarship-exam-routine-suggestion-2026/" style="color: #0f766e; text-decoration: underline; font-weight: bold;">৮ম শ্রেণির জুনিয়র বৃত্তি পরীক্ষা ২০২৬</a> এবং <a href="https://www.helptrickbd.com/class-6-to-9-annual-exam-marks-distribution-2026/" style="color: #0f766e; text-decoration: underline; font-weight: bold;">৬ষ্ঠ থেকে ৯ম শ্রেণির বার্ষিক পরীক্ষার মানবণ্টন</a> দেখে নিতে পারেন।</li>
</ul>
</div>

<!-- Table of Contents -->
<div class="htbd-toc-box wp-block-rank-math-toc-block" id="rank-math-toc" style="background: #f8fafc; border: 1.5px solid #0f766e; border-radius: 12px; padding: 22px 25px; margin: 30px 0; font-family: 'SolaimanLipi', sans-serif; box-shadow: 0 2px 10px rgba(0,0,0,0.04);">
  <div style="font-weight: 700; font-size: 19px; color: #0f766e; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
    <span>সূচিপত্র (Table of Contents)</span>
  </div>
  <p style="margin: 0 0 12px 0; color: #475569; font-size: 15px;">
    নিচে ২০২৭ শিক্ষাবর্ষের সরকারি ও বেসরকারি স্কুল ভর্তি নীতিমালা, ১ম শ্রেণির লটারি, ২য়-৯ম শ্রেণির লিখিত পরীক্ষার মানবণ্টন ও অনলাইন আবেদন পদ্ধতির বিষয়ভিত্তিক সূচি দেওয়া হলো:
  </p>
  <ol style="margin: 0; padding-left: 22px; color: #334155; line-height: 2; font-size: 15.5px;">
    <li><a href="#section-1" style="color: #0f766e; text-decoration: none; font-weight: 600;">{primary_kw} নীতিমালা ২০২৭: ঐতিহাসিক প্রেক্ষাপট ও বড় পরিবর্তনসমূহ</a></li>
    <li><a href="#section-2" style="color: #0f766e; text-decoration: none; font-weight: 600;">১ম শ্রেণি ডিজিটাল লটারি বনাম ২য়-৯ম শ্রেণি লিখিত পরীক্ষা: পূর্ণাঙ্গ তুলনামূলক সারণি</a></li>
    <li><a href="#section-3" style="color: #0f766e; text-decoration: none; font-weight: 600;">২য় থেকে ৯ম শ্রেণির লিখিত ভর্তি পরীক্ষার বিস্তারিত বিষয়ভিত্তিক মানবণ্টন ও সিলেবাস</a></li>
    <li><a href="#section-4" style="color: #0f766e; text-decoration: none; font-weight: 600;">জাতীয় শিক্ষানীতি ২০১০ অনুযায়ী শ্রেণিভিত্তিক বয়সসীমা ও অনলাইন জন্ম নিবন্ধন নিয়ম</a></li>
    <li><a href="#section-5" style="color: #0f766e; text-decoration: none; font-weight: 600;">gsa.teletalk.com.bd পোর্টালে ধাপে ধাপে অনলাইন আবেদন ফরম পূরণের নিয়ম</a></li>
    <li><a href="#section-6" style="color: #0f766e; text-decoration: none; font-weight: 600;">কোটা বণ্টন ব্যবস্থা: মুক্তিযোদ্ধা, এলাকা (ক্যাচমেন্ট) ও বিশেষ চাহিদাসম্পন্ন আসন</a></li>
    <li><a href="#section-7" style="color: #0f766e; text-decoration: none; font-weight: 600;">মেধা তালিকা, অপেক্ষমাণ তালিকা (Waiting List) ও ভর্তি নিশ্চিতকরণের নিয়মাবলী</a></li>
    <li><a href="#section-8" style="color: #0f766e; text-decoration: none; font-weight: 600;">সচরাচর জিজ্ঞাসিত প্রশ্নাবলী (FAQ)</a></li>
  </ol>
</div>

<h2 id="section-1" style="font-family: 'SolaimanLipi', sans-serif; font-size: 24px; color: #0f172a; border-bottom: 2px solid #0f766e; padding-bottom: 8px; margin-top: 40px;">১. {primary_kw} নীতিমালা ২০২৭: ঐতিহাসিক প্রেক্ষাপট ও বড় পরিবর্তনসমূহ</h2>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16.5px; line-height: 1.85; color: #334155; margin-bottom: 16px;">
বাংলাদেশে করোনা মহামারির সময় বিদ্যালয়গুলোতে শারীরিক উপস্থিতিতে পরীক্ষা নেওয়ার ঝুঁকি এড়াতে এবং ভর্তি বাণিজ্য বন্ধ করার লক্ষ্যে ১ম থেকে ৯ম শ্রেণি পর্যন্ত লটারি পদ্ধতি চালু করা হয়েছিল। তবে বিগত কয়েক বছরের লটারি প্রক্রিয়ার ফলে মেধার সঠিক মূল্যায়ন না হওয়া নিয়ে শিক্ষক, শিক্ষাবিদ ও অভিভাবকদের পক্ষ থেকে আপত্তি তৈরি হয়।
</p>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16.5px; line-height: 1.85; color: #334155; margin-bottom: 16px;">
এসব বাস্তব পর্যবেক্ষণ ও বিশেষজ্ঞ কমিটির সুপারিশের ভিত্তিতে শিক্ষা মন্ত্রণালয়ের মাধ্যমিক ও উচ্চশিক্ষা বিভাগ নতুন নীতিমালায় বৈপ্লবিক সংস্কার এনেছে। মন্ত্রণালয়ের সিদ্ধান্ত অনুযায়ী, ছোট শিশুদের মানসিক চাপমুক্ত রাখতে এন্ট্রি শ্রেণি হিসেবে কেবল <strong>প্রথম শ্রেণিতে ডিজিটাল লটারি</strong> কার্যকর থাকবে। কিন্তু দ্বিতীয় শ্রেণি থেকে নবম শ্রেণি পর্যন্ত প্রতিটি শ্রেণিতে মেধার ভিত্তিতে যোগ্য শিক্ষার্থী বাছাই নিশ্চিত করতে <strong>লিখিত ভর্তি পরীক্ষা</strong> পুনরায় বাধ্যতামূলক করা হয়েছে।
</p>

<div style="background: #fffbeb; border-left: 4px solid #f59e0b; padding: 18px 20px; border-radius: 0 8px 8px 0; margin: 25px 0; font-family: 'SolaimanLipi', sans-serif;">
<p style="margin: 0; color: #92400e; font-size: 15.5px; line-height: 1.75;">
<strong>সতর্কবার্তা ও দিকনির্দেশনা:</strong> কোনো শিক্ষা প্রতিষ্ঠান নিজস্ব উদ্যোগে আলাদাভাবে ভর্তি ফরম বিক্রি করতে পারবে না। সরকারি কিংবা বেসরকারি যেকোনো অনুমোদিত বিদ্যালয়ে ভর্তির জন্য অভিভাবক ও শিক্ষার্থীকে অবশ্যই সরকারি সেন্ট্রালাইজড ওয়েবসাইট <code>gsa.teletalk.com.bd</code>-এর মাধ্যমেই আবেদন সম্পন্ন করতে হবে।
</p>
</div>

<h2 id="section-2" style="font-family: 'SolaimanLipi', sans-serif; font-size: 24px; color: #0f172a; border-bottom: 2px solid #0f766e; padding-bottom: 8px; margin-top: 40px;">২. ১ম শ্রেণি ডিজিটাল লটারি বনাম ২য়-৯ম শ্রেণি লিখিত পরীক্ষা: পূর্ণাঙ্গ তুলনামূলক সারণি</h2>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16.5px; line-height: 1.85; color: #334155; margin-bottom: 16px;">
অনেক অভিভাবক এখনো বিভ্রান্তিতে আছেন কোন শ্রেণিতে লটারি হবে আর কোন শ্রেণিতে লিখিত পরীক্ষা হবে। নিচে ২০২৭ শিক্ষাবর্ষের ভর্তি নীতিমালার আলোকে শ্রেণিভিত্তিক পূর্ণাঙ্গ কাঠামোগত তুলনামূলক তালিকা উপস্থাপন করা হলো:
</p>

<div style="overflow-x: auto; margin: 25px 0;">
<table style="width: 100%; border-collapse: collapse; font-family: 'SolaimanLipi', sans-serif; font-size: 15.5px; background: #ffffff; box-shadow: 0 2px 8px rgba(0,0,0,0.06); border-radius: 8px; overflow: hidden;">
<thead>
<tr style="background: #024a4d; color: #ffffff; text-align: left;">
<th style="padding: 14px 16px; border: 1px solid #046c70;">শ্রেণি (Class)</th>
<th style="padding: 14px 16px; border: 1px solid #046c70;">ভর্তি নির্বাচন পদ্ধতি</th>
<th style="padding: 14px 16px; border: 1px solid #046c70;">পরীক্ষার পূর্ণমান</th>
<th style="padding: 14px 16px; border: 1px solid #046c70;">পরীক্ষার সময়</th>
<th style="padding: 14px 16px; border: 1px solid #046c70;">বিষয়ভিত্তিক নম্বর বিন্যাস</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
<td style="padding: 12px 16px; font-weight: bold; color: #0f172a;">প্রথম শ্রেণি (Class 1)</td>
<td style="padding: 12px 16px; color: #047857; font-weight: bold;">১০০% ডিজিটাল লটারি</td>
<td style="padding: 12px 16px; color: #64748b;">পরীক্ষা নেই (N/A)</td>
<td style="padding: 12px 16px; color: #64748b;">প্রযোজ্য নয়</td>
<td style="padding: 12px 16px; color: #334155;">সফটওয়্যার র‍্যান্ডম লটারি সিলেকশন</td>
</tr>
<tr style="border-bottom: 1px solid #e2e8f0;">
<td style="padding: 12px 16px; font-weight: bold; color: #0f172a;">দ্বিতীয় শ্রেণি (Class 2)</td>
<td style="padding: 12px 16px; color: #b91c1c; font-weight: bold;">লিখিত ভর্তি পরীক্ষা</td>
<td style="padding: 12px 16px; font-weight: bold; color: #024a4d;">৫০ নম্বর</td>
<td style="padding: 12px 16px;">১ ঘণ্টা</td>
<td style="padding: 12px 16px; color: #334155;">বাংলা ১৫ + ইংরেজি ১৫ + গণিত ২০</td>
</tr>
<tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
<td style="padding: 12px 16px; font-weight: bold; color: #0f172a;">তৃতীয় শ্রেণি (Class 3)</td>
<td style="padding: 12px 16px; color: #b91c1c; font-weight: bold;">লিখিত ভর্তি পরীক্ষা</td>
<td style="padding: 12px 16px; font-weight: bold; color: #024a4d;">৫০ নম্বর</td>
<td style="padding: 12px 16px;">১ ঘণ্টা</td>
<td style="padding: 12px 16px; color: #334155;">বাংলা ১৫ + ইংরেজি ১৫ + গণিত ২০</td>
</tr>
<tr style="border-bottom: 1px solid #e2e8f0;">
<td style="padding: 12px 16px; font-weight: bold; color: #0f172a;">চতুর্থ শ্রেণি (Class 4)</td>
<td style="padding: 12px 16px; color: #b91c1c; font-weight: bold;">লিখিত ভর্তি পরীক্ষা</td>
<td style="padding: 12px 16px; font-weight: bold; color: #024a4d;">৫০ নম্বর</td>
<td style="padding: 12px 16px;">১ ঘণ্টা</td>
<td style="padding: 12px 16px; color: #334155;">বাংলা ১৫ + ইংরেজি ১৫ + গণিত ২০</td>
</tr>
<tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
<td style="padding: 12px 16px; font-weight: bold; color: #0f172a;">পঞ্চম শ্রেণি (Class 5)</td>
<td style="padding: 12px 16px; color: #b91c1c; font-weight: bold;">লিখিত ভর্তি পরীক্ষা</td>
<td style="padding: 12px 16px; font-weight: bold; color: #024a4d;">৫০ নম্বর</td>
<td style="padding: 12px 16px;">১ ঘণ্টা</td>
<td style="padding: 12px 16px; color: #334155;">বাংলা ১৫ + ইংরেজি ১৫ + গণিত ২০</td>
</tr>
<tr style="border-bottom: 1px solid #e2e8f0;">
<td style="padding: 12px 16px; font-weight: bold; color: #0f172a;">ষষ্ঠ শ্রেণি (Class 6)</td>
<td style="padding: 12px 16px; color: #b91c1c; font-weight: bold;">লিখিত ভর্তি পরীক্ষা</td>
<td style="padding: 12px 16px; font-weight: bold; color: #024a4d;">১০০ নম্বর</td>
<td style="padding: 12px 16px;">২ ঘণ্টা</td>
<td style="padding: 12px 16px; color: #334155;">বাংলা ৩০ + ইংরেজি ৩০ + গণিত ৪০</td>
</tr>
<tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
<td style="padding: 12px 16px; font-weight: bold; color: #0f172a;">সপ্তম শ্রেণি (Class 7)</td>
<td style="padding: 12px 16px; color: #b91c1c; font-weight: bold;">লিখিত ভর্তি পরীক্ষা</td>
<td style="padding: 12px 16px; font-weight: bold; color: #024a4d;">১০০ নম্বর</td>
<td style="padding: 12px 16px;">২ ঘণ্টা</td>
<td style="padding: 12px 16px; color: #334155;">বাংলা ৩০ + ইংরেজি ৩০ + গণিত ৪০</td>
</tr>
<tr style="border-bottom: 1px solid #e2e8f0;">
<td style="padding: 12px 16px; font-weight: bold; color: #0f172a;">অষ্টম শ্রেণি (Class 8)</td>
<td style="padding: 12px 16px; color: #b91c1c; font-weight: bold;">লিখিত ভর্তি পরীক্ষা</td>
<td style="padding: 12px 16px; font-weight: bold; color: #024a4d;">১০০ নম্বর</td>
<td style="padding: 12px 16px;">২ ঘণ্টা</td>
<td style="padding: 12px 16px; color: #334155;">বাংলা ৩০ + ইংরেজি ৩০ + গণিত ৪০</td>
</tr>
<tr style="background: #ffffff;">
<td style="padding: 12px 16px; font-weight: bold; color: #0f172a;">নবম শ্রেণি (Class 9)</td>
<td style="padding: 12px 16px; color: #b91c1c; font-weight: bold;">লিখিত ভর্তি পরীক্ষা</td>
<td style="padding: 12px 16px; font-weight: bold; color: #024a4d;">১০০ নম্বর</td>
<td style="padding: 12px 16px;">২ ঘণ্টা</td>
<td style="padding: 12px 16px; color: #334155;">বাংলা ৩০ + ইংরেজি ৩০ + গণিত ৪০</td>
</tr>
</tbody>
</table>
</div>

<h2 id="section-3" style="font-family: 'SolaimanLipi', sans-serif; font-size: 24px; color: #0f172a; border-bottom: 2px solid #0f766e; padding-bottom: 8px; margin-top: 40px;">৩. ২য় থেকে ৯ম শ্রেণির লিখিত ভর্তি পরীক্ষার বিস্তারিত বিষয়ভিত্তিক মানবণ্টন ও সিলেবাস</h2>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16.5px; line-height: 1.85; color: #334155; margin-bottom: 16px;">
মাউশির নতুন নির্দেশিকা অনুসারে, শিক্ষার্থী যে শ্রেণিতে ভর্তি হতে আবেদন করবে, তার ঠিক পূর্ববর্তী শ্রেণির জাতীয় শিক্ষাক্রম ও পাঠ্যপুস্তক বোর্ড (NCTB) প্রণীত মূল পাঠ্যবই থেকেই প্রশ্নপত্র প্রণয়ন করা হবে। যেমন—ষষ্ঠ শ্রেণিতে ভর্তির পরীক্ষার প্রশ্ন হবে ৫ম শ্রেণির পাঠ্যবই থেকে; আবার ৯ম শ্রেণিতে ভর্তির পরীক্ষা হবে ৮ম শ্রেণির পাঠ্যবইয়ের ওপর।
</p>

<h3 style="font-family: 'SolaimanLipi', sans-serif; font-size: 20px; color: #024a4d; margin-top: 25px; margin-bottom: 12px;">ক) ২য় থেকে ৫ম শ্রেণির লিখিত পরীক্ষার মানবণ্টন (পূর্ণমান: ৫০ নম্বর)</h3>
<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16px; line-height: 1.8; color: #334155; margin-bottom: 14px;">
প্রাথমিক স্তরের শিক্ষার্থীদের জন্য ৫০ নম্বরের লিখিত পরীক্ষা অনুষ্ঠিত হবে ১ ঘণ্টার মধ্যে। বিষয়ভিত্তিক বিভাজন নিচে দেওয়া হলো:
</p>
<ul style="font-family: 'SolaimanLipi', sans-serif; font-size: 16px; line-height: 1.85; color: #1e293b; padding-left: 20px; margin-bottom: 20px;">
<li><strong>বাংলা (১৫ নম্বর):</strong> শব্দার্থ, বাক্য গঠন, যুক্তবর্ণ বিভাজন ও বাক্যে প্রয়োগ, কবিতার চরণ পূরণ, অনুচ্ছেদ পড়ে প্রশ্নের উত্তর লিখন।</li>
<li><strong>ইংরেজি (১৫ নম্বর):</strong> Meaning of words, Making sentences, Spelling, Fill in the blanks with correct prepositions/articles, Re-arrange jumbled words, Simple short translation.</li>
<li><strong>গণিত (২০ নম্বর):</strong> যোগ, বিয়োগ, গুণ, ভাগের সাধারণ সমস্যা, নামতাভিত্তিক ছোট ছোট সমাধান, বয়স ও সময় গণনা, এবং পাঠ্যবইয়ের সাধারণ জ্যামিতিক চিত্র পরিচিতি।</li>
</ul>

<h3 style="font-family: 'SolaimanLipi', sans-serif; font-size: 20px; color: #024a4d; margin-top: 25px; margin-bottom: 12px;">খ) ৬ষ্ঠ থেকে ৯ম শ্রেণির লিখিত পরীক্ষার মানবণ্টন (পূর্ণমান: ১০০ নম্বর)</h3>
<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16px; line-height: 1.8; color: #334155; margin-bottom: 14px;">
মাধ্যমিক স্তরের উচ্চতর শ্রেণির জন্য ১০০ নম্বরের পূর্ণাঙ্গ লিখিত পরীক্ষা নেওয়া হবে এবং সময় বরাদ্দ থাকবে ২ ঘণ্টা। মানবণ্টন নিম্নরূপ:
</p>
<ul style="font-family: 'SolaimanLipi', sans-serif; font-size: 16px; line-height: 1.85; color: #1e293b; padding-left: 20px; margin-bottom: 20px;">
<li><strong>বাংলা (৩০ নম্বর):</strong> ব্যাকরণ অংশ (সন্ধি, সমাস, কারক ও বিভক্তি, এককথায় প্রকাশ, বাগধারা), অনুধাবনমূলক প্রশ্ন, সারাংশ/সারমর্ম লিখন এবং পাঠ্যবইয়ের গল্প ও কবিতার মূলভাবভিত্তিক বিশ্লেষণ।</li>
<li><strong>ইংরেজি (৩০ নম্বর):</strong> Grammar (Parts of speech, Right form of verbs, Voice change, Prepositions, Tense and punctuation), Reading comprehension, Paragraph writing / Informal letter, Translation from Bengali to English.</li>
<li><strong>গণিত (৪০ নম্বর):</strong> পাটিগণিত (ঐকিক নিয়ম, লাভ-ক্ষতি, শতকরা, অনুপাত), বীজগণিত (সূত্র প্রয়োগ, উৎপাদকে বিশ্লেষণ, মান নির্ণয়, সমীকরণ গঠন ও সমাধান) এবং জ্যামিতি (উপপাদ্য ও সম্পাদ্যের সাধারণ ধারণা এবং ক্ষেত্রফল পরিমাপ)।</li>
</ul>

<h2 id="section-4" style="font-family: 'SolaimanLipi', sans-serif; font-size: 24px; color: #0f172a; border-bottom: 2px solid #0f766e; padding-bottom: 8px; margin-top: 40px;">৪. জাতীয় শিক্ষানীতি অনুযায়ী শ্রেণিভিত্তিক বয়সসীমা ও অনলাইন জন্ম নিবন্ধন নিয়ম</h2>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16.5px; line-height: 1.85; color: #334155; margin-bottom: 16px;">
{primary_kw}-র ক্ষেত্রে সবচেয়ে বড় জটিলতা তৈরি হয় বয়স নির্ধারণ নিয়ে। শিক্ষা মন্ত্রণালয়ের সরকারি নীতিমালা অনুযায়ী জাতীয় শিক্ষানীতি ২০১০-এর বয়স কাঠামো কঠোরভাবে অনুসরণ করা বাধ্যতামূলক। বিশেষ করে {primary_kw} আবেদনের সময় জন্ম তারিখের সামান্য ভুলে আবেদন বাতিল হতে পারে:
</p>

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 20px; margin: 20px 0; font-family: 'SolaimanLipi', sans-serif;">
<h4 style="margin-top: 0; color: #024a4d; font-size: 17px; font-weight: 700; margin-bottom: 10px;">শ্রেণিভিত্তিক বয়সসীমা নির্ধারণের মূল সূত্র:</h4>
<ul style="margin: 0; padding-left: 20px; line-height: 1.85; color: #334155; font-size: 15.5px;">
<li><strong>১ম শ্রেণি:</strong> ১ জানুয়ারি ২০২৭ তারিখে শিক্ষার্থীর বয়স সর্বনিম্ন ৫ বছর এবং সর্বোচ্চ ৭ বছর হতে হবে। এর অর্থ হলো শিক্ষার্থীর বয়স অবশ্যই <strong>৫+ বছর থেকে ৭ বছরের নিচে</strong> (আদর্শ বয়স ৬ বছর) হতে হবে।</li>
<li><strong>পরবর্তী শ্রেণিসমূহ (২য় থেকে ৯ম):</strong> ১ম শ্রেণির এই বয়সের ধারাবাহিকতা রক্ষা করে প্রতি শ্রেণির জন্য ১ বছর করে বৃদ্ধি পাবে। অর্থাৎ ২য় শ্রেণিতে ৬+, ৩য় শ্রেণিতে ৭+, ৪র্থ শ্রেণিতে ৮+, ৫ম শ্রেণিতে ৯+, ৬ষ্ঠ শ্রেণিতে ১০+, ৭ম শ্রেণিতে ১১+, ৮ম শ্রেণিতে ১২+ এবং ৯ম শ্রেণিতে ১৩+ বছর সর্বনিম্ন বয়স হতে হবে।</li>
<li><strong>বিশেষ চাহিদাসম্পন্ন (প্রতিবন্ধী) শিক্ষার্থী:</strong> প্রতিবন্ধী বা বিশেষ চাহিদাসম্পন্ন শিশুদের ক্ষেত্রে বয়স নির্ধারণে সর্বোচ্চ <strong>৫ বছর পর্যন্ত অতিরিক্ত শিথিলতা</strong> প্রদান করা হয়েছে।</li>
<li><strong>ডিজিটাল জন্ম নিবন্ধন সনদ (BRN):</strong> আবেদনকারীর জন্ম নিবন্ধন সনদটি অবশ্যই সরকার অনুমোদিত ১৭ ডিজিটের অনলাইন ভেরিফাইড (Online Birth Registration Certificate) হতে হবে। ম্যানুয়াল বা অফলাইন জন্ম সনদ কোনোভাবেই গ্রহণযোগ্য নয়।</li>
</ul>
</div>

<h2 id="section-5" style="font-family: 'SolaimanLipi', sans-serif; font-size: 24px; color: #0f172a; border-bottom: 2px solid #0f766e; padding-bottom: 8px; margin-top: 40px;">৫. gsa.teletalk.com.bd পোর্টালে ধাপে ধাপে অনলাইন আবেদন ফরম পূরণের নিয়ম</h2>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16.5px; line-height: 1.85; color: #334155; margin-bottom: 16px;">
অনলাইনে {primary_kw} আবেদন করার সময় কোনো রকম ভুল হলে পরবর্তীতে তা সংশোধনের সুযোগ থাকে না। নিচে ধাপে ধাপে সঠিক আবেদন ও {primary_kw} ফি পরিশোধের প্রক্রিয়া তুলে ধরা হলো:
</p>

<div style="display: flex; flex-direction: column; gap: 15px; margin: 25px 0; font-family: 'SolaimanLipi', sans-serif;">

<div style="background: #ffffff; border: 1.5px solid #e2e8f0; border-left: 5px solid #0f766e; padding: 18px 20px; border-radius: 8px; box-shadow: 0 1px 4px rgba(0,0,0,0.04);">
<strong style="color: #0f766e; font-size: 17px;">ধাপ ১: অফিসিয়াল পোর্টালে প্রবেশ</strong>
<p style="margin: 6px 0 0 0; color: #334155; font-size: 15.5px; line-height: 1.7;">
যেকোনো ওয়েব ব্রাউজার থেকে সরকারি সেন্ট্রালাইজড ওয়েবসাইট <a href="https://gsa.teletalk.com.bd/" target="_blank" rel="noopener noreferrer" style="color: #0f766e; font-weight: bold; text-decoration: underline;">gsa.teletalk.com.bd</a>-এ প্রবেশ করুন। সেখানে সরকারি বিদ্যালয় এবং বেসরকারি বিদ্যালয়ের আলাদা দুটি অপশন দেখতে পাবেন। আপনি যে ধরনের বিদ্যালয়ে আবেদন করতে চান সেই লিংকে ক্লিক করুন।
</p>
</div>

<div style="background: #ffffff; border: 1.5px solid #e2e8f0; border-left: 5px solid #0f766e; padding: 18px 20px; border-radius: 8px; box-shadow: 0 1px 4px rgba(0,0,0,0.04);">
<strong style="color: #0f766e; font-size: 17px;">ধাপ ২: ব্যক্তিগত তথ্য ও জন্ম নিবন্ধন নম্বর প্রদান</strong>
<p style="margin: 6px 0 0 0; color: #334155; font-size: 15.5px; line-height: 1.7;">
শিক্ষার্থীর নাম (ইংরেজি ও বাংলায়), ১৭ ডিজিটের ডিজিটাল অনলাইন জন্ম নিবন্ধন নম্বর, জন্ম তারিখ, পিতা ও মাতার নাম এবং অভিভাবকের সচল মোবাইল নম্বর নির্ভুলভাবে টাইপ করুন।
</p>
</div>

<div style="background: #ffffff; border: 1.5px solid #e2e8f0; border-left: 5px solid #0f766e; padding: 18px 20px; border-radius: 8px; box-shadow: 0 1px 4px rgba(0,0,0,0.04);">
<strong style="color: #0f766e; font-size: 17px;">ধাপ ৩: সর্বোচ্চ ৫টি স্কুল ও শিফট পছন্দক্রম (School Choice List)</strong>
<p style="margin: 6px 0 0 0; color: #334155; font-size: 15.5px; line-height: 1.7;">
একজন শিক্ষার্থী একটি আবেদনপত্রের মাধ্যমে সর্বোচ্চ ৫টি বিদ্যালয় নির্বাচন করতে পারবে। মনে রাখবেন, ডাবল শিফট স্কুলের ক্ষেত্রে মর্নিং শিফট এবং ডে শিফট আলাদাভাবে নির্বাচন করলে তা দুটি স্বতন্ত্র পছন্দ হিসেবে গণ্য হবে।
</p>
</div>

<div style="background: #ffffff; border: 1.5px solid #e2e8f0; border-left: 5px solid #0f766e; padding: 18px 20px; border-radius: 8px; box-shadow: 0 1px 4px rgba(0,0,0,0.04);">
<strong style="color: #0f766e; font-size: 17px;">ধাপ ৪: ছবি আপলোড ও প্রিভিউ চেক</strong>
<p style="margin: 6px 0 0 0; color: #334155; font-size: 15.5px; line-height: 1.7;">
শিক্ষার্থীর সদ্য তোলা রঙিন পাসপোর্ট সাইজের ছবি (৩০০ × ৩০০ পিক্সেল, ফাইল সাইজ সর্বোচ্চ ১০০ কেবি) আপলোড করুন। সাবমিট বাটনে চাপ দেওয়ার আগে অ্যাপ্লিকেশন প্রিভিউটি মনোযোগ দিয়ে দেখে নিন।
</p>
</div>

<div style="background: #ffffff; border: 1.5px solid #e2e8f0; border-left: 5px solid #0f766e; padding: 18px 20px; border-radius: 8px; box-shadow: 0 1px 4px rgba(0,0,0,0.04);">
<strong style="color: #0f766e; font-size: 17px;">ধাপ ৫: টেলিটক প্রিপেইড সিমের মাধ্যমে আবেদন ফি পরিশোধ</strong>
<p style="margin: 6px 0 0 0; color: #334155; font-size: 15.5px; line-height: 1.7;">
আবেদনপত্র সফলভাবে সাবমিট হলে একটি <strong>User ID</strong> সম্বলিত অ্যাপ্লিক্যান্টস কপি পাওয়া যাবে। এরপর টেলিটক সিমের মেসেজ অপশন থেকে নির্দিষ্ট ফরম্যাটে SMS পাঠিয়ে আবেদন ফি পরিশোধ করতে হবে:
<br><br>
<code>১ম SMS: GSA &lt;Space&gt; User ID লিখে পাঠাতে হবে 16222 নম্বরে।</code>
<br>
ফিরতি এসএমএসে প্রাপ্ত পিন নম্বর দিয়ে দ্বিতীয় মেসেজ পাঠাতে হবে:
<br>
<code>২য় SMS: GSA &lt;Space&gt; YES &lt;Space&gt; PIN লিখে পাঠাতে হবে 16222 নম্বরে।</code>
<br><br>
ফি জমা সম্পন্ন হলেই আবেদন চূড়ান্তভাবে গৃহীত হবে এবং ট্র্যাকিং নম্বর নিশ্চিত হবে।
</p>
</div>

</div>

<h2 id="section-6" style="font-family: 'SolaimanLipi', sans-serif; font-size: 24px; color: #0f172a; border-bottom: 2px solid #0f766e; padding-bottom: 8px; margin-top: 40px;">৬. কোটা বণ্টন ব্যবস্থা: মুক্তিযোদ্ধা, এলাকা (ক্যাচমেন্ট) ও বিশেষ চাহিদাসম্পন্ন আসন</h2>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16.5px; line-height: 1.85; color: #334155; margin-bottom: 16px;">
সরকারি মাধ্যমিক বিদ্যালয়ে শিক্ষার্থী ভর্তির ক্ষেত্রে নির্ধারিত কোটা অনুযায়ী আসন সংরক্ষিত থাকে। নীতিমালার প্রধান কোটা কাঠামো নিম্নরূপ:
</p>

<ul style="font-family: 'SolaimanLipi', sans-serif; font-size: 16px; line-height: 1.85; color: #1e293b; padding-left: 20px; margin-bottom: 20px;">
<li><strong>ক্যাচমেন্ট এলাকা (এলাকা কোটা) - ৪০%:</strong> বিদ্যালয় সংলগ্ন নির্দিষ্ট এলাকার স্থায়ী বাসিন্দা শিক্ষার্থীদের জন্য ৪০% আসন সংরক্ষিত থাকে। আবেদনের সময় সংশ্লিষ্ট এলাকার থানা বা ওয়ার্ড স্পষ্টভাবে উল্লেখ করতে হবে।</li>
<li><strong>মুক্তিযোদ্ধা কোটা - ৫%:</strong> বীর মুক্তিযোদ্ধার সন্তান এবং সন্তান না থাকলে নাতি-নাতনিদের জন্য ৫% কোটা সংরক্ষিত থাকবে (যথাযথ সরকারি সনদের প্রমাণপত্র প্রদর্শন সাপেক্ষে)।</li>
<li><strong>বিশেষ চাহিদাসম্পন্ন শিশু কোটা - ২%:</strong> প্রতিবন্ধী বা অটিস্টিক শিক্ষার্থীদের জন্য ২% আসন বরাদ্দ থাকবে।</li>
<li><strong>শিক্ষা মন্ত্রণালয় কোটা - ২%:</strong> শিক্ষা মন্ত্রণালয় এবং এর অধীনস্থ দপ্তর-সংস্থার কর্মকর্তা-কর্মচারীদের সন্তানদের জন্য এই আসন নির্ধারিত।</li>
<li><strong>সহোদর/সহোদরা (ভাই-বোন) কোটা:</strong> কোনো প্রতিষ্ঠানে যদি ইতোমধ্যে কোনো ভাই বা বোন অধ্যয়নরত থাকে, তবে শূন্য আসন সাপেক্ষে ভর্তির বিশেষ অগ্রাধিকার প্রদান করা হয়।</li>
</ul>

<h2 id="section-7" style="font-family: 'SolaimanLipi', sans-serif; font-size: 24px; color: #0f172a; border-bottom: 2px solid #0f766e; padding-bottom: 8px; margin-top: 40px;">৭. মেধা তালিকা, অপেক্ষমাণ তালিকা (Waiting List) ও ভর্তি নিশ্চিতকরণের নিয়মাবলী</h2>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16.5px; line-height: 1.85; color: #334155; margin-bottom: 16px;">
ডিজিটাল লটারি ও লিখিত পরীক্ষার ফলাফল প্রকাশের পর শিক্ষা মন্ত্রণালয় থেকে কেন্দ্রীয়ভাবে নির্বাচিত মেধা তালিকা ওয়েবসাইটে প্রকাশ করা হবে। একই সাথে শূন্য আসনের সমানসংখ্যক শিক্ষার্থীর একটি <strong>অপেক্ষমাণ তালিকা (Waiting List)</strong> প্রকাশ করা বাধ্যতামূলক।
</p>

<div style="background: #f1f5f9; border-radius: 8px; padding: 20px; margin: 20px 0; font-family: 'SolaimanLipi', sans-serif;">
<h4 style="margin-top: 0; color: #0f172a; font-size: 17px; margin-bottom: 10px;">ভর্তি হওয়ার সময় যেসব মূল কাগজপত্র সাথে আনতে হবে:</h4>
<ol style="margin: 0; padding-left: 20px; line-height: 1.8; color: #334155; font-size: 15.5px;">
<li>টেলিটক অনলাইন আবেদনপত্রের রঙিন প্রিন্ট কপি এবং প্রবেশপত্র (Admit Card)।</li>
<li>অনলাইন ১৭ ডিজিটের ডিজিটাল জন্ম নিবন্ধন সনদের মূল কপি ও সত্যায়িত ফটোকপি।</li>
<li>পিতা ও মাতার জাতীয় পরিচয়পত্রের (NID) সত্যায়িত ফটোকপি।</li>
<li>পূর্বে অধ্যয়নরত বিদ্যালয় থেকে ছাড়পত্র (Transfer Certificate / TC) ও সর্বশেষ বার্ষিক পরীক্ষার মার্কশিট।</li>
<li>কোটার ক্ষেত্রে সংশ্লিষ্ট উপযুক্ত কর্তৃপক্ষের প্রত্যয়নপত্র বা গেজেটের কপি।</li>
<li>সদ্য তোলা পাসপোর্ট সাইজের রঙিন ছবি (৪-৬ কপি)।</li>
</ol>
</div>

<h2 id="section-8" style="font-family: 'SolaimanLipi', sans-serif; font-size: 24px; color: #0f172a; border-bottom: 2px solid #0f766e; padding-bottom: 8px; margin-top: 40px;">৮. সচরাচর জিজ্ঞাসিত প্রশ্নাবলী (FAQ)</h2>

<div style="font-family: 'SolaimanLipi', sans-serif; margin-top: 20px;">

<details style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px 18px; margin-bottom: 12px; cursor: pointer;">
<summary style="font-weight: 700; font-size: 17px; color: #0f766e;">প্রশ্ন ১: ২০২৭ শিক্ষাবর্ষে স্কুল ভর্তির আবেদন কবে শুরু হবে?</summary>
<div style="margin-top: 10px; color: #334155; font-size: 15.5px; line-height: 1.75;">
উত্তর: শিক্ষা মন্ত্রণালয় ও মাউশির নিয়মিত ক্যালেন্ডার অনুযায়ী নভেম্বর মাসের প্রথমার্ধেই সেন্ট্রালাইজড পোর্টাল gsa.teletalk.com.bd-এ আবেদন শুরু হবে এবং নভেম্বরের শেষ পর্যন্ত আবেদন গ্রহণ করা হবে।
</div>
</details>

<details style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px 18px; margin-bottom: 12px; cursor: pointer;">
<summary style="font-weight: 700; font-size: 17px; color: #0f766e;">প্রশ্ন ২: কোন কোন শ্রেণিতে লিখিত পরীক্ষা হবে?</summary>
<div style="margin-top: 10px; color: #334155; font-size: 15.5px; line-height: 1.75;">
উত্তর: নতুন নীতিমালা অনুযায়ী শুধুমাত্র প্রথম শ্রেণিতে ডিজিটাল লটারি হবে। দ্বিতীয় শ্রেণি থেকে নবম শ্রেণি পর্যন্ত প্রতিটি শ্রেণিতে শূন্য আসনের বিপরীতে লিখিত ভর্তি পরীক্ষার মাধ্যমে শিক্ষার্থী ভর্তি করা হবে।
</div>
</details>

<details style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px 18px; margin-bottom: 12px; cursor: pointer;">
<summary style="font-weight: 700; font-size: 17px; color: #0f766e;">প্রশ্ন ৩: লিখিত ভর্তি পরীক্ষার সিলেবাস কী হবে?</summary>
<div style="margin-top: 10px; color: #334155; font-size: 15.5px; line-height: 1.75;">
উত্তর: শিক্ষার্থী যে শ্রেণিতে ভর্তি হতে আবেদন করবে, তার পূর্ববর্তী শ্রেণির জাতীয় শিক্ষাক্রম ও পাঠ্যপুস্তক বোর্ডের (NCTB) বাংলা, ইংরেজি ও গণিত পাঠ্যবইয়ের ওপর পরীক্ষা অনুষ্ঠিত হবে।
</div>
</details>

<details style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px 18px; margin-bottom: 12px; cursor: pointer;">
<summary style="font-weight: 700; font-size: 17px; color: #0f766e;">প্রশ্ন ৪: একজন শিক্ষার্থী কয়টি স্কুলে আবেদন করতে পারবে?</summary>
<div style="margin-top: 10px; color: #334155; font-size: 15.5px; line-height: 1.75;">
উত্তর: একটি আবেদনপত্রের বিপরীতে একজন শিক্ষার্থী সর্বোচ্চ ৫টি বিদ্যালয় পছন্দক্রম (Choice List) হিসেবে নির্বাচন করতে পারবে।
</div>
</details>

<details style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px 18px; margin-bottom: 12px; cursor: pointer;">
<summary style="font-weight: 700; font-size: 17px; color: #0f766e;">প্রশ্ন ৫: ১ম শ্রেণিতে ভর্তির জন্য বয়সের মাপকাঠি কী?</summary>
<div style="margin-top: 10px; color: #334155; font-size: 15.5px; line-height: 1.75;">
উত্তর: ১ জানুয়ারি ২০২৭ তারিখে শিক্ষার্থীর বয়স সর্বনিম্ন ৫ বছর এবং সর্বোচ্চ ৭ বছর হতে হবে। জাতীয় শিক্ষানীতি অনুযায়ী ৬+ বছর বয়সের শিশুদের প্রথম শ্রেণিতে ভর্তির আদর্শ মান হিসেবে বিবেচনা করা হয়।
</div>
</details>

</div>

<!-- Universal Faruk Sir Author Box (Rule 01 E-E-A-T Standard) -->
<div class="htbd-author-box" style="display: flex; gap: 20px; align-items: center; background: #f0fdf4; border: 1.5px solid #22c55e; border-radius: 14px; padding: 22px; margin: 40px 0; box-shadow: 0 4px 15px rgba(0,0,0,0.05); font-family: 'SolaimanLipi', sans-serif;">
<img src="https://secure.gravatar.com/avatar/9c55d045d625bc3b9d6a36fa2d2a420b?s=120&d=mm&r=g" alt="ফারুক স্যার" loading="lazy" style="width: 85px; height: 85px; border-radius: 50%; border: 3px solid #16a34a; object-fit: cover; flex-shrink: 0;" />
<div>
<div style="font-weight: 700; font-size: 19px; color: #166534; margin-bottom: 4px;">আর্টিকেল লেখক: ফারুক স্যার (Faruk Sir)</div>
<div style="font-size: 14px; color: #15803d; margin-bottom: 8px; font-weight: 600;">সিনিয়র শিক্ষা গবেষক ও প্রতিষ্ঠাতা, HelpTrickBD</div>
<p style="margin: 0; font-size: 14.5px; color: #374151; line-height: 1.65;">
মাধ্যমিক ও উচ্চশিক্ষা অধিদপ্তর (মাউশি) এবং বিভিন্ন শিক্ষা বোর্ডের সার্কুলার ও ভর্তি নীতিমালা নিয়ে নিয়মিত গবেষণা করছেন ফারুক স্যার। তাঁর দেওয়া দিকনির্দেশনা ও সঠিক তথ্যের সাহায্যে দেশের লাখ লাখ অভিভাবক ও শিক্ষার্থী সফলভাবে ডিজিটাল লটারি ও ভর্তি কার্যক্রম সম্পন্ন করে থাকেন।
</p>
<div style="margin-top: 10px; font-size: 13.5px; color: #166534;">
অফিসিয়াল চ্যানেল: <a href="https://t.me/helptrickbd_official" target="_blank" rel="noopener noreferrer" style="color: #16a34a; font-weight: bold; text-decoration: underline;">Telegram Channel</a> • <a href="https://whatsapp.com/channel/0029Vb956jgCHDyrx1wkUh2a" target="_blank" rel="noopener noreferrer" style="color: #16a34a; font-weight: bold; text-decoration: underline;">WhatsApp Channel</a>
</div>
</div>
</div>

<!-- Schema.org JSON-LD Microdata (BlogPosting) -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "{title}",
  "description": "{meta_desc}",
  "url": "https://www.helptrickbd.com/{slug}/",
  "datePublished": "2026-10-25T12:00:00+06:00",
  "dateModified": "2026-10-25T12:00:00+06:00",
  "author": {{
    "@type": "Person",
    "name": "ফারুক স্যার",
    "jobTitle": "Senior Education Researcher",
    "url": "https://www.helptrickbd.com"
  }},
  "publisher": {{
    "@type": "Organization",
    "name": "HelpTrickBD",
    "url": "https://www.helptrickbd.com",
    "logo": {{
      "@type": "ImageObject",
      "url": "https://www.helptrickbd.com/logo.png"
    }}
  }},
  "image": "{banner_cdn}"
}}
</script>

<!-- Schema.org JSON-LD Microdata (FAQPage) -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "২০২৭ শিক্ষাবর্ষে স্কুল ভর্তির আবেদন কবে শুরু হবে?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "শিক্ষা মন্ত্রণালয় ও মাউশির নিয়মিত ক্যালেন্ডার অনুযায়ী নভেম্বর মাসের প্রথমার্ধেই সেন্ট্রালাইজড পোর্টাল gsa.teletalk.com.bd-এ আবেদন শুরু হবে এবং নভেম্বরের শেষ পর্যন্ত আবেদন গ্রহণ করা হবে।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "কোন কোন শ্রেণিতে লিখিত পরীক্ষা হবে?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "নতুন নীতিমালা অনুযায়ী শুধুমাত্র প্রথম শ্রেণিতে ডিজিটাল লটারি হবে। দ্বিতীয় শ্রেণি থেকে নবম শ্রেণি পর্যন্ত প্রতিটি শ্রেণিতে শূন্য আসনের বিপরীতে লিখিত ভর্তি পরীক্ষার মাধ্যমে শিক্ষার্থী ভর্তি করা হবে।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "লিখিত ভর্তি পরীক্ষার সিলেবাস কী হবে?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "শিক্ষার্থী যে শ্রেণিতে ভর্তি হতে আবেদন করবে, তার পূর্ববর্তী শ্রেণির জাতীয় শিক্ষাক্রম ও পাঠ্যপুস্তক বোর্ডের (NCTB) বাংলা, ইংরেজি ও গণিত পাঠ্যবইয়ের ওপর পরীক্ষা অনুষ্ঠিত হবে।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "একজন শিক্ষার্থী কয়টি স্কুলে আবেদন করতে পারবে?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "একটি আবেদনপত্রের বিপরীতে একজন শিক্ষার্থী সর্বোচ্চ ৫টি বিদ্যালয় পছন্দক্রম (Choice List) হিসেবে নির্বাচন করতে পারবে।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "১ম শ্রেণিতে ভর্তির জন্য বয়সের মাপকাঠি কী?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "১ জানুয়ারি ২০২৭ তারিখে শিক্ষার্থীর বয়স সর্বনিম্ন ৫ বছর এবং সর্বোচ্চ ৭ বছর হতে হবে। জাতীয় শিক্ষানীতি অনুযায়ী ৬+ বছর বয়সের শিশুদের প্রথম শ্রেণিতে ভর্তির আদর্শ মান হিসেবে বিবেচনা করা হয়।"
      }}
    }}
  ]
}}
</script>
"""

# Save output files
html_file_path = os.path.join(OUTPUT_DIR, f"{slug}.html")
meta_file_path = os.path.join(OUTPUT_DIR, f"{slug}_meta.json")

with open(html_file_path, "w", encoding="utf-8") as f:
    f.write(html_content)

meta_data = {
    "title": title,
    "slug": slug,
    "focus_keyword": full_focus_kw,
    "meta_description": meta_desc,
    "categories": [
        "Education Guide"
    ],
    "tags": [
        "স্কুল ভর্তি ২০২৭",
        "স্কুল ভর্তি লটারি ২০২৭",
        "School Admission 2027",
        "gsa teletalk com bd",
        "লিখিত ভর্তি পরীক্ষা মানবণ্টন",
        "মাউশি স্কুল ভর্তি নীতিমালা"
    ],
    "banner_path": banner_local,
    "featured_media_id": 15938
}

with open(meta_file_path, "w", encoding="utf-8") as f:
    json.dump(meta_data, f, ensure_ascii=False, indent=2)

print(f"[SUCCESS] Generated HTML post: {html_file_path} ({len(html_content)} chars)")
print(f"[SUCCESS] Generated Metadata: {meta_file_path}")
