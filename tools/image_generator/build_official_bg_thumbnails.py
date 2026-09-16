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
1. Mandatory usage of official 'Thumbnail BG/' background images
2. 100% Zero-Emoji policy (zero tofu boxes)
3. Chromium HarfBuzz text-shaping engine for 100% flawless Bengali conjuncts
4. Strict Rule 8 Bilingual Governance (100% English for English posts, 100% Bengali for Bengali posts)
5. 10–20 KB Ultra-WebP Core Web Vitals compression
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

# Category configurations with tailored frosted cards and colors
CATEGORY_CONFIGS = {
    "Job Study Article": {
        "bg": "bg_4.png",
        "badge_bg": "#064e3b",
        "badge_border": "#f59e0b",
        "badge_color": "#ffffff",
        "card_bg": "rgba(10, 24, 20, 0.88)",
        "card_border": "rgba(245, 158, 11, 0.5)",
        "accent": "#fbbf24",
        "pill_bg": "rgba(255, 255, 255, 0.12)",
        "pill_border": "rgba(255, 255, 255, 0.25)"
    },
    "ICT Guide": {
        "bg": "bg_5.png",
        "badge_bg": "#0f172a",
        "badge_border": "#38bdf8",
        "badge_color": "#ffffff",
        "card_bg": "rgba(11, 19, 38, 0.88)",
        "card_border": "rgba(56, 189, 248, 0.45)",
        "accent": "#38bdf8",
        "pill_bg": "rgba(56, 189, 248, 0.12)",
        "pill_border": "rgba(56, 189, 248, 0.35)"
    },
    "Political Science": {
        "bg": "bg_2.png",
        "badge_bg": "#0c2340",
        "badge_border": "#d4af37",
        "badge_color": "#ffffff",
        "card_bg": "rgba(10, 18, 32, 0.88)",
        "card_border": "rgba(212, 175, 55, 0.5)",
        "accent": "#f3ba2f",
        "pill_bg": "rgba(255, 255, 255, 0.12)",
        "pill_border": "rgba(255, 255, 255, 0.25)"
    },
    "Education Guide": {
        "bg": "bg_3.png",
        "badge_bg": "#024a4d",
        "badge_border": "#20b2aa",
        "badge_color": "#ffffff",
        "card_bg": "rgba(8, 28, 30, 0.88)",
        "card_border": "rgba(32, 178, 170, 0.45)",
        "accent": "#2dd4bf",
        "pill_bg": "rgba(255, 255, 255, 0.12)",
        "pill_border": "rgba(255, 255, 255, 0.25)"
    },
    "Islamic Article": {
        "bg": "bg.png",
        "badge_bg": "#064e3b",
        "badge_border": "#eab308",
        "badge_color": "#ffffff",
        "card_bg": "rgba(8, 28, 18, 0.88)",
        "card_border": "rgba(234, 179, 8, 0.5)",
        "accent": "#facc15",
        "pill_bg": "rgba(255, 255, 255, 0.12)",
        "pill_border": "rgba(255, 255, 255, 0.25)"
    },
    "Class 6": {
        "bg": "bg_1.png",
        "badge_bg": "#1e1b4b",
        "badge_border": "#f59e0b",
        "badge_color": "#ffffff",
        "card_bg": "rgba(15, 23, 42, 0.88)",
        "card_border": "rgba(99, 102, 241, 0.45)",
        "accent": "#fbbf24",
        "pill_bg": "rgba(255, 255, 255, 0.12)",
        "pill_border": "rgba(255, 255, 255, 0.25)"
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
    is_english: bool
) -> str:
    """Creates pixel-perfect 1200x675 HTML card composited on official Thumbnail BG/."""
    bg_url = "file:///" + os.path.join(BG_DIR, bg_file).replace("\\", "/")
    font_url = "file:///" + FONT_PATH.replace("\\", "/")

    clean_cat = strip_emojis(category_label)
    clean_title = strip_emojis(title)
    clean_sub = strip_emojis(subtitle)
    clean_feats = [strip_emojis(f) for f in features]

    if is_english:
        footer_left = "© HelpTrickBD Smart Education Platform | All Rights Reserved 2026"
        footer_right = "100% Syllabus & Exam Preparation Guide"
        body_font = "'Segoe UI', Roboto, -apple-system, sans-serif"
    else:
        footer_left = "© HelpTrickBD স্মার্ট এডুকেশন প্ল্যাটফর্ম | সর্বস্বত্ব সংরক্ষিত ২০২৬"
        footer_right = "১০০% সিলেবাস ও পরীক্ষা সহায়ক"
        body_font = "'HindSiliguri', 'SolaimanLipi', sans-serif"

    pills_html = "".join([
        f'<div class="pill">{f}</div>' for f in clean_feats
    ])

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
  justify-content: space-between;
  padding: 44px 56px;
}}
.top-bar {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
}}
.brand-badge {{
  background: rgba(255, 255, 255, 0.95);
  color: #0f172a;
  font-size: 21px;
  font-weight: 700;
  padding: 10px 24px;
  border-radius: 24px;
  border: 1px solid rgba(0, 0, 0, 0.12);
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.1);
  letter-spacing: 0.3px;
}}
.category-badge {{
  background: {theme["badge_bg"]};
  color: {theme["badge_color"]};
  border: 2px solid {theme["badge_border"]};
  font-size: 21px;
  font-weight: 700;
  padding: 10px 24px;
  border-radius: 24px;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.2);
}}
.main-card {{
  width: 100%;
  height: 440px;
  background: {theme["card_bg"]};
  border: 2px solid {theme["card_border"]};
  border-radius: 20px;
  padding: 38px 44px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  box-shadow: 0 16px 36px rgba(0, 0, 0, 0.4);
}}
.card-content {{
  display: flex;
  flex-direction: column;
  gap: 14px;
}}
h1 {{
  margin: 0;
  font-size: 48px;
  line-height: 1.25;
  color: #ffffff;
  font-weight: 700;
  text-shadow: 0 3px 8px rgba(0, 0, 0, 0.6);
}}
.subtitle {{
  margin: 0;
  font-size: 25px;
  line-height: 1.35;
  color: #bae6fd;
  font-weight: 400;
  text-shadow: 0 2px 6px rgba(0, 0, 0, 0.5);
}}
.pills-container {{
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
}}
.pill {{
  background: {theme["pill_bg"]};
  border: 1.5px solid {theme["pill_border"]};
  color: #ffffff;
  font-size: 19px;
  font-weight: 600;
  padding: 9px 20px;
  border-radius: 12px;
}}
.footer-bar {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  font-size: 17px;
}}
.footer-left {{
  color: rgba(255, 255, 255, 0.9);
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.8);
  font-weight: 500;
}}
.footer-right {{
  color: {theme["accent"]};
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.8);
  font-weight: 700;
}}
</style>
</head>
<body>
<div class="top-bar">
  <div class="brand-badge">HelpTrickBD | helptrickbd.com</div>
  <div class="category-badge">{clean_cat}</div>
</div>

<div class="main-card">
  <div class="card-content">
    <h1>{clean_title}</h1>
    <p class="subtitle">{clean_sub}</p>
  </div>
  <div class="pills-container">
    {pills_html}
  </div>
</div>

<div class="footer-bar">
  <div class="footer-left">{footer_left}</div>
  <div class="footer-right">{footer_right}</div>
</div>
</body>
</html>"""

def generate_official_bg_banner(
    filename: str,
    category_key: str,
    badge_label: str,
    title: str,
    subtitle: str,
    features: list
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
        is_english=is_english
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
    print(f"  [✔] Generated on {bg_file}: {base_name}.webp ({size_kb:.1f} KB)")
    return out_webp

def build_all():
    print("=" * 75)
    print("🎨 COMPILING ALL BANNERS ON AUTHENTIC 'Thumbnail BG/' TEMPLATES")
    print("=" * 75)

    # 1. Primary Teacher Viva -> bg_4.png (Job Study)
    generate_official_bg_banner(
        filename="primary-teacher-viva-guide-banner.png",
        category_key="Job Study Article",
        badge_label="চাকরির প্রস্তুতি",
        title="সরকারি প্রাথমিক শিক্ষক নিয়োগ ও ভাইভা প্রস্তুতি গাইডলাইন",
        subtitle="ড্রেস কোড, সাধারণ জিজ্ঞাসা ও আত্মবিশ্বাসী ভাইভা সহায়িকা",
        features=["ভাইভা বোর্ডের প্রস্তুতি", "পোশাক ও ড্রেস কোড", "কমন প্রশ্নাবলি", "সংস্করণ ২০২৬"]
    )

    # 2. BCS Preliminary Marks -> bg_4.png (Job Study)
    generate_official_bg_banner(
        filename="bcs-preliminary-marks-booklist-banner.png",
        category_key="Job Study Article",
        badge_label="বিসিএস প্রস্তুতি",
        title="বিসিএস প্রিলিমিনারি ২০০ নম্বরের বিষয়ভিত্তিক মানবণ্টন ও বুক লিস্ট",
        subtitle="প্রথমবারে পাসের সেরা প্রস্তুতি ও বিষয়ভিত্তিক বই তালিকা",
        features=["২০০ নম্বরের সিলেবাস", "বিষয়ভিত্তিক মানবণ্টন", "সেরা রেফারেন্স বই", "সংস্করণ ২০২৬"]
    )

    # 3. Cloud Computing Guide -> bg_5.png (ICT Guide)
    generate_official_bg_banner(
        filename="cloud-computing-guide-banner.png",
        category_key="ICT Guide",
        badge_label="ক্লাউড ও আইসিটি",
        title="ক্লাউড কম্পিউটিং কি? প্রকারভেদ, সুবিধা ও বাস্তব ব্যবহার",
        subtitle="IaaS, PaaS ও SaaS মডেলের তুলনামূলক সহজ পাঠ্যপুস্তক গাইড",
        features=["ক্লাউড সার্ভিস মডেল", "প্রাইভেট ও পাবলিক ক্লাউড", "এডব্লিউএস ও গুগল ড্রাইভ", "সংস্করণ ২০২৬"]
    )

    # 4. Computer Virus & Cyber Security -> bg_5.png (ICT Guide)
    generate_official_bg_banner(
        filename="computer-virus-cyber-security-banner.png",
        category_key="ICT Guide",
        badge_label="আইসিটি ও নিরাপত্তা",
        title="কম্পিউটার ভাইরাস ও সাইবার নিরাপত্তা গাইডলাইন",
        subtitle="ম্যালওয়্যার, র‍্যানসমওয়্যার ও ফিশিং থেকে পিসি ও ডাটা সুরক্ষার উপায়",
        features=["ভাইরাস বনাম ম্যালওয়্যার", "টু-ফ্যাক্টর নিরাপত্তা", "ডাটা ব্যাকআপ টিপস", "সংস্করণ ২০২৬"]
    )

    # 5. HASON RAJA CLASS 6 ENGLISH GUIDE -> bg_1.png (School & Fallback - 100% English!)
    generate_official_bg_banner(
        filename="hason-raja-class6-english-guide-banner.png",
        category_key="Class 6",
        badge_label="Class 6 English",
        title="Hason Raja Was Born in 1854 | Class 6 English Seen Comprehension",
        subtitle="Textbook Passage, Bengali Translation, Word Meanings & Model Questions",
        features=["Seen Comprehension", "Passage Analysis", "Vocabulary & Synonyms", "Model Q&A 2026"]
    )

    print("\n" + "=" * 75)
    print("🎉 ALL 5 BANNERS COMPILED ON OFFICIAL 'Thumbnail BG/' TEMPLATES WITH HARFBUZZ SHAPING!")
    print("=" * 75)

if __name__ == "__main__":
    build_all()
