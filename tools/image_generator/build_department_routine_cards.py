#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/image_generator/build_department_routine_cards.py
-------------------------------------------------------
Generates authentic, clean Facebook-style examination routine cards (NO thumbnail BG):
1. Political Science (রাষ্ট্রবিজ্ঞান বিভাগ)
2. Accounting (হিসাববিজ্ঞান বিভাগ)
3. Management (ব্যবস্থাপনা বিভাগ)
4. Bangla (বাংলা বিভাগ)
5. English (ইংরেজি বিভাগ)

Design:
- Crisp white/light-slate document canvas with high-contrast academic framing.
- Official National University exam header.
- Small HelpTrickBD logo and branding at top right.
- High-contrast timetable table with dates, subject codes, and paper names.
- Bottom exam rules callout box.
- Output: 16:9 WebP format (15-25 KB) via headless browser.
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

POSTS_DIR = os.path.join(PROJECT_ROOT, "assets", "images", "posts")
THUMBS_DIR = os.path.join(PROJECT_ROOT, "assets", "images", "thumbnails")
FONT_PATH = os.path.join(PROJECT_ROOT, "assets", "fonts", "HindSiliguri-Bold.ttf")
LOGO_PATH = os.path.join(PROJECT_ROOT, "assets", "images", "logo", "helptrickbd_logo.png")

os.makedirs(POSTS_DIR, exist_ok=True)
os.makedirs(THUMBS_DIR, exist_ok=True)

DEPARTMENTS = [
    {
        "slug": "political_science",
        "faculty": "সামাজিক বিজ্ঞান অনুষদ",
        "dept_name": "রাষ্ট্রবিজ্ঞান বিভাগ | Department of Political Science",
        "primary_color": "#1e3a8a",
        "accent_color": "#2563eb",
        "papers": [
            ("পরীক্ষার ১ম দিন", "দুপুর ০১:০০ টা", "221109", "ইংরেজি (আবশ্যিক) — নন ক্রেডিট", "সকল শিক্ষার্থীর জন্য বাধ্যতামূলক"),
            ("পরীক্ষার ২য় দিন", "দুপুর ০১:০০ টা", "221901", "বৃটিশ ভারতের রাজনৈতিক ও সাংবিধানিক উন্নয়ন (১৭৫৭-১৯৪৭)", "তত্ত্বীয় মূল পত্র"),
            ("পরীক্ষার ৩য় দিন", "দুপুর ০১:০০ টা", "221903", "রাজনৈতিক সমাজবিজ্ঞান (Political Sociology)", "তত্ত্বীয় মূল পত্র"),
            ("পরীক্ষার ৪র্থ দিন", "দুপুর ০১:০০ টা", "221905", "পূর্ব এশিয়ার সরকার ও রাজনীতি (চীন ও জাপান)", "তত্ত্বীয় মূল পত্র"),
            ("পরীক্ষার ৫ম দিন", "দুপুর ০১:০০ টা", "221907", "দক্ষিণ এশিয়ার সরকার ও রাজনীতি (ভারত, পাকিস্তান ও শ্রীলঙ্কা)", "তত্ত্বীয় মূল পত্র")
        ]
    },
    {
        "slug": "accounting",
        "faculty": "ব্যবসায় শিক্ষা অনুষদ",
        "dept_name": "হিসাববিজ্ঞান বিভাগ | Department of Accounting",
        "primary_color": "#065f46",
        "accent_color": "#059669",
        "papers": [
            ("পরীক্ষার ১ম দিন", "দুপুর ০১:০০ টা", "221109", "English (Compulsory) — Non-Credit", "Mandatory Pass Subject"),
            ("পরীক্ষার ২য় দিন", "দুপুর ০১:০০ টা", "222501", "Advanced Accounting-I", "Core Major Paper"),
            ("পরীক্ষার ৩য় দিন", "দুপুর ০১:০০ টা", "222503", "Business Communication and Report Writing", "Written English Paper"),
            ("পরীক্ষার ৪র্থ দিন", "দুপুর ০১:০০ টা", "222505", "Business Mathematics", "Formulas & Problems"),
            ("পরীক্ষার ৫ম দিন", "দুপুর ০১:০০ টা", "222507", "Taxation in Bangladesh", "Income Tax & VAT Laws"),
            ("পরীক্ষার ৬ষ্ঠ দিন", "দুপুর ০১:০০ টা", "222509", "Principles of Finance", "Financial Analysis")
        ]
    },
    {
        "slug": "management",
        "faculty": "ব্যবসায় শিক্ষা অনুষদ",
        "dept_name": "ব্যবস্থাপনা বিভাগ | Department of Management",
        "primary_color": "#0f172a",
        "accent_color": "#0284c7",
        "papers": [
            ("পরীক্ষার ১ম দিন", "দুপুর ০১:০০ টা", "221109", "English (Compulsory) — Non-Credit", "Mandatory Pass Subject"),
            ("পরীক্ষার ২য় দিন", "দুপুর ০১:০০ টা", "222601", "Human Resource Management", "Core Major Paper"),
            ("পরীক্ষার ৩য় দিন", "দুপুর ০১:০০ টা", "222603", "Business Communication (In English)", "Applied Drafting"),
            ("পরীক্ষার ৪র্থ দিন", "দুপুর ০১:০০ টা", "222605", "Business Mathematics", "Quantitative Paper"),
            ("পরীক্ষার ৫ম দিন", "দুপুর ০১:০০ টা", "222607", "Principles of Finance", "Corporate Finance"),
            ("পরীক্ষার ৬ষ্ঠ দিন", "দুপুর ০১:০০ টা", "222609", "Legal Aspects of Business", "Commercial Law")
        ]
    },
    {
        "slug": "bangla",
        "faculty": "কলা অনুষদ",
        "dept_name": "বাংলা বিভাগ | Department of Bangla",
        "primary_color": "#9a3412",
        "accent_color": "#ea580c",
        "papers": [
            ("পরীক্ষার ১ম দিন", "দুপুর ০১:০০ টা", "221109", "ইংরেজি (আবশ্যিক) — নন ক্রেডিট", "সকল শিক্ষার্থীর জন্য বাধ্যতামূলক"),
            ("পরীক্ষার ২য় দিন", "দুপুর ০১:০০ টা", "221001", "বাংলা সাহিত্যের ইতিহাস-১ (প্রাচীন ও মধ্যযুগ)", "তত্ত্বীয় মূল পত্র"),
            ("পরীক্ষার ৩য় দিন", "দুপুর ০১:০০ টা", "221003", "মধ্যযুগের কবিতা (শ্রীকৃষ্ণকীর্তন ও মঙ্গলকাব্য)", "তত্ত্বীয় মূল পত্র"),
            ("পরীক্ষার ৪র্থ দিন", "দুপুর ০১:০০ টা", "221005", "বাংলা কবিতা-২ (আধুনিক যুগ)", "তত্ত্বীয় মূল পত্র"),
            ("পরীক্ষার ৫ম দিন", "দুপুর ০১:০০ টা", "221007", "বাংলা নাটক-১ (প্রারম্ভিক ও আধুনিক নাটক)", "তত্ত্বীয় মূল পত্র")
        ]
    },
    {
        "slug": "english",
        "faculty": "কলা অনুষদ",
        "dept_name": "ইংরেজি বিভাগ | Department of English",
        "primary_color": "#312e81",
        "accent_color": "#4338ca",
        "papers": [
            ("পরীক্ষার ১ম দিন", "দুপুর ০১:০০ টা", "221109", "English (Compulsory) — Non-Credit", "Common Mandatory Paper"),
            ("পরীক্ষার ২য় দিন", "দুপুর ০১:০০ টা", "221101", "Introduction to Drama", "Major Plays & Tragedy"),
            ("পরীক্ষার ৩য় দিন", "দুপুর ০১:০০ টা", "221103", "Romantic Poetry", "Romantic Period Poets"),
            ("পরীক্ষার ৪র্থ দিন", "দুপুর ০১:০০ টা", "221105", "Advanced Reading and Writing", "Linguistic Applications"),
            ("পরীক্ষার ৫ম দিন", "দুপুর ০১:০০ টা", "221107", "History of English Literature", "Literary Eras & Criticism")
        ]
    }
]


def render_facebook_routine_card_html(dept: dict) -> str:
    font_url = "file:///" + FONT_PATH.replace("\\", "/")
    logo_url = "file:///" + LOGO_PATH.replace("\\", "/")

    rows_html = ""
    for idx, (day, time_str, code, paper, note) in enumerate(dept["papers"]):
        bg_row = "#ffffff" if idx % 2 == 0 else "#f8fafc"
        rows_html += f"""
        <tr style="background: {bg_row};">
          <td style="padding: 9px 12px; font-weight: 700; color: #1e293b; border-bottom: 1px solid #e2e8f0; font-size: 14.5px;">{day}</td>
          <td style="padding: 9px 12px; font-weight: 600; color: #475569; border-bottom: 1px solid #e2e8f0; font-size: 14px;">{time_str}</td>
          <td style="padding: 9px 12px; font-weight: 800; color: {dept['primary_color']}; border-bottom: 1px solid #e2e8f0; font-size: 16px; font-family: Arial, sans-serif;">{code}</td>
          <td style="padding: 9px 12px; font-weight: 700; color: #0f172a; border-bottom: 1px solid #e2e8f0; font-size: 15px;">{paper}</td>
          <td style="padding: 9px 12px; color: #64748b; border-bottom: 1px solid #e2e8f0; font-size: 13.5px;">{note}</td>
        </tr>
        """

    return f"""<!DOCTYPE html>
<html lang="bn">
<head>
<meta charset="utf-8" />
<style>
@font-face {{
  font-family: 'HindSiliguri';
  src: url('{font_url}') format('truetype');
  font-weight: 700;
}}
* {{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}}
body {{
  width: 1200px;
  height: 675px;
  overflow: hidden;
  background: #f1f5f9;
  font-family: 'HindSiliguri', Arial, sans-serif;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 16px;
}}
.card-container {{
  width: 1168px;
  height: 643px;
  background: #ffffff;
  border-radius: 12px;
  border: 4px solid {dept['primary_color']};
  box-shadow: 0 10px 30px rgba(0,0,0,0.08);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 22px 28px 18px 28px;
}}

/* Top Official Header */
.top-header {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 2px solid #e2e8f0;
  padding-bottom: 14px;
}}
.inst-info {{
  display: flex;
  flex-direction: column;
}}
.inst-title {{
  font-size: 23px;
  font-weight: 800;
  color: #0f172a;
  line-height: 1.2;
}}
.inst-sub {{
  font-size: 15px;
  font-weight: 600;
  color: #475569;
  margin-top: 3px;
}}
.brand-box {{
  display: flex;
  align-items: center;
  gap: 12px;
}}
.brand-logo {{
  height: 38px;
  width: auto;
  object-fit: contain;
}}
.brand-text {{
  text-align: right;
}}
.brand-name {{
  font-size: 16px;
  font-weight: 800;
  color: {dept['primary_color']};
  line-height: 1.1;
}}
.brand-url {{
  font-size: 12px;
  color: #64748b;
  font-weight: 600;
}}

/* Department Banner Strip */
.dept-banner {{
  background: {dept['primary_color']};
  color: #ffffff;
  padding: 10px 20px;
  border-radius: 8px;
  margin: 12px 0 14px 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}}
.dept-name {{
  font-size: 22px;
  font-weight: 800;
  letter-spacing: 0.3px;
}}
.faculty-tag {{
  background: rgba(255,255,255,0.18);
  padding: 4px 14px;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 700;
  border: 1px solid rgba(255,255,255,0.3);
}}

/* Timetable */
.table-wrapper {{
  width: 100%;
  border-radius: 8px;
  overflow: hidden;
  border: 1.5px solid #cbd5e1;
}}
table {{
  width: 100%;
  border-collapse: collapse;
  text-align: left;
}}
th {{
  background: #0f172a;
  color: #ffffff;
  padding: 9px 12px;
  font-size: 14.5px;
  font-weight: 700;
}}

/* Rules Callout */
.notice-callout {{
  background: #eff6ff;
  border-left: 4px solid {dept['accent_color']};
  padding: 8px 14px;
  border-radius: 0 6px 6px 0;
  margin-top: 10px;
  font-size: 13.5px;
  color: #1e3a8a;
  line-height: 1.45;
}}

/* Footer */
.card-footer {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 13px;
  color: #64748b;
  font-weight: 600;
  padding-top: 8px;
  border-top: 1px solid #f1f5f9;
}}
.footer-badge {{
  background: #f8fafc;
  border: 1px solid #cbd5e1;
  padding: 3px 12px;
  border-radius: 8px;
  color: #334155;
  font-weight: 700;
}}
</style>
</head>
<body>

<div class="card-container">
  <div class="top-header">
    <div class="inst-info">
      <div class="inst-title">জাতীয় বিশ্ববিদ্যালয়, বাংলাদেশ | National University, Bangladesh</div>
      <div class="inst-sub">অনার্স ২য় বর্ষ চূড়ান্ত পরীক্ষা ২০২৬ • সংশোধিত সময়সূচি ও বিষয় কোড তালিকা</div>
    </div>
    <div class="brand-box">
      <div class="brand-text">
        <div class="brand-name">HelpTrickBD</div>
        <div class="brand-url">www.helptrickbd.com</div>
      </div>
      <img src="{logo_url}" class="brand-logo" alt="HelpTrickBD" />
    </div>
  </div>

  <div class="dept-banner">
    <div class="dept-name">{dept['dept_name']}</div>
    <div class="faculty-tag">{dept['faculty']}</div>
  </div>

  <div class="table-wrapper">
    <table>
      <thead>
        <tr>
          <th style="width: 17%;">পরীক্ষার দিন</th>
          <th style="width: 15%;">শুরুর সময়</th>
          <th style="width: 15%;">বিষয় কোড</th>
          <th style="width: 35%;">পত্রের নাম ও বিবরণ</th>
          <th style="width: 18%;">সিলেবাস নোট</th>
        </tr>
      </thead>
      <tbody>
        {rows_html}
      </tbody>
    </table>
  </div>

  <div class="notice-callout">
    <strong>জরুরি নির্দেশনাবলী:</strong> প্রতিদিন দুপুর ০১:০০ টা থেকে পরীক্ষা শুরু হবে • ইংরেজি আবশ্যিক (২২১১০৯) সকল শিক্ষার্থীর জন্য বাধ্যতামূলক • রুটিনের যেকোনো সর্বশেষ তথ্যের জন্য ভিজিট করুন HelpTrickBD.com
  </div>

  <div class="card-footer">
    <div>সংগ্রহে: HelpTrickBD Academic Portal • www.helptrickbd.com</div>
    <div class="footer-badge">নিয়মিত (২০২২-২৩), অনিয়মিত ও মানোন্নয়ন (২০২১-২২, ২০২০-২১)</div>
    <div>অফিসিয়াল সোর্স: nu.ac.bd</div>
  </div>
</div>

</body>
</html>"""


def main():
    print("=" * 72)
    print("  GENERATING CLEAN FACEBOOK-STYLE DEPARTMENT ROUTINE CARDS")
    print("=" * 72)

    browser_bin = get_browser_binary()
    generated_files = []

    for dept in DEPARTMENTS:
        slug = dept["slug"]
        base_name = f"nu_honours_2nd_year_routine_{slug}"
        print(f"\n[*] Processing: {dept['dept_name']}...")

        html_content = render_facebook_routine_card_html(dept)
        temp_html = os.path.join(PROJECT_ROOT, f"temp_{base_name}.html")
        with open(temp_html, "w", encoding="utf-8") as f:
            f.write(html_content)

        out_png = os.path.join(POSTS_DIR, f"{base_name}.png")
        out_webp = os.path.join(POSTS_DIR, f"{base_name}.webp")
        out_jpg = os.path.join(POSTS_DIR, f"{base_name}.jpg")

        import tempfile
        user_data_dir = os.path.join(tempfile.gettempdir(), f"edge_fb_{slug}")

        cmd = [
            browser_bin,
            "--headless=new",
            "--disable-gpu",
            "--hide-scrollbars",
            f"--user-data-dir={user_data_dir}",
            "--force-device-scale-factor=1",
            "--window-size=1200,675",
            f"--screenshot={out_png}",
            "file:///" + os.path.abspath(temp_html).replace("\\", "/")
        ]
        subprocess.run(cmd, check=True, capture_output=True)

        if os.path.exists(temp_html):
            os.remove(temp_html)

        img = Image.open(out_png).convert("RGB")
        img.save(out_jpg, "JPEG", quality=92)
        compress_to_target_webp(out_png, out_webp, target_min_kb=15.0, target_max_kb=30.0)

        # Sync to thumbnails folder
        import shutil
        shutil.copy2(out_webp, os.path.join(THUMBS_DIR, f"{base_name}.webp"))
        shutil.copy2(out_jpg, os.path.join(THUMBS_DIR, f"{base_name}.jpg"))

        if os.path.exists(out_png):
            os.remove(out_png)

        size_kb = os.path.getsize(out_webp) / 1024.0
        print(f"    [OK] Saved Clean FB-Style Card: {base_name}.webp ({size_kb:.1f} KB)")
        generated_files.append((dept, out_webp))

    print("\n" + "=" * 72)
    print(f"  [SUCCESS] All {len(generated_files)} Clean Cards Generated Successfully!")
    print("=" * 72)


if __name__ == "__main__":
    main()
