#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/image_generator/build_department_routine_cards.py
-------------------------------------------------------
Generates authentic, zero-AI-tone Facebook post size (1080x1350 px, 4:5 vertical)
examination routine cards for all major departments of National University
Honours 2nd Year Examination 2026:

Covered Departments across 4 Faculties:
1. Business Studies: Management, Accounting, Marketing, Finance & Banking
2. Social Science: Political Science, Sociology, Social Work, Economics
3. Arts: Bangla, English, Islamic History & Culture, History, Philosophy
4. Science: Mathematics, Physics, Chemistry, Zoology, Botany

Features:
- Pure official university examination terminology.
- Clean columns: তারিখ ও বার | পরীক্ষার সময় | বিষয় কোড | পত্রের শিরোনাম / নাম.
- Authentic exam hall rules (Admit card, No mobile phone, 30 min before).
- Small official HelpTrickBD logo and website.
- 1080x1350 px compressed to high-efficiency WebP (20-35 KB).
- Strictly ZERO EMOJIS!
"""

import os
import sys
import subprocess
from PIL import Image

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.image_optimizer.webp_compressor import compress_to_target_webp
from tools.image_generator.build_official_bg_thumbnails import get_browser_binary

OUTPUT_DIR = os.path.join(PROJECT_ROOT, "assets", "images", "posts")
ARTIFACT_DIR = r"C:\Users\omarf\.gemini\antigravity-ide\brain\1919afd7-77e9-4a5a-aeb3-60abfe06a7b9"
FONT_PATH = os.path.join(PROJECT_ROOT, "assets", "fonts", "HindSiliguri-Bold.ttf")
LOGO_PATH = os.path.join(PROJECT_ROOT, "assets", "images", "logo", "helptrickbd_logo.png")

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(ARTIFACT_DIR, exist_ok=True)

# Common dates
D1 = "২৮/০৯/২০২৬ (সোমবার)"
D2 = "০১/১০/২০২৬ (বৃহস্পতিবার)"
D3 = "০৭/১০/২০২৬ (বুধবার)"
D4 = "১২/১০/২০২৬ (সোমবার)"
D5 = "১৯/১০/২০২৬ (সোমবার)"
D6 = "২৬/১০/২০২৬ (সোমবার)"
TIME = "দুপুর ০১:০০ টা"

DEPARTMENTS = [
    # --- Business Studies Faculty ---
    {
        "slug": "management",
        "dept_name": "ব্যবস্থাপনা বিভাগ (Department of Management)",
        "faculty": "ব্যবসায় শিক্ষা অনুষদ",
        "primary_color": "#0f172a",
        "accent_color": "#0284c7",
        "badge_bg": "#0284c7",
        "papers": [
            (D1, TIME, "221109", "English (Compulsory) — Non-Credit"),
            (D2, TIME, "222601", "Human Resource Management"),
            (D3, TIME, "222603", "Business Communication (In English)"),
            (D4, TIME, "222605", "Business Mathematics"),
            (D5, TIME, "222607", "Principles of Finance"),
            (D6, TIME, "222609", "Legal Aspects of Business"),
        ]
    },
    {
        "slug": "accounting",
        "dept_name": "হিসাববিজ্ঞান বিভাগ (Department of Accounting)",
        "faculty": "ব্যবসায় শিক্ষা অনুষদ",
        "primary_color": "#064e3b",
        "accent_color": "#059669",
        "badge_bg": "#059669",
        "papers": [
            (D1, TIME, "221109", "English (Compulsory) — Non-Credit"),
            (D2, TIME, "222501", "Advanced Accounting-I"),
            (D3, TIME, "222503", "Business Communication and Report Writing"),
            (D4, TIME, "222505", "Business Mathematics"),
            (D5, TIME, "222507", "Taxation in Bangladesh"),
            (D6, TIME, "222509", "Principles of Finance"),
        ]
    },
    {
        "slug": "marketing",
        "dept_name": "মার্কেটিং বিভাগ (Department of Marketing)",
        "faculty": "ব্যবসায় শিক্ষা অনুষদ",
        "primary_color": "#831843",
        "accent_color": "#db2777",
        "badge_bg": "#db2777",
        "papers": [
            (D1, TIME, "221109", "English (Compulsory) — Non-Credit"),
            (D2, TIME, "222301", "Consumer Behavior"),
            (D3, TIME, "222303", "Principles of Finance"),
            (D4, TIME, "222305", "Business Communication (In English)"),
            (D5, TIME, "222307", "Business Statistics"),
            (D6, TIME, "222309", "Macro Economics"),
        ]
    },
    {
        "slug": "finance",
        "dept_name": "ফিন্যান্স ও ব্যাংকিং বিভাগ (Dept. of Finance & Banking)",
        "faculty": "ব্যবসায় শিক্ষা অনুষদ",
        "primary_color": "#1e3a8a",
        "accent_color": "#3b82f6",
        "badge_bg": "#2563eb",
        "papers": [
            (D1, TIME, "221109", "English (Compulsory) — Non-Credit"),
            (D2, TIME, "222401", "Commercial Banking"),
            (D3, TIME, "222403", "Financial Management"),
            (D4, TIME, "222405", "Business Communication"),
            (D5, TIME, "222407", "Business Mathematics"),
            (D6, TIME, "222409", "Auditing"),
        ]
    },

    # --- Social Science Faculty ---
    {
        "slug": "political_science",
        "dept_name": "রাষ্ট্রবিজ্ঞান বিভাগ (Department of Political Science)",
        "faculty": "সামাজিক বিজ্ঞান অনুষদ",
        "primary_color": "#1e3a8a",
        "accent_color": "#2563eb",
        "badge_bg": "#1d4ed8",
        "papers": [
            (D1, TIME, "221109", "English (Compulsory) — Non-Credit"),
            (D2, TIME, "221901", "Political and Constitutional Development in British India"),
            (D3, TIME, "221903", "Political Sociology"),
            (D4, TIME, "221905", "Government and Politics in East Asia (China & Japan)"),
            (D5, TIME, "221907", "Government and Politics in South Asia"),
        ]
    },
    {
        "slug": "sociology",
        "dept_name": "সমাজবিজ্ঞান বিভাগ (Department of Sociology)",
        "faculty": "সামাজিক বিজ্ঞান অনুষদ",
        "primary_color": "#312e81",
        "accent_color": "#6366f1",
        "badge_bg": "#4f46e5",
        "papers": [
            (D1, TIME, "221109", "English (Compulsory) — Non-Credit"),
            (D2, TIME, "222001", "Classical Sociological Theory"),
            (D3, TIME, "222003", "Social Structure of Bangladesh"),
            (D4, TIME, "222005", "Bangladesh Society and Culture"),
            (D5, TIME, "222007", "Social Psychology"),
        ]
    },
    {
        "slug": "social_work",
        "dept_name": "সমাজকর্ম বিভাগ (Department of Social Work)",
        "faculty": "সামাজিক বিজ্ঞান অনুষদ",
        "primary_color": "#134e4a",
        "accent_color": "#0d9488",
        "badge_bg": "#0f766e",
        "papers": [
            (D1, TIME, "221109", "English (Compulsory) — Non-Credit"),
            (D2, TIME, "222101", "Human Rights and Social Justice"),
            (D3, TIME, "222103", "Social Problems of Bangladesh"),
            (D4, TIME, "222105", "Social Policy and Planning"),
            (D5, TIME, "222107", "Social Research and Statistics"),
        ]
    },
    {
        "slug": "economics",
        "dept_name": "অর্থনীতি বিভাগ (Department of Economics)",
        "faculty": "সামাজিক বিজ্ঞান অনুষদ",
        "primary_color": "#701a75",
        "accent_color": "#c026d3",
        "badge_bg": "#a21caf",
        "papers": [
            (D1, TIME, "221109", "English (Compulsory) — Non-Credit"),
            (D2, TIME, "222201", "Intermediate Microeconomics"),
            (D3, TIME, "222203", "Mathematical Economics"),
            (D4, TIME, "222205", "Basic Econometrics"),
            (D5, TIME, "222207", "Agricultural Economics"),
        ]
    },

    # --- Arts Faculty ---
    {
        "slug": "bangla",
        "dept_name": "বাংলা বিভাগ (Department of Bangla)",
        "faculty": "কলা অনুষদ",
        "primary_color": "#7c2d12",
        "accent_color": "#ea580c",
        "badge_bg": "#c2410c",
        "papers": [
            (D1, TIME, "221109", "ইংরেজি (আবশ্যিক) — নন ক্রেডিট"),
            (D2, TIME, "221001", "বাংলা সাহিত্যের ইতিহাস-১ (প্রাচীন ও মধ্যযুগ)"),
            (D3, TIME, "221003", "মধ্যযুগের কবিতা (শ্রীকৃষ্ণকীর্তন ও মঙ্গলকাব্য)"),
            (D4, TIME, "221005", "বাংলা কবিতা-২ (আধুনিক যুগ)"),
            (D5, TIME, "221007", "বাংলা নাটক-১ (প্রারম্ভিক ও আধুনিক নাটক)"),
        ]
    },
    {
        "slug": "english",
        "dept_name": "ইংরেজি বিভাগ (Department of English)",
        "faculty": "কলা অনুষদ",
        "primary_color": "#1e293b",
        "accent_color": "#475569",
        "badge_bg": "#334155",
        "papers": [
            (D1, TIME, "221109", "English (Compulsory) — Non-Credit"),
            (D2, TIME, "221101", "Introduction to Drama"),
            (D3, TIME, "221103", "Romantic Poetry"),
            (D4, TIME, "221105", "Advanced Reading and Writing"),
            (D5, TIME, "221107", "History of English Literature"),
        ]
    },
    {
        "slug": "islamic_history",
        "dept_name": "ইসলামের ইতিহাস ও সংস্কৃতি বিভাগ (Dept. of Islamic History)",
        "faculty": "কলা অনুষদ",
        "primary_color": "#064e3b",
        "accent_color": "#047857",
        "badge_bg": "#059669",
        "papers": [
            (D1, TIME, "221109", "ইংরেজি (আবশ্যিক) — নন ক্রেডিট"),
            (D2, TIME, "221601", "আব্বাসীয় খিলাফত (৭৫০-১২৫৮ খ্রি.)"),
            (D3, TIME, "221603", "ভারতে মুসলিম শাসন (১২০৬-১৫২৬ খ্রি.)"),
            (D4, TIME, "221605", "মুসলিম দর্শন ও সংস্কৃতির ইতিহাস"),
            (D5, TIME, "221607", "আধুনিক মধ্যপ্রাচ্যের ইতিহাস"),
        ]
    },
    {
        "slug": "history",
        "dept_name": "ইতিহাস বিভাগ (Department of History)",
        "faculty": "কলা অনুষদ",
        "primary_color": "#831843",
        "accent_color": "#be185d",
        "badge_bg": "#9d174d",
        "papers": [
            (D1, TIME, "221109", "ইংরেজি (আবশ্যিক) — নন ক্রেডিট"),
            (D2, TIME, "221501", "প্রাচীন বাংলার ইতিহাস (১২০৪ খ্রি. পর্যন্ত)"),
            (D3, TIME, "221503", "দিল্লির সালতানাতের ইতিহাস"),
            (D4, TIME, "221505", "মধ্যযুগীয় ইউরোপের ইতিহাস"),
            (D5, TIME, "221507", "আমেরিকার ইতিহাস"),
        ]
    },
    {
        "slug": "philosophy",
        "dept_name": "দর্শন বিভাগ (Department of Philosophy)",
        "faculty": "কলা অনুষদ",
        "primary_color": "#4c1d95",
        "accent_color": "#7c3aed",
        "badge_bg": "#6d28d9",
        "papers": [
            (D1, TIME, "221109", "ইংরেজি (আবশ্যিক) — নন ক্রেডিট"),
            (D2, TIME, "221701", "সাধারণ নীতিবিদ্যা (General Ethics)"),
            (D3, TIME, "221703", "মুসলিম দর্শন (Muslim Philosophy)"),
            (D4, TIME, "221705", "ভারতীয় দর্শন (Indian Philosophy)"),
            (D5, TIME, "221707", "আধুনিক ইউরোপীয় দর্শন"),
        ]
    },

    # --- Science Faculty ---
    {
        "slug": "mathematics",
        "dept_name": "গণিত বিভাগ (Department of Mathematics)",
        "faculty": "বিজ্ঞান অনুষদ",
        "primary_color": "#0e7490",
        "accent_color": "#0891b2",
        "badge_bg": "#0284c7",
        "papers": [
            (D1, TIME, "221109", "English (Compulsory) — Non-Credit"),
            (D2, TIME, "223701", "Calculus-II"),
            (D3, TIME, "223703", "Ordinary Differential Equations"),
            (D4, TIME, "223705", "Fortran Programming"),
            (D5, TIME, "223707", "Linear Algebra"),
        ]
    },
    {
        "slug": "physics",
        "dept_name": "পদার্থবিজ্ঞান বিভাগ (Department of Physics)",
        "faculty": "বিজ্ঞান অনুষদ",
        "primary_color": "#1e3a8a",
        "accent_color": "#0284c7",
        "badge_bg": "#0369a1",
        "papers": [
            (D1, TIME, "221109", "English (Compulsory) — Non-Credit"),
            (D2, TIME, "222701", "Electricity and Magnetism"),
            (D3, TIME, "222703", "Thermal Physics"),
            (D4, TIME, "222705", "Optics"),
            (D5, TIME, "222707", "Mathematical Physics"),
        ]
    },
    {
        "slug": "chemistry",
        "dept_name": "রসায়ন বিভাগ (Department of Chemistry)",
        "faculty": "বিজ্ঞান অনুষদ",
        "primary_color": "#065f46",
        "accent_color": "#10b981",
        "badge_bg": "#047857",
        "papers": [
            (D1, TIME, "221109", "English (Compulsory) — Non-Credit"),
            (D2, TIME, "222801", "Physical Chemistry-II"),
            (D3, TIME, "222803", "Organic Chemistry-II"),
            (D4, TIME, "222805", "Inorganic Chemistry-II"),
            (D5, TIME, "222807", "Environmental Chemistry"),
        ]
    },
    {
        "slug": "zoology",
        "dept_name": "প্রাণিবিজ্ঞান বিভাগ (Department of Zoology)",
        "faculty": "বিজ্ঞান অনুষদ",
        "primary_color": "#14532d",
        "accent_color": "#16a34a",
        "badge_bg": "#15803d",
        "papers": [
            (D1, TIME, "221109", "English (Compulsory) — Non-Credit"),
            (D2, TIME, "223101", "Animal Diversity-II (Chordata)"),
            (D3, TIME, "223103", "Comparative Anatomy of Vertebrates"),
            (D4, TIME, "223105", "Environmental Biology"),
            (D5, TIME, "223107", "Genetics and Molecular Biology"),
        ]
    },
    {
        "slug": "botany",
        "dept_name": "উদ্ভিদবিজ্ঞান বিভাগ (Department of Botany)",
        "faculty": "বিজ্ঞান অনুষদ",
        "primary_color": "#166534",
        "accent_color": "#22c55e",
        "badge_bg": "#16a34a",
        "papers": [
            (D1, TIME, "221109", "English (Compulsory) — Non-Credit"),
            (D2, TIME, "223001", "Pteridophyta and Gymnosperms"),
            (D3, TIME, "223003", "Plant Anatomy and Embryology"),
            (D4, TIME, "223005", "Plant Ecology and Phytogeography"),
            (D5, TIME, "223007", "Plant Pathology and Protection"),
        ]
    },
]


def generate_dept_card_html(dept):
    table_rows = []
    for day, tm, code, paper in dept["papers"]:
        row_html = f"""        <tr>
          <td class="td-day">{day}</td>
          <td class="td-time">{tm}</td>
          <td class="td-code">{code}</td>
          <td class="td-paper">{paper}</td>
        </tr>"""
        table_rows.append(row_html)
    
    rows_str = "\n".join(table_rows)

    html = f"""<!DOCTYPE html>
<html lang="bn">
<head>
<meta charset="utf-8" />
<style>
@font-face {{
  font-family: 'HindSiliguri';
  src: url('file:///{FONT_PATH.replace("\\", "/")}');
  font-weight: 700;
}}
* {{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}}
body {{
  width: 1080px;
  height: 1350px;
  overflow: hidden;
  background: #f1f5f9;
  font-family: 'HindSiliguri', Arial, sans-serif;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}}
.card-wrapper {{
  width: 1032px;
  height: 1302px;
  background: #ffffff;
  border-radius: 14px;
  border: 4px solid #0f172a;
  box-shadow: 0 10px 30px rgba(0,0,0,0.08);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 34px 38px 24px 38px;
}}

/* Official Header */
.top-header {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 3px solid #0f172a;
  padding-bottom: 18px;
}}
.inst-meta {{
  display: flex;
  flex-direction: column;
}}
.inst-main-title {{
  font-size: 32px;
  font-weight: 800;
  color: #0f172a;
  line-height: 1.15;
}}
.inst-sub-title {{
  font-size: 21px;
  font-weight: 700;
  color: #1e3a8a;
  margin-top: 5px;
}}
.exam-session {{
  font-size: 16px;
  color: #475569;
  font-weight: 600;
  margin-top: 4px;
}}

.brand-section {{
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 3px;
}}
.brand-logo-img {{
  height: 48px;
  width: auto;
  object-fit: contain;
}}
.brand-url-text {{
  font-size: 14px;
  color: #64748b;
  font-weight: 700;
  font-family: Arial, sans-serif;
}}

/* Department Banner Strip */
.dept-banner-strip {{
  background: {dept['primary_color']};
  color: #ffffff;
  padding: 14px 22px;
  border-radius: 8px;
  margin: 20px 0 22px 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}}
.dept-title-text {{
  font-size: 26px;
  font-weight: 800;
}}
.faculty-badge {{
  background: {dept['badge_bg']};
  color: #ffffff;
  padding: 5px 16px;
  border-radius: 6px;
  font-size: 16px;
  font-weight: 700;
}}

/* Table */
.table-container {{
  width: 100%;
  border-radius: 8px;
  overflow: hidden;
  border: 2px solid #cbd5e1;
}}
table {{
  width: 100%;
  border-collapse: collapse;
  text-align: left;
}}
thead tr {{
  background: #1e293b;
  color: #ffffff;
}}
th {{
  padding: 13px 14px;
  font-size: 17px;
  font-weight: 700;
  border-bottom: 2px solid #0f172a;
}}
tbody tr {{
  border-bottom: 1.5px solid #e2e8f0;
}}
tbody tr:nth-child(even) {{
  background: #f8fafc;
}}
tbody tr:hover {{
  background: #f1f5f9;
}}
td {{
  padding: 12px 14px;
  vertical-align: middle;
}}
.td-day {{
  font-weight: 700;
  color: #0f172a;
  font-size: 16.5px;
}}
.td-time {{
  color: #334155;
  font-size: 16px;
  font-weight: 600;
}}
.td-code {{
  font-family: Arial, sans-serif;
  font-weight: 800;
  color: #1e40af;
  font-size: 19px;
  letter-spacing: 0.5px;
}}
.td-paper {{
  font-weight: 700;
  color: #0f172a;
  font-size: 18px;
  line-height: 1.35;
}}

/* Authentic Examination Rules Box */
.instructions-box {{
  background: #f8fafc;
  border: 1.5px solid #cbd5e1;
  border-left: 6px solid #0f172a;
  padding: 16px 20px;
  border-radius: 8px;
  margin: 18px 0 14px 0;
}}
.inst-head {{
  font-size: 17px;
  font-weight: 800;
  color: #0f172a;
  margin-bottom: 8px;
}}
.inst-list {{
  margin: 0;
  padding-left: 22px;
  color: #334155;
  font-size: 15px;
  line-height: 1.6;
  font-weight: 600;
}}

/* Footer */
.card-bottom-footer {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-top: 2px solid #e2e8f0;
  padding-top: 12px;
  font-size: 14.5px;
  color: #64748b;
  font-weight: 600;
}}
.authority-text {{
  font-weight: 700;
  color: #0f172a;
}}
</style>
</head>
<body>

<div class="card-wrapper">

  <!-- Top Official Header -->
  <div class="top-header">
    <div class="inst-meta">
      <div class="inst-main-title">জাতীয় বিশ্ববিদ্যালয়, বাংলাদেশ</div>
      <div class="inst-sub-title">অনার্স ২য় বর্ষ চূড়ান্ত পরীক্ষা ২০২৬ • বিষয়ভিত্তিক সময়সূচি</div>
      <div class="exam-session">শিক্ষাবর্ষ: ২০২২-২৩ (নিয়মিত), ২০২১-২২ ও ২০২০-২১ (অনিয়মিত ও মানোন্নয়ন)</div>
    </div>
    <div class="brand-section">
      <img src="file:///{LOGO_PATH.replace("\\", "/")}" class="brand-logo-img" alt="HelpTrickBD" />
      <div class="brand-url-text">helptrickbd.com</div>
    </div>
  </div>

  <!-- Department Banner Strip -->
  <div class="dept-banner-strip">
    <div class="dept-title-text">{dept['dept_name']}</div>
    <div class="faculty-badge">{dept['faculty']}</div>
  </div>

  <!-- Routine Table -->
  <div class="table-container">
    <table>
      <thead>
        <tr>
          <th style="width: 24%;">তারিখ ও বার</th>
          <th style="width: 18%;">পরীক্ষার সময়</th>
          <th style="width: 16%;">বিষয় কোড</th>
          <th style="width: 42%;">পত্রের শিরোনাম / নাম</th>
        </tr>
      </thead>
      <tbody>
{rows_str}
      </tbody>
    </table>
  </div>

  <!-- Official Examination Rules Box -->
  <div class="instructions-box">
    <div class="inst-head">পরীক্ষার্থীদের জন্য সাধারণ নির্দেশনাবলী:</div>
    <ul class="inst-list">
      <li>প্রশ্নপত্রে উল্লেখিত সময় ও পূর্ণমান অনুযায়ী পরীক্ষা অনুষ্ঠিত হবে।</li>
      <li>পরীক্ষার্থীকে অবশ্যই প্রবেশপত্র ও মূল রেজিস্ট্রেশন কার্ড সাথে আনতে হবে।</li>
      <li>পরীক্ষা শুরুর ৩০ মিনিট পূর্বে কেন্দ্রে প্রবেশ করে নির্ধারিত আসন গ্রহণ করতে হবে।</li>
      <li>পরীক্ষা কক্ষে মোবাইল ফোন বা যেকোনো প্রকার ইলেকট্রনিক ডিভাইস বহন সম্পূর্ণ নিষিদ্ধ।</li>
    </ul>
  </div>

  <!-- Card Bottom Footer -->
  <div class="card-bottom-footer">
    <div class="authority-text">পরীক্ষা নিয়ন্ত্রণ দপ্তর, জাতীয় বিশ্ববিদ্যালয়, গাজীপুর</div>
    <div>অফিসিয়াল সোর্স: nu.ac.bd</div>
    <div>সৌজন্যে: HelpTrickBD.com</div>
  </div>

</div>

</body>
</html>"""
    return html


def build_all_department_cards():
    browser_bin = get_browser_binary()
    if not browser_bin:
        print("[ERROR] Chrome or Edge browser binary not found!")
        return False

    temp_html = os.path.join(OUTPUT_DIR, "temp_dept_render.html")
    temp_png = os.path.join(OUTPUT_DIR, "temp_dept_render.png")

    print(f"[*] Starting generation for {len(DEPARTMENTS)} department routine cards...")

    for i, dept in enumerate(DEPARTMENTS, 1):
        slug = dept["slug"]
        webp_filename = f"nu_honours_2nd_year_routine_{slug}.webp"
        final_webp_path = os.path.join(OUTPUT_DIR, webp_filename)

        html_code = generate_dept_card_html(dept)
        with open(temp_html, "w", encoding="utf-8") as f:
            f.write(html_code)

        cmd = [
            browser_bin,
            "--headless=new",
            "--disable-gpu",
            "--window-size=1080,1350",
            "--force-device-scale-factor=1",
            "--hide-scrollbars",
            f"--screenshot={temp_png}",
            f"file:///{temp_html.replace(os.sep, '/')}"
        ]

        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

        if not os.path.exists(temp_png):
            print(f"[{i}/{len(DEPARTMENTS)}] Failed to capture screenshot for {slug}")
            continue

        # Target 20-35 KB
        compress_to_target_webp(
            temp_png,
            final_webp_path,
            target_min_kb=20.0,
            target_max_kb=35.0,
            max_width=1080,
            max_height=1350
        )
        file_size_kb = os.path.getsize(final_webp_path) / 1024
        print(f"[{i}/{len(DEPARTMENTS)}] [OK] {slug} -> {file_size_kb:.1f} KB ({final_webp_path})")

    # Clean up temp files
    if os.path.exists(temp_html):
        os.remove(temp_html)
    if os.path.exists(temp_png):
        os.remove(temp_png)

    print("\n[SUCCESS] All department cards generated successfully!")
    return True


if __name__ == "__main__":
    build_all_department_cards()
