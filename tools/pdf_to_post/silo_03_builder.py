#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/pdf_to_post/silo_03_builder.py
-------------------------------------
Generates Silo Post 03: Sentence Matching Table (Q6) & Re-arranging Sentences (Q7).
Includes all 32 Matching Tables + all 36 Re-arrange Items + Dakhil 2026 & Model Test.
"""

import json
from data_ssc_2027_matching_rearrange import (
    MATCHING_TABLES_32,
    REARRANGE_ITEMS_36,
    DAKHIL_2026_MATCHING,
    DAKHIL_2026_REARRANGE,
    MODEL_TEST_MATCHING,
    MODEL_TEST_REARRANGE
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
    slug = "ssc-2027-english-matching-rearrange"
    title = "SSC 2027 English Matching & Rearrange Suggestion | এসএসসি টেবিল ম্যাচিং ও রি-অ্যারেঞ্জিং"
    meta_desc = "SSC 2027 English Matching & Rearrange Suggestion। Q6 ও Q7 এর ৩২টি বোর্ড স্ট্যান্ডার্ড ম্যাচিং টেবিল এবং ৩৬টি রি-অ্যারেঞ্জিং গল্পের সাজানো সঠিক সমাধান।"
    banner_url = f"{CDN_BASE}/ssc_2027_silo_03_matching_rearrange.webp?v=2"
    banner_alt = "SSC 2027 English Sentence Matching Table and Rearranging Sentences Suggestion"
    url = f"{BLOG_BASE}/{slug}.html"
    series_nav = get_series_nav("Part 03")

    # Render 32 Matching Tables HTML
    matching_html = ""
    for item in MATCHING_TABLES_32:
        rows_tr = ""
        for i in range(5):
            ca = item["col_a"][i] if i < len(item["col_a"]) else ""
            cb = item["col_b"][i] if i < len(item["col_b"]) else ""
            cc = item["col_c"][i] if i < len(item["col_c"]) else ""
            rows_tr += f"<tr><td>{ca}</td><td>{cb}</td><td>{cc}</td></tr>\n"
        
        sentences_li = "".join([f"<li>{s}</li>" for s in item["sentences"]])
        key_p = f"<p style='margin:4px 0 8px 0; color:#15803d; font-weight:700;'>ম্যাচিং সূত্র (Key): {item.get('key', 'See sentences below')}</p>" if item.get("key") else ""

        matching_html += f"""<div style="background:#ffffff; border:1px solid #e2e8f0; border-left:4px solid #0c2340; border-radius:8px; padding:18px 22px; margin-bottom:26px; box-shadow:0 2px 5px rgba(0,0,0,0.04);">
          <h3 style="margin:0 0 6px 0; color:#0c2340; font-size:18.5px; font-weight:700;">ট্যাবিল {item['id']}: {item['title']}</h3>
          <p style="margin:0 0 12px 0; font-size:14px; color:#64748b;"><strong>বোর্ড রেফারেন্স:</strong> {item['board']}</p>
          <div style="overflow-x:auto; -webkit-overflow-scrolling:touch; margin-bottom:14px;">
            <table class="htbd-academic-table" style="margin:0;">
              <thead><tr><th>কলাম A (Column A)</th><th>কলাম B (Column B)</th><th>কলাম C (Column C)</th></tr></thead>
              <tbody>{rows_tr}</tbody>
            </table>
          </div>
          {key_p}
          <div style="background:#f8fafc; border-left:3px solid #16a34a; padding:10px 16px; border-radius:4px;">
            <p style="margin:0 0 4px 0; font-weight:700; color:#166534; font-size:15px;">সঠিক ৫টি বাক্য (Complete Meaningful Sentences):</p>
            <ol style="margin:0; padding-left:20px; font-size:15.5px; line-height:1.75; color:#1e293b;">
              {sentences_li}
            </ol>
          </div>
        </div>\n"""

    # Render 36 Re-arrange Items HTML
    rearrange_html = ""
    for item in REARRANGE_ITEMS_36:
        jumbled_li = "".join([f"<li><strong>({k})</strong> {v}</li>" for k, v in item["sentences"].items()])
        rearrange_html += f"""<div style="background:#ffffff; border:1px solid #e2e8f0; border-left:4px solid #0369a1; border-radius:8px; padding:18px 22px; margin-bottom:26px; box-shadow:0 2px 5px rgba(0,0,0,0.04);">
          <h3 style="margin:0 0 6px 0; color:#0369a1; font-size:18.5px; font-weight:700;">রি-অ্যারেঞ্জ {item['id']}: {item['title']}</h3>
          <p style="margin:0 0 12px 0; font-size:14px; color:#64748b;"><strong>উৎস ও বোর্ড:</strong> {item['board']}</p>
          <p style="margin:0 0 6px 0; font-weight:600; color:#334155;">এলোমেলো ৮টি বাক্য (Jumbled Sentences a-h):</p>
          <ul style="list-style:none; padding-left:0; margin:0 0 14px 0; font-size:15px; line-height:1.7; color:#475569;">
            {jumbled_li}
          </ul>
          <div style="background:#f0fdf4; border:1px solid #bbf7d0; padding:10px 14px; border-radius:6px; margin-bottom:12px;">
            <p style="margin:0; color:#166534; font-weight:700; font-size:15px;">ধারাবাহিক ক্রম (Sequence Key): <span style="font-family:monospace; font-size:16px;">{item['key']}</span></p>
          </div>
          <div style="background:#f8fafc; border-left:3px solid #0284c7; padding:12px 16px; border-radius:4px;">
            <p style="margin:0 0 4px 0; font-weight:700; color:#0369a1; font-size:15px;">সাজানো পূর্ণাঙ্গ অনুচ্ছেদ (Coherent Paragraph):</p>
            <p style="margin:0; font-size:16px; line-height:1.8; color:#1e293b;">{item['paragraph']}</p>
          </div>
        </div>\n"""

    # Render Dakhil 2026 Matching Rows
    dakhil_match_rows = ""
    for i in range(5):
        ca = DAKHIL_2026_MATCHING["col_a"][i]
        cb = DAKHIL_2026_MATCHING["col_b"][i]
        cc = DAKHIL_2026_MATCHING["col_c"][i]
        dakhil_match_rows += f"<tr><td>{ca}</td><td>{cb}</td><td>{cc}</td></tr>\n"
    dakhil_match_sent = "".join([f"<li>{s}</li>" for s in DAKHIL_2026_MATCHING["sentences"]])

    # Render Dakhil 2026 Rearrange Sentences
    dakhil_re_li = "".join([f"<li><strong>({k})</strong> {v}</li>" for k, v in DAKHIL_2026_REARRANGE["sentences"].items()])

    # Render Model Test Matching Rows
    model_match_rows = ""
    for i in range(5):
        ca = MODEL_TEST_MATCHING["col_a"][i]
        cb = MODEL_TEST_MATCHING["col_b"][i]
        cc = MODEL_TEST_MATCHING["col_c"][i]
        model_match_rows += f"<tr><td>{ca}</td><td>{cb}</td><td>{cc}</td></tr>\n"
    model_match_sent = "".join([f"<li>{s}</li>" for s in MODEL_TEST_MATCHING["sentences"]])

    # Render Model Test Rearrange Sentences
    model_re_li = "".join([f"<li><strong>({k})</strong> {v}</li>" for k, v in MODEL_TEST_REARRANGE["sentences"].items()])

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
    <figcaption style="font-size: 14px; color: #64748b; text-align: center; margin-top: 6px;">SSC 2027 English 1st Paper Matching & Re-arrange — Part 03 of the Study Silo Series</figcaption>
  </figure>

  <div class="htbd-overview-box">
    <p style="margin: 0 0 10px 0; font-size: 16px; color: #1e3a8a; font-weight: 700;">টপিক ও ফোকাস: SSC 2027 English Matching &amp; Rearrange Suggestion (Questions 6, 7)</p>
    <p>যৌক্তিক বাক্যগঠন ও ব্যাকরণিক সামঞ্জস্য যাচাইয়ের ক্ষেত্রে <strong>SSC 2027 English Matching &amp; Rearrange Suggestion</strong> পরীক্ষায় শিক্ষার্থীদের পূর্ণ নম্বর পাওয়ার অন্যতম সেরা সুযোগ তৈরি করে। এই অংশে মোট <strong>১৩ নম্বর</strong> বরাদ্দ রয়েছে—<strong>Question 6: Sentence Matching Table (5 Marks)</strong> যেখানে ৩টি কলাম থেকে ৫টি অর্থপূর্ণ বাক্য সাজাতে হয়, এবং <strong>Question 7: Re-arranging Sentences (8 Marks)</strong> যেখানে একটি এলোমেলো ঐতিহাসিক ঘটনা বা শিক্ষণীয় গল্পকে সঠিক ক্রমানুসারে সাজাতে হয়। সকল শিক্ষা বোর্ডের বিগত বছরের প্রশ্ন বিশ্লেষণ করে ৩২টি নিশ্চিত ম্যাচিং টেবিল ও ৩৬টি শীর্ষ রি-অ্যারেঞ্জিং অনুচ্ছেদের সঠিক সিকোয়েন্স ছক নিচে বিস্তারিত দেওয়া হলো।</p>
  </div>

<!--more-->

  <div class="htbd-toc-card">
    <p class="toc-title">বিষয়সূচি (Table of Contents)</p>
    <ul>
      <li><a href="#marks-dist">১. প্রশ্ন ৬ ও ৭: মানবণ্টন ও প্রশ্ন রূপরেখা (Marks Distribution)</a></li>
      <li><a href="#matching-rules">২. প্রশ্ন ৬: ৩-কলাম ম্যাচিং টেবিল মেলানোর গ্রামাটিক্যাল নিয়ম (Q6 Strategy)</a></li>
      <li><a href="#rearrange-rules">৩. প্রশ্ন ৭: রি-অ্যারেঞ্জিং অনুচ্ছেদ ক্রম নির্ণয়ের ৪টি সূত্র (Q7 Strategy)</a></li>
      <li><a href="#all-matching">৪. ৩২টি পূর্ণাঙ্গ ম্যাচিং টেবিল ও সমাধান (All 32 Matching Tables)</a></li>
      <li><a href="#all-rearrange">৫. ৩৬টি পূর্ণাঙ্গ রি-অ্যারেঞ্জিং অনুচ্ছেদ ও সিকোয়েন্স কি (All 36 Re-arrange Items)</a></li>
      <li><a href="#model-dakhil">৬. মডেল পরীক্ষা ০১: দাখিল ২০২৬ বোর্ড প্রশ্ন ও সমাধান (Madhusudan & Beggar)</a></li>
      <li><a href="#model-exclusive">৭. মডেল পরীক্ষা ০২: এক্সক্লুসিভ মডেল টেস্ট ও সমাধান (Facebook & Fleming)</a></li>
      <li><a href="#faq">৮. সচরাচর জিজ্ঞাসা (FAQ)</a></li>
    </ul>
  </div>

  <h2 class="htbd-academic-heading" id="marks-dist">১. প্রশ্ন ৬ ও ৭: মানবণ্টন ও প্রশ্ন রূপরেখা (Marks Distribution)</h2>
  <p>ইংরেজি ১ম পত্রে ১৩ নম্বরের এই অংশটিতে পূর্ণ নম্বর নিশ্চিত করা তুলনামূলকভাবে সহজ, যদি ব্যাকরণিক সংযোগ ও ঘটনার কালানুক্রম বোঝা যায়:</p>

  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 22px 0;">
    <table class="htbd-academic-table">
      <thead>
        <tr>
          <th>প্রশ্ন নম্বর</th>
          <th>আইটেমের নাম (Item)</th>
          <th>কাঠামো (Structure)</th>
          <th>নম্বর (Marks)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>প্রশ্ন ৬ (Q6)</strong></td>
          <td>Matching Table (Sentence Parts)</td>
          <td>Column A (Subject) + Column B (Verb/Phrase) + Column C (Extension)</td>
          <td><strong>1 × 5 = 5 নম্বর</strong></td>
        </tr>
        <tr>
          <td><strong>প্রশ্ন ৭ (Q7)</strong></td>
          <td>Re-arranging Sentences</td>
          <td>৮টি এলোমেলো বাক্যকে (a থেকে h) যৌক্তিক ক্রমানুসারে সাজিয়ে অনুচ্ছেদ গঠন</td>
          <td><strong>1 × 8 = 8 নম্বর</strong></td>
        </tr>
        <tr>
          <td colspan="3" style="text-align:right; font-weight:700; background:#f1f5f9;">মোট নম্বর (Total Marks):</td>
          <td style="font-weight:700; background:#f1f5f9; color:#0c2340;"><strong>১৩ নম্বর</strong></td>
        </tr>
      </tbody>
    </table>
  </div>

  <h2 class="htbd-academic-heading" id="matching-rules">২. প্রশ্ন ৬: ৩-কলাম ম্যাচিং টেবিল মেলানোর গ্রামাটিক্যাল নিয়ম (Q6 Strategy)</h2>
  <p>প্রশ্ন ৬-এ ৫টি বাক্য তৈরি করতে হয়। ৩টি কলাম মেলাতে নিচের কৌশলগুলো অনুসরণ করুন:</p>
  <ul style="line-height:1.85;">
    <li><strong>Subject-Verb Agreement লক্ষ্য করুন:</strong> Column A-এর Subject Singular হলে Column B-এর Verb-ও Singular (যেমন: -s/-es বা was/has) হবে। এটি অনেক অপশন সরাসরি বাদ দিতে সাহায্য করে।</li>
    <li><strong>Prepositional Linkers ধরুন:</strong> Column B-এর শেষ শব্দটি যদি Preposition হয় (যেমন: <em>consists of, devoted to, stands at</em>), তাহলে Column C-তে সেই Preposition-এর পর বসতে পারে এমন Noun বা Noun Phrase খুঁজুন।</li>
    <li><strong>উত্তরের উপস্থাপনা:</strong> খাতায় প্রথমে সূত্র লিখুন, যেমন: <code>(a + iii + v)</code> এবং তার নিচে সম্পূর্ণ বাক্যটি নির্ভুলভাবে লিখুন। সম্পূর্ণ বাক্য লেখা বাঞ্ছনীয়।</li>
  </ul>

  <h2 class="htbd-academic-heading" id="rearrange-rules">৩. প্রশ্ন ৭: রি-অ্যারেঞ্জিং অনুচ্ছেদ ক্রম নির্ণয়ের ৪টি সূত্র (Q7 Strategy)</h2>
  <p>রি-অ্যারেঞ্জিংয়ে ৮টি বাক্য ক্রমানুসারে সাজাতে নিচের ৪টি মূল সূত্র সবচেয়ে কার্যকর:</p>
  <ul style="line-height:1.85;">
    <li><strong>১. পরিচয় ও জন্ম (Introduction & Birth):</strong> জীবনীমূলক অনুচ্ছেদে ব্যক্তির নাম, জাতীয়তা বা জন্ম সংক্রান্ত বাক্যটি সবসময় ১ম স্থানে (1st Sentence) বসে।</li>
    <li><strong>২. শিক্ষা ও কর্মজীবন (Education & Early Career):</strong> শৈশব, প্রাথমিক পড়াশোনা, উচ্চশিক্ষা এবং কর্মজীবন কালানুক্রমিক (Chronological Order) অনুযায়ী পর্যায়ক্রমে আসে।</li>
    <li><strong>৩. বৈবাহিক ও পারিবারিক জীবন (Marriage & Struggle):</strong> বিয়ে, পারিবারিক ট্র্যাজেডি বা জীবনসংগ্রামের ধাপগুলো ক্যারিয়ারের শুরুর পরপরই ঘটে।</li>
    <li><strong>৪. অমর কীর্তি ও প্রয়াণ (Masterpiece & Death):</strong> জীবনের সবচেয়ে বড় আবিষ্কার বা সাহিত্যকীর্তি শেষভাগে আসে এবং মৃত্যু ও শেষ সম্মাননা সংক্রান্ত বাক্যটি সবার শেষে বসে।</li>
    <li><strong>খাতায় উপস্থাপনা:</strong> খাতায় প্রথমে ১ থেকে ৮ নম্বরের সিকোয়েন্স বক্স (Sequence Table) আঁকুন এবং নিচে প্যারাগ্রাফ আকারে সাজানো সম্পূর্ণ অনুচ্ছেদটি লিখুন।</li>
  </ul>

  <h2 class="htbd-academic-heading" id="all-matching">৪. ৩২টি পূর্ণাঙ্গ ম্যাচিং টেবিল ও সমাধান (All 32 Matching Tables for SSC 2027)</h2>
  <p>নিচে জাতীয় শিক্ষাক্রমের পূর্ণাঙ্গ পাঠ্য ও বিগত বোর্ড পরীক্ষার ৩২টি ৩-কলাম ম্যাচিং টেবিল এবং প্রতিটি টেবিলের সঠিক ৫টি বাক্য সমাধানসহ দেওয়া হলো:</p>
  {matching_html}

  <h2 class="htbd-academic-heading" id="all-rearrange">৫. ৩৬টি পূর্ণাঙ্গ রি-অ্যারেঞ্জিং অনুচ্ছেদ ও সিকোয়েন্স কি (All 36 Re-arrange Items for SSC 2027)</h2>
  <p>নিচে এসএসসি ও দাখিল ২০২৭-এর জন্য ৩৬টি গুরুত্বপূর্ণ ঐতিহাসিক, রূপকথা ও শিক্ষণীয় গল্পের রি-অ্যারেঞ্জিং জ্যাম্বলড বাক্য, সিকোয়েন্স কি এবং পূর্ণাঙ্গ সাজানো অনুচ্ছেদ দেওয়া হলো:</p>
  {rearrange_html}

  <h2 class="htbd-academic-heading" id="model-dakhil">৬. মডেল পরীক্ষা ০১: দাখিল ২০২৬ বোর্ড প্রশ্ন ও সমাধান (Michael Madhusudan & Beggar)</h2>
  
  <h3 class="htbd-academic-subheading">Question 6: Match the parts of sentences given in Column 'A', 'B' and 'C' (5 Marks)</h3>
  <p><strong>বিষয়:</strong> Michael Madhusudan Dutt and Kopotaksha Nad</p>
  <div style="overflow-x:auto; -webkit-overflow-scrolling:touch; margin-bottom:14px;">
    <table class="htbd-academic-table">
      <thead><tr><th>Column A</th><th>Column B</th><th>Column C</th></tr></thead>
      <tbody>{dakhil_match_rows}</tbody>
    </table>
  </div>
  <div style="background:#f0fdf4; border:1px solid #bbf7d0; padding:12px 16px; border-radius:6px; margin-bottom:20px;">
    <p style="margin:0 0 4px 0; color:#166534; font-weight:700;">সঠিক সমাধান:</p>
    <ol style="margin:0; padding-left:20px; color:#1e293b; line-height:1.75;">
      {dakhil_match_sent}
    </ol>
  </div>

  <h3 class="htbd-academic-subheading">Question 7: Put the following sentences into correct order (8 Marks)</h3>
  <p><strong>বিষয়:</strong> Prophet Muhammad (Sm) and the Poor Beggar</p>
  <ul style="list-style:none; padding-left:0; margin:0 0 12px 0; font-size:15px; line-height:1.7; color:#475569;">
    {dakhil_re_li}
  </ul>
  <p style="background:#f1f5f9; border-left:4px solid #0c2340; padding:10px 14px; border-radius:4px; font-weight:700; color:#0c2340;">
    ক্রমিক সূত্র (Sequence Key): {DAKHIL_2026_REARRANGE['key']}
  </p>
  <p style="background:#f8fafc; padding:14px 18px; border-radius:6px; line-height:1.8; color:#1e293b;">
    <strong>সাজানো অনুচ্ছেদ:</strong> {DAKHIL_2026_REARRANGE['paragraph']}
  </p>

  <h2 class="htbd-academic-heading" id="model-exclusive">৭. মডেল পরীক্ষা ০২: এক্সক্লুসিভ মডেল টেস্ট ও সমাধান (Facebook & Fleming)</h2>
  
  <h3 class="htbd-academic-subheading">Question 6: Match the parts of sentences given in Column 'A', 'B' and 'C' (5 Marks)</h3>
  <p><strong>বিষয়:</strong> Facebook and Global Communication</p>
  <div style="overflow-x:auto; -webkit-overflow-scrolling:touch; margin-bottom:14px;">
    <table class="htbd-academic-table">
      <thead><tr><th>Column A</th><th>Column B</th><th>Column C</th></tr></thead>
      <tbody>{model_match_rows}</tbody>
    </table>
  </div>
  <div style="background:#f0fdf4; border:1px solid #bbf7d0; padding:12px 16px; border-radius:6px; margin-bottom:20px;">
    <p style="margin:0 0 4px 0; color:#166534; font-weight:700;">সঠিক সমাধান:</p>
    <ol style="margin:0; padding-left:20px; color:#1e293b; line-height:1.75;">
      {model_match_sent}
    </ol>
  </div>

  <h3 class="htbd-academic-subheading">Question 7: Put the following sentences into correct order (8 Marks)</h3>
  <p><strong>বিষয়:</strong> Sir Alexander Fleming and the Life-Saving Medicine Penicillin</p>
  <ul style="list-style:none; padding-left:0; margin:0 0 12px 0; font-size:15px; line-height:1.7; color:#475569;">
    {model_re_li}
  </ul>
  <p style="background:#f1f5f9; border-left:4px solid #0c2340; padding:10px 14px; border-radius:4px; font-weight:700; color:#0c2340;">
    ক্রমিক সূত্র (Sequence Key): {MODEL_TEST_REARRANGE['key']}
  </p>
  <p style="background:#f8fafc; padding:14px 18px; border-radius:6px; line-height:1.8; color:#1e293b;">
    <strong>সাজানো অনুচ্ছেদ:</strong> {MODEL_TEST_REARRANGE['paragraph']}
  </p>

  <h2 class="htbd-academic-heading" id="faq">৮. সচরাচর জিজ্ঞাসা (FAQ)</h2>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">Question 1: ম্যাচিং টেবিলে কি শুধু সূত্র যেমন (a+iii+v) লিখলে চলবে?</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">উত্তর: শুধু সূত্র লিখলে অনেক সময় পরীক্ষক নম্বর কেটে দেন। নিরাপদ ও সর্বোচ্চ নম্বর নিশ্চিত করতে সূত্রের সাথে সম্পূর্ণ বাক্যটি লিখে দেওয়া আবশ্যক।</p>
  </div>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">Question 2: Re-arrange-এ কি সিকোয়েন্স টেবিল এবং অনুচ্ছেদ দুটোই লিখতে হবে?</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">উত্তর: হ্যাঁ! উত্তরপত্রের শুরুতে ১ থেকে ৮ ঘর বিশিষ্ট ক্রমিক ছক (Sequence Table) আঁকবেন এবং তার ঠিক নিচে সাজানো প্যারাগ্রাফটি লিখে দেবেন। এতে শতভাগ ৮ নম্বর নিশ্চিত হয়।</p>
  </div>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">Question 3: রি-অ্যারেঞ্জে কোনো একটি বাক্যের ক্রম ভুল হলে কি পুরো নম্বর কাটা যায়?</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">উত্তর: না, পুরো নম্বর কাটা যায় না। প্রতি সঠিক অবস্থানের জন্য আলাদা ১ নম্বর থাকে। তবে মাঝের কোনো বাক্য ভুল স্থানে বসলে তার পরের ধারাবাহিকতা নষ্ট হওয়ার ঝুঁকি থাকে, তাই মনোযোগ দিয়ে প্রথম থেকে শেষ পর্যন্ত যাচাই করা জরুরি।</p>
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
    {{"@type": "Question", "name": "Is writing full sentences required in Q6 Matching Table?", "acceptedAnswer": {{"@type": "Answer", "text": "Writing the code formula along with the full sentence ensures you receive full credit without ambiguity."}}}},
    {{"@type": "Question", "name": "Should I write both sequence table and coherent paragraph in Q7 Re-arrange?", "acceptedAnswer": {{"@type": "Answer", "text": "Yes, drawing the sequence box followed by the coherent written paragraph is the standard board presentation."}}}},
    {{"@type": "Question", "name": "What happens if one sentence order is mixed up in re-arrange?", "acceptedAnswer": {{"@type": "Answer", "text": "Each correctly positioned sentence earns 1 mark, so you do not lose all 8 marks for a single displacement."}}}}
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
    print(f"Silo 03 generated successfully! Length: {len(html)} chars, Slug: {slug}")
