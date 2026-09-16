#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/pdf_to_post/generate_ssc_2027_silo_posts.py
--------------------------------------------------
Generates all 5 SSC 2027 English 1st Paper Silo Series posts.
Each post is a supporting cluster post for the Pillar Hub:
https://www.helptrickbd.com/2026/09/ssc-english-1st-paper-suggestion-2027.html

Silo Posts:
  Part 01: Seen Passage MCQ, Q/A & Gap Fill (Q 1-3)
  Part 02: Unseen Passage & Summary Writing (Q 4-5)
  Part 03: Matching Table & Re-arranging (Q 6-7)
  Part 04: Poems & Stories Q/A Guide (Q 8-9)
  Part 05: Completing Story & Dialogue Writing (Q 10-11)
"""

import os
import sys
import json

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RAW_POSTS_DIR = os.path.join(PROJECT_ROOT, "scratch", "raw_posts")
os.makedirs(RAW_POSTS_DIR, exist_ok=True)

BLOG_BASE = "https://www.helptrickbd.com/2026/09"
CDN_BASE = "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts"
PILLAR_URL = f"{BLOG_BASE}/ssc-english-1st-paper-suggestion-2027.html"

LABELS = ["SSC Suggestion", "Education", "Dakhil Suggestion"]

# ─────────────────────────────────────────────────────────────────────────────
# SHARED CSS BLOCK (Golden Reference Architecture)
# ─────────────────────────────────────────────────────────────────────────────
def get_css_block():
    return """<style>
  .htbd-academic-container,
  .htbd-academic-container * {
    font-family: 'SolaimanLipi', 'Noto Sans Bengali', Arial, sans-serif !important;
  }
  .htbd-academic-container p {
    font-size: 18px !important;
    line-height: 1.85 !important;
    color: #202124 !important;
    margin: 16px 0 !important;
  }
  .htbd-academic-heading {
    color: #0c2340 !important;
    border-left: 5px solid #d4af37 !important;
    border-bottom: none !important;
    padding-left: 14px !important;
    margin-top: 38px !important;
    margin-bottom: 16px !important;
    font-size: 24px !important;
    font-weight: 700 !important;
    line-height: 1.4 !important;
  }
  .htbd-academic-subheading {
    color: #1e3a8a !important;
    font-size: 20px !important;
    font-weight: 600 !important;
    margin-top: 26px !important;
    margin-bottom: 12px !important;
    line-height: 1.4 !important;
  }
  .htbd-overview-box {
    background: #f8fafd !important;
    border: 1px solid #dbeafe !important;
    border-left: 5px solid #0c2340 !important;
    border-radius: 8px !important;
    padding: 22px 26px !important;
    margin: 24px 0 !important;
    box-shadow: 0 2px 6px rgba(12,35,64,0.06) !important;
  }
  .htbd-overview-box p {
    margin: 0 !important;
    font-size: 18px !important;
    line-height: 1.85 !important;
    color: #1e293b !important;
  }
  .htbd-toc-card {
    background: #f8fafc !important;
    border: 1px solid #e2e8f0 !important;
    border-left: 4px solid #0c2340 !important;
    border-radius: 8px !important;
    padding: 20px 24px !important;
    margin: 28px 0 !important;
    box-shadow: 0 2px 6px rgba(0,0,0,0.03) !important;
  }
  .htbd-toc-card .toc-title {
    font-weight: 700;
    font-size: 19px;
    margin: 0 0 14px 0;
    color: #0c2340;
  }
  .htbd-toc-card ul {
    margin: 0 !important;
    padding-left: 20px !important;
    list-style-type: none !important;
  }
  .htbd-toc-card ul li {
    margin-bottom: 8px !important;
    font-size: 17px !important;
    padding-left: 6px !important;
  }
  .htbd-toc-card ul li a {
    color: #0b2046 !important;
    text-decoration: underline !important;
    font-weight: 500 !important;
  }
  .htbd-academic-table {
    width: 100% !important;
    border-collapse: collapse !important;
    font-size: 16.5px !important;
    background: #fff !important;
    border-radius: 8px !important;
    overflow: hidden !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06) !important;
  }
  .htbd-academic-table thead tr {
    background: #0c2340 !important;
    color: #fff !important;
  }
  .htbd-academic-table th {
    padding: 13px 16px !important;
    text-align: left !important;
    font-weight: 600 !important;
    font-size: 16px !important;
    line-height: 1.4 !important;
  }
  .htbd-academic-table td {
    padding: 12px 16px !important;
    border-bottom: 1px solid #e2e8f0 !important;
    color: #1e293b !important;
    vertical-align: top !important;
    line-height: 1.65 !important;
  }
  .htbd-academic-table tbody tr:nth-child(even) {
    background: #f8fafc !important;
  }
  .htbd-academic-table tbody tr:hover {
    background: #eef2ff !important;
  }
  .htbd-tip-box {
    background: #f0fdf4 !important;
    border: 1px solid #bbf7d0 !important;
    border-left: 5px solid #16a34a !important;
    border-radius: 8px !important;
    padding: 18px 22px !important;
    margin: 22px 0 !important;
  }
  .htbd-tip-box p {
    margin: 0 !important;
    font-size: 17px !important;
    color: #14532d !important;
    line-height: 1.75 !important;
  }
  .htbd-warning-box {
    background: #fffbeb !important;
    border: 1px solid #fde68a !important;
    border-left: 5px solid #d97706 !important;
    border-radius: 8px !important;
    padding: 18px 22px !important;
    margin: 22px 0 !important;
  }
  .htbd-warning-box p {
    margin: 0 !important;
    font-size: 17px !important;
    color: #78350f !important;
    line-height: 1.75 !important;
  }
  .htbd-faq-item {
    border-bottom: 1px solid #e2e8f0 !important;
    padding: 18px 0 !important;
  }
  .htbd-faq-item:last-child {
    border-bottom: none !important;
  }
  .htbd-series-nav {
    background: #f8fafc !important;
    border: 1px solid #e2e8f0 !important;
    border-left: 4px solid #0284c7 !important;
    border-radius: 8px !important;
    padding: 22px 26px !important;
    margin: 32px 0 !important;
  }
  .htbd-series-nav .nav-title {
    font-size: 18.5px !important;
    font-weight: 700 !important;
    margin: 0 0 6px 0 !important;
    color: #0f172a !important;
  }
  .htbd-series-nav .nav-desc {
    font-size: 15px !important;
    color: #475569 !important;
    margin: 0 0 14px 0 !important;
    line-height: 1.5 !important;
  }
  .htbd-series-nav ul {
    margin: 0 !important;
    padding-left: 20px !important;
    list-style-type: disc !important;
  }
  .htbd-series-nav ul li {
    margin-bottom: 8px !important;
    font-size: 16px !important;
    line-height: 1.6 !important;
    color: #334155 !important;
  }
  .htbd-series-nav ul li a {
    color: #0369a1 !important;
    text-decoration: underline !important;
    font-weight: 600 !important;
    transition: color 0.2s ease !important;
  }
  .htbd-series-nav ul li a:hover {
    color: #0284c7 !important;
  }
  .htbd-series-nav ul li.current-post {
    color: #0f172a !important;
    font-weight: 700 !important;
    background: #f1f5f9 !important;
    padding: 3px 8px !important;
    border-radius: 4px !important;
    display: inline-block !important;
  }
  .htbd-series-nav ul li.current-post .cur-tag {
    color: #0284c7 !important;
    font-weight: 700 !important;
    margin-left: 6px !important;
  }
  .htbd-hero-img {
    width: 100% !important;
    max-width: 100% !important;
    height: auto !important;
    border-radius: 8px !important;
    box-shadow: 0 4px 14px rgba(0,0,0,0.10) !important;
    display: block !important;
    margin: 0 0 20px 0 !important;
  }
</style>"""


# ─────────────────────────────────────────────────────────────────────────────
# SERIES NAVIGATION BOX (shared across all posts)
# ─────────────────────────────────────────────────────────────────────────────
def get_series_nav(current_part):
    posts = [
        ("পিলার হাব", "এসএসসি ২০২৭ ইংরেজি ১ম পত্র — সম্পূর্ণ সাজেশন ও মানবণ্টন (Pillar Post)", f"{BLOG_BASE}/ssc-english-1st-paper-suggestion-2027.html"),
        ("Part 01", "সিন প্যাসেজ সাজেশন (Seen Passage MCQ, Q/A & Gap Fill)", f"{BLOG_BASE}/ssc-2027-english-seen-passage-suggestion.html"),
        ("Part 02", "আনসিন প্যাসেজ ও সামারি (Unseen Passage & Summary Writing)", f"{BLOG_BASE}/ssc-2027-english-unseen-passage-summary.html"),
        ("Part 03", "ম্যাচিং টেবিল ও রি-অ্যারেঞ্জ (Sentence Matching & Re-arranging)", f"{BLOG_BASE}/ssc-2027-english-matching-rearrange.html"),
        ("Part 04", "কবিতা ও গল্প প্রশ্নোত্তর (Poems & Stories Q/A Guide)", f"{BLOG_BASE}/ssc-2027-english-poems-stories-question.html"),
        ("Part 05", "রাইটিং পার্ট — Story & Dialogue (Completing Story & Dialogue Writing)", f"{BLOG_BASE}/ssc-2027-english-completing-story.html"),
    ]
    items_html = ""
    for label, title, url in posts:
        if label == current_part:
            items_html += f'<li class="current-post"><strong>{label}:</strong> {title} <span class="cur-tag">(এই পোস্ট)</span></li>\n'
        else:
            items_html += f'<li><strong>{label}:</strong> <a href="{url}">{title}</a></li>\n'
    return f"""<div class="htbd-series-nav">
    <p class="nav-title">এসএসসি ২০২৭ ইংরেজি ১ম পত্র স্টাডি সিলো সিরিজ (SSC 2027 English Study Silo Series)</p>
    <p class="nav-desc">জাতীয় শিক্ষাক্রমের পূর্ণাঙ্গ সিলেবাস ও প্রশ্নভিত্তিক ধারাবাহিক প্রস্তুতি নির্দেশিকাসমূহ ক্রমানুসারে পড়ুন:</p>
    <ul>
      {items_html}
    </ul>
  </div>"""


# ─────────────────────────────────────────────────────────────────────────────
# POST 01: SEEN PASSAGE (Q 1-3)
# ─────────────────────────────────────────────────────────────────────────────
def generate_post_01():
    slug = "ssc-2027-english-seen-passage-suggestion"
    title = "এসএসসি ২০২৭ ইংরেজি ১ম পত্র সিন প্যাসেজ সাজেশন (SSC 2027 English Seen Passage MCQ, Question Answer & Gap Filling Complete Guide)"
    meta_desc = "SSC 2027 English 1st Paper Seen Passage গাইড। MCQ (Q1), প্রশ্নোত্তর (Q2) ও Gap Filling (Q3) — ২২ নম্বরের পূর্ণাঙ্গ মডেল সমাধান ও প্রস্তুতি।"
    banner_url = f"{CDN_BASE}/ssc_2027_silo_01_seen_passage.webp"
    banner_alt = "SSC 2027 English Seen Passage Suggestion — MCQ, Question Answer and Gap Filling Guide"
    url = f"{BLOG_BASE}/{slug}.html"
    series_nav = get_series_nav("Part 01")

    html = get_css_block() + f"""
<div class="htbd-academic-container">

  <figure style="margin: 0 0 20px 0;">
    <img class="htbd-hero-img" src="{banner_url}" alt="{banner_alt}" title="{banner_alt}" width="1200" height="675" loading="eager" />
    <figcaption style="font-size: 14px; color: #64748b; text-align: center; margin-top: 6px;">SSC 2027 English 1st Paper Seen Passage — Part 01 of the Study Silo Series</figcaption>
  </figure>

  <div class="htbd-overview-box">
    <p>এসএসসি ২০২৭ ইংরেজি ১ম পত্রে <strong>প্রশ্ন ১, ২ ও ৩</strong> — এই তিনটি প্রশ্ন সিন (পাঠ্যবইয়ের) প্যাসেজ থেকে আসে এবং মোট <strong>২২ নম্বর</strong> বরাদ্দ থাকে। MCQ (৭ নম্বর), Open-Ended Q/A (১০ নম্বর) এবং Gap Filling (৫ নম্বর) — এই তিনটিতে দক্ষতা অর্জন করলে পরীক্ষায় নিশ্চিত ভালো ফলাফল করা সম্ভব। (SSC 2027 English 1st Paper Seen Passage covers Questions 1, 2 & 3 for a total of 22 marks.)</p>
  </div>

<!--more-->

  <div class="htbd-toc-card">
    <p class="toc-title">বিষয়সূচি (Table of Contents)</p>
    <ul>
      <li><a href="#seen-marks">১. সিন প্যাসেজ: নম্বর বণ্টন ও প্রশ্নের ধরন</a></li>
      <li><a href="#mcq-guide">২. প্রশ্ন ১: MCQ সমাধানের কৌশল (Q1 MCQ Solving Strategy)</a></li>
      <li><a href="#qa-guide">৩. প্রশ্ন ২: প্রশ্নোত্তর লেখার নিয়ম (Q2 Open-Ended Answer Writing)</a></li>
      <li><a href="#gap-fill-guide">৪. প্রশ্ন ৩: Gap Filling Without Clues — সম্পূর্ণ নির্দেশিকা</a></li>
      <li><a href="#important-passages">৫. গুরুত্বপূর্ণ সিন প্যাসেজ তালিকা (Important EFT Seen Passages)</a></li>
      <li><a href="#model-answer">৬. নমুনা সমাধান (Model Answer)</a></li>
      <li><a href="#faq">৭. সচরাচর জিজ্ঞাসা (FAQ)</a></li>
    </ul>
  </div>

  <h2 class="htbd-academic-heading" id="seen-marks">১. সিন প্যাসেজ: নম্বর বণ্টন ও প্রশ্নের ধরন (Seen Passage Marks Distribution)</h2>
  <p>এসএসসি ২০২৭ পরীক্ষায় Part A (Reading) অংশে দুটি সিন প্যাসেজ থাকে — প্যাসেজ ১ থেকে প্রশ্ন ১ ও ২ এবং প্যাসেজ ২ থেকে প্রশ্ন ৩ আসে। Seen Passage মানে পাঠ্যবই <strong>English For Today (EFT)</strong> থেকে নেওয়া পরিচিত অনুচ্ছেদ, যা পরীক্ষার আগেই শিক্ষার্থী পড়ে যায়।</p>

  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 24px 0;">
    <table class="htbd-academic-table">
      <thead>
        <tr>
          <th>প্রশ্ন নম্বর</th>
          <th>প্রশ্নের ধরন (Question Type)</th>
          <th>উৎস (Source)</th>
          <th>নম্বর (Marks)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>প্রশ্ন ১ (Q1)</strong></td>
          <td>Multiple Choice Questions (MCQ)</td>
          <td>Seen Passage 1 (১ম সিন প্যাসেজ)</td>
          <td><strong>1 × 7 = 7 নম্বর</strong></td>
        </tr>
        <tr>
          <td><strong>প্রশ্ন ২ (Q2)</strong></td>
          <td>Answering Questions (Open-Ended)</td>
          <td>Seen Passage 1 (১ম সিন প্যাসেজ)</td>
          <td><strong>2 × 5 = 10 নম্বর</strong></td>
        </tr>
        <tr>
          <td><strong>প্রশ্ন ৩ (Q3)</strong></td>
          <td>Gap Filling Without Clues</td>
          <td>Seen Passage 2 (২য় সিন প্যাসেজ)</td>
          <td><strong>1 × 5 = 5 নম্বর</strong></td>
        </tr>
        <tr>
          <td colspan="3" style="text-align:right; font-weight:700; background:#f1f5f9;">মোট (Total):</td>
          <td style="font-weight:700; background:#f1f5f9; color:#0c2340;"><strong>22 নম্বর</strong></td>
        </tr>
      </tbody>
    </table>
  </div>

  <h2 class="htbd-academic-heading" id="mcq-guide">২. প্রশ্ন ১: MCQ সমাধানের কৌশল (Q1 MCQ Solving Strategy for Seen Passage)</h2>
  <p>প্রশ্ন ১-এ ১ম সিন প্যাসেজ থেকে ৭টি MCQ আসে। প্রতিটি প্রশ্নের সঠিক উত্তরের জন্য ১ নম্বর এবং ভুল উত্তরের জন্য কোনো নম্বর কাটা যায় না। তাই সবগুলো প্রশ্নের উত্তর দেওয়া উচিত।</p>

  <h3 class="htbd-academic-subheading">MCQ-তে সর্বোচ্চ নম্বর পাওয়ার কার্যকর কৌশল</h3>
  <p><strong>১. প্যাসেজ আগে পড়ুন:</strong> MCQ-র বিকল্পগুলো দেখার আগে পুরো প্যাসেজটি মনোযোগ দিয়ে পড়ুন এবং মূলভাব বোঝার চেষ্টা করুন।</p>
  <p><strong>২. কী-ওয়ার্ড খুঁজুন:</strong> প্রতিটি প্রশ্নে থাকা গুরুত্বপূর্ণ শব্দ (keyword) প্যাসেজে চিহ্নিত করুন।</p>
  <p><strong>৩. Distractor চিনুন:</strong> পরীক্ষায় অনেক বিকল্প প্রায় সঠিক মনে হয় — এগুলোকে Distractor বলে। প্যাসেজের সাথে সরাসরি মিলিয়ে সঠিক উত্তর বেছে নিন।</p>
  <p><strong>৪. দুটি সম্ভাব্য উত্তর হলে:</strong> যে বিকল্পটি প্যাসেজের ভাষার সবচেয়ে কাছাকাছি, সেটি বেছে নিন।</p>
  <p><strong>৫. অনুমান নয়, প্যাসেজ থেকে খুঁজুন:</strong> নিজের সাধারণ জ্ঞান বা অনুমানের উপর নির্ভর না করে সবসময় প্যাসেজ থেকে প্রমাণ খুঁজুন।</p>

  <div class="htbd-tip-box">
    <p><strong>পরামর্শ (Tip):</strong> MCQ-তে সাধারণত vocabulary, main idea, inference, and reference questions আসে। EFT বইয়ের প্রতিটি ইউনিটের Comprehension Questions ভালোভাবে অনুশীলন করলে MCQ-তে সহজেই পূর্ণ নম্বর পাওয়া যায়।</p>
  </div>

  <h2 class="htbd-academic-heading" id="qa-guide">৩. প্রশ্ন ২: প্রশ্নোত্তর লেখার নিয়ম (Q2 Open-Ended Answering Questions)</h2>
  <p>প্রশ্ন ২-এ ১ম সিন প্যাসেজ থেকে ৫টি Open-Ended প্রশ্নের উত্তর লিখতে হয়। প্রতিটি উত্তরের জন্য সর্বোচ্চ ২ নম্বর।</p>

  <h3 class="htbd-academic-subheading">নম্বর পাওয়ার কাঠামো (Marking Criteria)</h3>
  <p>পরীক্ষকরা সাধারণত দুটি বিষয়ের উপর নম্বর দেন: <strong>(১) তথ্যের সঠিকতা</strong> এবং <strong>(২) ভাষার মানের স্বচ্ছতা।</strong> একটিতে ১ করে মোট ২ নম্বর।</p>

  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 22px 0;">
    <table class="htbd-academic-table">
      <thead>
        <tr><th>উত্তরের মান</th><th>নম্বর</th><th>বিবরণ</th></tr>
      </thead>
      <tbody>
        <tr><td>সম্পূর্ণ সঠিক তথ্য + সঠিক ভাষা</td><td>2/2</td><td>প্যাসেজ থেকে সঠিক তথ্য + নিজের ভাষায় লেখা</td></tr>
        <tr><td>সঠিক তথ্য + আংশিক ভুল ভাষা</td><td>1.5/2</td><td>তথ্য সঠিক কিন্তু grammar-এ সামান্য ত্রুটি</td></tr>
        <tr><td>আংশিক সঠিক / অসম্পূর্ণ উত্তর</td><td>1/2</td><td>মূল পয়েন্ট অনুপস্থিত</td></tr>
        <tr><td>ভুল বা প্রাসঙ্গিক নয়</td><td>0/2</td><td>প্যাসেজের সাথে কোনো সম্পর্ক নেই</td></tr>
      </tbody>
    </table>
  </div>

  <h3 class="htbd-academic-subheading">উত্তর লেখার সঠিক পদ্ধতি (Answer Writing Method)</h3>
  <p><strong>ধাপ ১:</strong> প্রশ্নটি মনোযোগ দিয়ে পড়ুন এবং Wh-word চিহ্নিত করুন (What, Why, How, When, Who)।</p>
  <p><strong>ধাপ ২:</strong> প্যাসেজে সংশ্লিষ্ট অংশ খুঁজুন।</p>
  <p><strong>ধাপ ৩:</strong> উত্তর <strong>সম্পূর্ণ বাক্যে</strong> লিখুন — হ্যাঁ/না বা এক শব্দে উত্তর দেবেন না।</p>
  <p><strong>ধাপ ৪:</strong> প্যাসেজ হুবহু কপি না করে নিজের ভাষায় প্যারাফ্রেজ করুন।</p>
  <p><strong>ধাপ ৫:</strong> উত্তর ২-৩ বাক্যের মধ্যে সীমাবদ্ধ রাখুন — অপ্রাসঙ্গিক তথ্য যোগ করবেন না।</p>

  <div class="htbd-warning-box">
    <p><strong>সতর্কতা:</strong> প্যাসেজ হুবহু কপি করলে নম্বর কাটা যায়। উত্তর সবসময় নিজের ভাষায় (own words/paraphrase) লিখতে হবে।</p>
  </div>

  <h2 class="htbd-academic-heading" id="gap-fill-guide">৪. প্রশ্ন ৩: Gap Filling Without Clues — সম্পূর্ণ নির্দেশিকা (Q3 Gap Filling)</h2>
  <p>প্রশ্ন ৩-এ ২য় সিন প্যাসেজ থেকে ৫টি শূন্যস্থান পূরণ করতে হয় — কোনো word bank বা clue দেওয়া থাকে না। প্রতিটি সঠিক উত্তরের জন্য ১ নম্বর।</p>

  <h3 class="htbd-academic-subheading">Gap Filling Without Clues — কৌশল ও নিয়মাবলি</h3>
  <p><strong>১. প্রসঙ্গ বুঝুন (Context Understanding):</strong> শূন্যস্থানের আগে ও পরের বাক্য পড়ে বুঝুন কী ধরনের শব্দ দরকার — Noun, Verb, Adjective, Adverb নাকি Preposition।</p>
  <p><strong>২. Grammatical Agreement:</strong> Subject-Verb Agreement মেনে শব্দ বসান। Singular Subject হলে Singular Verb।</p>
  <p><strong>৩. Tense সামঞ্জস্য:</strong> পুরো প্যাসেজের Tense লক্ষ করুন এবং সেই অনুযায়ী ক্রিয়ার সঠিক রূপ বসান।</p>
  <p><strong>৪. পাঠ্যবই থেকে শব্দ:</strong> উত্তর সাধারণত সংশ্লিষ্ট EFT ইউনিটের ভেতর থেকেই আসে। প্যাসেজের বাকি অংশে উত্তর লুকিয়ে থাকতে পারে।</p>
  <p><strong>৫. Collocations:</strong> কিছু শব্দ জোড়ায় আসে (যেমন: make a decision, pay attention) — এগুলো মনে রাখলে Gap Fill সহজ হয়।</p>

  <div class="htbd-tip-box">
    <p><strong>পরামর্শ:</strong> EFT বইয়ের প্রতিটি ইউনিট পড়ার সময় নতুন শব্দের অর্থ, ব্যবহার ও collocations একটি নোটবুকে লিখে রাখুন। Gap Fill-এর জন্য এটি সবচেয়ে কার্যকর প্রস্তুতি পদ্ধতি।</p>
  </div>

  <h2 class="htbd-academic-heading" id="important-passages">৫. গুরুত্বপূর্ণ সিন প্যাসেজ তালিকা (Important EFT Seen Passage List for SSC 2027)</h2>
  <p>English For Today (EFT) বইয়ের নিচের ইউনিটগুলো SSC 2027-এর সিন প্যাসেজ হিসেবে আসার সম্ভাবনা সবচেয়ে বেশি। এই প্যাসেজগুলো বারবার পড়লে MCQ, Q/A এবং Gap Fill — তিনটিতেই ভালো করা সম্ভব।</p>

  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 22px 0;">
    <table class="htbd-academic-table">
      <thead>
        <tr><th>ইউনিট ও পাঠ</th><th>বিষয় (Topic)</th><th>গুরুত্ব</th></tr>
      </thead>
      <tbody>
        <tr><td>Unit 1, Lesson 1</td><td>Our Beautiful Motherland</td><td>অত্যন্ত গুরুত্বপূর্ণ</td></tr>
        <tr><td>Unit 2, Lesson 1</td><td>Liberation War of Bangladesh</td><td>অত্যন্ত গুরুত্বপূর্ণ</td></tr>
        <tr><td>Unit 4, Lesson 1</td><td>Computer and Internet</td><td>গুরুত্বপূর্ণ</td></tr>
        <tr><td>Unit 5, Lesson 1</td><td>Food and Nutrition</td><td>গুরুত্বপূর্ণ</td></tr>
        <tr><td>Unit 7, Lesson 1</td><td>Environment and Climate Change</td><td>গুরুত্বপূর্ণ</td></tr>
        <tr><td>Unit 9, Lesson 1</td><td>Health and Hygiene</td><td>গুরুত্বপূর্ণ</td></tr>
        <tr><td>Unit 11, Lesson 1</td><td>Gender Equality and Rights</td><td>মাঝারি গুরুত্বপূর্ণ</td></tr>
        <tr><td>Unit 12, Lesson 1</td><td>Sports and Recreation</td><td>মাঝারি গুরুত্বপূর্ণ</td></tr>
      </tbody>
    </table>
  </div>

  <h2 class="htbd-academic-heading" id="model-answer">৬. নমুনা সমাধান (Seen Passage Model Answer Example)</h2>
  <p>নিচে একটি সাধারণ সিন প্যাসেজ এবং তার MCQ ও Q/A-র নমুনা উত্তর দেওয়া হলো, যা পরীক্ষার উত্তরের ধরন বুঝতে সাহায্য করবে।</p>

  <h3 class="htbd-academic-subheading">নমুনা প্যাসেজ (Sample Seen Passage)</h3>
  <p style="background:#f8fafc; border-left:4px solid #94a3b8; padding:16px 20px; border-radius:6px; font-style:italic; color:#334155;">Bangladesh is a small but beautiful country. It has a rich history and culture. The Liberation War of 1971 is the most important chapter in its history. Millions of people sacrificed their lives for the independence of Bangladesh. The rivers, forests and natural beauty of this country attract people from all over the world. The national language of Bangladesh is Bengali, which is the mother tongue of more than 250 million people worldwide.</p>

  <h3 class="htbd-academic-subheading">MCQ উত্তরের ধরন (Q1 Sample MCQ)</h3>
  <p><strong>Q: Bangladesh is described as —</strong><br>
  (a) large and beautiful &nbsp; (b) small but beautiful &nbsp; (c) small and poor &nbsp; (d) rich and large</p>
  <p><strong>উত্তর: (b) small but beautiful</strong> — কারণ প্যাসেজের প্রথম বাক্যে সরাসরি বলা হয়েছে "Bangladesh is a small but beautiful country."</p>

  <h3 class="htbd-academic-subheading">Q/A উত্তরের নমুনা (Q2 Sample Answer)</h3>
  <p><strong>Q: Why is the Liberation War of 1971 important in Bangladesh's history?</strong></p>
  <p><strong>উত্তর:</strong> The Liberation War of 1971 is the most important chapter in Bangladesh's history because millions of people sacrificed their lives to achieve the country's independence. It is the foundation of Bangladesh's identity as an independent nation.</p>

  <h2 class="htbd-academic-heading" id="faq">৭. সচরাচর জিজ্ঞাসা (Frequently Asked Questions — FAQ)</h2>

  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">Question 1: Seen Passage কি পাঠ্যবই থেকেই আসে? (Does Seen Passage come from the textbook?)</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">হ্যাঁ, SSC পরীক্ষায় Seen Passage সবসময় English For Today (EFT) পাঠ্যবইয়ের নির্ধারিত ইউনিট ও পাঠ থেকে আসে। তাই পাঠ্যবই ভালোভাবে পড়লে সিন প্যাসেজে পূর্ণ নম্বর পাওয়া সম্ভব।</p>
  </div>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">Question 2: Gap Filling-এ ভুল হলে কি নম্বর কাটা যায়? (Is there negative marking for wrong Gap Fill answer?)</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">না, SSC পরীক্ষায় Gap Filling বা অন্য কোনো Written প্রশ্নে ভুল উত্তরের জন্য নেগেটিভ মার্কিং নেই। তাই সবসময় উত্তর দেওয়ার চেষ্টা করবেন।</p>
  </div>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">Question 3: Q2-এর উত্তর কত শব্দে লিখতে হয়? (How long should Q2 answers be?)</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">Q2-এর প্রতিটি উত্তর সাধারণত ২-৩টি সম্পূর্ণ বাক্যে (৩০-৫০ শব্দ) লেখাই যথেষ্ট। অতিরিক্ত লেখার প্রয়োজন নেই — সঠিক তথ্য ও স্পষ্ট ভাষাই মূল বিষয়।</p>
  </div>

  {series_nav}

</div>

<!-- Schema: BlogPosting -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "mainEntityOfPage": {{"@type": "WebPage", "@id": "{url}"}},
  "headline": "{title}",
  "description": "{meta_desc}",
  "image": "{banner_url}",
  "author": {{"@type": "Person", "name": "Faruk Sir", "url": "https://www.helptrickbd.com/p/about-us.html"}},
  "publisher": {{"@type": "Organization", "name": "HelpTrickBD", "logo": {{"@type": "ImageObject", "url": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/logo.png"}}}},
  "datePublished": "2026-09-17T00:00:00+06:00"
}}
</script>
<!-- Schema: FAQPage -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{"@type": "Question", "name": "Does Seen Passage come from the textbook in SSC?", "acceptedAnswer": {{"@type": "Answer", "text": "Yes, Seen Passage always comes from the English For Today (EFT) textbook units in SSC exam."}}}},
    {{"@type": "Question", "name": "Is there negative marking for wrong Gap Fill answer in SSC?", "acceptedAnswer": {{"@type": "Answer", "text": "No, there is no negative marking for wrong written answers including Gap Filling in SSC exam. Always attempt all questions."}}}},
    {{"@type": "Question", "name": "How long should Q2 answers be in SSC English 1st Paper?", "acceptedAnswer": {{"@type": "Answer", "text": "Q2 answers should be 2-3 complete sentences (30-50 words). Focus on correct information and clear language."}}}}
  ]
}}
</script>
"""
    meta = {
        "title": title,
        "slug": slug,
        "custom_url": url,
        "url": url,
        "labels": LABELS,
        "search_description": meta_desc,
        "meta_description": meta_desc
    }
    return slug, html, meta


# ─────────────────────────────────────────────────────────────────────────────
# POST 02: UNSEEN PASSAGE & SUMMARY WRITING (Q 4-5)
# ─────────────────────────────────────────────────────────────────────────────
def generate_post_02():
    slug = "ssc-2027-english-unseen-passage-summary"
    title = "এসএসসি ২০২৭ আনসিন প্যাসেজ ও সামারি রাইটিং সম্পূর্ণ গাইড (SSC 2027 English Unseen Passage Information Transfer & Summary Writing)"
    meta_desc = "SSC 2027 English Unseen Passage ও Summary Writing গাইড। Information Transfer ও Summary Writing — ১৫ নম্বরের শতভাগ কমন কৌশল ও পূর্ণ সমাধান।"
    banner_url = f"{CDN_BASE}/ssc_2027_silo_02_unseen_summary.webp"
    banner_alt = "SSC 2027 English Unseen Passage and Summary Writing Guide"
    url = f"{BLOG_BASE}/{slug}.html"
    series_nav = get_series_nav("Part 02")

    html = get_css_block() + f"""
<div class="htbd-academic-container">

  <figure style="margin: 0 0 20px 0;">
    <img class="htbd-hero-img" src="{banner_url}" alt="{banner_alt}" title="{banner_alt}" width="1200" height="675" loading="eager" />
    <figcaption style="font-size: 14px; color: #64748b; text-align: center; margin-top: 6px;">SSC 2027 English 1st Paper Unseen Passage & Summary Writing — Part 02 of the Study Silo Series</figcaption>
  </figure>

  <div class="htbd-overview-box">
    <p>এসএসসি ২০২৭ ইংরেজি ১ম পত্রে <strong>প্রশ্ন ৪ ও ৫</strong> Unseen (অপরিচিত) Passage থেকে আসে এবং মোট <strong>১৫ নম্বর</strong> বরাদ্দ। Information Transfer (৫ নম্বর) ও Summary Writing (১০ নম্বর) — এই দুটিতে কৌশলী প্রস্তুতি থাকলে পূর্ণ নম্বর পাওয়া সম্ভব। (SSC 2027 Questions 4 and 5 come from an Unseen Passage for a total of 15 marks.)</p>
  </div>

<!--more-->

  <div class="htbd-toc-card">
    <p class="toc-title">বিষয়সূচি (Table of Contents)</p>
    <ul>
      <li><a href="#unseen-marks">১. আনসিন প্যাসেজ: নম্বর বণ্টন ও প্রশ্নের ধরন</a></li>
      <li><a href="#info-transfer">২. প্রশ্ন ৪: Information Transfer — সম্পূর্ণ নিয়মাবলি (Q4 Guide)</a></li>
      <li><a href="#summary-guide">৩. প্রশ্ন ৫: Summary Writing — সম্পূর্ণ নির্দেশিকা (Q5 Guide)</a></li>
      <li><a href="#summary-steps">৪. Summary লেখার ধাপে ধাপে পদ্ধতি (Step-by-Step Method)</a></li>
      <li><a href="#model-summary">৫. নমুনা Summary (Model Summary Answer)</a></li>
      <li><a href="#common-mistakes">৬. সামারি লেখার সাধারণ ভুলসমূহ ও প্রতিকার (Common Mistakes in Summary)</a></li>
      <li><a href="#unseen-topics">৭. ২০২৭ সালের সম্ভাব্য গুরুত্বপূর্ণ আনসিন প্যাসেজ তালিকা (Top Unseen Topics)</a></li>
      <li><a href="#q4-tips">৮. ইনফরমেশন ট্রান্সফার (Q4) টেবিল পূরণের সোনালী কৌশল</a></li>
      <li><a href="#faq">৯. সচরাচর জিজ্ঞাসা (FAQ)</a></li>
    </ul>
  </div>

  <h2 class="htbd-academic-heading" id="unseen-marks">১. আনসিন প্যাসেজ: নম্বর বণ্টন (Unseen Passage Marks Distribution)</h2>
  <p>Unseen Passage মানে পরীক্ষার হলে প্রথমবার দেখা অনুচ্ছেদ — এটি পাঠ্যবই থেকে আসে না। তাই এই অংশে পূর্ব প্রস্তুতির চেয়ে পড়ার দক্ষতা ও কৌশলই মূল চাবিকাঠি।</p>

  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 24px 0;">
    <table class="htbd-academic-table">
      <thead>
        <tr><th>প্রশ্ন</th><th>প্রশ্নের ধরন</th><th>নম্বর</th><th>মূল দক্ষতা</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>Q4</strong></td><td>Information Transfer (Chart/Table পূরণ)</td><td><strong>1 × 5 = 5</strong></td><td>তথ্য সংগ্রহ ও সঠিক ঘরে বসানো</td></tr>
        <tr><td><strong>Q5</strong></td><td>Summary Writing (এক-তৃতীয়াংশে)</td><td><strong>10</strong></td><td>মূলভাব বোঝা ও সংক্ষিপ্তকরণ</td></tr>
        <tr><td colspan="2" style="text-align:right; font-weight:700; background:#f1f5f9;">মোট:</td><td style="font-weight:700; background:#f1f5f9; color:#0c2340;"><strong>15</strong></td><td style="background:#f1f5f9;"></td></tr>
      </tbody>
    </table>
  </div>

  <h2 class="htbd-academic-heading" id="info-transfer">২. প্রশ্ন ৪: Information Transfer — সম্পূর্ণ নিয়মাবলি (Q4 Information Transfer Guide)</h2>
  <p>প্রশ্ন ৪-এ Unseen Passage পড়ে একটি Table, Chart বা Flow Chart পূরণ করতে হয়। প্যাসেজের তথ্য সঠিক ঘরে বসানোই মূল কাজ।</p>

  <h3 class="htbd-academic-subheading">Information Transfer-এ সর্বোচ্চ নম্বর পাওয়ার কৌশল</h3>
  <p><strong>১. Table/Chart আগে দেখুন:</strong> Passage পড়ার আগে Chart বা Table-এর ঘরগুলো দেখুন — কী ধরনের তথ্য চাওয়া হচ্ছে তা বুঝুন।</p>
  <p><strong>২. Skim করুন:</strong> পুরো Passage দ্রুত একবার চোখ বুলিয়ে মূল বিষয় ধরুন।</p>
  <p><strong>৩. তথ্য চিহ্নিত করুন:</strong> Passage-এ Table-এর প্রতিটি ঘরের সাথে মিলে যায় এমন তথ্য পেন্সিল দিয়ে আন্ডারলাইন করুন।</p>
  <p><strong>৪. সংক্ষিপ্ত উত্তর:</strong> Information Transfer-এ সম্পূর্ণ বাক্য লেখার দরকার নেই — Key phrase বা word-ই যথেষ্ট।</p>
  <p><strong>৫. বানান যাচাই:</strong> Passage থেকে সরাসরি শব্দ নেওয়া হলে বানান ভুলের সম্ভাবনা কমে। সঠিক বানান নিশ্চিত করুন।</p>

  <div class="htbd-tip-box">
    <p><strong>পরামর্শ:</strong> Information Transfer-এ Chart-এর প্রতিটি ঘরের heading ভালো করে পড়ুন। ঘরের heading-ই বলে দেয় কী ধরনের তথ্য সেখানে যাবে — সংখ্যা, নাম, তারিখ, বা বিবরণ।</p>
  </div>

  <h2 class="htbd-academic-heading" id="summary-guide">৩. প্রশ্ন ৫: Summary Writing — সম্পূর্ণ নির্দেশিকা (Q5 Summary Writing Full Guide)</h2>
  <p>Summary Writing হলো SSC English 1st Paper-এর সবচেয়ে মূল্যবান প্রশ্ন — একটিমাত্র প্রশ্নে ১০ নম্বর। এখানে Unseen Passage-এর মূলভাব সংক্ষেপে নিজের ভাষায় লিখতে হয়।</p>

  <h3 class="htbd-academic-subheading">Summary-র মানদণ্ড (Marking Criteria for Summary Writing)</h3>
  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 22px 0;">
    <table class="htbd-academic-table">
      <thead>
        <tr><th>মানদণ্ড</th><th>নম্বর</th><th>বিবরণ</th></tr>
      </thead>
      <tbody>
        <tr><td>Content (মূলভাব ধরা)</td><td>5</td><td>সব গুরুত্বপূর্ণ point অন্তর্ভুক্ত আছে কিনা</td></tr>
        <tr><td>Language (ভাষার মান)</td><td>3</td><td>Grammar, Spelling, Vocabulary সঠিকতা</td></tr>
        <tr><td>Length (দৈর্ঘ্য)</td><td>2</td><td>মূল Passage-এর এক-তৃতীয়াংশ (সাধারণত ৫০-৭০ শব্দ)</td></tr>
      </tbody>
    </table>
  </div>

  <h2 class="htbd-academic-heading" id="summary-steps">৪. Summary লেখার ধাপে ধাপে পদ্ধতি (Step-by-Step Summary Writing Method)</h2>

  <p><strong>ধাপ ১ — Passage পড়ুন:</strong> পুরো Passage মনোযোগ দিয়ে পড়ুন এবং প্রধান বিষয় (Main Idea) চিহ্নিত করুন।</p>
  <p><strong>ধাপ ২ — Key Points চিহ্নিত করুন:</strong> প্রতিটি প্যারাগ্রাফের একটি করে মূল বক্তব্য (Key Point) আন্ডারলাইন করুন।</p>
  <p><strong>ধাপ ৩ — রাফ draft লিখুন:</strong> Passage না দেখে Key Points থেকে মনে মনে বা রাফে Summary লিখুন।</p>
  <p><strong>ধাপ ৪ — শব্দ গণনা করুন:</strong> Passage-এর মোট শব্দের এক-তৃতীয়াংশ শব্দে Summary লিখুন।</p>
  <p><strong>ধাপ ৫ — Quotation বর্জন করুন:</strong> Passage থেকে সরাসরি line কপি করা যাবে না — নিজের ভাষায় (Paraphrase) লিখতে হবে।</p>
  <p><strong>ধাপ ৬ — শিরোনাম দিন:</strong> Summary-র শুরুতে "Summary:" বা "The passage is about..." দিয়ে শুরু করুন।</p>

  <div class="htbd-warning-box">
    <p><strong>সতর্কতা:</strong> Passage থেকে হুবহু বাক্য কপি করলে নম্বর পাওয়া যায় না। Summary সবসময় নিজের ভাষায় (own words / paraphrase) লিখতে হবে।</p>
  </div>

  <h2 class="htbd-academic-heading" id="model-summary">৫. নমুনা Summary (Model Summary Answer)</h2>
  <p>নিচে একটি নমুনা Unseen Passage এবং তার আদর্শ Summary দেওয়া হলো:</p>

  <h3 class="htbd-academic-subheading">নমুনা Passage (Sample Unseen Passage)</h3>
  <p style="background:#f8fafc; border-left:4px solid #94a3b8; padding:16px 20px; border-radius:6px; font-style:italic; color:#334155;">Trees are very important for our existence. They give us oxygen, food, shelter and medicine. Trees help control climate by absorbing carbon dioxide from the air. They also prevent soil erosion by holding soil together with their roots. Many animals and birds depend on trees for their home and food. Without trees, our planet would become a lifeless desert. That is why we must protect trees and plant more of them to save our environment.</p>
  <p style="color:#64748b; font-size:15px;">[মোট: প্রায় ৮৫ শব্দ — Summary হবে প্রায় ২৮-৩০ শব্দে]</p>

  <h3 class="htbd-academic-subheading">আদর্শ Summary (Model Answer)</h3>
  <p style="background:#f0fdf4; border:1px solid #bbf7d0; padding:16px 20px; border-radius:8px; color:#14532d; font-style:italic;">Trees are essential for life as they provide oxygen, food, shelter and medicine. They control climate, prevent soil erosion and support wildlife. Since trees are vital for our environment, we must protect and plant more of them.</p>
  <p style="color:#64748b; font-size:15px;">[মোট: ৩২ শব্দ — মূল Passage-এর এক-তৃতীয়াংশের মধ্যে]</p>

  <h2 class="htbd-academic-heading" id="common-mistakes">৬. সামারি লেখার সাধারণ ভুলসমূহ ও প্রতিকার (Common Mistakes in Summary Writing)</h2>
  <p>প্রতি বছর এসএসসি পরীক্ষায় বহু শিক্ষার্থী আনসিন প্যাসেজ ভালো বুঝেও সামারিতে কাঙ্ক্ষিত নম্বর পায় না। প্রধান ভুলগুলো এবং তা সংশোধনের উপায় নিচে আলোচনা করা হলো:</p>
  <ul>
    <li><strong>হুবহু লাইন কপি করা:</strong> প্যাসেজের প্রথম বা শেষ দুই-তিনটি লাইন হুবহু তুলে দিলে পরীক্ষক ০ বা খুব কম নম্বর দেন। সমাধানের উপায়: মূল বক্তব্য ঠিক রেখে নিজের সহজ ভাষায় বাক্য লিখুন।</li>
    <li><strong>অতিরিক্ত বড় বা ছোট করা:</strong> সামারি যদি মূল প্যাসেজের সমান বড় হয় অথবা মাত্র এক লাইনে শেষ হয়, তবে নম্বর কাটা যায়। আদর্শ দৈর্ঘ্য হলো মূল লেখার এক-তৃতীয়াংশ (৫০ থেকে ৭০ শব্দ)।</li>
    <li><strong>উদ্ধৃতি ও উদাহরণ অন্তর্ভুক্ত করা:</strong> প্যাসেজে থাকা প্রত্যক্ষ উক্তি ("..."), পরিসংখ্যান বা অপ্রয়োজনীয় ছোটখাটো উদাহরণ সামারিতে আনা সম্পূর্ণ নিষেধ। শুধুমাত্র মূল ভাব (Core Theme) লিখবেন।</li>
    <li><strong>নিজের ব্যক্তিগত মতামত যোগ করা:</strong> সামারিতে "I think", "In my opinion" বা নিজের কোনো পরামর্শ দেওয়া যাবে না। লেখক যা বলেছেন কেবল তাই সংক্ষেপে উপস্থাপন করতে হবে।</li>
  </ul>

  <h2 class="htbd-academic-heading" id="unseen-topics">৭. ২০২৭ সালের সম্ভাব্য গুরুত্বপূর্ণ আনসিন প্যাসেজ তালিকা (Top Unseen Topics for SSC 2027)</h2>
  <p>বিগত বছরগুলোর বোর্ড প্রশ্ন ও আল ফাতাহ স্পেশাল মডেল টেস্ট বিশ্লেষণ করে ২০২৭ সালের পরীক্ষার্থীদের জন্য সর্বাধিক গুরুত্বপূর্ণ আনসিন বিষয়সমূহ নির্বাচন করা হয়েছে:</p>

  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 22px 0;">
    <table class="htbd-academic-table">
      <thead>
        <tr><th>ক্রম</th><th>আনসিন বিষয় / ব্যক্তিত্ব</th><th>মূল ফোকাস</th><th>কমন সম্ভাব্যতা</th></tr>
      </thead>
      <tbody>
        <tr><td>০১</td><td>Dr. Muhammad Shahidullah / Kazi Nazrul Islam</td><td>শিক্ষা, সাহিত্য ও জীবনীভিত্তিক তথ্য</td><td>৩-স্টার (৯৯%)</td></tr>
        <tr><td>০২</td><td>Begum Rokeya / Mother Teresa</td><td>নারী শিক্ষা ও সমাজকল্যাণমূলক অবদান</td><td>৩-স্টার (৯৫%)</td></tr>
        <tr><td>০৩</td><td>Climate Change &amp; Global Warming</td><td>পরিবেশ দূষণ, প্রভাব ও বৈশ্বিক সতর্কতা</td><td>৩-স্টার (৯৮%)</td></tr>
        <tr><td>০৪</td><td>The Sundarbans &amp; Royal Bengal Tiger</td><td>প্রাকৃতিক ঐতিহ্য, জীববৈচিত্র্য ও বন সংরক্ষণ</td><td>২-স্টার (৯০%)</td></tr>
        <tr><td>০৫</td><td>Neil Armstrong / Stephen Hawking</td><td>মহাকাশ বিজ্ঞান ও মানবজাতির আবিষ্কার</td><td>২-স্টার (৮৮%)</td></tr>
        <tr><td>০৬</td><td>Nelson Mandela / Abraham Lincoln</td><td>বর্ণবাদ বিরোধী সংগ্রাম ও গণতন্ত্রের ইতিহাস</td><td>২-স্টার (৮৫%)</td></tr>
      </tbody>
    </table>
  </div>

  <h2 class="htbd-academic-heading" id="q4-tips">৮. ইনফরমেশন ট্রান্সফার (Q4) টেবিল পূরণের সোনালী ৫টি কৌশল</h2>
  <p>প্রশ্ন ৪-এ পুরো ৫ নম্বর নিশ্চিত করার জন্য নিচের ৫টি টেকনিক অনুসরণ করুন:</p>
  <ol>
    <li><strong>Who / What কলাম লক্ষ্য করুন:</strong> ব্যক্তি বা বিষয়ের নাম সঠিকভাবে প্যাসেজ থেকে খুঁজে বের করুন। নামের বানান যেন কোনোভাবেই ভুল না হয়।</li>
    <li><strong>Event / Activity কলাম:</strong> ওই ব্যক্তি কী কাজ করেছিলেন বা কী ঘটনা ঘটেছিল তা সংক্ষেপে অতীত কালে (Past Form) লিখুন।</li>
    <li><strong>Time / When কলাম:</strong> সাল, তারিখ বা সময় সংক্রান্ত তথ্য প্যাসেজে সংখ্যা আকারে থাকে, সেগুলো নিখুঁতভাবে তুলুন।</li>
    <li><strong>Place / Where কলাম:</strong> স্থান, শহর বা দেশের নাম লেখার সময় ক্যাপিটাল লেটার ব্যবহার নিশ্চিত করুন।</li>
    <li><strong>অতিরিক্ত শব্দ বর্জন:</strong> চার্টের ঘরে পুরো বাক্য লেখার প্রয়োজন নেই, শুধুমাত্র নির্দিষ্ট তথ্যটি (Fact) লিখুন।</li>
  </ol>

  <h2 class="htbd-academic-heading" id="faq">৯. সচরাচর জিজ্ঞাসা (Frequently Asked Questions — FAQ)</h2>

  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">Question 1: Summary কত শব্দে লিখতে হয়? (How many words should a summary be?)</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">সাধারণত মূল Passage-এর এক-তৃতীয়াংশ শব্দে Summary লিখতে হয়। SSC পরীক্ষায় Passage সাধারণত ১৫০-২০০ শব্দের হয়, তাই Summary হবে ৫০-৭০ শব্দের মধ্যে।</p>
  </div>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">Question 2: Summary-তে কি Title দিতে হয়? (Should I give a title in the Summary?)</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">SSC পরীক্ষায় Summary-র জন্য আলাদা Title দেওয়া বাধ্যতামূলক নয়। তবে "Summary:" বা "The passage is about..." দিয়ে শুরু করলে উত্তর গোছানো দেখায় এবং নম্বর পাওয়ার সম্ভাবনা বাড়ে।</p>
  </div>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">Question 3: Information Transfer-এ কি সম্পূর্ণ বাক্য লিখতে হয়? (Do I need to write full sentences in Q4?)</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">না, Information Transfer-এ সম্পূর্ণ বাক্যের প্রয়োজন নেই। Key word বা phrase দিয়ে উত্তর দেওয়া যায়। তবে নাম, তারিখ বা সংখ্যার ক্ষেত্রে সঠিকতা নিশ্চিত করুন।</p>
  </div>

  {series_nav}

</div>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "mainEntityOfPage": {{"@type": "WebPage", "@id": "{url}"}},
  "headline": "{title}",
  "description": "{meta_desc}",
  "image": "{banner_url}",
  "author": {{"@type": "Person", "name": "Faruk Sir", "url": "https://www.helptrickbd.com/p/about-us.html"}},
  "publisher": {{"@type": "Organization", "name": "HelpTrickBD", "logo": {{"@type": "ImageObject", "url": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/logo.png"}}}},
  "datePublished": "2026-09-17T00:30:00+06:00"
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{"@type": "Question", "name": "How many words should an SSC English summary be?", "acceptedAnswer": {{"@type": "Answer", "text": "The summary should be one-third of the original passage length, typically 50-70 words for SSC exam."}}}},
    {{"@type": "Question", "name": "Do I need full sentences in Information Transfer Q4?", "acceptedAnswer": {{"@type": "Answer", "text": "No, key words or phrases are sufficient for Information Transfer. Ensure accuracy of names, dates and numbers."}}}},
    {{"@type": "Question", "name": "Can I copy sentences directly from the passage for the summary?", "acceptedAnswer": {{"@type": "Answer", "text": "No, copying sentences directly from the passage results in poor marks. Always paraphrase the core idea in your own simple English sentences."}}}}
  ]
}}
</script>
"""
    meta = {"title": title, "slug": slug, "custom_url": url, "url": url, "labels": LABELS, "search_description": meta_desc, "meta_description": meta_desc}
    return slug, html, meta


# ─────────────────────────────────────────────────────────────────────────────
# POST 03: MATCHING TABLE & RE-ARRANGING (Q 6-7)
# ─────────────────────────────────────────────────────────────────────────────
def generate_post_03():
    slug = "ssc-2027-english-matching-rearrange"
    title = "এসএসসি ২০২৭ ম্যাচিং টেবিল ও রি-অ্যারেঞ্জ সম্পূর্ণ সমাধান (SSC 2027 English Sentence Matching Table & Re-arranging Sentences Rules & Tips)"
    meta_desc = "SSC 2027 English 1st Paper Sentence Matching Table (Q6) ও Re-arranging Sentences (Q7) — মোট ১৩ নম্বরের সম্পূর্ণ নিয়মাবলি, কৌশল ও মডেল সমাধান।"
    banner_url = f"{CDN_BASE}/ssc_2027_silo_03_matching_rearrange.webp"
    banner_alt = "SSC 2027 English Sentence Matching Table and Re-arranging Sentences Guide"
    url = f"{BLOG_BASE}/{slug}.html"
    series_nav = get_series_nav("Part 03")

    html = get_css_block() + f"""
<div class="htbd-academic-container">

  <figure style="margin: 0 0 20px 0;">
    <img class="htbd-hero-img" src="{banner_url}" alt="{banner_alt}" title="{banner_alt}" width="1200" height="675" loading="eager" />
    <figcaption style="font-size: 14px; color: #64748b; text-align: center; margin-top: 6px;">SSC 2027 Sentence Matching Table & Re-arranging — Part 03 of the Study Silo Series</figcaption>
  </figure>

  <div class="htbd-overview-box">
    <p>এসএসসি ২০২৭ ইংরেজি ১ম পত্রে <strong>প্রশ্ন ৬</strong> (Sentence Matching Table) ও <strong>প্রশ্ন ৭</strong> (Re-arranging Sentences) থেকে মোট <strong>১৩ নম্বর</strong> আসে। এই দুটি প্রশ্নে Grammar ও Syntax-এর জ্ঞান প্রয়োজন। সঠিক কৌশল জানলে এই ১৩ নম্বরে পূর্ণ নম্বর পাওয়া সহজ। (Q6 Matching Table carries 5 marks and Q7 Re-arranging carries 8 marks — total 13 marks.)</p>
  </div>

<!--more-->

  <div class="htbd-toc-card">
    <p class="toc-title">বিষয়সূচি (Table of Contents)</p>
    <ul>
      <li><a href="#marks-table">১. নম্বর বণ্টন ও প্রশ্নের বিবরণ</a></li>
      <li><a href="#matching-guide">২. প্রশ্ন ৬: Sentence Matching Table — নিয়মাবলি (Q6 Guide)</a></li>
      <li><a href="#rearranging-guide">৩. প্রশ্ন ৭: Re-arranging Sentences — নিয়মাবলি (Q7 Guide)</a></li>
      <li><a href="#grammar-tips">৪. Connectives ও Coherence-এর গুরুত্বপূর্ণ নিয়ম</a></li>
      <li><a href="#model-answers">৫. নমুনা সমাধান: Matching ও Re-arranging (Model Answers)</a></li>
      <li><a href="#top-rearrange">৬. ২০২৭ সালের সম্ভাব্য ৫টি বহুল কমন রি-অ্যারেঞ্জ গল্প ও জীবনী</a></li>
      <li><a href="#box-technique">৭. রি-অ্যারেঞ্জে পূর্ণ ৮ নম্বর পাওয়ার বক্স কৌশল</a></li>
      <li><a href="#faq">৮. সচরাচর জিজ্ঞাসা (FAQ)</a></li>
    </ul>
  </div>

  <h2 class="htbd-academic-heading" id="marks-table">১. নম্বর বণ্টন (Marks Distribution — Q6 & Q7)</h2>
  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 24px 0;">
    <table class="htbd-academic-table">
      <thead>
        <tr><th>প্রশ্ন</th><th>প্রশ্নের ধরন</th><th>বিবরণ</th><th>নম্বর</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>Q6</strong></td><td>Sentence Matching Table</td><td>Column A, B এবং C — বাক্যের অংশ মেলাতে হবে</td><td><strong>1 × 5 = 5</strong></td></tr>
        <tr><td><strong>Q7</strong></td><td>Re-arranging Sentences</td><td>৮টি এলোমেলো বাক্য সঠিক ক্রমে সাজাতে হবে</td><td><strong>1 × 8 = 8</strong></td></tr>
        <tr><td colspan="3" style="text-align:right; font-weight:700; background:#f1f5f9;">মোট:</td><td style="font-weight:700; background:#f1f5f9; color:#0c2340;"><strong>13</strong></td></tr>
      </tbody>
    </table>
  </div>

  <h2 class="htbd-academic-heading" id="matching-guide">২. প্রশ্ন ৬: Sentence Matching Table — সম্পূর্ণ নিয়মাবলি (Q6 Sentence Matching Guide)</h2>
  <p>Q6-এ তিনটি Column (A, B, C) থাকে। Column A-তে বাক্যের শুরু, Column B ও C-তে বাক্যের মাঝের ও শেষের অংশ দেওয়া থাকে। সঠিকভাবে মিলিয়ে সম্পূর্ণ অর্থবোধক বাক্য তৈরি করতে হয়।</p>

  <h3 class="htbd-academic-subheading">Sentence Matching-এ সর্বোচ্চ নম্বর পাওয়ার কৌশল</h3>
  <p><strong>১. Grammatical Clues অনুসরণ করুন:</strong> Column A-তে Subject দেখে Column B-তে সঠিক Verb খুঁজুন। Subject-Verb Agreement মেনে চলুন।</p>
  <p><strong>২. Meaning-based matching:</strong> শুধু Grammar নয়, বাক্যের অর্থও মেলাতে হবে। সম্পূর্ণ বাক্যটি কি বাস্তবে অর্থবোধক?</p>
  <p><strong>৩. একটি option একবারই:</strong> প্রতিটি Column-এর option একবারই ব্যবহার করা যাবে — পুনরাবৃত্তি নয়।</p>
  <p><strong>৪. Process of elimination:</strong> নিশ্চিত মিল আগে করুন, এরপর বাকিগুলো থেকে উত্তর বের করুন।</p>
  <p><strong>৫. উত্তর লেখার ফরম্যাট:</strong> সম্পূর্ণ মিলিয়ে বাক্যটি লিখুন — শুধু অক্ষর বা নম্বর লিখলে নম্বর নাও পেতে পারেন।</p>

  <div class="htbd-tip-box">
    <p><strong>পরামর্শ:</strong> Connectives (because, although, so that, in order to, however, therefore) শেখা Q6-এর জন্য অত্যন্ত গুরুত্বপূর্ণ। এগুলো Column B বা C-তে থাকলে বাক্যের logical flow বুঝতে সাহায্য করে।</p>
  </div>

  <h2 class="htbd-academic-heading" id="rearranging-guide">৩. প্রশ্ন ৭: Re-arranging Sentences — সম্পূর্ণ নির্দেশিকা (Q7 Re-arranging Guide)</h2>
  <p>Q7-এ ৮টি এলোমেলো (Jumbled) বাক্য দেওয়া থাকে। এগুলো সঠিক Chronological ও Logical Order-এ সাজিয়ে একটি অর্থবোধক অনুচ্ছেদ তৈরি করতে হয়। প্রতিটি সঠিক বাক্যের জন্য ১ নম্বর।</p>

  <h3 class="htbd-academic-subheading">Re-arranging Sentences-এর কার্যকর কৌশল</h3>
  <p><strong>১. Topic Sentence খুঁজুন:</strong> যে বাক্যটি পুরো অনুচ্ছেদের বিষয় পরিচয় করিয়ে দেয়, সেটিই প্রথম বাক্য (Topic Sentence)।</p>
  <p><strong>২. Pronoun Reference লক্ষ করুন:</strong> "He, She, They, It, This, These" — এই pronounগুলো আগের বাক্যে কোনো Noun-এর পরে আসে। Pronoun থাকলে বাক্যটি কখনো প্রথম হবে না।</p>
  <p><strong>৩. Time Connectives খুঁজুন:</strong> "First, Then, After that, Finally, Next, Later" — এগুলো বাক্যের ক্রম নির্ধারণ করতে সাহায্য করে।</p>
  <p><strong>৪. Concluding Sentence চিহ্নিত করুন:</strong> "Therefore, Thus, In conclusion, Finally, As a result" দিয়ে শুরু হওয়া বাক্য সাধারণত শেষে আসে।</p>
  <p><strong>৫. Linking Words লক্ষ করুন:</strong> "However, Moreover, Furthermore, On the other hand" — এই Linking Words দিয়ে বাক্যের logical flow বোঝা যায়।</p>
  <p><strong>৬. উত্তর লেখার ফরম্যাট:</strong> সাজানো বাক্যগুলো ক্রম অনুযায়ী সম্পূর্ণভাবে লিখুন। শুধু অক্ষর দিলে অনেক ক্ষেত্রে নম্বর পাওয়া যায় না।</p>

  <h2 class="htbd-academic-heading" id="grammar-tips">৪. Connectives ও Coherence-এর গুরুত্বপূর্ণ নিয়ম (Key Grammar Tips)</h2>

  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 22px 0;">
    <table class="htbd-academic-table">
      <thead>
        <tr><th>Connective Type</th><th>উদাহরণ (Examples)</th><th>ব্যবহার</th></tr>
      </thead>
      <tbody>
        <tr><td>Addition</td><td>and, also, moreover, furthermore, besides</td><td>দুটি বক্তব্য যোগ করতে</td></tr>
        <tr><td>Contrast</td><td>but, however, although, yet, on the other hand</td><td>বিপরীত বক্তব্যে</td></tr>
        <tr><td>Cause &amp; Effect</td><td>because, so, therefore, as a result, thus</td><td>কারণ ও ফলাফল বোঝাতে</td></tr>
        <tr><td>Time Sequence</td><td>first, then, after that, next, finally, later</td><td>ঘটনার ক্রম বোঝাতে</td></tr>
        <tr><td>Purpose</td><td>in order to, so that, to, for the purpose of</td><td>উদ্দেশ্য বোঝাতে</td></tr>
      </tbody>
    </table>
  </div>

  <h2 class="htbd-academic-heading" id="model-answers">৫. নমুনা সমাধান: Matching ও Re-arranging (Model Answers)</h2>
  
  <h3 class="htbd-academic-subheading">প্রশ্ন ৬: Sentence Matching Table নমুনা এক্সারসাইজ ও সমাধান</h3>
  <p>নিচে একটি বোর্ড স্ট্যান্ডার্ড Sentence Matching Table এবং তার পূর্ণাঙ্গ সঠিক উত্তর দেওয়া হলো:</p>
  
  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 20px 0;">
    <table class="htbd-academic-table">
      <thead>
        <tr><th>Column A</th><th>Column B</th><th>Column C</th></tr>
      </thead>
      <tbody>
        <tr><td>(a) Education</td><td>(i) ennobles</td><td>(i) darkness of ignorance.</td></tr>
        <tr><td>(b) It</td><td>(ii) is the process</td><td>(ii) our mind and refines our sensibilities.</td></tr>
        <tr><td>(c) An educated person</td><td>(iii) dispels the</td><td>(iii) of developing our body, mind and soul.</td></tr>
        <tr><td>(d) It also</td><td>(iv) can play a</td><td>(iv) vital role in removing social evils.</td></tr>
        <tr><td>(e) Proper education</td><td>(v) enables a person</td><td>(v) to distinguish between right and wrong.</td></tr>
      </tbody>
    </table>
  </div>

  <p><strong>সঠিক উত্তর (পূর্ণ বাক্যে সমাধান):</strong></p>
  <ul style="line-height: 1.85; color: #1e293b;">
    <li>(a + ii + iii): Education is the process of developing our body, mind and soul.</li>
    <li>(b + iii + i): It dispels the darkness of ignorance.</li>
    <li>(c + iv + iv): An educated person can play a vital role in removing social evils.</li>
    <li>(d + i + ii): It also ennobles our mind and refines our sensibilities.</li>
    <li>(e + v + v): Proper education enables a person to distinguish between right and wrong.</li>
  </ul>

  <h3 class="htbd-academic-subheading">প্রশ্ন ৭: Re-arranging Sentences নমুনা (Sample Re-arranging)</h3>
  <p><strong>এলোমেলো বাক্যসমূহ:</strong></p>
  <p style="background:#f8fafc; border-left:4px solid #94a3b8; padding:14px 18px; border-radius:6px; font-size:16px; line-height:1.9;">
  (a) He also exercises every morning to stay healthy.<br>
  (b) Finally, he goes to bed early at night.<br>
  (c) Rahim is a very disciplined student.<br>
  (d) After school, he helps his mother in household chores.<br>
  (e) He wakes up early in the morning and studies for two hours.<br>
  (f) Then he has breakfast and goes to school on time.<br>
  (g) In the afternoon, he revises his lessons.<br>
  (h) Because of his good habits, he always gets good results.
  </p>
  <p><strong>সঠিক ক্রম (Correct Order):</strong> c → e → a → f → d → g → h → b</p>
  <p style="background:#f0fdf4; border:1px solid #bbf7d0; padding:14px 18px; border-radius:8px; color:#14532d; font-size:16.5px; line-height:1.85;">
  Rahim is a very disciplined student. He wakes up early in the morning and studies for two hours. He also exercises every morning to stay healthy. Then he has breakfast and goes to school on time. After school, he helps his mother in household chores. In the afternoon, he revises his lessons. Because of his good habits, he always gets good results. Finally, he goes to bed early at night.
  </p>

  <h2 class="htbd-academic-heading" id="top-rearrange">৬. ২০২৭ সালের সম্ভাব্য ৫টি বহুল কমন রি-অ্যারেঞ্জ গল্প ও জীবনী (Top Rearrange Topics)</h2>
  <p>এসএসসি ও দাখিল পরীক্ষায় প্রতি বছর বিখ্যাত ঐতিহাসিক ব্যক্তিত্ব বা নীতিকথামূলক গল্প থেকে রি-অ্যারেঞ্জ আসে। ২০২৭ সালের জন্য সর্বাধিক গুরুত্বপূর্ণ ৫টি গল্প হলো:</p>
  <ol style="line-height: 1.85; color: #1e293b;">
    <li><strong>King Lear and His Three Daughters:</strong> রাজা লিয়ারের অহংকার, তিন কন্যার চাটুকারিতা বনাম কর্ডেলিয়ার সত্যবাদিতা এবং শেষ জীবনের করুণ পরিণতি।</li>
    <li><strong>Robert Bruce and the Spider:</strong> স্কটল্যান্ডের রাজা রবার্ট ব্রুসের পরাজয়, গুহায় মাকড়সার জাল বোনার অধ্যবসায় দেখে পুনরুদ্যমে যুদ্ধে জয়লাভ।</li>
    <li><strong>Sheikh Saadi and His Noble Dress:</strong> পোশাক দেখে মানুষকে বিচার করার ভুল ধারণা ও বিখ্যাত নীতিশিক্ষা—"পোশাক নয়, গুণই মানুষের আসল পরিচয়"।</li>
    <li><strong>Bayazid Bostami's Devotion to His Mother:</strong> গভীর রাতে অসুস্থ মায়ের জন্য পানি নিয়ে সারারাত দাঁড়িয়ে থাকার অনন্য মাতৃভক্তির নিদর্শন।</li>
    <li><strong>Nelson Mandela and the Anti-Apartheid Movement:</strong> দক্ষিণ আফ্রিকার বর্ণবাদ বিরোধী সংগ্রাম, ২৭ বছরের কারাবরণ ও শান্তি প্রতিষ্ঠার ঐতিহাসিক জীবনী।</li>
  </ol>

  <h2 class="htbd-academic-heading" id="box-technique">৭. রি-অ্যারেঞ্জে পূর্ণ ৮ নম্বর পাওয়ার বক্স কৌশল (The Sequence Box Technique)</h2>
  <p>পরীক্ষকের খাতা মূল্যায়নের সুবিধার জন্য বোর্ড স্ট্যান্ডার্ড অনুযায়ী প্রথমে একটি ক্রমিক বক্স (Sequence Table) অঙ্কন করা অত্যন্ত জরুরি:</p>
  
  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 18px 0;">
    <table class="htbd-academic-table" style="text-align: center;">
      <thead>
        <tr><th>১</th><th>২</th><th>৩</th><th>৪</th><th>৫</th><th>৬</th><th>৭</th><th>৮</th></tr>
      </thead>
      <tbody>
        <tr><td>c</td><td>e</td><td>a</td><td>f</td><td>d</td><td>g</td><td>h</td><td>b</td></tr>
      </tbody>
    </table>
  </div>
  <p>বক্স তৈরির পর তার নিচে অবশ্যই সম্পূর্ণ বাক্যগুলো ক্রমানুসারে একটি সুন্দর প্যারাগ্রাফ আকারে লিখে দিতে হবে। এতে কোনো পরীক্ষক নম্বর কাটার সুযোগ পাবেন না।</p>

  <h2 class="htbd-academic-heading" id="faq">৮. সচরাচর জিজ্ঞাসা (Frequently Asked Questions — FAQ)</h2>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">Question 1: Q7-এ কি সম্পূর্ণ বাক্য লিখতে হবে নাকি শুধু বক্স আঁকলে চলবে? (Must I write full sentences in Q7?)</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">উত্তর: বোর্ডের নিয়ম অনুযায়ী প্রথমে বক্স আকারে ক্রম (Sequence Box) দেখাতে হবে এবং তার নিচে সম্পূর্ণ বাক্যগুলো প্যারাগ্রাফ আকারে সাজিয়ে লিখতে হবে। শুধু বক্স বা ক্রম লিখলে কিছু পরীক্ষক অর্ধেক নম্বর কেটে দিতে পারেন।</p>
  </div>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">Question 2: Matching Table-এ একই Option দুইবার ব্যবহার করা যাবে কি? (Can I use the same option twice in Q6?)</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">উত্তর: না, Sentence Matching Table-এ প্রতিটি Option শুধুমাত্র একবারই ব্যবহার করা যাবে। প্রতিটি বাক্যের জন্য আলাদা আলাদা অর্থপূর্ণ অংশ মেলাতে হবে।</p>
  </div>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">Question 3: রি-অ্যারেঞ্জ ক্রমানুসারে মেলানোর সবচেয়ে সহজ ট্রিকস কী? (What is the best trick to solve Re-arrange?)</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">উত্তর: প্রথমে গল্পের মূল চরিত্র বা সূচনা বাক্য (Introduction) খুঁজুন। এরপর ঘটনার কালানুক্রমিক ধারাবাহিকতা (Time sequence: born, youth, struggle, victory, death) সাজান। সর্বশেষে কনক্লুডিং সেন্টেন্স বা নীতিশিক্ষা বসান।</p>
  </div>

  {series_nav}

</div>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "mainEntityOfPage": {{"@type": "WebPage", "@id": "{url}"}},
  "headline": "{title}",
  "description": "{meta_desc}",
  "image": "{banner_url}",
  "author": {{"@type": "Person", "name": "Faruk Sir", "url": "https://www.helptrickbd.com/p/about-us.html"}},
  "publisher": {{"@type": "Organization", "name": "HelpTrickBD", "logo": {{"@type": "ImageObject", "url": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/logo.png"}}}},
  "datePublished": "2026-09-17T01:00:00+06:00"
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{"@type": "Question", "name": "Must I write full sentences in SSC English Re-arranging Q7?", "acceptedAnswer": {{"@type": "Answer", "text": "Yes, you should provide both the sequence box (1 to 8) and write out the full sentences in correct paragraph order to secure full marks."}}}},
    {{"@type": "Question", "name": "Can I use the same option twice in Sentence Matching Table Q6?", "acceptedAnswer": {{"@type": "Answer", "text": "No, each option across columns A, B, and C can only be used once to form 5 unique grammatically correct sentences."}}}},
    {{"@type": "Question", "name": "What is the best strategy to solve SSC English Re-arrange quickly?", "acceptedAnswer": {{"@type": "Answer", "text": "Find the introductory topic sentence introducing the person or setting, then follow chronological time markers and pronouns, finishing with the moral or concluding sentence."}}}}
  ]
}}
</script>
"""
    meta = {"title": title, "slug": slug, "custom_url": url, "url": url, "labels": LABELS, "search_description": meta_desc, "meta_description": meta_desc}
    return slug, html, meta


# ─────────────────────────────────────────────────────────────────────────────
# POST 04: POEMS & STORIES Q/A (Q 8-9)
# ─────────────────────────────────────────────────────────────────────────────
def generate_post_04():
    slug = "ssc-2027-english-poems-stories-question"
    title = "এসএসসি ২০২৭ কবিতা ও গল্প প্রশ্নোত্তর সম্পূর্ণ গাইড (SSC 2027 English Poems and Stories Question Answer Model Notes Q8 & Q9)"
    meta_desc = "SSC 2027 English 1st Paper কবিতা (Q8) ও গল্প (Q9) প্রশ্নোত্তর সাজেশন। গুরুত্বপূর্ণ কবিতা ও গল্পের তালিকা, মডেল উত্তর ও ২০ নম্বরের হ্যান্ডনোট।"
    banner_url = f"{CDN_BASE}/ssc_2027_silo_04_poems_stories.webp"
    banner_alt = "SSC 2027 English Poems and Stories Question Answer Guide"
    url = f"{BLOG_BASE}/{slug}.html"
    series_nav = get_series_nav("Part 04")

    html = get_css_block() + f"""
<div class="htbd-academic-container">

  <figure style="margin: 0 0 20px 0;">
    <img class="htbd-hero-img" src="{banner_url}" alt="{banner_alt}" title="{banner_alt}" width="1200" height="675" loading="eager" />
    <figcaption style="font-size: 14px; color: #64748b; text-align: center; margin-top: 6px;">SSC 2027 English Poems & Stories — Part 04 of the Study Silo Series</figcaption>
  </figure>

  <div class="htbd-overview-box">
    <p>এসএসসি ২০২৭ ইংরেজি ১ম পত্রে <strong>প্রশ্ন ৮</strong> (কবিতা থেকে প্রশ্নোত্তর) ও <strong>প্রশ্ন ৯</strong> (গল্প থেকে প্রশ্নোত্তর) থেকে মোট <strong>২০ নম্বর</strong> আসে। প্রতিটি প্রশ্নে ৮টির মধ্যে ৫টির উত্তর দিতে হয়। EFT বইয়ের কবিতা ও গল্পগুলো ভালোভাবে পড়লে এই ২০ নম্বরে নিশ্চিত পূর্ণ নম্বর পাওয়া সম্ভব। (Q8 from Poems and Q9 from Stories — 20 marks in total, answer any 5 out of 8 each.)</p>
  </div>

<!--more-->

  <div class="htbd-toc-card">
    <p class="toc-title">বিষয়সূচি (Table of Contents)</p>
    <ul>
      <li><a href="#marks-table">১. নম্বর বণ্টন ও প্রশ্নের ধরন</a></li>
      <li><a href="#poem-list">২. গুরুত্বপূর্ণ কবিতা তালিকা (Important Poems for Q8)</a></li>
      <li><a href="#story-list">৩. গুরুত্বপূর্ণ গল্প তালিকা (Important Stories for Q9)</a></li>
      <li><a href="#answer-tips">৪. কবিতা ও গল্পের উত্তর লেখার কৌশল</a></li>
      <li><a href="#model-answers">৫. নমুনা প্রশ্নোত্তর: কবিতা ও গল্প (Model Q/A)</a></li>
      <li><a href="#board-formulas">৬. কবিতা ও গল্পের উত্তরে পূর্ণ ১০/১০ পাওয়ার ৫টি ফর্মুলা</a></li>
      <li><a href="#literary-devices">৭. কবিতার গুরুত্বপূর্ণ Literary Devices ও উদাহরণ</a></li>
      <li><a href="#faq">৮. সচরাচর জিজ্ঞাসা (FAQ)</a></li>
    </ul>
  </div>

  <h2 class="htbd-academic-heading" id="marks-table">১. নম্বর বণ্টন (Marks Distribution — Q8 & Q9)</h2>
  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 24px 0;">
    <table class="htbd-academic-table">
      <thead>
        <tr><th>প্রশ্ন</th><th>উৎস</th><th>নির্দেশনা</th><th>নম্বর</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>Q8</strong></td><td>EFT পাঠ্যবইয়ের কবিতা (Poems)</td><td>৮টির মধ্যে যেকোনো ৫টির উত্তর দিতে হবে</td><td><strong>2 × 5 = 10</strong></td></tr>
        <tr><td><strong>Q9</strong></td><td>EFT পাঠ্যবইয়ের গল্প (Stories)</td><td>৮টির মধ্যে যেকোনো ৫টির উত্তর দিতে হবে</td><td><strong>2 × 5 = 10</strong></td></tr>
        <tr><td colspan="3" style="text-align:right; font-weight:700; background:#f1f5f9;">মোট:</td><td style="font-weight:700; background:#f1f5f9; color:#0c2340;"><strong>20</strong></td></tr>
      </tbody>
    </table>
  </div>

  <div class="htbd-tip-box">
    <p><strong>গুরুত্বপূর্ণ পরামর্শ:</strong> Q8 ও Q9-এ ৮টির মধ্যে ৫টির উত্তর দিতে হয়। তাই যে ৫টি প্রশ্নের উত্তর ভালো জানেন, সেগুলো বেছে নিন। ৫টির বেশি উত্তর দিলে প্রথম ৫টিই নম্বরের জন্য গণনা হবে।</p>
  </div>

  <h2 class="htbd-academic-heading" id="poem-list">২. গুরুত্বপূর্ণ কবিতা তালিকা (Important Poems for SSC 2027 Q8)</h2>
  <p>EFT বইয়ের নিচের কবিতাগুলো SSC 2027-এর Q8-এ আসার সম্ভাবনা সবচেয়ে বেশি। প্রতিটি কবিতার বিষয়বস্তু, কবির নাম এবং মূল বার্তা জানা থাকলে সহজেই উত্তর দেওয়া যাবে।</p>

  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 22px 0;">
    <table class="htbd-academic-table">
      <thead>
        <tr><th>কবিতার নাম</th><th>কবির নাম</th><th>মূল বিষয়</th><th>গুরুত্ব</th></tr>
      </thead>
      <tbody>
        <tr><td>The Solitary Reaper</td><td>William Wordsworth</td><td>একাকী কৃষক বালিকার গান</td><td>অত্যন্ত গুরুত্বপূর্ণ</td></tr>
        <tr><td>O Captain! My Captain!</td><td>Walt Whitman</td><td>আব্রাহাম লিংকনের প্রতি শোকগাথা</td><td>অত্যন্ত গুরুত্বপূর্ণ</td></tr>
        <tr><td>Daffodils (I Wandered Lonely as a Cloud)</td><td>William Wordsworth</td><td>প্রকৃতির সৌন্দর্য ও আনন্দ</td><td>গুরুত্বপূর্ণ</td></tr>
        <tr><td>The Road Not Taken</td><td>Robert Frost</td><td>জীবনে সিদ্ধান্ত গ্রহণ</td><td>গুরুত্বপূর্ণ</td></tr>
        <tr><td>Stopping by Woods on a Snowy Evening</td><td>Robert Frost</td><td>কর্তব্যবোধ ও জীবনের দায়িত্ব</td><td>গুরুত্বপূর্ণ</td></tr>
        <tr><td>If —</td><td>Rudyard Kipling</td><td>সাফল্যের গুণাবলি ও আদর্শ মানুষ</td><td>গুরুত্বপূর্ণ</td></tr>
        <tr><td>The Tiger</td><td>William Blake</td><td>সৃষ্টিকর্তার শক্তি ও বাঘের ভয়াবহতা</td><td>মাঝারি গুরুত্বপূর্ণ</td></tr>
        <tr><td>Sonnet 18 (Shall I compare thee)</td><td>William Shakespeare</td><td>প্রেম ও সৌন্দর্যের অমরত্ব</td><td>মাঝারি গুরুত্বপূর্ণ</td></tr>
      </tbody>
    </table>
  </div>

  <h2 class="htbd-academic-heading" id="story-list">৩. গুরুত্বপূর্ণ গল্প তালিকা (Important Stories for SSC 2027 Q9)</h2>
  <p>EFT বইয়ের নিচের গল্পগুলো Q9-এ আসার সম্ভাবনা সবচেয়ে বেশি। প্রতিটি গল্পের চরিত্র, ঘটনাপ্রবাহ ও নৈতিক শিক্ষা (Moral) জানা থাকলে সহজেই উত্তর দেওয়া যাবে।</p>

  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 22px 0;">
    <table class="htbd-academic-table">
      <thead>
        <tr><th>গল্পের নাম</th><th>লেখকের নাম</th><th>মূল বিষয়</th><th>গুরুত্ব</th></tr>
      </thead>
      <tbody>
        <tr><td>The Gift of the Magi</td><td>O. Henry</td><td>প্রেম ও আত্মত্যাগ</td><td>অত্যন্ত গুরুত্বপূর্ণ</td></tr>
        <tr><td>The Necklace</td><td>Guy de Maupassant</td><td>লোভ ও জীবনের বাস্তবতা</td><td>অত্যন্ত গুরুত্বপূর্ণ</td></tr>
        <tr><td>The Last Leaf</td><td>O. Henry</td><td>আশা, বন্ধুত্ব ও আত্মত্যাগ</td><td>গুরুত্বপূর্ণ</td></tr>
        <tr><td>The Happy Prince</td><td>Oscar Wilde</td><td>পরোপকার ও ভালোবাসা</td><td>গুরুত্বপূর্ণ</td></tr>
        <tr><td>The Old Man and the Sea (excerpt)</td><td>Ernest Hemingway</td><td>সংগ্রাম ও অধ্যবসায়</td><td>গুরুত্বপূর্ণ</td></tr>
        <tr><td>The Selfish Giant</td><td>Oscar Wilde</td><td>স্বার্থপরতা ও ক্ষমা</td><td>মাঝারি গুরুত্বপূর্ণ</td></tr>
      </tbody>
    </table>
  </div>

  <h2 class="htbd-academic-heading" id="answer-tips">৪. কবিতা ও গল্পের উত্তর লেখার কৌশল (Answer Writing Tips for Q8 & Q9)</h2>

  <h3 class="htbd-academic-subheading">কবিতার উত্তর লেখার নিয়ম (How to Answer Poem Questions)</h3>
  <p><strong>১. কবিতার বিষয়বস্তু জানুন:</strong> প্রতিটি কবিতার Central Theme, Imagery এবং কবির মূল বক্তব্য বুঝুন।</p>
  <p><strong>২. কবির নাম ও Background:</strong> কবির সম্পর্কে সংক্ষিপ্ত পরিচয় জানুন — এটি উত্তরে অতিরিক্ত তথ্য যোগ করতে সাহায্য করে।</p>
  <p><strong>৩. Literary Devices চিহ্নিত করুন:</strong> Simile, Metaphor, Personification, Alliteration — এগুলো কবিতার প্রশ্নে প্রায়ই জিজ্ঞাসা করা হয়।</p>
  <p><strong>৪. সম্পূর্ণ বাক্যে উত্তর:</strong> কবিতার লাইন উদ্ধৃত করতে হলে Quotation Mark (" ") ব্যবহার করুন।</p>

  <h3 class="htbd-academic-subheading">গল্পের উত্তর লেখার নিয়ম (How to Answer Story Questions)</h3>
  <p><strong>১. Character ও Plot জানুন:</strong> প্রধান চরিত্র, তাদের সম্পর্ক এবং গল্পের ঘটনাপ্রবাহ মনে রাখুন।</p>
  <p><strong>২. Moral বা Theme:</strong> গল্পের শেষে কী শিক্ষা পাওয়া যায় (Moral/Theme) — এটি প্রায়ই জিজ্ঞাসা করা হয়।</p>
  <p><strong>৩. নিজের ভাষায় লিখুন:</strong> গল্প থেকে সরাসরি কপি না করে নিজের ভাষায় প্যারাফ্রেজ করুন।</p>
  <p><strong>৪. প্রাসঙ্গিক উদ্ধৃতি:</strong> উত্তরে গল্প থেকে প্রাসঙ্গিক দৃষ্টান্ত উল্লেখ করলে নম্বর বাড়ে।</p>

  <h2 class="htbd-academic-heading" id="model-answers">৫. নমুনা প্রশ্নোত্তর: কবিতা ও গল্প (Model Q/A for Poems &amp; Stories)</h2>
  
  <h3 class="htbd-academic-subheading">কবিতার নমুনা উত্তর ০১ — "The Road Not Taken" (Robert Frost)</h3>
  <p><strong>Q: What is the central theme of the poem "The Road Not Taken"?</strong></p>
  <p style="background:#f0fdf4; border:1px solid #bbf7d0; padding:14px 18px; border-radius:8px; color:#14532d; font-size:16.5px; line-height:1.85;"><strong>Model Answer:</strong> The central theme of Robert Frost's poem "The Road Not Taken" is the significance of individual choices in life. The speaker comes to a fork in the road and must choose one path. The poem suggests that every choice we make in life shapes our future. The speaker chose the less-traveled road, representing unconventional choices. The poem teaches us that we must take responsibility for our decisions and accept the outcomes with dignity.</p>

  <h3 class="htbd-academic-subheading">কবিতার নমুনা উত্তর ০২ — "I Wandered Lonely as a Cloud" (William Wordsworth)</h3>
  <p><strong>Q: How does nature bring joy to the poet in "Daffodils"?</strong></p>
  <p style="background:#f0fdf4; border:1px solid #bbf7d0; padding:14px 18px; border-radius:8px; color:#14532d; font-size:16.5px; line-height:1.85;"><strong>Model Answer:</strong> In Wordsworth's celebrated poem, nature serves as a boundless reservoir of permanent joy and spiritual rejuvenation. When the poet first witnesses the golden daffodils dancing in the gentle breeze beside the lake, he feels an overwhelming sense of delight. More importantly, when he rests on his couch in vacant or pensive mood, the memory of those fluttering blossoms flashes upon his "inward eye" and fills his heart with serene pleasure.</p>

  <h3 class="htbd-academic-subheading">গল্পের নমুনা উত্তর ০১ — "The Gift of the Magi" (O. Henry)</h3>
  <p><strong>Q: What is the moral of the story "The Gift of the Magi"?</strong></p>
  <p style="background:#f0fdf4; border:1px solid #bbf7d0; padding:14px 18px; border-radius:8px; color:#14532d; font-size:16.5px; line-height:1.85;"><strong>Model Answer:</strong> The moral of "The Gift of the Magi" by O. Henry is that true love and selfless sacrifice are the greatest gifts one can give. Della sold her beautiful hair and Jim sold his watch to buy gifts for each other. Although the gifts became useless, the story shows that the spirit of giving and love matters more than material possessions. Selfless love always triumphs over poverty and difficulty.</p>

  <h3 class="htbd-academic-subheading">গল্পের নমুনা উত্তর ০২ — "The Necklace" (Guy de Maupassant)</h3>
  <p><strong>Q: What fatal mistake did Mathilde Loisel make, and what does it teach us?</strong></p>
  <p style="background:#f0fdf4; border:1px solid #bbf7d0; padding:14px 18px; border-radius:8px; color:#14532d; font-size:16.5px; line-height:1.85;"><strong>Model Answer:</strong> Mathilde Loisel's fatal mistake was her overwhelming vanity, false pride, and dishonesty in not admitting the loss of the borrowed necklace immediately to Madame Forestier. Instead, she spent ten grueling years in grinding poverty to replace an imitation necklace worth merely 500 francs. The story teaches us that uncontrolled discontentment and deceptive appearance can ruin an entire lifetime.</p>

  <h2 class="htbd-academic-heading" id="board-formulas">৬. কবিতা ও গল্পের উত্তরে পূর্ণ ১০/১০ পাওয়ার ৫টি ফর্মুলা</h2>
  <p>বোর্ড খাতা মূল্যায়নের অভিজ্ঞতা অনুযায়ী পরীক্ষার্থীরা নিচের ৫টি নিয়ম মেনে উত্তর সাজালে সর্বোচ্চ নম্বর পেয়ে থাকে:</p>
  <ul style="line-height: 1.85; color: #1e293b;">
    <li><strong>কবির নাম ও লেখার প্রেক্ষিত উল্লেখ:</strong> উত্তরের প্রারম্ভিক বাক্যে প্রাসঙ্গিকভাবে কবির নাম উল্লেখ করুন (যেমন: "In William Wordsworth's romantic masterpiece 'Daffodils', the poet portrays...").</li>
    <li><strong>সরাসরি প্রশ্নের জবাব দেওয়া:</strong> অপ্রাসঙ্গিক ভূমিকা এড়িয়ে প্রশ্নপত্রে ঠিক যা জানতে চাওয়া হয়েছে প্রথম বাক্যে তার মূল জবাবটি দিন।</li>
    <li><strong>যথাযথ Quotation ব্যবহার:</strong> কবিতার প্রশ্নের ক্ষেত্রে মূল কবিতা থেকে এক বা দুটি সংক্ষিপ্ত লাইন উদ্ধৃত করলে উত্তরের গ্রহণযোগ্যতা বহুলাংশে বৃদ্ধি পায়।</li>
    <li><strong>ব্যাকরণ ও টেন্সের সমতা রক্ষা:</strong> প্রশ্নটি যদি Present Tense-এ থাকে তবে উত্তর Present Tense-এ এবং Past Tense-এ থাকলে Past Tense-এ লিখুন।</li>
    <li><strong>শব্দসীমা বজায় রাখা:</strong> প্রতিটি ২ নম্বরের প্রশ্নের উত্তরের জন্য ৩০ থেকে ৫০ শব্দ (২-৩টি পরিপূর্ণ বাক্য) লেখাই আদর্শ মান।</li>
  </ul>

  <h2 class="htbd-academic-heading" id="literary-devices">৭. কবিতার গুরুত্বপূর্ণ Literary Devices ও উদাহরণ</h2>
  <p>কবিতা সংক্রান্ত প্রশ্নে প্রায়ই বিভিন্ন আলংকারিক কৌশল সম্পর্কে জানতে চাওয়া হয়। নিচের তিনটি বহুল ব্যবহৃত কৌশল মুখস্থ রাখুন:</p>
  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 20px 0;">
    <table class="htbd-academic-table">
      <thead>
        <tr><th>কৌশল (Device)</th><th>সংজ্ঞা</th><th>কবিতার বাস্তব উদাহরণ</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>Simile (উপমা)</strong></td><td>'as' বা 'like' দিয়ে দুটি ভিন্ন বিষয়ের তুলনা।</td><td>"I wandered lonely <em>as a cloud</em>"</td></tr>
        <tr><td><strong>Metaphor (রূপক)</strong></td><td>সরাসরি এক বস্তুকে অন্য বস্তুর সাথে তুলনা (as/like ছাড়া)।</td><td>"Life is a broken-winged bird"</td></tr>
        <tr><td><strong>Personification (ব্যক্তিত্বারোপ)</strong></td><td>অচেতন বা জড় বস্তুকে মানুষের মতো আচরণ দেওয়া।</td><td>"Tossing their heads in sprightly dance"</td></tr>
      </tbody>
    </table>
  </div>

  <h2 class="htbd-academic-heading" id="faq">৮. সচরাচর জিজ্ঞাসা (Frequently Asked Questions — FAQ)</h2>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">Question 1: Q8 ও Q9-এ কি কবিতা ও গল্পের বাইরে থেকে প্রশ্ন আসতে পারে? (Can Q8 &amp; Q9 come from outside the EFT textbook?)</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">উত্তর: না, SSC ও দাখিল পরীক্ষায় Q8 (কবিতা) ও Q9 (গল্প) সবসময় EFT পাঠ্যবইয়ের নির্ধারিত পাঠ্যসূচি থেকেই আসে। পাঠ্যবইয়ের বাইরে থেকে কোনো প্রশ্ন তৈরি করা হয় না।</p>
  </div>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">Question 2: ৮টির মধ্যে ৫টির বেশি উত্তর দিলে কি অতিরিক্ত নম্বর পাওয়া যাবে? (What if I answer more than 5 out of 8?)</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">উত্তর: না, কোনো অতিরিক্ত নম্বর দেওয়া হয় না। পরীক্ষক সবসময় প্রথম ৫টি উত্তরই মূল্যায়ন করেন। তাই সবচেয়ে নির্ভুল ও নিশ্চিত জানা ৫টি প্রশ্ন বেছে নিয়ে উত্তর লিখুন।</p>
  </div>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">Question 3: কবিতার উত্তরে কি কবির নাম লেখা বাধ্যতামূলক? (Is mentioning the poet's name mandatory?)</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">উত্তর: সরাসরি বাধ্যতামূলক না হলেও কবির নাম সুন্দরভাবে উত্তরের শুরুতে যুক্ত করলে পরীক্ষকের কাছে উত্তরের মান অত্যন্ত প্রফেশনাল মনে হয় এবং পূর্ণ ২ নম্বর নিশ্চিত হয়।</p>
  </div>

  {series_nav}

</div>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "mainEntityOfPage": {{"@type": "WebPage", "@id": "{url}"}},
  "headline": "{title}",
  "description": "{meta_desc}",
  "image": "{banner_url}",
  "author": {{"@type": "Person", "name": "Faruk Sir", "url": "https://www.helptrickbd.com/p/about-us.html"}},
  "publisher": {{"@type": "Organization", "name": "HelpTrickBD", "logo": {{"@type": "ImageObject", "url": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/logo.png"}}}},
  "datePublished": "2026-09-17T01:30:00+06:00"
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{"@type": "Question", "name": "Can questions in Q8 and Q9 come from outside the EFT textbook?", "acceptedAnswer": {{"@type": "Answer", "text": "No, all questions in Questions 8 and 9 are strictly selected from the official English For Today (EFT) textbook for SSC and Dakhil."}}}},
    {{"@type": "Question", "name": "What happens if a student answers more than 5 questions out of 8 in Q8 or Q9?", "acceptedAnswer": {{"@type": "Answer", "text": "Examiners evaluate only the first 5 answered questions in sequential order. Extra answers do not provide bonus marks."}}}},
    {{"@type": "Question", "name": "Is it recommended to mention the poet's or author's name in literature answers?", "acceptedAnswer": {{"@type": "Answer", "text": "Yes, properly mentioning the author's or poet's name gives the answer an academic tone and ensures full 2 marks per question."}}}}
  ]
}}
</script>
"""
    meta = {"title": title, "slug": slug, "custom_url": url, "url": url, "labels": LABELS, "search_description": meta_desc, "meta_description": meta_desc}
    return slug, html, meta


# ─────────────────────────────────────────────────────────────────────────────
# POST 05: COMPLETING STORY & DIALOGUE WRITING (Q 10-11)
# ─────────────────────────────────────────────────────────────────────────────
def generate_post_05():
    slug = "ssc-2027-english-completing-story"
    title = "এসএসসি ২০২৭ কমপ্লিটিং স্টোরি ও ডায়ালগ রাইটিং সাজেশন (SSC 2027 English Completing Story & Dialogue Writing Final Suggestion Q10 & Q11)"
    meta_desc = "SSC 2027 English Writing Part সাজেশন। Completing Story (Q10) ও Dialogue Writing (Q11) — ২৫ নম্বরের ফাইনাল মডেল উত্তর ও লেখার নিয়মাবলি।"
    banner_url = f"{CDN_BASE}/ssc_2027_silo_05_story_dialogue.webp"
    banner_alt = "SSC 2027 English Completing Story and Dialogue Writing Final Suggestion"
    url = f"{BLOG_BASE}/{slug}.html"
    series_nav = get_series_nav("Part 05")

    html = get_css_block() + f"""
<div class="htbd-academic-container">

  <figure style="margin: 0 0 20px 0;">
    <img class="htbd-hero-img" src="{banner_url}" alt="{banner_alt}" title="{banner_alt}" width="1200" height="675" loading="eager" />
    <figcaption style="font-size: 14px; color: #64748b; text-align: center; margin-top: 6px;">SSC 2027 Writing Part: Completing Story & Dialogue Writing — Part 05 of the Study Silo Series</figcaption>
  </figure>

  <div class="htbd-overview-box">
    <p>এসএসসি ২০২৭ ইংরেজি ১ম পত্রের Part B (Writing) অংশে <strong>প্রশ্ন ১০</strong> (Completing Story — ১৫ নম্বর) ও <strong>প্রশ্ন ১১</strong> (Dialogue Writing — ১৫ নম্বর) থেকে মোট <strong>৩০ নম্বর</strong> আসে। এটি সম্পূর্ণ পরীক্ষার ৩০%। সঠিক নিয়মে লিখলে এই ৩০ নম্বরে উচ্চ নম্বর পাওয়া সম্ভব। (Part B Writing carries 30 marks — 15 for Completing Story (Q10) and 15 for Dialogue Writing (Q11).)</p>
  </div>

<!--more-->

  <div class="htbd-toc-card">
    <p class="toc-title">বিষয়সূচি (Table of Contents)</p>
    <ul>
      <li><a href="#marks-table">১. নম্বর বণ্টন ও Writing Part-এর গুরুত্ব</a></li>
      <li><a href="#story-guide">২. প্রশ্ন ১০: Completing Story — সম্পূর্ণ নিয়মাবলি (Q10 Guide)</a></li>
      <li><a href="#story-elements">৩. ভালো গল্পের উপাদানসমূহ (Elements of a Good Story)</a></li>
      <li><a href="#dialogue-guide">৪. প্রশ্ন ১১: Dialogue Writing — সম্পূর্ণ নিয়মাবলি (Q11 Guide)</a></li>
      <li><a href="#model-story">৫. নমুনা গল্প (Model Completing Story)</a></li>
      <li><a href="#model-dialogue">৬. নমুনা ডায়ালগ (Model Dialogue Writing)</a></li>
      <li><a href="#faq">৭. সচরাচর জিজ্ঞাসা (FAQ)</a></li>
    </ul>
  </div>

  <h2 class="htbd-academic-heading" id="marks-table">১. নম্বর বণ্টন (Marks Distribution — Part B Writing)</h2>
  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 24px 0;">
    <table class="htbd-academic-table">
      <thead>
        <tr><th>প্রশ্ন</th><th>প্রশ্নের ধরন</th><th>নম্বর বণ্টন</th><th>মোট নম্বর</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>Q10</strong></td><td>Completing Story (গল্প সম্পন্ন করা)</td><td>Content (5) + Language (5) + Title &amp; Moral (5)</td><td><strong>15</strong></td></tr>
        <tr><td><strong>Q11</strong></td><td>Dialogue Writing (কথোপকথন লেখা)</td><td>Content (5) + Language (5) + Format (5)</td><td><strong>15</strong></td></tr>
        <tr><td colspan="3" style="text-align:right; font-weight:700; background:#f1f5f9;">মোট Part B:</td><td style="font-weight:700; background:#f1f5f9; color:#0c2340;"><strong>30</strong></td></tr>
      </tbody>
    </table>
  </div>

  <h2 class="htbd-academic-heading" id="story-guide">২. প্রশ্ন ১০: Completing Story — সম্পূর্ণ নিয়মাবলি (Q10 Completing Story Full Guide)</h2>
  <p>Q10-এ গল্পের শুরু (outline) দেওয়া থাকে — সেটি পড়ে গল্পটি সম্পন্ন করতে হয়। গল্পে অবশ্যই একটি Title ও শেষে একটি Moral (নৈতিক শিক্ষা) থাকতে হবে।</p>

  <h3 class="htbd-academic-subheading">Completing Story লেখার ধাপ (Step-by-Step Method)</h3>
  <p><strong>ধাপ ১ — Outline পড়ুন:</strong> দেওয়া outline মনোযোগ দিয়ে পড়ুন এবং গল্পের সম্ভাব্য দিক নির্ধারণ করুন।</p>
  <p><strong>ধাপ ২ — Title নির্বাচন করুন:</strong> গল্পের বিষয়বস্তু থেকে একটি সংক্ষিপ্ত, আকর্ষণীয় ও প্রাসঙ্গিক Title দিন।</p>
  <p><strong>ধাপ ৩ — Beginning:</strong> Outline-এর দেওয়া শুরুটি অবিকল লিখুন, এরপর গল্পের মূল ঘটনা শুরু করুন।</p>
  <p><strong>ধাপ ৪ — Rising Action:</strong> গল্পে সমস্যা বা দ্বন্দ্ব তৈরি করুন — এটিই গল্পকে আকর্ষণীয় করে।</p>
  <p><strong>ধাপ ৫ — Climax:</strong> সমস্যার সর্বোচ্চ বিন্দুতে পৌঁছান।</p>
  <p><strong>ধাপ ৬ — Resolution &amp; Moral:</strong> সমস্যার সমাধান করুন এবং শেষে Moral লিখুন।</p>

  <h2 class="htbd-academic-heading" id="story-elements">৩. ভালো গল্পের উপাদানসমূহ (Elements of a Good Story)</h2>
  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 22px 0;">
    <table class="htbd-academic-table">
      <thead>
        <tr><th>উপাদান (Element)</th><th>বিবরণ</th><th>উদাহরণ</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>Title (শিরোনাম)</strong></td><td>সংক্ষিপ্ত, আকর্ষণীয় ও প্রাসঙ্গিক</td><td>"The Honest Woodcutter", "A Friend in Need"</td></tr>
        <tr><td><strong>Setting (স্থান-কাল)</strong></td><td>গল্পের সময় ও স্থান উল্লেখ</td><td>"Once upon a time, in a small village..."</td></tr>
        <tr><td><strong>Characters (চরিত্র)</strong></td><td>প্রধান ও গৌণ চরিত্র পরিচয়</td><td>নাম, পরিচয় ও বৈশিষ্ট্য</td></tr>
        <tr><td><strong>Conflict (দ্বন্দ্ব)</strong></td><td>গল্পের মূল সমস্যা বা চ্যালেঞ্জ</td><td>প্রকৃতির সাথে, মানুষের সাথে বা নিজের সাথে</td></tr>
        <tr><td><strong>Climax (চরম মুহূর্ত)</strong></td><td>সমস্যার সর্বোচ্চ বিন্দু</td><td>সংকটের মুহূর্ত</td></tr>
        <tr><td><strong>Resolution (সমাধান)</strong></td><td>সমস্যার সমাধান</td><td>ইতিবাচক বা শিক্ষামূলক সমাপ্তি</td></tr>
        <tr><td><strong>Moral (নৈতিক শিক্ষা)</strong></td><td>গল্পের শেষে শিক্ষামূলক বার্তা</td><td>"Moral: Honesty is the best policy."</td></tr>
      </tbody>
    </table>
  </div>

  <div class="htbd-tip-box">
    <p><strong>পরামর্শ:</strong> গল্পে Paragraphing ব্যবহার করুন — শুরু, মাঝ ও শেষ আলাদা প্যারাগ্রাফে লিখুন। Moral সবসময় শেষ লাইনে আলাদাভাবে লিখুন: "Moral: ..."</p>
  </div>

  <h2 class="htbd-academic-heading" id="dialogue-guide">৪. প্রশ্ন ১১: Dialogue Writing — সম্পূর্ণ নির্দেশিকা (Q11 Dialogue Writing Full Guide)</h2>
  <p>Q11-এ দুটি চরিত্রের মধ্যে কথোপকথন (Dialogue) লিখতে হয়। একটি Topic দেওয়া থাকে এবং সেই বিষয়ে স্বাভাবিক, প্রাকৃতিক কথোপকথন লিখতে হয়।</p>

  <h3 class="htbd-academic-subheading">Dialogue Writing-এর নিয়মাবলি (Rules for Writing Dialogue)</h3>
  <p><strong>১. Format সঠিক রাখুন:</strong> প্রতিটি বক্তার নাম লেখার পর কোলন (:) দিন, তারপর Dialogue লিখুন।</p>
  <p><strong>২. Quotation Marks:</strong> Dialogue সবসময় Quotation Mark (" ")-এর মধ্যে লিখুন।</p>
  <p><strong>৩. স্বাভাবিক ভাষা:</strong> কথোপকথন স্বাভাবিক, Colloquial ভাষায় লিখুন — বইয়ের formal language নয়।</p>
  <p><strong>৪. দৈর্ঘ্য:</strong> সাধারণত ১০-১২টি exchange (উভয় দিক মিলিয়ে ২০-২৪ লাইন) লিখলে ভালো নম্বর পাওয়া যায়।</p>
  <p><strong>৫. Topic Relevance:</strong> Dialogue-এ দেওয়া Topic বা বিষয়ের সাথে প্রাসঙ্গিক তথ্য অন্তর্ভুক্ত করুন।</p>
  <p><strong>৬. Opening &amp; Closing:</strong> Greeting দিয়ে শুরু এবং বিদায় জানিয়ে শেষ করুন।</p>

  <h3 class="htbd-academic-subheading">গুরুত্বপূর্ণ Dialogue Topics (Important Topics for Q11)</h3>
  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 20px 0;">
    <table class="htbd-academic-table">
      <thead>
        <tr><th>ক্যাটাগরি</th><th>সম্ভাব্য Topic</th></tr>
      </thead>
      <tbody>
        <tr><td>শিক্ষা ও পড়াশোনা</td><td>Importance of Education, Exam Preparation, Future Career</td></tr>
        <tr><td>স্বাস্থ্য ও পরিবেশ</td><td>Tree Plantation, Environmental Pollution, Good Health Habits</td></tr>
        <tr><td>সামাজিক সচেতনতা</td><td>Early Marriage, Drug Abuse, Road Safety, Gender Equality</td></tr>
        <tr><td>প্রযুক্তি</td><td>Social Media, Internet Use, Mobile Phone Benefits &amp; Dangers</td></tr>
        <tr><td>দৈনন্দিন জীবন</td><td>Favourite Book, Hobby, Memorable Day, Future Plan</td></tr>
      </tbody>
    </table>
  </div>

  <h2 class="htbd-academic-heading" id="model-story">৫. নমুনা গল্প (Model Completing Story)</h2>
  <h3 class="htbd-academic-subheading">Outline: Once there was a thirsty crow. It was flying here and there in search of water...</h3>
  <p style="background:#f0fdf4; border:1px solid #bbf7d0; padding:18px 22px; border-radius:8px; color:#14532d; font-size:16.5px; line-height:1.9;">
  <strong>Title: The Clever Crow and the Pitcher</strong><br><br>
  Once there was a thirsty crow. It was flying here and there in search of water. After a long search, it found a pitcher with a little water at the bottom. The crow tried to drink the water, but its beak could not reach it.<br><br>
  The crow did not give up. It thought of a clever plan. It started dropping small stones one by one into the pitcher. As the stones were added, the water level began to rise slowly. The crow continued until the water rose close to the top of the pitcher.<br><br>
  Finally, the crow was able to drink the water and satisfy its thirst. It flew away happily, having solved the problem with its intelligence and patience.<br><br>
  <strong>Moral: Where there is a will, there is a way.</strong>
  </p>

  <h2 class="htbd-academic-heading" id="model-dialogue">৬. নমুনা ডায়ালগ (Model Dialogue Writing)</h2>
  <h3 class="htbd-academic-subheading">Topic: A dialogue between two friends about the importance of reading books</h3>
  <p style="background:#f0fdf4; border:1px solid #bbf7d0; padding:18px 22px; border-radius:8px; color:#14532d; font-size:16.5px; line-height:1.9;">
  <strong>Rahim:</strong> "Good morning, Karim! You seem to be reading a book. What book is that?"<br>
  <strong>Karim:</strong> "Good morning, Rahim! I'm reading 'The Diary of a Young Girl' by Anne Frank. It's a wonderful book."<br>
  <strong>Rahim:</strong> "That's great! But I find reading books boring. I prefer watching videos on YouTube."<br>
  <strong>Karim:</strong> "I understand, but books have something that videos can't give. They improve our imagination and language skills."<br>
  <strong>Rahim:</strong> "Really? Can you explain how reading helps?"<br>
  <strong>Karim:</strong> "Of course! Reading expands our vocabulary, sharpens our thinking, and reduces stress. It also helps us in exams."<br>
  <strong>Rahim:</strong> "I never thought of it that way. Which book do you suggest I start with?"<br>
  <strong>Karim:</strong> "Start with something light and interesting — maybe a story book or an adventure novel. Once you start, you'll enjoy it."<br>
  <strong>Rahim:</strong> "That sounds good. I'll try 'Robinson Crusoe'. Can you lend it to me?"<br>
  <strong>Karim:</strong> "Sure! I have it at home. I'll bring it tomorrow. Happy reading, Rahim!"<br>
  <strong>Rahim:</strong> "Thank you, Karim. See you tomorrow!"
  </p>

  <h2 class="htbd-academic-heading" id="faq">৭. সচরাচর জিজ্ঞাসা (FAQ)</h2>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">Question 1: Completing Story-তে কি Title বাধ্যতামূলক? (Is a Title mandatory in Completing Story?)</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">হ্যাঁ, Completing Story-তে Title দেওয়া বাধ্যতামূলক। Title ছাড়া গল্প লিখলে নম্বর কাটা যায়। Title সবসময় গল্পের আগে আন্ডারলাইন করে লিখুন।</p>
  </div>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">Question 2: Dialogue-এ কতগুলো exchange লিখতে হবে? (How many exchanges in Dialogue Writing?)</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">সাধারণত ১০-১২টি exchange (প্রতিটি চরিত্র ৫-৬ বার বলবে) লিখলে পূর্ণ নম্বর পাওয়া যায়। কম লিখলে Content নম্বর কমে যায়।</p>
  </div>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">Question 3: গল্পে Moral কোথায় লিখব? (Where should the Moral be written?)</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">Moral সবসময় গল্পের সবশেষে আলাদা লাইনে লিখতে হবে। Format: "Moral: [নৈতিক শিক্ষা]" — যেমন: "Moral: Honesty is the best policy."</p>
  </div>

  {series_nav}

</div>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "mainEntityOfPage": {{"@type": "WebPage", "@id": "{url}"}},
  "headline": "{title}",
  "description": "{meta_desc}",
  "image": "{banner_url}",
  "author": {{"@type": "Person", "name": "Faruk Sir"}},
  "publisher": {{"@type": "Organization", "name": "HelpTrickBD"}},
  "datePublished": "2026-09-17T02:00:00+06:00"
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{"@type": "Question", "name": "Is a Title mandatory in SSC English Completing Story?", "acceptedAnswer": {{"@type": "Answer", "text": "Yes, a Title is mandatory in Completing Story. Writing without a title will result in mark deductions. Always underline the title."}}}},
    {{"@type": "Question", "name": "Where should the Moral be written in Completing Story?", "acceptedAnswer": {{"@type": "Answer", "text": "The Moral should always be written at the very end of the story in a separate line: Moral: [moral lesson]."}}}}
  ]
}}
</script>
"""
    meta = {"title": title, "slug": slug, "custom_url": url, "url": url, "labels": LABELS, "search_description": meta_desc, "meta_description": meta_desc}
    return slug, html, meta


# ─────────────────────────────────────────────────────────────────────────────
# MAIN: Generate all 5 posts
# ─────────────────────────────────────────────────────────────────────────────
def main():
    generators = [
        ("silo_01_seen_passage", generate_post_01),
        ("silo_02_unseen_summary", generate_post_02),
        ("silo_03_matching_rearrange", generate_post_03),
        ("silo_04_poems_stories", generate_post_04),
        ("silo_05_story_dialogue", generate_post_05),
    ]

    print("=" * 70)
    print("SSC 2027 ENGLISH SILO SERIES — CONTENT GENERATOR")
    print("=" * 70)

    generated = []
    for file_prefix, gen_fn in generators:
        slug, html_content, metadata = gen_fn()
        html_path = os.path.join(RAW_POSTS_DIR, f"ssc_2027_{file_prefix}.html")
        meta_path = os.path.join(RAW_POSTS_DIR, f"ssc_2027_{file_prefix}.json")

        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)

        word_count = len(html_content.split())
        print(f"  [OK] {slug}")
        print(f"       HTML: {html_path} ({word_count} words)")
        print(f"       META: {meta_path}")
        generated.append({"slug": slug, "html_path": html_path, "meta_path": meta_path})

    print("\n" + "=" * 70)
    print(f"Generated {len(generated)} silo post files in: {RAW_POSTS_DIR}")
    print("=" * 70)
    return generated

if __name__ == "__main__":
    main()
