#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/pdf_to_post/silo_01_builder.py
-------------------------------------
Generates Silo Post 01: Seen Passage (Q1-3)
Includes:
- Master Seen Index (#seen-index) with 33 Passages + Jump Links
- 33 Comprehensive Solution Cards (#seen-01 to #seen-33) with Passage Excerpt,
  Question 1 MCQs, Question 2 Open Q/As, Question 3 Gap Filling, and Vocabulary Notes
- Interactive :target golden glow highlight (#d4af37)
- Dakhil 2026 Model Test & Solution (Zahir Raihan)
- Exclusive Model Test & Solution (Climate Change)
- Schema.org FAQPage & BlogPosting
- Zero-Emoji Policy strictly enforced
"""

import json
from data_ssc_2027_seen_full import SEEN_PASSAGES_FULL_33
from data_ssc_2027_seen import (
    DAKHIL_2026_SEEN_MODEL as DAKHIL_2026_SEEN,
    EXCLUSIVE_MODEL_TEST_SEEN as MODEL_TEST_SEEN
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

def render_gap_answers(ans_dict):
    items = [f"<strong>({k})</strong> {v}" for k, v in ans_dict.items()]
    return " &nbsp;|&nbsp; ".join(items)

def render_mcqs_html(mcqs_list):
    res = ""
    romans = ["(i)", "(ii)", "(iii)", "(iv)", "(v)", "(vi)", "(vii)"]
    letters = ["(a)", "(b)", "(c)", "(d)"]
    for idx, m in enumerate(mcqs_list):
        r_num = romans[idx] if idx < len(romans) else f"({idx+1})"
        opts_html = " ".join([f"<span>{letters[i]} {opt}</span>" for i, opt in enumerate(m["opts"])])
        res += f"""<div style="margin-bottom:12px; background:#f8fafc; padding:10px 14px; border-radius:6px;">
          <p style="margin:0 0 6px 0; font-weight:600; color:#0f172a;">{r_num} {m['q']}</p>
          <p style="margin:0; font-size:15px; color:#334155; display:flex; flex-wrap:wrap; gap:16px;">{opts_html}</p>
          <p style="margin:5px 0 0 0; color:#15803d; font-size:14.5px; font-weight:600;">সঠিক উত্তর: {m['ans']}</p>
        </div>\n"""
    return res

def render_open_qas_html(qas_list):
    res = ""
    letters = ["(a)", "(b)", "(c)", "(d)", "(e)"]
    for idx, qa in enumerate(qas_list):
        lbl = letters[idx] if idx < len(letters) else f"({idx+1})"
        res += f"""<div style="margin-bottom:12px; background:#f8fafc; padding:12px 16px; border-radius:6px; border-left:4px solid #0c2340;">
          <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340;">{lbl} {qa['q']}</p>
          <p style="margin:0; color:#1e293b; font-size:15.5px; line-height:1.7;"><strong>উত্তর:</strong> {qa['a']}</p>
        </div>\n"""
    return res

def build_post():
    slug = "ssc-2027-english-seen-passage-suggestion"
    title = "SSC 2027 English Seen Passage Suggestion | এসএসসি সিন প্যাসেজ MCQ ও প্রশ্নোত্তর (100% Common)"
    meta_desc = "SSC 2027 English Seen Passage Suggestion। EFT-এর ৩৩টি সিন প্যাসেজ, MCQ (Q1), প্রশ্নোত্তর (Q2) ও Gap Filling (Q3) এর পূর্ণাঙ্গ বোর্ড সমাধান।"
    banner_url = f"{CDN_BASE}/ssc_2027_silo_01_seen_passage.webp?v=2"
    banner_alt = "SSC 2027 English Seen Passage Suggestion — MCQ, Question Answer and Gap Filling Guide"
    url = f"{BLOG_BASE}/{slug}.html"
    series_nav = get_series_nav("Part 01")

    # 1. Render 33 Passages Master Index & Solution Cards
    seen_index_rows = ""
    seen_cards_html = ""

    for item in SEEN_PASSAGES_FULL_33:
        s_id = item["slug_id"]
        star_color = "#b91c1c" if item["stars"] == "***" else ("#c2410c" if item["stars"] == "**" else "#4b5563")

        # Master Table Row
        seen_index_rows += f"""<tr>
          <td style="text-align:center; font-weight:700;">{item['id']:02d}</td>
          <td style="text-align:center; font-weight:700; color:{star_color}; font-size:16px;">{item['stars']}</td>
          <td><a href="#{s_id}" style="color:#0369a1; font-weight:600; text-decoration:none;">{item['title']}</a><br><span style="font-size:13px; color:#64748b;">{item['theme']}</span></td>
          <td style="text-align:center; font-size:13.5px; color:#475569;">{item['unit_lesson']}</td>
          <td style="font-size:13px; color:#64748b;">{item['boards']}</td>
          <td style="text-align:center;"><a href="#{s_id}" class="htbd-jump-pill">অনুশীলন ও সমাধান দেখুন</a></td>
        </tr>\n"""

        # Card components
        mcqs_html = render_mcqs_html(item["mcqs"])
        qas_html = render_open_qas_html(item["open_qas"])
        gap_ans_html = render_gap_answers(item["gap_fill"]["answers"])

        seen_cards_html += f"""<div id="{s_id}" class="htbd-qa-card" style="background:#ffffff; border:1px solid #e2e8f0; border-left:4px solid #0c2340; border-radius:8px; padding:22px 24px; margin-bottom:30px; box-shadow:0 2px 6px rgba(0,0,0,0.04); scroll-margin-top:80px;">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:10px; margin-bottom:8px;">
            <h3 style="margin:0; color:#0c2340; font-size:18.5px; font-weight:700;">Seen Passage {item['id']:02d}: {item['title']}</h3>
            <a href="#seen-index" class="htbd-back-btn" title="উপরে সিন প্যাসেজ সূচিতে ফিরে যান">↑ সিন প্যাসেজ সূচি</a>
          </div>
          <p style="margin:0 0 12px 0; font-size:14px; color:#64748b;"><strong>ইউনিট ও লেসন:</strong> {item['unit_lesson']} &bull; <strong>বিষয়বস্তু:</strong> {item['theme']} &bull; <strong>রেটিং:</strong> <span style="color:{star_color}; font-weight:700;">{item['stars']}</span> &bull; <strong style="color:{star_color};">{item['priority']}</strong> &bull; <strong>বোর্ড:</strong> {item['boards']}</p>
          
          <div style="background:#f8fafc; border-left:3px solid #0284c7; padding:14px 18px; border-radius:4px; margin-bottom:16px;">
            <p style="margin:0 0 6px 0; font-weight:700; color:#0369a1; font-size:14.5px;">সিন প্যাসেজ মূল অনুচ্ছেদ (EFT Text Excerpt):</p>
            <p style="margin:0; font-style:italic; line-height:1.8; color:#334155; font-size:16px;">"{item['passage']}"</p>
          </div>

          <div style="background:#ffffff; border:1px solid #e2e8f0; padding:16px 20px; border-radius:6px; margin-bottom:16px;">
            <p style="margin:0 0 10px 0; font-weight:700; color:#0c2340; font-size:15.5px;">Question 1: Choose the correct answer from the following alternatives (MCQ - 3 Model Questions)</p>
            {mcqs_html}
          </div>

          <div style="background:#ffffff; border:1px solid #e2e8f0; padding:16px 20px; border-radius:6px; margin-bottom:16px;">
            <p style="margin:0 0 10px 0; font-weight:700; color:#0c2340; font-size:15.5px;">Question 2: Answer the following questions based on the passage (Open-Ended - 2 Questions)</p>
            {qas_html}
          </div>

          <div style="background:#fdfefe; border:1px solid #dbeafe; border-left:4px solid #0284c7; padding:16px 20px; border-radius:6px; margin-bottom:14px;">
            <p style="margin:0 0 8px 0; font-weight:700; color:#0284c7; font-size:15.5px;">Question 3: Fill in each gap with a suitable word based on the passage (Gap Filling Without Clues - 5 Marks)</p>
            <p style="margin:0 0 10px 0; font-size:15.5px; line-height:1.8; color:#1e293b;">{item['gap_fill']['sentence']}</p>
            <div style="background:#f0fdf4; border:1px solid #bbf7d0; padding:10px 14px; border-radius:4px; color:#14532d; font-size:14.5px;">
              <strong>সঠিক উত্তর (Answer Key):</strong> {gap_ans_html}
            </div>
          </div>

          <p style="margin:10px 0 0 0; font-size:13.5px; color:#64748b; border-top:1px dashed #cbd5e1; padding-top:8px;">
            <strong>গুরুত্বপূর্ণ শব্দার্থ ও সমার্থক শব্দ (Key Vocabulary &amp; Synonyms):</strong> {item['vocab_notes']}
          </p>
          <div style="text-align:right; margin-top:10px;">
            <a href="#seen-index" class="htbd-back-text-link">↑ সিন প্যাসেজ সূচিতে ফিরে যান</a>
          </div>
        </div>\n"""

    # 2. Render Dakhil 2026 MCQs
    dakhil_mcqs = ""
    for m in DAKHIL_2026_SEEN["mcq_questions"]:
        opts = " ".join([f"<span>{opt}</span>" for opt in m["options"]])
        dakhil_mcqs += f"""<div style="margin-bottom:14px; background:#f8fafc; padding:10px 14px; border-radius:6px;">
          <p style="margin:0 0 6px 0; font-weight:600;">({m['id']}) {m['question']}</p>
          <p style="margin:0; font-size:15.5px; color:#334155; display:flex; flex-wrap:wrap; gap:16px;">{opts}</p>
          <p style="margin:4px 0 0 0; color:#15803d; font-size:15px; font-weight:600;">সঠিক উত্তর: {m['answer']}</p>
        </div>\n"""

    # 3. Render Dakhil 2026 Q/A
    dakhil_qas = ""
    for q in DAKHIL_2026_SEEN["open_questions"]:
        dakhil_qas += f"""<div style="margin-bottom:14px; background:#f8fafc; padding:12px 16px; border-radius:6px; border-left:4px solid #0c2340;">
          <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340;">({q['id']}) {q['question']}</p>
          <p style="margin:0; color:#1e293b; font-size:16px; line-height:1.7;"><strong>উত্তর:</strong> {q['answer']}</p>
        </div>\n"""

    # 4. Render Dakhil 2026 Gap Fill
    dakhil_gaps = " ".join([f"<strong>({k})</strong> {v}" for k, v in DAKHIL_2026_SEEN["gap_fill"]["answers"].items()])

    # 5. Render Model Test MCQs
    model_mcqs = ""
    for m in MODEL_TEST_SEEN["mcq_questions"]:
        opts = " ".join([f"<span>{opt}</span>" for opt in m["options"]])
        model_mcqs += f"""<div style="margin-bottom:14px; background:#f8fafc; padding:10px 14px; border-radius:6px;">
          <p style="margin:0 0 6px 0; font-weight:600;">({m['id']}) {m['question']}</p>
          <p style="margin:0; font-size:15.5px; color:#334155; display:flex; flex-wrap:wrap; gap:16px;">{opts}</p>
          <p style="margin:4px 0 0 0; color:#15803d; font-size:15px; font-weight:600;">সঠিক উত্তর: {m['answer']}</p>
        </div>\n"""

    # 6. Render Model Test Q/A
    model_qas = ""
    for q in MODEL_TEST_SEEN["open_questions"]:
        model_qas += f"""<div style="margin-bottom:14px; background:#f8fafc; padding:12px 16px; border-radius:6px; border-left:4px solid #0c2340;">
          <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340;">({q['id']}) {q['question']}</p>
          <p style="margin:0; color:#1e293b; font-size:16px; line-height:1.7;"><strong>উত্তর:</strong> {q['answer']}</p>
        </div>\n"""

    # 7. Render Model Test Gap Fill
    model_gaps = " ".join([f"<strong>({k})</strong> {v}" for k, v in MODEL_TEST_SEEN["gap_fill"]["answers"].items()])

    html = f"""<style>
  html {{
    scroll-behavior: smooth;
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
    <figcaption style="font-size: 14px; color: #64748b; text-align: center; margin-top: 6px;">SSC 2027 English 1st Paper Seen Passage — Part 01 of the Study Silo Series</figcaption>
  </figure>

  <div class="htbd-overview-box">
    <p style="margin: 0 0 10px 0; font-size: 16px; color: #1e3a8a; font-weight: 700;">টপিক ও ফোকাস: SSC 2027 English Seen Passage Suggestion (Questions 1, 2, 3)</p>
    <p>মাধ্যমিক ও উচ্চমাধ্যমিক শিক্ষা বোর্ডের নতুন কারিকুলাম অনুসারে <strong>SSC 2027 English Seen Passage Suggestion</strong> পর্বে শিক্ষার্থীদের পাঠ্যবই <em>English For Today (EFT)</em> থেকে প্রথম তিনটি প্রশ্ন সমাধান করতে হয়। এই অংশে মোট <strong>২২ নম্বর</strong> বরাদ্দ থাকে—যার মধ্যে <strong>Question 1: Multiple Choice Questions (MCQ - 7 Marks)</strong>, <strong>Question 2: Open-Ended Question Answer (10 Marks)</strong> এবং <strong>Question 3: Gap Filling Without Clues (5 Marks)</strong> অন্তর্ভুক্ত। ঢাকা, চট্টগ্রাম, রাজশাহীসহ সকল শিক্ষা বোর্ডের বিগত ৫ বছরের বোর্ড প্রশ্ন বিশ্লেষণ করে এখানে পাঠ্যবইয়ের ৩৩টি গুরুত্বপূর্ণ সিন প্যাসেজের ৩-স্টার সুপার সাজেশন, জাম্প-লিংক মাস্টার সূচি, হুবহু বোর্ড প্রশ্নের মডেল টেস্ট এবং শতভাগ কমন পাওয়ার টেকনিক্যাল টিপস তুলে ধরা হলো।</p>
  </div>

<!--more-->

  <div class="htbd-toc-card">
    <p class="toc-title">বিষয়সূচি (Table of Contents)</p>
    <ul>
      <li><a href="#seen-marks">১. সিন প্যাসেজ: নম্বর বণ্টন ও প্রশ্নকাঠামো (Marks Distribution)</a></li>
      <li><a href="#seen-index">২. পাঠ্যবইয়ের ৩৩টি সিন প্যাসেজ মাস্টার সূচি ও জাম্প আর্কিটেকচার (Master Index)</a></li>
      <li><a href="#mcq-guide">৩. প্রশ্ন ১: MCQ সমাধানের ব্যাকরণ ও টেক্সচুয়াল কৌশল (Q1 Guide)</a></li>
      <li><a href="#qa-guide">৪. প্রশ্ন ২: Open-Ended প্রশ্নে পূর্ণ ১০/১০ পাওয়ার নিয়ম (Q2 Guide)</a></li>
      <li><a href="#gap-fill-guide">৫. প্রশ্ন ৩: Gap Filling Without Clues সমাধানের ৫টি কৌশল (Q3 Guide)</a></li>
      <li><a href="#seen-solutions">৬. ৩৩টি সিন প্যাসেজ: পূর্ণাঙ্গ টেক্সট, MCQ, প্রশ্নোত্তর ও গ্যাপ ফিলিং সমাধান (All 33 Solution Cards)</a></li>
      <li><a href="#model-dakhil">৭. মডেল পরীক্ষা ০১: দাখিল ২০২৬ বোর্ড প্রশ্ন ও পূর্ণাঙ্গ সমাধান (Zahir Raihan)</a></li>
      <li><a href="#model-exclusive">৮. মডেল পরীক্ষা ০২: এক্সক্লুসিভ মডেল টেস্ট ও পূর্ণাঙ্গ সমাধান (Climate Change)</a></li>
      <li><a href="#faq">৯. সচরাচর জিজ্ঞাসা (FAQ)</a></li>
    </ul>
  </div>

  <h2 class="htbd-academic-heading" id="seen-marks">১. সিন প্যাসেজ: নম্বর বণ্টন ও প্রশ্নকাঠামো (Marks Distribution)</h2>
  <p>এসএসসি ও দাখিল পরীক্ষায় প্রথম দুটি প্যাসেজ সরাসরি NCTB প্রণীত পাঠ্যবই <em>English For Today</em> থেকে নেওয়া হয়। ১ম প্যাসেজ থেকে প্রশ্ন ১ ও ২ এবং ২য় প্যাসেজ থেকে প্রশ্ন ৩ গঠিত হয়।</p>

  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 22px 0;">
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
          <td colspan="3" style="text-align:right; font-weight:700; background:#f1f5f9;">মোট নম্বর (Total Marks):</td>
          <td style="font-weight:700; background:#f1f5f9; color:#0c2340;"><strong>২২ নম্বর</strong></td>
        </tr>
      </tbody>
    </table>
  </div>

  <h2 class="htbd-academic-heading" id="seen-index">২. পাঠ্যবইয়ের ৩৩টি সিন প্যাসেজ মাস্টার সূচি ও জাম্প আর্কিটেকচার (Master Index)</h2>
  <p>নিচে ২০২৭ সালের এসএসসি ও দাখিল পরীক্ষার্থীদের জন্য পাঠ্যবইয়ের ৩৩টি সিন প্যাসেজ গুরুত্ব অনুযায়ী ৩-স্টার (সর্বাধিক সম্ভাব্য), ২-স্টার ও ১-স্টার ক্যাটাগরিতে বোর্ড রেফারেন্সসহ সাজানো হলো। যেকোনো প্যাসেজের নামের ওপর অথবা ডানের সবুজ পিল বাটনে ক্লিক করে সরাসরি সংশ্লিষ্ট প্যাসেজের টেক্সট, MCQ, প্রশ্নোত্তর ও গ্যাপ ফিলিং অনুশীলনীতে চলে যান:</p>

  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 22px 0;">
    <table class="htbd-academic-table">
      <thead>
        <tr>
          <th style="width:6%;">ক্র.</th>
          <th style="width:8%; text-align:center;">স্টার</th>
          <th style="width:36%;">প্যাসেজের শিরোনাম ও বিষয়বস্তু</th>
          <th style="width:16%; text-align:center;">ইউনিট ও লেসন</th>
          <th style="width:18%;">বিগত বোর্ড পরীক্ষা</th>
          <th style="width:16%; text-align:center;">অনুশীলনী লিঙ্ক</th>
        </tr>
      </thead>
      <tbody>
        {seen_index_rows}
      </tbody>
    </table>
  </div>

  <h2 class="htbd-academic-heading" id="mcq-guide">৩. প্রশ্ন ১: MCQ সমাধানের ব্যাকরণ ও টেক্সচুয়াল কৌশল (Q1 Guide)</h2>
  <p>Q1-এ ৭টি বহুনির্বাচনী প্রশ্ন থাকে। প্রতিটি প্রশ্নে সঠিক উত্তরের জন্য ১ নম্বর বরাদ্দ। MCQ-তে পূর্ণ ৭ নম্বর পাওয়ার মূল কৌশলগুলো হলো:</p>
  <ul style="line-height:1.85;">
    <li><strong>Contextual Synonym ও Antonym:</strong> শব্দার্থ সরাসরি আভিধানিক না হয়ে অনেক সময় প্যাসেজের ভাবার্থ অনুযায়ী হয়। বাক্যটির পুরো অর্থ পড়ে উত্তরের অপশন নির্বাচন করুন।</li>
    <li><strong>Elimination Method:</strong> চারটি অপশনের মধ্যে যেসব অপশন নিশ্চিতভাবে ভুল বা প্যাসেজের তথ্যের সাথে সাংঘর্ষিক, সেগুলো আগে বাদ দিন।</li>
    <li><strong>Part of Speech রূপান্তর:</strong> প্রশ্নে যে Part of Speech-এ জানতে চাওয়া হয়েছে, সঠিক উত্তরও সেই একই ব্যাকরণিক ক্যাটাগরির হবে।</li>
  </ul>

  <h2 class="htbd-academic-heading" id="qa-guide">৪. প্রশ্ন ২: Open-Ended প্রশ্নে পূর্ণ ১০/১০ পাওয়ার নিয়ম (Q2 Guide)</h2>
  <p>Q2-এ ৫টি প্রশ্নের উত্তর লিখতে হয় (প্রতিটিতে ২ নম্বর)। পূর্ণ নম্বর পেতে নিচের নিয়মগুলো কঠোরভাবে মেনে চলুন:</p>
  <ul style="line-height:1.85;">
    <li><strong>হুবহু প্যাসেজ কপি না করা:</strong> প্যাসেজের বাক্য সরাসরি তুলে দিলে পরীক্ষক নম্বর কমিয়ে দেন। তথ্য প্যাসেজ থেকে নিয়ে নিজের ভাষায় বাক্য গঠন করুন।</li>
    <li><strong>Tense সঙ্গতি বজায় রাখা:</strong> প্রশ্ন যে Tense-এ থাকবে (Present/Past), উত্তরও ঠিক সেই Tense-এ লিখতে হবে। যেমন: প্রশ্ন "Why did he go?" হলে উত্তর "He went because..." দিয়ে শুরু হবে।</li>
    <li><strong>Two-part Structure:</strong> প্রতিটি ২ নম্বরের উত্তরে মূল উত্তরের সাথে ১টি প্রাসঙ্গিক সহায়ক বাক্য যুক্ত করলে পূর্ণ ২ নম্বর নিশ্চিত হয়।</li>
  </ul>

  <h2 class="htbd-academic-heading" id="gap-fill-guide">৫. প্রশ্ন ৩: Gap Filling Without Clues সমাধানের ৫টি কৌশল (Q3 Guide)</h2>
  <p>২য় সিন প্যাসেজ থেকে এই ৫ নম্বরের শূন্যস্থান পূরণ আসে। কোনো অপশন বা বক্স দেওয়া থাকে না। এটি সমাধানের নিয়ম:</p>
  <ul style="line-height:1.85;">
    <li>প্যাসেজ ২ মনোযোগ দিয়ে পড়ে শূন্যস্থানযুক্ত বাক্যটির সাথে প্যাসেজের মূল বাক্যের অর্থ মেলান।</li>
    <li>শূন্যস্থানে Noun, Adjective, Verb না Adverb বসবে—তা ব্যাকরণিক নিয়মে চিহ্নিত করুন। Preposition-এর পর Noun/Gerund এবং Be-verb-এর পর Adjective বা Past Participle বসে।</li>
    <li>একই শূন্যস্থানে একাধিক প্রাসঙ্গিক সমার্থক শব্দ গ্রহণযোগ্য, তবে বানান শতভাগ নির্ভুল হতে হবে।</li>
  </ul>

  <h2 class="htbd-academic-heading" id="seen-solutions">৬. ৩৩টি সিন প্যাসেজ: পূর্ণাঙ্গ টেক্সট, MCQ, প্রশ্নোত্তর ও গ্যাপ ফিলিং সমাধান (All 33 Solution Cards)</h2>
  <p>নিচে ৩৩টি সিন প্যাসেজের প্রতিটি অধ্যায়ের পাঠ্যবইয়ের নির্বাচিত অনুচ্ছেদ, প্রশ্ন ১-এর মডেল MCQ, প্রশ্ন ২-এর অ্যানালিটিক্যাল প্রশ্নোত্তর এবং প্রশ্ন ৩-এর গ্যাপ ফিলিং মডেল এক্সারসাইজ ও সঠিক উত্তর দেওয়া হলো। প্রতিটি কার্ডের উপরে ও নিচে সিন প্যাসেজ সূচিতে ফিরে যাওয়ার বাটন সংযুক্ত রয়েছে:</p>

  {seen_cards_html}

  <h2 class="htbd-academic-heading" id="model-dakhil">৭. মডেল পরীক্ষা ০১: দাখিল ২০২৬ বোর্ড প্রশ্ন ও পূর্ণাঙ্গ সমাধান (Zahir Raihan)</h2>
  <p style="background:#f1f5f9; padding:16px 20px; border-radius:6px; font-style:italic; line-height:1.8;">
    "{DAKHIL_2026_SEEN['passage']}"
  </p>

  <h3 class="htbd-academic-subheading">Question 1: Multiple Choice Questions (7 Marks)</h3>
  {dakhil_mcqs}

  <h3 class="htbd-academic-subheading">Question 2: Answering Questions (10 Marks)</h3>
  {dakhil_qas}

  <h3 class="htbd-academic-subheading">Question 3: Gap Filling Without Clues (5 Marks)</h3>
  <p style="background:#f8fafc; padding:14px 18px; border-radius:6px; line-height:1.85;">{DAKHIL_2026_SEEN['gap_fill']['text']}</p>
  <p style="background:#f0fdf4; border:1px solid #bbf7d0; padding:12px 16px; border-radius:6px; color:#14532d;">
    <strong>সঠিক উত্তর:</strong> {dakhil_gaps}
  </p>

  <h2 class="htbd-academic-heading" id="model-exclusive">৮. মডেল পরীক্ষা ০২: এক্সক্লুসিভ মডেল টেস্ট ও পূর্ণাঙ্গ সমাধান (Climate Change)</h2>
  <p style="background:#f1f5f9; padding:16px 20px; border-radius:6px; font-style:italic; line-height:1.8;">
    "{MODEL_TEST_SEEN['passage']}"
  </p>

  <h3 class="htbd-academic-subheading">Question 1: Multiple Choice Questions (7 Marks)</h3>
  {model_mcqs}

  <h3 class="htbd-academic-subheading">Question 2: Answering Questions (10 Marks)</h3>
  {model_qas}

  <h3 class="htbd-academic-subheading">Question 3: Gap Filling Without Clues (5 Marks)</h3>
  <p style="background:#f8fafc; padding:14px 18px; border-radius:6px; line-height:1.85;">{MODEL_TEST_SEEN['gap_fill']['text']}</p>
  <p style="background:#f0fdf4; border:1px solid #bbf7d0; padding:12px 16px; border-radius:6px; color:#14532d;">
    <strong>সঠিক উত্তর:</strong> {model_gaps}
  </p>

  <h2 class="htbd-academic-heading" id="faq">৯. সচরাচর জিজ্ঞাসা (FAQ)</h2>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">প্রশ্ন ১: এসএসসি ২০২৭ ইংরেজি ১ম পত্রে সিন প্যাসেজে কত নম্বর বরাদ্দ থাকে?</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">উত্তর: সিন প্যাসেজ থেকে মোট ২২ নম্বর বরাদ্দ থাকে—প্রশ্ন ১ (MCQ - ৭ নম্বর), প্রশ্ন ২ (Open-Ended প্রশ্নোত্তর - ১০ নম্বর) এবং প্রশ্ন ৩ (Gap Filling Without Clues - ৫ নম্বর)।</p>
  </div>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">প্রশ্ন ২: সিন প্যাসেজ থেকে কি হুবহু লাইন তুলে উত্তর দেওয়া যাবে?</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">উত্তর: না, হুবহু লাইন তুলে দিলে পরীক্ষক নম্বর কমিয়ে দেন। প্যাসেজ থেকে মূল তথ্য সংগ্রহ করে নিজের ভাষায় বাক্য গঠন করে উত্তর লিখতে হবে।</p>
  </div>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">প্রশ্ন ৩: Gap Filling Without Clues-এ কি পুরো বাক্য লিখতে হবে?</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">উত্তর: শুধু ক্রমিক নম্বর দিয়ে (a), (b), (c), (d), (e) এর সঠিক শব্দ লিখলেই চলে। তবে পুরো বাক্য তুলে শূন্যস্থানের নিচে দাগ দিয়ে লিখলে খাতার মান আকর্ষণীয় হয়।</p>
  </div>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">প্রশ্ন ৪: MCQ-তে সর্বোচ্চ নম্বর নিশ্চিত করার উপায় কী?</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">উত্তর: শব্দার্থ ও সিনোনিম-অ্যান্টোনিম প্যাসেজের কনটেক্সট অনুসারে যাচাই করতে হবে। খাতায় লেখার সময় অপশন নম্বর ও সঠিক উত্তর উভয়ই লিখবেন (যেমন: (a) (ii) Carbon dioxide)।</p>
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
    {{"@type": "Question", "name": "How is marks distributed in SSC 2027 English 1st Paper Seen Passage?", "acceptedAnswer": {{"@type": "Answer", "text": "Total 22 marks are allocated: Question 1 Multiple Choice Questions (7 marks), Question 2 Open-Ended Answering Questions (10 marks), and Question 3 Gap Filling Without Clues (5 marks)."}}}},
    {{"@type": "Question", "name": "Should I copy sentences directly from the seen passage in Q2?", "acceptedAnswer": {{"@type": "Answer", "text": "No, copying sentences directly will lead to mark deductions. Always extract information and write in your own words with proper grammatical tense."}}}},
    {{"@type": "Question", "name": "Do I need to write full sentences in Q3 Gap Filling Without Clues?", "acceptedAnswer": {{"@type": "Answer", "text": "Writing just the answers beside (a) through (e) is acceptable, but writing full sentences with the filled word underlined is considered best practice."}}}},
    {{"@type": "Question", "name": "How to answer MCQ questions in Q1 properly?", "acceptedAnswer": {{"@type": "Answer", "text": "Always write both the Roman numeral or option letter and the exact text answer, e.g., (a) (ii) Carbon dioxide, to make evaluation clear for examiners."}}}}
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
