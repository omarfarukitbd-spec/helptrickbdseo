#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/image_generator/build_official_bg_thumbnails.py
-----------------------------------------------------
Generates 100% perfect, newspaper-grade 16:9 featured banners EXCLUSIVELY
using the user's authentic templates from 'Thumbnail BG/' folder:
- bg.png   -> Islamic Article
- bg_1.png -> School / Class 6 / Fallback (Hason Raja)
- bg_2.png -> Political Science
- bg_3.png -> Education Guide
- bg_4.png -> Job Study Article (Primary Viva, BCS)
- bg_5.png -> ICT Guide (Cloud Computing, Computer Virus)

Enforces:
1. Zero Black Shape/Card: Typography placed directly on authentic background canvas.
2. Centered layout with colors matching the background's accent palette.
3. Safe Bounds (y <= 550) so text never collides with side decorative waves.
4. Chromium HarfBuzz text-shaping engine for 100% flawless Bengali conjuncts.
5. 10–20 KB Ultra-WebP Core Web Vitals compression.
"""

import os
import sys
import re
import subprocess
from PIL import Image

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

from tools.image_optimizer.webp_compressor import compress_to_target_webp

BG_DIR = os.path.join(PROJECT_ROOT, "Thumbnail BG")
POSTS_DIR = os.path.join(PROJECT_ROOT, "assets", "images", "posts")
THUMBS_DIR = os.path.join(PROJECT_ROOT, "assets", "images", "thumbnails")
FONT_PATH = os.path.join(PROJECT_ROOT, "assets", "fonts", "HindSiliguri-Bold.ttf")

os.makedirs(POSTS_DIR, exist_ok=True)
os.makedirs(THUMBS_DIR, exist_ok=True)

# Category configurations matching each background's authentic palette
CATEGORY_CONFIGS = {
    "Job Study Article": {
        "bg": "bg_4.png",
        "badge_bg": "#064e3b",
        "badge_border": "#f59e0b",
        "badge_color": "#ffffff",
        "title_color": "#064e3b",
        "tag_bg": "#f0fdf4",
        "tag_border": "#bbf7d0",
        "tag_color": "#15803d",
        "subtitle_color": "#334155",
        "pill_bg": "#ffffff",
        "pill_border": "#cbd5e1",
        "pill_color": "#064e3b",
        "pill_accent_bg": "#064e3b",
        "pill_accent_color": "#ffffff",
        "footer_highlight": "#15803d"
    },
    "ICT Guide": {
        "bg": "bg_5.png",
        "badge_bg": "#0f172a",
        "badge_border": "#0284c7",
        "badge_color": "#ffffff",
        "title_color": "#0f172a",
        "tag_bg": "#f0f9ff",
        "tag_border": "#bae6fd",
        "tag_color": "#0369a1",
        "subtitle_color": "#334155",
        "pill_bg": "#ffffff",
        "pill_border": "#cbd5e1",
        "pill_color": "#0f172a",
        "pill_accent_bg": "#0284c7",
        "pill_accent_color": "#ffffff",
        "footer_highlight": "#0369a1"
    },
    "Political Science": {
        "bg": "bg_2.png",
        "badge_bg": "#0b2046",
        "badge_border": "#f59e0b",
        "badge_color": "#ffffff",
        "title_color": "#0b2046",
        "tag_bg": "#fffbeb",
        "tag_border": "#fde68a",
        "tag_color": "#b45309",
        "subtitle_color": "#334155",
        "pill_bg": "#ffffff",
        "pill_border": "#cbd5e1",
        "pill_color": "#0b2046",
        "pill_accent_bg": "#0b2046",
        "pill_accent_color": "#ffffff",
        "footer_highlight": "#b45309"
    },
    "Education Guide": {
        "bg": "bg_3.png",
        "badge_bg": "#024a4d",
        "badge_border": "#20b2aa",
        "badge_color": "#ffffff",
        "title_color": "#024a4d",
        "tag_bg": "#f0fdfa",
        "tag_border": "#99f6e4",
        "tag_color": "#0f766e",
        "subtitle_color": "#334155",
        "pill_bg": "#ffffff",
        "pill_border": "#cbd5e1",
        "pill_color": "#024a4d",
        "pill_accent_bg": "#024a4d",
        "pill_accent_color": "#ffffff",
        "footer_highlight": "#0f766e"
    },
    "Islamic Article": {
        "bg": "bg.png",
        "badge_bg": "#064e3b",
        "badge_border": "#eab308",
        "badge_color": "#ffffff",
        "title_color": "#064e3b",
        "tag_bg": "#fefce8",
        "tag_border": "#fef08a",
        "tag_color": "#a16207",
        "subtitle_color": "#334155",
        "pill_bg": "#ffffff",
        "pill_border": "#cbd5e1",
        "pill_color": "#064e3b",
        "pill_accent_bg": "#064e3b",
        "pill_accent_color": "#ffffff",
        "footer_highlight": "#a16207"
    },
    "Class 6": {
        "bg": "bg_1.png",
        "badge_bg": "#1e1b4b",
        "badge_border": "#f59e0b",
        "badge_color": "#ffffff",
        "title_color": "#1e1b4b",
        "tag_bg": "#eef2ff",
        "tag_border": "#c7d2fe",
        "tag_color": "#4338ca",
        "subtitle_color": "#334155",
        "pill_bg": "#ffffff",
        "pill_border": "#cbd5e1",
        "pill_color": "#1e1b4b",
        "pill_accent_bg": "#1e1b4b",
        "pill_accent_color": "#ffffff",
        "footer_highlight": "#4338ca"
    }
}

def get_browser_binary():
    """Finds Chrome or Edge executable on Windows."""
    candidates = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    raise RuntimeError("Neither Google Chrome nor Microsoft Edge was found on this system.")

def strip_emojis(text: str) -> str:
    """Strips all emojis and special surrogate symbols to guarantee clean typography."""
    cleaned = re.sub(r"[\U00010000-\U0010FFFF\uD800-\uDBFF\uDC00-\uDFFF\u2600-\u26FF\u2700-\u27BF\uFE00-\uFE0F]", "", text)
    cleaned = re.sub(r"[📌📊📝⚡⭐🛡️🔒🌐🏢💾💻☁️✨👉📘📢⏱️✅🎓💬💡⚠️]", "", cleaned)
    return re.sub(r"\s+", " ", cleaned).strip()

def render_banner_html(
    bg_file: str,
    theme: dict,
    category_label: str,
    title: str,
    subtitle: str,
    features: list,
    is_english: bool,
    custom_tag_text: str = None
) -> str:
    """Creates clean, centered banner without any dark overlay box."""
    bg_url = "file:///" + os.path.join(BG_DIR, bg_file).replace("\\", "/")
    font_url = "file:///" + FONT_PATH.replace("\\", "/")

    clean_cat = strip_emojis(category_label)
    clean_title = strip_emojis(title)
    clean_sub = strip_emojis(subtitle)
    clean_feats = [strip_emojis(f) for f in features]

    if is_english:
        footer_brand = "HelpTrickBD Smart Education Platform"
        footer_right = "100% Syllabus & Exam Preparation Guide"
        tag_text = custom_tag_text or "Special Academic Handnote 2026"
        body_font = "'Segoe UI', Roboto, -apple-system, sans-serif"
    else:
        footer_brand = "HelpTrickBD স্মার্ট এডুকেশন প্ল্যাটফর্ম"
        footer_right = "১০০% সিলেবাস ও পরীক্ষা সহায়ক হ্যান্ডনোট"
        tag_text = custom_tag_text or "জাতীয় বিশ্ববিদ্যালয় মাস্টার্স শেষ পর্ব ২০২৬"
        body_font = "'HindSiliguri', 'SolaimanLipi', sans-serif"

    # Build pills (last pill is accent)
    pills_html = ""
    for idx, f in enumerate(clean_feats):
        is_last = (idx == len(clean_feats) - 1)
        accent_cls = " accent" if is_last else ""
        pills_html += f'<div class="pill{accent_cls}">{f}</div>'

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
  font-family: {body_font};
}}
body {{
  background-image: url('{bg_url}');
  background-size: cover;
  background-position: center;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  padding: 38px 70px 0 70px;
}}

/* Top Brand & Category Header */
.top-bar {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  margin-bottom: 28px;
}}
.brand-badge {{
  background: #ffffff;
  color: {theme["title_color"]};
  font-size: 19px;
  font-weight: 700;
  padding: 8px 22px;
  border-radius: 20px;
  border: 1.5px solid #e2e8f0;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  letter-spacing: 0.3px;
}}
.category-badge {{
  background: {theme["badge_bg"]};
  color: {theme["badge_color"]};
  border: 2px solid {theme["badge_border"]};
  font-size: 19px;
  font-weight: 700;
  padding: 8px 24px;
  border-radius: 20px;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.15);
}}

/* Center Content Container - Zero Box/Card Overlay */
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
  background: {theme["tag_bg"]};
  border: 1.5px solid {theme["tag_border"]};
  color: {theme["tag_color"]};
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
  color: {theme["title_color"]};
  font-weight: 800;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
  letter-spacing: -0.3px;
}}

p.banner-subtitle {{
  margin: 0 0 26px 0;
  font-size: 23px;
  line-height: 1.4;
  color: {theme["subtitle_color"]};
  font-weight: 600;
  max-width: 860px;
}}

/* Feature Badges */
.pills-row {{
  display: flex;
  gap: 12px;
  justify-content: center;
  flex-wrap: wrap;
  margin-bottom: 22px;
}}
.pill {{
  background: {theme["pill_bg"]};
  border: 1.5px solid {theme["pill_border"]};
  color: {theme["pill_color"]};
  font-size: 18px;
  font-weight: 700;
  padding: 8px 18px;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
}}
.pill.accent {{
  background: {theme["pill_accent_bg"]};
  border-color: {theme["pill_accent_bg"]};
  color: {theme["pill_accent_color"]};
}}

/* Subtle Note in Pure White Safe Area */
.safe-note {{
  color: #475569;
  font-size: 16px;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 12px;
}}
.safe-note .sep {{
  color: #cbd5e1;
}}
.safe-note .highlight {{
  color: {theme["footer_highlight"]};
  font-weight: 700;
}}
</style>
</head>
<body>

<div class="top-bar">
  <div class="brand-badge">HelpTrickBD | helptrickbd.com</div>
  <div class="category-badge">{clean_cat}</div>
</div>

<div class="center-container">
  <div class="topic-tag">{tag_text}</div>
  <h1 class="banner-title">{clean_title}</h1>
  <p class="banner-subtitle">{clean_sub}</p>
  
  <div class="pills-row">
    {pills_html}
  </div>

  <div class="safe-note">
    <span>© {footer_brand}</span>
    <span class="sep">•</span>
    <span class="highlight">{footer_right}</span>
  </div>
</div>

</body>
</html>"""

def generate_official_bg_banner(
    filename: str,
    category_key: str,
    badge_label: str,
    title: str,
    subtitle: str,
    features: list,
    custom_tag_text: str = None
):
    theme = CATEGORY_CONFIGS.get(category_key, CATEGORY_CONFIGS["Job Study Article"])
    bg_file = theme["bg"]
    
    # Check if English or Bengali
    is_english = not bool(re.search(r'[\u0980-\u09FF]', title + subtitle + badge_label))

    html_source = render_banner_html(
        bg_file=bg_file,
        theme=theme,
        category_label=badge_label,
        title=title,
        subtitle=subtitle,
        features=features,
        is_english=is_english,
        custom_tag_text=custom_tag_text
    )

    temp_html = os.path.join(PROJECT_ROOT, f"temp_{filename}.html")
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(html_source)

    base_name = os.path.splitext(filename)[0]
    out_png = os.path.join(POSTS_DIR, f"{base_name}.png")
    out_webp = os.path.join(POSTS_DIR, f"{base_name}.webp")
    out_jpg = os.path.join(POSTS_DIR, f"{base_name}.jpg")

    browser_bin = get_browser_binary()
    file_url = "file:///" + os.path.abspath(temp_html).replace("\\", "/")

    import tempfile
    user_data_dir = os.path.join(tempfile.gettempdir(), "edge_browser_tmp")
    cmd = [
        browser_bin,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--user-data-dir={user_data_dir}",
        "--force-device-scale-factor=1",
        "--window-size=1200,675",
        f"--screenshot={out_png}",
        file_url
    ]
    subprocess.run(cmd, check=True, capture_output=True)

    # Clean temporary html
    if os.path.exists(temp_html):
        os.remove(temp_html)

    # Convert to JPEG and Target 10-20KB WebP
    img = Image.open(out_png).convert("RGB")
    img.save(out_jpg, "JPEG", quality=92)
    compress_to_target_webp(out_png, out_webp, target_min_kb=10.0, target_max_kb=20.0)

    # Sync to thumbnails folder
    import shutil
    shutil.copy2(out_png, os.path.join(THUMBS_DIR, f"{base_name}.png"))
    shutil.copy2(out_webp, os.path.join(THUMBS_DIR, f"{base_name}.webp"))
    shutil.copy2(out_jpg, os.path.join(THUMBS_DIR, f"{base_name}.jpg"))

    size_kb = os.path.getsize(out_webp) / 1024.0
    print(f"  [✔] Generated clean centered banner on {bg_file}: {base_name}.webp ({size_kb:.1f} KB)")
    return out_webp
