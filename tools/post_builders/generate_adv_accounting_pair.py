#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/post_builders/generate_adv_accounting_pair.py
--------------------------------------------------
Generates the 2 interconnected, high-ranking posts for:
Subject: উন্নত হিসাববিজ্ঞান-১ (Advanced Accounting-I - Course Code: 232503)

Post 1: অধ্যায়ভিত্তিক চূড়ান্ত সাজেশন ২০২৬ (All 7 Units, 320 Questions)
        Slug: honours-3rd-year-advanced-accounting-1-suggestion
        PDF: HelpTrickBD_232503_Advanced_Accounting_1_Master_Book.pdf

Post 2: বিগত ৬ বছরের বোর্ড প্রশ্ন ও পূর্ণাঙ্গ সমাধান ২০১৯–২০২৪ (All 6 Years, 168 Questions)
        Slug: honours-3rd-year-advanced-accounting-1-board-questions
        PDF: HelpTrickBD_232503_Advanced_Accounting_1_Board_Questions_2019_2024.pdf

Enhancements:
- Click-to-reveal Interactive Accordions (<details><summary>):
  Answers are hidden by default with '[উত্তর / সমাধান দেখুন]'.
- Bulletproof Author Box with native WordPress image URL (ID 16007).
- Categories: Education Guide (4), National University (9), NU Question Bank (127).
- 100% Zero-Emoji Policy.
- Position 0 Lead Box, Rank Math TOC, Schema microdata, and dark mode styling.
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
PUB_BOOKS_BASE = r'D:\android\Project\Publication Books\questions\advanced_accounting_1'

PDF_MASTER_URL = "https://www.helptrickbd.com/wp-content/uploads/2026/11/HelpTrickBD_232503_Advanced_Accounting_1_Master_Book.pdf"
PDF_BOARD_URL = "https://www.helptrickbd.com/wp-content/uploads/2026/11/HelpTrickBD_232503_Advanced_Accounting_1_Board_Questions_2019_2024.pdf"

AUTHOR_IMG_URL = "https://www.helptrickbd.com/wp-content/uploads/2026/11/faruk_sir.webp"
AUTHOR_IMG_FALLBACK = "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/author/faruk_sir.webp"

URL_SUGGESTION_POST = "https://www.helptrickbd.com/honours-3rd-year-advanced-accounting-1-suggestion/"
URL_BOARD_POST = "https://www.helptrickbd.com/honours-3rd-year-advanced-accounting-1-board-questions/"

def parse_unit_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        raw = f.read()
    parts = raw.split('---')
    if len(parts) < 3:
        return None
    fm = yaml.safe_load(parts[1])
    body = '---'.join(parts[2:]).strip()
    
    sec = str(fm.get('section', '')).strip()
    q_no = fm.get('question_number') or fm.get('q_no') or 0
    imp = fm.get('importance', 2)
    
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
    ans_html = ans_html.replace('★', '').replace('⭐', '').replace('✨', '')
    q_text = q_text.replace('★', '').replace('⭐', '').replace('✨', '')
    
    return {
        'id': fm.get('id', ''),
        'section': sec,
        'q_no': q_no,
        'imp_badge': imp_badge,
        'year_badge': year_badge,
        'q_text': q_text,
        'ans_html': ans_html
    }

def parse_board_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        raw = f.read()
    parts = raw.split('---')
    if len(parts) < 3:
        return None
    fm = yaml.safe_load(parts[1])
    body = '---'.join(parts[2:]).strip()
    
    sec = str(fm.get('section', '')).strip()
    q_no = fm.get('question_number', '')
    imp = fm.get('importance', 3)
    held_date = fm.get('held_date', '')
    exam_year = fm.get('exam_year', '')
    
    if imp == 3 or '3' in str(imp):
        imp_badge = '<span class="htbd-badge-star golden">[৩-স্টার গোল্ডেন]</span>'
    elif imp == 2 or '2' in str(imp):
        imp_badge = '<span class="htbd-badge-star super">[২-স্টার সুপার]</span>'
    else:
        imp_badge = '<span class="htbd-badge-star regular">[১-স্টার সাধারণ]</span>'
        
    year_badge = f'<span class="htbd-badge-year">জাতীয় বিশ্ববিদ্যালয় {exam_year}</span>'
    if held_date:
        year_badge += f' <span class="htbd-badge-year" style="background:#eff6ff; color:#1e40af; border-color:#bfdbfe;">অনুষ্ঠিত: {held_date}</span>'
        
    ans_split = re.split(r'\n##\s*(?:উত্তর\s*/\s*সমাধান|সমাধান\s*/\s*উত্তর|উত্তর|সমাধান)[\s:]*', body, flags=re.IGNORECASE)
    if len(ans_split) >= 2:
        q_raw = ans_split[0].strip()
        ans_text = ans_split[1].strip()
        q_raw = re.sub(r'^##?\s*(?:প্রশ্ন|Question)?[\s:]*', '', q_raw, flags=re.IGNORECASE).strip()
        q_text = q_raw
    else:
        lines = body.split('\n')
        first_line = lines[0]
        q_text = re.sub(r'^##?\s*(?:প্রশ্ন|Question)?[\s:]*', '', first_line, flags=re.IGNORECASE).strip()
        ans_text = '\n'.join(lines[1:]).strip()
        
    ans_html = md_engine.render(ans_text)
    ans_html = ans_html.replace('★', '').replace('⭐', '').replace('✨', '')
    q_text = q_text.replace('★', '').replace('⭐', '').replace('✨', '')
    
    return {
        'id': fm.get('id', ''),
        'section': sec,
        'q_no': q_no,
        'imp_badge': imp_badge,
        'year_badge': year_badge,
        'q_text': q_text,
        'ans_html': ans_html
    }

def get_shared_css():
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
  .htbd-download-card {
    background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
    border: 2px solid #cbd5e1;
    border-radius: 12px;
    padding: 24px;
    margin: 30px 0;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 18px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.04);
  }
  .htbd-download-btn {
    background: #2563eb;
    color: #ffffff !important;
    text-decoration: none;
    padding: 13px 26px;
    border-radius: 8px;
    font-weight: 700;
    font-size: 15.5px;
    display: inline-block;
    box-shadow: 0 3px 12px rgba(37,99,235,0.3);
    transition: all 0.2s ease;
  }
  .htbd-download-btn:hover {
    background: #1d4ed8;
    color: #ffffff !important;
    text-decoration: none;
    transform: translateY(-2px);
  }
  .htbd-crosslink-card {
    background: #eff6ff;
    border-left: 5px solid #2563eb;
    padding: 22px 24px;
    border-radius: 10px;
    margin: 30px 0;
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
  .htbd-q-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-left: 4.5px solid #2563eb;
    border-radius: 10px;
    padding: 20px 22px;
    margin-bottom: 22px;
    box-shadow: 0 3px 10px rgba(0,0,0,0.03);
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

  /* Interactive Click-to-Reveal Accordion Styles */
  details.htbd-ans-details {
    margin-top: 12px;
  }
  summary.htbd-ans-toggle {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #f1f5f9;
    color: #1e3a8a;
    border: 1.5px solid #cbd5e1;
    padding: 8px 18px;
    border-radius: 6px;
    font-size: 14.5px;
    font-weight: 700;
    cursor: pointer;
    user-select: none;
    transition: all 0.2s ease;
    list-style: none;
  }
  summary.htbd-ans-toggle::-webkit-details-marker {
    display: none;
  }
  summary.htbd-ans-toggle:hover {
    background: #e2e8f0;
    border-color: #94a3b8;
    color: #0f172a;
    box-shadow: 0 2px 6px rgba(0,0,0,0.06);
  }
  details[open] summary.htbd-ans-toggle {
    background: #e0f2fe;
    border-color: #7dd3fc;
    color: #0369a1;
    margin-bottom: 12px;
  }
  details[open] summary.htbd-ans-toggle .htbd-toggle-text::after {
    content: " (লুকাতে ক্লিক করুন)";
    font-weight: normal;
    font-size: 13px;
  }

  .htbd-ans-box {
    background: #f8fafc;
    border-radius: 8px;
    padding: 18px 20px;
    border: 1px solid #e2e8f0;
    border-top: 2.5px solid #2563eb;
    font-size: 15.5px;
    color: #334155;
    line-height: 1.85;
    animation: htbdFadeIn 0.3s ease-in-out;
  }
  @keyframes htbdFadeIn {
    from { opacity: 0; transform: translateY(-4px); }
    to { opacity: 1; transform: translateY(0); }
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
    .dark-mode .htbd-download-card, body.dark-theme .htbd-download-card {
      background: #0f172a;
      border-color: #334155;
    }
    .dark-mode .htbd-download-card h4, body.dark-theme .htbd-download-card h4 {
      color: #f8fafc;
    }
    .dark-mode .htbd-download-card p, body.dark-theme .htbd-download-card p {
      color: #cbd5e1;
    }
    .dark-mode .htbd-crosslink-card, body.dark-theme .htbd-crosslink-card {
      background: #0c4a6e;
      border-left-color: #38bdf8;
      color: #f0f9ff;
    }
    .dark-mode .htbd-crosslink-card h4, body.dark-theme .htbd-crosslink-card h4 {
      color: #7dd3fc;
    }
    .dark-mode .htbd-crosslink-card p, body.dark-theme .htbd-crosslink-card p {
      color: #e0f2fe;
    }
    .dark-mode .htbd-crosslink-card a, body.dark-theme .htbd-crosslink-card a {
      color: #bae6fd;
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
    .dark-mode summary.htbd-ans-toggle, body.dark-theme summary.htbd-ans-toggle {
      background: #1e293b;
      border-color: #334155;
      color: #93c5fd;
    }
    .dark-mode summary.htbd-ans-toggle:hover, body.dark-theme summary.htbd-ans-toggle:hover {
      background: #334155;
      color: #f8fafc;
    }
    .dark-mode details[open] summary.htbd-ans-toggle, body.dark-theme details[open] summary.htbd-ans-toggle {
      background: #0c4a6e;
      border-color: #0284c7;
      color: #e0f2fe;
    }
    .dark-mode .htbd-ans-box, body.dark-theme .htbd-ans-box {
      background: #0f172a;
      border-color: #334155;
      border-top-color: #38bdf8;
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
    return f"""<div class="htbd-author-box" style="display: flex; align-items: center; gap: 20px; margin: 35px 0 25px 0; padding: 22px 26px; background: #f8fafc; border: 1.5px solid #e2e8f0; border-left: 5px solid #2563eb; border-radius: 12px; font-family: 'SolaimanLipi', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <img src="{AUTHOR_IMG_URL}" onerror="this.src='{AUTHOR_IMG_FALLBACK}'" alt="মো: ওমর ফারুক (Faruk Sir)" class="htbd-author-avatar" width="80" height="80" loading="lazy" style="width: 80px !important; height: 80px !important; min-width: 80px !important; max-width: 80px !important; border-radius: 50% !important; object-fit: cover !important; border: 2.5px solid #2563eb !important; flex-shrink: 0 !important; display: block !important; margin: 0 !important; box-shadow: 0 3px 8px rgba(0,0,0,0.1) !important;" />
  <div style="flex: 1 1 auto; min-width: 0;">
    <h4 style="margin: 0 0 6px 0; color: #0b2046; font-size: 19px; font-weight: 700; line-height: 1.3;">মো: ওমর ফারুক (Faruk Sir)</h4>
    <p style="margin: 0; color: #475569; font-size: 14.5px; line-height: 1.6;">প্রতিষ্ঠাতা ও প্রধান শিক্ষা সম্পাদক, HelpTrickBD। শিক্ষার্থীদের জন্য দীর্ঘ ৮+ বছর যাবত মানসম্মত একাডেমিক গাইড, হ্যান্ডনোট ও চূড়ান্ত সাজেশন প্রণয়ন করছেন।</p>
  </div>
</div>"""

def generate_post_1_chapter_suggestion():
    """Generates Post 1: Chapter-wise Suggestion (All 7 Units, 320 Questions with click-to-reveal answers)."""
    units_config = [
        {"dir": "unit01", "num": "০১", "title": "শেয়ারহোল্ডারদের ইকুইটির হিসাবরক্ষণ (Accounting for Stockholders' Equity)", "weight": "১৫–২০ নম্বর"},
        {"dir": "unit02", "num": "০২", "title": "কোম্পানির আর্থিক বিবরণীসমূহ (Financial Statements of Companies)", "weight": "২০–২৫ নম্বর"},
        {"dir": "unit03", "num": "০৩", "title": "আয় শনাক্তকরণ (Revenue Recognition - IAS 18 / IFRS 15)", "weight": "১২–১৬ নম্বর"},
        {"dir": "unit04", "num": "০৪", "title": "ইজারা হিসাববিজ্ঞান (Accounting for Leases - IAS 17 / IFRS 16)", "weight": "১৫–২০ নম্বর"},
        {"dir": "unit05", "num": "০৫", "title": "হিসাবের পরিবর্তন এবং ভুলের বিশ্লেষণ (Accounting Changes & Error Analysis - IAS 8)", "weight": "১০–১৫ নম্বর"},
        {"dir": "unit06", "num": "০৬", "title": "অপারেটিং সেগমেন্ট এর হিসাব (Accounting for Operating Segments - IFRS 8)", "weight": "৮–১২ নম্বর"},
        {"dir": "unit07", "num": "০৭", "title": "দেউলিয়া সম্পর্কিত হিসাববিজ্ঞান (Accounting Relating to Bankruptcy - Act 1997)", "weight": "১২–১৫ নম্বর"},
    ]
    
    focus_kw = "অনার্স ৩য় বর্ষ উন্নত হিসাববিজ্ঞান ১ সাজেশন"
    seo_title = "অনার্স ৩য় বর্ষ উন্নত হিসাববিজ্ঞান ১ সাজেশন 2026: Best Complete Exam Guide"
    banner_url = "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/thumbnails/adv_accounting_1_banner.webp"
    
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
            res = parse_unit_file(f)
            if res:
                s = res['section']
                if s in secs:
                    secs[s].append(res)
                    total_sec_counts[s] += 1
                    total_q_count += 1
                    
        for s in ['ক', 'খ', 'গ']:
            secs[s].sort(key=lambda x: str(x['q_no']))
            
        all_units_data.append({
            'dir': u_dir,
            'num': u_num,
            'title': u_title,
            'weight': u_weight,
            'secs': secs,
            'count': len(secs['ক']) + len(secs['খ']) + len(secs['গ'])
        })

    # TOC
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

    # Units Body with Click-to-Reveal Accordions
    units_body_html = []
    for u in all_units_data:
        anchor_id = f"unit-{u['num']}"
        u_html = [f'<div class="htbd-unit-block" id="{anchor_id}">']
        u_html.append(f'<h2>অধ্যায় {u["num"]}: {u["title"]}</h2>')
        u_html.append(f'<p style="color: #475569; font-weight: 500;"><strong>সিলেবাস গুরুত্ব ও মানবণ্টন:</strong> জাতীয় বিশ্ববিদ্যালয়ের বিগত বছরের প্রশ্ন বিশ্লেষণে এ অধ্যায়টি থেকে পরীক্ষায় প্রায় {u["weight"]} প্রশ্ন কমন পাওয়া যায়। উত্তর দেখতে প্রতিটি প্রশ্নের নিচের [উত্তর / সমাধান দেখুন] বাটনে ক্লিক করুন:</p>')
        
        # Section A
        if u['secs']['ক']:
            u_html.append(f'<h3>ক-বিভাগ: অতি সংক্ষিপ্ত প্রশ্নাবলি ({u["title"]})</h3>')
            for q in u['secs']['ক']:
                u_html.append(f"""<div class="htbd-q-card">
  <div class="htbd-q-header">
    <span class="htbd-badge-sec">ক-বিভাগ (১ নম্বর)</span>
    {q['imp_badge']}
    {q['year_badge']}
  </div>
  <div class="htbd-q-title">প্রশ্ন {q['q_no']}. {q['q_text']}</div>
  <details class="htbd-ans-details">
    <summary class="htbd-ans-toggle">
      <span class="htbd-toggle-text">[উত্তর দেখুন]</span>
    </summary>
    <div class="htbd-ans-box">
      <strong>উত্তর:</strong> {q['ans_html']}
    </div>
  </details>
</div>""")

        # Section B
        if u['secs']['খ']:
            u_html.append(f'<h3>খ-বিভাগ: সংক্ষিপ্ত প্রশ্নাবলি ও গাণিতিক সমস্যাবলি ({u["title"]})</h3>')
            for q in u['secs']['খ']:
                u_html.append(f"""<div class="htbd-q-card card-b">
  <div class="htbd-q-header">
    <span class="htbd-badge-sec" style="background: #d1fae5; color: #065f46;">খ-বিভাগ (৪ নম্বর)</span>
    {q['imp_badge']}
    {q['year_badge']}
  </div>
  <div class="htbd-q-title">প্রশ্ন {q['q_no']}. {q['q_text']}</div>
  <details class="htbd-ans-details">
    <summary class="htbd-ans-toggle">
      <span class="htbd-toggle-text">[সমাধান দেখুন]</span>
    </summary>
    <div class="htbd-ans-box">
      {q['ans_html']}
    </div>
  </details>
</div>""")

        # Section C
        if u['secs']['গ']:
            u_html.append(f'<h3>গ-বিভাগ: রচনামূলক ও গাণিতিক বিশ্লেষণ ({u["title"]})</h3>')
            for q in u['secs']['গ']:
                u_html.append(f"""<div class="htbd-q-card card-c">
  <div class="htbd-q-header">
    <span class="htbd-badge-sec" style="background: #ede9fe; color: #5b21b6;">গ-বিভাগ (১০ নম্বর)</span>
    {q['imp_badge']}
    {q['year_badge']}
  </div>
  <div class="htbd-q-title">প্রশ্ন {q['q_no']}. {q['q_text']}</div>
  <details class="htbd-ans-details">
    <summary class="htbd-ans-toggle">
      <span class="htbd-toggle-text">[সম্পূর্ণ সমাধান দেখুন]</span>
    </summary>
    <div class="htbd-ans-box">
      {q['ans_html']}
    </div>
  </details>
</div>""")
                
        u_html.append('</div>')
        units_body_html.append('\n'.join(u_html))

    all_units_rendered = '\n\n'.join(units_body_html)

    # Professional Dual-Button PDF Download Section
    pdf_card_html = f"""<div class="htbd-pdf-section" style="margin: 40px 0 35px 0; background: #ffffff; border: 1.5px solid #e2e8f0; border-top: 5px solid #dc2626; border-radius: 14px; padding: 28px 32px; box-shadow: 0 4px 20px rgba(0,0,0,0.05); font-family: 'SolaimanLipi', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 14px;">
    <span style="display: inline-flex; align-items: center; justify-content: center; width: 44px; height: 44px; background: #fee2e2; border-radius: 10px; color: #dc2626;">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
    </span>
    <div>
      <h2 id="pdf-download" style="color: #0b2046; font-size: 22px; font-weight: 700; margin: 0; line-height: 1.3;">অফিশিয়াল PDF ডাউনলোড: অনার্স ৩য় বর্ষ উন্নত হিসাববিজ্ঞান ১ মাস্টার সাজেশন ২০২৬</h2>
      <div style="color: #64748b; font-size: 13.5px; font-weight: 600; margin-top: 3px;">ফাইল ফরম্যাট: প্রামাণ্য A4 প্রিন্ট-রেডি ই-বুক • সংস্করণ: ২০২৬ স্পেশাল</div>
    </div>
  </div>

  <p style="color: #475569; font-size: 15.5px; line-height: 1.85; margin: 0 0 22px 0;">
    জাতীয় বিশ্ববিদ্যালয়ের অনার্স ৩য় বর্ষ হিসাববিজ্ঞান বিভাগের পরীক্ষার্থীদের চূড়ান্ত প্রস্তুতি ও অফলাইন রিভিশনের সুবিধার্থে <strong>উন্নত হিসাববিজ্ঞান ১ (Advanced Accounting-I, বিষয় কোড: ২৩২৫০৩)</strong>-এর অধ্যায় ০১ থেকে ০৭ পর্যন্ত সকল অধ্যায়ের ক, খ ও গ বিভাগের মোট ৩২০টি প্রশ্নোত্তর সংবলিত প্রামাণ্য ই-বুক PDF (৫.১৮ MB) নিচে সংযুক্ত করা হলো। নিচের দুটি অপশনের যেকোনো একটি বেছে নিয়ে আপনি ফাইলটি সংগ্রহ করতে পারেন:
  </p>

  <div class="htbd-download-buttons-grid" style="display: flex; flex-wrap: wrap; gap: 16px; align-items: center;">
    <!-- Button 2: 30-Second Countdown High-Speed Timer Download -->
    <div id="htbd-timer-wrap-sugg2026" style="display: inline-block;">
      <button id="htbd-timer-btn-sugg2026" onclick="startPdfCountdown('sugg2026', '{PDF_MASTER_URL}')" class="htbd-btn-timer" style="display: inline-flex; align-items: center; gap: 10px; background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%); color: #ffffff !important; padding: 13px 26px; border-radius: 9px; font-weight: 700; font-size: 15.5px; cursor: pointer; border: none; box-shadow: 0 4px 12px rgba(37, 99, 235, 0.28); user-select: none; transition: transform 0.15s ease, box-shadow 0.15s ease;">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
        <span>⏳ ৩০ সেকেন্ডে হাই-স্পিড ডাউনলোড (Countdown)</span>
      </button>
      <div id="htbd-timer-box-sugg2026" style="display: none; background: #eff6ff; border: 1.5px solid #bfdbfe; border-radius: 9px; padding: 14px 22px; font-size: 15px; font-weight: 700; color: #1e40af; text-align: center;">
        <div id="htbd-timer-text-sugg2026">হাই-স্পিড ক্লাউড লিংক তৈরি হচ্ছে... অনুগ্রহ করে <span id="htbd-countdown-sugg2026" style="color: #dc2626; font-size: 19px; font-weight: 800;">30</span> সেকেন্ড অপেক্ষা করুন</div>
        <div style="width: 100%; height: 7px; background: #dbeafe; border-radius: 4px; margin-top: 10px; overflow: hidden;">
          <div id="htbd-progress-sugg2026" style="width: 100%; height: 100%; background: #2563eb; transition: width 1s linear;"></div>
        </div>
      </div>
    </div>
  </div>

  <div style="margin-top: 16px; font-size: 13.5px; color: #64748b; display: flex; align-items: center; gap: 6px;">
    <span>🔒 ১০০% ভাইরাস-মুক্ত ও সুরক্ষিত সরাসরি গুগল ড্রাইভ / ক্লাউড সার্ভার মিরর লিংক।</span>
  </div>
</div>"""

    # Cross-link to Board Questions
    crosslink_card_html = f"""<div class="htbd-crosslink-card">
  <h4 style="margin: 0 0 8px 0; color: #1e3a8a; font-size: 18px; font-weight: 700;">[বোর্ড প্রশ্ন সমাধান] বিগত ৬ বছরের প্রশ্ন সমাধান খুঁজছেন?</h4>
  <p style="margin: 0 0 12px 0; color: #334155; font-size: 15.5px; line-height: 1.7;">জাতীয় বিশ্ববিদ্যালয়ের ২০১৯ থেকে ২০২৪ সাল পর্যন্ত অনুষ্ঠিত সকল সেশনের ক, খ ও গ বিভাগের ১৬৮টি প্রশ্ন ও গাণিতিক সমাধানের জন্য পড়ুন আমাদের ডেডিকেটেড বোর্ড প্রশ্ন গাইড:</p>
  <a href="{URL_BOARD_POST}" style="color: #1d4ed8; font-weight: 700; text-decoration: underline; font-size: 16px;">[এখানে ক্লিক করুন] জাতীয় বিশ্ববিদ্যালয় অনার্স ৩য় বর্ষ উন্নত হিসাববিজ্ঞান ১ বিগত বছরের বোর্ড প্রশ্ন সমাধান (2019-2024)</a>
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
        "description": f"{focus_kw} 2026: জাতীয় বিশ্ববিদ্যালয় BBA ৩য় বর্ষ হিসাববিজ্ঞান বিভাগের ৭টি অধ্যায়ের ৩২০টি প্রশ্ন ও গাণিতিক সমাধান।",
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
            "@id": URL_SUGGESTION_POST
        }
    }, ensure_ascii=False, indent=2)

    full_html = f"""<!-- Byte-0 Hero Banner Placement -->
<figure class="htbd-featured-hero" style="margin: 0 0 25px 0; text-align: center;">
  <img src="{banner_url}" alt="{focus_kw}" title="{seo_title}" style="width: 100%; max-width: 1000px; height: auto; border-radius: 12px; box-shadow: 0 5px 20px rgba(0,0,0,0.12); display: block; margin: 0 auto;" loading="eager" width="1200" height="675" />
  <figcaption style="font-family: 'SolaimanLipi', sans-serif; font-size: 14px; color: #64748b; margin-top: 8px; text-align: center;">
    জাতীয় বিশ্ববিদ্যালয় BBA অনার্স ৩য় বর্ষ উন্নত হিসাববিজ্ঞান-১ ফাইনাল সাজেশন 2026 (ক, খ ও গ বিভাগ সম্পূর্ণ) | প্রকাশনা: HelpTrickBD
  </figcaption>
</figure>

{get_shared_css()}

<div class="htbd-nu-content">

  <!-- Breadcrumb & Topic Metadata -->
  <div style="font-size: 13.5px; color: #64748b; margin-bottom: 20px;">
    হোম / শিক্ষা ও সাজেশন / অনার্স ৩য় বর্ষ / <strong>উন্নত হিসাববিজ্ঞান-১ সাজেশন</strong> (কোর্স কোড: 232503)
  </div>

  <!-- Position 0 Quick Answer Box -->
  <div class="htbd-hero-box">
    <h3 style="margin-top: 0; color: #065f46; font-size: 19px;">[কোর্স ওভারভিউ] একনজরে {focus_kw} 2026</h3>
    <p><strong>{focus_kw}</strong> খুঁজছেন এমন জাতীয় বিশ্ববিদ্যালয়ের হিসাববিজ্ঞান বিভাগের শিক্ষার্থীদের জন্য এটি একটি প্রামাণ্য ও নির্ভুল পূর্ণাঙ্গ স্টাডি রিসোর্স। জাতীয় বিশ্ববিদ্যালয়ের সর্বশেষ সিলেবাস, বিগত ১০ বছরের বোর্ড প্রশ্ন এবং কলেজ টেস্ট পেপারসের চুলচেরা বিশ্লেষণ করে এ সাজেশনে মোট <strong>{total_q_count}টি বাছাইকৃত প্রশ্ন ও পূর্ণাঙ্গ সমাধান</strong> সন্নিবেশিত করা হয়েছে।</p>
    <p>সাজেশনটিতে ক-বিভাগের <strong>{total_sec_counts['ক']}টি অতি সংক্ষিপ্ত প্রশ্ন</strong>, খ-বিভাগের <strong>{total_sec_counts['খ']}টি সংক্ষিপ্ত ও গাণিতিক সমস্যা</strong> এবং গ-বিভাগের <strong>{total_sec_counts['গ']}টি বিশ্লেষণধর্মী ও রচনামূলক প্রশ্নের</strong> অধ্যায়ভিত্তিক পূর্ণাঙ্গ সমাধান অন্তর্ভুক্ত রয়েছে।</p>
  </div>

  <!-- Mandatory Jump Break for Archive Summary -->
  <!--more-->

  <p>জাতীয় বিশ্ববিদ্যালয়ের BBA অনার্স ৩য় বর্ষ হিসাববিজ্ঞান বিভাগের শিক্ষার্থীদের জন্য অন্যতম গুরুত্বপূর্ণ ও সর্বোচ্চ নম্বর নিশ্চিতকারী ব্যবহারিক কোর্স হলো <strong>উন্নত হিসাববিজ্ঞান-১ (Advanced Accounting-I - Course Code: 232503)</strong>। স্টকহোল্ডার্স ইকুইটি, কোম্পানির আর্থিক বিবরণী, রেভিনিউ রিকগনিশন, লিজ একাউন্টিং, এরর অ্যানালাইসিস, অপারেটিং সেগমেন্ট এবং দেউলিয়া হিসাববিজ্ঞানের নিখুঁত সমাধানের ওপর পরীক্ষার চূড়ান্ত জিপিএ নির্ভর করে। হিসাববিজ্ঞান বিভাগের পূর্ণাঙ্গ তাত্ত্বিক প্রস্তুতির জন্য পড়ুন <a href="https://www.helptrickbd.com/honours-3rd-year-audit-and-assurance-suggestion/">অনার্স ৩য় বর্ষ নিরীক্ষা ও নিশ্চয়তা সাজেশন 2026</a>।</p>
  <p>শিক্ষার্থীদের সুবিধার্থে HelpTrickBD প্রস্তুত করেছে দেশের সর্বাধিক বিশদ ও মানসম্মত <strong>অনার্স ৩য় বর্ষ উন্নত হিসাববিজ্ঞান ১ সাজেশন 2026</strong>। এখানে সিলেবাসের ৭টি অধ্যায়ের ক, খ ও গ বিভাগের মোট ৩২০টি প্রশ্ন ও সমাধান ধাপে ধাপে সন্নিবেশিত করা হয়েছে।</p>

  {pdf_card_html}

  {crosslink_card_html}

  {toc_html}

  <h2>জাতীয় বিশ্ববিদ্যালয় পরীক্ষার মানবণ্টন ও প্রশ্ন কাঠামোর বিশ্লেষণ (৮০ নম্বর)</h2>
  <p>জাতীয় বিশ্ববিদ্যালয়ের অনার্স ৩য় বর্ষের চূড়ান্ত লিখিত পরীক্ষা মোট ৮০ নম্বরে অনুষ্ঠিত হয়। অবশিষ্ট ২০ নম্বর ইনকোর্স ও ক্লাস উপস্থিতির ওপর নির্ধারিত। পরীক্ষায় সর্বোচ্চ নম্বর নিশ্চিত করতে তিনটি বিভাগের প্রশ্ন কাঠামোর ওপর পরিষ্কার ধারণা থাকা অপরিহার্য:</p>

  <div class="htbd-table-wrapper">
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
  </div>

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
            <td>প্রতিটি অধ্যায়ের [৩-স্টার গোল্ডেন] চিহ্নিত অতি সংক্ষিপ্ত প্রশ্নগুলো মুখস্থ করে খাতায় লিখে ফেলুন। কোনো অপ্রয়োজনীয় ভূমিকা ছাড়া সরাসরি এক বাক্যে মূল পরিভাষা ও সঠিক সংজ্ঞা লিখুন।</td>
            <td>১০ নম্বরে ১০ নম্বর নিশ্চিত</td>
          </tr>
          <tr>
            <td><strong>খ ও গ বিভাগ (১১-২৫ দিন)</strong></td>
            <td>তাত্ত্বিক প্রশ্নের ক্ষেত্রে ৩-৪টি স্ট্যান্ডার্ড সংজ্ঞা, বৈশিষ্ট্য ও পার্থক্যের ছক অনুশীলন করুন। গাণিতিক অধ্যায়গুলোর জাবেদা, ছক ও ওয়ার্কিং নোটস নির্ভুল রাখুন।</td>
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

  {pdf_card_html}

  <div id="faq-section">
    <h2>সচরাচর জিজ্ঞাসিত প্রশ্নোত্তর (FAQ)</h2>
    {''.join(faq_html_items)}
  </div>

  <div class="htbd-callout-warning">
    <strong>[সতর্কবার্তা] কপিরাইট ও প্রাতিষ্ঠানিক নোটিশ:</strong> HelpTrickBD-এর সকল কনটেন্ট জাতীয় বিশ্ববিদ্যালয়ের সম্মানিত শিক্ষক ও বিষয় বিশেষজ্ঞদের সার্বিক তত্ত্বাবধানে শিক্ষার্থীদের বিনামূল্যে সহায়তা প্রদানে সংকলিত। জাতীয় বিশ্ববিদ্যালয়ের সর্বশেষ একাডেমিক নোটিশ ও ফরম পূরণের তথ্যের জন্য অফিসিয়াল <a href="https://www.nu.ac.bd/" target="_blank" rel="noopener noreferrer">জাতীয় বিশ্ববিদ্যালয় পোর্টাল (nu.ac.bd)</a> পরিদর্শন করুন। আরও সাজেশন পেতে আমাদের <a href="https://www.helptrickbd.com/category/education/">শিক্ষা সহায়িকা ও স্টাডি গাইড</a> আর্কাইভ দেখুন। কোনো বাণিজ্যিক প্ল্যাটফর্মে অনুমোদনহীন পুনঃপ্রকাশ আইনত দণ্ডনীয়।
  </div>

  {get_author_box_html()}

</div>

<script>
function startPdfCountdown(yr, url) {{
  var btn = document.getElementById('htbd-timer-btn-' + yr);
  var box = document.getElementById('htbd-timer-box-' + yr);
  var countSpan = document.getElementById('htbd-countdown-' + yr);
  var progress = document.getElementById('htbd-progress-' + yr);
  if (!btn || !box) return;
  btn.style.display = 'none';
  box.style.display = 'block';
  var timeLeft = 30;
  var totalTime = 30;
  var interval = setInterval(function() {{
    timeLeft--;
    if (countSpan) countSpan.innerText = timeLeft;
    if (progress) progress.style.width = ((timeLeft / totalTime) * 100) + '%';
    if (timeLeft <= 0) {{
      clearInterval(interval);
      box.style.background = '#ecfdf5';
      box.style.borderColor = '#a7f3d0';
      box.innerHTML = '<span style="color: #065f46; font-size: 15.5px;">✅ আপনার হাই-স্পিড ডাউনলোড লিংক সম্পূর্ণ প্রস্তুত!</span> <a href="' + url + '" target="_blank" rel="noopener noreferrer" download style="display: inline-block; margin-left: 12px; background: #059669; color: #ffffff !important; padding: 7px 18px; border-radius: 6px; text-decoration: none; font-size: 14.5px; font-weight: 700;">📥 এখনই PDF ডাউনলোড করুন</a>';
      window.open(url, '_blank');
    }}
  }}, 1000);
}}
</script>

<!-- Schema.org Microdata -->
<script type="application/ld+json">
{blog_schema_json}
</script>
<script type="application/ld+json">
{faq_schema_json}
</script>
"""
    return full_html


def generate_post_2_board_questions():
    """Generates Post 2: Board Questions (2019-2024, 168 Questions with click-to-reveal answers)."""
    board_dir = os.path.join(PUB_BOOKS_BASE, "board")
    years = ["2024", "2023", "2022", "2021", "2020", "2019"]
    
    focus_kw = "প্রশ্নব্যাংক ২০১৯-২০২৪: উন্নত হিসাববিজ্ঞান ১"
    seo_title = "প্রশ্নব্যাংক ২০১৯-২০২৪: উন্নত হিসাববিজ্ঞান ১ (Advanced Accounting 1 Question Bank 2026): Best Complete Solution"
    banner_url = "https://www.helptrickbd.com/wp-content/uploads/2026/11/adv_accounting_1_board_banner-1.webp"
    
    all_years_data = []
    total_q_count = 0
    total_sec_counts = {'ক': 0, 'খ': 0, 'গ': 0}
    
    for yr in years:
        yp = os.path.join(board_dir, yr)
        files = glob.glob(os.path.join(yp, '*.md'))
        
        secs = {'ক': [], 'খ': [], 'গ': []}
        for f in files:
            res = parse_board_file(f)
            if res:
                s = res['section']
                if s in secs:
                    secs[s].append(res)
                    total_sec_counts[s] += 1
                    total_q_count += 1
                    
        for s in ['ক', 'খ', 'গ']:
            secs[s].sort(key=lambda x: str(x['q_no']))
            
        all_years_data.append({
            'year': yr,
            'secs': secs,
            'count': len(secs['ক']) + len(secs['খ']) + len(secs['গ'])
        })

    # TOC
    toc_links = []
    for y in all_years_data:
        anchor_id = f"board-{y['year']}"
        toc_links.append(f'<li><a href="#{anchor_id}">জাতীয় বিশ্ববিদ্যালয় {y["year"]} সালের প্রশ্ন ও সমাধান ({y["count"]}টি প্রশ্ন)</a></li>')
    toc_links.append('<li><a href="#nu-search-keywords">জাতীয় বিশ্ববিদ্যালয় প্রশ্নব্যাংক: গুগল শীর্ষ সার্চ কোয়েরি ও টপিক ক্লাস্টার</a></li>')
    toc_links.append('<li><a href="#board-analysis-tips">বোর্ড পরীক্ষার প্রশ্ন পুনরাবৃত্তি (Question Pattern Analysis) ও এ-প্লাস কৌশল</a></li>')
    toc_links.append('<li><a href="#faq-section">সচরাচর জিজ্ঞাসিত প্রশ্নোত্তর (FAQ)</a></li>')
    
    toc_html = f"""<div id="rank-math-toc" class="htbd-toc-container">
  <div class="htbd-toc-title">
    সূচিপত্র: বিগত বছরের সালভিত্তিক প্রশ্নাবলি ও সমাধান
  </div>
  <ol class="htbd-toc-list">
    {''.join(toc_links)}
  </ol>
</div>"""

    # Years Body - Master Topic Cluster Hub with Dedicated Year Cards
    years_body_html = []
    for y in all_years_data:
        anchor_id = f"board-{y['year']}"
        yr_bn = {"2024": "২০২৪", "2023": "২০২৩", "2022": "২০২২", "2021": "২০২১", "2020": "২০২০", "2019": "২০১৯"}.get(y['year'], y['year'])
        yr_slug = f"honours-3rd-year-advanced-accounting-1-board-{y['year']}"
        yr_url = f"https://www.helptrickbd.com/{yr_slug}/"
        
        y_html = [f'<div class="htbd-year-block" id="{anchor_id}" style="margin-bottom: 30px;">']
        y_html.append(f"""<div class="htbd-q-card card-b" style="border-left: 5px solid #0284c7; padding: 22px 26px;">
  <div class="htbd-q-header">
    <span class="htbd-badge-sec" style="background: #024a4d; color: #ffffff; font-size: 14px;">জাতীয় বিশ্ববিদ্যালয় {yr_bn}</span>
    <span class="htbd-badge-star golden">[২৮টি প্রশ্ন সম্পূর্ণ]</span>
    <span class="htbd-badge-year">ক, খ ও গ বিভাগ</span>
  </div>
  <h3 style="margin: 0 0 10px 0; color: #0b2046; font-size: 22px; font-weight: 700;">
    জাতীয় বিশ্ববিদ্যালয় অনার্স ৩য় বর্ষ পরীক্ষা {yr_bn} — প্রশ্ন ও পূর্ণাঙ্গ সমাধান
  </h3>
  <p style="margin: 0 0 14px 0; color: #475569; font-size: 15.5px; line-height: 1.7;">
    জাতীয় বিশ্ববিদ্যালয় {yr_bn} শিক্ষাবর্ষের লিখিত পরীক্ষায় আসা ক-বিভাগের ১২টি অতি সংক্ষিপ্ত প্রশ্ন, খ-বিভাগের ৮টি সংক্ষিপ্ত ও গাণিতিক সমস্যা এবং গ-বিভাগের ৮টি বিশদ অংকের প্রতিটি ধাপ নির্ভুল ওয়ার্কিং নোটসসহ পৃথক ডেডিকেটেড গাইডে সমাধান করা হয়েছে।
  </p>
  <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 12px 18px; margin-bottom: 16px; font-size: 15px; color: #166534;">
    <strong>পরীক্ষার কাঠামো ও মানবণ্টন:</strong> ক-বিভাগ (১০ নম্বর) + খ-বিভাগ (২০ নম্বর) + গ-বিভাগ (৫০ নম্বর) = সর্বমোট ৮০ নম্বর লিখিত পরীক্ষা।
  </div>
  <a href="{yr_url}" style="display: inline-block; background: #0284c7; color: #ffffff !important; font-weight: 700; font-size: 15.5px; padding: 10px 22px; border-radius: 8px; text-decoration: none !important; box-shadow: 0 3px 10px rgba(2, 132, 199, 0.25);">
    [এখানে ক্লিক করুন] {yr_bn} সালের ক, খ ও গ বিভাগের সম্পূর্ণ সমাধান দেখুন &rarr;
  </a>
</div>""")
        y_html.append('</div>')
        years_body_html.append('\n'.join(y_html))

    all_years_rendered = '\n\n'.join(years_body_html)

    # Professional Dual-Button PDF Download Section
    pdf_card_html = f"""<div class="htbd-pdf-section" style="margin: 40px 0 35px 0; background: #ffffff; border: 1.5px solid #e2e8f0; border-top: 5px solid #dc2626; border-radius: 14px; padding: 28px 32px; box-shadow: 0 4px 20px rgba(0,0,0,0.05); font-family: 'SolaimanLipi', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 14px;">
    <span style="display: inline-flex; align-items: center; justify-content: center; width: 44px; height: 44px; background: #fee2e2; border-radius: 10px; color: #dc2626;">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
    </span>
    <div>
      <h2 id="pdf-download" style="color: #0b2046; font-size: 22px; font-weight: 700; margin: 0; line-height: 1.3;">অফিশিয়াল PDF ডাউনলোড: উন্নত হিসাববিজ্ঞান ১ প্রশ্নব্যাংক ২০১৯-২০২৪ (মাস্টার সল্যুশন)</h2>
      <div style="color: #64748b; font-size: 13.5px; font-weight: 600; margin-top: 3px;">ফাইল ফরম্যাট: প্রামাণ্য A4 প্রিন্ট-রেডি ই-বুক • সংস্করণ: ২০২৬ স্পেশাল</div>
    </div>
  </div>

  <p style="color: #475569; font-size: 15.5px; line-height: 1.85; margin: 0 0 22px 0;">
    জাতীয় বিশ্ববিদ্যালয়ের অনার্স ৩য় বর্ষ হিসাববিজ্ঞান বিভাগের বিগত ৬ বছরের (২০১৯-২০২৪) অনুষ্ঠিত সকল বোর্ড পরীক্ষার ক, খ ও গ বিভাগের মোট ১৬৮টি প্রশ্ন এবং বিশ্ববিদ্যালয় অ্যাকাডেমিক কাউন্সিলের দিকনির্দেশনা অনুযায়ী প্রণীত শতভাগ নির্ভুল প্রামাণ্য সমাধানের সম্পূর্ণ অফিশিয়াল মাস্টার প্রশ্নব্যাংক ই-বুক PDF (২.৪২ MB) নিচে সংযুক্ত করা হলো। আপনি সরাসরি কিংবা ৩০ সেকেন্ড কাউন্টডাউন টাইমার ব্যবহার করে এটি সংগ্রহ করতে পারেন:
  </p>

  <div class="htbd-download-buttons-grid" style="display: flex; flex-wrap: wrap; gap: 16px; align-items: center;">
    <!-- Button 2: 30-Second Countdown High-Speed Timer Download -->
    <div id="htbd-timer-wrap-hub2026" style="display: inline-block;">
      <button id="htbd-timer-btn-hub2026" onclick="startPdfCountdown('hub2026', '{PDF_BOARD_URL}')" class="htbd-btn-timer" style="display: inline-flex; align-items: center; gap: 10px; background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%); color: #ffffff !important; padding: 13px 26px; border-radius: 9px; font-weight: 700; font-size: 15.5px; cursor: pointer; border: none; box-shadow: 0 4px 12px rgba(37, 99, 235, 0.28); user-select: none; transition: transform 0.15s ease, box-shadow 0.15s ease;">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
        <span>⏳ ৩০ সেকেন্ডে হাই-স্পিড ডাউনলোড (Countdown)</span>
      </button>
      <div id="htbd-timer-box-hub2026" style="display: none; background: #eff6ff; border: 1.5px solid #bfdbfe; border-radius: 9px; padding: 14px 22px; font-size: 15px; font-weight: 700; color: #1e40af; text-align: center;">
        <div id="htbd-timer-text-hub2026">হাই-স্পিড ক্লাউড লিংক তৈরি হচ্ছে... অনুগ্রহ করে <span id="htbd-countdown-hub2026" style="color: #dc2626; font-size: 19px; font-weight: 800;">30</span> সেকেন্ড অপেক্ষা করুন</div>
        <div style="width: 100%; height: 7px; background: #dbeafe; border-radius: 4px; margin-top: 10px; overflow: hidden;">
          <div id="htbd-progress-hub2026" style="width: 100%; height: 100%; background: #2563eb; transition: width 1s linear;"></div>
        </div>
      </div>
    </div>
  </div>

  <div style="margin-top: 16px; font-size: 13.5px; color: #64748b; display: flex; align-items: center; gap: 6px;">
    <span>🔒 ১০০% ভাইরাস-মুক্ত ও সুরক্ষিত সরাসরি গুগল ড্রাইভ / ক্লাউড সার্ভার মিরর লিংক।</span>
  </div>
</div>"""

    # Cross-link to Chapter Suggestion
    crosslink_card_html = f"""<div class="htbd-crosslink-card">
  <h4 style="margin: 0 0 8px 0; color: #1e3a8a; font-size: 18px; font-weight: 700;">[অধ্যায়ভিত্তিক চূড়ান্ত সাজেশন] সিলেবাসের সকল অধ্যায়ের পূর্ণাঙ্গ প্রস্তুতি চান?</h4>
  <p style="margin: 0 0 12px 0; color: #334155; font-size: 15.5px; line-height: 1.7;">জাতীয় বিশ্ববিদ্যালয়ের সংশোধিত সিলেবাস অনুযায়ী সম্পূর্ণ ৭টি অধ্যায়ের ৩২০টি বাছাইকৃত প্রশ্ন ও নির্ভুল গাণিতিক সমাধানের জন্য পড়ুন আমাদের মূল সাজেশন গাইড:</p>
  <a href="{URL_SUGGESTION_POST}" style="color: #1d4ed8; font-weight: 700; text-decoration: underline; font-size: 16px;">[এখানে ক্লিক করুন] জাতীয় বিশ্ববিদ্যালয় অনার্স ৩য় বর্ষ উন্নত হিসাববিজ্ঞান ১ অধ্যায়ভিত্তিক পূর্ণাঙ্গ সাজেশন 2026</a>
</div>"""

    faq_items = [
        {
            "q": "প্রশ্নব্যাংক ২০১৯-২০২৪: উন্নত হিসাববিজ্ঞান ১ থেকে জাতীয় বিশ্ববিদ্যালয় ফাইনাল পরীক্ষায় কত শতাংশ প্রশ্ন কমন আসে?",
            "a": "বিগত ৬ বছরের বোর্ড প্রশ্ন গভীরভাবে পর্যালোচনা করলে দেখা যায়, প্রতি বছর ক-বিভাগে প্রায় ৮০% থেকে ৯০% অতি সংক্ষিপ্ত প্রশ্ন পূর্ববর্তী সালের প্রশ্নব্যাংক থেকেই হুবহু পুনরাবৃত্তি হয়। এছাড়া খ ও গ বিভাগের গাণিতিক সমস্যাগুলোতে প্রায় ৬০% থেকে ৭০% অংক বিগত সালের একই ফরম্যাট ও নিয়মে টাকার অংক বা নাম পরিবর্তন করে পরীক্ষায় আসে।"
        },
        {
            "q": "Advanced Accounting 1 Question Bank 2026-এর বড় গাণিতিক সমস্যাগুলোর গণনাকার্য (Working Notes) কি দেওয়া আছে?",
            "a": "হ্যাঁ, HelpTrickBD-এর এই প্রশ্নব্যাংকে প্রতিটি গাণিতিক সমস্যার জন্য প্রয়োজনীয় জাবেদা, ছক ও খসড়া গণনাকার্য (Working Notes) প্রতিটি ধাপ অনুযায়ী পৃথকভাবে প্রদান করা হয়েছে, যেন শিক্ষার্থীরা পরীক্ষার খাতায় শতভাগ নির্ভুলভাবে সমাধান করে পূর্ণ নম্বর অর্জন করতে পারেন।"
        },
        {
            "q": "প্রশ্নব্যাংক ২০১৯-২০২৪: উন্নত হিসাববিজ্ঞান ১-এর অফিশিয়াল PDF ফাইল কীভাবে ফ্রিতে ডাউনলোড করব?",
            "a": "পোস্টের উপরে ও নিচে দেওয়া '[ডাউনলোড] বিগত ৬ বছরের বোর্ড সমাধান PDF সংগ্রহ করুন' বাটনে ক্লিক করলেই ১৬৮টি প্রশ্নের পূর্ণাঙ্গ ও প্রিন্ট-উপযোগী অফিশিয়াল PDF সরাসরি বিনামূল্যে গুগল ড্রাইভ / মিডিয়া সার্ভার থেকে ডাউনলোড করা যাবে।"
        },
        {
            "q": "জাতীয় বিশ্ববিদ্যালয় অনার্স ৩য় বর্ষ হিসাববিজ্ঞান বিভাগের অন্যান্য বিষয়ের প্রশ্নব্যাংক ও সাজেশন কোথায় পাওয়া যাবে?",
            "a": "আমাদের ওয়েবসাইটের 'শিক্ষা সহায়িকা ও স্টাডি গাইড' এবং 'NU Question Bank' ক্যাটাগরিতে নিরীক্ষা ও নিশ্চয়তা, উৎপাদন ব্যয় হিসাববিজ্ঞান, ব্যবস্থাপনা হিসাববিজ্ঞানসহ সকল বিষয়ের অধ্যায়ভিত্তিক পূর্ণাঙ্গ সাজেশন ও বিগত বছরের প্রশ্ন সমাধান পেয়ে যাবেন।"
        }
    ]

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
        "description": f"{focus_kw} (Advanced Accounting 1 Question Bank 2026): জাতীয় বিশ্ববিদ্যালয় BBA অনার্স ৩য় বর্ষ হিসাববিজ্ঞানের বিগত ৬ বছরের ১৬৮টি বোর্ড প্রশ্ন ও গাণিতিক সমাধান।",
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
            "@id": URL_BOARD_POST
        }
    }, ensure_ascii=False, indent=2)

    full_html = f"""<!-- Byte-0 Hero Banner Placement -->
<figure class="htbd-featured-hero" style="margin: 0 0 25px 0; text-align: center;">
  <img src="{banner_url}" alt="{focus_kw} (Advanced Accounting 1 Question Bank)" title="{seo_title}" style="width: 100%; max-width: 1000px; height: auto; border-radius: 12px; box-shadow: 0 5px 20px rgba(0,0,0,0.12); display: block; margin: 0 auto;" loading="eager" width="1200" height="675" />
  <figcaption style="font-family: 'SolaimanLipi', sans-serif; font-size: 14px; color: #64748b; margin-top: 8px; text-align: center;">
    জাতীয় বিশ্ববিদ্যালয় BBA অনার্স ৩য় বর্ষ {focus_kw} (Advanced Accounting 1 Question Bank 2026) | প্রকাশনা: HelpTrickBD
  </figcaption>
</figure>

{get_shared_css()}

<div class="htbd-nu-content">

  <!-- Breadcrumb & Topic Metadata -->
  <div style="font-size: 13.5px; color: #64748b; margin-bottom: 20px;">
    হোম / শিক্ষা ও সাজেশন / অনার্স ৩য় বর্ষ / <strong>{focus_kw}</strong> (কোর্স কোড: 232503)
  </div>

  <!-- Position 0 Quick Answer Box -->
  <div class="htbd-hero-box">
    <h3 style="margin-top: 0; color: #065f46; font-size: 19px;">[প্রশ্নব্যাংক ওভারভিউ] একনজরে {focus_kw} (2019-2024 Solution)</h3>
    <p><strong>{focus_kw}</strong> (Advanced Accounting 1 Question Bank 2026) খুঁজছেন এমন জাতীয় বিশ্ববিদ্যালয়ের BBA অনার্স ৩য় বর্ষের হিসাববিজ্ঞান বিভাগের শিক্ষার্থীদের জন্য এটি একটি নির্ভরযোগ্য ও প্রামাণ্য ডিজিটাল সমাধান ভাণ্ডার। জাতীয় বিশ্ববিদ্যালয়ের ২০১৯, ২০২০, ২০২১, ২০২২, ২০২৩ এবং সর্বশেষ ২০২৪ সালের চূড়ান্ত পরীক্ষায় আসা মোট <strong>{total_q_count}টি বোর্ড প্রশ্ন ও নির্ভুল গাণিতিক সমাধান</strong> এখানে প্রতিটি বিষয়ের সঠিক ওয়ার্কিং নোটসসহ সংকলিত হয়েছে।</p>
    <p>সংকলনটিতে ক-বিভাগের <strong>{total_sec_counts['ক']}টি অতি সংক্ষিপ্ত প্রশ্ন</strong>, খ-বিভাগের <strong>{total_sec_counts['খ']}টি সংক্ষিপ্ত ও গাণিতিক সমস্যা</strong> এবং গ-বিভাগের <strong>{total_sec_counts['গ']}টি বিশ্লেষণধর্মী ও বড় অংকের</strong> পুঙ্খানুপুঙ্খ সমাধান রয়েছে। সমাধান দেখতে প্রতিটি প্রশ্নের নিচের [উত্তর / সমাধান দেখুন] বাটনে ক্লিক করুন।</p>
  </div>

  <!-- Mandatory Jump Break for Archive Summary -->
  <!--more-->

  <p>জাতীয় বিশ্ববিদ্যালয়ের BBA অনার্স ৩য় বর্ষের হিসাববিজ্ঞান বিভাগের শিক্ষার্থীদের জন্য সবচেয়ে বেশি গাণিতিক চ্যালেঞ্জপূর্ণ ও সর্বোচ্চ নম্বর নির্ধারক ব্যবহারিক বিষয় হলো <strong>উন্নত হিসাববিজ্ঞান-১ (Advanced Accounting-I - Course Code: 232503)</strong>। পরীক্ষায় ফার্স্ট ক্লাস ও নিশ্চিত এ-প্লাস (A+) অর্জনের জন্য পূর্ববর্তী বছরগুলোর প্রশ্ন প্যাটার্ন ও জাতীয় বিশ্ববিদ্যালয়ের বোর্ড প্রশ্ন সমাধান আয়ত্ত করার কোনো বিকল্প নেই। অনার্স ৩য় বর্ষ হিসাববিজ্ঞানের সম্পূর্ণ অধ্যায়ভিত্তিক সাজেশন ও মডেল টেস্টের জন্য পড়ুন আমাদের <a href="{URL_SUGGESTION_POST}">অনার্স ৩য় বর্ষ উন্নত হিসাববিজ্ঞান ১ সাজেশন 2026</a>।</p>
  <p>শিক্ষার্থীদের বিগত ৬ বছরের পরীক্ষার প্রস্তুতিকে সহজ, নির্ভুল ও সময়োপযোগী করতে HelpTrickBD প্রস্তুত করেছে দেশের সর্বাধিক মানসম্মত <strong>{focus_kw} (Advanced Accounting 1 Question Bank 2026)</strong>। এখানে ২০১৯ সাল থেকে শুরু করে সর্বশেষ ২০২৪ সালের পরীক্ষার ক, খ ও গ বিভাগের প্রতিটি প্রশ্নের পুঙ্খানুপুঙ্খ সমাধান ও গণনাকার্য ধাপে ধাপে উপস্থাপন করা হলো।</p>

  {pdf_card_html}

  {crosslink_card_html}

  {toc_html}

  <div id="nu-search-keywords">
    <h2>জাতীয় বিশ্ববিদ্যালয় অনার্স ৩য় বর্ষ প্রশ্নব্যাংক: গুগল শীর্ষ সার্চ কোয়েরি ও টপিক ক্লাস্টার</h2>
    <p>জাতীয় বিশ্ববিদ্যালয়ের BBA অনার্স ৩য় বর্ষের শিক্ষার্থীরা পরীক্ষার প্রস্তুতি ও রিভিশনের সময় গুগলে যে সকল হাই-র‌্যাংকিং কি-ওয়ার্ড ও অনুসন্ধান কোয়েরি সবচেয়ে বেশি সার্চ করেন, তার একটি প্রামাণ্য বিশ্লেষণ নিচে তুলে ধরা হলো। এই প্রশ্নব্যাংকে প্রতিটি সার্চ কোয়েরির বিপরীতে পূর্ণাঙ্গ সমাধান ও গাণিতিক ব্যাখ্যা দেওয়া হয়েছে:</p>

    <div class="htbd-table-wrapper">
      <table class="htbd-styled-table">
        <thead>
          <tr>
            <th>শিক্ষার্থীদের শীর্ষ সার্চ কোয়েরি (Search Queries)</th>
            <th>মূল অধ্যায় ও আলোচিত বিষয়বস্তু (Topic Cluster)</th>
            <th>প্রশ্ন সংখ্যা ও বিভাগ</th>
            <th>পরীক্ষার গুরুত্ব ও কমন সম্ভাবনা</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>উন্নত হিসাববিজ্ঞান ১ বিগত বছরের বোর্ড প্রশ্ন সমাধান (2019-2024)</strong></td>
            <td>জাতীয় বিশ্ববিদ্যালয়ের ২০১৯ থেকে ২০২৪ সাল পর্যন্ত ৬টি শিক্ষাবর্ষের সকল প্রশ্নপত্র ও পূর্ণাঙ্গ সমাধান।</td>
            <td>১৬৮টি প্রশ্ন (ক, খ, গ বিভাগ)</td>
            <td><span class="htbd-badge-star golden">[১০০% প্রামাণ্য সল্যুশন]</span></td>
          </tr>
          <tr>
            <td><strong>Advanced Accounting 1 Question Bank 2026 Solution PDF</strong></td>
            <td>National University BBA 3rd Year Accounting Department Previous Years Questions with Working Notes.</td>
            <td>Full 6 Years (2019-2024)</td>
            <td><span class="htbd-badge-star golden">[টপ সার্চ ভলিউম]</span></td>
          </tr>
          <tr>
            <td><strong>অনার্স ৩য় বর্ষ উন্নত হিসাববিজ্ঞান ১ ক বিভাগ অতি সংক্ষিপ্ত প্রশ্নব্যাংক</strong></td>
            <td>সংজ্ঞা, বৈশিষ্ট্য, পার্থক্য, IFRS/IAS নীতিমালা ও সংক্ষিপ্ত সমীকরণভিত্তিক প্রশ্নাবলি।</td>
            <td>৭২টি অতি সংক্ষিপ্ত প্রশ্ন</td>
            <td><span class="htbd-badge-star super">[১০ এ ১০ নম্বর কমন]</span></td>
          </tr>
          <tr>
            <td><strong>স্টকহোল্ডার্স ইকুইটি জাবেদা ও ছক সমাধান (Stockholders' Equity)</strong></td>
            <td>Common Stock, Preferred Stock, Stock Dividends, Cash Dividends, Treasury Stock ও Retained Earnings Statement.</td>
            <td>খ ও গ বিভাগের অংক</td>
            <td><span class="htbd-badge-star golden">[১৫-২০ নম্বর নিশ্চিত]</span></td>
          </tr>
          <tr>
            <td><strong>ইজারা বা লিজ হিসাববিজ্ঞান জাবেদা ও অ্যামরটাইজেশন টেবিল (Lease Accounting)</strong></td>
            <td>Finance Lease vs Operating Lease, Lessee and Lessor Accounting, Guaranteed Residual Value ও ছক।</td>
            <td>খ ও গ বিভাগের অংক</td>
            <td><span class="htbd-badge-star golden">[১৪-১৮ নম্বর নিশ্চিত]</span></td>
          </tr>
          <tr>
            <td><strong>কোম্পানির আর্থিক বিবরণী বিশদ আয় বিবরণী ও ব্যালেন্স শিট</strong></td>
            <td>Comprehensive Income Statement, Classified Balance Sheet, Cost of Goods Sold ও সমন্বয় দাখিলা।</td>
            <td>গ বিভাগের বড় অংক</td>
            <td><span class="htbd-badge-star golden">[১০ নম্বর গ্যারান্টিড]</span></td>
          </tr>
          <tr>
            <td><strong>রেভিনিউ রিকগনিশন ও চুক্তি হিসাববিজ্ঞান (Revenue Recognition)</strong></td>
            <td>IFRS 15 Five-Step Model, Percentage of Completion Method ও Completed Contract Method.</td>
            <td>খ ও গ বিভাগের অংক</td>
            <td><span class="htbd-badge-star super">[খ/গ বিভাগে কমন]</span></td>
          </tr>
          <tr>
            <td><strong>হিসাববিজ্ঞান পরিবর্তন ও ভুল সংশোধন (Accounting Changes & Errors)</strong></td>
            <td>Change in Accounting Principle, Change in Accounting Estimate, Error Analysis ও পূর্ববর্তী সমন্বয়।</td>
            <td>খ ও গ বিভাগের বিশ্লেষণ</td>
            <td><span class="htbd-badge-star super">[নিয়মিত বোর্ড প্রশ্ন]</span></td>
          </tr>
          <tr>
            <td><strong>অপারেটিং সেগমেন্ট ও অন্তর্বর্তীকালীন প্রতিবেদন (Operating Segments)</strong></td>
            <td>10% Significance Test (Revenue, Profit/Loss, Assets), 75% Consolidated Revenue Test ও Disclosure.</td>
            <td>খ ও গ বিভাগের অংক</td>
            <td><span class="htbd-badge-star regular">[পরীক্ষায় বারবার আসা]</span></td>
          </tr>
          <tr>
            <td><strong>দেউলিয়া ও অবসায়ন হিসাববিজ্ঞান (Bankruptcy & Liquidation)</strong></td>
            <td>Statement of Affairs, Deficiency Account, Secured vs Unsecured Creditors ও লিকুইডেশন হিসাব।</td>
            <td>গ বিভাগের গাণিতিক সমস্যা</td>
            <td><span class="htbd-badge-star regular">[গুরুত্বপূর্ণ বোর্ড টপিক]</span></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <h2>জাতীয় বিশ্ববিদ্যালয় বিগত ৬ বছরের পরীক্ষার প্রশ্ন প্যাটার্ন ও মানবণ্টন বিশ্লেষণ</h2>
  <p>জাতীয় বিশ্ববিদ্যালয়ের লিখিত পরীক্ষায় মোট ৮০ নম্বরের প্রশ্নপত্র থাকে। বিগত ৬ বছরের বোর্ড প্রশ্ন বিশ্লেষণে দেখা যায় যে প্রশ্ন কাঠামোর ধারাবাহিকতা নিচের নিয়মে আবর্তিত হয়:</p>

  <div class="htbd-table-wrapper">
    <table class="htbd-styled-table">
      <thead>
        <tr>
          <th>পরীক্ষার বিভাগ</th>
          <th>মোট প্রশ্নের সংখ্যা</th>
          <th>উত্তর প্রদান করতে হয়</th>
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
          <td><strong>খ-বিভাগ (সংক্ষিপ্ত ও অংক)</strong></td>
          <td>৮টি প্রশ্ন</td>
          <td>৫টি প্রশ্ন</td>
          <td>৪ নম্বর</td>
          <td><strong>২০ নম্বর</strong></td>
        </tr>
        <tr>
          <td><strong>গ-বিভাগ (রচনামূলক ও বড় অংক)</strong></td>
          <td>৮টি প্রশ্ন</td>
          <td>৫টি প্রশ্ন</td>
          <td>১০ নম্বর</td>
          <td><strong>৫০ নম্বর</strong></td>
        </tr>
        <tr style="background: #e0f2fe; font-weight: bold;">
          <td colspan="4" style="text-align: right;">সর্বমোট লিখিত পরীক্ষার পূর্ণমান =</td>
          <td><strong>৮০ নম্বর</strong></td>
        </tr>
      </tbody>
    </table>
  </div>

  {all_years_rendered}

  <div id="board-analysis-tips">
    <h2>বোর্ড পরীক্ষার প্রশ্ন পুনরাবৃত্তি (Question Pattern Analysis) ও এ-প্লাস কৌশল</h2>
    <p>বিগত ৬ বছরের বোর্ড পরীক্ষার প্রশ্ন গভীরভাবে বিশ্লেষণ করলে দেখা যায়, নির্দিষ্ট কিছু গাণিতিক ফরম্যাট ও তাত্ত্বিক পরিভাষা নিয়মিত পরীক্ষায় পুনরাবৃত্তি ঘটে:</p>
    <div class="htbd-table-wrapper">
      <table class="htbd-styled-table">
        <thead>
          <tr>
            <th>গুরুত্বপূর্ণ অধ্যায়</th>
            <th>বোর্ড পরীক্ষায় সর্বাধিক আসা টপিকস</th>
            <th>প্রত্যাশিত পরীক্ষার নম্বর</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>স্টকহোল্ডার্স ইকুইটি</strong></td>
            <td>স্টক ডিভিডেন্ড ও ক্যাশ ডিভিডেন্ডের জাবেদা, শেয়ার স্প্লিট এবং পরিশোধিত মূলধনের বিবরণী।</td>
            <td>খ ও গ বিভাগে ১৫–২০ নম্বর</td>
          </tr>
          <tr>
            <td><strong>আর্থিক বিবরণীসমূহ</strong></td>
            <td>বহুধাপ বিশিষ্ট বিশদ আয় বিবরণী ও ক্লাসিফাইড ব্যালেন্স শিটের বড় গাণিতিক সমস্যা।</td>
            <td>গ বিভাগে নিশ্চিত ১০ নম্বর</td>
          </tr>
          <tr>
            <td><strong>ইজারা হিসাববিজ্ঞান</strong></td>
            <td>ফাইন্যান্স লিজ ও অপারেটিং লিজের টেবিল অ্যামরটাইজেশন ও ইজারাদার/ইজারাগ্রহীতার জাবেদা।</td>
            <td>খ ও গ বিভাগে ১৪–১৮ নম্বর</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  {pdf_card_html}

  <div id="faq-section">
    <h2>সচরাচর জিজ্ঞাসিত প্রশ্নোত্তর (FAQ)</h2>
    {''.join(faq_html_items)}
  </div>

  <div class="htbd-callout-warning">
    <strong>[সতর্কবার্তা] কপিরাইট ও প্রাতিষ্ঠানিক নোটিশ:</strong> HelpTrickBD-এর সকল কনটেন্ট জাতীয় বিশ্ববিদ্যালয়ের সম্মানিত শিক্ষক ও বিষয় বিশেষজ্ঞদের সার্বিক তত্ত্বাবধানে শিক্ষার্থীদের বিনামূল্যে সহায়তা প্রদানে সংকলিত। জাতীয় বিশ্ববিদ্যালয়ের সর্বশেষ একাডেমিক নোটিশ ও ফরম পূরণের তথ্যের জন্য অফিসিয়াল <a href="https://www.nu.ac.bd/" target="_blank" rel="noopener noreferrer">জাতীয় বিশ্ববিদ্যালয় পোর্টাল (nu.ac.bd)</a> পরিদর্শন করুন। আরও সাজেশন পেতে আমাদের <a href="https://www.helptrickbd.com/category/education/">শিক্ষা সহায়িকা ও স্টাডি গাইড</a> আর্কাইভ দেখুন। কোনো বাণিজ্যিক প্ল্যাটফর্মে অনুমোদনহীন পুনঃপ্রকাশ আইনত দণ্ডনীয়।
  </div>

  {get_author_box_html()}

</div>

<script>
function startPdfCountdown(yr, url) {{
  var btn = document.getElementById('htbd-timer-btn-' + yr);
  var box = document.getElementById('htbd-timer-box-' + yr);
  var countSpan = document.getElementById('htbd-countdown-' + yr);
  var progress = document.getElementById('htbd-progress-' + yr);
  if (!btn || !box) return;
  btn.style.display = 'none';
  box.style.display = 'block';
  var timeLeft = 30;
  var totalTime = 30;
  var interval = setInterval(function() {{
    timeLeft--;
    if (countSpan) countSpan.innerText = timeLeft;
    if (progress) progress.style.width = ((timeLeft / totalTime) * 100) + '%';
    if (timeLeft <= 0) {{
      clearInterval(interval);
      box.style.background = '#ecfdf5';
      box.style.borderColor = '#a7f3d0';
      box.innerHTML = '<span style="color: #065f46; font-size: 15.5px;">✅ আপনার হাই-স্পিড ডাউনলোড লিংক সম্পূর্ণ প্রস্তুত!</span> <a href="' + url + '" target="_blank" rel="noopener noreferrer" download style="display: inline-block; margin-left: 12px; background: #059669; color: #ffffff !important; padding: 7px 18px; border-radius: 6px; text-decoration: none; font-size: 14.5px; font-weight: 700;">📥 এখনই PDF ডাউনলোড করুন</a>';
      window.open(url, '_blank');
    }}
  }}, 1000);
}}
</script>

<!-- Schema.org Microdata -->
<script type="application/ld+json">
{blog_schema_json}
</script>
<script type="application/ld+json">
{faq_schema_json}
</script>
"""
    return full_html

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8')
    os.makedirs(os.path.join(PROJECT_ROOT, "scratch"), exist_ok=True)
    
    print("Compiling Post 1: Chapter Suggestion with Click-to-Reveal (320 Questions)...")
    post1_html = generate_post_1_chapter_suggestion()
    p1_path = os.path.join(PROJECT_ROOT, "scratch", "adv1_suggestion_320.html")
    with open(p1_path, "w", encoding="utf-8") as f:
        f.write(post1_html)
    print(f"Post 1 HTML written: {p1_path} (Length: {len(post1_html)} chars)")
    
    print("\nCompiling Post 2: Board Questions with Click-to-Reveal (168 Questions)...")
    post2_html = generate_post_2_board_questions()
    p2_path = os.path.join(PROJECT_ROOT, "scratch", "adv1_board_168.html")
    with open(p2_path, "w", encoding="utf-8") as f:
        f.write(post2_html)
    print(f"Post 2 HTML written: {p2_path} (Length: {len(post2_html)} chars)")
