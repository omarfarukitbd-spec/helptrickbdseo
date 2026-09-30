#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/image_generator/build_fb_routine_card_demo.py
---------------------------------------------------
Generates a 100% authentic, zero-AI-tone Facebook post size (1080x1350 px)
examination routine card for Management Department:
- No artificial fluff or AI commentary ("বিভাগীয় মূল পত্র", "সর্বশেষ সংস্করণ").
- Pure official university examination terminology.
- Clean columns: তারিখ ও বার | পরীক্ষার সময় | বিষয় কোড | পত্রের শিরোনাম / নাম.
- Authentic exam hall rules (Admit card, No mobile phone, 30 min before).
- Clean HelpTrickBD logo and website.
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

ARTIFACT_DIR = r"C:\Users\omarf\.gemini\antigravity-ide\brain\1919afd7-77e9-4a5a-aeb3-60abfe06a7b9"
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "assets", "images", "posts")
FONT_PATH = os.path.join(PROJECT_ROOT, "assets", "fonts", "HindSiliguri-Bold.ttf")
LOGO_PATH = os.path.join(PROJECT_ROOT, "assets", "images", "logo", "helptrickbd_logo.png")

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(ARTIFACT_DIR, exist_ok=True)

HTML_CONTENT = f"""<!DOCTYPE html>
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
  background: #0f172a;
  color: #ffffff;
  padding: 14px 22px;
  border-radius: 8px;
  margin: 20px 0 22px 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}}
.dept-title-text {{
  font-size: 27px;
  font-weight: 800;
}}
.faculty-badge {{
  background: #0284c7;
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
  padding: 13px 16px;
  font-size: 18px;
  font-weight: 700;
}}
tbody tr {{
  border-bottom: 1.5px solid #e2e8f0;
}}
tbody tr:nth-child(even) {{
  background: #f8fafc;
}}
tbody tr:nth-child(odd) {{
  background: #ffffff;
}}
td {{
  padding: 15px 16px;
  font-size: 18px;
  color: #0f172a;
  vertical-align: middle;
}}
.td-day {{
  font-weight: 700;
  color: #1e293b;
  font-size: 17px;
}}
.td-time {{
  font-size: 16px;
  color: #475569;
  font-weight: 600;
}}
.td-code {{
  font-size: 21px;
  font-weight: 800;
  color: #0284c7;
  font-family: Arial, sans-serif;
}}
.td-paper {{
  font-weight: 700;
  color: #0f172a;
  font-size: 19px;
  line-height: 1.35;
}}

/* Authentic Examination Rules Box */
.instructions-box {{
  background: #f8fafc;
  border: 1.5px solid #cbd5e1;
  border-left: 6px solid #0f172a;
  padding: 16px 20px;
  border-radius: 8px;
  margin: 20px 0 16px 0;
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
  font-size: 15.5px;
  line-height: 1.65;
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
    <div class="dept-title-text">ব্যবস্থাপনা বিভাগ (Department of Management)</div>
    <div class="faculty-badge">ব্যবসায় শিক্ষা অনুষদ</div>
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
        <tr>
          <td class="td-day">২৮/০৯/২০২৬ (সোমবার)</td>
          <td class="td-time">দুপুর ০১:০০ টা</td>
          <td class="td-code">221109</td>
          <td class="td-paper">English (Compulsory) — Non-Credit</td>
        </tr>
        <tr>
          <td class="td-day">০১/১০/২০২৬ (বৃহস্পতিবার)</td>
          <td class="td-time">দুপুর ০১:০০ টা</td>
          <td class="td-code">222601</td>
          <td class="td-paper">Human Resource Management</td>
        </tr>
        <tr>
          <td class="td-day">০৭/১০/২০২৬ (বুধবার)</td>
          <td class="td-time">দুপুর ০১:০০ টা</td>
          <td class="td-code">222603</td>
          <td class="td-paper">Business Communication (In English)</td>
        </tr>
        <tr>
          <td class="td-day">১২/১০/২০২৬ (সোমবার)</td>
          <td class="td-time">দুপুর ০১:০০ টা</td>
          <td class="td-code">222605</td>
          <td class="td-paper">Business Mathematics</td>
        </tr>
        <tr>
          <td class="td-day">১৯/১০/২০২৬ (সোমবার)</td>
          <td class="td-time">দুপুর ০১:০০ টা</td>
          <td class="td-code">222607</td>
          <td class="td-paper">Principles of Finance</td>
        </tr>
        <tr>
          <td class="td-day">২৬/১০/২০২৬ (সোমবার)</td>
          <td class="td-time">দুপুর ০১:০০ টা</td>
          <td class="td-code">222609</td>
          <td class="td-paper">Legal Aspects of Business</td>
        </tr>
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

  <!-- Footer -->
  <div class="card-bottom-footer">
    <div class="authority-text">পরীক্ষা নিয়ন্ত্রণ দপ্তর, জাতীয় বিশ্ববিদ্যালয়, গাজীপুর</div>
    <div>অফিসিয়াল সোর্স: nu.ac.bd</div>
    <div>সৌজন্যে: HelpTrickBD.com</div>
  </div>

</div>

</body>
</html>"""


def main():
    print("=" * 72)
    print("  GENERATING 100% AUTHENTIC ZERO-AI-TONE ROUTINE CARD DEMO")
    print("=" * 72)

    temp_html = os.path.join(PROJECT_ROOT, "temp_fb_card_demo.html")
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)

    out_png = os.path.join(OUTPUT_DIR, "demo_fb_routine_management.png")
    out_webp = os.path.join(OUTPUT_DIR, "demo_fb_routine_management.webp")
    out_artifact_png = os.path.join(ARTIFACT_DIR, "demo_fb_routine_management.png")
    out_artifact_webp = os.path.join(ARTIFACT_DIR, "demo_fb_routine_management.webp")

    browser_bin = get_browser_binary()
    import tempfile
    user_data_dir = os.path.join(tempfile.gettempdir(), "edge_fb_demo_clean")

    cmd = [
        browser_bin,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--user-data-dir={user_data_dir}",
        "--force-device-scale-factor=1",
        "--window-size=1080,1350",
        f"--screenshot={out_png}",
        "file:///" + os.path.abspath(temp_html).replace("\\", "/")
    ]
    subprocess.run(cmd, check=True, capture_output=True)

    if os.path.exists(temp_html):
        os.remove(temp_html)

    # Compress to WebP
    compress_to_target_webp(out_png, out_webp, target_min_kb=25.0, target_max_kb=50.0)

    # Copy to artifact dir
    import shutil
    shutil.copy2(out_png, out_artifact_png)
    shutil.copy2(out_webp, out_artifact_webp)

    size_kb = os.path.getsize(out_webp) / 1024.0
    print(f"\n[OK] Clean Authentic Facebook Card Generated!")
    print(f"     WebP: {out_webp} ({size_kb:.1f} KB)")
    print(f"     Artifact: {out_artifact_png}")
    print("=" * 72)


if __name__ == "__main__":
    main()
