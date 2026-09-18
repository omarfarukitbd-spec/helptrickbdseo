#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/image_generator/batch_synthesize_87_thumbnails.py
-------------------------------------------------------
Synthesizes 87 official 16:9 featured banners using Chromium HarfBuzz engine
and compresses them to 10-20 KB WebP, mapped to authentic Thumbnail BG/ templates:
- bg.png   -> Islamic Article
- bg_2.png -> Political Science
- bg_3.png -> Education Guide
- bg_4.png -> Job Study Article
- bg_5.png -> ICT Guide
- bg_8.png -> International Affairs
"""

import os
import sys
import re
import json
import subprocess
from PIL import Image

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

BG_DIR = os.path.join(PROJECT_ROOT, "Thumbnail BG")
POSTS_DIR = os.path.join(PROJECT_ROOT, "assets", "images", "posts")
PLAN_FILE = os.path.join(PROJECT_ROOT, "scratch", "batch_thumbnail_plan.json")
TEMP_DIR = os.path.join(PROJECT_ROOT, "scratch", "temp_render")

os.makedirs(POSTS_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
if not os.path.exists(CHROME_PATH):
    CHROME_PATH = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
if not os.path.exists(CHROME_PATH):
    CHROME_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

CATEGORY_PALETTES = {
    "Islamic Article": {
        "badge_bg": "#064e3b", "badge_border": "#eab308", "badge_color": "#ffffff",
        "title_color": "#064e3b", "tag_bg": "#fefce8", "tag_border": "#fef08a", "tag_color": "#a16207",
        "subtitle_color": "#334155", "pill_bg": "#ffffff", "pill_border": "#cbd5e1", "pill_color": "#064e3b",
        "pill_accent_bg": "#064e3b", "pill_accent_color": "#ffffff", "category_bn": "ইসলামিক প্রবন্ধ"
    },
    "Political Science": {
        "badge_bg": "#0b2046", "badge_border": "#f59e0b", "badge_color": "#ffffff",
        "title_color": "#0b2046", "tag_bg": "#fffbeb", "tag_border": "#fde68a", "tag_color": "#b45309",
        "subtitle_color": "#334155", "pill_bg": "#ffffff", "pill_border": "#cbd5e1", "pill_color": "#0b2046",
        "pill_accent_bg": "#0b2046", "pill_accent_color": "#ffffff", "category_bn": "রাষ্ট্রবিজ্ঞান স্পেশাল"
    },
    "Education Guide": {
        "badge_bg": "#024a4d", "badge_border": "#20b2aa", "badge_color": "#ffffff",
        "title_color": "#024a4d", "tag_bg": "#f0fdfa", "tag_border": "#99f6e4", "tag_color": "#0f766e",
        "subtitle_color": "#334155", "pill_bg": "#ffffff", "pill_border": "#cbd5e1", "pill_color": "#024a4d",
        "pill_accent_bg": "#024a4d", "pill_accent_color": "#ffffff", "category_bn": "শিক্ষা গাইড ও সাজেশন"
    },
    "Job Study Article": {
        "badge_bg": "#064e3b", "badge_border": "#f59e0b", "badge_color": "#ffffff",
        "title_color": "#064e3b", "tag_bg": "#f0fdf4", "tag_border": "#bbf7d0", "tag_color": "#15803d",
        "subtitle_color": "#334155", "pill_bg": "#ffffff", "pill_border": "#cbd5e1", "pill_color": "#064e3b",
        "pill_accent_bg": "#064e3b", "pill_accent_color": "#ffffff", "category_bn": "চাকরির প্রস্তুতি"
    },
    "ICT Guide": {
        "badge_bg": "#0f172a", "badge_border": "#0284c7", "badge_color": "#ffffff",
        "title_color": "#0f172a", "tag_bg": "#f0f9ff", "tag_border": "#bae6fd", "tag_color": "#0369a1",
        "subtitle_color": "#334155", "pill_bg": "#ffffff", "pill_border": "#cbd5e1", "pill_color": "#0f172a",
        "pill_accent_bg": "#0284c7", "pill_accent_color": "#ffffff", "category_bn": "তথ্যপ্রযুক্তি ও কম্পিউটার"
    },
    "International Affairs": {
        "badge_bg": "#0f172a", "badge_border": "#eab308", "badge_color": "#ffffff",
        "title_color": "#0f172a", "tag_bg": "#fefce8", "tag_border": "#fef08a", "tag_color": "#a16207",
        "subtitle_color": "#334155", "pill_bg": "#ffffff", "pill_border": "#cbd5e1", "pill_color": "#0f172a",
        "pill_accent_bg": "#0f172a", "pill_accent_color": "#ffffff", "category_bn": "আন্তর্জাতিক বিষয়াবলি"
    }
}

def clean_title(title):
    # Remove pipes or trailing dashes
    t = re.sub(r'\|.*$', '', title).strip()
    t = re.sub(r'—.*$', '', t).strip()
    return t

def slugify(title):
    # Create clean english transliteration or hash slug
    slug = re.sub(r'[^\w\s-]', '', title.lower())
    slug = re.sub(r'[\s_]+', '-', slug).strip()
    if len(slug) < 3:
        import hashlib
        slug = "post-" + hashlib.md5(title.encode('utf-8')).hexdigest()[:10]
    return slug[:45]

with open(PLAN_FILE, "r", encoding="utf-8") as f:
    plan = json.load(f)

print(f"Total posts to synthesize: {len(plan)}")

manifest_out = []

for idx, item in enumerate(plan, start=1):
    pid = item["id"]
    full_title = item["title"]
    cat = item["assigned_category"]
    bg_name = item["assigned_bg"]
    
    t_cfg = CATEGORY_PALETTES.get(cat, CATEGORY_PALETTES["Political Science"])
    
    # Clean display title
    display_title = clean_title(full_title)
    if len(display_title) > 55:
        display_title = display_title[:52] + "..."
        
    # Generate subhook
    if cat == "Islamic Article":
        tag = "কুরআন ও সুন্নাহর আলোকে"
        subtitle = "বিশুদ্ধ দলিল, ঐতিহাসিক প্রেক্ষাপট ও পূর্ণাঙ্গ জীবনবিধান নির্দেশনা"
        pills = ["সহিহ দলিল", "বাস্তব আমল", "১০০% প্রামাণ্য", "লেটেস্ট সংস্করণ ২০২৬"]
    elif cat == "Political Science":
        tag = "মাস্টার্স ও অনার্স বিশেষ লেকচার"
        subtitle = "পরীক্ষার কমন উপযোগী সম্পূর্ণ তাত্ত্বিক ব্যাখ্যা ও পয়েন্টভিত্তিক হ্যান্ডনোট"
        pills = ["মাস্টার হ্যান্ডনোট", "বোর্ড প্রশ্ন সমাধান", "পয়েন্টভিত্তিক নোট", "লেটেস্ট সংস্করণ ২০২৬"]
    elif cat == "Education Guide":
        tag = "বোর্ড পরীক্ষা প্রস্তুতি"
        subtitle = "পরীক্ষার্থীদের জন্য নির্ভরযোগ্য অধ্যায়ভিত্তিক গাইড ও মডেল সমাধান"
        pills = ["গোল্ডেন সাজেশন", "১০০% কমন উপযোগী", "শর্টকাট কৌশল", "লেটেস্ট সংস্করণ ২০২৬"]
    elif cat == "Job Study Article":
        tag = "বিসিএস ও সরকারি চাকরি প্রস্তুতি"
        subtitle = "প্রিলিমিনারি ও ভাইভা পরীক্ষার সর্বাধিক কমন উপযোগী প্রশ্নব্যাংক"
        pills = ["বিসিএস প্রিলি", "ভাইভা গাইড", "শর্টকাট ট্রিকস", "লেটেস্ট সংস্করণ ২০২৬"]
    elif cat == "ICT Guide":
        tag = "প্র্যাকটিক্যাল কম্পিউটার গাইড"
        subtitle = "সহজ বাংলা ভাষায় বাস্তবমুখী প্রযুক্তি টিউটোরিয়াল ও ব্যবহারিক সমাধান"
        pills = ["সহজ টেকনিক", "স্টেপ-বাই-স্টেপ", "আইসিটি স্পেশাল", "লেটেস্ট সংস্করণ ২০২৬"]
    else:
        tag = "আন্তর্জাতিক রাজনীতি ও কূটনীতি"
        subtitle = "বৈশ্বিক পরাশক্তি দ্বন্দ্ব ও সাম্প্রতিক চুক্তি বিশ্লেষণ সহায়িকা"
        pills = ["আন্তর্জাতিক তথ্য", "বিসিএস প্রস্তুতি", "বিশ্লেষণধর্মী", "লেটেস্ট সংস্করণ ২০২৬"]

    # Image filename
    filename = f"htbd-official-{pid}.webp"
    webp_path = os.path.join(POSTS_DIR, filename)
    png_path = os.path.join(TEMP_DIR, f"{pid}.png")
    bg_path = os.path.join(BG_DIR, bg_name).replace("\\", "/")
    
    pills_html = f'<div class="pill pill-accent">{pills[0]}</div>'
    for p in pills[1:]:
        pills_html += f'<div class="pill">{p}</div>'
        
    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@500;600;700;800&family=Inter:wght@600;700;800&display=swap');
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  width: 1200px;
  height: 675px;
  overflow: hidden;
  font-family: 'Hind Siliguri', sans-serif;
  background-image: url('file:///{bg_path}');
  background-size: cover;
  background-position: center;
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
  color: {t_cfg["title_color"]};
  font-size: 19px;
  font-weight: 700;
  padding: 8px 22px;
  border-radius: 20px;
  border: 1.5px solid #e2e8f0;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}}
.category-badge {{
  background: {t_cfg["badge_bg"]};
  color: {t_cfg["badge_color"]};
  border: 2px solid {t_cfg["badge_border"]};
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
  background: {t_cfg["tag_bg"]};
  border: 1.5px solid {t_cfg["tag_border"]};
  color: {t_cfg["tag_color"]};
  font-size: 20px;
  font-weight: 700;
  padding: 6px 22px;
  border-radius: 16px;
  margin-bottom: 14px;
}}
h1.banner-title {{
  margin: 0 0 14px 0;
  font-size: 47px;
  line-height: 1.25;
  color: {t_cfg["title_color"]};
  font-weight: 800;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
}}
p.banner-subtitle {{
  margin: 0 0 26px 0;
  font-size: 23px;
  line-height: 1.4;
  color: {t_cfg["subtitle_color"]};
  font-weight: 600;
  max-width: 860px;
}}
.pills-row {{
  display: flex;
  gap: 12px;
  justify-content: center;
  flex-wrap: wrap;
  margin-bottom: 22px;
}}
.pill {{
  background: {t_cfg["pill_bg"]};
  border: 1.5px solid {t_cfg["pill_border"]};
  color: {t_cfg["pill_color"]};
  font-size: 18px;
  font-weight: 700;
  padding: 7px 20px;
  border-radius: 14px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}}
.pill-accent {{
  background: {t_cfg["pill_accent_bg"]};
  color: {t_cfg["pill_accent_color"]};
  border-color: {t_cfg["pill_accent_bg"]};
}}
.footer-bar {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  margin-top: auto;
  padding-bottom: 24px;
}}
.author-pill {{
  background: rgba(255, 255, 255, 0.9);
  padding: 6px 18px;
  border-radius: 12px;
  border: 1px solid #cbd5e1;
  font-size: 16px;
  font-weight: 700;
  color: #334155;
}}
.brand-pill {{
  background: rgba(255, 255, 255, 0.9);
  padding: 6px 18px;
  border-radius: 12px;
  border: 1px solid #cbd5e1;
  font-size: 15px;
  font-family: 'Inter', sans-serif;
  font-weight: 700;
  color: {t_cfg["title_color"]};
}}
</style>
</head>
<body>
<div class="top-bar">
  <div class="brand-badge">HelpTrickBD • Education</div>
  <div class="category-badge">{t_cfg["category_bn"]}</div>
</div>
<div class="center-container">
  <div class="topic-tag">{tag}</div>
  <h1 class="banner-title">{display_title}</h1>
  <p class="banner-subtitle">{subtitle}</p>
  <div class="pills-row">
    {pills_html}
  </div>
</div>
<div class="footer-bar">
  <div class="author-pill">লেখক: হেল্পট্রিকবিডি এক্সপার্ট প্যানেল</div>
  <div class="brand-pill">Learn Smart • Lead Future • Latest Edition 2026</div>
</div>
</body>
</html>"""

    temp_html = os.path.join(TEMP_DIR, f"{pid}.html")
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(html)
        
    cmd = [
        CHROME_PATH,
        "--headless",
        "--disable-gpu",
        "--force-device-scale-factor=1",
        "--window-size=1200,675",
        f"--screenshot={png_path}",
        temp_html
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    
    # Compress PNG to target WebP (10-20 KB)
    im = Image.open(png_path).convert("RGB")
    im.save(webp_path, "WEBP", quality=75, method=6)
    
    sz_kb = os.path.getsize(webp_path) / 1024
    cdn_url = f"https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/{filename}"
    
    manifest_out.append({
        "num": idx,
        "id": pid,
        "title": full_title,
        "display_title": display_title,
        "category": cat,
        "bg": bg_name,
        "filename": filename,
        "size_kb": round(sz_kb, 1),
        "cdn_url": cdn_url
    })
    
    if idx % 10 == 0 or idx == len(plan):
        print(f"Synthesized {idx}/{len(plan)} banners (Latest: {filename}, {sz_kb:.1f} KB)")

# Clean up temp html and pngs
import shutil
shutil.rmtree(TEMP_DIR, ignore_errors=True)

manifest_file = os.path.join(PROJECT_ROOT, "scratch", "synthesized_87_manifest.json")
with open(manifest_file, "w", encoding="utf-8") as f:
    json.dump(manifest_out, f, ensure_ascii=False, indent=2)

print(f"\n[OK] All {len(manifest_out)} thumbnails synthesized and compressed successfully in assets/images/posts/!")
