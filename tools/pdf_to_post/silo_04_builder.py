#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/pdf_to_post/silo_04_builder.py
-------------------------------------
Generates Silo Post 04: Literature - Poems (Q8) & Stories (Q9).
Includes all 7 Poems + all 23 Stories + Dakhil 2026 Q8/9 (16 Q/As) + Model Test Q8/9 (16 Q/As).
"""

import json
from data_ssc_2027_literature import (
    POEMS_7_RATINGS,
    STORIES_23_RATINGS,
    DAKHIL_2026_POEMS_QA,
    DAKHIL_2026_STORIES_QA,
    MODEL_TEST_POEMS_QA,
    MODEL_TEST_STORIES_QA
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

def build_post():
    slug = "ssc-2027-english-poems-stories-question"
    title = "SSC 2027 English Poems & Stories Suggestion | এসএসসি ইংরেজি কবিতা ও গল্প প্রশ্নোত্তর (Q8-9)"
    meta_desc = "SSC 2027 English Poems & Stories Suggestion। প্রশ্ন ৮ ও ৯ (কবিতা ও গল্প) এর ৭টি কবিতা, ২৩টি গল্প এবং দাখিল ও মডেল টেস্টের ৩২টি পূর্ণাঙ্গ প্রশ্নোত্তর।"
    banner_url = f"{CDN_BASE}/ssc_2027_silo_04_poems_stories.webp"
    banner_alt = "SSC 2027 English Poems and Stories Question Answer Suggestion"
    url = f"{BLOG_BASE}/{slug}.html"
    series_nav = get_series_nav("Part 04")

    # Render 7 Poems Rows
    poems_rows = ""
    for p in POEMS_7_RATINGS:
        star_color = "#b91c1c" if p["stars"] == "***" else "#c2410c"
        poems_rows += f"""<tr>
          <td style="text-align:center; font-weight:700;">{p['id']}</td>
          <td style="text-align:center; font-weight:700; color:{star_color}; font-size:18px;">{p['stars']}</td>
          <td><strong>{p['title']}</strong><br><span style="font-size:13.5px; color:#64748b;">কবি: {p['poet']}</span></td>
          <td>{p['theme']}</td>
          <td>{p['devices']}</td>
        </tr>\n"""

    # Render 23 Stories Rows
    stories_rows = ""
    for s in STORIES_23_RATINGS:
        star_color = "#b91c1c" if s["stars"] == "***" else ("#c2410c" if s["stars"] == "**" else "#4b5563")
        stories_rows += f"""<tr>
          <td style="text-align:center; font-weight:700;">{s['id']}</td>
          <td style="text-align:center; font-weight:700; color:{star_color}; font-size:18px;">{s['stars']}</td>
          <td><strong>{s['title']}</strong><br><span style="font-size:13.5px; color:#64748b;">লেখক: {s['author']}</span></td>
          <td>{s['theme']}</td>
          <td>{s['characters']}</td>
        </tr>\n"""

    # Render Dakhil Q8 (Poems Q/A)
    dakhil_p_qa = ""
    for q in DAKHIL_2026_POEMS_QA:
        dakhil_p_qa += f"""<div style="margin-bottom:14px; background:#f8fafc; padding:12px 16px; border-radius:6px; border-left:4px solid #0c2340;">
          <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340;">{q['q_num']}: {q['question']}</p>
          <p style="margin:0; color:#1e293b; font-size:16px; line-height:1.75;"><strong>উত্তর:</strong> {q['answer']}</p>
        </div>\n"""

    # Render Dakhil Q9 (Stories Q/A)
    dakhil_s_qa = ""
    for q in DAKHIL_2026_STORIES_QA:
        dakhil_s_qa += f"""<div style="margin-bottom:14px; background:#f8fafc; padding:12px 16px; border-radius:6px; border-left:4px solid #0369a1;">
          <p style="margin:0 0 6px 0; font-weight:700; color:#0369a1;">{q['q_num']}: {q['question']}</p>
          <p style="margin:0; color:#1e293b; font-size:16px; line-height:1.75;"><strong>উত্তর:</strong> {q['answer']}</p>
        </div>\n"""

    # Render Model Test Q8 (Poems Q/A)
    model_p_qa = ""
    for q in MODEL_TEST_POEMS_QA:
        model_p_qa += f"""<div style="margin-bottom:14px; background:#f8fafc; padding:12px 16px; border-radius:6px; border-left:4px solid #0c2340;">
          <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340;">{q['q_num']}: {q['question']}</p>
          <p style="margin:0; color:#1e293b; font-size:16px; line-height:1.75;"><strong>উত্তর:</strong> {q['answer']}</p>
        </div>\n"""

    # Render Model Test Q9 (Stories Q/A)
    model_s_qa = ""
    for q in MODEL_TEST_STORIES_QA:
        model_s_qa += f"""<div style="margin-bottom:14px; background:#f8fafc; padding:12px 16px; border-radius:6px; border-left:4px solid #0369a1;">
          <p style="margin:0 0 6px 0; font-weight:700; color:#0369a1;">{q['q_num']}: {q['question']}</p>
          <p style="margin:0; color:#1e293b; font-size:16px; line-height:1.75;"><strong>উত্তর:</strong> {q['answer']}</p>
        </div>\n"""

    html = f"""<style>
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
    font-size: 16px !important;
    border: 1px solid #0c2340 !important;
    text-align: left !important;
  }}
  .htbd-academic-table td {{
    padding: 10px 14px !important;
    border: 1px solid #e2e8f0 !important;
    font-size: 15.5px !important;
    vertical-align: middle !important;
  }}
  .htbd-academic-table tr:nth-child(even) {{
    background: #f8fafc !important;
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
    <figcaption style="font-size: 14px; color: #64748b; text-align: center; margin-top: 6px;">SSC 2027 English 1st Paper Literature (Poems & Stories) — Part 04 of the Study Silo Series</figcaption>
  </figure>

  <div class="htbd-overview-box">
    <p style="margin: 0 0 10px 0; font-size: 16px; color: #1e3a8a; font-weight: 700;">টপিক ও ফোকাস: SSC 2027 English Poems &amp; Stories Suggestion (Questions 8, 9)</p>
    <p>এসএসসি ২০২৭ ইংরেজি ১ম পত্রে সাহিত্যভিত্তিক বোধগম্যতা যাচাইয়ের জন্য <strong>প্রশ্ন ৮ ও ৯</strong> অন্তর্ভুক্ত থাকে। এতে মোট <strong>১৬ নম্বর</strong> বরাদ্দ—প্রশ্ন ৮-এ পাঠ্যবইয়ের কবিতা থেকে ৮টি সংক্ষিপ্ত প্রশ্নোত্তর (Answering Questions from Poems - ৮ নম্বর) এবং প্রশ্ন ৯-এ নির্বাচিত বিশ্বসাহিত্যের ছোটগল্প থেকে ৮টি সংক্ষিপ্ত প্রশ্নোত্তর (Answering Questions from Stories - ৮ নম্বর)। নিচে ৭টি শীর্ষ কবিতা, ২৩টি ক্লাসিক ছোটগল্প এবং বোর্ড ও এক্সক্লুসিভ মডেল টেস্টের ৩২টি পূর্ণাঙ্গ প্রশ্নোত্তর সংযুক্ত করা হলো।</p>
    <p style="margin: 12px 0 0 0; font-size: 15px; background: #e0f2fe; padding: 8px 12px; border-radius: 6px; color: #0369a1; line-height: 1.6;"><strong>টার্গেট সার্চ কিওয়ার্ড (Target Keywords):</strong> SSC 2027 English Poems Suggestion, SSC Stories Question Answer Q8 Q9, Class 10 English Literature Suggestion, SSC English 1st Paper Poems</p>
  </div>

<!--more-->

  <div class="htbd-toc-card">
    <p class="toc-title">বিষয়সূচি (Table of Contents)</p>
    <ul>
      <li><a href="#lit-marks">১. সাহিত্য অংশ: নম্বর বণ্টন ও প্রশ্ন কাঠামো (Marks Distribution)</a></li>
      <li><a href="#poems-analysis">২. ৭টি নির্বাচিত কবিতা: মূলভাব, কাব্যিক অলংকার ও স্টার রেটিং (All 7 Poems)</a></li>
      <li><a href="#stories-analysis">৩. ২৩টি নির্বাচিত ছোটগল্প: প্লট, চরিত্র ও শিক্ষণীয় নীতিকথা (All 23 Stories)</a></li>
      <li><a href="#writing-secrets">৪. সাহিত্যভিত্তিক প্রশ্নে পূর্ণ ৮+৮ নম্বর অর্জনের ৪টি নিয়ম (Answering Strategy)</a></li>
      <li><a href="#model-dakhil">৫. মডেল পরীক্ষা ০১: দাখিল ২০২৬ বোর্ড প্রশ্ন ও পূর্ণাঙ্গ সমাধান (১৬টি প্রশ্নোত্তর)</a></li>
      <li><a href="#model-exclusive">৬. মডেল পরীক্ষা ০২: এক্সক্লুসিভ মডেল টেস্ট ও পূর্ণাঙ্গ সমাধান (১৬টি প্রশ্নোত্তর)</a></li>
      <li><a href="#faq">৭. সচরাচর জিজ্ঞাসা (FAQ)</a></li>
    </ul>
  </div>

  <h2 class="htbd-academic-heading" id="lit-marks">১. সাহিত্য অংশ: নম্বর বণ্টন ও প্রশ্ন কাঠামো (Marks Distribution)</h2>
  <p>সাহিত্য অংশে শিক্ষার্থীদের ইংরেজি সাহিত্যের রসবোধ, রূপক অর্থ অনুধাবন ও চরিত্র বিশ্লেষণের গভীরতা পরীক্ষা করা হয়:</p>

  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 22px 0;">
    <table class="htbd-academic-table">
      <thead>
        <tr>
          <th>প্রশ্ন নম্বর</th>
          <th>সাহিত্যের মাধ্যম (Medium)</th>
          <th>প্রশ্নের ধরন ও সংখ্যা</th>
          <th>নম্বর (Marks)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>প্রশ্ন ৮ (Q8)</strong></td>
          <td>Selected English Poems</td>
          <td>৮টি সংক্ষিপ্ত প্রশ্ন (a থেকে h)</td>
          <td><strong>1 × 8 = 8 নম্বর</strong></td>
        </tr>
        <tr>
          <td><strong>প্রশ্ন ৯ (Q9)</strong></td>
          <td>Selected Classic Short Stories</td>
          <td>৮টি সংক্ষিপ্ত প্রশ্ন (a থেকে h)</td>
          <td><strong>1 × 8 = 8 নম্বর</strong></td>
        </tr>
        <tr>
          <td colspan="3" style="text-align:right; font-weight:700; background:#f1f5f9;">মোট সাহিত্য নম্বর (Total Literature Marks):</td>
          <td style="font-weight:700; background:#f1f5f9; color:#0c2340;"><strong>১৬ নম্বর</strong></td>
        </tr>
      </tbody>
    </table>
  </div>

  <h2 class="htbd-academic-heading" id="poems-analysis">২. ৭টি নির্বাচিত কবিতা: মূলভাব, কাব্যিক অলংকার ও স্টার রেটিং (All 7 Poems for SSC 2027)</h2>
  <p>নিচে পাঠ্যক্রমের ৭টি কবিতার স্টার রেটিং, কবি, অন্তর্নিহিত ভাবার্থ এবং প্রধান আলংকারিক কৌশল (Poetic Devices) তুলনামূলক ছকে সাজানো হলো:</p>

  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 22px 0;">
    <table class="htbd-academic-table">
      <thead>
        <tr>
          <th style="width:6%;">ক্র.</th>
          <th style="width:8%; text-align:center;">স্টার</th>
          <th style="width:24%;">কবিতা ও কবি</th>
          <th style="width:36%;">মূল দর্শন ও থিম (Core Theme)</th>
          <th style="width:26%;">কাব্যিক অলংকার (Poetic Devices)</th>
        </tr>
      </thead>
      <tbody>
        {poems_rows}
      </tbody>
    </table>
  </div>

  <h2 class="htbd-academic-heading" id="stories-analysis">৩. ২৩টি নির্বাচিত ছোটগল্প: প্লট, চরিত্র ও শিক্ষণীয় নীতিকথা (All 23 Stories for SSC 2027)</h2>
  <p>নিচে ২৩টি কালজয়ী ছোটগল্পের স্টারভিত্তিক গুরুত্ব, মূল চরিত্র এবং নৈতিক শিক্ষা তুলে ধরা হলো:</p>

  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 22px 0;">
    <table class="htbd-academic-table">
      <thead>
        <tr>
          <th style="width:6%;">ক্র.</th>
          <th style="width:8%; text-align:center;">স্টার</th>
          <th style="width:24%;">গল্প ও রচয়িতা</th>
          <th style="width:36%;">মূল প্লট ও দর্শন (Theme)</th>
          <th style="width:26%;">মূল চরিত্রসমূহ (Key Characters)</th>
        </tr>
      </thead>
      <tbody>
        {stories_rows}
      </tbody>
    </table>
  </div>

  <h2 class="htbd-academic-heading" id="writing-secrets">৪. সাহিত্যভিত্তিক প্রশ্নে পূর্ণ ৮+৮ নম্বর অর্জনের ৪টি নিয়ম (Answering Strategy)</h2>
  <p>প্রশ্ন ৮ ও ৯-এ প্রতি প্রশ্নে ১ নম্বর নির্ধারিত থাকায় অতিরিক্ত বড় বা অপ্রাসঙ্গিক উত্তর লেখার কোনো প্রয়োজন নেই। নিচের ৪টি নিয়ম মানলে পূর্ণ ১৬ নম্বর পাওয়া সম্ভব:</p>
  <ul style="line-height:1.85;">
    <li><strong>সরাসরি ও প্রাসঙ্গিক উত্তর (Direct Answer):</strong> প্রশ্নের মূল উত্তরটি ১ম বাক্যেই দিয়ে দিন। যেমন: প্রশ্ন যদি হয় "Who is the poet of the poem?", উত্তর সরাসরি লিখবেন "Ralph Hodgson is the poet of the poem 'Time, You Old Gipsy Man'."</li>
    <li><strong>টেনস সঙ্গতি (Tense Consistency):</strong> প্রশ্নে Did থাকলে Past Tense এবং Does থাকলে Present Tense ব্যবহার করুন। সাহিত্যের ভাবার্থ বর্ণনায় সাধারণত Simple Present Tense ব্যবহার করা হয়।</li>
    <li><strong>১ থেকে ২টি পূর্ণাঙ্গ বাক্য:</strong> প্রতিটি প্রশ্নের উত্তর ১ বা সর্বোচ্চ ২টি সুগঠিত বাক্যে শেষ করুন। এক শব্দে উত্তর না লিখে পূর্ণাঙ্গ বাক্যে উত্তর লেখা বোর্ড স্ট্যান্ডার্ড।</li>
    <li><strong>উদ্ধৃতি ও চরিত্র মূল্যায়ন:</strong> গল্পের ক্ষেত্রে চরিত্রের সঠিক নাম ও কবিতার ক্ষেত্রে অন্তর্নিহিত রূপক (Metaphor) এক বাক্যে ব্যাখ্যা করলে উত্তরটি মানসম্মত হয়।</li>
  </ul>

  <h2 class="htbd-academic-heading" id="model-dakhil">৫. মডেল পরীক্ষা ০১: দাখিল ২০২৬ বোর্ড প্রশ্ন ও পূর্ণাঙ্গ সমাধান (১৬টি প্রশ্নোত্তর)</h2>
  
  <h3 class="htbd-academic-subheading">Question 8: Answer the following questions from Poems (1 × 8 = 8 Marks)</h3>
  {dakhil_p_qa}

  <h3 class="htbd-academic-subheading">Question 9: Answer the following questions from Stories (1 × 8 = 8 Marks)</h3>
  {dakhil_s_qa}

  <h2 class="htbd-academic-heading" id="model-exclusive">৬. মডেল পরীক্ষা ০২: এক্সক্লুসিভ মডেল টেস্ট ও পূর্ণাঙ্গ সমাধান (১৬টি প্রশ্নোত্তর)</h2>
  
  <h3 class="htbd-academic-subheading">Question 8: Answer the following questions from Poems (1 × 8 = 8 Marks)</h3>
  {model_p_qa}

  <h3 class="htbd-academic-subheading">Question 9: Answer the following questions from Stories (1 × 8 = 8 Marks)</h3>
  {model_s_qa}

  <h2 class="htbd-academic-heading" id="faq">৭. সচরাচর জিজ্ঞাসা (FAQ)</h2>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">Question 1: প্রশ্ন ৮ ও ৯-এর উত্তরে কত বড় বাক্য লেখা উচিত?</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">উত্তর: যেহেতু প্রতিটি প্রশ্নে ১ নম্বর বরাদ্দ, তাই ১ থেকে সর্বোচ্চ ২টি পূর্ণাঙ্গ ব্যাকরণিক বাক্যে সুনির্দিষ্ট উত্তর লেখাই আদর্শ। অপ্রয়োজনীয় বড় প্যারাগ্রাফ লেখার প্রয়োজন নেই।</p>
  </div>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">Question 2: কবি ও লেখকের নামের বানান ভুল হলে কি নম্বর কাটা যায়?</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">উত্তর: হ্যাঁ, বিখ্যাত সাহিত্যিকদের নামের বানান (যেমন: Ralph Hodgson, Robert Frost, Walt Whitman, Guy de Maupassant) অবশ্যই শতভাগ নির্ভুলভাবে লিখতে হবে। ভুল বানানে নম্বর কাটা হতে পারে।</p>
  </div>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">Question 3: কবিতায় Poetic Devices থেকে কি প্রশ্ন হতে পারে?</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">উত্তর: হ্যাঁ! বিশেষ করে Personification, Metaphor, Alliteration এবং Imagery নিয়ে প্রায়ই প্রশ্ন হয় (যেমন: "How is Time portrayed?"). তাই কবিতার রূপক অর্থ বুঝে রাখা জরুরি।</p>
  </div>

  <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px 24px; margin: 30px 0 20px 0;">
    <h3 style="margin: 0 0 10px 0; font-size: 19px; color: #0c2340; font-weight: 700;">সম্পর্কিত সার্চ টার্মস ও টপিকস (Related Search Keywords)</h3>
    <p style="margin: 0 0 12px 0; font-size: 15px; color: #64748b;">শিক্ষার্থীরা গুগলে এই অধ্যায়ের তথ্য খুঁজতে সাধারণত যেসব কি-ওয়ার্ড ব্যবহার করে থাকে:</p>
    <div style="display: flex; flex-wrap: wrap; gap: 8px;">
      <span style="background: #ffffff; border: 1px solid #cbd5e1; color: #1e3a8a; padding: 5px 12px; border-radius: 20px; font-size: 14.5px; font-weight: 500;">SSC 2027 English Poems Question Answer</span>
      <span style="background: #ffffff; border: 1px solid #cbd5e1; color: #1e3a8a; padding: 5px 12px; border-radius: 20px; font-size: 14.5px; font-weight: 500;">SSC English 1st Paper Stories Suggestion Q8 Q9</span>
      <span style="background: #ffffff; border: 1px solid #cbd5e1; color: #1e3a8a; padding: 5px 12px; border-radius: 20px; font-size: 14.5px; font-weight: 500;">Class 10 English Literature Questions with Answers</span>
      <span style="background: #ffffff; border: 1px solid #cbd5e1; color: #1e3a8a; padding: 5px 12px; border-radius: 20px; font-size: 14.5px; font-weight: 500;">EFT Poems Analysis and Central Idea SSC 2027</span>
      <span style="background: #ffffff; border: 1px solid #cbd5e1; color: #1e3a8a; padding: 5px 12px; border-radius: 20px; font-size: 14.5px; font-weight: 500;">SSC Dakhil English 1st Paper Literature Suggestion</span>
    </div>
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
    {{"@type": "Question", "name": "How long should each answer be for Q8 and Q9 in SSC English?", "acceptedAnswer": {{"@type": "Answer", "text": "Writing 1 or 2 precise, grammatically accurate sentences directly answering the question is optimal for 1 mark each."}}}},
    {{"@type": "Question", "name": "Will spelling mistakes in authors' names be penalized?", "acceptedAnswer": {{"@type": "Answer", "text": "Yes, proper names of renowned poets and authors must be spelled accurately without error."}}}},
    {{"@type": "Question", "name": "Do board questions cover figurative language in poems?", "acceptedAnswer": {{"@type": "Answer", "text": "Yes, literary devices like personification, imagery, and symbolism are frequently tested in Q8."}}}}
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
    print(f"Silo 04 generated successfully! Length: {len(html)} chars, Slug: {slug}")
