#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/image_generator/build_ntrca_school_banner.py
--------------------------------------------------
Builds the official HelpTrickBD 16:9 featured banner for NTRCA School Syllabus
using Thumbnail BG/bg_4.png and Chromium HarfBuzz rendering.
"""

import os
import sys
import subprocess
from PIL import Image

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

from tools.image_optimizer.webp_compressor import compress_to_target_webp

BG_PATH = os.path.join(PROJECT_ROOT, "Thumbnail BG", "bg_4.png")
OUTPUT_WEBP = os.path.join(PROJECT_ROOT, "assets", "images", "posts", "ntrca_school_level_assistant_teacher_syllabus_2026.webp")
OUTPUT_PNG = os.path.join(PROJECT_ROOT, "scratch", "ntrca_school_banner.png")
TEMP_HTML = os.path.join(PROJECT_ROOT, "scratch", "banner_ntrca.html")

chrome_candidates = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
]
CHROME_PATH = None
for c in chrome_candidates:
    if os.path.exists(c):
        CHROME_PATH = c
        break

html_template = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
@import url('https://fonts.maateen.me/solaiman-lipi/font.css');
* {{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}}
body {{
  width: 1200px;
  height: 675px;
  overflow: hidden;
  position: relative;
  font-family: 'SolaimanLipi', sans-serif;
  background: url('{BG_PATH.replace(os.sep, "/")}') no-repeat center center;
  background-size: cover;
}}
.canvas {{
  width: 1200px;
  height: 675px;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  padding: 38px 70px 0 70px;
}}
.top-bar {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  margin-bottom: 28px;
}}
.brand-badge {{
  background: #ffffff;
  color: #064e3b;
  font-size: 20px;
  font-weight: 700;
  padding: 8px 24px;
  border-radius: 20px;
  border: 1.5px solid #e2e8f0;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  letter-spacing: 0.5px;
}}
.category-badge {{
  background: #064e3b;
  color: #ffffff;
  border: 2px solid #f59e0b;
  font-size: 19px;
  font-weight: 700;
  padding: 8px 24px;
  border-radius: 20px;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.15);
}}
.center-container {{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  width: 100%;
  max-width: 980px;
  margin: 0 auto;
}}
.topic-tag {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: #f0fdf4;
  border: 1.5px solid #bbf7d0;
  color: #15803d;
  font-size: 20px;
  font-weight: 700;
  padding: 6px 22px;
  border-radius: 16px;
  margin-bottom: 14px;
}}
h1.banner-title {{
  margin: 0 0 14px 0;
  font-size: 44px;
  line-height: 1.25;
  color: #064e3b;
  font-weight: 800;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
}}
p.banner-subtitle {{
  margin: 0 0 26px 0;
  font-size: 22px;
  line-height: 1.4;
  color: #334155;
  font-weight: 600;
  max-width: 860px;
}}
.meta-pills {{
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 14px;
  margin-bottom: 24px;
}}
.pill {{
  background: #ffffff;
  border: 1.5px solid #cbd5e1;
  color: #064e3b;
  font-size: 17px;
  font-weight: 700;
  padding: 8px 20px;
  border-radius: 25px;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.05);
}}
.pill.accent {{
  background: #064e3b;
  color: #ffffff;
  border-color: #064e3b;
}}
.footer-bar {{
  position: absolute;
  bottom: 28px;
  left: 70px;
  right: 70px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 14px;
  border-top: 1.5px solid rgba(0, 0, 0, 0.08);
}}
.footer-author {{
  font-size: 16px;
  font-weight: 700;
  color: #1e293b;
  display: flex;
  align-items: center;
  gap: 8px;
}}
.footer-author span {{
  color: #15803d;
}}
.footer-tagline {{
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(0, 0, 0, 0.08);
  padding: 6px 18px;
  border-radius: 20px;
  font-size: 15px;
  font-weight: 700;
  color: #064e3b;
}}
</style>
</head>
<body>
<div class="canvas">
  <div class="top-bar">
    <div class="brand-badge">HEL訊TRICKBD • EDU</div>
    <div class="category-badge">Job Study Article</div>
  </div>

  <div class="center-container">
    <div class="topic-tag">
      <span>📌</span>
      <span>শিক্ষক নিবন্ধন পরীক্ষা ২০২৬ • NTRCA School Level</span>
    </div>

    <h1 class="banner-title">
      NTRCA স্কুল পর্যায় সহকারী শিক্ষক<br>পূর্ণাঙ্গ সিলেবাস ও মানবণ্টন ২০২৬
    </h1>

    <p class="banner-subtitle">
      সকল বিষয়ের লিখিত ও প্রিলিমিনারি সিলেবাস, ব্লুমস ট্যাক্সোনমি প্রশ্ন কাঠামো ও PDF গাইড
    </p>

    <div class="meta-pills">
      <div class="pill accent">⚡ প্রিলি ও লিখিত সিলেবাস</div>
      <div class="pill">📚 সকল বিষয় অন্তর্ভুক্ত</div>
      <div class="pill">📥 ফ্রি অফিসিয়াল PDF</div>
    </div>
  </div>

  <div class="footer-bar">
    <div class="footer-author">
      <span>✍️ উপস্থাপনায়:</span> ফারুক স্যার (মো. ওমর ফারুক), প্রতিষ্ঠাতা HelpTrickBD
    </div>
    <div class="footer-tagline">
      Learn Smart • Lead Future • Latest Edition 2026
    </div>
  </div>
</div>
</body>
</html>
"""

def generate_banner():
    # Fix brand badge text to exact English
    fixed_html = html_template.replace("HEL訊TRICKBD", "HELPTRICKBD")
    with open(TEMP_HTML, "w", encoding="utf-8") as f:
        f.write(fixed_html)

    cmd = [
        CHROME_PATH,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--window-size=1200,675",
        f"--screenshot={OUTPUT_PNG}",
        TEMP_HTML
    ]
    print("[*] Rendering banner via Chromium...")
    subprocess.run(cmd, check=True)

    # Crop/Resize exactly to 1200x675
    img = Image.open(OUTPUT_PNG)
    img = img.resize((1200, 675), Image.Resampling.LANCZOS)
    img.save(OUTPUT_PNG)

    # Compress to Target WebP (10-20 KB)
    print("[*] Compressing banner to WebP (10-20 KB)...")
    final_webp, size_kb = compress_to_target_webp(OUTPUT_PNG, OUTPUT_WEBP, target_min_kb=10.0, target_max_kb=20.0)
    print(f"[SUCCESS] Banner created at: {final_webp} ({size_kb:.1f} KB)")
    return final_webp

if __name__ == "__main__":
    generate_banner()
