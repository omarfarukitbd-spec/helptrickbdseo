#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/pdf_to_post/silo_05_builder.py
-------------------------------------
Generates Silo Post 05: Writing Test - Completing Story (Q10) & Dialogue Writing (Q11).
Includes all 34 Stories + all 32 Dialogues + 3 Full Model Stories + 7 Full Model Dialogues.
"""

import json
from data_ssc_2027_writing import (
    COMPLETING_STORIES_34,
    MODEL_STORY_LUCKY_TICKET,
    DAKHIL_2026_STORY,
    MODEL_TEST_STORY,
    DIALOGUES_32,
    MODEL_DIALOGUES_VERBATIM,
    DAKHIL_2026_DIALOGUE,
    MODEL_TEST_DIALOGUE
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
    slug = "ssc-2027-english-completing-story"
    title = "SSC 2027 English Completing Story & Dialogue Suggestion | এসএসসি স্টোরি ও ডায়ালগ রাইটিং"
    meta_desc = "SSC 2027 English Completing Story & Dialogue Suggestion। রাইটিং পার্ট (Q10 ও Q11) এর শীর্ষ গল্প ও ডায়ালগ তালিকা এবং বোর্ড মডেল সমাধান।"
    banner_url = f"{CDN_BASE}/ssc_2027_silo_05_story_dialogue.webp?v=2"
    banner_alt = "SSC 2027 English Completing Story and Dialogue Writing Suggestion"
    url = f"{BLOG_BASE}/{slug}.html"
    series_nav = get_series_nav("Part 05")

    # Render 34 Completing Stories Rows
    stories_rows = ""
    for s in COMPLETING_STORIES_34:
        star_color = "#b91c1c" if "Top Priority" in s["priority"] else ("#c2410c" if "High" in s["priority"] else "#4b5563")
        stories_rows += f"""<tr>
          <td style="text-align:center; font-weight:700;">{s['id']}</td>
          <td><strong>{s['title']}</strong><br><span style="font-size:13.5px; color:#64748b;"><em>প্রম্পট:</em> {s['prompt'][:100]}...</span></td>
          <td style="text-align:center; font-weight:700; color:{star_color}; font-size:14px;">{s['priority']}</td>
          <td>{s['boards']}</td>
        </tr>\n"""

    # Render 32 Dialogue Topics Rows
    dialogues_rows = ""
    for d in DIALOGUES_32:
        star_color = "#b91c1c" if "Top Priority" in d["priority"] else ("#c2410c" if "High" in d["priority"] else "#4b5563")
        dialogues_rows += f"""<tr>
          <td style="text-align:center; font-weight:700;">{d['id']}</td>
          <td><strong>{d['title']}</strong><br><span style="font-size:13.5px; color:#64748b;"><em>চরিত্র:</em> {d['characters']}</span></td>
          <td>{d['scenario']}</td>
          <td style="text-align:center; font-weight:700; color:{star_color}; font-size:14px;">{d['priority']}</td>
          <td>{d['boards']}</td>
        </tr>\n"""

    # Helper function to format dialogue turns
    def format_dialogue(text):
        lines = text.strip().split("\n")
        res = ""
        for line in lines:
            if ":" in line:
                speaker, utterance = line.split(":", 1)
                res += f"<p style='margin:0 0 8px 0; line-height:1.75; font-size:16px;'><strong style='color:#0c2340;'>{speaker.strip()}:</strong> {utterance.strip()}</p>\n"
            else:
                res += f"<p style='margin:0 0 8px 0; line-height:1.75; font-size:16px;'>{line.strip()}</p>\n"
        return res

    # Format 5 Model Dialogues from textbook
    d28_html = format_dialogue(MODEL_DIALOGUES_VERBATIM["dialogue_28"]["dialogue_text"])
    d29_html = format_dialogue(MODEL_DIALOGUES_VERBATIM["dialogue_29"]["dialogue_text"])
    d30_html = format_dialogue(MODEL_DIALOGUES_VERBATIM["dialogue_30"]["dialogue_text"])
    d31_html = format_dialogue(MODEL_DIALOGUES_VERBATIM["dialogue_31"]["dialogue_text"])
    d32_html = format_dialogue(MODEL_DIALOGUES_VERBATIM["dialogue_32"]["dialogue_text"])

    # Format Board and Model Dialogues
    dakhil_d_html = format_dialogue(DAKHIL_2026_DIALOGUE["dialogue_text"])
    model_d_html = format_dialogue(MODEL_TEST_DIALOGUE["dialogue_text"])

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
    <figcaption style="font-size: 14px; color: #64748b; text-align: center; margin-top: 6px;">SSC 2027 English 1st Paper Writing Part (Story & Dialogue) — Part 05 of the Study Silo Series</figcaption>
  </figure>

  <div class="htbd-overview-box">
    <p style="margin: 0 0 10px 0; font-size: 16px; color: #1e3a8a; font-weight: 700;">টপিক ও ফোকাস: SSC 2027 English Completing Story &amp; Dialogue Suggestion (Questions 10, 11)</p>
    <p>পরীক্ষায় সর্বোচ্চ নম্বর অর্জনের মূল চাবিকাঠি হলো ফ্রি-হ্যান্ড রাইটিং বা রচনামূলক অংশ। এই <strong>SSC 2027 English Completing Story &amp; Dialogue Suggestion</strong> গাইডে মোট <strong>২৫ নম্বর</strong>-এর পূর্ণাঙ্গ দিকনির্দেশনা দেওয়া হয়েছে। এর মধ্যে রয়েছে <strong>Question 10: Completing Story with Title and Moral (15 Marks)</strong> এবং <strong>Question 11: Dialogue Writing (10 Marks)</strong>। গল্প লেখার ক্ষেত্রে সঠিক টাইটেল নির্ধারণ, প্লট ডেভেলপমেন্ট ও নীতিকথা উপস্থাপন এবং ডায়ালগ রচনার ক্ষেত্রে প্রমিত অভিবাদন ও প্রাসঙ্গিক প্রশ্নোত্তরের সঠিক ফরম্যাটসহ ৩৪টি ক্লাসিক গল্প ও ৩২টি শীর্ষ ডায়ালগের সম্পূর্ণ তালিকা ও নমুনা সমাধান এখানে তুলে ধরা হলো।</p>
  </div>

<!--more-->

  <div class="htbd-toc-card">
    <p class="toc-title">বিষয়সূচি (Table of Contents)</p>
    <ul>
      <li><a href="#writing-marks">১. রাইটিং টেস্ট: নম্বর বণ্টন ও সিলেবাস রূপরেখা (Marks Distribution)</a></li>
      <li><a href="#all-stories">২. ৩৪টি শীর্ষ Completing Story তালিকা ও প্রম্পট (All 34 Stories)</a></li>
      <li><a href="#all-dialogues">৩. ৩২টি শীর্ষ Dialogue Writing তালিকা ও প্রেক্ষাপট (All 32 Dialogues)</a></li>
      <li><a href="#writing-rules">৪. গল্প ও ডায়ালগে পূর্ণ নম্বর পাওয়ার ৪টি পেশাদার নিয়ম (Writing Strategies)</a></li>
      <li><a href="#model-stories">৫. ৩টি পূর্ণাঙ্গ মডেল Completing Story সমাধান (Model Stories)</a></li>
      <li><a href="#model-dialogues">৬. ৭টি পূর্ণাঙ্গ মডেল Dialogue Writing সমাধান (Model Dialogues)</a></li>
      <li><a href="#faq">৭. সচরাচর জিজ্ঞাসা (FAQ)</a></li>
    </ul>
  </div>

  <h2 class="htbd-academic-heading" id="writing-marks">১. রাইটিং টেস্ট: নম্বর বণ্টন ও সিলেবাস রূপরেখা (Marks Distribution)</h2>
  <p>ইংরেজি ১ম পত্রে ১০০ নম্বরের মধ্যে এক-চতুর্থাংশ (২৫%) নম্বর নির্ভর করে এই দুটি আইটেমের ওপর:</p>

  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 22px 0;">
    <table class="htbd-academic-table">
      <thead>
        <tr>
          <th>প্রশ্ন নম্বর</th>
          <th>আইটেমের নাম (Item Name)</th>
          <th>কৌশলগত বৈশিষ্ট্য (Key Focus)</th>
          <th>নম্বর (Marks)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>প্রশ্ন ১০ (Q10)</strong></td>
          <td>Completing a Story</td>
          <td>দেওয়া প্রম্পট অনুসরণ করে আকর্ষণীয় শিরোনামসহ ১৫০–২০০ শব্দের সুসংহত গল্প রচনা</td>
          <td><strong>১৫ নম্বর</strong></td>
        </tr>
        <tr>
          <td><strong>প্রশ্ন ১১ (Q11)</strong></td>
          <td>Writing a Dialogue</td>
          <td>দুইটি চরিত্রের মধ্যে বাস্তবসম্মত ও ব্যাকরণসম্মত ১০–১২টি টার্নের প্রাসঙ্গিক সংলাপ রচনা</td>
          <td><strong>১০ নম্বর</strong></td>
        </tr>
        <tr>
          <td colspan="3" style="text-align:right; font-weight:700; background:#f1f5f9;">মোট রাইটিং নম্বর (Total Writing Marks):</td>
          <td style="font-weight:700; background:#f1f5f9; color:#0c2340;"><strong>২৫ নম্বর</strong></td>
        </tr>
      </tbody>
    </table>
  </div>

  <h2 class="htbd-academic-heading" id="all-stories">২. ৩৪টি শীর্ষ Completing Story তালিকা ও প্রম্পট (All 34 Stories for SSC 2027)</h2>
  <p>নিচে জাতীয় পাঠ্যক্রম ও বিগত বোর্ড পরীক্ষার ৩৪টি সম্ভাব্য গল্পের প্রম্পট ও গুরুত্ব তালিকাভুক্ত করা হলো:</p>

  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 22px 0;">
    <table class="htbd-academic-table">
      <thead>
        <tr>
          <th style="width:6%;">ক্র.</th>
          <th style="width:40%;">গল্পের শিরোনাম ও প্রম্পট স্নিপেট</th>
          <th style="width:18%; text-align:center;">গুরুত্ব</th>
          <th style="width:36%;">বিগত বোর্ড পরীক্ষা</th>
        </tr>
      </thead>
      <tbody>
        {stories_rows}
      </tbody>
    </table>
  </div>

  <h2 class="htbd-academic-heading" id="all-dialogues">৩. ৩২টি শীর্ষ Dialogue Writing তালিকা ও প্রেক্ষাপট (All 32 Dialogues for SSC 2027)</h2>
  <p>নিচে ৩২টি গুরুত্বপূর্ণ ডায়ালগ টপিক, চরিত্র এবং প্রেক্ষাপটের তালিকা দেওয়া হলো:</p>

  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 22px 0;">
    <table class="htbd-academic-table">
      <thead>
        <tr>
          <th style="width:5%;">ক্র.</th>
          <th style="width:28%;">বিষয় ও চরিত্র</th>
          <th style="width:35%;">প্রেক্ষাপট ও আলোচনার বিষয়</th>
          <th style="width:14%; text-align:center;">গুরুত্ব</th>
          <th style="width:18%;">বোর্ড পরীক্ষা</th>
        </tr>
      </thead>
      <tbody>
        {dialogues_rows}
      </tbody>
    </table>
  </div>

  <h2 class="htbd-academic-heading" id="writing-rules">৪. গল্প ও ডায়ালগে পূর্ণ নম্বর পাওয়ার ৪টি পেশাদার নিয়ম (Writing Strategies)</h2>
  <ul style="line-height:1.85;">
    <li><strong>গল্পে উপযুক্ত শিরোনাম (Suitable Title):</strong> গল্পের শুরুতে একটি উপযুক্ত শিরোনাম লিখলে বোর্ড নিয়মে ২ নম্বর নিশ্চিত হয়। গল্পের মূলভাব স্পষ্ট করে এমন শিরোনাম দিন (যেমন: <em>"Where There is a Will, There is a Way"</em>)।</li>
    <li><strong>গল্পের ধারাবাহিক সমাপ্তি (Logical Resolution):</strong> প্রশ্নের দেওয়া প্রম্পটের বাক্যগুলো প্রথমে তুলবেন এবং তারপর নিজের ভাষায় গল্পের প্লটকে পূর্ণাঙ্গ রূপ দেবেন। হঠাৎ করে গল্প শেষ না করে একটি চমৎকার শিক্ষণীয় নীতিকথা (Moral) দিয়ে শেষ করুন।</li>
    <li><strong>ডায়ালগের সম্ভাষণ ও বিদায় (Greeting & Farewell):</strong> ডায়ালগ শুরু করবেন স্বাভাবিক সালাম বা কুশল বিনিময়ের মাধ্যমে (যেমন: <em>"Assalamu Alaikum"</em> বা <em>"Hello, how are you?"</em>) এবং শেষে আন্তরিক বিদায় সম্ভাষণ (যেমন: <em>"Thank you for this fruitful discussion"</em>) দিয়ে শেষ করবেন।</li>
    <li><strong>১০–১২টি তথ্যবহুল সংলাপ টার্ন (Conversational Turns):</strong> প্রতিটি চরিত্র কমপক্ষে ৫–৬ বার কথা বলবে (মোট ১০–১২টি টার্ন)। শুধু "Yes", "No" বা "I agree" না বলে যুক্তি ও তথ্যপূর্ণ পূর্ণাঙ্গ বাক্যে বক্তব্য উপস্থাপন করুন।</li>
  </ul>

  <h2 class="htbd-academic-heading" id="model-stories">৫. ৩টি পূর্ণাঙ্গ মডেল Completing Story সমাধান (Model Stories)</h2>
  
  <div style="background:#ffffff; border:1px solid #e2e8f0; border-left:4px solid #0c2340; border-radius:8px; padding:20px 24px; margin-bottom:24px;">
    <h3 style="margin:0 0 8px 0; color:#0c2340; font-size:19px; font-weight:700;">Story 01: {MODEL_STORY_LUCKY_TICKET['title']}</h3>
    <p style="margin:0 0 10px 0; font-size:14px; color:#64748b;"><strong>উৎস:</strong> NCTB Model Completing Story (Page 26)</p>
    <p style="background:#f8fafc; padding:12px 16px; border-radius:6px; font-style:italic; line-height:1.75; margin-bottom:14px;">"{MODEL_STORY_LUCKY_TICKET['prompt']}"</p>
    <div style="font-size:16.5px; line-height:1.85; color:#1e293b;">
      <p style="margin:0 0 10px 0;">{MODEL_STORY_LUCKY_TICKET['full_story'].replace(chr(10)+chr(10), '</p><p style=\"margin:0 0 10px 0;\">')}</p>
    </div>
  </div>

  <div style="background:#ffffff; border:1px solid #e2e8f0; border-left:4px solid #0c2340; border-radius:8px; padding:20px 24px; margin-bottom:24px;">
    <h3 style="margin:0 0 8px 0; color:#0c2340; font-size:19px; font-weight:700;">Story 02: {DAKHIL_2026_STORY['title']}</h3>
    <p style="margin:0 0 10px 0; font-size:14px; color:#64748b;"><strong>উৎস:</strong> {DAKHIL_2026_STORY['board']}</p>
    <p style="background:#f8fafc; padding:12px 16px; border-radius:6px; font-style:italic; line-height:1.75; margin-bottom:14px;">"{DAKHIL_2026_STORY['prompt']}"</p>
    <div style="font-size:16.5px; line-height:1.85; color:#1e293b;">
      <p style="margin:0 0 10px 0;">{DAKHIL_2026_STORY['full_story'].replace(chr(10)+chr(10), '</p><p style=\"margin:0 0 10px 0;\">')}</p>
    </div>
  </div>

  <div style="background:#ffffff; border:1px solid #e2e8f0; border-left:4px solid #0c2340; border-radius:8px; padding:20px 24px; margin-bottom:24px;">
    <h3 style="margin:0 0 8px 0; color:#0c2340; font-size:19px; font-weight:700;">Story 03: {MODEL_TEST_STORY['title']}</h3>
    <p style="margin:0 0 10px 0; font-size:14px; color:#64748b;"><strong>উৎস:</strong> {MODEL_TEST_STORY['board']}</p>
    <p style="background:#f8fafc; padding:12px 16px; border-radius:6px; font-style:italic; line-height:1.75; margin-bottom:14px;">"{MODEL_TEST_STORY['prompt']}"</p>
    <div style="font-size:16.5px; line-height:1.85; color:#1e293b;">
      <p style="margin:0 0 10px 0;">{MODEL_TEST_STORY['full_story'].replace(chr(10)+chr(10), '</p><p style=\"margin:0 0 10px 0;\">')}</p>
    </div>
  </div>

  <h2 class="htbd-academic-heading" id="model-dialogues">৬. ৭টি পূর্ণাঙ্গ মডেল Dialogue Writing সমাধান (Model Dialogues)</h2>

  <div style="background:#ffffff; border:1px solid #e2e8f0; border-left:4px solid #0284c7; border-radius:8px; padding:20px 24px; margin-bottom:24px;">
    <h3 style="margin:0 0 8px 0; color:#0284c7; font-size:19px; font-weight:700;">Dialogue 01: {MODEL_DIALOGUES_VERBATIM['dialogue_28']['title']}</h3>
    {d28_html}
  </div>

  <div style="background:#ffffff; border:1px solid #e2e8f0; border-left:4px solid #0284c7; border-radius:8px; padding:20px 24px; margin-bottom:24px;">
    <h3 style="margin:0 0 8px 0; color:#0284c7; font-size:19px; font-weight:700;">Dialogue 02: {MODEL_DIALOGUES_VERBATIM['dialogue_29']['title']}</h3>
    <p style="margin:0 0 10px 0; font-size:13.5px; color:#64748b;">বোর্ড: {MODEL_DIALOGUES_VERBATIM['dialogue_29']['board']}</p>
    {d29_html}
  </div>

  <div style="background:#ffffff; border:1px solid #e2e8f0; border-left:4px solid #0284c7; border-radius:8px; padding:20px 24px; margin-bottom:24px;">
    <h3 style="margin:0 0 8px 0; color:#0284c7; font-size:19px; font-weight:700;">Dialogue 03: {MODEL_DIALOGUES_VERBATIM['dialogue_30']['title']}</h3>
    <p style="margin:0 0 10px 0; font-size:13.5px; color:#64748b;">বোর্ড: {MODEL_DIALOGUES_VERBATIM['dialogue_30']['board']}</p>
    {d30_html}
  </div>

  <div style="background:#ffffff; border:1px solid #e2e8f0; border-left:4px solid #0284c7; border-radius:8px; padding:20px 24px; margin-bottom:24px;">
    <h3 style="margin:0 0 8px 0; color:#0284c7; font-size:19px; font-weight:700;">Dialogue 04: {MODEL_DIALOGUES_VERBATIM['dialogue_31']['title']}</h3>
    {d31_html}
  </div>

  <div style="background:#ffffff; border:1px solid #e2e8f0; border-left:4px solid #0284c7; border-radius:8px; padding:20px 24px; margin-bottom:24px;">
    <h3 style="margin:0 0 8px 0; color:#0284c7; font-size:19px; font-weight:700;">Dialogue 05: {MODEL_DIALOGUES_VERBATIM['dialogue_32']['title']}</h3>
    {d32_html}
  </div>

  <div style="background:#ffffff; border:1px solid #e2e8f0; border-left:4px solid #0284c7; border-radius:8px; padding:20px 24px; margin-bottom:24px;">
    <h3 style="margin:0 0 8px 0; color:#0284c7; font-size:19px; font-weight:700;">Dialogue 06: {DAKHIL_2026_DIALOGUE['title']}</h3>
    <p style="margin:0 0 10px 0; font-size:13.5px; color:#64748b;">উৎস: {DAKHIL_2026_DIALOGUE['board']}</p>
    {dakhil_d_html}
  </div>

  <div style="background:#ffffff; border:1px solid #e2e8f0; border-left:4px solid #0284c7; border-radius:8px; padding:20px 24px; margin-bottom:24px;">
    <h3 style="margin:0 0 8px 0; color:#0284c7; font-size:19px; font-weight:700;">Dialogue 07: {MODEL_TEST_DIALOGUE['title']}</h3>
    <p style="margin:0 0 10px 0; font-size:13.5px; color:#64748b;">উৎস: {MODEL_TEST_DIALOGUE['board']}</p>
    {model_d_html}
  </div>

  <h2 class="htbd-academic-heading" id="faq">৭. সচরাচর জিজ্ঞাসা (FAQ)</h2>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">Question 1: Completing Story-তে টাইটেল না দিলে কি নম্বর কাটা যায়?</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">উত্তর: হ্যাঁ, বোর্ড পরীক্ষার নির্দেশনা অনুযায়ী গল্পের একটি চমৎকার ও প্রাসঙ্গিক শিরোনামের জন্য আলাদা ২ নম্বর বরাদ্দ থাকে। তাই শিরোনাম কখনোই বাদ দেওয়া যাবে না।</p>
  </div>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">Question 2: Dialogue Writing-এ কত জোড়া সংলাপ লেখা আদর্শ?</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">উত্তর: আদর্শ সংলাপে প্রতিটি চরিত্রের কমপক্ষে ৫ থেকে ৬টি করে অর্থপূর্ণ বক্তব্য অর্থাৎ মোট ১০ থেকে ১২টি সংলাপ টার্ন থাকা উচিত। খুব ছোট সংলাপে পুরো নম্বর পাওয়া কঠিন।</p>
  </div>
  <div class="htbd-faq-item">
    <p style="margin:0 0 6px 0; font-weight:700; color:#0c2340; font-size:18px;">Question 3: প্রম্পটের বাক্যগুলো কি উত্তরপত্রে লিখতে হবে?</p>
    <p style="margin:0; color:#334155; font-size:17px; line-height:1.75;">উত্তর: হ্যাঁ, প্রশ্নপত্রে যে প্রম্পট দেওয়া থাকে, সেই অংশটুকু উত্তরপত্রে প্রথমে তুলে তারপর গল্পের স্বাভাবিক সমাপ্তি পর্যন্ত নিজস্ব বাক্য যোগ করতে হবে।</p>
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
    {{"@type": "Question", "name": "Will I lose marks if I omit the story title in Q10?", "acceptedAnswer": {{"@type": "Answer", "text": "Yes, board evaluation allocates up to 2 marks specifically for a suitable and meaningful story title."}}}},
    {{"@type": "Question", "name": "How many conversational turns should a dialogue contain in Q11?", "acceptedAnswer": {{"@type": "Answer", "text": "A standard dialogue should feature at least 10 to 12 meaningful exchanges between the speakers."}}}},
    {{"@type": "Question", "name": "Should I write the given prompt before continuing the story?", "acceptedAnswer": {{"@type": "Answer", "text": "Yes, always copy the beginning prompt into your script before narrating your creative continuation."}}}}
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
    print(f"Silo 05 generated successfully! Length: {len(html)} chars, Slug: {slug}")
