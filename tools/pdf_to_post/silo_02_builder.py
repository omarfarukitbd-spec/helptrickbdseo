#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/pdf_to_post/silo_02_builder.py
-------------------------------------
Generates Silo Post 02: Unseen Passage, Information Transfer & Summary Writing (Q4-5).
Includes all 41 Unseen Topics + 3 Full Model Sets (Hazrat Omar R, 26 March, John Milton).
"""

import json
from data_ssc_2027_unseen import (
    UNSEEN_TOPICS_41,
    MODEL_01_HAZRAT_OMAR,
    MODEL_02_INDEPENDENCE_DAY as MODEL_02_26_MARCH,
    MODEL_03_JOHN_MILTON
)

BLOG_BASE = "https://www.helptrickbd.com/2026/09"
CDN_BASE = "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts"
LABELS = ["SSC Suggestion", "Education", "Dakhil Suggestion"]

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

def build_post():
    slug = "ssc-2027-english-unseen-passage-summary"
    title = "এসএসসি ২০২৭ ইংরেজি ১ম পত্র আনসিন প্যাসেজ ও সামারি রাইটিং গাইড (SSC 2027 English Unseen Passage, Information Transfer & Summary Writing Complete Guide)"
    meta_desc = "SSC 2027 English 1st Paper Unseen Passage ও Summary Writing গাইড। Information Transfer (Q4) ও Summary (Q5) এর ৪১টি প্যাসেজ এবং ৩টি মডেল সমাধান।"
    banner_url = f"{CDN_BASE}/ssc_2027_silo_02_unseen_passage.webp"
    banner_alt = "SSC 2027 English Unseen Passage Information Transfer and Summary Writing Suggestion"
    url = f"{BLOG_BASE}/{slug}.html"
    series_nav = get_series_nav("Part 02")

    # Render 41 Unseen Topics table rows
    topics_rows = ""
    for t in UNSEEN_TOPICS_41:
        star_color = "#b91c1c" if t["stars"] == "***" else ("#c2410c" if t["stars"] == "**" else "#4b5563")
        topics_rows += f"""<tr>
          <td style="text-align:center; font-weight:700;">{t['id']}</td>
          <td style="text-align:center; font-weight:700; color:{star_color}; font-size:18px;">{t['stars']}</td>
          <td><strong>{t['title']}</strong><br><span style="font-size:13.5px; color:#64748b;">বিষয়বস্তু: {t['theme']}</span></td>
          <td style="text-align:center;">p. {t['page_pdf']}</td>
          <td>{t['boards']}</td>
        </tr>\n"""

    # Helper function to render an info transfer table
    def render_info_table(table_data):
        th_cells = "".join([f"<th>{h}</th>" for h in table_data["headers"]])
        tr_rows = ""
        for row in table_data["rows"]:
            td_cells = "".join([f"<td>{c}</td>" for c in row])
            tr_rows += f"<tr>{td_cells}</tr>\n"
        return f"""<div style="overflow-x:auto; -webkit-overflow-scrolling:touch; margin:16px 0;">
          <table class="htbd-academic-table">
            <thead><tr>{th_cells}</tr></thead>
            <tbody>{tr_rows}</tbody>
          </table>
        </div>"""

    # Helper function to render answers dictionary
    def render_answers(ans_dict):
        items = [f"<strong>({k})</strong> {v}" for k, v in ans_dict.items()]
        return " &nbsp;|&nbsp; ".join(items)

    omar_table = render_info_table(MODEL_01_HAZRAT_OMAR["info_transfer_table"])
    omar_ans = render_answers(MODEL_01_HAZRAT_OMAR["info_transfer_answers"])

    march_table = render_info_table(MODEL_02_26_MARCH["info_transfer_table"])
    march_ans = render_answers(MODEL_02_26_MARCH["info_transfer_answers"])

    milton_table = render_info_table(MODEL_03_JOHN_MILTON["info_transfer_table"])
    milton_ans = render_answers(MODEL_03_JOHN_MILTON["info_transfer_answers"])

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
    <figcaption style="font-size: 14px; color: #64748b; text-align: center; margin-top: 6px;">SSC 2027 English 1st Paper Unseen Passage — Part 02 of the Study Silo Series</figcaption>
  </figure>

  <div class="htbd-overview-box">
    <p>এসএসসি ২০২৭ ইংরেজি ১ম পত্র পরীক্ষায় <strong>প্রশ্ন ৪ ও ৫</strong> একটি পাঠ্যবই-বহির্ভূত আনসিন প্যাসেজ (Unseen Passage) থেকে আসে এবং এতে মোট <strong>১৫ নম্বর</strong> নির্ধারিত থাকে। এর মধ্যে Q4-এ থাকে ৫ নম্বরের ইনফরমেশন ট্রান্সফার গ্রিড (Information Transfer) এবং Q5-এ থাকে ১০ নম্বরের সামারি রাইটিং (Summary Writing)। নিচে ৪১টি গুরুত্বপূর্ণ আনসিন বিষয়ের স্টারভিত্তিক তালিকা এবং ৩টি পূর্ণাঙ্গ মডেল টেস্ট প্রশ্ন ও উত্তরসহ প্রদান করা হলো।</p>
  </div>

<!--more-->

  <div class="htbd-toc-card">
    <p class="toc-title">বিষয়সূচি (Table of Contents)</p>
    <ul>
      <li><a href="#unseen-marks">১. আনসিন প্যাসেজ: নম্বর বণ্টন ও প্রশ্ন রূপরেখা (Marks Distribution)</a></li>
      <li><a href="#unseen-topics">২. ৪১টি সম্ভাব্য আনসিন প্যাসেজের পূর্ণ তালিকা (All 41 Unseen Topics)</a></li>
      <li><a href="#info-transfer-rules">৩. প্রশ্ন ৪: Information Transfer সমাধানের নিয়ম ও কলাম ট্র্যাকিং (Q4 Guide)</a></li>
      <li><a href="#summary-rules">৪. প্রশ্ন ৫: Summary Writing-এ পূর্ণ ১০/১০ পাওয়ার ৫টি সোনালী নিয়ম (Q5 Guide)</a></li>
      <li><a href="#model-omar">৫. মডেল পরীক্ষা ০১: হযরত ওমর (রা.) ও সেবামূলক রাষ্ট্রনায়কত্ব (Hazrat Omar R)</a></li>
      <li><a href="#model-march">৬. মডেল পরীক্ষা ০২: দাখিল ২০২৬ বোর্ড প্রশ্ন — ২৬শে মার্চ স্বাধীনতা দিবস (26 March)</a></li>
      <li><a href="#model-milton">৭. মডেল পরীক্ষা ০৩: এক্সক্লুসিভ মডেল টেস্ট — মহাকবি জন মিল্টন (John Milton)</a></li>
      <li><a href="#faq">৮. সচরাচর জিজ্ঞাসা (FAQ)</a></li>
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
          <td><strong>1 × 5 = 5 নম্বর</strong></td>
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

  <h2 class="htbd-academic-heading" id="unseen-topics">২. ৪১টি সম্ভাব্য আনসিন প্যাসেজের পূর্ণ তালিকা (All 41 Unseen Topics for SSC 2027)</h2>
  <p>নিচে ২০২৭ সালের এসএসসি ও দাখিল পরীক্ষার্থীদের জন্য বিগত বোর্ড প্রশ্ন ও শীর্ষ ক্যাডেট কলেজের মডেল বিশ্লেষণের ভিত্তিতে ৪১টি শীর্ষ আনসিন টপিকের স্টারভিত্তিক রেটিং তুলে ধরা হলো:</p>

  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 22px 0;">
    <table class="htbd-academic-table">
      <thead>
        <tr>
          <th style="width:6%;">ক্র.</th>
          <th style="width:8%; text-align:center;">স্টার</th>
          <th style="width:48%;">প্যাসেজের শিরোনাম ও টেক্সট স্নিপেট</th>
          <th style="width:14%; text-align:center;">বইয়ের পৃষ্ঠা</th>
          <th style="width:24%;">বিগত বোর্ড পরীক্ষা</th>
        </tr>
      </thead>
      <tbody>
        {topics_rows}
      </tbody>
    </table>
  </div>

  <h2 class="htbd-academic-heading" id="info-transfer-rules">৩. প্রশ্ন ৪: Information Transfer সমাধানের নিয়ম ও কলাম ট্র্যাকিং (Q4 Guide)</h2>
  <p>ইনফরমেশন ট্রান্সফার মূলত একটি দ্রুত তথ্য বিশ্লেষণমূলক প্রশ্ন। এখানে ৫টি শূন্যস্থান পূরণ করতে ৫ নম্বর পাওয়া যায়। শতভাগ নম্বর অর্জনের পদ্ধতি:</p>
  <ul style="line-height:1.85;">
    <li><strong>কলামের হেডিং লক্ষ্য করুন:</strong> ছকের কলামে "Who / What", "Event / Activity", "Year / Time", "Place / Where" এবং "Whom / Why" হেডিংগুলো খুব যত্নসহকারে পড়ুন। প্রতিটি কলাম ঠিক কোন প্রশ্নের উত্তর চাইছে, তা বুঝলেই অর্ধেক কাজ শেষ।</li>
    <li><strong>অনর্থক বড় বাক্য না লেখা:</strong> ছকের ভেতর পুরো বাক্য লেখার প্রয়োজন নেই। শুধু মূল শব্দগুচ্ছ (Phrase) বা নির্দিষ্ট তথ্য (যেমন: <em>"in 1971"</em> বা <em>"at Cambridge University"</em>) লিখলেই পূর্ণ নম্বর দেওয়া হয়।</li>
    <li><strong>ক্রমানুসারে সাজানো:</strong> উত্তরপত্রে শুধু (i), (ii), (iii), (iv), (v) লিখে পাশে সরাসরি উত্তর লিখে দিন। সম্পূর্ণ টেবিল খাতায় আঁকা বাধ্যতামূলক নয়, তবে স্পষ্ট হস্তাক্ষরে লিখলে পরীক্ষকের নম্বর দিতে স্বাচ্ছন্দ্য হয়।</li>
  </ul>

  <h2 class="htbd-academic-heading" id="summary-rules">৪. প্রশ্ন ৫: Summary Writing-এ পূর্ণ ১০/১০ পাওয়ার ৫টি সোনালী নিয়ম (Q5 Guide)</h2>
  <p>১০ নম্বরের সামারি রাইটিং অনেক শিক্ষার্থীর কাছেই চ্যালেঞ্জিং মনে হয়। তবে নিচের ৫টি টেকনিক প্রয়োগ করলে পরীক্ষক ৮ থেকে ১০ নম্বর দিতে বাধ্য হন:</p>
  <ul style="line-height:1.85;">
    <li><strong>এক-তৃতীয়াংশ দৈর্ঘ্য (One-third Rule):</strong> সামারির দৈর্ঘ্য মূল প্যাসেজের মোটামুটি এক-তৃতীয়াংশ (সাধারণত ৪ থেকে ৫টি সুসংহত বাক্য বা ৬০–৮০ শব্দ) হতে হবে। বেশি বড় লেখা সামারির মূল নিয়মের পরিপন্থী।</li>
    <li><strong>নিজস্ব ভাষার প্রকাশ (Paraphrasing):</strong> মূল প্যাসেজের কোনো বাক্য হুবহু কপি করে লিখবেন না। সমার্থক শব্দ (Synonyms) ও বাক্যের গঠন বদলে মূল অর্থ তুলে ধরুন।</li>
    <li><strong>উদাহরণ ও প্রত্যক্ষ উক্তি বর্জন:</strong> প্যাসেজের কোনো উদাহরণ, উদ্ধৃতি (Quotation), বা সংখ্যাতাত্ত্বিক সূক্ষ্ম ব্যাখ্যা সামারিতে কখনোই অন্তর্ভুক্ত করবেন না। শুধু মূল সত্য বা ফলাফল লিখুন।</li>
    <li><strong>উত্তম ও মধ্যম পুরুষ বর্জন:</strong> সামারি সবসময় Third Person (He/She/They/The passage) এবং বর্ণনামূলক টেন্সে লিখতে হবে। "I think" বা "We see that" জাতীয় মন্তব্য সম্পূর্ণরূপে বাদ দিন।</li>
    <li><strong>লিঙ্কার ও সাবলীল সংযোগ:</strong> প্রতিটি বাক্যের মাঝে যৌক্তিক ধারাবাহিকতা রক্ষায় উপযুক্ত লিঙ্কার (যেমন: <em>Although, However, In addition, Consequently, Ultimately</em>) ব্যবহার করুন।</li>
  </ul>

  <h2 class="htbd-academic-heading" id="model-omar">৫. মডেল পরীক্ষা ০১: হযরত ওমর (রা.) ও সেবামূলক রাষ্ট্রনায়কত্ব (Hazrat Omar R)</h2>
  <p style="background:#f1f5f9; padding:16px 20px; border-radius:6px; font-style:italic; line-height:1.8;">
    "{MODEL_01_HAZRAT_OMAR['passage']}"
  </p>

  <h3 class="htbd-academic-subheading">Question 4: Complete the table below with information from the passage (5 Marks)</h3>
  {omar_table}
  <p style="background:#f0fdf4; border:1px solid #bbf7d0; padding:12px 16px; border-radius:6px; color:#14532d;">
    <strong>সঠিক উত্তর (Answer Key):</strong> {omar_ans}
  </p>

  <h3 class="htbd-academic-subheading">Question 5: Write a summary of the passage in your own words (10 Marks)</h3>
  <div style="background:#f8fafc; border-left:4px solid #0c2340; padding:16px 20px; border-radius:6px; margin:16px 0;">
    <p style="margin:0; font-size:16.5px; line-height:1.8; color:#1e293b;">
      {MODEL_01_HAZRAT_OMAR['model_summary']}
    </p>
  </div>

  <h2 class="htbd-academic-heading" id="model-march">৬. মডেল পরীক্ষা ০২: দাখিল ২০২৬ বোর্ড প্রশ্ন — ২৬শে মার্চ স্বাধীনতা দিবস (26 March)</h2>
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

  <h2 class="htbd-academic-heading" id="model-milton">৭. মডেল পরীক্ষা ০৩: এক্সক্লুসিভ মডেল টেস্ট — মহাকবি জন মিল্টন (John Milton)</h2>
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

  <h2 class="htbd-academic-heading" id="faq">৮. সচরাচর জিজ্ঞাসা (FAQ)</h2>
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
