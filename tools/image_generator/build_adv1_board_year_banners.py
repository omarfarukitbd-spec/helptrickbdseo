#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/image_generator/build_adv1_board_year_banners.py
------------------------------------------------------
Generates 6 dedicated, high-contrast, professional 16:9 thumbnails (1200x675)
for each year of Advanced Accounting-1 Board Questions (2019 to 2024).

Features:
- Official National University (NU) logo embedded
- Download PDF logo / badge embedded
- Official HelpTrickBD logo embedded
- Authentic 'Thumbnail BG/bg_3.png' template
- Clean Bengali typography (HindSiliguri Bold)
- Headless Chromium/Edge HarfBuzz rendering for perfect conjuncts
- 12-20 KB WebP compression for Core Web Vitals
"""

import os
import sys
import subprocess
import tempfile
import shutil

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.image_optimizer.webp_compressor import compress_to_target_webp

BG_PATH = os.path.join(PROJECT_ROOT, "Thumbnail BG", "bg_3.png")
NU_LOGO_PATH = os.path.join(PROJECT_ROOT, "assets", "images", "logo", "nu_logo.png")
HTBD_LOGO_PATH = os.path.join(PROJECT_ROOT, "assets", "images", "logo", "helptrickbd_logo.png")
FONT_PATH = os.path.join(PROJECT_ROOT, "assets", "fonts", "HindSiliguri-Bold.ttf")

OUTPUT_DIR = os.path.join(PROJECT_ROOT, "assets", "images", "thumbnails")
os.makedirs(OUTPUT_DIR, exist_ok=True)

YEAR_BN_MAP = {
    "2024": "২০২৪",
    "2023": "২০২৩",
    "2022": "২০২২",
    "2021": "২০২১",
    "2020": "২০২০",
    "2019": "২০১৯"
}

def get_browser_binary():
    candidates = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    raise RuntimeError("Browser not found.")

def render_year_html(year_en: str, year_bn: str) -> str:
    bg_url = "file:///" + BG_PATH.replace("\\", "/")
    nu_logo_url = "file:///" + NU_LOGO_PATH.replace("\\", "/")
    htbd_logo_url = "file:///" + HTBD_LOGO_PATH.replace("\\", "/")
    font_url = "file:///" + FONT_PATH.replace("\\", "/")
    
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@font-face {{
  font-family: 'HindSiliguri';
  src: url('{font_url}');
  font-weight: bold;
}}
* {{
  box-sizing: border-box;
}}
html, body {{
  margin: 0;
  padding: 0;
  width: 1200px;
  height: 675px;
  overflow: hidden;
  font-family: 'HindSiliguri', sans-serif;
}}
body {{
  background-image: url('{bg_url}');
  background-size: cover;
  background-position: center;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 34px 60px 28px 60px;
}}

/* Top Header Bar */
.top-bar {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
}}
.brand-box {{
  display: flex;
  align-items: center;
  gap: 12px;
  background: #ffffff;
  padding: 8px 20px;
  border-radius: 14px;
  border: 1.5px solid #e2e8f0;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.08);
}}
.brand-logo {{
  height: 38px;
  width: auto;
  display: block;
}}

.nu-badge {{
  display: flex;
  align-items: center;
  gap: 12px;
  background: linear-gradient(135deg, #024a4d 0%, #065f46 100%);
  color: #ffffff;
  padding: 8px 22px;
  border-radius: 14px;
  border: 2px solid #20b2aa;
  box-shadow: 0 4px 16px rgba(2, 74, 77, 0.25);
  font-size: 18px;
  font-weight: 700;
  letter-spacing: 0.3px;
}}
.nu-crest {{
  height: 36px;
  width: auto;
  filter: drop-shadow(0 2px 4px rgba(0,0,0,0.3));
}}

.pdf-badge {{
  display: flex;
  align-items: center;
  gap: 8px;
  background: #ffffff;
  border: 2px solid #dc2626;
  color: #991b1b;
  padding: 7px 18px;
  border-radius: 14px;
  font-size: 16.5px;
  font-weight: 800;
  box-shadow: 0 4px 12px rgba(220, 38, 38, 0.15);
}}
.pdf-icon-tag {{
  background: #dc2626;
  color: #ffffff;
  padding: 3px 8px;
  border-radius: 6px;
  font-size: 13.5px;
  font-weight: 900;
  letter-spacing: 0.5px;
}}

/* Center Content */
.center-container {{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  width: 100%;
  margin: auto 0;
}}

.topic-tag {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: #f0fdfa;
  border: 1.5px solid #99f6e4;
  color: #0f766e;
  font-size: 21px;
  font-weight: 700;
  padding: 6px 26px;
  border-radius: 30px;
  margin-bottom: 12px;
  box-shadow: 0 2px 8px rgba(15, 118, 110, 0.08);
}}

h1.banner-title {{
  margin: 0 0 10px 0;
  font-size: 52px;
  line-height: 1.22;
  color: #02383b;
  font-weight: 800;
  text-shadow: 0 2px 6px rgba(0, 0, 0, 0.08);
  letter-spacing: -0.5px;
}}

.highlight-year {{
  color: #b45309;
  background: #fef3c7;
  padding: 2px 14px;
  border-radius: 12px;
  border: 1.5px solid #fde68a;
  display: inline-block;
}}

p.banner-subtitle {{
  margin: 0 0 22px 0;
  font-size: 24px;
  line-height: 1.35;
  color: #334155;
  font-weight: 700;
  font-family: 'Segoe UI', Roboto, sans-serif;
}}

/* Pills */
.pills-row {{
  display: flex;
  justify-content: center;
  gap: 14px;
  width: 100%;
}}
.pill {{
  background: #ffffff;
  border: 1.5px solid #cbd5e1;
  color: #024a4d;
  font-size: 19px;
  font-weight: 700;
  padding: 9px 20px;
  border-radius: 12px;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.06);
}}
.pill.accent {{
  background: linear-gradient(135deg, #024a4d 0%, #065f46 100%);
  border-color: #20b2aa;
  color: #ffffff;
  box-shadow: 0 4px 14px rgba(2, 74, 77, 0.25);
}}
.pill.gold {{
  background: linear-gradient(135deg, #d97706 0%, #b45309 100%);
  border-color: #f59e0b;
  color: #ffffff;
  box-shadow: 0 4px 14px rgba(180, 83, 9, 0.25);
}}

/* Footer */
.footer-bar {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  padding-top: 10px;
}}
.footer-left {{
  font-size: 16px;
  color: #0f766e;
  font-weight: 700;
}}
.footer-pill {{
  background: rgba(255, 255, 255, 0.92);
  border: 1px solid #cbd5e1;
  color: #024a4d;
  font-family: 'Segoe UI', Roboto, sans-serif;
  font-size: 15px;
  font-weight: 700;
  padding: 6px 18px;
  border-radius: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}}
</style>
</head>
<body>

  <!-- Top Bar -->
  <div class="top-bar">
    <div class="brand-box">
      <img src="{htbd_logo_url}" class="brand-logo" alt="HelpTrickBD" />
    </div>
    <div class="nu-badge">
      <img src="{nu_logo_url}" class="nu-crest" alt="National University" />
      <span>জাতীয় বিশ্ববিদ্যালয় • BBA অনার্স ৩য় বর্ষ</span>
    </div>
    <div class="pdf-badge">
      <span class="pdf-icon-tag">PDF</span>
      <span>Download Included</span>
    </div>
  </div>

  <!-- Center Content -->
  <div class="center-container">
    <div class="topic-tag">
      হিসাববিজ্ঞান বিভাগ • কোর্স কোড: ২৩২৫০৩ • চূড়ান্ত বোর্ড প্রশ্ন
    </div>

    <h1 class="banner-title">
      প্রশ্নব্যাংক <span class="highlight-year">{year_bn}</span>: উন্নত হিসাববিজ্ঞান ১
    </h1>

    <p class="banner-subtitle">
      Advanced Accounting-1 Solution {year_en} (Complete Solution Guide)
    </p>

    <div class="pills-row">
      <div class="pill">ক-বিভাগ (১২টি প্রশ্ন)</div>
      <div class="pill">খ-বিভাগ (৮টি প্রশ্ন)</div>
      <div class="pill accent">গ-বিভাগ (৮টি বিশদ সমাধান)</div>
      <div class="pill gold">১০০% নির্ভুল সমাধান PDF</div>
    </div>
  </div>

  <!-- Footer Bar -->
  <div class="footer-bar">
    <div class="footer-left">HelpTrickBD স্মার্ট অ্যাকাডেমিক প্রকাশনা • helptrickbd.com</div>
    <div class="footer-pill">Learn Smart • Lead Future • Latest Edition 2026</div>
  </div>

</body>
</html>"""

def generate_all_year_banners():
    browser_bin = get_browser_binary()
    print(f"[*] Using browser: {browser_bin}")
    
    generated_assets = {}
    
    for yr_en, yr_bn in YEAR_BN_MAP.items():
        base_name = f"adv_accounting_1_board_{yr_en}"
        png_path = os.path.join(OUTPUT_DIR, f"{base_name}.png")
        webp_path = os.path.join(OUTPUT_DIR, f"{base_name}.webp")
        
        print(f"\n[*] Generating banner for Year {yr_en} ({yr_bn})...")
        html_code = render_year_html(yr_en, yr_bn)
        
        with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as tf:
            tf.write(html_code)
            temp_html = tf.name
            
        try:
            cmd = [
                browser_bin,
                "--headless=new",
                "--disable-gpu",
                "--hide-scrollbars",
                "--force-device-scale-factor=1",
                "--window-size=1200,675",
                f"--screenshot={png_path}",
                temp_html
            ]
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"    PNG rendered: {png_path} ({os.path.getsize(png_path)} bytes)")
            
            compress_to_target_webp(
                input_path=png_path,
                output_path=webp_path,
                target_min_kb=12,
                target_max_kb=24
            )
            print(f"    WebP created: {webp_path} ({os.path.getsize(webp_path)} bytes)")
            generated_assets[yr_en] = {
                "png": png_path,
                "webp": webp_path
            }
        finally:
            if os.path.exists(temp_html):
                os.remove(temp_html)
                
    print(f"\n[SUCCESS] All 6 banners generated successfully!")
    return generated_assets

if __name__ == "__main__":
    generate_all_year_banners()
