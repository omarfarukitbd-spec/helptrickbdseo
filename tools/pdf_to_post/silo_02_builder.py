#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/pdf_to_post/silo_02_builder.py
-------------------------------------
Generates Silo Post 02: Unseen Passage, Information Transfer (Q4) & Summary Writing (Q5).
Curriculum Architecture:
- Section 1: Marks Distribution & Focus (Q4: 5 marks, Q5: 10 marks = 15 marks)
- Section 2: 41 Unseen Topics Master Navigation Table (#unseen-index) with jump pills
- Section 3: 41 Comprehensive Solution Cards (#unseen-01 to #unseen-41)
             Each with: Passage Text, Question 4 Info Transfer Table & Answer Key,
             Question 5 Exam-Standard Model Summary (60-80 words), and Paraphrasing Tips.
- Section 4: Question 4 Information Transfer Column Tracking Guide
- Section 5: Question 5 Summary Writing 5 Golden Rules (10/10 scoring guide)
- Section 6: Board Exam & Model Test Analysis (Dakhil 2026: 26 March & Model: John Milton)
- Section 7: LSI Related Keywords & Target Searches
- Section 8: FAQ with Schema.org FAQPage JSON-LD
- Section 9: Helptrickbd Study Silo Series Navigation Widget
"""

import os
import sys
import json

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.pdf_to_post.data_ssc_2027_unseen_full import UNSEEN_TOPICS_FULL_41
from tools.pdf_to_post.data_ssc_2027_unseen import (
    MODEL_02_INDEPENDENCE_DAY as MODEL_02_26_MARCH,
    MODEL_03_JOHN_MILTON
)

BLOG_BASE = "https://www.helptrickbd.com/2026/09"
CDN_BASE = "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts"
LABELS = ["SSC Suggestion", "Education", "Dakhil Suggestion"]

def get_series_nav(current_part):
    posts = [
        ("পিলার হাব", "SSC English 1st Paper Suggestion 2027 (মাস্টার হাব ও মানবণ্টন)", f"{BLOG_BASE}/ssc-english-1st-paper-suggestion-2027.html"),
        ("Part 01", "SSC 2027 English Seen Passage Suggestion (সিন প্যাসেজ MCQ ও প্রশ্নোত্তর)", f"{BLOG_BASE}/ssc-2027-english-seen-passage-suggestion.html"),
        ("Part 02", "SSC 2027 English Unseen Passage & Summary Suggestion (আনসিন ও সামারি)", f"{BLOG_BASE}/ssc-2027-english-unseen-passage-summary.html"),
        ("Part 03", "SSC 2027 English Matching & Rearrange Suggestion (ম্যাচিং টেবিল ও রি-অ্যারেঞ্জ)", f"{BLOG_BASE}/ssc-2027-english-matching-rearrange.html"),
        ("Part 04", "SSC 2027 English Poems & Stories Suggestion (কবিতা ও গল্প প্রশ্নোত্তর)", f"{BLOG_BASE}/ssc-2027-english-poems-stories-question.html"),
        ("Part 05", "SSC 2027 English Completing Story & Dialogue Suggestion (স্টোরি ও ডায়ালগ)", f"{BLOG_BASE}/ssc-2027-english-completing-story.html"),
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

def render_info_table_html(table_data):
    th_cells = "".join([f"<th>{h}</th>" for h in table_data["headers"]])
    tr_rows = ""
    for row in table_data["rows"]:
        td_cells = "".join([f"<td>{c}</td>" for c in row])
        tr_rows += f"<tr>{td_cells}</tr>\n"
    return f"""<div style="overflow-x:auto; -webkit-overflow-scrolling:touch; margin:14px 0;">
      <table class="htbd-academic-table" style="margin:0; font-size:14.5px;">
        <thead><tr>{th_cells}</tr></thead>
        <tbody>{tr_rows}</tbody>
      </table>
    </div>"""

def render_answers_html(ans_dict):
    items = [f"<strong>({k})</strong> {v}" for k, v in ans_dict.items()]
    return " &nbsp;|&nbsp; ".join(items)

def build_post():
    slug = "ssc-2027-english-unseen-passage-summary"
    title = "SSC 2027 English Unseen Passage & Summary Suggestion | এসএসসি আনসিন প্যাসেজ ও সামারি রাইটিং"
    meta_desc = "SSC 2027 English Unseen Passage Suggestion। Information Transfer (Q4) ও Summary Writing (Q5) এর ৪১টি প্যাসেজ ও পূর্ণাঙ্গ মডেল সমাধান।"
    banner_url = f"{CDN_BASE}/ssc_2027_silo_02_unseen_summary.webp?v=2"
    banner_alt = "SSC 2027 English Unseen Passage Information Transfer and Summary Writing Suggestion"
    url = f"{BLOG_BASE}/{slug}.html"
    series_nav = get_series_nav("Part 02")

    # 1. Generate 41 Unseen Topics Master Index & Comprehensive Solution Cards
    unseen_index_rows = ""
    unseen_cards_html = ""

    for item in UNSEEN_TOPICS_FULL_41:
        u_id = item["slug_id"]
        star_color = "#b91c1c" if item["stars"] == "***" else ("#c2410c" if item["stars"] == "**" else "#4b5563")

        # Master Table Row
        unseen_index_rows += f"""<tr>
          <td style="text-align:center; font-weight:700;">{item['id']:02d}</td>
          <td style="text-align:center; font-weight:700; color:{star_color}; font-size:16px;">{item['stars']}</td>
          <td><a href="#{u_id}" style="color:#0369a1; font-weight:600; text-decoration:none;">{item['title']}</a><br><span style="font-size:13px; color:#64748b;">{item['bn_title']}</span></td>
          <td style="font-size:13.5px; color:#475569;">{item['theme']}</td>
          <td style="font-size:13px; color:#64748b;">{item['boards']}</td>
          <td style="text-align:center;"><a href="#{u_id}" class="htbd-jump-pill">প্যাসেজ ও সমাধান দেখুন</a></td>
        </tr>\n"""

        # Table & Answer Key
        card_table_html = render_info_table_html(item["info_table"])
        card_ans_html = render_answers_html(item["answers"])

        # Card Container
        unseen_cards_html += f"""<div id="{u_id}" class="htbd-qa-card" style="background:#ffffff; border:1px solid #e2e8f0; border-left:4px solid #0c2340; border-radius:8px; padding:22px 24px; margin-bottom:30px; box-shadow:0 2px 6px rgba(0,0,0,0.04); scroll-margin-top:80px;">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:10px; margin-bottom:8px;">
            <h3 style="margin:0; color:#0c2340; font-size:18.5px; font-weight:700;">Unseen {item['id']:02d}: {item['title']}</h3>
            <a href="#unseen-index" class="htbd-back-btn" title="উপরে আনসিন সূচিতে ফিরে যান">↑ আনসিন সূচি</a>
          </div>
          <p style="margin:0 0 12px 0; font-size:14px; color:#64748b;"><strong>বাংলা অর্থ:</strong> {item['bn_title']} &bull; <strong>রেটিং:</strong> <span style="color:{star_color}; font-weight:700;">{item['stars']}</span> &bull; <strong style="color:{star_color};">{item['priority']}</strong> &bull; <strong>বোর্ড:</strong> {item['boards']}</p>
          
          <div style="background:#f8fafc; border-left:3px solid #0284c7; padding:14px 18px; border-radius:4px; margin-bottom:16px;">
            <p style="margin:0 0 6px 0; font-weight:700; color:#0369a1; font-size:14.5px;">আনসিন প্যাসেজ অনুচ্ছেদ (Reading Comprehension Passage):</p>
            <p style="margin:0; font-style:italic; line-height:1.8; color:#334155; font-size:16px;">"{item['passage']}"</p>
          </div>

          <div style="background:#ffffff; border:1px solid #e2e8f0; padding:16px 20px; border-radius:6px; margin-bottom:16px;">
            <p style="margin:0 0 8px 0; font-weight:700; color:#0c2340; font-size:15.5px;">Question 4: Complete the table below with information from the passage (5 Marks)</p>
            {card_table_html}
            <div style="background:#f0fdf4; border:1px solid #bbf7d0; padding:10px 14px; border-radius:4px; margin-top:10px; color:#14532d; font-size:15px;">
              <strong>সঠিক উত্তর (Answer Key):</strong> {card_ans_html}
            </div>
          </div>

          <div style="background:#fdfefe; border:1px solid #dbeafe; border-left:4px solid #1e40af; padding:16px 20px; border-radius:6px; margin-bottom:14px;">
            <p style="margin:0 0 8px 0; font-weight:700; color:#1e40af; font-size:15.5px;">Question 5: Write a summary of the passage in your own words (10 Marks)</p>
            <p style="margin:0; font-size:16px; line-height:1.8; color:#1e293b;">
              {item['model_summary']}
            </p>
            <p style="margin:10px 0 0 0; font-size:13.5px; color:#64748b; border-top:1px dashed #cbd5e1; padding-top:8px;">
              <strong>প্যারাফ্রেজিং ও কি-ওয়ার্ড নোট:</strong> {item['vocab_notes']}
            </p>
          </div>

          <div style="text-align:right;">
            <a href="#unseen-index" class="htbd-back-text-link">↑ উপরে আনসিন মাস্টার সূচিতে ফিরুন</a>
          </div>
        </div>\n"""

    unseen_master_index = f"""<div id="unseen-index" class="htbd-master-index-card">
      <h3 style="margin:0 0 8px 0; color:#0c2340; font-size:19.5px; font-weight:700;">৪১টি সম্ভাব্য আনসিন প্যাসেজের মাস্টার সূচি ও সলিউশন জাম্প-লিংক (Questions 4 &amp; 5)</h3>
      <p style="margin:0 0 16px 0; font-size:15px; color:#475569;">নিচের যেকোনো প্যাসেজের শিরোনাম বা "প্যাসেজ ও সমাধান দেখুন" বাটনে ক্লিক করে সরাসরি সংশ্লিষ্ট অনুচ্ছেদ, ইনফরমেশন ট্রান্সফার ছক ও পূর্ণাঙ্গ মডেল সামারিতে জাম্প করুন:</p>
      <div style="overflow-x:auto; -webkit-overflow-scrolling:touch;">
        <table class="htbd-academic-table" style="font-size:14.5px; margin:0;">
          <thead>
            <tr>
              <th style="width:40px; text-align:center;">নং</th>
              <th style="width:50px; text-align:center;">স্টার</th>
              <th style="width:30%;">প্যাসেজ শিরোনাম ও বিষয়বস্তু</th>
              <th style="width:22%;">থিম ও ক্যাটাগরি</th>
              <th style="width:18%;">বোর্ড রেফারেন্স</th>
              <th style="width:160px; text-align:center;">সরাসরি জাম্প লিংক</th>
            </tr>
          </thead>
          <tbody>
            {unseen_index_rows}
          </tbody>
        </table>
      </div>
    </div>"""

    # 2. Render Board Exam Analysis (26 March & John Milton)
    march_table = render_info_table_html(MODEL_02_26_MARCH["info_transfer_table"])
    march_ans = render_answers_html(MODEL_02_26_MARCH["info_transfer_answers"])

    milton_table = render_info_table_html(MODEL_03_JOHN_MILTON["info_transfer_table"])
    milton_ans = render_answers_html(MODEL_03_JOHN_MILTON["info_transfer_answers"])

    # 3. Assemble Complete HTML Body
    html = f"""<style>
  html {{
    scroll-behavior: smooth !important;
  }}
  .htbd-academic-container {{
    font-family: 'SolaimanLipi', Arial, sans-serif !important;
    font-size: 17.5px !important;
    line-height: 1.85 !important;
    color: #1e293b !important;
  }}
  .htbd-academic-heading {{
    color: #0c2340 !important;
    border-left: 5px solid #d4af37 !important;
    padding-left: 14px !important;
    margin-top: 38px !important;
    margin-bottom: 16px !important;
    font-size: 24px !important;
    font-weight: 700 !important;
    line-height: 1.4 !important;
  }}
  .htbd-academic-subheading {{
    color: #1e3a8a !important;
    font-size: 20px !important;
    font-weight: 600 !important;
    margin-top: 26px !important;
    margin-bottom: 12px !important;
    line-height: 1.4 !important;
  }}
  .htbd-overview-box {{
    background: #f8fafd !important;
    border: 1px solid #dbeafe !important;
    border-left: 5px solid #0c2340 !important;
    border-radius: 8px !important;
    padding: 22px 26px !important;
    margin: 24px 0 !important;
    box-shadow: 0 2px 6px rgba(12,35,64,0.06) !important;
  }}
  .htbd-toc-card {{
    background: #f8fafc !important;
    border: 1px solid #e2e8f0 !important;
    border-left: 4px solid #0c2340 !important;
    border-radius: 8px !important;
    padding: 20px 24px !important;
    margin: 28px 0 !important;
  }}
  .htbd-toc-card .toc-title {{
    font-weight: 700;
    font-size: 19px;
    margin: 0 0 14px 0;
    color: #0c2340;
  }}
  .htbd-toc-card ul {{
    list-style: none;
    padding-left: 0;
    margin: 0;
  }}
  .htbd-toc-card ul li {{
    padding: 6px 0;
    border-bottom: 1px dashed #e2e8f0;
  }}
  .htbd-toc-card ul li a {{
    color: #0369a1;
    text-decoration: none;
    font-weight: 600;
  }}
  .htbd-academic-table {{
    width: 100% !important;
    border-collapse: collapse !important;
    margin: 20px 0 !important;
    background: #ffffff !important;
  }}
  .htbd-academic-table th {{
    background: #0c2340 !important;
    color: #ffffff !important;
    padding: 12px 14px !important;
    font-size: 15.5px !important;
    border: 1px solid #0c2340 !important;
    text-align: left !important;
  }}
  .htbd-academic-table td {{
    padding: 10px 14px !important;
    border: 1px solid #e2e8f0 !important;
    font-size: 15px !important;
    vertical-align: middle !important;
  }}
  .htbd-academic-table tr:nth-child(even) {{
    background: #f8fafc !important;
  }}
  .htbd-jump-pill {{
    display: inline-block;
    padding: 5px 12px;
    background: #f0fdf4;
    color: #166534;
    border: 1px solid #bbf7d0;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 700;
    text-decoration: none;
    transition: all 0.2s ease;
    white-space: nowrap;
  }}
  .htbd-jump-pill:hover {{
    background: #16a34a;
    color: #ffffff !important;
    border-color: #16a34a;
  }}
  .htbd-back-btn {{
    display: inline-block;
    font-size: 13px;
    font-weight: 600;
    color: #475569;
    background: #f1f5f9;
    padding: 4px 10px;
    border-radius: 4px;
    text-decoration: none;
    border: 1px solid #cbd5e1;
  }}
  .htbd-back-btn:hover {{
    background: #e2e8f0;
    color: #0f172a;
  }}
  .htbd-back-text-link {{
    font-size: 14px;
    font-weight: 600;
    color: #0284c7;
    text-decoration: none;
  }}
  .htbd-back-text-link:hover {{
    text-decoration: underline;
  }}
  .htbd-master-index-card {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-left: 4px solid #0c2340;
    border-radius: 8px;
    padding: 22px 24px;
    margin: 28px 0;
    box-shadow: 0 2px 6px rgba(0,0,0,0.04);
  }}
  .htbd-qa-card {{
    transition: background 0.3s ease, border 0.3s ease, box-shadow 0.3s ease;
  }}
  .htbd-qa-card:target {{
    border-left-color: #d4af37 !important;
    background: #fffdf5 !important;
    box-shadow: 0 0 0 3px rgba(212,175,55,0.25) !important;
  }}
  .htbd-faq-item {{
    background: #ffffff !important;
    border: 1px solid #e2e8f0 !important;
    border-left: 4px solid #0c2340 !important;
    border-radius: 6px !important;
    padding: 16px 20px !important;
    margin-bottom: 16px !important;
  }}
  .htbd-series-nav {{
    background: #f1f5f9 !important;
    border: 1px solid #cbd5e1 !important;
    border-left: 6px solid #0c2340 !important;
    border-radius: 8px !important;
    padding: 22px 26px !important;
    margin: 32px 0 !important;
  }}
  .htbd-series-nav .nav-title {{
    font-size: 18.5px !important;
    font-weight: 700 !important;
    margin: 0 0 6px 0 !important;
    color: #0f172a !important;
  }}
  .htbd-series-nav .nav-desc {{
    font-size: 15px !important;
    color: #475569 !important;
    margin: 0 0 14px 0 !important;
    line-height: 1.5 !important;
  }}
  .htbd-series-nav ul {{
    margin: 0 !important;
    padding-left: 20px !important;
    list-style-type: disc !important;
  }}
  .htbd-series-nav ul li {{
    margin-bottom: 8px !important;
    font-size: 16px !important;
    line-height: 1.6 !important;
    color: #334155 !important;
  }}
  .htbd-series-nav ul li a {{
    color: #0369a1 !important;
    text-decoration: underline !important;
    font-weight: 600 !important;
  }}
  .htbd-series-nav ul li.current-post {{
    color: #0f172a !important;
    font-weight: 700 !important;
    background: #e2e8f0 !important;
    padding: 3px 8px !important;
    border-radius: 4px !important;
    display: inline-block !important;
  }}
  .htbd-hero-img {{
    width: 100% !important;
    max-width: 100% !important;
    height: auto !important;
    border-radius: 8px !important;
    box-shadow: 0 4px 14px rgba(0,0,0,0.10) !important;
    display: block !important;
    margin: 0 0 20px 0 !important;
  }}
</style>

<div class="htbd-academic-container">

  <figure style="margin: 0 0 20px 0;">
    <img class="htbd-hero-img" src="{banner_url}" alt="{banner_alt}" title="{banner_alt}" width="1200" height="675" loading="eager" />
    <figcaption style="font-size: 14px; color: #64748b; text-align: center; margin-top: 6px;">SSC 2027 English 1st Paper Unseen Passage &amp; Summary Writing &mdash; Part 02 of the Study Silo Series</figcaption>
  </figure>

  <div class="htbd-overview-box">
    <p style="margin: 0 0 10px 0; font-size: 16px; color: #1e3a8a; font-weight: 700;">টপিক ও ফোকাস: SSC 2027 English Unseen Passage &amp; Summary Suggestion (Questions 4, 5)</p>
    <p>বোর্ড পরীক্ষায় শিক্ষার্থীদের ফ্রি-হ্যান্ড রিডিং ও সিন্থেসিস দক্ষতা যাচাইয়ে <strong>SSC 2027 English Unseen Passage Suggestion</strong> পর্বটি অত্যন্ত গুরুত্বপূর্ণ। এই অংশে পাঠ্যবই-বহির্ভূত আনসিন প্যাসেজ থেকে মোট <strong>১৫ নম্বর</strong> বরাদ্দ থাকে—যার মধ্যে <strong>Question 4: Information Transfer (5 Marks)</strong> এবং <strong>Question 5: Summary Writing (10 Marks)</strong> অন্তর্ভুক্ত। ঐতিহাসিক ব্যক্তিত্ব, বিশিষ্ট বিজ্ঞানী, স্বাধীনতা সংগ্রামী ও আন্তর্জাতিক ঘটনাবলী সম্পর্কিত ৪১টি নির্বাচিত আনসিন বিষয়ের মাস্টার সূচি, সরাসরি সলিউশন জাম্প-লিংক এবং প্রতিটি প্যাসেজের পূর্ণাঙ্গ ইনফরমেশন ট্রান্সফার ছক ও নিখুঁত মডেল সামারি নিচে সন্নিবেশিত হলো।</p>
  </div>

<!--more-->

  <div class="htbd-toc-card">
    <p class="toc-title">বিষয়সূচি (Table of Contents)</p>
    <ul>
      <li><a href="#unseen-marks">১. আনসিন প্যাসেজ: নম্বর বণ্টন ও প্রশ্ন রূপরেখা (Marks Distribution)</a></li>
      <li><a href="#unseen-index">২. ৪১টি সম্ভাব্য আনসিন প্যাসেজের মাস্টার সূচি (Master Navigation Index)</a></li>
      <li><a href="#unseen-cards">৩. ৪১টি আনসিন প্যাসেজের পূর্ণ সমাধান ও সামারি কার্ড (Complete Solution Cards)</a></li>
      <li><a href="#info-transfer-rules">৪. প্রশ্ন ৪: Information Transfer সমাধানের নিয়ম ও কলাম ট্র্যাকিং (Q4 Guide)</a></li>
      <li><a href="#summary-rules">৫. প্রশ্ন ৫: Summary Writing-এ পূর্ণ ১০/১০ পাওয়ার ৫টি সোনালী নিয়ম (Q5 Guide)</a></li>
      <li><a href="#model-march">৬. বোর্ড প্রশ্ন বিশ্লেষণ: দাখিল ২০২৬ — ২৬শে মার্চ স্বাধীনতা দিবস (26 March)</a></li>
      <li><a href="#model-milton">৭. এক্সক্লুসিভ মডেল টেস্ট: মহাকবি জন মিল্টন (John Milton)</a></li>
      <li><a href="#lsi-keywords">৮. সম্পর্কিত গুরুত্বপূর্ণ সার্চ টার্মস ও টপিকস (Related Search Queries)</a></li>
      <li><a href="#faq">৯. সচরাচর জিজ্ঞাসা (FAQ)</a></li>
    </ul>
  </div>

  <h2 class="htbd-academic-heading" id="unseen-marks">১. আনসিন প্যাসেজ: নম্বর বণ্টন ও প্রশ্ন রূপরেখা (Marks Distribution)</h2>
  <p>আনসিন প্যাসেজ সাধারণত কোনো ঐতিহাসিক ব্যক্তিত্বের জীবনী, বৈজ্ঞানিক আবিষ্কার, বিখ্যাত স্থাপনা বা আন্তর্জাতিক ঘটনাপ্রবাহ থেকে সংকলিত হয়। এই একই প্যাসেজের ওপর ভিত্তি করে দুটি পৃথক দক্ষতার মূল্যায়ন করা হয়:</p>

  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 22px 0;">
    <table class="htbd-academic-table">
      <thead>
        <tr>
          <th>প্রশ্ন নম্বর</th>
          <th>আইটেমের নাম (Item Name)</th>
          <th>দক্ষতা ও কার্যক্রম (Skill Tested)</th>
          <th>নম্বর (Marks)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>প্রশ্ন ৪ (Q4)</strong></td>
          <td>Information Transfer</td>
          <td>প্যাসেজ থেকে নির্দিষ্ট তথ্য (নাম, সন, স্থান, অবদান) খুঁজে ছকে সন্নিবেশ করা</td>
          <td><strong>1 &times; 5 = 5 নম্বর</strong></td>
        </tr>
        <tr>
          <td><strong>প্রশ্ন ৫ (Q5)</strong></td>
          <td>Summary Writing</td>
          <td>প্যাসেজের মূল ভাবার্থ সংক্ষেপ করে ১/৩ দৈর্ঘ্যে নিজস্ব ভাষায় সারসংক্ষেপ লেখা</td>
          <td><strong>১০ নম্বর</strong></td>
        </tr>
        <tr>
          <td colspan="3" style="text-align:right; font-weight:700; background:#f1f5f9;">মোট নম্বর (Total Marks):</td>
          <td style="font-weight:700; background:#f1f5f9; color:#0c2340;"><strong>১৫ নম্বর</strong></td>
        </tr>
      </tbody>
    </table>
  </div>

  <h2 class="htbd-academic-heading">২. ৪১টি সম্ভাব্য আনসিন প্যাসেজের মাস্টার সূচি ও জাম্প-লিংক</h2>
  {unseen_master_index}

  <h2 class="htbd-academic-heading" id="unseen-cards">৩. ৪১টি আনসিন প্যাসেজের পূর্ণ সমাধান ও সামারি কার্ড (Complete Solution Cards)</h2>
  <p>নিচে প্রতিটি আনসিন প্যাসেজের পূর্ণ অনুচ্ছেদ, প্রশ্ন ৪-এর ইনফরমেশন ট্রান্সফার টেবিল ও সঠিক উত্তর এবং প্রশ্ন ৫-এর জন্য পূর্ণ ১০/১০ পাওয়ার উপযোগী ৬০–৮০ শব্দের নিখুঁত মডেল সামারি দেওয়া হলো:</p>
  {unseen_cards_html}

  <h2 class="htbd-academic-heading" id="info-transfer-rules">৪. প্রশ্ন ৪: Information Transfer সমাধানের নিয়ম ও কলাম ট্র্যাকিং (Q4 Guide)</h2>
  <p>ইনফরমেশন ট্রান্সফার মূলত একটি দ্রুত তথ্য বিশ্লেষণমূলক প্রশ্ন। এখানে ৫টি শূন্যস্থান পূরণ করতে ৫ নম্বর পাওয়া যায়। শতভাগ নম্বর অর্জনের পদ্ধতি:</p>
  <ul style="line-height:1.85;">
    <li><strong>কলামের হেডিং লক্ষ্য করুন:</strong> ছকের কলামে "Who / What", "Event / Activity", "Year / Time", "Place / Where" এবং "Whom / Why" হেডিংগুলো খুব যত্নসহকারে পড়ুন। প্রতিটি কলাম ঠিক কোন প্রশ্নের উত্তর চাইছে, তা বুঝলেই অর্ধেক কাজ শেষ।</li>
    <li><strong>অনর্থক বড় বাক্য না লেখা:</strong> ছকের ভেতর পুরো বাক্য লেখার প্রয়োজন নেই। শুধু মূল শব্দগুচ্ছ (Phrase) বা নির্দিষ্ট তথ্য (যেমন: <em>"in 1971"</em> বা <em>"at Cambridge University"</em>) লিখলেই পূর্ণ নম্বর দেওয়া হয়।</li>
    <li><strong>ক্রমানুসারে সাজানো:</strong> উত্তরপত্রে শুধু (i), (ii), (iii), (iv), (v) লিখে পাশে সরাসরি উত্তর লিখে দিন। সম্পূর্ণ টেবিল খাতায় আঁকা বাধ্যতামূলক নয়, তবে স্পষ্ট হস্তাক্ষরে লিখলে পরীক্ষকের নম্বর দিতে স্বাচ্ছন্দ্য হয়।</li>
  </ul>

  <h2 class="htbd-academic-heading" id="summary-rules">৫. প্রশ্ন ৫: Summary Writing-এ পূর্ণ ১০/১০ পাওয়ার ৫টি সোনালী নিয়ম (Q5 Guide)</h2>
  <p>১০ নম্বরের সামারি রাইটিং অনেক শিক্ষার্থীর কাছেই চ্যালেঞ্জিং মনে হয়। তবে নিচের ৫টি টেকনিক প্রয়োগ করলে পরীক্ষক ৮ থেকে ১০ নম্বর দিতে বাধ্য হন:</p>
  <ul style="line-height:1.85;">
    <li><strong>এক-তৃতীয়াংশ দৈর্ঘ্য (One-third Rule):</strong> সামারির দৈর্ঘ্য মূল প্যাসেজের মোটামুটি এক-তৃতীয়াংশ (সাধারণত ৪ থেকে ৫টি সুসংহত বাক্য বা ৬০–৮০ শব্দ) হতে হবে। বেশি বড় লেখা সামারির মূল নিয়মের পরিপন্থী।</li>
    <li><strong>নিজস্ব ভাষার প্রকাশ (Paraphrasing):</strong> মূল প্যাসেজের কোনো বাক্য হুবহু কপি করে লিখবেন না। সমার্থক শব্দ (Synonyms) ও বাক্যের গঠন বদলে মূল অর্থ তুলে ধরুন।</li>
    <li><strong>উদাহরণ ও প্রত্যক্ষ উক্তি বর্জন:</strong> প্যাসেজের কোনো উদাহরণ, উদ্ধৃতি (Quotation), বা সংখ্যাতাত্ত্বিক সূক্ষ্ম ব্যাখ্যা সামারিতে কখনোই অন্তর্ভুক্ত করবেন না। শুধু মূল সত্য বা ফলাফল লিখুন।</li>
    <li><strong>উত্তম ও মধ্যম পুরুষ বর্জন:</strong> সামারি সবসময় Third Person (He/She/They/The passage) এবং বর্ণনামূলক টেন্সে লিখতে হবে। "I think" বা "We see that" জাতীয় মন্তব্য সম্পূর্ণরূপে বাদ দিন।</li>
    <li><strong>লিঙ্কার ও সাবলীল সংযোগ:</strong> প্রতিটি বাক্যের মাঝে যৌক্তিক ধারাবাহিকতা রক্ষায় উপযুক্ত লিঙ্কার (যেমন: <em>Although, However, In addition, Consequently, Ultimately</em>) ব্যবহার করুন।</li>
  </ul>

  <h2 class="htbd-academic-heading" id="model-march">৬. বোর্ড প্রশ্ন বিশ্লেষণ: দাখিল ২০২৬ — ২৬শে মার্চ স্বাধীনতা দিবস (26 March)</h2>
  <p style="background:#f1f5f9; padding:16px 20px; border-radius:6px; font-style:italic; line-height:1.8;">
    "{MODEL_02_26_MARCH['passage']}"
  </p>
  <h3 class="htbd-academic-subheading">Question 4: Complete the table below with information from the passage (5 Marks)</h3>
  {march_table}
  <p style="background:#f0fdf4; border:1px solid #bbf7d0; padding:12px 16px; border-radius:6px; color:#14532d;">
    <strong>সঠিক উত্তর (Answer Key):</strong> {march_ans}
  </p>
  <h3 class="htbd-academic-subheading">Question 5: Write a summary of the passage in your own words (10 Marks)</h3>
  <div style="background:#f8fafc; border-left:4px solid #0c2340; padding:16px 20px; border-radius:6px; margin:16px 0;">
    <p style="margin:0; font-size:16.5px; line-height:1.8; color:#1e293b;">
      {MODEL_02_26_MARCH['model_summary']}
    </p>
  </div>

  <h2 class="htbd-academic-heading" id="model-milton">৭. এক্সক্লুসিভ মডেল টেস্ট: মহাকবি জন মিল্টন (John Milton)</h2>
  <p style="background:#f1f5f9; padding:16px 20px; border-radius:6px; font-style:italic; line-height:1.8;">
    "{MODEL_03_JOHN_MILTON['passage']}"
  </p>
  <h3 class="htbd-academic-subheading">Question 4: Complete the table below with information from the passage (5 Marks)</h3>
  {milton_table}
  <p style="background:#f0fdf4; border:1px solid #bbf7d0; padding:12px 16px; border-radius:6px; color:#14532d;">
    <strong>সঠিক উত্তর (Answer Key):</strong> {milton_ans}
  </p>
  <h3 class="htbd-academic-subheading">Question 5: Write a summary of the passage in your own words (10 Marks)</h3>
  <div style="background:#f8fafc; border-left:4px solid #0c2340; padding:16px 20px; border-radius:6px; margin:16px 0;">
    <p style="margin:0; font-size:16.5px; line-height:1.8; color:#1e293b;">
      {MODEL_03_JOHN_MILTON['model_summary']}
    </p>
  </div>

  <h2 class="htbd-academic-heading" id="lsi-keywords">৮. সম্পর্কিত গুরুত্বপূর্ণ সার্চ টার্মস ও টপিকস (Related Search Queries)</h2>
  <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:20px 24px; margin:20px 0;">
    <p style="margin:0 0 10px 0; font-size:15px; color:#475569;">গুগলে পরীক্ষার্থীদের বহুল ব্যবহৃত সম্পর্কিত অনুসন্ধানসমূহ:</p>
    <div style="display:flex; flex-wrap:wrap; gap:8px;">
      <span style="background:#e0f2fe; color:#0369a1; padding:4px 10px; border-radius:4px; font-size:13.5px; font-weight:600;">SSC 2027 English Unseen Passage Suggestion</span>
      <span style="background:#e0f2fe; color:#0369a1; padding:4px 10px; border-radius:4px; font-size:13.5px; font-weight:600;">Class 10 Information Transfer Table Question 4</span>
      <span style="background:#e0f2fe; color:#0369a1; padding:4px 10px; border-radius:4px; font-size:13.5px; font-weight:600;">How to Write Summary in English 1st Paper</span>
      <span style="background:#e0f2fe; color:#0369a1; padding:4px 10px; border-radius:4px; font-size:13.5px; font-weight:600;">SSC English Unseen Summary 10 out of 10 Rules</span>
      <span style="background:#e0f2fe; color:#0369a1; padding:4px 10px; border-radius:4px; font-size:13.5px; font-weight:600;">Bir Shrestha Mohiuddin Jahangir Unseen Passage</span>
      <span style="background:#e0f2fe; color:#0369a1; padding:4px 10px; border-radius:4px; font-size:13.5px; font-weight:600;">Hazrat Omar Unseen Passage Model Answer</span>
      <span style="background:#e0f2fe; color:#0369a1; padding:4px 10px; border-radius:4px; font-size:13.5px; font-weight:600;">Dakhil 2026 English 1st Paper Question Solution</span>
    </div>
  </div>

  <h2 class="htbd-academic-heading" id="faq">৯. সচরাচর জিজ্ঞাসা (FAQ)</h2>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">Question 1: Information Transfer-এ কি পরীক্ষার খাতায় পুরো ছক তুলতে হবে?</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">উত্তর: পুরো ছক তোলা বাধ্যতামূলক নয়। পরীক্ষার খাতায় শুধুমাত্র রোমান সংখ্যা দিয়ে (i), (ii), (iii), (iv), (v) লিখে সরাসরি সঠিক তথ্য লিখলে পূর্ণ নম্বর পাওয়া যায়। তবে স্পষ্ট টেবিল আঁকলে পরীক্ষকের খাতা দেখার সুবিধা হয়।</p>
  </div>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">Question 2: সামারিতে কতটি বাক্য লেখা আদর্শ?</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">উত্তর: সামারিতে সাধারণত ৪ থেকে ৬টি সুসংহত ও অর্থবহ বাক্য লেখা সবচেয়ে আদর্শ। মোট শব্দের পরিমাণ ৬০ থেকে ৮০ শব্দের মধ্যে রাখা বাঞ্ছনীয়।</p>
  </div>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">Question 3: সামারিতে কি মূল প্যাসেজের লাইন হুবহু লেখা যাবে?</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">উত্তর: কখনোই না। হুবহু লাইন তুললে পরীক্ষক নম্বর কমিয়ে দেন। তথ্য ঠিক রেখে সমার্থক শব্দ ও নিজস্ব বাক্য গঠনে প্যারাফ্রেজ করে লিখলেই সর্বোচ্চ নম্বর পাওয়া সম্ভব।</p>
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
  "datePublished": "2026-09-17T02:00:00+06:00",
  "dateModified": "2026-09-17T02:00:00+06:00"
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{"@type": "Question", "name": "Do I have to draw the complete table for Information Transfer in the exam?", "acceptedAnswer": {{"@type": "Answer", "text": "No, drawing the table is not mandatory. Simply writing the Roman numerals (i) through (v) with the exact answer phrases guarantees full marks."}}}},
    {{"@type": "Question", "name": "How many sentences are ideal for Summary Writing in Q5?", "acceptedAnswer": {{"@type": "Answer", "text": "Writing 4 to 6 concise and coherent sentences (between 60 to 80 words) is the national curriculum standard for summary writing."}}}},
    {{"@type": "Question", "name": "Can I copy exact sentences from the passage into my summary?", "acceptedAnswer": {{"@type": "Answer", "text": "No, copying sentences directly causes mark penalties. Paraphrase using synonyms and your own sentence structures."}}}}
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

if __name__ == "__main__":
    slug, html, meta = build_post()
    print(f"Silo 02 generated successfully! Length: {len(html)} chars, Slug: {slug}")
