#!/usr/bin/env python3
"""
HelpTrickBD - Category-Wise Automated Thumbnail Generator
Uses custom background templates from 'Thumbnail BG/', Hind Siliguri typography,
the official transparent HelpTrickBD logo, and consistent brand elements.

Category Mapping (1 Category = 1 Fixed Design):
- Political Science  -> bg_2.png (Deep Navy Blue & Gold Academic Curves)
- Islamic Article    -> bg.png   (Emerald Green & Gold Botanical Watercolor)
- Education Guide    -> bg_3.png (Teal Waves & Geometric Shapes)
- Job Study Article  -> bg_4.png (Forest Green & Warm Sand Fluid Shapes)
- ICT Guide          -> bg_5.png (Dark Navy & Tech Yellow Diagonal Geometry)
- Fallback / School  -> bg_1.png (Clean Dual-tone Green Waves)
"""

import os
import subprocess
import sys
import tempfile
from PIL import Image

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
BG_DIR = os.path.join(PROJECT_ROOT, "Thumbnail BG")
LOGO_PATH = os.path.join(PROJECT_ROOT, "assets", "images", "logo", "helptrickbd_logo.png")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "assets", "images", "thumbnails")
os.makedirs(OUTPUT_DIR, exist_ok=True)

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
]

CHROME_PATH = None
for c in CHROME_CANDIDATES:
    if os.path.exists(c):
        CHROME_PATH = c
        break

if not CHROME_PATH:
    raise RuntimeError("Google Chrome executable not found for headless thumbnail rendering.")

# Category Configuration Dictionary
CATEGORY_CONFIG = {
    "Political Science": {
        "bg_file": "bg_2.png",
        "badge_name": "রাষ্ট্রবিজ্ঞান বিভাগ",
        "badge_icon": "📚",
        "badge_bg": "#0c2340",
        "badge_border": "#d4af37",
        "badge_text": "#ffffff",
        "title_color": "#0a1f38",
        "sub_bg": "#f0f4f9",
        "sub_border": "#c2d4ea",
        "sub_text": "#0c2340",
    },
    "Islamic Article": {
        "bg_file": "bg.png",
        "badge_name": "ইসলামিক সাহিত্য ও প্রবন্ধ",
        "badge_icon": "🌙",
        "badge_bg": "#0a4c2e",
        "badge_border": "#e2b024",
        "badge_text": "#ffffff",
        "title_color": "#083e25",
        "sub_bg": "#f2faf5",
        "sub_border": "#b8e2cb",
        "sub_text": "#0a4c2e",
    },
    "Education Guide": {
        "bg_file": "bg_3.png",
        "badge_name": "শিক্ষা সহায়িকা ও স্টাডি গাইড",
        "badge_icon": "🎓",
        "badge_bg": "#025b5e",
        "badge_border": "#20b2aa",
        "badge_text": "#ffffff",
        "title_color": "#013b3d",
        "sub_bg": "#f0faf9",
        "sub_border": "#b2e3e1",
        "sub_text": "#025b5e",
    },
    "Job Study Article": {
        "bg_file": "bg_4.png",
        "badge_name": "বিসিএস ও চাকরির প্রস্তুতি",
        "badge_icon": "💼",
        "badge_bg": "#164e3b",
        "badge_border": "#b48c36",
        "badge_text": "#ffffff",
        "title_color": "#113e2f",
        "sub_bg": "#f7f6f0",
        "sub_border": "#dcd4b8",
        "sub_text": "#164e3b",
    },
    "ICT Guide": {
        "bg_file": "bg_5.png",
        "badge_name": "কম্পিউটার ও তথ্যপ্রযুক্তি",
        "badge_icon": "💻",
        "badge_bg": "#0f172a",
        "badge_border": "#eab308",
        "badge_text": "#facc15",
        "title_color": "#0b1324",
        "sub_bg": "#f8fafc",
        "sub_border": "#cbd5e1",
        "sub_text": "#0f172a",
    },
    "Default": {
        "bg_file": "bg_1.png",
        "badge_name": "স্টাডি ও ক্যারিয়ার গাইড",
        "badge_icon": "📝",
        "badge_bg": "#064e3b",
        "badge_border": "#10b981",
        "badge_text": "#ffffff",
        "title_color": "#064e3b",
        "sub_bg": "#f0fdf4",
        "sub_border": "#bbf7d0",
        "sub_text": "#064e3b",
    },
}


def get_category_config(category_name):
    """Matches category name or falls back to default."""
    if not category_name:
        return CATEGORY_CONFIG["Default"]

    for key, conf in CATEGORY_CONFIG.items():
        if key.lower() in category_name.lower():
            return conf

    # Bengali matches
    cat_lower = category_name.lower()
    if "রাষ্ট্রবিজ্ঞান" in cat_lower or "রাজনৈতিক" in cat_lower or "political" in cat_lower:
        return CATEGORY_CONFIG["Political Science"]
    if "ইসলাম" in cat_lower or "ক্বাসিদা" in cat_lower or "দরূদ" in cat_lower or "islamic" in cat_lower:
        return CATEGORY_CONFIG["Islamic Article"]
    if "শিক্ষা" in cat_lower or "ক্লাস" in cat_lower or "class" in cat_lower or "education" in cat_lower:
        return CATEGORY_CONFIG["Education Guide"]
    if "চাকরি" in cat_lower or "বিসিএস" in cat_lower or "job" in cat_lower or "নিয়োগ" in cat_lower:
        return CATEGORY_CONFIG["Job Study Article"]
    if "কম্পিউটার" in cat_lower or "ict" in cat_lower or "তথ্যপ্রযুক্তি" in cat_lower or "প্রযুক্তি" in cat_lower:
        return CATEGORY_CONFIG["ICT Guide"]

    return CATEGORY_CONFIG["Default"]


def render_html_template(title, category, subtitle=None):
    """Generates pure HTML5/CSS3 template for Chrome headless rendering."""
    conf = get_category_config(category)
    bg_file_path = os.path.join(BG_DIR, conf["bg_file"]).replace(os.sep, "/")
    logo_file_path = LOGO_PATH.replace(os.sep, "/")

    # Title size calculation based on character count
    title_len = len(title)
    if title_len > 70:
        title_font_size = "43px"
        title_line_height = "1.32"
    elif title_len > 45:
        title_font_size = "49px"
        title_line_height = "1.35"
    else:
        title_font_size = "56px"
        title_line_height = "1.38"

    subtitle_html = ""
    if subtitle:
        subtitle_html = f"""
        <div class="subtitle-pill">
            <span style="font-size: 20px;">✨</span>
            <span>{subtitle}</span>
        </div>
        """

    html = f"""<!DOCTYPE html>
<html lang="bn">
<head>
<meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@500;600;700&display=swap" rel="stylesheet">
<style>
  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}
  body {{
    width: 1200px;
    height: 675px;
    overflow: hidden;
    font-family: 'Hind Siliguri', -apple-system, BlinkMacSystemFont, sans-serif;
    background-image: url('file:///{bg_file_path}');
    background-size: cover;
    background-position: center center;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 34px 48px 28px 48px;
  }}

  /* Top Header Bar */
  .top-bar {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    z-index: 10;
  }}
  .logo-capsule {{
    background: rgba(255, 255, 255, 0.94);
    border: 1.5px solid rgba(0, 0, 0, 0.09);
    padding: 7px 18px;
    border-radius: 14px;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.07);
    display: flex;
    align-items: center;
  }}
  .logo-capsule img {{
    height: 48px;
    width: auto;
    display: block;
  }}
  .category-pill {{
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: {conf['badge_bg']};
    border: 2px solid {conf['badge_border']};
    color: {conf['badge_text']};
    padding: 10px 24px;
    border-radius: 50px;
    font-size: 21px;
    font-weight: 700;
    box-shadow: 0 4px 14px rgba(0,0,0,0.14);
  }}

  /* Center Title Content Area */
  .center-content {{
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 10px 45px;
    z-index: 10;
  }}
  .main-title {{
    color: {conf['title_color']};
    font-size: {title_font_size};
    line-height: {title_line_height};
    font-weight: 700;
    max-width: 940px;
    letter-spacing: -0.2px;
    text-shadow: 0 2px 16px rgba(255,255,255,0.95), 0 1px 3px rgba(0,0,0,0.06);
  }}
  .subtitle-pill {{
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: rgba(255, 255, 255, 0.92);
    border: 2px solid {conf['sub_border']};
    color: {conf['sub_text']};
    padding: 9px 26px;
    border-radius: 30px;
    font-size: 22px;
    font-weight: 600;
    margin-top: 22px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.06);
  }}

  /* Bottom Footer Bar */
  .bottom-bar {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    z-index: 10;
  }}
  .footer-domain-pill {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(255, 255, 255, 0.95);
    border: 1.5px solid rgba(0, 0, 0, 0.08);
    padding: 8px 20px;
    border-radius: 30px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    color: #1e293b;
    font-size: 19px;
    font-weight: 700;
    letter-spacing: 0.3px;
  }}
  .footer-domain-pill svg {{
    width: 20px;
    height: 20px;
    fill: #2563eb;
  }}
  .footer-tagline-pill {{
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: rgba(255, 255, 255, 0.95);
    border: 1.5px solid rgba(0, 0, 0, 0.08);
    padding: 8px 20px;
    border-radius: 30px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    color: #334155;
    font-size: 18px;
    font-weight: 600;
  }}
  .footer-tagline-pill .dot {{
    color: #94a3b8;
    font-size: 12px;
  }}
</style>
</head>
<body>

  <!-- Top Bar: Logo Capsule & Category Badge -->
  <div class="top-bar">
    <div class="logo-capsule">
      <img src="file:///{logo_file_path}" alt="HelpTrickBD Logo">
    </div>
    <div class="category-pill">
      <span>{conf['badge_icon']}</span>
      <span>{conf['badge_name']}</span>
    </div>
  </div>

  <!-- Center Area: Hind Siliguri Title & Feature Subtitle -->
  <div class="center-content">
    <h1 class="main-title">{title}</h1>
    {subtitle_html}
  </div>

  <!-- Bottom Bar: Protected Floating Domain & Tagline Pills -->
  <div class="bottom-bar">
    <div class="footer-domain-pill">
      <svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/></svg>
      <span>www.helptrickbd.com</span>
    </div>
    <div class="footer-tagline-pill">
      <span>Learn Smart</span>
      <span class="dot">•</span>
      <span>Lead Future</span>
      <span class="dot">•</span>
      <span style="color: #047857; font-weight: 700;">সর্বশেষ সংস্করণ ২০২৬</span>
    </div>
  </div>

</body>
</html>"""
    return html


def generate_thumbnail(title, category, subtitle=None, output_filename=None):
    """
    Renders and exports a 1200x675 16:9 banner image.
    Returns the absolute path to the generated image.
    """
    if not output_filename:
        safe_name = "".join(c if c.isalnum() else "_" for c in title[:30]).strip("_")
        output_filename = f"thumb_{safe_name}.png"

    if not output_filename.endswith((".png", ".jpg", ".webp")):
        output_filename += ".png"

    output_path = os.path.join(OUTPUT_DIR, output_filename)
    html_content = render_html_template(title, category, subtitle)

    with tempfile.NamedTemporaryFile(suffix=".html", delete=False, mode="w", encoding="utf-8") as tf:
        tf.write(html_content)
        temp_html_path = tf.name

    try:
        cmd = [
            CHROME_PATH,
            "--headless=new",
            "--disable-gpu",
            "--hide-scrollbars",
            "--window-size=1200,675",
            f"--screenshot={output_path}",
            f"file:///{temp_html_path.replace(os.sep, '/')}",
        ]
        subprocess.run(cmd, check=True, capture_output=True)

        # Optimize image with PIL
        with Image.open(output_path) as im:
            im.save(output_path, optimize=True)

        print(f"✅ Thumbnail Generated: {output_filename}")
        return output_path
    finally:
        if os.path.exists(temp_html_path):
            os.remove(temp_html_path)


if __name__ == "__main__":
    print("Thumbnail Generator Engine Initialized.")
