#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/pdf_to_post/silo_04_builder.py
-------------------------------------
Generates Silo Post 04: Literature - Poems (Q8) & Stories (Q9).
Includes:
1. Master Poem Index (#poem-index) with all 7 Poems and Jump-Links (#poem-01 to #poem-07)
2. Master Story Index (#story-lit-index) with all 23 Stories and Jump-Links (#story-lit-01 to #story-lit-23)
3. Full themes, poetic devices, memorable lines, and Q/A for all 7 Poems
4. Full themes, characters, plot climaxes, and Q/A for all 23 Stories
5. Dakhil 2026 Board Exam (16 Q/As) & Exclusive Model Test (16 Q/As)
6. Smooth scrolling, :target golden highlight, and Schema.org FAQPage microdata
"""

import json
from data_ssc_2027_literature_full import POEMS_FULL_7, STORIES_FULL_23
from data_ssc_2027_literature import (
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
    meta_desc = "SSC 2027 English Poems & Stories Suggestion। প্রশ্ন ৮ ও ৯ (কবিতা ও গল্প) এর ৭টি কবিতা ও ২৩টি গল্পের মাস্টার সূচি ও পূর্ণাঙ্গ প্রশ্নোত্তর সমাধান।"
    banner_url = f"{CDN_BASE}/ssc_2027_silo_04_poems_stories.webp?v=2"
    banner_alt = "SSC 2027 English Poems and Stories Question Answer Suggestion"
    url = f"{BLOG_BASE}/{slug}.html"
    series_nav = get_series_nav("Part 04")

    # 1. Render 7 Poems Master Index & Cards
    poem_index_rows = ""
    poem_html = ""
    for item in POEMS_FULL_7:
        p_id = f"poem-{item['id']:02d}"
        star_color = "#b91c1c" if item["stars"] == "***" else "#c2410c"
        poem_index_rows += f"""<tr>
          <td style="text-align:center; font-weight:700;">{item['id']:02d}</td>
          <td style="text-align:center; font-weight:700; color:{star_color}; font-size:16px;">{item['stars']}</td>
          <td><a href="#{p_id}" style="color:#0c2340; font-weight:600; text-decoration:none;">{item['title']}</a><br><span style="font-size:13px; color:#64748b;">কবি: {item['poet']}</span></td>
          <td style="font-size:13.5px; color:#475569;">{item['theme'][:85]}...</td>
          <td style="text-align:center;"><a href="#{p_id}" class="htbd-jump-pill">কবিতা ও প্রশ্নোত্তর দেখুন</a></td>
        </tr>\n"""

        # Build QA items
        qa_html = ""
        for q_idx, qa in enumerate(item["qa_list"], 1):
            qa_html += f"""<div style="background:#f8fafc; border-left:3px solid #16a34a; padding:12px 16px; border-radius:4px; margin-bottom:12px;">
              <p style="margin:0 0 6px 0; font-weight:700; color:#166534; font-size:15.5px;">প্রশ্ন {q_idx}: {qa['q']}</p>
              <p style="margin:0; color:#1e293b; font-size:16px; line-height:1.75;"><strong>উত্তর (Answer):</strong> {qa['a']}</p>
            </div>\n"""

        poem_html += f"""<div id="{p_id}" class="htbd-qa-card" style="background:#ffffff; border:1px solid #e2e8f0; border-left:4px solid #0c2340; border-radius:8px; padding:20px 22px; margin-bottom:26px; box-shadow:0 2px 5px rgba(0,0,0,0.04); scroll-margin-top:80px;">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:10px; margin-bottom:8px;">
            <h3 style="margin:0; color:#0c2340; font-size:18.5px; font-weight:700;">Poem {item['id']:02d}: {item['title']} &mdash; {item['poet']}</h3>
            <a href="#poem-index" class="htbd-back-btn" title="উপরে কবিতা সূচিতে ফিরে যান">↑ কবিতা সূচি</a>
          </div>
          <p style="margin:0 0 10px 0; font-size:14px; color:#64748b;"><strong>রেটিং:</strong> <span style="color:{star_color}; font-weight:700;">{item['stars']}</span> &bull; <strong style="color:{star_color};">{item['priority']}</strong></p>
          
          <div style="background:#f1f5f9; border-left:3px solid #0284c7; padding:12px 16px; border-radius:4px; margin-bottom:14px;">
            <p style="margin:0 0 6px 0; font-weight:700; color:#0369a1; font-size:14.5px;">মূল পঙ্ক্তি ও উদ্ধৃতি (Key Stanza / Memorable Lines):</p>
            <p style="margin:0; font-style:italic; line-height:1.75; color:#334155; font-size:15.5px;">"{item['key_lines']}"</p>
          </div>

          <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin-bottom:14px;">
            <p style="margin:0 0 6px 0; font-size:15px; color:#1e293b;"><strong>কেন্দ্রীয় থিম (Central Theme):</strong> {item['theme']}</p>
            <p style="margin:0; font-size:15px; color:#475569;"><strong>কাব্যিক অলঙ্কার ও চিত্রকল্প (Poetic Devices &amp; Imagery):</strong> {item['devices']}</p>
          </div>

          <div style="margin-top:14px;">
            <p style="margin:0 0 10px 0; font-weight:700; color:#0c2340; font-size:16px;">বোর্ড স্ট্যান্ডার্ড গুরুত্বপূর্ণ প্রশ্নোত্তর (Question 8 Model Q/A):</p>
            {qa_html}
          </div>

          <div style="text-align:right;">
            <a href="#poem-index" class="htbd-back-text-link">↑ উপরে কবিতা সূচিতে ফিরুন</a>
          </div>
        </div>\n"""

    poem_master_index = f"""<div id="poem-index" class="htbd-master-index-card">
      <h3 style="margin:0 0 8px 0; color:#0c2340; font-size:19px; font-weight:700;">৭টি কবিতার মাস্টার সূচি ও প্রশ্নোত্তর জাম্প-লিংক (Question 8 Navigation)</h3>
      <p style="margin:0 0 16px 0; font-size:15px; color:#475569;">নিচের যেকোনো কবিতার শিরোনাম বা "কবিতা ও প্রশ্নোত্তর দেখুন" বাটনে ক্লিক করে সরাসরি তার থিম, অলঙ্কার ও প্রশ্নোত্তরে জাম্প করুন:</p>
      <div style="overflow-x:auto; -webkit-overflow-scrolling:touch;">
        <table class="htbd-academic-table" style="font-size:15px; margin:0;">
          <thead>
            <tr>
              <th style="width:45px; text-align:center;">নং</th>
              <th style="width:55px; text-align:center;">স্টার</th>
              <th>কবিতার শিরোনাম ও কবি</th>
              <th style="width:38%;">কেন্দ্রীয় ভাব ও থিম</th>
              <th style="width:145px; text-align:center;">সরাসরি প্রশ্নোত্তর</th>
            </tr>
          </thead>
          <tbody>
            {poem_index_rows}
          </tbody>
        </table>
      </div>
    </div>"""

    # 2. Render 23 Stories Master Index & Cards
    story_index_rows = ""
    story_html = ""
    for item in STORIES_FULL_23:
        s_id = f"story-lit-{item['id']:02d}"
        star_color = "#b91c1c" if item["stars"] == "***" else ("#c2410c" if item["stars"] == "**" else "#4b5563")
        story_index_rows += f"""<tr>
          <td style="text-align:center; font-weight:700;">{item['id']:02d}</td>
          <td style="text-align:center; font-weight:700; color:{star_color}; font-size:16px;">{item['stars']}</td>
          <td><a href="#{s_id}" style="color:#0369a1; font-weight:600; text-decoration:none;">{item['title']}</a><br><span style="font-size:13px; color:#64748b;">লেখক: {item['author']}</span></td>
          <td style="font-size:13.5px; color:#475569;">{item['theme'][:85]}...</td>
          <td style="text-align:center;"><a href="#{s_id}" class="htbd-jump-pill" style="background:#e0f2fe; color:#0369a1; border-color:#bae6fd;">গল্প ও প্রশ্নোত্তর দেখুন</a></td>
        </tr>\n"""

        # Build QA items
        qa_html = ""
        for q_idx, qa in enumerate(item["qa_list"], 1):
            qa_html += f"""<div style="background:#f8fafc; border-left:3px solid #0284c7; padding:12px 16px; border-radius:4px; margin-bottom:12px;">
              <p style="margin:0 0 6px 0; font-weight:700; color:#0369a1; font-size:15.5px;">প্রশ্ন {q_idx}: {qa['q']}</p>
              <p style="margin:0; color:#1e293b; font-size:16px; line-height:1.75;"><strong>উত্তর (Answer):</strong> {qa['a']}</p>
            </div>\n"""

        story_html += f"""<div id="{s_id}" class="htbd-qa-card" style="background:#ffffff; border:1px solid #e2e8f0; border-left:4px solid #0369a1; border-radius:8px; padding:20px 22px; margin-bottom:26px; box-shadow:0 2px 5px rgba(0,0,0,0.04); scroll-margin-top:80px;">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:10px; margin-bottom:8px;">
            <h3 style="margin:0; color:#0369a1; font-size:18.5px; font-weight:700;">Story {item['id']:02d}: {item['title']} &mdash; {item['author']}</h3>
            <a href="#story-lit-index" class="htbd-back-btn" title="উপরে গল্প সূচিতে ফিরে যান">↑ গল্প সূচি</a>
          </div>
          <p style="margin:0 0 10px 0; font-size:14px; color:#64748b;"><strong>রেটিং:</strong> <span style="color:{star_color}; font-weight:700;">{item['stars']}</span> &bull; <strong style="color:{star_color};">{item['priority']}</strong></p>

          <div style="background:#f8fafc; border:1px solid #e2e8f0; padding:12px 16px; border-radius:6px; margin-bottom:14px;">
            <p style="margin:0 0 6px 0; font-size:15px; color:#1e293b;"><strong>প্রধান চরিত্রসমূহ (Key Characters):</strong> {item['characters']}</p>
            <p style="margin:0 0 6px 0; font-size:15px; color:#1e293b;"><strong>মূল বিষয়বস্তু (Core Theme):</strong> {item['theme']}</p>
            <p style="margin:0; font-size:15px; color:#475569;"><strong>কাহিনীর সারসংক্ষেপ ও ক্লাইম্যাক্স (Plot Climax):</strong> {item['plot_climax']}</p>
          </div>

          <div style="margin-top:14px;">
            <p style="margin:0 0 10px 0; font-weight:700; color:#0369a1; font-size:16px;">বোর্ড স্ট্যান্ডার্ড গুরুত্বপূর্ণ প্রশ্নোত্তর (Question 9 Model Q/A):</p>
            {qa_html}
          </div>

          <div style="text-align:right;">
            <a href="#story-lit-index" class="htbd-back-text-link">↑ উপরে গল্প সূচিতে ফিরুন</a>
          </div>
        </div>\n"""

    story_master_index = f"""<div id="story-lit-index" class="htbd-master-index-card" style="border-left-color:#0284c7;">
      <h3 style="margin:0 0 8px 0; color:#0284c7; font-size:19px; font-weight:700;">২৩টি গল্পের মাস্টার সূচি ও প্রশ্নোত্তর জাম্প-লিংক (Question 9 Navigation)</h3>
      <p style="margin:0 0 16px 0; font-size:15px; color:#475569;">নিচের যেকোনো গল্পের শিরোনাম বা "গল্প ও প্রশ্নোত্তর দেখুন" বাটনে ক্লিক করে সরাসরি তার চরিত্র বিশ্লেষণ ও প্রশ্নোত্তরে জাম্প করুন:</p>
      <div style="overflow-x:auto; -webkit-overflow-scrolling:touch;">
        <table class="htbd-academic-table" style="font-size:15px; margin:0;">
          <thead>
            <tr>
              <th style="width:45px; text-align:center;">নং</th>
              <th style="width:55px; text-align:center;">স্টার</th>
              <th>গল্পের শিরোনাম ও লেখক</th>
              <th style="width:38%;">মূল বিষয়বস্তু ও প্রেক্ষাপট</th>
              <th style="width:145px; text-align:center;">সরাসরি প্রশ্নোত্তর</th>
            </tr>
          </thead>
          <tbody>
            {story_index_rows}
          </tbody>
        </table>
      </div>
    </div>"""

    # 3. Render Dakhil 2026 & Model Test Sections
    dakhil_p_qa = "".join([f"""<div style="margin-bottom:12px; background:#f8fafc; padding:12px 16px; border-radius:6px; border-left:3px solid #0c2340;">
      <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:15.5px;">{q['q_num']}: {q['question']}</p>
      <p style="margin:0; color:#1e293b; font-size:16px; line-height:1.75;"><strong>উত্তর:</strong> {q['answer']}</p>
    </div>\n""" for q in DAKHIL_2026_POEMS_QA])

    dakhil_s_qa = "".join([f"""<div style="margin-bottom:12px; background:#f8fafc; padding:12px 16px; border-radius:6px; border-left:3px solid #0369a1;">
      <p style="margin:0 0 6px 0; font-weight:700; color:#0369a1; font-size:15.5px;">{q['q_num']}: {q['question']}</p>
      <p style="margin:0; color:#1e293b; font-size:16px; line-height:1.75;"><strong>উত্তর:</strong> {q['answer']}</p>
    </div>\n""" for q in DAKHIL_2026_STORIES_QA])

    model_p_qa = "".join([f"""<div style="margin-bottom:12px; background:#f8fafc; padding:12px 16px; border-radius:6px; border-left:3px solid #0c2340;">
      <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:15.5px;">{q['q_num']}: {q['question']}</p>
      <p style="margin:0; color:#1e293b; font-size:16px; line-height:1.75;"><strong>উত্তর:</strong> {q['answer']}</p>
    </div>\n""" for q in MODEL_TEST_POEMS_QA])

    model_s_qa = "".join([f"""<div style="margin-bottom:12px; background:#f8fafc; padding:12px 16px; border-radius:6px; border-left:3px solid #0369a1;">
      <p style="margin:0 0 6px 0; font-weight:700; color:#0369a1; font-size:15.5px;">{q['q_num']}: {q['question']}</p>
      <p style="margin:0; color:#1e293b; font-size:16px; line-height:1.75;"><strong>উত্তর:</strong> {q['answer']}</p>
    </div>\n""" for q in MODEL_TEST_STORIES_QA])

    # 4. Assemble HTML
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
    <figcaption style="font-size: 14px; color: #64748b; text-align: center; margin-top: 6px;">SSC 2027 English 1st Paper Literature Part (Poems &amp; Stories Q8-9) &mdash; Part 04 of the Study Silo Series</figcaption>
  </figure>

  <div class="htbd-overview-box">
    <p style="margin: 0 0 10px 0; font-size: 16px; color: #1e3a8a; font-weight: 700;">টপিক ও ফোকাস: SSC 2027 English Poems &amp; Stories Suggestion (Questions 8, 9)</p>
    <p>ইংরেজি ১ম পত্রে সাহিত্য বা লিটারেচার অংশের <strong>১৬ নম্বর</strong> অত্যন্ত গুরুত্বপূর্ণ। এই <strong>SSC 2027 English Poems &amp; Stories Suggestion</strong> নির্দেশিকায় রয়েছে <strong>Question 8: Answering Questions from Poems (8 Marks)</strong> এবং <strong>Question 9: Answering Questions from Stories (8 Marks)</strong> এর পূর্ণাঙ্গ রূপরেখা। জাতীয় শিক্ষাক্রম ও বোর্ড প্রশ্নোত্তরের ভিত্তিতে ৭টি কবিতা ও ২৩টি বিখ্যাত গল্পের স্টার রেটিং, থিম, কাব্যিক অলঙ্কার ও চরিত্র বিশ্লেষণসহ বোর্ড স্ট্যান্ডার্ড সকল প্রশ্নোত্তরের মাস্টার নেভিগেশন সূচি ও লাইভ সলিউশন এখানে তুলে ধরা হলো।</p>
  </div>

<!--more-->

  <div class="htbd-toc-card">
    <p class="toc-title">বিষয়সূচি (Table of Contents)</p>
    <ul>
      <li><a href="#lit-marks">১. সাহিত্য অংশ: নম্বর বণ্টন ও সিলেবাস রূপরেখা (Marks Distribution)</a></li>
      <li><a href="#poem-index">২. ৭টি কবিতার মাস্টার সূচি ও জাম্প-লিংক (Master Poem Index)</a></li>
      <li><a href="#story-lit-index">৩. ২৩টি গল্পের মাস্টার সূচি ও জাম্প-লিংক (Master Story Index)</a></li>
      <li><a href="#lit-rules">৪. কবিতা ও গল্পে পূর্ণ ১৬ নম্বর পাওয়ার ৪টি পেশাদার কৌশল (Answering Strategies)</a></li>
      <li><a href="#all-poems-cards">৫. ৭টি কবিতার পূর্ণাঙ্গ থিম, অলঙ্কার ও বোর্ড প্রশ্নোত্তর সমাধান (All 7 Poems Solved)</a></li>
      <li><a href="#all-stories-cards">৬. ২৩টি গল্পের মূলভাব, চরিত্র ও বিশ্লেষণধর্মী প্রশ্নোত্তর সমাধান (All 23 Stories Solved)</a></li>
      <li><a href="#dakhil-solutions">৭. দাখিল বোর্ড পরীক্ষা ২০২৬: কবিতা ও গল্প সমাধান (Dakhil 2026 Board Solutions)</a></li>
      <li><a href="#model-solutions">৮. এক্সক্লুসিভ মডেল টেস্ট: কবিতা ও গল্প সমাধান (Model Test Solutions)</a></li>
      <li><a href="#faq">৯. সচরাচর জিজ্ঞাসা (FAQ)</a></li>
    </ul>
  </div>

  <h2 class="htbd-academic-heading" id="lit-marks">১. সাহিত্য অংশ: নম্বর বণ্টন ও সিলেবাস রূপরেখা (Marks Distribution)</h2>
  <p>ইংরেজি ১ম পত্রের সাহিত্য অংশে মোট ১৬ নম্বর বরাদ্দ থাকে, যার রূপরেখা নিম্নরূপ:</p>

  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 22px 0;">
    <table class="htbd-academic-table">
      <thead>
        <tr>
          <th>প্রশ্ন নম্বর</th>
          <th>আইটেমের নাম (Item Name)</th>
          <th>প্রশ্নের ধরন ও মূল্যায়ন (Question Pattern)</th>
          <th>নম্বর (Marks)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>প্রশ্ন ৮ (Q8)</strong></td>
          <td>Answering Questions from Poems</td>
          <td>কবিতা থেকে ৪টি সংক্ষিপ্ত ব্যাখ্যামূলক ও থিমভিত্তিক প্রশ্ন (৪ × ২ নম্বর)</td>
          <td><strong>৮ নম্বর</strong></td>
        </tr>
        <tr>
          <td><strong>প্রশ্ন ৯ (Q9)</strong></td>
          <td>Answering Questions from Stories</td>
          <td>গল্প ও নাটকের কাহিনী, চরিত্র ও ক্লাইম্যাক্স থেকে ৪টি প্রশ্ন (৪ × ২ নম্বর)</td>
          <td><strong>৮ নম্বর</strong></td>
        </tr>
        <tr>
          <td colspan="3" style="text-align:right; font-weight:700; background:#f1f5f9;">মোট সাহিত্য নম্বর (Total Literature Marks):</td>
          <td style="font-weight:700; background:#f1f5f9; color:#0c2340;"><strong>১৬ নম্বর</strong></td>
        </tr>
      </tbody>
    </table>
  </div>

  {poem_master_index}

  {story_master_index}

  <h2 class="htbd-academic-heading" id="lit-rules">৪. কবিতা ও গল্পে পূর্ণ ১৬ নম্বর পাওয়ার ৪টি পেশাদার কৌশল (Answering Strategies)</h2>
  <ul style="line-height:1.85;">
    <li><strong>সরাসরি টু-দ্য-পয়েন্ট উত্তর (Direct &amp; Concise Answers):</strong> প্রতিটি প্রশ্নের মান ২ নম্বর। অপ্রাসঙ্গিক ভূমিকা না লিখে প্রথম বাক্যেই প্রশ্নের মূল উত্তরটি দিন এবং পরের ১–২ বাক্যে কবিতার পঙ্ক্তি বা গল্পের ঘটনার রেফারেন্স দিয়ে ব্যাখ্যা করুন।</li>
    <li><strong>কাব্যিক অলঙ্কারের নাম উল্লেখ (Poetic Devices Citation):</strong> কবিতার উত্তরে রূপক (Metaphor), উপমা (Simile) বা মানবারোপ (Personification) থাকলে তা উল্লেখ করুন। যেমন: 'Time' কবিতায় কবি সময়কে 'old gipsy man' হিসেবে Personify করেছেন।</li>
    <li><strong>চরিত্রের মনস্তাত্ত্বিক গভীরতা (Character Depth in Stories):</strong> গল্পের প্রশ্নের ক্ষেত্রে চরিত্রের ভালো-মন্দ দিক ও নৈতিক সিদ্ধান্ত পরিষ্কারভাবে ফুটিয়ে তুলুন (যেমন: Portia-এর প্রজ্ঞা বা Antonio-এর নিঃস্বার্থ বন্ধুত্ব)।</li>
    <li><strong>যথাযথ টেন্স ও গ্রামার শুদ্ধতা (Grammatical Accuracy):</strong> প্রশ্ন যে টেন্সে থাকবে (Past Tense বা Present Tense), উত্তর অবশ্যই সেই একই টেন্সে লিখতে হবে। ভুল টেন্স ব্যবহার করলে নম্বর কাটা যায়।</li>
  </ul>

  <h2 class="htbd-academic-heading" id="all-poems-cards">৫. ৭টি কবিতার পূর্ণাঙ্গ থিম, অলঙ্কার ও বোর্ড প্রশ্নোত্তর সমাধান (All 7 Poems Solved)</h2>
  <p>নিচে জাতীয় পাঠ্যক্রমের ৭টি কবিতার কেন্দ্রীয় থিম, স্মরণীয় পঙ্ক্তি, কাব্যিক অলঙ্কার এবং সম্ভাব্য বোর্ড প্রশ্নোত্তর ক্রমানুসারে দেওয়া হলো:</p>

  {poem_html}

  <h2 class="htbd-academic-heading" id="all-stories-cards">৬. ২৩টি গল্পের মূলভাব, চরিত্র ও বিশ্লেষণধর্মী প্রশ্নোত্তর সমাধান (All 23 Stories Solved)</h2>
  <p>নিচে সিলেবাসভুক্ত ২৩টি বিশ্বখ্যাত গল্প ও নাটকের প্রধান চরিত্র, মূল প্রেক্ষাপট, কাহিনীর ক্লাইম্যাক্স এবং গুরুত্বপূর্ণ বোর্ড প্রশ্নোত্তরের রূপরেখা দেওয়া হলো:</p>

  {story_html}

  <h2 class="htbd-academic-heading" id="dakhil-solutions">৭. দাখিল বোর্ড পরীক্ষা ২০২৬: কবিতা ও গল্প সমাধান (Dakhil 2026 Board Solutions)</h2>
  <p>বিগত দাখিল ২০২৬ বোর্ড পরীক্ষায় আসা কবিতা ও গল্পের পূর্ণাঙ্গ ১৬টি প্রশ্নোত্তর নিচে হুবহু তুলে ধরা হলো:</p>

  <h3 class="htbd-academic-subheading">ক. কবিতা অংশ (Question 8: 8 Questions &amp; Answers)</h3>
  {dakhil_p_qa}

  <h3 class="htbd-academic-subheading">খ. গল্প অংশ (Question 9: 8 Questions &amp; Answers)</h3>
  {dakhil_s_qa}

  <h2 class="htbd-academic-heading" id="model-solutions">৮. এক্সক্লুসিভ মডেল টেস্ট: কবিতা ও গল্প সমাধান (Model Test Solutions)</h2>
  <p>বোর্ড স্ট্যান্ডার্ড এক্সক্লুসিভ মডেল টেস্টের ১৬টি নির্বাচিত প্রশ্ন ও আদর্শ উত্তরমালা:</p>

  <h3 class="htbd-academic-subheading">ক. কবিতা অংশ (Question 8: 8 Questions &amp; Answers)</h3>
  {model_p_qa}

  <h3 class="htbd-academic-subheading">খ. গল্প অংশ (Question 9: 8 Questions &amp; Answers)</h3>
  {model_s_qa}

  <h2 class="htbd-academic-heading" id="faq">৯. সচরাচর জিজ্ঞাসা (FAQ)</h2>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">Question 1: কবিতার উত্তরে কি কবিতার হুবহু লাইন উদ্ধৃত করা যাবে?</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">উত্তর: হ্যাঁ, তবে শুধু লাইন তুলে দিলে হবে না। নিজের ভাষায় উত্তর লিখে তার সমর্থনে কবিতার গুরুত্বপূর্ণ পঙ্ক্তি কোটেশন চিহ্নের মধ্যে উল্লেখ করলে সর্বোচ্চ নম্বর পাওয়া যায়।</p>
  </div>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">Question 2: গল্পের উত্তরে কত বাক্য লেখা আদর্শ?</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">উত্তর: প্রতিটি ২ নম্বরের প্রশ্নের জন্য ২ থেকে ৩টি পূর্ণাঙ্গ, ব্যাকরণগতভাবে নির্ভুল ও তথ্যবহুল বাক্য লেখা সবচেয়ে আদর্শ।</p>
  </div>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">Question 3: পরীক্ষায় কোন কবিতাগুলো সবচেয়ে বেশি গুরুত্বপূর্ণ?</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">উত্তর: এসএসসি ২০২৭ এর জন্য ৩-স্টার চিহ্নিত ৩টি কবিতা সবচেয়ে বেশি গুরুত্বপূর্ণ: 'Time, You Old Gipsy Man', 'Stopping by Woods on a Snowy Evening' এবং 'O Me! O Life!'।</p>
  </div>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">Question 4: গল্প অংশে কোন গল্পগুলো টপ প্রায়োরিটি?</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">উত্তর: 'The Merchant of Venice', 'The Story of an Hour', 'The Purple Jar', 'The Gift of the Magi', 'The Last Leaf', 'The Necklace', 'The Luncheon' এবং 'A Mother in Mannville'—এই গল্পগুলো ৩-স্টার প্রায়োরিটিভুক্ত।</p>
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
    {{"@type": "Question", "name": "What is the main theme of 'Time, You Old Gipsy Man'?", "acceptedAnswer": {{"@type": "Answer", "text": "The relentless, irreversible flight of Time and humanity's yearning to pause its passage to cherish precious moments."}}}},
    {{"@type": "Question", "name": "Why did the speaker pause near the woods in 'Stopping by Woods on a Snowy Evening'?", "acceptedAnswer": {{"@type": "Answer", "text": "To watch the snow falling quietly and admire the peaceful, dark, and deep forest scenery before continuing his journey to keep his promises."}}}},
    {{"@type": "Question", "name": "How did Portia save Antonio's life in 'The Merchant of Venice'?", "acceptedAnswer": {{"@type": "Answer", "text": "Portia granted Shylock his pound of flesh under the strict condition that if he shed a single drop of Christian blood, all his wealth and life would be forfeited to Venice."}}}},
    {{"@type": "Question", "name": "Why did Mrs. Mallard feel joy before dying in 'The Story of an Hour'?", "acceptedAnswer": {{"@type": "Answer", "text": "She realized that she had achieved exhilarating personal freedom and autonomy to live exclusively for herself without marital subjugation."}}}},
    {{"@type": "Question", "name": "What did Rosamond learn from buying 'The Purple Jar'?", "acceptedAnswer": {{"@type": "Answer", "text": "She learned the bitter consequence of prioritizing superficial, glittering vanity over practical necessity, walking in ripped shoes while the jar was merely colored water."}}}},
    {{"@type": "Question", "name": "Why are Jim and Della called the wisest of magi in 'The Gift of the Magi'?", "acceptedAnswer": {{"@type": "Answer", "text": "Because they sacrificed their most sacred earthly treasures out of pure, unconditional love for each other."}}}},
    {{"@type": "Question", "name": "Why is Behrman's last leaf considered a masterpiece?", "acceptedAnswer": {{"@type": "Answer", "text": "Because he sacrificed his own life in a freezing blizzard to paint a life-saving leaf that restored Johnsy's will to survive pneumonia."}}}},
    {{"@type": "Question", "name": "What is the tragic irony of 'The Necklace'?", "acceptedAnswer": {{"@type": "Answer", "text": "The Loisels endured ten years of crushing, ruinous debt to replace a diamond necklace that was actually cheap paste worth only 500 francs."}}}}
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
