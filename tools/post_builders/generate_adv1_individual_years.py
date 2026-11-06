#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/post_builders/generate_adv1_individual_years.py
-----------------------------------------------------
Generates the 6 individual dedicated posts for Advanced Accounting-1 Board Questions:
- Year 2024 (28 questions) -> Slug: honours-3rd-year-advanced-accounting-1-board-2024
- Year 2023 (28 questions) -> Slug: honours-3rd-year-advanced-accounting-1-board-2023
- Year 2022 (28 questions) -> Slug: honours-3rd-year-advanced-accounting-1-board-2022
- Year 2021 (28 questions) -> Slug: honours-3rd-year-advanced-accounting-1-board-2021
- Year 2020 (28 questions) -> Slug: honours-3rd-year-advanced-accounting-1-board-2020
- Year 2019 (28 questions) -> Slug: honours-3rd-year-advanced-accounting-1-board-2019

Features:
- Individual dedicated banners with NU Logo & PDF Download Badge.
- Click-to-reveal Interactive Accordions (<details><summary>).
- Position 0 Lead Box.
- Year Navigation Bar (bidirectional cross-linking).
- Rank Math TOC, FAQPage & BlogPosting Schema.
- Zero-Emoji Policy & SolaimanLipi typography.
"""

import os
import sys
import re
import glob
import json
import yaml
from markdown_it import MarkdownIt
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.post_builders.academic_answer_enricher import enrich_answer_markdown
from tools.post_builders.pdf_download_component import render_pdf_download_section

md_engine = MarkdownIt('commonmark').enable('table').enable('strikethrough')
PUB_BOOKS_BASE = r'D:\android\Project\Publication Books\questions\advanced_accounting_1'
PDF_BOARD_URL = "https://www.helptrickbd.com/wp-content/uploads/2026/11/HelpTrickBD_232503_Advanced_Accounting_1_Board_Questions_2019_2024.pdf"
AUTHOR_IMG_URL = "https://www.helptrickbd.com/wp-content/uploads/2026/11/faruk_sir.webp"
URL_SUGGESTION_POST = "https://www.helptrickbd.com/honours-3rd-year-advanced-accounting-1-suggestion/"
URL_BOARD_HUB = "https://www.helptrickbd.com/honours-3rd-year-advanced-accounting-1-board-questions/"

YEARS = ["2024", "2023", "2022", "2021", "2020", "2019"]
YEAR_BN_MAP = {
    "2024": "২০২৪",
    "2023": "২০২৩",
    "2022": "২০২২",
    "2021": "২০২১",
    "2020": "২০২০",
    "2019": "২০১৯"
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
    exam_year = fm.get('exam_year', '')
    
    if imp == 3 or '3' in str(imp):
        imp_badge = '<span class="htbd-badge-star golden" style="font-size: 12.5px; font-weight: 700; padding: 4px 10px; border-radius: 6px; background: #fef3c7; color: #92400e; border: 1px solid #fde68a;">[৩-স্টার গোল্ডেন]</span>'
    elif imp == 2 or '2' in str(imp):
        imp_badge = '<span class="htbd-badge-star super" style="font-size: 12.5px; font-weight: 700; padding: 4px 10px; border-radius: 6px; background: #ecfdf5; color: #065f46; border: 1px solid #a7f3d0;">[২-স্টার সুপার]</span>'
    else:
        imp_badge = '<span class="htbd-badge-star regular" style="font-size: 12.5px; font-weight: 600; padding: 4px 10px; border-radius: 6px; background: #f1f5f9; color: #475569; border: 1px solid #cbd5e1;">[বোর্ড প্রশ্ন]</span>'
        
    year_badge = f'<span class="htbd-badge-year" style="font-size: 12.5px; font-weight: 600; padding: 4px 10px; border-radius: 6px; background: #e2e8f0; color: #334155; border: 1px solid #cbd5e1;">জাতীয় বিশ্ববিদ্যালয় {exam_year}</span>'
        
    # Robust split between question and answer
    split_match = re.split(r'\n\s*(?:##\s*)?(?:উত্তর\s*/\s*সমাধান|সমাধান\s*/\s*উত্তর|উত্তর|সমাধান)[\s:]*\n?', body, flags=re.IGNORECASE)
    if len(split_match) >= 2:
        q_raw = split_match[0].strip()
        ans_text = '\n'.join(split_match[1:]).strip()
    else:
        lines = body.split('\n')
        q_raw = lines[0]
        ans_text = '\n'.join(lines[1:]).strip()
        
    # Remove leading 'প্রশ্ন:'
    q_raw = re.sub(r'^(?:##\s*)?প্রশ্ন[\s:]*\n?', '', q_raw, flags=re.IGNORECASE).strip()
    
    # Extract English question if present
    eng_match = re.search(r'\*\*English:\*\*[\s]*(.*)', q_raw, re.DOTALL)
    if eng_match:
        eng_text = eng_match.group(1).strip()
        bn_text = re.sub(r'\*\*English:\*\*.*', '', q_raw, flags=re.DOTALL).strip()
    else:
        eng_text = ""
        bn_text = q_raw
        
    # Extract tags
    tags = fm.get('tags', [])
    if not isinstance(tags, list):
        tags = [str(tags)]
        
    # Enrich Section B and Section C answers with academic Introduction & Conclusion
    ans_text_enriched = enrich_answer_markdown(sec, q_no, bn_text, tags, ans_text)
    
    ans_html = md_engine.render(ans_text_enriched)
    # Wrap markdown tables in responsive container for smooth mobile display
    ans_html = re.sub(r'(<table[\s\S]*?</table>)', r'<div class="htbd-table-responsive" style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 16px 0;">\1</div>', ans_html)
    ans_html = ans_html.replace('★', '').replace('⭐', '').replace('✨', '')
    bn_text = bn_text.replace('★', '').replace('⭐', '').replace('✨', '')
    eng_text = eng_text.replace('★', '').replace('⭐', '').replace('✨', '')
    
    return {
        'id': fm.get('id', ''),
        'section': sec,
        'q_no': q_no,
        'imp_badge': imp_badge,
        'year_badge': year_badge,
        'bn_text': bn_text,
        'eng_text': eng_text,
        'ans_html': ans_html
    }

def get_shared_css():
    return """<style>
/* Helptrickbd SolaimanLipi Font & Clean Design System */
@import url('https://cdn.jsdelivr.net/gh/ekushey/solaimanlipi@latest/solaimanlipi.css');
.htbd-nu-content {
  font-family: 'SolaimanLipi', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  font-size: 17.5px;
  line-height: 1.85;
  color: #1e293b;
  max-width: 100%;
}
.htbd-hero-box {
  background: #f0fdf4;
  border-left: 5px solid #10b981;
  padding: 22px 26px;
  margin: 22px 0 28px 0;
  border-radius: 0 10px 10px 0;
  box-shadow: 0 2px 8px rgba(16, 185, 129, 0.08);
}
.htbd-toc-container {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-left: 4px solid #2563eb;
  padding: 20px 24px;
  margin: 26px 0;
  border-radius: 0 8px 8px 0;
}
.htbd-toc-title {
  font-size: 19px;
  font-weight: 700;
  color: #0b2046;
  margin-bottom: 12px;
}
.htbd-toc-list {
  margin: 0;
  padding-left: 22px;
}
.htbd-toc-list li {
  margin-bottom: 8px;
}
.htbd-toc-list a {
  color: #1d4ed8;
  text-decoration: none;
  font-weight: 600;
}
.htbd-toc-list a:hover {
  text-decoration: underline;
}
.htbd-nav-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin: 18px 0 24px 0;
}
.htbd-nav-btn {
  display: inline-block;
  padding: 8px 16px;
  background: #f1f5f9;
  border: 1.5px solid #cbd5e1;
  border-radius: 8px;
  color: #0b2046;
  text-decoration: none;
  font-size: 14.5px;
  font-weight: 600;
  transition: all 0.2s ease;
}
.htbd-nav-btn:hover {
  background: #0284c7;
  color: #ffffff;
  border-color: #0284c7;
}
.htbd-nav-btn.active {
  background: #065f46;
  color: #ffffff;
  border-color: #047857;
  font-weight: 700;
}
.htbd-download-card {
  background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
  border: 2px dashed #10b981;
  border-radius: 12px;
  padding: 22px 26px;
  margin: 28px 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 16px;
}
.htbd-download-btn {
  display: inline-block;
  background: #065f46;
  color: #ffffff !important;
  font-weight: 700;
  font-size: 16px;
  padding: 12px 24px;
  border-radius: 8px;
  text-decoration: none !important;
  box-shadow: 0 4px 12px rgba(6, 95, 70, 0.25);
}
.htbd-crosslink-card {
  background: #eff6ff;
  border-left: 4px solid #3b82f6;
  padding: 18px 22px;
  margin: 22px 0;
  border-radius: 0 8px 8px 0;
}
.htbd-q-card {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 10px;
  padding: 18px 22px;
  margin-bottom: 18px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.03);
}
.htbd-q-card.card-b {
  border-left: 4px solid #10b981;
}
.htbd-q-card {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 0;
  margin-bottom: 24px;
  box-shadow: 0 4px 14px rgba(0,0,0,0.04);
  overflow: hidden;
}
.htbd-q-card.card-a {
  border-left: 5px solid #0284c7;
}
.htbd-q-card.card-b {
  border-left: 5px solid #10b981;
}
.htbd-q-card.card-c {
  border-left: 5px solid #8b5cf6;
}
.htbd-q-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 10px;
  background: #f8fafc;
  padding: 12px 20px;
  border-bottom: 1px solid #e2e8f0;
}
.htbd-q-header-left, .htbd-q-header-right {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
}
.htbd-badge-sec {
  font-size: 13.5px;
  font-weight: 700;
  padding: 4px 12px;
  border-radius: 6px;
  letter-spacing: 0.2px;
}
.htbd-q-num {
  font-size: 15.5px;
  font-weight: 700;
  color: #0b2046;
}
.htbd-badge-star {
  font-size: 13px;
  font-weight: 700;
  padding: 3px 10px;
  border-radius: 4px;
}
.htbd-badge-star.golden {
  background: #fef3c7;
  color: #b45309;
  border: 1px solid #fde68a;
}
.htbd-badge-star.super {
  background: #dbeafe;
  color: #1e40af;
  border: 1px solid #bfdbfe;
}
.htbd-badge-star.regular {
  background: #f1f5f9;
  color: #475569;
  border: 1px solid #cbd5e1;
}
.htbd-badge-year {
  background: #f3e8ff;
  color: #6b21a8;
  font-size: 13px;
  font-weight: 600;
  padding: 3px 10px;
  border-radius: 4px;
  border: 1px solid #e9d5ff;
}
.htbd-q-body {
  padding: 20px 22px 14px 22px;
}
.htbd-q-bengali {
  font-size: 18.5px;
  font-weight: 700;
  color: #0f172a;
  line-height: 1.65;
  margin-bottom: 10px;
}
.htbd-q-english {
  font-size: 15px;
  color: #64748b;
  font-family: 'Segoe UI', Roboto, sans-serif;
  font-style: italic;
  margin-bottom: 14px;
  padding-left: 12px;
  border-left: 2px solid #cbd5e1;
  line-height: 1.5;
}
.htbd-ans-details {
  margin: 0 22px 18px 22px;
}
summary::-webkit-details-marker { display: none !important; }
summary { list-style: none !important; }
.htbd-ans-btn:hover { opacity: 0.92; transform: translateY(-1px); }
details[open] summary .htbd-toggle-arrow { transform: rotate(180deg); }
.htbd-ans-toggle {
  cursor: pointer;
  user-select: none;
  font-weight: 700;
  color: #065f46;
  outline: none;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 7px 18px;
  border-radius: 8px;
  background: #f0fdf4;
  border: 1.5px solid #86efac;
  font-size: 14.5px;
  transition: all 0.2s ease;
}
.htbd-ans-toggle:hover {
  background: #dcfce7;
  color: #047857;
}
.htbd-ans-box {
  margin-top: 12px;
  padding: 18px 20px;
  background: #f8fafc;
  border-radius: 8px;
  border: 1px solid #e2e8f0;
  border-left: 4px solid #10b981;
  overflow-x: auto;
}
.htbd-ans-label {
  font-size: 15.5px;
  font-weight: 700;
  color: #065f46;
  margin-bottom: 10px;
}
.htbd-ans-box p {
  margin: 0 0 10px 0;
}
.htbd-ans-box p:last-child {
  margin-bottom: 0;
}
.htbd-ans-box table {
  width: 100%;
  border-collapse: collapse;
  margin: 12px 0;
}
.htbd-ans-box th, .htbd-ans-box td {
  border: 1px solid #cbd5e1;
  padding: 8px 12px;
  font-size: 15.5px;
}
.htbd-ans-box th {
  background: #e2e8f0;
}
.htbd-table-wrapper {
  overflow-x: auto;
  margin: 22px 0;
}
.htbd-styled-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 16px;
}
.htbd-styled-table th, .htbd-styled-table td {
  border: 1px solid #cbd5e1;
  padding: 10px 14px;
}
.htbd-styled-table th {
  background: #f1f5f9;
  color: #0b2046;
  font-weight: 700;
}
.htbd-callout-warning {
  background: #fffbeb;
  border-left: 4px solid #f59e0b;
  padding: 16px 20px;
  margin: 26px 0;
  border-radius: 0 8px 8px 0;
  font-size: 15.5px;
  color: #92400e;
}
.htbd-author-box {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 22px 26px;
  margin: 32px 0;
  display: flex;
  align-items: center;
  gap: 20px;
}
.htbd-author-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid #ffffff;
  box-shadow: 0 3px 10px rgba(0,0,0,0.1);
  display: block;
}
.htbd-faq-item {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 16px 20px;
  margin-bottom: 12px;
}
.htbd-faq-q {
  margin: 0 0 8px 0;
  color: #0b2046;
  font-size: 16.5px;
}
.htbd-faq-a {
  margin: 0;
  color: #475569;
  font-size: 15px;
}
/* Dark Mode Support (.dark, [data-theme="dark"], and prefers-color-scheme) */
.dark .htbd-nu-content,
[data-theme="dark"] .htbd-nu-content {
  color: #e2e8f0;
}
.dark .htbd-hero-box,
[data-theme="dark"] .htbd-hero-box {
  background: #064e3b22;
  border-color: #059669;
}
.dark .htbd-toc-container,
[data-theme="dark"] .htbd-toc-container {
  background: #1e293b;
  border-color: #334155;
}
.dark .htbd-q-card,
[data-theme="dark"] .htbd-q-card {
  background: #1e293b;
  border-color: #334155;
}
.dark .htbd-q-header,
[data-theme="dark"] .htbd-q-header {
  background: #0f172a;
  border-color: #334155;
}
.dark .htbd-q-num,
[data-theme="dark"] .htbd-q-num {
  color: #f8fafc;
}
.dark .htbd-q-bengali,
[data-theme="dark"] .htbd-q-bengali {
  color: #f8fafc;
}
.dark .htbd-q-english,
[data-theme="dark"] .htbd-q-english {
  color: #94a3b8;
  border-color: #475569;
}
.dark .htbd-ans-box,
[data-theme="dark"] .htbd-ans-box {
  background: #0f172a;
  border-color: #334155;
  border-left-color: #10b981;
}
.dark .htbd-ans-label,
[data-theme="dark"] .htbd-ans-label {
  color: #34d399;
}
.dark .htbd-ans-toggle,
[data-theme="dark"] summary::-webkit-details-marker { display: none !important; }
summary { list-style: none !important; }
.htbd-ans-btn:hover { opacity: 0.92; transform: translateY(-1px); }
details[open] summary .htbd-toggle-arrow { transform: rotate(180deg); }
.htbd-ans-toggle {
  background: #064e3b33;
  border-color: #059669;
  color: #a7f3d0;
}
.dark .htbd-download-card,
[data-theme="dark"] .htbd-download-card {
  background: #064e3b33;
  border-color: #059669;
}
.dark .htbd-styled-table th,
[data-theme="dark"] .htbd-styled-table th {
  background: #1e293b;
  color: #f8fafc;
  border-color: #334155;
}
.dark .htbd-styled-table td,
[data-theme="dark"] .htbd-styled-table td {
  border-color: #334155;
}
.dark .htbd-author-box,
[data-theme="dark"] .htbd-author-box {
  background: #1e293b;
  border-color: #334155;
}
.dark .htbd-nav-btn,
[data-theme="dark"] .htbd-nav-btn {
  background: #1e293b;
  border-color: #334155;
  color: #cbd5e1;
}
.dark .htbd-faq-item,
[data-theme="dark"] .htbd-faq-item {
  background: #1e293b;
  border-color: #334155;
}
.dark .htbd-faq-q,
[data-theme="dark"] .htbd-faq-q {
  color: #f8fafc;
}
.dark .htbd-faq-a,
[data-theme="dark"] .htbd-faq-a {
  color: #cbd5e1;
}
@media (prefers-color-scheme: dark) {
  .htbd-nu-content { color: #e2e8f0; }
  .htbd-hero-box { background: #064e3b22; border-color: #059669; }
  .htbd-toc-container { background: #1e293b; border-color: #334155; }
  .htbd-q-card { background: #1e293b; border-color: #334155; }
  .htbd-q-header { background: #0f172a; border-color: #334155; }
  .htbd-q-num { color: #f8fafc; }
  .htbd-q-bengali { color: #f8fafc; }
  .htbd-q-english { color: #94a3b8; border-color: #475569; }
  .htbd-ans-box { background: #0f172a; border-color: #334155; border-left-color: #10b981; }
  .htbd-ans-label { color: #34d399; }
  summary::-webkit-details-marker { display: none !important; }
summary { list-style: none !important; }
.htbd-ans-btn:hover { opacity: 0.92; transform: translateY(-1px); }
details[open] summary .htbd-toggle-arrow { transform: rotate(180deg); }
.htbd-ans-toggle { background: #064e3b33; border-color: #059669; color: #a7f3d0; }
  .htbd-download-card { background: #064e3b33; border-color: #059669; }
  .htbd-styled-table th { background: #1e293b; color: #f8fafc; border-color: #334155; }
  .htbd-styled-table td { border-color: #334155; }
  .htbd-author-box { background: #1e293b; border-color: #334155; }
  .htbd-nav-btn { background: #1e293b; border-color: #334155; color: #cbd5e1; }
  .htbd-faq-item { background: #1e293b; border-color: #334155; }
  .htbd-faq-q { color: #f8fafc; }
  .htbd-faq-a { color: #cbd5e1; }
}
</style>"""


def get_author_box_html():
    return f"""<div class="htbd-author-box" style="display: flex; align-items: center; gap: 20px; margin: 35px 0 25px 0; padding: 22px 26px; background: #f8fafc; border: 1.5px solid #e2e8f0; border-left: 5px solid #2563eb; border-radius: 12px; font-family: 'SolaimanLipi', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <img src="{AUTHOR_IMG_URL}" alt="মো: ওমর ফারুক (Faruk Sir)" class="htbd-author-avatar" width="80" height="80" loading="lazy" style="width: 80px !important; height: 80px !important; min-width: 80px !important; max-width: 80px !important; border-radius: 50% !important; object-fit: cover !important; border: 2.5px solid #2563eb !important; flex-shrink: 0 !important; display: block !important; margin: 0 !important; box-shadow: 0 3px 8px rgba(0,0,0,0.1) !important;" onerror="this.onerror=null; this.src='https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/author/faruk_sir.webp';" />
  <div style="flex: 1 1 auto; min-width: 0;">
    <h4 style="margin: 0 0 6px 0; color: #0b2046; font-size: 19px; font-weight: 700; line-height: 1.3;">মো: ওমর ফারুক (Faruk Sir)</h4>
    <p style="margin: 0; color: #475569; font-size: 14.5px; line-height: 1.6;">প্রতিষ্ঠাতা ও প্রধান শিক্ষা সম্পাদক, HelpTrickBD। শিক্ষার্থীদের জন্য দীর্ঘ ৮+ বছর যাবত মানসম্মত একাডেমিক গাইড, হ্যান্ডনোট ও চূড়ান্ত সাজেশন প্রণয়ন করছেন।</p>
  </div>
</div>"""

def generate_individual_year_post(year_en: str, media_info: dict):
    year_bn = YEAR_BN_MAP[year_en]
    board_dir = os.path.join(PUB_BOOKS_BASE, "board", year_en)
    files = glob.glob(os.path.join(board_dir, '*.md'))
    
    focus_kw = f"প্রশ্নব্যাংক {year_bn}: উন্নত হিসাববিজ্ঞান ১"
    seo_title = f"প্রশ্নব্যাংক {year_bn}: উন্নত হিসাববিজ্ঞান ১ (Advanced Accounting 1 Solution {year_en}): Complete Board Guide"
    slug = f"honours-3rd-year-advanced-accounting-1-board-{year_en}"
    post_url = f"https://www.helptrickbd.com/{slug}/"
    banner_url = media_info['source_url']
    
    secs = {'ক': [], 'খ': [], 'গ': []}
    for f in files:
        res = parse_board_file(f)
        if res:
            s = res['section']
            if s in secs:
                secs[s].append(res)
    for s in ['ক', 'খ', 'গ']:
        secs[s].sort(key=lambda x: str(x['q_no']))
        
    total_q = len(secs['ক']) + len(secs['খ']) + len(secs['গ'])
    
    # Year Navigation Grid
    nav_links = []
    for y in YEARS:
        y_bn = YEAR_BN_MAP[y]
        active_cls = " active" if y == year_en else ""
        y_slug = f"honours-3rd-year-advanced-accounting-1-board-{y}"
        nav_links.append(f'<a href="https://www.helptrickbd.com/{y_slug}/" class="htbd-nav-btn{active_cls}">প্রশ্নব্যাংক {y_bn}</a>')
    nav_links.append(f'<a href="{URL_BOARD_HUB}" class="htbd-nav-btn" style="background: #e0f2fe; color: #0369a1; font-weight: 700;">[সকল সাল ২০১৯-২০২৪]</a>')
    nav_links.append(f'<a href="{URL_SUGGESTION_POST}" class="htbd-nav-btn" style="background: #fef3c7; color: #b45309; font-weight: 700;">[অধ্যায়ভিত্তিক সাজেশন ২০২৬]</a>')
    nav_html = f"""<div style="margin: 20px 0 25px 0;">
  <div style="font-size: 15px; font-weight: 700; color: #475569; margin-bottom: 8px;">অন্যান্য সালের বোর্ড প্রশ্ন ও সমাধান বেছে নিন:</div>
  <div class="htbd-nav-grid">
    {''.join(nav_links)}
  </div>
</div>"""

    def build_card(q, sec_badge, card_class, sec_bg, sec_color, accent_color, btn_gradient, btn_shadow, btn_text):
        eng_block = ""
        if q['eng_text']:
            eng_block = f"""    <div class="htbd-q-english" style="font-size: 15px; color: #475569; font-style: italic; background: #f8fafc; padding: 10px 14px; border-radius: 6px; border-left: 3px solid #94a3b8; margin-top: 8px; margin-bottom: 6px; line-height: 1.5;">
      <strong>English:</strong> {q['eng_text']}
    </div>"""
            
        return f"""<div class="htbd-q-card {card_class}" style="background: #ffffff; border: 1.5px solid #e2e8f0; border-left: 5px solid {accent_color}; border-radius: 12px; margin-bottom: 26px; box-shadow: 0 4px 14px rgba(0,0,0,0.04); overflow: hidden;">
  <div class="htbd-q-header" style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; background: #f8fafc; padding: 12px 18px; border-bottom: 1px solid #e2e8f0;">
    <div class="htbd-q-header-left" style="display: flex; align-items: center; gap: 8px; flex-wrap: wrap;">
      <span class="htbd-badge-sec" style="font-size: 13.5px; font-weight: 700; padding: 4px 12px; border-radius: 6px; background: {sec_bg}; color: {sec_color}; letter-spacing: 0.2px;">{sec_badge}</span>
      <span class="htbd-q-num" style="font-size: 16px; font-weight: 700; color: #0b2046;">প্রশ্ন নং {q['q_no']}</span>
    </div>
    <div class="htbd-q-header-right" style="display: flex; align-items: center; gap: 8px; flex-wrap: wrap;">
      {q['imp_badge']}
      {q['year_badge']}
    </div>
  </div>
  <div class="htbd-q-body" style="padding: 18px 20px;">
    <div class="htbd-q-bengali" style="font-size: 17.5px; font-weight: 700; color: #0f172a; line-height: 1.65; margin-bottom: 10px;">
      {q['bn_text']}
    </div>
{eng_block}
  </div>
  <details class="htbd-ans-details" style="margin: 0; border: none; background: transparent;">
    <summary class="htbd-ans-btn" style="display: inline-flex; align-items: center; gap: 8px; background: {btn_gradient}; color: #ffffff !important; padding: 10px 22px; border-radius: 8px; font-weight: 700; font-size: 15px; cursor: pointer; border: none; box-shadow: 0 3px 10px {btn_shadow}; list-style: none; user-select: none; outline: none; margin: 0 0 16px 20px; transition: transform 0.15s ease, box-shadow 0.15s ease;">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0;"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
      <span style="letter-spacing: 0.3px;">[{btn_text}]</span>
      <span class="htbd-toggle-arrow" style="font-size: 11px; margin-left: 4px; opacity: 0.85;">▼</span>
    </summary>
    <div class="htbd-ans-box" style="background: #f8fafc; border-top: 1.5px solid #e2e8f0; border-left: 5px solid {accent_color}; padding: 20px 24px; font-size: 16.5px; color: #1e293b; line-height: 1.8;">
      <div class="htbd-ans-label" style="font-weight: 700; color: {accent_color}; margin-bottom: 12px; font-size: 16px; display: flex; align-items: center; gap: 6px;">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
        <span>[প্রামাণ্য সমাধান ও নির্ভুল ব্যাখ্যা]:</span>
      </div>
      {q['ans_html']}
    </div>
  </details>
</div>"""

    # Section A rendered (Blue Button)
    sec_a_html = [build_card(q, "ক-বিভাগ (১ নম্বর)", "card-a", "#0284c7", "#ffffff", "#0284c7", "linear-gradient(135deg, #0284c7 0%, #0369a1 100%)", "rgba(2, 132, 199, 0.3)", "উত্তর দেখুন") for q in secs['ক']]

    # Section B rendered (Emerald Green Button)
    sec_b_html = [build_card(q, "খ-বিভাগ (৪ নম্বর)", "card-b", "#059669", "#ffffff", "#059669", "linear-gradient(135deg, #059669 0%, #047857 100%)", "rgba(5, 150, 105, 0.3)", "সমাধান দেখুন") for q in secs['খ']]

    # Section C rendered (Royal Purple Button)
    sec_c_html = [build_card(q, "গ-বিভাগ (১০ নম্বর)", "card-c", "#7c3aed", "#ffffff", "#7c3aed", "linear-gradient(135deg, #7c3aed 0%, #6d28d9 100%)", "rgba(124, 58, 237, 0.3)", "সম্পূর্ণ সমাধান দেখুন") for q in secs['গ']]

    # Professional PDF Download Section (30s Countdown Timer Mode - End of Post)
    pdf_card_html = render_pdf_download_section(
        pdf_url=PDF_BOARD_URL,
        heading_title=f"{focus_kw} (ক, খ ও গ বিভাগের পূর্ণাঙ্গ সমাধান)",
        file_spec="ফাইল ফরম্যাট: প্রামাণ্য A4 প্রিন্ট-রেডি ই-বুক • ফাইল সাইজ: ২.৪২ MB • সংস্করণ: ২০২৬ স্পেশাল",
        description_text=f"জাতীয় বিশ্ববিদ্যালয়ের অনার্স ৩য় বর্ষ হিসাববিজ্ঞান বিভাগের পরীক্ষার্থীদের চূড়ান্ত প্রস্তুতি ও অফলাইন রিভিশনের সুবিধার্থে <strong>উন্নত হিসাববিজ্ঞান ১ (Advanced Accounting-I, বিষয় কোড: ২৩২৫০৩)</strong>-এর {year_bn} সালের ক, খ ও গ বিভাগের মোট ২৮টি প্রশ্ন এবং বিশ্ববিদ্যালয় অ্যাকাডেমিক কাউন্সিলের মূল্যায়ন নির্দেশিকা অনুযায়ী রচিত শতভাগ নির্ভুল প্রামাণ্য সমাধানের অফিসিয়াল মাস্টার পিডিএফ হ্যান্ডনোট নিচে সংযুক্ত করা হলো। আপনার সুবিধার্থে ৩০ সেকেন্ডের কাউন্টডাউন টাইমার ব্যবহার করে প্রামাণ্য ই-বুকটি সংগ্রহ করতে পারবেন:",
        mode="timer",
        unique_id=year_en,
        include_script=False
    )

    faq_items = [
        {
            "q": f"জাতীয় বিশ্ববিদ্যালয় অনার্স ৩য় বর্ষ {year_bn} সালের পরীক্ষায় ক-বিভাগে কয়টি প্রশ্ন এসেছিল?",
            "a": f"জাতীয় বিশ্ববিদ্যালয় {year_bn} সালের লিখিত পরীক্ষায় ক-বিভাগে মোট ১২টি অতি সংক্ষিপ্ত প্রশ্ন এসেছিল, যার মধ্যে যেকোনো ১০টি প্রশ্নের উত্তর দিতে হয়েছিল। এখানে ১২টি প্রশ্নেরই নির্ভুল প্রামাণ্য উত্তর দেওয়া হয়েছে।"
        },
        {
            "q": f"উন্নত হিসাববিজ্ঞান ১ {year_bn} সালের গাণিতিক সমস্যাগুলোর গণনাকার্য (Working Notes) কি রয়েছে?",
            "a": "হ্যাঁ, HelpTrickBD-এর এই ডেডিকেটেড প্রশ্নব্যাংকে প্রতিটি গাণিতিক সমস্যার জন্য প্রয়োজনীয় জাবেদা, ছক ও খসড়া গণনাকার্য (Working Notes) প্রতিটি ধাপ অনুযায়ী পৃথকভাবে প্রদান করা হয়েছে।"
        },
        {
            "q": f"প্রশ্নব্যাংক {year_bn}: উন্নত হিসাববিজ্ঞান ১-এর অফিশিয়াল PDF ফাইল কীভাবে ফ্রিতে ডাউনলোড করব?",
            "a": f"পোস্টে দেওয়া '[ডাউনলোড] {year_bn} সালের বোর্ড সমাধান PDF সংগ্রহ করুন' বাটনে ক্লিক করলেই সম্পূর্ণ সল্যুশন PDF ফাইল সরাসরি গুগল ড্রাইভ / মিডিয়া সার্ভার থেকে বিনামূল্যে ডাউনলোড করা যাবে।"
        }
    ]

    faq_html_items = []
    faq_schema_items = []
    for idx, item in enumerate(faq_items, 1):
        q = item['q']
        a = item['a']
        faq_html_items.append(f"""<div class="htbd-faq-item">
  <h4 class="htbd-faq-q">{idx}. {q}</h4>
  <p class="htbd-faq-a">{a}</p>
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
        "description": f"{focus_kw} (Advanced Accounting 1 Solution {year_en}): জাতীয় বিশ্ববিদ্যালয় BBA ৩য় বর্ষের {year_bn} সালের ২৮টি বোর্ড প্রশ্ন ও সমাধান।",
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
            "@id": post_url
        }
    }, ensure_ascii=False, indent=2)

    full_html = f"""<!-- Byte-0 Hero Banner Placement -->
<figure class="htbd-featured-hero" style="margin: 0 0 25px 0; text-align: center;">
  <img src="{banner_url}" alt="{focus_kw} (Advanced Accounting 1 Solution {year_en})" title="{seo_title}" style="width: 100%; max-width: 1000px; height: auto; border-radius: 12px; box-shadow: 0 5px 20px rgba(0,0,0,0.12); display: block; margin: 0 auto;" loading="eager" width="1200" height="675" />
  <figcaption style="font-family: 'SolaimanLipi', sans-serif; font-size: 14px; color: #64748b; margin-top: 8px; text-align: center;">
    জাতীয় বিশ্ববিদ্যালয় BBA অনার্স ৩য় বর্ষ {focus_kw} (Advanced Accounting 1 Solution {year_en}) | প্রকাশনা: HelpTrickBD
  </figcaption>
</figure>

{get_shared_css()}

<div class="htbd-nu-content">

  <!-- Breadcrumb & Topic Metadata -->
  <div style="font-size: 13.5px; color: #64748b; margin-bottom: 20px;">
    হোম / শিক্ষা ও সাজেশন / অনার্স ৩য় বর্ষ / <strong>{focus_kw}</strong> (কোর্স কোড: ২৩২৫০৩)
  </div>

  <!-- Position 0 Quick Answer Box -->
  <div class="htbd-hero-box">
    <h3 style="margin-top: 0; color: #065f46; font-size: 19px;">[বোর্ড ওভারভিউ] একনজরে {focus_kw}</h3>
    <p><strong>{focus_kw}</strong> (Advanced Accounting 1 Solution {year_en}) খুঁজছেন এমন জাতীয় বিশ্ববিদ্যালয়ের BBA অনার্স ৩য় বর্ষের হিসাববিজ্ঞান বিভাগের শিক্ষার্থীদের জন্য এটি একটি নির্ভরযোগ্য ও প্রামাণ্য ডিজিটাল সমাধান ভাণ্ডার। জাতীয় বিশ্ববিদ্যালয়ের {year_bn} সালের চূড়ান্ত পরীক্ষায় আসা ক, খ ও গ বিভাগের মোট <strong>{total_q}টি বোর্ড প্রশ্ন ও নির্ভুল গাণিতিক সমাধান</strong> এখানে প্রতিটি বিষয়ের সঠিক ওয়ার্কিং নোটসসহ সন্নিবেশিত হয়েছে।</p>
    <p>পোস্টটিতে ক-বিভাগের <strong>১২টি অতি সংক্ষিপ্ত প্রশ্ন</strong>, খ-বিভাগের <strong>৮টি সংক্ষিপ্ত ও গাণিতিক সমস্যা</strong> এবং গ-বিভাগের <strong>৮টি বিশ্লেষণধর্মী ও বড় অংকের</strong> পুঙ্খানুপুঙ্খ সমাধান রয়েছে। প্রতিটি প্রশ্নের নিচে [উত্তর / সমাধান দেখুন] বাটনে ক্লিক করে সমাধান দেখা যাবে।</p>
  </div>

  <!-- Mandatory Jump Break for Archive Summary -->
  <!--more-->

  <p>জাতীয় বিশ্ববিদ্যালয়ের BBA অনার্স ৩য় বর্ষ হিসাববিজ্ঞান বিভাগের শিক্ষার্থীদের জন্য সবচেয়ে বেশি গাণিতিক চ্যালেঞ্জপূর্ণ ও সর্বোচ্চ নম্বর নির্ধারক ব্যবহারিক বিষয় হলো <strong>উন্নত হিসাববিজ্ঞান-১ (Advanced Accounting-I - Course Code: 232503)</strong>। পরীক্ষায় এ-প্লাস (A+) নিশ্চিত করতে পূর্ববর্তী বছরগুলোর প্রশ্ন প্যাটার্ন ও জাতীয় বিশ্ববিদ্যালয়ের বোর্ড প্রশ্ন সমাধান আয়ত্ত করার কোনো বিকল্প নেই। অনার্স ৩য় বর্ষের সম্পূর্ণ অধ্যায়ভিত্তিক সাজেশনের জন্য পড়ুন আমাদের <a href="{URL_SUGGESTION_POST}">অনার্স ৩য় বর্ষ উন্নত হিসাববিজ্ঞান ১ সাজেশন 2026</a> এবং বিগত ৬ বছরের সমন্বিত তালিকার জন্য দেখুন <a href="{URL_BOARD_HUB}">উন্নত হিসাববিজ্ঞান ১ বোর্ড প্রশ্নব্যাংক (২০১৯-২০২৪)</a>।</p>
  <p>শিক্ষার্থীদের {year_bn} সালের পরীক্ষার প্রস্তুতিকে সহজ ও ত্রুটিমুক্ত করতে HelpTrickBD প্রস্তুত করেছে দেশের সর্বাধিক মানসম্মত <strong>{focus_kw} (Advanced Accounting 1 Solution {year_en})</strong>। এখানে {year_bn} সালের পরীক্ষার ক, খ ও গ বিভাগের প্রতিটি প্রশ্নের পুঙ্খানুপুঙ্খ সমাধান ও গণনাকার্য ধাপে ধাপে উপস্থাপন করা হলো।</p>

  {nav_html}

  <div id="rank-math-toc" class="htbd-toc-container">
    <div class="htbd-toc-title">সূচিপত্র: {year_bn} সালের প্রশ্ন ও সমাধান</div>
    <ol class="htbd-toc-list">
      <li><a href="#section-a">ক-বিভাগ: অতি সংক্ষিপ্ত প্রশ্ন ও উত্তর (১২টি প্রশ্ন)</a></li>
      <li><a href="#section-b">খ-বিভাগ: সংক্ষিপ্ত প্রশ্ন ও গাণিতিক সমাধান (৮টি প্রশ্ন)</a></li>
      <li><a href="#section-c">গ-বিভাগ: রচনামূলক প্রশ্ন ও ব্যবহারিক গাণিতিক বিশ্লেষণ (৮টি প্রশ্ন)</a></li>
      <li><a href="#exam-marks-pattern">জাতীয় বিশ্ববিদ্যালয় {year_bn} সালের পরীক্ষার প্রশ্ন প্যাটার্ন ও মানবণ্টন</a></li>
      <li><a href="#year-exam-strategy">পরীক্ষার চূড়ান্ত প্রস্তুতি ও রিভিশন টিপস</a></li>
      <li><a href="#faq-section">সচরাচর জিজ্ঞাসিত প্রশ্নোত্তর (FAQ)</a></li>
    </ol>
  </div>

  <div id="section-a">
    <h2>ক-বিভাগ: অতি সংক্ষিপ্ত প্রশ্নাবলি ও সমাধান (সাল {year_bn})</h2>
    <p style="color: #475569; font-weight: 500;">জাতীয় বিশ্ববিদ্যালয় {year_bn} সালের পরীক্ষার ক-বিভাগের ১২টি প্রশ্ন নিচে নির্ভুলভাবে সমাধান করা হলো (যেকোনো ১০টি প্রশ্নের উত্তর আবশ্যক, পূর্ণমান ১০):</p>
    {''.join(sec_a_html)}
  </div>

  <div id="section-b">
    <h2>খ-বিভাগ: সংক্ষিপ্ত প্রশ্ন ও গাণিতিক সমস্যাবলি (সাল {year_bn})</h2>
    <p style="color: #475569; font-weight: 500;">জাতীয় বিশ্ববিদ্যালয় {year_bn} সালের পরীক্ষার খ-বিভাগের ৮টি সংক্ষিপ্ত প্রশ্ন ও গাণিতিক সমস্যার পুঙ্খানুপুঙ্খ সমাধান (যেকোনো ৫টি প্রশ্নের উত্তর আবশ্যক, পূর্ণমান ২০):</p>
    {''.join(sec_b_html)}
  </div>

  <div id="section-c">
    <h2>গ-বিভাগ: রচনামূলক প্রশ্ন ও ব্যবহারিক গাণিতিক বিশ্লেষণ (সাল {year_bn})</h2>
    <p style="color: #475569; font-weight: 500;">জাতীয় বিশ্ববিদ্যালয় {year_bn} সালের পরীক্ষার গ-বিভাগের ৮টি বড় গাণিতিক সমস্যার পূর্ণাঙ্গ ওয়ার্কিং নোটস ও বিবরণী (যেকোনো ৫টি প্রশ্নের উত্তর আবশ্যক, পূর্ণমান ৫০):</p>
    {''.join(sec_c_html)}
  </div>

  <div id="exam-marks-pattern">
    <h2>জাতীয় বিশ্ববিদ্যালয় {year_bn} সালের পরীক্ষার প্রশ্ন প্যাটার্ন ও মানবণ্টন</h2>
    <p>জাতীয় বিশ্ববিদ্যালয়ের লিখিত পরীক্ষায় মোট ৮০ নম্বরের প্রশ্নপত্র থাকে। {year_bn} শিক্ষাবর্ষের লিখিত পরীক্ষার মানবণ্টন নিম্নরূপ:</p>
    <div class="htbd-table-wrapper">
      <table class="htbd-styled-table">
        <thead>
          <tr>
            <th>পরীক্ষার বিভাগ</th>
            <th>মোট প্রশ্নের সংখ্যা</th>
            <th>উত্তর দিতে হয়</th>
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
  </div>

  <div id="year-exam-strategy">
    <h2>পরীক্ষার চূড়ান্ত প্রস্তুতি ও রিভিশন টিপস ({year_bn} সালের আলোকেই)</h2>
    <p>{year_bn} সালের বোর্ড প্রশ্ন গভীরভাবে বিশ্লেষণ করলে দেখা যায় যে, স্টকহোল্ডার্স ইকুইটি, ইজারা হিসাববিজ্ঞান এবং কোম্পানির আর্থিক বিবরণী প্রস্তুতের অংকগুলোতে ওয়ার্কিং নোটস নির্ভুল রাখা সর্বোচ্চ নম্বর নিশ্চিত করে। নিয়মিত প্রশ্নব্যাংক অনুশীলনের মাধ্যমে সময়ের অপচয় রোধ করা সম্ভব হয়।</p>
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
      box.innerHTML = '<span style="color: #065f46; font-size: 15.5px;">[প্রস্তুত] আপনার হাই-স্পিড ডাউনলোড লিংক সক্রিয় হয়েছে!</span> <a href="' + url + '" target="_blank" rel="noopener noreferrer" download style="display: inline-block; margin-left: 12px; background: #059669; color: #ffffff !important; padding: 7px 18px; border-radius: 6px; text-decoration: none; font-size: 14.5px; font-weight: 700;">এখনই PDF ডাউনলোড করুন</a>';
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
    return full_html, {
        "title": seo_title,
        "seo_title": seo_title,
        "focus_keyword": focus_kw,
        "rank_math_focus_keyword": f"{focus_kw}, Advanced Accounting 1 Solution {year_en}, অনার্স ৩য় বর্ষ হিসাববিজ্ঞান {year_bn}, জাতীয় বিশ্ববিদ্যালয় প্রশ্নব্যাংক",
        "custom_url": slug,
        "url": post_url,
        "search_description": f"{focus_kw} (Advanced Accounting 1): জাতীয় বিশ্ববিদ্যালয় BBA ৩য় বর্ষের {year_bn} সালের ২৮টি বোর্ড প্রশ্ন ও সমাধান।",
        "meta_description": f"{focus_kw} (Advanced Accounting 1): জাতীয় বিশ্ববিদ্যালয় BBA ৩য় বর্ষের {year_bn} সালের ২৮টি বোর্ড প্রশ্ন ও সমাধান।",
        "banner_url": banner_url,
        "banner_alt": f"{focus_kw} (Advanced Accounting 1 Solution {year_en})",
        "featured_media_id": media_info['media_id']
    }

def build_all_individual_years():
    with open(os.path.join(PROJECT_ROOT, "scratch", "adv1_year_media.json"), "r", encoding="utf-8") as f:
        media_data = json.load(f)
        
    compiled_posts = {}
    for yr in YEARS:
        media_info = media_data[yr]
        html_content, meta_dict = generate_individual_year_post(yr, media_info)
        
        html_path = os.path.join(PROJECT_ROOT, "scratch", f"adv1_board_{yr}.html")
        meta_path = os.path.join(PROJECT_ROOT, "scratch", f"adv1_board_{yr}_meta.json")
        
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(meta_dict, f, ensure_ascii=False, indent=2)
            
        print(f"[SUCCESS] Year {yr}: HTML written to {html_path} ({len(html_content)} chars)")
        compiled_posts[yr] = {
            "html_path": html_path,
            "meta_path": meta_path,
            "meta": meta_dict
        }
    return compiled_posts

if __name__ == "__main__":
    build_all_individual_years()
