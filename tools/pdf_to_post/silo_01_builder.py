#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/pdf_to_post/silo_01_builder.py
-------------------------------------
Generates Silo Post 01: Seen Passage (Q1-3)
Includes all 33 Seen Passages + Dakhil 2026 Model + Exclusive Model Test.
"""

import json
from data_ssc_2027_seen import (
    SEEN_PASSAGES_33,
    DAKHIL_2026_SEEN_MODEL as DAKHIL_2026_SEEN,
    EXCLUSIVE_MODEL_TEST_SEEN as MODEL_TEST_SEEN
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
    slug = "ssc-2027-english-seen-passage-suggestion"
    title = "এসএসসি ২০২৭ ইংরেজি ১ম পত্র সিন প্যাসেজ সাজেশন (SSC 2027 English Seen Passage MCQ, Question Answer & Gap Filling Complete Guide)"
    meta_desc = "SSC 2027 English 1st Paper Seen Passage গাইড। MCQ (Q1), প্রশ্নোত্তর (Q2) ও Gap Filling (Q3) — ২২ নম্বরের পূর্ণাঙ্গ মডেল সমাধান ও প্রস্তুতি।"
    banner_url = f"{CDN_BASE}/ssc_2027_silo_01_seen_passage.webp"
    banner_alt = "SSC 2027 English Seen Passage Suggestion — MCQ, Question Answer and Gap Filling Guide"
    url = f"{BLOG_BASE}/{slug}.html"
    series_nav = get_series_nav("Part 01")

    # Render 33 passages table rows
    passages_rows = ""
    for p in SEEN_PASSAGES_33:
        star_color = "#b91c1c" if p["stars"] == "***" else ("#c2410c" if p["stars"] == "**" else "#4b5563")
        passages_rows += f"""<tr>
          <td style="text-align:center; font-weight:700;">{p['id']}</td>
          <td style="text-align:center; font-weight:700; color:{star_color}; font-size:18px;">{p['stars']}</td>
          <td><strong>{p['title']}</strong></td>
          <td style="text-align:center;">{p['unit']}, {p['lesson']} (p. {p['page_pdf']})</td>
          <td>{p['boards']}</td>
        </tr>\n"""

    # Render Dakhil 2026 MCQs
    dakhil_mcqs = ""
    for m in DAKHIL_2026_SEEN["mcq_questions"]:
        opts = " ".join([f"<span>{opt}</span>" for opt in m["options"]])
        dakhil_mcqs += f"""<div style="margin-bottom:14px; background:#f8fafc; padding:10px 14px; border-radius:6px;">
          <p style="margin:0 0 6px 0; font-weight:600;">({m['id']}) {m['question']}</p>
          <p style="margin:0; font-size:15.5px; color:#334155; display:flex; flex-wrap:wrap; gap:16px;">{opts}</p>
          <p style="margin:4px 0 0 0; color:#15803d; font-size:15px; font-weight:600;">সঠিক উত্তর: {m['answer']}</p>
        </div>\n"""

    # Render Dakhil 2026 Q/A
    dakhil_qas = ""
    for q in DAKHIL_2026_SEEN["open_questions"]:
        dakhil_qas += f"""<div style="margin-bottom:14px; background:#f8fafc; padding:12px 16px; border-radius:6px; border-left:4px solid #0c2340;">
          <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340;">({q['id']}) {q['question']}</p>
          <p style="margin:0; color:#1e293b; font-size:16px; line-height:1.7;"><strong>উত্তর:</strong> {q['answer']}</p>
        </div>\n"""

    # Render Dakhil 2026 Gap Fill
    dakhil_gaps = " ".join([f"<strong>({k})</strong> {v}" for k, v in DAKHIL_2026_SEEN["gap_fill"]["answers"].items()])

    # Render Model Test MCQs
    model_mcqs = ""
    for m in MODEL_TEST_SEEN["mcq_questions"]:
        opts = " ".join([f"<span>{opt}</span>" for opt in m["options"]])
        model_mcqs += f"""<div style="margin-bottom:14px; background:#f8fafc; padding:10px 14px; border-radius:6px;">
          <p style="margin:0 0 6px 0; font-weight:600;">({m['id']}) {m['question']}</p>
          <p style="margin:0; font-size:15.5px; color:#334155; display:flex; flex-wrap:wrap; gap:16px;">{opts}</p>
          <p style="margin:4px 0 0 0; color:#15803d; font-size:15px; font-weight:600;">সঠিক উত্তর: {m['answer']}</p>
        </div>\n"""

    # Render Model Test Q/A
    model_qas = ""
    for q in MODEL_TEST_SEEN["open_questions"]:
        model_qas += f"""<div style="margin-bottom:14px; background:#f8fafc; padding:12px 16px; border-radius:6px; border-left:4px solid #0c2340;">
          <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340;">({q['id']}) {q['question']}</p>
          <p style="margin:0; color:#1e293b; font-size:16px; line-height:1.7;"><strong>উত্তর:</strong> {q['answer']}</p>
        </div>\n"""

    # Render Model Test Gap Fill
    model_gaps = " ".join([f"<strong>({k})</strong> {v}" for k, v in MODEL_TEST_SEEN["gap_fill"]["answers"].items()])

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
    <figcaption style="font-size: 14px; color: #64748b; text-align: center; margin-top: 6px;">SSC 2027 English 1st Paper Seen Passage — Part 01 of the Study Silo Series</figcaption>
  </figure>

  <div class="htbd-overview-box">
    <p>এসএসসি ২০২৭ ইংরেজি ১ম পত্রে <strong>প্রশ্ন ১, ২ ও ৩</strong> — এই তিনটি প্রশ্ন পাঠ্যবই <em>English For Today (EFT)</em> এর সিন প্যাসেজ থেকে আসে এবং এতে মোট <strong>২২ নম্বর</strong> বরাদ্দ থাকে। এর মধ্যে Q1-এ ৭টি MCQ (৭ নম্বর), Q2-এ ৫টি ওপেন-এন্ডেড প্রশ্নোত্তর (১০ নম্বর) এবং Q3-এ ৫টি ক্লু-হীন গ্যাপ ফিলিং (৫ নম্বর) অন্তর্ভুক্ত। নিচে পাঠ্যবইয়ের ৩৩টি প্যাসেজের স্টারভিত্তিক চূড়ান্ত তালিকা এবং ২টি সম্পূর্ণ মডেল টেস্ট সমাধানসহ উপস্থাপন করা হলো।</p>
  </div>

<!--more-->

  <div class="htbd-toc-card">
    <p class="toc-title">বিষয়সূচি (Table of Contents)</p>
    <ul>
      <li><a href="#seen-marks">১. সিন প্যাসেজ: নম্বর বণ্টন ও প্রশ্নকাঠামো (Marks Distribution)</a></li>
      <li><a href="#important-passages">২. পাঠ্যবইয়ের ৩৩টি সিন প্যাসেজ তালিকা (All 33 Seen Passages)</a></li>
      <li><a href="#mcq-guide">৩. প্রশ্ন ১: MCQ সমাধানের ব্যাকরণ ও টেক্সচুয়াল কৌশল (Q1 Guide)</a></li>
      <li><a href="#qa-guide">৪. প্রশ্ন ২: Open-Ended প্রশ্নে পূর্ণ ১০/১০ পাওয়ার নিয়ম (Q2 Guide)</a></li>
      <li><a href="#gap-fill-guide">৫. প্রশ্ন ৩: Gap Filling Without Clues সমাধানের ৫টি কৌশল (Q3 Guide)</a></li>
      <li><a href="#model-dakhil">৬. মডেল পরীক্ষা ০১: দাখিল ২০২৬ বোর্ড প্রশ্ন ও পূর্ণাঙ্গ সমাধান (Zahir Raihan)</a></li>
      <li><a href="#model-exclusive">৭. মডেল পরীক্ষা ০২: এক্সক্লুসিভ মডেল টেস্ট ও পূর্ণাঙ্গ সমাধান (Climate Change)</a></li>
      <li><a href="#faq">৮. সচরাচর জিজ্ঞাসা (FAQ)</a></li>
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

  <h2 class="htbd-academic-heading" id="important-passages">২. পাঠ্যবইয়ের ৩৩টি সিন প্যাসেজ তালিকা (All 33 Seen Passages for SSC 2027)</h2>
  <p>নিচে ২০২৭ সালের এসএসসি ও দাখিল পরীক্ষার্থীদের জন্য পাঠ্যবইয়ের ৩৩টি সিন প্যাসেজ গুরুত্ব অনুযায়ী ৩-স্টার (সর্বাধিক সম্ভাব্য), ২-স্টার ও ১-স্টার ক্যাটাগরিতে বোর্ড রেফারেন্সসহ সাজানো হলো:</p>

  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 22px 0;">
    <table class="htbd-academic-table">
      <thead>
        <tr>
          <th style="width:6%;">ক্র.</th>
          <th style="width:8%; text-align:center;">স্টার</th>
          <th style="width:40%;">প্যাসেজের শিরোনাম ও টেক্সট স্নিপেট</th>
          <th style="width:20%; text-align:center;">ইউনিট ও লেসন</th>
          <th style="width:26%;">বিগত বোর্ড পরীক্ষা</th>
        </tr>
      </thead>
      <tbody>
        {passages_rows}
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

  <h2 class="htbd-academic-heading" id="model-dakhil">৬. মডেল পরীক্ষা ০১: দাখিল ২০২৬ বোর্ড প্রশ্ন ও পূর্ণাঙ্গ সমাধান (Zahir Raihan)</h2>
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

  <h2 class="htbd-academic-heading" id="model-exclusive">৭. মডেল পরীক্ষা ০২: এক্সক্লুসিভ মডেল টেস্ট ও পূর্ণাঙ্গ সমাধান (Climate Change)</h2>
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

  <h2 class="htbd-academic-heading" id="faq">৮. সচরাচর জিজ্ঞাসা (FAQ)</h2>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">Question 1: সিন প্যাসেজ থেকে কি হুবহু লাইন তুলে উত্তর দেওয়া যাবে?</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">উত্তর: না, হুবহু লাইন তুলে দিলে পরীক্ষক পূর্ণ নম্বর কাটেন। প্যাসেজ থেকে তথ্য নিয়ে নিজের বাক্য গঠনে উত্তর সাজাতে হবে।</p>
  </div>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">Question 2: Gap Filling-এ কি পুরো বাক্য তুলে লিখতে হবে?</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">উত্তর: শুধু ক্রমিক নম্বর দিয়ে (a), (b), (c), (d), (e) এর উত্তর লিখলেই চলে। তবে পুরো বাক্য তুলে আন্ডারলাইন করে লিখলে খাতার মান আরও ভালো দেখায়।</p>
  </div>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">Question 3: MCQ-তে কি শুধু অপশন নম্বর নাকি উত্তরসহ লিখতে হবে?</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">উত্তর: সবসময় অপশন ও উত্তর উভয়ই লিখুন, যেমন: (a) (ii) Carbon dioxide। এতে পরীক্ষকের খাতা দেখতে সুবিধা হয়।</p>
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
    {{"@type": "Question", "name": "Should I copy sentences directly from the seen passage in Q2?", "acceptedAnswer": {{"@type": "Answer", "text": "No, copying sentences directly will lead to mark deductions. Always extract information and write in your own words with proper tense."}}}},
    {{"@type": "Question", "name": "Do I need to write full sentences in Q3 Gap Filling?", "acceptedAnswer": {{"@type": "Answer", "text": "Writing just the answers beside (a) through (e) is acceptable, but writing full sentences with the filled word underlined is considered best practice."}}}},
    {{"@type": "Question", "name": "How to answer MCQ in Q1?", "acceptedAnswer": {{"@type": "Answer", "text": "Always write both the Roman numeral option and the text answer, e.g., (a) (ii) Carbon dioxide."}}}}
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
