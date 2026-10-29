#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/post_builders/master_suggestion_compiler.py
-------------------------------------------------
Universal Subject Suggestion Compiler for HelpTrickBD.
Parses 100% of questions from 'Publication Books/questions' directory,
formats them into high-converting, responsive, dark-mode compatible HTML,
embeds Rank Math 90+ SEO signals, schema microdata, and author cards.

Supports:
1. Audit & Assurance (নিরীক্ষা ও নিশ্চয়তা - Code: 232501) -> 10 Units, 288 Questions
2. Advanced Accounting-I (উন্নত হিসাববিজ্ঞান-১ - Code: 232503) -> 5 Units, 245 Questions
"""

import os
import sys
import re
import glob
import json
import yaml
from markdown_it import MarkdownIt

# Initialize markdown-it with tables and strikethrough
md_engine = MarkdownIt('commonmark').enable('table').enable('strikethrough')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PUB_BOOKS_BASE = r'D:\android\Project\Publication Books\questions'

def parse_question_file(filepath):
    """Parses a single markdown question file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        raw = f.read()
    parts = raw.split('---')
    if len(parts) < 3:
        return None
    fm = yaml.safe_load(parts[1])
    body = '---'.join(parts[2:]).strip()
    
    sec = fm.get('section', '').strip()
    if sec == 'খ/গ':
        sec = 'গ'
    q_no = fm.get('question_number') or fm.get('q_no') or 0
    imp = fm.get('importance', 2)
    
    # Normalize importance
    if isinstance(imp, str):
        if '★★★' in imp or '3' in imp:
            imp_val = 3
        elif '★★' in imp or '2' in imp:
            imp_val = 2
        else:
            imp_val = 1
    elif isinstance(imp, int):
        imp_val = imp
    else:
        imp_val = 2
        
    if imp_val >= 3:
        imp_badge = '<span class="htbd-badge-star golden">[৩-স্টার গোল্ডেন]</span>'
    elif imp_val == 2:
        imp_badge = '<span class="htbd-badge-star super">[২-স্টার সুপার]</span>'
    else:
        imp_badge = '<span class="htbd-badge-star regular">[১-স্টার সাধারণ]</span>'
        
    exam_years = fm.get('exam_years', [])
    year_strings = []
    if isinstance(exam_years, list):
        for ey in exam_years:
            if isinstance(ey, dict):
                uni = str(ey.get('university', '')).strip()
                yr = str(ey.get('year', '')).strip()
                qno = str(ey.get('question_number', '') or ey.get('q_no', '')).strip()
                piece = f"{uni} {yr}".strip()
                if qno:
                    piece += f" ({qno})"
                if piece:
                    year_strings.append(piece)
            elif isinstance(ey, (str, int)):
                year_strings.append(str(ey).strip())
    year_badge = ""
    if year_strings:
        year_badge = f'<span class="htbd-badge-year">{", ".join(year_strings)}</span>'
        
    # Split question from answer
    ans_split = re.split(r'\n##\s*(?:সমাধান\s*/\s*উত্তর|উত্তর\s*/\s*সমাধান|উত্তর|সমাধান)[\s:]*', body, flags=re.IGNORECASE)
    if len(ans_split) >= 2:
        q_raw = ans_split[0].strip()
        ans_text = ans_split[1].strip()
        q_raw = re.sub(r'^##?\s*(?:প্রশ্ন|Question)?[\s:]*', '', q_raw, flags=re.IGNORECASE).strip()
        q_raw = re.sub(r'^(?:[0-9]+|[০-৯]+)[\.\)]\s*', '', q_raw).strip()
        q_text = q_raw
    else:
        lines = body.split('\n')
        first_line = lines[0]
        q_text = re.sub(r'^##?\s*(?:প্রশ্ন|Question)?[\s:]*', '', first_line, flags=re.IGNORECASE).strip()
        q_text = re.sub(r'^(?:[0-9]+|[০-৯]+)[\.\)]\s*', '', q_text).strip()
        ans_text = '\n'.join(lines[1:]).strip()
        
    ans_html = md_engine.render(ans_text)
    
    # Strip emojis and forbidden star glyphs per Zero-Emoji Policy
    ans_html = ans_html.replace('★', '').replace('⭐', '').replace('✨', '')
    q_text = q_text.replace('★', '').replace('⭐', '').replace('✨', '')
    
    return {
        'id': fm.get('id', ''),
        'section': sec,
        'q_no': q_no,
        'imp_val': imp_val,
        'imp_badge': imp_badge,
        'year_badge': year_badge,
        'q_text': q_text,
        'ans_html': ans_html
    }

def get_shared_css():
    """CSS styling for SolaimanLipi, cards, responsive tables, and dark mode."""
    return """<!-- Modern Typography & Layout Styling -->
<link href="https://cdn.jsdelivr.net/gh/maateen/ekushey-cdn@1.0/fonts/solaiman-lipi/stylesheet.css" rel="stylesheet" type="text/css" />
<style>
  .htbd-nu-content {
    font-family: 'SolaimanLipi', Arial, sans-serif;
    color: #1e293b;
    line-height: 1.85;
    font-size: 16.5px;
  }
  .htbd-nu-content h2 {
    font-family: 'SolaimanLipi', sans-serif;
    color: #0b2046;
    font-size: 24px;
    font-weight: 700;
    margin: 40px 0 20px 0;
    border-bottom: 2.5px solid #0b2046;
    padding-bottom: 10px;
  }
  .htbd-nu-content h3 {
    font-family: 'SolaimanLipi', sans-serif;
    color: #1e3a8a;
    font-size: 20px;
    font-weight: 700;
    margin: 30px 0 15px 0;
  }
  .htbd-nu-content p {
    margin-bottom: 18px;
    text-align: justify;
  }
  .htbd-hero-box {
    background: linear-gradient(135deg, #f0fdf4 0%, #e0f2fe 100%);
    border-left: 5px solid #059669;
    padding: 24px;
    border-radius: 10px;
    margin-bottom: 30px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.04);
  }
  .htbd-hero-box p {
    margin-bottom: 10px;
  }
  .htbd-hero-box p:last-child {
    margin-bottom: 0;
  }
  .htbd-toc-container {
    background: #f8fafc;
    border: 1.5px solid #cbd5e1;
    border-radius: 12px;
    padding: 22px 26px;
    margin: 30px 0;
  }
  .htbd-toc-title {
    font-size: 19px;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 14px;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 1px dashed #cbd5e1;
    padding-bottom: 8px;
  }
  .htbd-toc-list {
    margin: 0;
    padding-left: 20px;
    column-count: 2;
    column-gap: 30px;
  }
  @media (max-width: 640px) {
    .htbd-toc-list {
      column-count: 1;
    }
  }
  .htbd-toc-list li {
    margin-bottom: 8px;
  }
  .htbd-toc-list a {
    color: #2563eb;
    text-decoration: none;
    font-weight: 500;
  }
  .htbd-toc-list a:hover {
    text-decoration: underline;
    color: #1d4ed8;
  }
  .htbd-table-wrapper {
    overflow-x: auto;
    margin: 25px 0;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
  }
  .htbd-table-wrapper table, table.htbd-styled-table {
    width: 100%;
    border-collapse: collapse;
    font-family: 'SolaimanLipi', sans-serif;
    background: #ffffff;
  }
  .htbd-table-wrapper th, table.htbd-styled-table th {
    background: #0b2046;
    color: #ffffff;
    padding: 12px 16px;
    text-align: left;
    font-weight: 600;
    font-size: 15px;
  }
  .htbd-table-wrapper td, table.htbd-styled-table td {
    padding: 12px 16px;
    border-bottom: 1px solid #e2e8f0;
    font-size: 15px;
  }
  .htbd-table-wrapper tr:nth-child(even), table.htbd-styled-table tr:nth-child(even) {
    background: #f8fafc;
  }
  .htbd-table-wrapper tr:hover, table.htbd-styled-table tr:hover {
    background: #f1f5f9;
  }
  .htbd-q-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-left: 4.5px solid #2563eb;
    border-radius: 10px;
    padding: 20px 22px;
    margin-bottom: 22px;
    box-shadow: 0 3px 10px rgba(0,0,0,0.03);
    transition: transform 0.2s ease;
  }
  .htbd-q-card.card-b {
    border-left-color: #059669;
  }
  .htbd-q-card.card-c {
    border-left-color: #7c3aed;
  }
  .htbd-q-header {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 8px;
    margin-bottom: 10px;
  }
  .htbd-badge-sec {
    background: #e0e7ff;
    color: #3730a3;
    font-size: 12px;
    font-weight: 700;
    padding: 3px 9px;
    border-radius: 6px;
  }
  .htbd-badge-star {
    font-size: 12px;
    font-weight: 700;
    padding: 3px 9px;
    border-radius: 6px;
  }
  .htbd-badge-star.golden {
    background: #fef3c7;
    color: #92400e;
    border: 1px solid #fde68a;
  }
  .htbd-badge-star.super {
    background: #e0f2fe;
    color: #0369a1;
    border: 1px solid #bae6fd;
  }
  .htbd-badge-star.regular {
    background: #f1f5f9;
    color: #475569;
  }
  .htbd-badge-year {
    background: #ecfdf5;
    color: #065f46;
    font-size: 12px;
    font-weight: 600;
    padding: 3px 9px;
    border-radius: 6px;
    border: 1px solid #a7f3d0;
  }
  .htbd-q-title {
    font-size: 17px;
    font-weight: 700;
    color: #0f172a;
    line-height: 1.6;
    margin: 6px 0 12px 0;
  }
  .htbd-ans-box {
    background: #f8fafc;
    border-radius: 8px;
    padding: 16px 18px;
    border-top: 1px dashed #cbd5e1;
    font-size: 15.5px;
    color: #334155;
    line-height: 1.8;
  }
  .htbd-ans-box p {
    margin-bottom: 12px;
  }
  .htbd-ans-box p:last-child {
    margin-bottom: 0;
  }
  .htbd-ans-box ul, .htbd-ans-box ol {
    margin: 8px 0 14px 22px;
    padding: 0;
  }
  .htbd-ans-box li {
    margin-bottom: 6px;
  }
  .htbd-ans-box table {
    width: 100%;
    border-collapse: collapse;
    margin: 14px 0;
    font-size: 14px;
    background: #ffffff;
  }
  .htbd-ans-box th, .htbd-ans-box td {
    border: 1px solid #cbd5e1;
    padding: 8px 12px;
    text-align: left;
  }
  .htbd-ans-box th {
    background: #f1f5f9;
    font-weight: 700;
  }
  .htbd-callout-warning {
    background: #fffbeb;
    border-left: 4.5px solid #d97706;
    padding: 16px 20px;
    border-radius: 8px;
    margin: 25px 0;
    color: #92400e;
  }
  .htbd-author-box {
    display: flex;
    gap: 20px;
    align-items: center;
    background: #f8fafc;
    border: 1.5px solid #e2e8f0;
    padding: 24px;
    border-radius: 12px;
    margin: 40px 0;
  }
  .htbd-author-avatar {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    object-fit: cover;
    flex-shrink: 0;
    border: 2px solid #2563eb;
  }
  .htbd-author-info h4 {
    margin: 0 0 6px 0;
    font-size: 18px;
    color: #0f172a;
    font-weight: 700;
  }
  .htbd-author-info p {
    margin: 0;
    font-size: 14.5px;
    color: #64748b;
    line-height: 1.6;
  }

  /* Dark mode compatibility */
  @media (prefers-color-scheme: dark) {
    .dark-mode .htbd-nu-content, body.dark-theme .htbd-nu-content {
      color: #e2e8f0;
    }
    .dark-mode .htbd-nu-content h2, body.dark-theme .htbd-nu-content h2 {
      color: #93c5fd;
      border-bottom-color: #3b82f6;
    }
    .dark-mode .htbd-nu-content h3, body.dark-theme .htbd-nu-content h3 {
      color: #bfdbfe;
    }
    .dark-mode .htbd-hero-box, body.dark-theme .htbd-hero-box {
      background: #064e3b;
      border-left-color: #10b981;
      color: #ecfdf5;
    }
    .dark-mode .htbd-toc-container, body.dark-theme .htbd-toc-container {
      background: #0f172a;
      border-color: #334155;
    }
    .dark-mode .htbd-toc-title, body.dark-theme .htbd-toc-title {
      color: #f8fafc;
      border-bottom-color: #334155;
    }
    .dark-mode .htbd-toc-list a, body.dark-theme .htbd-toc-list a {
      color: #60a5fa;
    }
    .dark-mode .htbd-q-card, body.dark-theme .htbd-q-card {
      background: #1e293b;
      border-color: #334155;
    }
    .dark-mode .htbd-q-title, body.dark-theme .htbd-q-title {
      color: #f1f5f9;
    }
    .dark-mode .htbd-ans-box, body.dark-theme .htbd-ans-box {
      background: #0f172a;
      border-top-color: #334155;
      color: #cbd5e1;
    }
    .dark-mode .htbd-author-box, body.dark-theme .htbd-author-box {
      background: #0f172a;
      border-color: #334155;
    }
    .dark-mode .htbd-author-info h4, body.dark-theme .htbd-author-info h4 {
      color: #f8fafc;
    }
    .dark-mode .htbd-author-info p, body.dark-theme .htbd-author-info p {
      color: #94a3b8;
    }
  }
</style>"""

def get_author_box_html():
    """Generates the official Faruk Sir author card."""
    return """<div class="htbd-author-box">
  <img src="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/authors/faruk_sir.webp" alt="মো: ওমর ফারুক" class="htbd-author-avatar" width="80" height="80" loading="lazy" />
  <div class="htbd-author-info">
    <h4>মো: ওমর ফারুক (Faruk Sir)</h4>
    <p>প্রতিষ্ঠাতা ও প্রধান শিক্ষা সম্পাদক, HelpTrickBD। জাতীয় বিশ্ববিদ্যালয়ের হিসাববিজ্ঞান ও ব্যবসায় শিক্ষা অনুষদের শিক্ষার্থীদের জন্য দীর্ঘ ৮+ বছর যাবত মানসম্মত একাডেমিক গাইড, হ্যান্ডনোট ও চূড়ান্ত সাজেশন প্রণয়ন করছেন।</p>
  </div>
</div>"""

def generate_subject_html(
    subject_title: str,
    subject_code: str,
    focus_kw: str,
    seo_title: str,
    banner_url: str,
    units_config: list,
    prefix: str,
    marks_table_html: str,
    faq_items: list,
    intro_p1: str,
    intro_p2: str,
    canonical_url: str
):
    """Generates complete monolithic HTML for a subject with 100% of questions."""
    
    # 1. Parse all questions per unit
    all_units_data = []
    total_q_count = 0
    total_sec_counts = {'ক': 0, 'খ': 0, 'গ': 0}
    
    for u_cfg in units_config:
        u_dir = u_cfg['dir']
        u_num = u_cfg['num']
        u_title = u_cfg['title']
        u_weight = u_cfg.get('weight', '১২–১৫ নম্বর')
        
        dp = os.path.join(PUB_BOOKS_BASE, u_dir)
        files = glob.glob(os.path.join(dp, '*.md'))
        
        secs = {'ক': [], 'খ': [], 'গ': []}
        for f in files:
            res = parse_question_file(f)
            if res:
                s = res['section']
                if s in secs:
                    secs[s].append(res)
                    total_sec_counts[s] += 1
                    total_q_count += 1
                else:
                    print(f"Unknown section: {s} in {f}")
                    
        # Sort questions by q_no
        for s in ['ক', 'খ', 'গ']:
            secs[s].sort(key=lambda x: x['q_no'])
            
        all_units_data.append({
            'dir': u_dir,
            'num': u_num,
            'title': u_title,
            'weight': u_weight,
            'secs': secs,
            'count': len(secs['ক']) + len(secs['খ']) + len(secs['গ'])
        })

    # 2. Build TOC HTML
    toc_links = []
    for u in all_units_data:
        anchor_id = f"unit-{u['num']}"
        toc_links.append(f'<li><a href="#{anchor_id}">অধ্যায় {u["num"]}: {u["title"]} ({u["count"]}টি প্রশ্ন)</a></li>')
    toc_links.append('<li><a href="#nu-exam-strategy">জাতীয় বিশ্ববিদ্যালয় পরীক্ষার প্রস্তুতি ও রিভিশন কৌশল</a></li>')
    toc_links.append('<li><a href="#faq-section">সচরাচর জিজ্ঞাসিত প্রশ্নোত্তর (FAQ)</a></li>')
    
    toc_html = f"""<div id="rank-math-toc" class="htbd-toc-container">
  <div class="htbd-toc-title">
    সূচিপত্র: বিষয়ভিত্তিক অধ্যায় ও সম্পূর্ণ প্রশ্নাবলি
  </div>
  <ol class="htbd-toc-list">
    {''.join(toc_links)}
  </ol>
</div>"""

    # 3. Build Question Blocks per Unit
    units_body_html = []
    for u in all_units_data:
        anchor_id = f"unit-{u['num']}"
        u_html = [f'<div class="htbd-unit-block" id="{anchor_id}">']
        u_html.append(f'<h2>অধ্যায় {u["num"]}: {u["title"]}</h2>')
        u_html.append(f'<p style="color: #475569; font-weight: 500;"><strong>সিলেবাস গুরুত্ব ও মানবণ্টন:</strong> জাতীয় বিশ্ববিদ্যালয়ের বিগত বছরের প্রশ্ন পর্যালোচনায় এ অধ্যায়টি থেকে পরীক্ষায় প্রায় {u["weight"]} প্রশ্ন কমন পাওয়া যায়। নিম্নে ক, খ ও গ বিভাগের সকল প্রশ্ন ক্রমানুসারে দেওয়া হলো:</p>')
        
        # Section A
        if u['secs']['ক']:
            u_html.append(f'<h3>ক-বিভাগ: অতি সংক্ষিপ্ত প্রশ্নাবলি ({u["title"]})</h3>')
            u_html.append(f'<p>অতি সংক্ষিপ্ত প্রশ্নের নির্ভুল ও টু-দ্য-পয়েন্ট উত্তর নিচে দেওয়া হলো। পরীক্ষায় পূর্ণ ১ নম্বর পেতে সংজ্ঞার মূল টার্ম ও প্রাসঙ্গিক ধারা বা মান সঠিকভাবে উল্লেখ করুন:</p>')
            for q in u['secs']['ক']:
                u_html.append(f"""<div class="htbd-q-card">
  <div class="htbd-q-header">
    <span class="htbd-badge-sec">ক-বিভাগ (১ নম্বর)</span>
    {q['imp_badge']}
    {q['year_badge']}
  </div>
  <div class="htbd-q-title">প্রশ্ন {q['q_no']}. {q['q_text']}</div>
  <div class="htbd-ans-box">
    <strong>উত্তর:</strong> {q['ans_html']}
  </div>
</div>""")

        # Section B
        if u['secs']['খ']:
            u_html.append(f'<h3>খ-বিভাগ: সংক্ষিপ্ত প্রশ্নাবলি ও সমস্যাবলি ({u["title"]})</h3>')
            u_html.append(f'<p>খ-বিভাগের প্রতি প্রশ্নের মান ৪ নম্বর। পয়েন্টভিত্তিক স্পষ্ট উপস্থাপন ও প্রয়োজনীয় গণনাকার্য বা জার্নাল এন্ট্রি নিচে দেওয়া হলো:</p>')
            for q in u['secs']['খ']:
                u_html.append(f"""<div class="htbd-q-card card-b">
  <div class="htbd-q-header">
    <span class="htbd-badge-sec" style="background: #d1fae5; color: #065f46;">খ-বিভাগ (৪ নম্বর)</span>
    {q['imp_badge']}
    {q['year_badge']}
  </div>
  <div class="htbd-q-title">প্রশ্ন {q['q_no']}. {q['q_text']}</div>
  <div class="htbd-ans-box">
    {q['ans_html']}
  </div>
</div>""")

        # Section C
        if u['secs']['গ']:
            u_html.append(f'<h3>গ-বিভাগ: রচনামূলক ও বিশ্লেষণধর্মী প্রশ্নাবলি ({u["title"]})</h3>')
            u_html.append(f'<p>গ-বিভাগের প্রতিটি প্রশ্নের মান ১০ নম্বর। পূর্ণাঙ্গ পরীক্ষার নম্বর অর্জনের জন্য ভূমিকা, ধারাবাহিক পয়েন্ট, ছক এবং উপসংহারের পরিপূর্ণ সমাধান নিচে দেওয়া হলো:</p>')
            for q in u['secs']['গ']:
                u_html.append(f"""<div class="htbd-q-card card-c">
  <div class="htbd-q-header">
    <span class="htbd-badge-sec" style="background: #ede9fe; color: #5b21b6;">গ-বিভাগ (১০ নম্বর)</span>
    {q['imp_badge']}
    {q['year_badge']}
  </div>
  <div class="htbd-q-title">প্রশ্ন {q['q_no']}. {q['q_text']}</div>
  <div class="htbd-ans-box">
    {q['ans_html']}
  </div>
</div>""")
                
        u_html.append('</div>')
        units_body_html.append('\n'.join(u_html))

    all_units_rendered = '\n\n'.join(units_body_html)

    # 4. FAQ Schema & HTML
    faq_html_items = []
    faq_schema_items = []
    for idx, item in enumerate(faq_items, 1):
        q = item['q']
        a = item['a']
        faq_html_items.append(f"""<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px 20px; margin-bottom: 12px;">
  <h4 style="margin: 0 0 8px 0; color: #0b2046; font-size: 16.5px;">{idx}. {q}</h4>
  <p style="margin: 0; color: #475569; font-size: 15px;">{a}</p>
</div>""")
        faq_schema_items.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a
            }
        })

    faq_schema_json = json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": faq_schema_items
    }, ensure_ascii=False, indent=2)

    blog_schema_json = json.dumps({
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": seo_title,
        "description": f"{focus_kw} 2026: জাতীয় বিশ্ববিদ্যালয় BBA ৩য় বর্ষ হিসাববিজ্ঞান বিভাগের ক, খ ও গ বিভাগের ১০০% কমন উপযোগী পূর্ণাঙ্গ সাজেশন ও সমাধান।",
        "image": banner_url,
        "author": {
            "@type": "Person",
            "name": "Faruk Sir",
            "url": "https://www.helptrickbd.com/about-us"
        },
        "publisher": {
            "@type": "Organization",
            "name": "HelpTrickBD",
            "logo": {
                "@type": "ImageObject",
                "url": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/logo/helptrickbd_logo.png"
            }
        },
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": canonical_url
        }
    }, ensure_ascii=False, indent=2)

    # 5. Full HTML assembly
    full_html = f"""<!-- Byte-0 Hero Banner Placement -->
<figure class="htbd-featured-hero" style="margin: 0 0 25px 0; text-align: center;">
  <img src="{banner_url}" alt="{focus_kw}" title="{seo_title}" style="width: 100%; max-width: 1000px; height: auto; border-radius: 12px; box-shadow: 0 5px 20px rgba(0,0,0,0.12); display: block; margin: 0 auto;" loading="eager" width="1200" height="675" />
  <figcaption style="font-family: 'SolaimanLipi', sans-serif; font-size: 14px; color: #64748b; margin-top: 8px; text-align: center;">
    জাতীয় বিশ্ববিদ্যালয় BBA অনার্স ৩য় বর্ষ {subject_title} ফাইনাল সাজেশন 2026 (ক, খ ও গ বিভাগ সম্পূর্ণ) | প্রকাশনা: HelpTrickBD
  </figcaption>
</figure>

{get_shared_css()}

<div class="htbd-nu-content">

  <!-- Breadcrumb & Topic Metadata -->
  <div style="font-size: 13.5px; color: #64748b; margin-bottom: 20px;">
    হোম / শিক্ষা ও সাজেশন / অনার্স ৩য় বর্ষ / <strong>{subject_title} সাজেশন</strong> (কোর্স কোড: {subject_code})
  </div>

  <!-- Position 0 Quick Answer Box -->
  <div class="htbd-hero-box">
    <h3 style="margin-top: 0; color: #065f46; font-size: 19px;">[কোর্স ওভারভিউ] একনজরে {focus_kw} 2026</h3>
    <p><strong>{focus_kw}</strong> খুঁজছেন এমন জাতীয় বিশ্ববিদ্যালয়ের হিসাববিজ্ঞান বিভাগের শিক্ষার্থীদের জন্য এটি একটি প্রামাণ্য ও নির্ভুল পূর্ণাঙ্গ স্টাডি রিসোর্স। জাতীয় বিশ্ববিদ্যালয়ের সর্বশেষ সিলেবাস, বিগত ১০ বছরের বোর্ড প্রশ্ন এবং কলেজ টেস্ট পেপারসের চুলচেরা বিশ্লেষণ করে এ সাজেশনে মোট <strong>{total_q_count}টি বাছাইকৃত প্রশ্ন ও পূর্ণাঙ্গ সমাধান</strong> সন্নিবেশিত করা হয়েছে।</p>
    <p>সাজেশনটিতে ক-বিভাগের <strong>{total_sec_counts['ক']}টি অতি সংক্ষিপ্ত প্রশ্ন</strong>, খ-বিভাগের <strong>{total_sec_counts['খ']}টি সংক্ষিপ্ত ও গাণিতিক সমস্যা</strong> এবং গ-বিভাগের <strong>{total_sec_counts['গ']}টি বিশ্লেষণধর্মী ও রচনামূলক প্রশ্নের</strong> অধ্যায়ভিত্তিক পূর্ণাঙ্গ সমাধান অন্তর্ভুক্ত রয়েছে।</p>
  </div>

  <!-- Mandatory Jump Break for Archive Summary -->
  <!--more-->

  <p>{intro_p1}</p>
  <p>{intro_p2}</p>

  {toc_html}

  <h2>জাতীয় বিশ্ববিদ্যালয় পরীক্ষার মানবণ্টন ও প্রশ্ন কাঠামোর বিশ্লেষণ (৮০ নম্বর)</h2>
  <p>জাতীয় বিশ্ববিদ্যালয়ের অনার্স ৩য় বর্ষের চূড়ান্ত লিখিত পরীক্ষা মোট ৮০ নম্বরে অনুষ্ঠিত হয়। অবশিষ্ট ২০ নম্বর ইনকোর্স ও ক্লাস উপস্থিতির ওপর নির্ধারিত। পরীক্ষায় সর্বোচ্চ নম্বর নিশ্চিত করতে তিনটি বিভাগের প্রশ্ন কাঠামোর ওপর পরিষ্কার ধারণা থাকা অপরিহার্য:</p>

  {marks_table_html}

  {all_units_rendered}

  <div id="nu-exam-strategy">
    <h2>জাতীয় বিশ্ববিদ্যালয় পরীক্ষার প্রস্তুতি ও রিভিশন কৌশল</h2>
    <p>জাতীয় বিশ্ববিদ্যালয়ের চূড়ান্ত পরীক্ষায় ৯০%+ নম্বর অর্জনের জন্য একটি সুশৃঙ্খল রিভিশন রুটিন অনুসরণ করা প্রয়োজন। অভিজ্ঞ শিক্ষকদের সমন্বয়ে প্রস্তুতকৃত বিশেষ প্রস্তুতি কৌশল নিচে তুলে ধরা হলো:</p>
    <div class="htbd-table-wrapper">
      <table class="htbd-styled-table">
        <thead>
          <tr>
            <th>প্রস্তুতির স্তর</th>
            <th>মূল করণীয় ও দিকনির্দেশনা</th>
            <th>প্রত্যাশিত সাফল্য</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>ক-বিভাগ (১-১০ দিন)</strong></td>
            <td>প্রতিটি অধ্যায়ের [৩-স্টার গোল্ডেন] চিহ্নিত অতি সংক্ষিপ্ত প্রশ্নগুলো মুখস্থ করে খাতায় লিখে ফেলুন। কোনো অপ্রয়োজনীয় ভূমিকা ছাড়া সরাসরি এক বাক্যে মূল টার্ম লিখুন।</td>
            <td>১০ নম্বরে ১০ নম্বর নিশ্চিত</td>
          </tr>
          <tr>
            <td><strong>খ ও গ বিভাগ (১১-২৫ দিন)</strong></td>
            <td>তাত্ত্বিক প্রশ্নের ক্ষেত্রে ৩-৪টি স্ট্যান্ডার্ড সংজ্ঞা, বৈশিষ্ট্য ও পার্থক্যের ছক অনুশীলন করুন। গাণিতিক অধ্যায়গুলোর জাবেদা ও ছক নির্ভুল রাখুন।</td>
            <td>সংক্ষিপ্ত ও বড় প্রশ্নে সর্বোচ্চ নম্বর</td>
          </tr>
          <tr>
            <td><strong>মডেল টেস্ট (শেষ ৫ দিন)</strong></td>
            <td>বিগত ৪ বছরের বোর্ড প্রশ্নের ওপর ভিত্তি করে সময় ধরে পূর্ণ ৮০ নম্বরের ২টি হ্যান্ডরিটেন পরীক্ষা দিন। হাতের লেখার স্পষ্টতা ও গতি বৃদ্ধি পাবে।</td>
            <td>পরীক্ষার হলে শতভাগ আত্মবিশ্বাস</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div id="faq-section">
    <h2>সচরাচর জিজ্ঞাসিত প্রশ্নোত্তর (FAQ)</h2>
    {''.join(faq_html_items)}
  </div>

  <div class="htbd-callout-warning">
    <strong>[সতর্কবার্তা] কপিরাইট ও প্রাতিষ্ঠানিক নোটিশ:</strong> HelpTrickBD-এর সকল কনটেন্ট জাতীয় বিশ্ববিদ্যালয়ের সম্মানিত শিক্ষক ও বিষয় বিশেষজ্ঞদের সার্বিক তত্ত্বাবধানে শিক্ষার্থীদের বিনামূল্যে সহায়তা প্রদানে সংকলিত। জাতীয় বিশ্ববিদ্যালয়ের সর্বশেষ একাডেমিক নোটিশ ও ফরম পূরণের তথ্যের জন্য অফিসিয়াল <a href="https://www.nu.ac.bd/" target="_blank" rel="noopener noreferrer">জাতীয় বিশ্ববিদ্যালয় পোর্টাল (nu.ac.bd)</a> পরিদর্শন করুন। আরও সাজেশন পেতে আমাদের <a href="https://www.helptrickbd.com/category/education/">শিক্ষা সহায়িকা ও স্টাডি গাইড</a> আর্কাইভ দেখুন। কোনো বাণিজ্যিক প্ল্যাটফর্মে অনুমোদনহীন পুনঃপ্রকাশ আইনত দণ্ডনীয়।
  </div>

  {get_author_box_html()}

</div>

<!-- Schema.org Microdata -->
<script type="application/ld+json">
{blog_schema_json}
</script>
<script type="application/ld+json">
{faq_schema_json}
</script>
"""
    return full_html


def compile_audit_post():
    """Compiles the complete 288-question Audit & Assurance post."""
    units_config = [
        {"dir": "unit01", "num": "০১", "title": "নিরীক্ষার চাহিদা এবং অন্যান্য নিশ্চয়তা সেবা (Demand for Audit & Assurance)", "weight": "১০–১২ নম্বর"},
        {"dir": "unit02", "num": "০২", "title": "হিসাব নিরীক্ষা পেশা ও নিরীক্ষা মান (The CPA Profession & Standards)", "weight": "৮–১০ নম্বর"},
        {"dir": "unit03", "num": "০৩", "title": "নিরীক্ষা প্রতিবেদন (Audit Reports & Audit Opinions)", "weight": "১০–১৪ নম্বর"},
        {"dir": "unit04", "num": "০৪", "title": "আইনগত দায় ও বিধিবদ্ধ বাধ্যবাধকতা (Legal Liability)", "weight": "৮–১০ নম্বর"},
        {"dir": "unit05", "num": "০৫", "title": "নিরীক্ষার দায়-দায়িত্ব এবং উদ্দেশ্যসমূহ (Audit Responsibilities & Objectives)", "weight": "১০–১২ নম্বর"},
        {"dir": "unit06", "num": "০৬", "title": "নিরীক্ষার সাক্ষ্যপ্রমাণ ও কার্যপদ্ধতি (Audit Evidence & Procedures)", "weight": "১২–১৪ নম্বর"},
        {"dir": "unit07", "num": "০৭", "title": "নিরীক্ষা পরিকল্পনা ও বিশ্লেষণাত্মক প্রক্রিয়া (Audit Planning & Analytical Procedures)", "weight": "৮–১০ নম্বর"},
        {"dir": "unit08", "num": "০৮", "title": "অভ্যন্তরীণ নিয়ন্ত্রণ নিরীক্ষা এবং নিয়ন্ত্রণ ঝুঁকি (Internal Control & Control Risk)", "weight": "১২–১৪ নম্বর"},
        {"dir": "unit09", "num": "০৯", "title": "সার্বিক নিরীক্ষা পরিকল্পনা ও নিরীক্ষা কর্মসূচি (Overall Audit Plan & Program)", "weight": "৮–১০ নম্বর"},
        {"dir": "unit10", "num": "১০", "title": "নিরীক্ষা কার্য সমাপ্তি ও চূড়ান্তকরণ (Completing the Audit)", "weight": "৬–৮ নম্বর"},
    ]
    
    marks_table_html = """<div class="htbd-table-wrapper">
    <table class="htbd-styled-table">
      <thead>
        <tr>
          <th>বিভাগ ও ধরন</th>
          <th>মোট প্রশ্নের সংখ্যা</th>
          <th>উত্তর দিতে হবে</th>
          <th>প্রতি প্রশ্নের নম্বর</th>
          <th>মোট নম্বর</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>ক-বিভাগ (অতি সংক্ষিপ্ত প্রশ্ন)</strong></td>
          <td>১২টি প্রশ্ন</td>
          <td>১০টি প্রশ্ন</td>
          <td>১ নম্বর</td>
          <td><strong>১০ নম্বর</strong></td>
        </tr>
        <tr>
          <td><strong>খ-বিভাগ (সংক্ষিপ্ত প্রশ্ন)</strong></td>
          <td>৮টি প্রশ্ন</td>
          <td>৫টি প্রশ্ন</td>
          <td>৪ নম্বর</td>
          <td><strong>২০ নম্বর</strong></td>
        </tr>
        <tr>
          <td><strong>গ-বিভাগ (রচনামূলক প্রশ্ন)</strong></td>
          <td>৮টি প্রশ্ন</td>
          <td>৫টি প্রশ্ন</td>
          <td>১০ নম্বর</td>
          <td><strong>৫০ নম্বর</strong></td>
        </tr>
        <tr style="background: #e0f2fe; font-weight: bold;">
          <td colspan="4" style="text-align: right;">সর্বমোট লিখিত পরীক্ষার নম্বর =</td>
          <td><strong>৮০ নম্বর</strong></td>
        </tr>
      </tbody>
    </table>
  </div>"""

    faq_items = [
        {
            "q": "অনার্স ৩য় বর্ষ নিরীক্ষা ও নিশ্চয়তা পরীক্ষায় ক-বিভাগে কীভাবে ১০-এ ১০ পাওয়া সম্ভব?",
            "a": "ক-বিভাগের অতি সংক্ষিপ্ত প্রশ্নের ক্ষেত্রে অতিরিক্ত ভূমিকা না লিখে সরাসরি এক বা দুই বাক্যে মূল পরিভাষা ও সঠিক সংজ্ঞা লিখুন। এই সাজেশনের [৩-স্টার গোল্ডেন] প্রশ্নগুলো নিয়মিত রিভিশন দিলে শতভাগ কমন পাওয়া সম্ভব।"
        },
        {
            "q": "খ ও গ বিভাগে ভালো নম্বর পাওয়ার মূল কৌশল কী?",
            "a": "আন্তর্জাতিক নিরীক্ষা মানদণ্ড (ISA), কোম্পানি আইন ১৯৯৪-এর নির্দিষ্ট ধারা এবং প্রয়োজনীয় ক্ষেত্রে তুলনামূলক ছক ও ডায়াগ্রাম উপস্থাপন করুন। পয়েন্টগুলো নীল কালির কলমে সাব-হেডিং আকারে লিখলে পরীক্ষকের কাছে খাতার মান বহুগুণ বৃদ্ধি পায়।"
        },
        {
            "q": "এই সাজেশনের প্রশ্নগুলো জাতীয় বিশ্ববিদ্যালয়ের কোন কোন সেশনের জন্য প্রযোজ্য?",
            "a": "এই সাজেশনটি জাতীয় বিশ্ববিদ্যালয়ের অনার্স ৩য় বর্ষ (হিসাববিজ্ঞান বিভাগ) পরীক্ষা ২০২৪-২০২৫ (অনুষ্ঠিতব্য ২০২৬) শিক্ষাবর্ষের সর্বশেষ সংশোধিত সিলেবাস অনুযায়ী প্রণীত।"
        }
    ]

    intro_p1 = "জাতীয় বিশ্ববিদ্যালয়ের BBA অনার্স ৩য় বর্ষের হিসাববিজ্ঞান বিভাগের অন্যতম মৌলিক ও গুরুত্বপূর্ণ তাত্ত্বিক বিষয় হলো <strong>নিরীক্ষা ও নিশ্চয়তা (Audit and Assurance - Course Code: 232501)</strong>। সঠিক টেকনিক্যাল উপস্থাপনা ও আন্তর্জাতিক নিরীক্ষা মানদণ্ডের (ISA) গভীর ধারণা না থাকলে এ বিষয়ে এ-প্লাস (A+) অর্জন করা বেশ চ্যালেঞ্জিং হয়ে দাঁড়ায়। হিসাববিজ্ঞান বিভাগের পরবর্তী আবশ্যক বিষয়ের জন্য পড়ুন আমাদের <a href=\"https://www.helptrickbd.com/honours-3rd-year-advanced-accounting-1-suggestion/\">অনার্স ৩য় বর্ষ উন্নত হিসাববিজ্ঞান ১ সাজেশন 2026</a>।"
    intro_p2 = "শিক্ষার্থীদের এই জটিলতা দূরীকরণে HelpTrickBD প্রস্তুত করেছে দেশের সর্বাধিক তথ্যবহুল ও পূর্ণাঙ্গ <strong>অনার্স ৩য় বর্ষ নিরীক্ষা ও নিশ্চয়তা সাজেশন 2026</strong>। এখানে কোনো আংশিক প্রশ্ন নয়, বরং সিলেবাসের সম্পূর্ণ ১০টি অধ্যায়ের মোট ২৮৮টি প্রশ্ন ও উত্তর পুঙ্খানুপুঙ্খভাবে সংকলিত হয়েছে।"

    return generate_subject_html(
        subject_title="নিরীক্ষা ও নিশ্চয়তা (Audit and Assurance)",
        subject_code="232501",
        focus_kw="অনার্স ৩য় বর্ষ নিরীক্ষা ও নিশ্চয়তা সাজেশন",
        seo_title="অনার্স ৩য় বর্ষ নিরীক্ষা ও নিশ্চয়তা সাজেশন 2026: Best Complete Exam Guide",
        banner_url="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/thumbnails/audit_post_1_banner.webp",
        units_config=units_config,
        prefix="unit",
        marks_table_html=marks_table_html,
        faq_items=faq_items,
        intro_p1=intro_p1,
        intro_p2=intro_p2,
        canonical_url="https://www.helptrickbd.com/honours-3rd-year-audit-and-assurance-suggestion/"
    )

def compile_adv1_post():
    """Compiles the complete 245-question Advanced Accounting-I post."""
    units_config = [
        {"dir": "adv1_unit01", "num": "০১", "title": "শেয়ারহোল্ডারদের ইকুইটির হিসাবরক্ষণ (Accounting for Stockholders' Equity)", "weight": "১৫–২০ নম্বর"},
        {"dir": "adv1_unit02", "num": "০২", "title": "কোম্পানির আর্থিক বিবরণীসমূহ (Financial Statements of Companies)", "weight": "২০–২৫ নম্বর"},
        {"dir": "adv1_unit03", "num": "০৩", "title": "আয় শনাক্তকরণ (Revenue Recognition - IAS 18 / IFRS 15)", "weight": "১২–১৬ নম্বর"},
        {"dir": "adv1_unit04", "num": "০৪", "title": "ইজারা হিসাববিজ্ঞান (Accounting for Leases - IAS 17 / IFRS 16)", "weight": "১৫–২০ নম্বর"},
        {"dir": "adv1_unit05", "num": "০৫", "title": "হিসাবের পরিবর্তন এবং ভুলের বিশ্লেষণ (Accounting Changes & Error Analysis - IAS 8)", "weight": "১০–১৫ নম্বর"},
    ]
    
    marks_table_html = """<div class="htbd-table-wrapper">
    <table class="htbd-styled-table">
      <thead>
        <tr>
          <th>বিভাগ ও প্রশ্নের ধরন</th>
          <th>মোট প্রশ্নের সংখ্যা</th>
          <th>উত্তর দিতে হবে</th>
          <th>প্রতি প্রশ্নের নম্বর</th>
          <th>মোট নম্বর</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>ক-বিভাগ (অতি সংক্ষিপ্ত প্রশ্ন)</strong></td>
          <td>১২টি প্রশ্ন</td>
          <td>১০টি প্রশ্ন</td>
          <td>১ নম্বর</td>
          <td><strong>১০ নম্বর</strong></td>
        </tr>
        <tr>
          <td><strong>খ-বিভাগ (সংক্ষিপ্ত ও গাণিতিক সমস্যা)</strong></td>
          <td>৮টি প্রশ্ন</td>
          <td>৫টি প্রশ্ন</td>
          <td>৪ নম্বর</td>
          <td><strong>২০ নম্বর</strong></td>
        </tr>
        <tr>
          <td><strong>গ-বিভাগ (রচনামূলক ও গাণিতিক বিশ্লেষণ)</strong></td>
          <td>৮টি প্রশ্ন</td>
          <td>৫টি প্রশ্ন</td>
          <td>১০ নম্বর</td>
          <td><strong>৫০ নম্বর</strong></td>
        </tr>
        <tr style="background: #e0f2fe; font-weight: bold;">
          <td colspan="4" style="text-align: right;">সর্বমোট লিখিত পরীক্ষার নম্বর =</td>
          <td><strong>৮০ নম্বর</strong></td>
        </tr>
      </tbody>
    </table>
  </div>"""

    faq_items = [
        {
            "q": "অনার্স ৩য় বর্ষ উন্নত হিসাববিজ্ঞান ১ পরীক্ষায় অংক ও থিওরির অনুপাত কেমন থাকে?",
            "a": "উন্নত হিসাববিজ্ঞান-১ বিষয়ে খ ও গ বিভাগে সাধারণত ৭০% থেকে ৮০% গাণিতিক সমস্যা থাকে এবং ২০% থেকে ৩০% মৌলিক তাত্ত্বিক প্রশ্ন আসে। তাই গাণিতিক সমস্যাগুলোর জাবেদা ও ওয়ার্কিং নোটে পারদর্শী হওয়া সর্বাধিক জরুরি।"
        },
        {
            "q": "গাণিতিক সমস্যাবলিতে পূর্ণ নম্বর পাওয়ার উপায় কী?",
            "a": "আন্তর্জাতিক হিসাবমান (IAS ও IFRS) অনুযায়ী জাবেদার বিবরণ ও ব্যাখ্যা সঠিকভাবে লিখুন। প্রতিটি অংকের নিচে সুস্পষ্ট Working Notes বা গণনাকার্য উপস্থাপন করলে পরীক্ষক পূর্ণ নম্বর প্রদান করেন।"
        },
        {
            "q": "এই সাজেশনের প্রশ্নগুলো জাতীয় বিশ্ববিদ্যালয়ের কোন কোন সেশনের জন্য প্রযোজ্য?",
            "a": "এই সাজেশনটি জাতীয় বিশ্ববিদ্যালয়ের অনার্স ৩য় বর্ষ (হিসাববিজ্ঞান বিভাগ) পরীক্ষা ২০২৪-২০২৫ (অনুষ্ঠিতব্য ২০২৬) শিক্ষাবর্ষের সর্বশেষ সিলেবাস অনুযায়ী প্রণীত।"
        }
    ]

    intro_p1 = "জাতীয় বিশ্ববিদ্যালয়ের BBA অনার্স ৩য় বর্ষ হিসাববিজ্ঞান বিভাগের শিক্ষার্থীদের জন্য অন্যতম গুরুত্বপূর্ণ ও সর্বোচ্চ নম্বর নিশ্চিতকারী ব্যবহারিক কোর্স হলো <strong>উন্নত হিসাববিজ্ঞান-১ (Advanced Accounting-I - Course Code: 232503)</strong>। স্টকহোল্ডার্স ইকুইটি, কোম্পানির আর্থিক বিবরণী, রেভিনিউ রিকগনিশন, লিজ একাউন্টিং এবং এরর অ্যানালাইসিসের মতো আন্তর্জাতিক মানসম্পন্ন চ্যাপ্টারগুলোর নিখুঁত সমাধানের ওপর পরীক্ষার চূড়ান্ত জিপিএ নির্ভর করে। হিসাববিজ্ঞান বিভাগের পূর্ণাঙ্গ তাত্ত্বিক প্রস্তুতির জন্য পড়ুন <a href=\"https://www.helptrickbd.com/honours-3rd-year-audit-and-assurance-suggestion/\">অনার্স ৩য় বর্ষ নিরীক্ষা ও নিশ্চয়তা সাজেশন 2026</a>।"
    intro_p2 = "শিক্ষার্থীদের সুবিধার্থে HelpTrickBD প্রস্তুত করেছে দেশের সর্বাধিক বিশদ ও মানসম্মত <strong>অনার্স ৩য় বর্ষ উন্নত হিসাববিজ্ঞান ১ সাজেশন 2026</strong>। এখানে সিলেবাসের ৫টি অধ্যায়ের ক, খ ও গ বিভাগের মোট ২৪৫টি প্রশ্ন ও সমাধান ধাপে ধাপে সন্নিবেশিত করা হয়েছে।"

    return generate_subject_html(
        subject_title="উন্নত হিসাববিজ্ঞান-১ (Advanced Accounting-I)",
        subject_code="232503",
        focus_kw="অনার্স ৩য় বর্ষ উন্নত হিসাববিজ্ঞান ১ সাজেশন",
        seo_title="অনার্স ৩য় বর্ষ উন্নত হিসাববিজ্ঞান ১ সাজেশন 2026: Best Complete Exam Guide",
        banner_url="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/thumbnails/adv_accounting_1_banner.webp",
        units_config=units_config,
        prefix="adv1_unit",
        marks_table_html=marks_table_html,
        faq_items=faq_items,
        intro_p1=intro_p1,
        intro_p2=intro_p2,
        canonical_url="https://www.helptrickbd.com/honours-3rd-year-advanced-accounting-1-suggestion/"
    )

def compile_cost_post():
    """Compiles the complete 312-question Cost Accounting post."""
    units_config = [
        {"dir": "cost_unit01", "num": "০১", "title": "উৎপাদন ব্যয় হিসাববিজ্ঞান ও ব্যয় হিসাবরক্ষক (Cost Accounting & Cost Accountant)", "weight": "১০–১২ নম্বর"},
        {"dir": "cost_unit02", "num": "০২", "title": "বিভিন্ন প্রকার ব্যয়ের পরিচিতি এবং উদ্দেশ্যসমূহ (Cost Terms & Purposes)", "weight": "১৫–২০ নম্বর"},
        {"dir": "cost_unit03", "num": "০৩", "title": "ব্যয় আচরণ বিশ্লেষণ (Cost Behaviour Analysis)", "weight": "১২–১৫ নম্বর"},
        {"dir": "cost_unit04", "num": "০৪", "title": "কাঁচামাল নিয়ন্ত্রণ ও হিসাবরক্ষণ (Materials Control & Valuations)", "weight": "১৫–২০ নম্বর"},
        {"dir": "cost_unit05", "num": "০৫", "title": "শ্রম ব্যয় ও মজুরি পরিকল্পনা (Labor Cost & Wage Incentive Plans)", "weight": "১৫–২০ নম্বর"},
        {"dir": "cost_unit06", "num": "০৬", "title": "কারখানা উপরি-ব্যয় বণ্টন (Factory Overhead Allocation & Rates)", "weight": "১২–১৫ নম্বর"},
    ]
    
    marks_table_html = """<div class="htbd-table-wrapper">
    <table class="htbd-styled-table">
      <thead>
        <tr>
          <th>বিভাগ ও প্রশ্নের ধরন</th>
          <th>মোট প্রশ্নের সংখ্যা</th>
          <th>উত্তর দিতে হবে</th>
          <th>প্রতি প্রশ্নের নম্বর</th>
          <th>মোট নম্বর</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>ক-বিভাগ (অতি সংক্ষিপ্ত প্রশ্ন)</strong></td>
          <td>১২টি প্রশ্ন</td>
          <td>১০টি প্রশ্ন</td>
          <td>১ নম্বর</td>
          <td><strong>১০ নম্বর</strong></td>
        </tr>
        <tr>
          <td><strong>খ-বিভাগ (সংক্ষিপ্ত ও গাণিতিক সমস্যা)</strong></td>
          <td>৮টি প্রশ্ন</td>
          <td>৫টি প্রশ্ন</td>
          <td>৪ নম্বর</td>
          <td><strong>২০ নম্বর</strong></td>
        </tr>
        <tr>
          <td><strong>গ-বিভাগ (রচনামূলক ও ব্যবহারিক অংক)</strong></td>
          <td>৮টি প্রশ্ন</td>
          <td>৫টি প্রশ্ন</td>
          <td>১০ নম্বর</td>
          <td><strong>৫০ নম্বর</strong></td>
        </tr>
        <tr style="background: #e0f2fe; font-weight: bold;">
          <td colspan="4" style="text-align: right;">সর্বমোট লিখিত পরীক্ষার নম্বর =</td>
          <td><strong>৮০ নম্বর</strong></td>
        </tr>
      </tbody>
    </table>
  </div>"""

    faq_items = [
        {
            "q": "অনার্স ৩য় বর্ষ উৎপাদন ব্যয় হিসাববিজ্ঞান পরীক্ষায় অংক কত নম্বরের আসে?",
            "a": "উৎপাদন ব্যয় হিসাববিজ্ঞান একটি অত্যন্ত উচ্চমানের ব্যবহারিক কোর্স। জাতীয় বিশ্ববিদ্যালয়ের বিগত বছরগুলোর প্রশ্ন বিশ্লেষণে দেখা যায়, খ ও গ বিভাগে প্রায় ৭০% থেকে ৮০% প্রশ্ন সরাসরি গাণিতিক সমস্যা (কস্ট শিট, ইওকিউ, হলসে-রোয়ান প্ল্যান ও মেশিন আওয়ার রেট) থেকে আসে।"
        },
        {
            "q": "গাণিতিক সমস্যাবলিতে পূর্ণ নম্বর পাওয়ার মূল উপায় কী?",
            "a": "প্রতিটি অংকের শুরুতে স্পষ্ট ফর্মুলা উল্লেখ করুন এবং নিচে পরিচ্ছন্ন Working Notes (গণনাকার্য) উপস্থাপন করুন। ছকগুলো স্কেল দিয়ে নিখুঁতভাবে আঁকলে এবং দশমিক বা টাকার একক উল্লেখ করলে পরীক্ষক সম্পূর্ণ নম্বর প্রদান করেন।"
        },
        {
            "q": "এই সাজেশনের প্রশ্নগুলো জাতীয় বিশ্ববিদ্যালয়ের কোন শিক্ষাবর্ষের জন্য প্রযোজ্য?",
            "a": "এই সাজেশনটি জাতীয় বিশ্ববিদ্যালয়ের অনার্স ৩য় বর্ষ (হিসাববিজ্ঞান বিভাগ) পরীক্ষা ২০২৪-২০২৫ (অনুষ্ঠিতব্য ২০২৬) শিক্ষাবর্ষের সর্বশেষ অনুমোদিত সিলেবাস অনুযায়ী প্রণীত।"
        }
    ]

    intro_p1 = "জাতীয় বিশ্ববিদ্যালয়ের BBA অনার্স ৩য় বর্ষ হিসাববিজ্ঞান বিভাগের অন্যতম সর্বোচ্চ স্কোরিং ও কৌশলগত কোর্স হলো <strong>উৎপাদন ব্যয় হিসাববিজ্ঞান (Cost Accounting - Course Code: 232505)</strong>। কস্ট কনসেপ্ট, ব্যয় বিবরণী প্রস্তুতকরণ, কাঁচামালের সঠিক মূল্যায়ন (FIFO, LIFO, Weighted Average), শ্রম মজুরি নির্ধারণ (Halsey, Rowan & Taylor) এবং কারখানা উপরিব্যয় বণ্টনের নিখুঁত দক্ষতার ওপর প্রথম শ্রেণি বা এ-প্লাস (A+) অর্জন নির্ভর করে। হিসাববিজ্ঞান বিভাগের অন্যান্য আবশ্যিক বিষয়ের জন্য পড়ুন আমাদের <a href=\"https://www.helptrickbd.com/honours-3rd-year-advanced-accounting-1-suggestion/\">অনার্স ৩য় বর্ষ উন্নত হিসাববিজ্ঞান ১ সাজেশন 2026</a> এবং <a href=\"https://www.helptrickbd.com/honours-3rd-year-audit-and-assurance-suggestion/\">অনার্স ৩য় বর্ষ নিরীক্ষা ও নিশ্চয়তা সাজেশন 2026</a>।"
    intro_p2 = "শিক্ষার্থীদের চূড়ান্ত প্রস্তুতির পূর্ণাঙ্গ সহায়তায় HelpTrickBD প্রস্তুত করেছে দেশের সর্বাধিক সমৃদ্ধ <strong>অনার্স ৩য় বর্ষ উৎপাদন ব্যয় হিসাববিজ্ঞান সাজেশন 2026</strong>। এখানে কোনো আংশিক প্রশ্ন বা অসম্পূর্ণ সমাধান নয়, বরং সিলেবাসের ৬টি অধ্যায়ের ক, খ ও গ বিভাগের মোট ৩১২টি প্রশ্ন ও অংকের পুঙ্খানুপুঙ্খ সমাধান অন্তর্ভুক্ত করা হয়েছে।"

    return generate_subject_html(
        subject_title="উৎপাদন ব্যয় হিসাববিজ্ঞান (Cost Accounting)",
        subject_code="232505",
        focus_kw="অনার্স ৩য় বর্ষ উৎপাদন ব্যয় হিসাববিজ্ঞান সাজেশন",
        seo_title="অনার্স ৩য় বর্ষ উৎপাদন ব্যয় হিসাববিজ্ঞান সাজেশন 2026: Best Complete Exam Guide",
        banner_url="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/thumbnails/cost_accounting_banner.webp",
        units_config=units_config,
        prefix="cost_unit",
        marks_table_html=marks_table_html,
        faq_items=faq_items,
        intro_p1=intro_p1,
        intro_p2=intro_p2,
        canonical_url="https://www.helptrickbd.com/honours-3rd-year-cost-accounting-suggestion/"
    )

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8')
    os.makedirs(os.path.join(PROJECT_ROOT, "scratch"), exist_ok=True)
    
    print("Compiling Cost Accounting post (all 312 questions)...")
    cost_html = compile_cost_post()
    cost_path = os.path.join(PROJECT_ROOT, "scratch", "cost_master_312.html")
    with open(cost_path, "w", encoding="utf-8") as f:
        f.write(cost_html)
    print(f"Cost Accounting HTML written: {cost_path} (Length: {len(cost_html)} chars)")

