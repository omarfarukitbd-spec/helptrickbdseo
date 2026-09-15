#!/usr/bin/env python3
"""
Generates 6 authentic tutorial images using REAL government education board portal screenshots
with Hind Siliguri Bold Bengali annotations, red click boxes, and arrows.
"""

import os
import subprocess
import sys
try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from PIL import Image

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT_DIR = os.path.join(PROJECT_ROOT, "assets", "images", "tutorials")
os.makedirs(OUT_DIR, exist_ok=True)

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
if not os.path.exists(CHROME_PATH):
    CHROME_PATH = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

def prepare_sources():
    brain_dir = r"C:\Users\omarf\.gemini\antigravity-ide\brain\b8a04e65-e2a3-4935-89f2-c55d9c7ebecd"
    
    # Source 1: Dhaka e-service menu (1366x599)
    s1 = os.path.join(brain_dir, "dhaka_eservice_menu_1789455782397.png")
    im1 = Image.open(s1)
    bg1_path = os.path.join(OUT_DIR, "raw_step1.png")
    im1.save(bg1_path)

    # Source 2: Dhaka action sub-menu (1366x599)
    s2 = os.path.join(brain_dir, "name_age_correction_page_1789455885607.png")
    im2 = Image.open(s2)
    bg2_path = os.path.join(OUT_DIR, "raw_step2.png")
    im2.save(bg2_path)

    # Source 3: Rajshahi Exam Search (Top section)
    s3 = os.path.join(PROJECT_ROOT, "rajshahi_name_cor_loaded.png")
    im3 = Image.open(s3)
    # Crop to include Search button fully
    im3_crop = im3.crop((0, 0, 1280, 600))
    bg3_path = os.path.join(OUT_DIR, "raw_step3.png")
    im3_crop.save(bg3_path)

    # Source 4: Rajshahi Correction Details (Middle section)
    im4_crop = im3.crop((0, 535, 1280, 1080))
    bg4_path = os.path.join(OUT_DIR, "raw_step4.png")
    im4_crop.save(bg4_path)

    # Source 5: Sonali Seba Application (Crop from 150 to 800)
    s5 = os.path.join(PROJECT_ROOT, "rajshahi_sonali.png")
    im5 = Image.open(s5)
    im5_crop = im5.crop((0, 140, 1280, 780))
    bg5_path = os.path.join(OUT_DIR, "raw_step5.png")
    im5_crop.save(bg5_path)

    # Source 6: Dhaka Last Update Tracking (1280x800)
    s6 = os.path.join(PROJECT_ROOT, "dhaka_lastupdate.png")
    im6 = Image.open(s6)
    bg6_path = os.path.join(OUT_DIR, "raw_step6.png")
    im6.save(bg6_path)

    return {
        "step1": bg1_path,
        "step2": bg2_path,
        "step3": bg3_path,
        "step4": bg4_path,
        "step5": bg5_path,
        "step6": bg6_path
    }

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
from tools.image_optimizer.webp_compressor import compress_to_target_webp

def render_annotated_image(html_content, out_path, width=1280, height=800):
    tmp_html = os.path.join(OUT_DIR, "temp_render.html")
    with open(tmp_html, "w", encoding="utf-8") as f:
        f.write(html_content)

    cmd = [
        CHROME_PATH,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--window-size={width},{height}",
        f"--screenshot={out_path}",
        f"file:///{tmp_html.replace(os.sep, '/')}"
    ]
    subprocess.run(cmd, check=True)
    if os.path.exists(tmp_html):
        os.remove(tmp_html)

    # Automatically generate 10–20 KB WebP version for Core Web Vitals
    webp_out = os.path.splitext(out_path)[0] + ".webp"
    compress_to_target_webp(out_path, webp_out, target_min_kb=10.0, target_max_kb=20.0, max_width=width, max_height=height)
    sz_kb = os.path.getsize(webp_out) / 1024.0
    print(f"  ⚡ WebP Created: {os.path.basename(webp_out)} ({sz_kb:.1f} KB)")
    return webp_out

def main():
    print("Preparing authentic source backgrounds...")
    sources = prepare_sources()

    # Step 1: Dhaka Board e-Service Menu
    html_step1 = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@600;700&display=swap" rel="stylesheet">
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ background: #f1f5f9; display: flex; justify-content: center; align-items: center; min-height: 100vh; }}
  .container {{ position: relative; width: 1366px; height: 599px; overflow: hidden; }}
  .bg-img {{ width: 100%; height: 100%; display: block; }}
  .highlight-box {{
    position: absolute;
    left: 92px;
    top: 184px;
    width: 1182px;
    height: 48px;
    border: 3.5px solid #dc2626;
    border-radius: 8px;
    box-shadow: 0 0 18px rgba(220, 38, 38, 0.6);
    background: rgba(220, 38, 38, 0.08);
  }}
  .badge {{
    position: absolute;
    left: 380px;
    top: 122px;
    background: #dc2626;
    color: #ffffff;
    font-family: 'Hind Siliguri', sans-serif;
    font-size: 20px;
    font-weight: 700;
    padding: 8px 24px;
    border-radius: 30px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.3);
    border: 2px solid #ffffff;
    z-index: 10;
  }}
  .badge::after {{
    content: '';
    position: absolute;
    bottom: -10px;
    left: 50%;
    transform: translateX(-50%);
    border-width: 10px 10px 0;
    border-style: solid;
    border-color: #dc2626 transparent;
  }}
</style>
</head>
<body>
  <div class="container">
    <img class="bg-img" src="file:///{sources['step1'].replace(os.sep, '/')}" />
    <div class="highlight-box"></div>
    <div class="badge">ধাপ ১: এই 'নাম ও বয়স সংশোধনের আবেদন' অপশনে ক্লিক করুন</div>
  </div>
</body>
</html>"""
    out1 = os.path.join(OUT_DIR, "cert_step1_portal_access.png")
    render_annotated_image(html_step1, out1, 1366, 599)
    print("Step 1 OK:", out1)

    # Step 2: Dhaka Board Sub-menu (Cyan 'আবেদন ফরম' button)
    html_step2 = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@600;700&display=swap" rel="stylesheet">
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ background: #f1f5f9; display: flex; justify-content: center; align-items: center; min-height: 100vh; }}
  .container {{ position: relative; width: 1366px; height: 599px; overflow: hidden; }}
  .bg-img {{ width: 100%; height: 100%; display: block; }}
  .highlight-box {{
    position: absolute;
    left: 106px;
    top: 310px;
    width: 126px;
    height: 48px;
    border: 3.5px solid #dc2626;
    border-radius: 6px;
    box-shadow: 0 0 18px rgba(220, 38, 38, 0.7);
    background: rgba(220, 38, 38, 0.12);
  }}
  .badge {{
    position: absolute;
    left: 45px;
    top: 382px;
    background: #dc2626;
    color: #ffffff;
    font-family: 'Hind Siliguri', sans-serif;
    font-size: 19px;
    font-weight: 700;
    padding: 8px 22px;
    border-radius: 30px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.3);
    border: 2px solid #ffffff;
    z-index: 10;
  }}
  .badge::before {{
    content: '';
    position: absolute;
    top: -10px;
    left: 70px;
    border-width: 0 10px 10px;
    border-style: solid;
    border-color: #dc2626 transparent;
  }}
</style>
</head>
<body>
  <div class="container">
    <img class="bg-img" src="file:///{sources['step2'].replace(os.sep, '/')}" />
    <div class="highlight-box"></div>
    <div class="badge">ধাপ ২: নতুন আবেদনের জন্য 'আবেদন ফরম' বাটনে ক্লিক করুন</div>
  </div>
</body>
</html>"""
    out2 = os.path.join(OUT_DIR, "cert_step2_student_search.png")
    render_annotated_image(html_step2, out2, 1366, 599)
    print("Step 2 OK:", out2)

    # Step 3: Exam Information & Search Form (1280x600)
    html_step3 = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@600;700&display=swap" rel="stylesheet">
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ background: #f1f5f9; display: flex; justify-content: center; align-items: center; min-height: 100vh; }}
  .container {{ position: relative; width: 1280px; height: 600px; overflow: hidden; }}
  .bg-img {{ width: 100%; height: 100%; display: block; }}
  .inputs-box {{
    position: absolute;
    left: 88px;
    top: 380px;
    width: 1080px;
    height: 90px;
    border: 2.5px dashed #2563eb;
    border-radius: 8px;
    background: rgba(37, 99, 235, 0.04);
  }}
  .search-box {{
    position: absolute;
    left: 591px;
    top: 543px;
    width: 82px;
    height: 36px;
    border: 3.5px solid #dc2626;
    border-radius: 6px;
    box-shadow: 0 0 18px rgba(220, 38, 38, 0.85);
    background: rgba(220, 38, 38, 0.15);
  }}
  .badge {{
    position: absolute;
    left: 310px;
    top: 472px;
    background: #dc2626;
    color: #ffffff;
    font-family: 'Hind Siliguri', sans-serif;
    font-size: 19px;
    font-weight: 700;
    padding: 7px 24px;
    border-radius: 30px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.3);
    border: 2px solid #ffffff;
    z-index: 10;
  }}
  .badge::after {{
    content: '';
    position: absolute;
    bottom: -10px;
    left: 50%;
    transform: translateX(-50%);
    border-width: 10px 10px 0;
    border-style: solid;
    border-color: #dc2626 transparent;
  }}
</style>
</head>
<body>
  <div class="container">
    <img class="bg-img" src="file:///{sources['step3'].replace(os.sep, '/')}" />
    <div class="inputs-box"></div>
    <div class="search-box"></div>
    <div class="badge">ধাপ ৩: পরীক্ষার তথ্য, রোল ও রেজি নম্বর পূরণ করে 'Search' বাটনে ক্লিক করুন</div>
  </div>
</body>
</html>"""
    out3 = os.path.join(OUT_DIR, "cert_step3_correction_form.png")
    render_annotated_image(html_step3, out3, 1280, 600)
    print("Step 3 OK:", out3)

    # Step 4: Correction Information Data Entry (1280x545)
    html_step4 = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@600;700&display=swap" rel="stylesheet">
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ background: #f1f5f9; display: flex; justify-content: center; align-items: center; min-height: 100vh; }}
  .container {{ position: relative; width: 1280px; height: 545px; overflow: hidden; }}
  .bg-img {{ width: 100%; height: 100%; display: block; }}
  .highlight-box {{
    position: absolute;
    left: 88px;
    top: 36px;
    width: 1080px;
    height: 360px;
    border: 3.5px solid #dc2626;
    border-radius: 8px;
    box-shadow: 0 0 18px rgba(220, 38, 38, 0.45);
    background: rgba(220, 38, 38, 0.04);
  }}
  .badge {{
    position: absolute;
    left: 320px;
    top: 418px;
    background: #dc2626;
    color: #ffffff;
    font-family: 'Hind Siliguri', sans-serif;
    font-size: 19px;
    font-weight: 700;
    padding: 8px 24px;
    border-radius: 30px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.3);
    border: 2px solid #ffffff;
    z-index: 10;
  }}
  .badge::before {{
    content: '';
    position: absolute;
    top: -10px;
    left: 50%;
    transform: translateX(-50%);
    border-width: 0 10px 10px;
    border-style: solid;
    border-color: #dc2626 transparent;
  }}
</style>
</head>
<body>
  <div class="container">
    <img class="bg-img" src="file:///{sources['step4'].replace(os.sep, '/')}" />
    <div class="highlight-box"></div>
    <div class="badge">ধাপ ৪: সংশোধিত সঠিক নাম, পিতা-মাতার নাম ও যোগাযোগের তথ্য এন্ট্রি করুন</div>
  </div>
</body>
</html>"""
    out4 = os.path.join(OUT_DIR, "cert_step4_document_upload.png")
    render_annotated_image(html_step4, out4, 1280, 545)
    print("Step 4 OK:", out4)

    # Step 5: Sonali Seba Application Gateway (1280x640)
    html_step5 = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@600;700&display=swap" rel="stylesheet">
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ background: #f1f5f9; display: flex; justify-content: center; align-items: center; min-height: 100vh; }}
  .container {{ position: relative; width: 1280px; height: 640px; overflow: hidden; }}
  .bg-img {{ width: 100%; height: 100%; display: block; }}
  .highlight-box {{
    position: absolute;
    left: 88px;
    top: 245px;
    width: 1080px;
    height: 360px;
    border: 3.5px solid #dc2626;
    border-radius: 8px;
    box-shadow: 0 0 18px rgba(220, 38, 38, 0.5);
    background: rgba(220, 38, 38, 0.05);
  }}
  .badge {{
    position: absolute;
    left: 270px;
    top: 175px;
    background: #dc2626;
    color: #ffffff;
    font-family: 'Hind Siliguri', sans-serif;
    font-size: 19px;
    font-weight: 700;
    padding: 8px 24px;
    border-radius: 30px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.3);
    border: 2px solid #ffffff;
    z-index: 10;
  }}
  .badge::after {{
    content: '';
    position: absolute;
    bottom: -10px;
    left: 50%;
    transform: translateX(-50%);
    border-width: 10px 10px 0;
    border-style: solid;
    border-color: #dc2626 transparent;
  }}
</style>
</head>
<body>
  <div class="container">
    <img class="bg-img" src="file:///{sources['step5'].replace(os.sep, '/')}" />
    <div class="highlight-box"></div>
    <div class="badge">ধাপ ৫: সোনালী সেবায় ফি যাচাই করে মোবাইল ব্যাংকিং বা কাউন্টারে ফি পরিশোধ করুন</div>
  </div>
</body>
</html>"""
    out5 = os.path.join(OUT_DIR, "cert_step5_sonali_payment.png")
    render_annotated_image(html_step5, out5, 1280, 640)
    print("Step 5 OK:", out5)

    # Step 6: Application Tracking & Status (1280x800)
    html_step6 = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@600;700&display=swap" rel="stylesheet">
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ background: #f1f5f9; display: flex; justify-content: center; align-items: center; min-height: 100vh; }}
  .container {{ position: relative; width: 1280px; height: 800px; overflow: hidden; }}
  .bg-img {{ width: 100%; height: 100%; display: block; }}
  .inputs-box {{
    position: absolute;
    left: 435px;
    top: 350px;
    width: 380px;
    height: 95px;
    border: 2px dashed #2563eb;
    border-radius: 6px;
    background: rgba(37, 99, 235, 0.04);
  }}
  .find-btn {{
    position: absolute;
    left: 698px;
    top: 397px;
    width: 104px;
    height: 39px;
    border: 3.5px solid #dc2626;
    border-radius: 6px;
    box-shadow: 0 0 18px rgba(220, 38, 38, 0.85);
    background: rgba(220, 38, 38, 0.15);
  }}
  .badge {{
    position: absolute;
    left: 270px;
    top: 270px;
    background: #dc2626;
    color: #ffffff;
    font-family: 'Hind Siliguri', sans-serif;
    font-size: 19px;
    font-weight: 700;
    padding: 8px 24px;
    border-radius: 30px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.3);
    border: 2px solid #ffffff;
    z-index: 10;
  }}
  .badge::after {{
    content: '';
    position: absolute;
    bottom: -10px;
    left: 50%;
    transform: translateX(-50%);
    border-width: 10px 10px 0;
    border-style: solid;
    border-color: #dc2626 transparent;
  }}
</style>
</head>
<body>
  <div class="container">
    <img class="bg-img" src="file:///{sources['step6'].replace(os.sep, '/')}" />
    <div class="inputs-box"></div>
    <div class="find-btn"></div>
    <div class="badge">ধাপ ৬: Application ID ও Password লিখে 'Find' বাটনে ক্লিক করে স্ট্যাটাস দেখুন</div>
  </div>
</body>
</html>"""
    out6 = os.path.join(OUT_DIR, "cert_step6_tracking_receipt.png")
    render_annotated_image(html_step6, out6, 1280, 800)
    print("Step 6 OK:", out6)

    print("\nAll 6 authentic tutorial screenshots generated successfully!")

if __name__ == "__main__":
    main()
