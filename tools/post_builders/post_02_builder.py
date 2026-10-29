#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Post 2 Builder: নিরীক্ষা প্রতিবেদনের প্রকারভেদ
Optimized for Rank Math 90+ Score:
- Title starts with exact focus keyword + Best Complete Guide + 2026
- Focus Keyword in first 10%
- Focus Keyword in multiple H2 Subheadings
- Focus Keyword Density: ~1.1% (15-16 occurrences)
- Zero-Emoji, 100% Academic Depth, FARUK SIR Author Card
"""

import os
import json

def get_post_data(banner_path):
    focus_kw = "নিরীক্ষা প্রতিবেদনের প্রকারভেদ"
    title = f"{focus_kw}: Best Complete Guide 2026 (ISA 700 ও 705 নমুনা ছক)"
    slug = "audit-report-types-components-format"
    rank_math_focus_kw = f"{focus_kw}, Audit Report Types"
    meta_desc = f"{focus_kw}, মূল উপাদান ও আন্তর্জাতিক নিরীক্ষা মান ISA 700 ও 705 অনুযায়ী শর্তহীন অডিট রিপোর্টের পূর্ণাঙ্গ নমুনা ছক ও হ্যান্ডনোট 2026।"
    
    html = f"""<!-- Byte-0 Hero Banner Placement -->
<figure class="htbd-featured-hero" style="margin: 0 0 25px 0; text-align: center;">
  <img src="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/thumbnails/audit_post_2_banner.webp" alt="{focus_kw}" title="{title}" style="width: 100%; max-width: 1000px; height: auto; border-radius: 12px; box-shadow: 0 5px 20px rgba(0,0,0,0.12); display: block; margin: 0 auto;" loading="eager" />
  <figcaption style="font-family: 'SolaimanLipi', sans-serif; font-size: 14px; color: #64748b; margin-top: 8px; text-align: center;">
    আন্তর্জাতিক নিরীক্ষা মান ISA 700/705 অনুযায়ী নিরীক্ষা প্রতিবেদনের প্রকারভেদ ও পূর্ণাঙ্গ রূপরেখা | সূত্র: HelpTrickBD
  </figcaption>
</figure>

<!-- Modern Typography & Layout Styling -->
<link href="https://cdn.jsdelivr.net/gh/maateen/ekushey-cdn@1.0/fonts/solaiman-lipi/stylesheet.css" rel="stylesheet" type="text/css" />
<style>
  .htbd-nu-content {{
    font-family: 'SolaimanLipi', Arial, sans-serif;
    color: #1e293b;
    line-height: 1.85;
    font-size: 16.5px;
  }}
  .htbd-nu-content h2 {{
    font-family: 'SolaimanLipi', sans-serif;
    color: #0b2046;
    font-size: 24px;
    font-weight: 700;
    margin: 40px 0 20px 0;
    border-bottom: 2.5px solid #0b2046;
    padding-bottom: 10px;
  }}
  .htbd-nu-content h3 {{
    font-family: 'SolaimanLipi', sans-serif;
    color: #1e3a8a;
    font-size: 20px;
    font-weight: 700;
    margin: 30px 0 15px 0;
  }}
  .htbd-nu-content p {{
    margin-bottom: 18px;
    text-align: justify;
  }}
  .htbd-table {{
    width: 100%;
    border-collapse: collapse;
    margin: 25px 0;
    font-size: 15.5px;
  }}
  .htbd-table th, .htbd-table td {{
    border: 1px solid #cbd5e1;
    padding: 12px 14px;
    text-align: left;
  }}
  .htbd-table th {{
    background-color: #0b2046;
    color: #ffffff;
    font-weight: 700;
  }}
  .htbd-table tr:nth-child(even) {{
    background-color: #f8fafc;
  }}
  .htbd-callout {{
    border-radius: 8px;
    padding: 18px 22px;
    margin: 25px 0;
  }}
  .htbd-callout-info {{
    background-color: #eff6ff;
    border-left: 5px solid #2563eb;
    color: #1e40af;
  }}
  .htbd-callout-warning {{
    background-color: #fffbeb;
    border-left: 5px solid #f59e0b;
    color: #92400e;
  }}
  .htbd-specimen-box {{
    background: #fdfefe;
    border: 1.5px dashed #0b2046;
    border-radius: 8px;
    padding: 20px;
    margin: 25px 0;
  }}
  .dark .htbd-nu-content, [data-theme="dark"] .htbd-nu-content {{
    color: #cbd5e1;
  }}
</style>

<div class="htbd-nu-content">
  <!-- Position 0 Quick Answer Box -->
  <div class="htbd-callout htbd-callout-info">
    <p style="margin: 0; font-weight: 600; font-size: 17.5px;">
      <strong>দ্রুত সারসংক্ষেপ:</strong> <strong>{focus_kw}</strong> এবং এর প্রায়োগিক কাঠামো জানা হিসাববিজ্ঞান ও নিরীক্ষা শিক্ষার্থীদের জন্য অত্যন্ত গুরুত্বপূর্ণ। আন্তর্জাতিক নিরীক্ষা মান ISA 700 ও 705 অনুসারে নিরীক্ষা প্রতিবেদন মূলত ৪ প্রকার: (১) শর্তহীন বা আনকোয়ালিফাইড অডিট রিপোর্ট, (২) শর্তযুক্ত বা কোয়ালিফাইড রিপোর্ট, (৩) প্রতিকূল বা অ্যাডভার্স রিপোর্ট, এবং (৪) মতদানে অসম্মতি বা ডিসক্লেইমার। প্রতিটি <strong>{focus_kw}</strong> নির্ভর করে নিরীক্ষকের সংগৃহীত প্রমাণের পর্যাপ্ততা এবং আর্থিক বিবরণীতে ভুলত্রুটির প্রভাবের ওপর।
    </p>
  </div>

  <!--more-->

  <div id="rank-math-toc" class="htbd-callout htbd-callout-warning wp-block-rank-math-toc" style="margin: 20px 0;">
    <h3 style="margin-top:0;">সূচিপত্র (Table of Contents)</h3>
    <ul>
      <li><a href="#section-1">১. নিরীক্ষা প্রতিবেদন কি এবং নিরীক্ষা প্রতিবেদনের প্রকারভেদ এর সাধারণ ধারণা</a></li>
      <li><a href="#section-2">২. আন্তর্জাতিক নিরীক্ষা মান অনুযায়ী নিরীক্ষা প্রতিবেদনের প্রকারভেদ (ISA 700 ও 705)</a></li>
      <li><a href="#section-3">৩. নিরীক্ষা প্রতিবেদনের প্রকারভেদ অনুযায়ী বিভিন্ন মতামতের তুলনামূলক ছক</a></li>
      <li><a href="#section-4">৪. নিরীক্ষা প্রতিবেদনের প্রকারভেদ নির্বিশেষে একটি আদর্শ প্রতিবেদনের ৮টি উপাদান</a></li>
      <li><a href="#section-5">৫. একটি শর্তহীন নিরীক্ষা প্রতিবেদনের বাস্তব নমুনা ছক (Specimen Format)</a></li>
      <li><a href="#section-6">৬. নিরীক্ষা প্রতিবেদন ও নিরীক্ষকের প্রত্যয়নপত্রের পার্থক্য</a></li>
      <li><a href="#section-7">৭. নিরীক্ষা প্রতিবেদনের প্রকারভেদ সম্পর্কিত সাধারণ প্রশ্নাবলি (FAQ)</a></li>
    </ul>
  </div>

  <p>
    যেকোনো যৌথ মূলধনী কোম্পানি বা করপোরেট প্রতিষ্ঠানের হিসাব পরীক্ষার চূড়ান্ত পরিণতি হলো নিরীক্ষা প্রতিবেদন (Audit Report)। একজন পেশাদার চার্টার্ড অ্যাকাউন্ট্যান্ট দীর্ঘ নিরীক্ষা কার্যশেষে যে আনুষ্ঠানিক দলিলে তাঁর নিরপেক্ষ অভিমত ব্যক্ত করেন, তার ওপর ভিত্তি করেই বিভিন্ন <strong>{focus_kw}</strong> নির্ধারিত হয়। বিনিয়োগকারী, ব্যাংক, কর কর্তৃপক্ষ এবং শেয়ারহোল্ডাররা কোনো কোম্পানির আর্থিক স্বাস্থ্যের অবস্থা জানতে এই অডিট রিপোর্টের ওপর শতভাগ নির্ভর করেন। আরও বিশদ অ্যাকাউন্টিং সহায়তার জন্য আমাদের <a href="https://www.helptrickbd.com/category/education-guide/national-university/">জাতীয় বিশ্ববিদ্যালয় লেকচার সিরিজ</a> দেখতে পারেন।
  </p>

  <h2 id="section-1">১. নিরীক্ষা প্রতিবেদন কি এবং নিরীক্ষা প্রতিবেদনের প্রকারভেদ এর সাধারণ ধারণা</h2>
  <p>
    সাধারণভাবে, কোনো প্রতিষ্ঠানের যাবতীয় হিসাবের বহি, আর্থিক বিবরণী এবং অভ্যন্তরীণ নিয়ন্ত্রণ ব্যবস্থা পুঙ্খানুপুঙ্খ পরীক্ষা করার পর নিরীক্ষক তাঁর মতামত ব্যক্ত করে সংশ্লিষ্ট কর্তৃপক্ষের নিকট যে আনুষ্ঠানিক লিখিত বিবরণী দাখিল করেন, তাকে নিরীক্ষা প্রতিবেদন বলা হয়। বাস্তব ক্ষেত্রে প্রতিষ্ঠানের স্বচ্ছতা ও হিসাবের নির্ভুলতার ওপর ভিত্তি করে <strong>{focus_kw}</strong> পরিলক্ষিত হয়।
  </p>
  <p>
    ১৯৯৪ সালের কোম্পানি আইনের ২১৩(৩) ধারা অনুযায়ী, প্রত্যেক কোম্পানি নিরীক্ষক কোম্পানির শেয়ারহোল্ডারদের উদ্দেশ্যে প্রস্তুতকৃত বার্ষিক আর্থিক হিসাব (উদ্বৃত্তপত্র ও লাভ-লোকসান হিসাব)-এর ওপর একটি বিধিবদ্ধ প্রতিবেদন দাখিল করতে আইনত বাধ্য। আন্তর্জাতিক নিরীক্ষা মানদণ্ড (<a href="https://www.icab.org.bd/" target="_blank" rel="noopener noreferrer">ICAB অনুমোদিত ISA 700</a>) অনুযায়ী, নিরীক্ষক তাঁর স্বাধীন বিচার-বিশ্লেষণের মাধ্যমে নিশ্চিত করেন যে আর্থিক বিবরণীটি সংশ্লিষ্ট হিসাব মানদণ্ড (IFRS/BFRS) অনুসরণ করে প্রস্তুত হয়েছে কি না।
  </p>

  <h2 id="section-2">২. আন্তর্জাতিক নিরীক্ষা মান অনুযায়ী নিরীক্ষা প্রতিবেদনের প্রকারভেদ (ISA 700 ও 705)</h2>
  <p>
    আন্তর্জাতিক নিরীক্ষা মানদণ্ড (ISA 700 ও ISA 705) অনুসারে <strong>{focus_kw}</strong> মূলত নিরীক্ষকের মতামতের বৈশিষ্ট্যের ওপর ভিত্তি করে দুটি প্রধান ভাগে এবং পরবর্তীতে চারটি সুনির্দিষ্ট উপভাগে বিভক্ত:
  </p>

  <h3>ক. অপরিবর্তিত বা শর্তহীন প্রতিবেদন (Unmodified / Unqualified Report - ISA 700)</h3>
  <p>
    যখন নিরীক্ষক পর্যাপ্ত উপযুক্ত সাক্ষ্যপ্রমাণ পেয়ে নিশ্চিত হন যে কোম্পানির আর্থিক বিবরণী কোনো বস্তুগত ভুলত্রুটি বা জালিয়াতি ছাড়াই পুরোপুরি সত্য ও ন্যায্য অবস্থা (True and Fair View) প্রতিফলিত করছে, তখন তিনি যে প্রতিবেদন দেন তাকে শর্তহীন বা ক্লিন অডিট রিপোর্ট বলে। <strong>{focus_kw}</strong>-এর মধ্যে এটি একটি কোম্পানির সুনাম ও নির্ভরযোগ্যতার সর্বোচ্চ মাপকাঠি।
  </p>

  <h3>খ. পরিবর্তিত বা সংশোধিত প্রতিবেদন (Modified Audit Reports - ISA 705)</h3>
  <p>
    যখন নিরীক্ষক হিসাবের কোনো অংশে বিচ্যুতি পান বা পর্যাপ্ত প্রমাণ সংগ্রহে ব্যর্থ হন, তখন ISA 705 অনুযায়ী নিচের ৩টি পরিবর্তিত মতামতের যেকোনো একটি প্রদান করেন:
  </p>

  <h2 id="section-3">৩. নিরীক্ষা প্রতিবেদনের প্রকারভেদ অনুযায়ী বিভিন্ন মতামতের তুলনামূলক ছক</h2>
  <p>
    শিক্ষার্থীদের পরীক্ষার খাতায় সহজে উপস্থাপনের জন্য <strong>{focus_kw}</strong>-এর অন্তর্ভুক্ত প্রতিটি মতামতের প্রয়োগ ও প্রভাবের মাত্রা নিচে তুলে ধরা হলো:
  </p>

  <table class="htbd-table">
    <thead>
      <tr>
        <th>প্রতিবেদনের ধরন</th>
        <th>প্রয়োগের পরিস্থিতি</th>
        <th>প্রভাবের মাত্রা</th>
        <th>ফলাফল</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>১. শর্তসাপেক্ষ মতামত (Qualified Opinion)</strong></td>
        <td>হিসাবে নির্দিষ্ট কোনো ভুল আছে কিন্তু তা সামগ্রিক আর্থিক বিবরণীকে নষ্ট করে না।</td>
        <td>বস্তুগত কিন্তু সর্বব্যাপী নয় (Material but NOT Pervasive)</td>
        <td>অমুক বিষয় ব্যতীত বাকি হিসাব সঠিক</td>
      </tr>
      <tr>
        <td><strong>২. বিরূপ বা প্রতিকূল মতামত (Adverse Opinion)</strong></td>
        <td>আর্থিক বিবরণীতে এত বড় জালিয়াতি বা ভুল রয়েছে যা পুরো হিসাবকে বিভ্রান্তিকর করে তোলে।</td>
        <td>বস্তুগত এবং সর্বব্যাপী (Material AND Pervasive)</td>
        <td>আর্থিক হিসাব সত্য ও ন্যায্য নয়</td>
      </tr>
      <tr>
        <td><strong>৩. মতদানে অসম্মতি (Disclaimer of Opinion)</strong></td>
        <td>ব্যবস্থাপনা প্রয়োজনীয় প্রমাণপত্র সরবরাহ না করায় নিরীক্ষক কোনো মতামত দিতে অক্ষম হন।</td>
        <td>প্রমাণের অভাব সর্বব্যাপী (Pervasive limitation)</td>
        <td>নিরীক্ষক মতামত দিতে অপারগ</td>
      </tr>
    </tbody>
  </table>

  <h2 id="section-4">৪. নিরীক্ষা প্রতিবেদনের প্রকারভেদ নির্বিশেষে একটি আদর্শ প্রতিবেদনের ৮টি উপাদান</h2>
  <p>
    যেকোনো <strong>{focus_kw}</strong> পর্যালোচনা করলে দেখা যায়, একটি স্ট্যান্ডার্ড অডিট রিপোর্টে আন্তর্জাতিক মান অনুযায়ী ধারাবাহিকভাবে নিচের ৮টি সেকশন বা উপাদান উপস্থিত থাকতে হয়:
  </p>
  <ol style="padding-left: 20px;">
    <li><strong>সুস্পষ্ট শিরোনাম (Title):</strong> প্রতিবেদনের শীর্ষে স্পষ্ট করে লেখা থাকতে হবে: Independent Auditor's Report (স্বতন্ত্র নিরীক্ষকের প্রতিবেদন), যাতে এর নিরপেক্ষতা প্রকাশ পায়।</li>
    <li><strong>প্রাপক (Addressee):</strong> সাধারণত কোম্পানির শেয়ারহোল্ডার বা পরিচালনা পর্ষদকে সম্বোধন করা হয়।</li>
    <li><strong>নিরীক্ষকের মতামত (Auditor's Opinion):</strong> প্রতিবেদনের শুরুতেই নিরীক্ষক কোম্পানির নাম, হিসাবকাল এবং তাঁর পরিষ্কার মতামত ব্যক্ত করেন।</li>
    <li><strong>মতামতের ভিত্তি (Basis for Opinion):</strong> তিনি কোন আন্তর্জাতিক মান (ISA) মেনে অডিট পরিচালনা করেছেন এবং তাঁর স্বাধীনতা নিশ্চিত করেছেন তা উল্লেখ থাকে।</li>
    <li><strong>মূল নিরীক্ষা বিষয় (Key Audit Matters - KAM - ISA 701):</strong> তালিকাভুক্ত কোম্পানির ক্ষেত্রে অডিটে সবচেয়ে ঝুঁকিপূর্ণ বা জটিল যে বিষয়গুলো নিরীক্ষকের নজরে এসেছে তা এখানে আলোচনা করা হয়।</li>
    <li><strong>ব্যবস্থাপনার দায়িত্ব (Management's Responsibilities):</strong> আর্থিক হিসাব নির্ভুল প্রস্তুত এবং অভ্যন্তরীণ নিয়ন্ত্রণ বজায় রাখার দায়িত্ব ব্যবস্থাপনার—তা পরিষ্কারভাবে উল্লেখ করা হয়।</li>
    <li><strong>নিরীক্ষকের দায়িত্ব (Auditor's Responsibilities):</strong> আর্থিক বিবরণী বস্তুগত ভুলত্রুটি মুক্ত কি না সে বিষয়ে যুক্তিসঙ্গত নিশ্চয়তা (Reasonable Assurance) অর্জনের প্রক্রিয়া ব্যাখ্যা করা হয়।</li>
    <li><strong>স্বাক্ষর, তারিখ ও স্থান (Signature & Date):</strong> অডিট ফার্মের নাম, চার্টার্ড অ্যাকাউন্ট্যান্ট পার্টনারের স্বাক্ষর, তারিখ এবং ফার্মের লাইসেন্স নম্বর ও ঠিকানা।</li>
  </ol>

  <h2 id="section-5">৫. একটি শর্তহীন নিরীক্ষা প্রতিবেদনের বাস্তব নমুনা ছক (Specimen Format)</h2>
  <p>
    জাতীয় বিশ্ববিদ্যালয়ের লিখিত পরীক্ষায় <strong>{focus_kw}</strong> সংক্রান্ত প্রশ্নে সরাসরি অডিট রিপোর্টের খসড়া বা ড্রাফট প্রস্তুত করতে বলা হয়। নিচে একটি প্রমিত নমুনা তুলে ধরা হলো:
  </p>

  <div class="htbd-specimen-box">
    <h3 style="text-align: center; margin-top: 0; color: #0b2046;">স্বতন্ত্র নিরীক্ষকের প্রতিবেদন (নমুনা ছক)</h3>
    <p style="text-align: center; font-weight: bold; margin-bottom: 20px;">
      প্রতি: মেঘনা টেক্সটাইল মিলস লিমিটেড-এর শেয়ারহোল্ডারবৃন্দ
    </p>

    <p><strong>মতামত (Opinion):</strong><br />
    আমরা মেঘনা টেক্সটাইল মিলস লিমিটেড-এর ৩১ ডিসেম্বর ২০২৫ তারিখে সমাপ্ত বছরের আর্থিক বিবরণী (আর্থিক অবস্থার বিবরণী, লাভ-লোকসান হিসাব এবং নগদ প্রবাহ বিবরণী) নিরীক্ষা সম্পন্ন করেছি। আমাদের মতে, সংশ্লিষ্ট আর্থিক বিবরণীসমূহ বাংলাদেশ ফিন্যান্সিয়াল রিপোর্টিং স্ট্যান্ডার্ডস (BFRS) অনুযায়ী প্রতিষ্ঠানের আর্থিক অবস্থা ও ফলাফলের সত্য ও ন্যায্য চিত্র (True and Fair View) উপস্থাপন করছে।</p>

    <p><strong>মতামতের ভিত্তি (Basis for Opinion):</strong><br />
    আমরা ইন্টারন্যাশনাল স্ট্যান্ডার্ডস অন অডিটিং (ISA) অনুসরণ করে আমাদের নিরীক্ষা কার্য পরিচালনা করেছি। আমরা বিশ্বাস করি যে আমাদের সংগৃহীত নিরীক্ষা সাক্ষ্যপ্রমাণ আমাদের মতামত প্রকাশের জন্য পর্যাপ্ত ও উপযুক্ত।</p>

    <div style="margin-top: 30px; display: flex; justify-content: space-between;">
      <div>
        <strong>তারিখ:</strong> ২৫ ফেব্রুয়ারি 2026<br />
        <strong>স্থান:</strong> মতিঝিল, ঢাকা।
      </div>
      <div style="text-align: right;">
        <strong>রহমান ফারুক অ্যান্ড কোং</strong><br />
        চার্টার্ড অ্যাকাউন্ট্যান্টস<br />
        স্বাক্ষর: ..........................
      </div>
    </div>
  </div>

  <h2 id="section-6">৬. নিরীক্ষা প্রতিবেদন ও নিরীক্ষকের প্রত্যয়নপত্রের পার্থক্য</h2>
  <p>
    অ্যাকাউন্টিং শিক্ষার্থীদের জন্য <strong>{focus_kw}</strong> অধ্যয়নের সময় নিরীক্ষা প্রতিবেদন ও প্রত্যয়নপত্রের মধ্যকার ধারণাগত পার্থক্য স্পষ্ট থাকা জরুরি:
  </p>
  <table class="htbd-table">
    <thead>
      <tr>
        <th>তুলনার ভিত্তি</th>
        <th>নিরীক্ষা প্রতিবেদন (Audit Report)</th>
        <th>নিরীক্ষকের প্রত্যয়নপত্র (Audit Certificate)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>প্রকৃতি</strong></td>
        <td>এটি নিরীক্ষকের পেশাগত ও ব্যক্তিগত অভিমত বা মতামত (Opinion)।</td>
        <td>এটি কোনো তথ্যের ১০০% নির্ভুলতার গ্যারান্টি বা নিশ্চয়তা (Factual Guarantee)।</td>
      </tr>
      <tr>
        <td><strong>দায়দায়িত্ব</strong></td>
        <td>যুক্তিসঙ্গত নিশ্চয়তা প্রদান করে; নিরীক্ষক গ্যারান্টার নন।</td>
        <td>নিরীক্ষক তথ্যের শতভাগ সঠিকতার জন্য ব্যক্তিগতভাবে সম্পূর্ণ দায়ী থাকেন।</td>
      </tr>
      <tr>
        <td><strong>ব্যবহার</strong></td>
        <td>বার্ষিক সাধারণ সভায় শেয়ারহোল্ডারদের উদ্দেশ্যে পেশ করা হয়।</td>
        <td>নির্দিষ্ট বিশেষ উদ্দেশ্যে (যেমন: ঋণ গ্রহণ, কর নিরূপণ) দেওয়া হয়।</td>
      </tr>
    </tbody>
  </table>

  <h2 id="section-7">৭. নিরীক্ষা প্রতিবেদনের প্রকারভেদ সম্পর্কিত সাধারণ প্রশ্নাবলি (FAQ)</h2>
  <div style="margin-top: 15px;">
    <h3>প্রশ্ন ১: নিরীক্ষা প্রতিবেদনের প্রকারভেদ অনুযায়ী প্রতিকূল (Adverse) রিপোর্ট পেলে কি কোম্পানি শেয়ারবাজারে লেনদেন চালিয়ে যেতে পারে?</h3>
    <p>উত্তর: সাধারণত না। বাংলাদেশ সিকিউরিটিজ অ্যান্ড এক্সচেঞ্জ কমিশন (BSEC) এর বিধি অনুযায়ী কোনো কোম্পানি প্রতিকূল বা মতদানে অসম্মতি রিপোর্ট পেলে তাদের শেয়ার লেনদেন স্থগিত বা বিশেষ তদন্তের মুখোমুখি হতে হয়। আরও তথ্য পেতে আমাদের <a href="https://www.helptrickbd.com/">HelpTrickBD এডুকেশন হাব</a> ফলো করুন।</p>

    <h3>প্রশ্ন ২: নিরীক্ষা প্রতিবেদনের প্রকারভেদ নির্ধারণে KAM (Key Audit Matters) এর ভূমিকা কী?</h3>
    <p>উত্তর: ISA 701 অনুযায়ী, নিরীক্ষকের পেশাগত মূল্যায়নে নিরীক্ষা চলাকালীন সবচেয়ে বেশি ঝুঁকিপূর্ণ বা ব্যবস্থাপনার জটিল অনুমানের সাথে জড়িত বিষয়গুলোকে কে-এ-এম বলা হয়, যা প্রতিবেদনের নির্ভরযোগ্যতা ব্যাখ্যা করে।</p>
  </div>

  <!-- Mandatory Author Box -->
  <div class="htbd-author-card htbd-author-box" style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 22px; margin: 40px 0; display: flex; align-items: center; gap: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); font-family: 'SolaimanLipi', sans-serif;">
    <img src="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/author/faruk_sir.webp" alt="ফারুক স্যার" loading="lazy" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; border: 3px solid #0f766e;" />
    <div>
      <h4 style="margin: 0 0 6px 0; color: #0f766e; font-size: 19px;">লেখক পরিচিতি: ফারুক স্যার (মো. ওমর ফারুক)</h4>
      <p style="margin: 0; color: #475569; font-size: 14.5px; line-height: 1.6;">
        প্রতিষ্ঠাতা ও প্রধান সম্পাদক, HelpTrickBD। বিগত এক দশকেরও বেশি সময় ধরে জাতীয় বিশ্ববিদ্যালয়, ডিগ্রি ও অনার্স পর্যায়ের শিক্ষার্থীদের পরীক্ষা প্রস্তুতি ও শিক্ষা নির্দেশনায় নিবেদিতপ্রাণ শিক্ষক ও কনটেন্ট স্ট্র্যাটেজিস্ট।
      </p>
    </div>
  </div>
</div>

<!-- Structured Data Microdata (JSON-LD) -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "{title}",
  "description": "{meta_desc}",
  "image": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/thumbnails/audit_post_2_banner.webp",
  "author": {{
    "@type": "Person",
    "name": "ফারুক স্যার (Faruk Sir)"
  }},
  "publisher": {{
    "@type": "Organization",
    "name": "HelpTrickBD",
    "logo": {{
      "@type": "ImageObject",
      "url": "https://www.helptrickbd.com/wp-content/uploads/2026/09/cropped-helptrickbd_logo.png"
    }}
  }},
  "datePublished": "2026-10-29T03:32:00+06:00",
  "dateModified": "2026-10-29T03:32:00+06:00",
  "mainEntityOfPage": {{
    "@type": "WebPage",
    "@id": "https://www.helptrickbd.com/{slug}/"
  }}
}}
</script>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "একটি কোম্পানি কি প্রতিকূল (Adverse) অডিট রিপোর্ট নিয়ে শেয়ারবাজারে তালিকাভুক্ত থাকতে পারে?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "সাধারণত না। বাংলাদেশ সিকিউরিটিজ অ্যান্ড এক্সচেঞ্জ কমিশন (BSEC) এর বিধি অনুযায়ী কোনো কোম্পানি প্রতিকূল বা মতদানে অসম্মতি রিপোর্ট পেলে তাদের শেয়ার লেনদেন স্থগিত বা তদন্তের মুখোমুখি হতে হয়।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "অডিট রিপোর্টে KAM বলতে কী বোঝায়?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "ISA 701 অনুযায়ী, নিরীক্ষকের পেশাগত মূল্যায়নে নিরীক্ষা চলাকালীন সবচেয়ে বেশি ঝুঁকিপূর্ণ বা ব্যবস্থাপনার জটিল অনুমানের সাথে জড়িত বিষয়গুলোকে কে-এ-এম (Key Audit Matters) বলা হয়।"
      }}
    }}
  ]
}}
</script>
"""

    meta = {
        "title": title,
        "slug": slug,
        "focus_keyword": focus_kw,
        "rank_math_focus_keyword": rank_math_focus_kw,
        "meta_description": meta_desc,
        "categories": ["Education Guide", "National University"],
        "tags": ["নিরীক্ষা প্রতিবেদন", "Audit Report", "ISA 700", "অনার্স ৩য় বর্ষ হিসাববিজ্ঞান", "অডিট রিপোর্ট নমুনা"],
        "banner_path": banner_path,
        "status": "draft"
    }

    return html, meta
