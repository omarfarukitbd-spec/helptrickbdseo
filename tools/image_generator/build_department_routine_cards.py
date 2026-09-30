#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/image_generator/build_department_routine_cards.py
-------------------------------------------------------
Generates individual, 16:9 high-resolution department-wise timetable cards
for National University Honours 2nd Year Exam Routine 2026:
1. Political Science (রাষ্ট্রবিজ্ঞান বিভাগ)
2. Accounting (হিসাববিজ্ঞান বিভাগ)
3. Management (ব্যবস্থাপনা বিভাগ)
4. Bangla (বাংলা বিভাগ)
5. English (ইংরেজি বিভাগ)

Renders via headless Chrome / Edge and compresses to 15-25 KB WebP.
Zero emojis, 100% SolaimanLipi / Hind Siliguri typography.
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

BG_DIR = os.path.join(PROJECT_ROOT, "Thumbnail BG")
POSTS_DIR = os.path.join(PROJECT_ROOT, "assets", "images", "posts")
THUMBS_DIR = os.path.join(PROJECT_ROOT, "assets", "images", "thumbnails")
FONT_PATH = os.path.join(PROJECT_ROOT, "assets", "fonts", "HindSiliguri-Bold.ttf")

os.makedirs(POSTS_DIR, exist_ok=True)
os.makedirs(THUMBS_DIR, exist_ok=True)

DEPARTMENTS = [
    {
        "slug": "political_science",
        "bg": "bg_2.png",
        "faculty": "সামাজিক বিজ্ঞান অনুষদ | Social Science Faculty",
        "dept_name": "রাষ্ট্রবিজ্ঞান বিভাগ (Department of Political Science)",
        "theme_color": "#0b2046",
        "accent_color": "#d97706",
        "badge_bg": "#1e3a8a",
        "papers": [
            ("পরীক্ষার ১ম দিন", "221109", "ইংরেজি (আবশ্যিক) — নন ক্রেডিট", "সকল শিক্ষার্থীর জন্য বাধ্যতামূলক"),
            ("পরীক্ষার ২য় দিন", "221901", "বৃটিশ ভারতের রাজনৈতিক ও সাংবিধানিক উন্নয়ন", "১৭৫৭ থেকে ১৯৪৭ সাল পর্যন্ত ইতিহাস"),
            ("পরীক্ষার ৩য় দিন", "221903", "রাজনৈতিক সমাজবিজ্ঞান (Political Sociology)", "মূল তাত্ত্বিক ও প্রায়োগিক কাঠামো"),
            ("পরীক্ষার ৪র্থ দিন", "221905", "পূর্ব এশিয়ার সরকার ও রাজনীতি", "চীন ও জাপান শাসনব্যবস্থা"),
            ("পরীক্ষার ৫ম দিন", "221907", "দক্ষিণ এশিয়ার সরকার ও রাজনীতি", "ভারত, পাকিস্তান ও শ্রীলঙ্কা রাজনীতি")
        ]
    },
    {
        "slug": "accounting",
        "bg": "bg_3.png",
        "faculty": "ব্যবসায় শিক্ষা অনুষদ | Business Studies Faculty",
        "dept_name": "হিসাববিজ্ঞান বিভাগ (Department of Accounting)",
        "theme_color": "#064e3b",
        "accent_color": "#059669",
        "badge_bg": "#065f46",
        "papers": [
            ("পরীক্ষার ১ম দিন", "221109", "English (Compulsory) — Non-Credit", "Mandatory Pass Course"),
            ("পরীক্ষার ২য় দিন", "222501", "Advanced Accounting-I", "Core Departmental Paper"),
            ("পরীক্ষার ৩য় দিন", "222503", "Business Communication and Report Writing", "In English Language"),
            ("পরীক্ষার ৪র্থ দিন", "222505", "Business Mathematics", "Formulas & Practical Problems"),
            ("পরীক্ষার ৫ম দিন", "222507", "Taxation in Bangladesh", "Direct & Indirect Tax Laws"),
            ("পরীক্ষার ৬ষ্ঠ দিন", "222509", "Principles of Finance", "Financial Analysis & Planning")
        ]
    },
    {
        "slug": "management",
        "bg": "bg_3.png",
        "faculty": "ব্যবসায় শিক্ষা অনুষদ | Business Studies Faculty",
        "dept_name": "ব্যবস্থাপনা বিভাগ (Department of Management)",
        "theme_color": "#0f172a",
        "accent_color": "#0284c7",
        "badge_bg": "#1e293b",
        "papers": [
            ("পরীক্ষার ১ম দিন", "221109", "English (Compulsory) — Non-Credit", "Mandatory Pass Course"),
            ("পরীক্ষার ২য় দিন", "222601", "Human Resource Management", "Core Management Paper"),
            ("পরীক্ষার ৩য় দিন", "222603", "Business Communication (In English)", "Written & Practical Drafting"),
            ("পরীক্ষার ৪র্থ দিন", "222605", "Business Mathematics", "Quantitative Techniques"),
            ("পরীক্ষার ৫ম দিন", "222607", "Principles of Finance", "Capital Budgeting & Risk"),
            ("পরীক্ষার ৬ষ্ঠ দিন", "222609", "Legal Aspects of Business", "Commercial & Company Law")
        ]
    },
    {
        "slug": "bangla",
        "bg": "bg_1.png",
        "faculty": "কলা অনুষদ | Arts Faculty",
        "dept_name": "বাংলা বিভাগ (Department of Bangla)",
        "theme_color": "#7c2d12",
        "accent_color": "#ea580c",
        "badge_bg": "#9a3412",
        "papers": [
            ("পরীক্ষার ১ম দিন", "221109", "ইংরেজি (আবশ্যিক) — নন ক্রেডিট", "সকল শিক্ষার্থীর জন্য বাধ্যতামূলক"),
            ("পরীক্ষার ২য় দিন", "221001", "বাংলা সাহিত্যের ইতিহাস-১", "প্রাচীন ও মধ্যযুগীয় সাহিত্যের ধারা"),
            ("পরীক্ষার ৩য় দিন", "221003", "মধ্যযুগের কবিতা", "শ্রীকৃষ্ণকীর্তন ও মঙ্গলকাব্য ধারা"),
            ("পরীক্ষার ৪র্থ দিন", "221005", "বাংলা কবিতা-২", "আধুনিক যুগের প্রধান প্রধান কাব্যধারা"),
            ("পরীক্ষার ৫ম দিন", "221007", "বাংলা নাটক-১", "মাইকেল, দীনবন্ধু ও গিরিশচন্দ্র নাটক")
        ]
    },
    {
        "slug": "english",
        "bg": "bg_1.png",
        "faculty": "কলা অনুষদ | Arts Faculty",
        "dept_name": "ইংরেজি বিভাগ (Department of English)",
        "theme_color": "#1e1b4b",
        "accent_color": "#4338ca",
        "badge_bg": "#312e81",
        "papers": [
            ("পরীক্ষার ১ম দিন", "221109", "English (Compulsory) — Non-Credit", "Common Compulsory Subject"),
            ("পরীক্ষার ২য় দিন", "221101", "Introduction to Drama", "Major Plays & Dramatic History"),
            ("পরীক্ষার ৩য় দিন", "221103", "Romantic Poetry", "Wordsworth, Coleridge, Keats, Shelley"),
            ("পরীক্ষার ৪র্থ দিন", "221105", "Advanced Reading and Writing", "Applied Language & Essays"),
            ("পরীক্ষার ৫ম দিন", "221107", "History of English Literature", "Anglo-Saxon to Modern Age")
        ]
    }
]


def render_card_html(dept: dict) -> str:
    bg_file = dept["bg"]
    bg_url = "file:///" + os.path.join(BG_DIR, bg_file).replace("\\", "/")
    font_url = "file:///" + FONT_PATH.replace("\\", "/")

    rows_html = ""
    for idx, (day, code, paper, note) in enumerate(dept["papers"]):
        bg_row = "#ffffff" if idx % 2 == 0 else "#f8fafc"
        rows_html += f"""
        <tr style="background: {bg_row};">
          <td style="padding: 10px 14px; font-weight: 700; color: #1e293b; border-bottom: 1px solid #e2e8f0; font-size: 15px;">{day}</td>
          <td style="padding: 10px 14px; font-weight: 800; color: {dept['theme_color']}; border-bottom: 1px solid #e2e8f0; font-size: 16px; font-family: Arial, sans-serif;">{code}</td>
          <td style="padding: 10px 14px; font-weight: 700; color: #0f172a; border-bottom: 1px solid #e2e8f0; font-size: 15px;">{paper}</td>
          <td style="padding: 10px 14px; color: #64748b; border-bottom: 1px solid #e2e8f0; font-size: 13.5px;">{note}</td>
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
  background-image: url('{bg_url}');
  background-size: 1200px 675px;
  background-position: center;
  background-repeat: no-repeat;
  font-family: 'HindSiliguri', sans-serif;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  padding: 30px 65px 0 65px;
}}
.header-bar {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  margin-bottom: 16px;
}}
.brand-pill {{
  background: #ffffff;
  color: {dept['theme_color']};
  font-size: 16px;
  font-weight: 700;
  padding: 6px 18px;
  border-radius: 14px;
  border: 1.5px solid #cbd5e1;
  box-shadow: 0 3px 8px rgba(0,0,0,0.06);
}}
.faculty-pill {{
  background: {dept['badge_bg']};
  color: #ffffff;
  font-size: 16px;
  font-weight: 700;
  padding: 6px 20px;
  border-radius: 14px;
  border: 1.5px solid {dept['accent_color']};
  box-shadow: 0 4px 10px rgba(0,0,0,0.12);
}}
.title-area {{
  text-align: center;
  margin-bottom: 15px;
}}
.main-title {{
  font-size: 32px;
  color: {dept['theme_color']};
  font-weight: 800;
  line-height: 1.25;
  margin-bottom: 4px;
}}
.sub-meta {{
  font-size: 17px;
  color: #334155;
  font-weight: 600;
}}
.table-card {{
  width: 100%;
  background: #ffffff;
  border-radius: 12px;
  box-shadow: 0 6px 20px rgba(0,0,0,0.08);
  border: 1.5px solid #e2e8f0;
  overflow: hidden;
  margin-bottom: 14px;
}}
table {{
  width: 100%;
  border-collapse: collapse;
  text-align: left;
}}
th {{
  background: {dept['theme_color']};
  color: #ffffff;
  padding: 10px 14px;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: 0.2px;
}}
.footer-bar {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 10px;
  font-size: 14px;
  color: #475569;
  font-weight: 600;
}}
.footer-badge {{
  background: #f1f5f9;
  padding: 4px 14px;
  border-radius: 10px;
  border: 1px solid #cbd5e1;
  color: {dept['theme_color']};
  font-weight: 700;
}}
</style>
</head>
<body>

<div class="header-bar">
  <div class="brand-pill">HelpTrickBD • জাতীয় বিশ্ববিদ্যালয় গাইড</div>
  <div class="faculty-pill">{dept['faculty']}</div>
</div>

<div class="title-area">
  <h1 class="main-title">{dept['dept_name']}</h1>
  <div class="sub-meta">অনার্স ২য় বর্ষ চূড়ান্ত পরীক্ষা ২০২৬ • বিষয়ভিত্তিক পরীক্ষার রুটিন ও পূর্ণাঙ্গ কোড তালিকা</div>
</div>

<div class="table-card">
  <table>
    <thead>
      <tr>
        <th style="width: 18%;">পরীক্ষার দিন / সময়</th>
        <th style="width: 16%;">বিষয় কোড</th>
        <th style="width: 38%;">পত্রের নাম ও বিবরণ</th>
        <th style="width: 28%;">বিশেষ নির্দেশনা / সিলেবাস নোট</th>
      </tr>
    </thead>
    <tbody>
      {rows_html}
    </tbody>
  </table>
</div>

<div class="footer-bar">
  <div>© HelpTrickBD Education Platform • www.helptrickbd.com</div>
  <div class="footer-badge">নিয়মিত, অনিয়মিত ও মানোন্নয়ন পরীক্ষার্থীদের জন্য প্রযোজ্য</div>
  <div>অফিসিয়াল সোর্স: nu.ac.bd</div>
</div>

</body>
</html>"""


def main():
    print("=" * 72)
    print("  GENERATING DEPARTMENT-WISE EXAM ROUTINE CARDS (NU 2ND YEAR 2026)")
    print("=" * 72)

    browser_bin = get_browser_binary()
    generated_files = []

    for dept in DEPARTMENTS:
        slug = dept["slug"]
        base_name = f"nu_honours_2nd_year_routine_{slug}"
        print(f"\n[*] Processing: {dept['dept_name']}...")

        html_content = render_card_html(dept)
        temp_html = os.path.join(PROJECT_ROOT, f"temp_{base_name}.html")
        with open(temp_html, "w", encoding="utf-8") as f:
            f.write(html_content)

        out_png = os.path.join(POSTS_DIR, f"{base_name}.png")
        out_webp = os.path.join(POSTS_DIR, f"{base_name}.webp")
        out_jpg = os.path.join(POSTS_DIR, f"{base_name}.jpg")

        import tempfile
        user_data_dir = os.path.join(tempfile.gettempdir(), f"edge_{slug}")

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

        # Clean temporary PNG
        if os.path.exists(out_png):
            os.remove(out_png)

        size_kb = os.path.getsize(out_webp) / 1024.0
        print(f"    [OK] Saved: {base_name}.webp ({size_kb:.1f} KB)")
        generated_files.append((dept, out_webp))

    print("\n" + "=" * 72)
    print(f"  [SUCCESS] Total {len(generated_files)} Department Cards Generated!")
    print("=" * 72)


if __name__ == "__main__":
    main()
