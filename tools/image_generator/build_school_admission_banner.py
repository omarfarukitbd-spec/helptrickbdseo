import os
import sys
import subprocess
import tempfile
import shutil
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.image_generator.build_official_bg_thumbnails import (
    CATEGORY_CONFIGS,
    get_browser_binary,
    render_banner_html
)
from tools.image_optimizer.webp_compressor import compress_to_target_webp

POSTS_DIR = os.path.join(PROJECT_ROOT, "assets", "images", "posts")
THUMBS_DIR = os.path.join(PROJECT_ROOT, "assets", "images", "thumbnails")
os.makedirs(POSTS_DIR, exist_ok=True)
os.makedirs(THUMBS_DIR, exist_ok=True)

png_path = os.path.join(POSTS_DIR, "school_admission_lottery_exam_guide_2027.png")
webp_path = os.path.join(POSTS_DIR, "school_admission_lottery_exam_guide_2027.webp")

theme = CATEGORY_CONFIGS["Education Guide"]
category_label = "শিক্ষা সহায়িকা ও বিদ্যালয় ভর্তি গাইড"
custom_tag_text = "মাউশি সরকারি ও বেসরকারি স্কুল ভর্তি নীতিমালা ২০২৭ চূড়ান্ত নির্দেশিকা"
title = "স্কুল ভর্তি লটারি ও লিখিত পরীক্ষা ২০২৭"
subtitle = "১ম শ্রেণিতে লটারি • ২য়-৯ম শ্রেণিতে লিখিত পরীক্ষা • gsa.teletalk.com.bd"
features = [
    "১ম শ্রেণিতে ডিজিটাল লটারি",
    "২য়-৯ম লিখিত পরীক্ষা (৫০ ও ১০০)",
    "সর্বোচ্চ ৫টি স্কুল পছন্দক্রম",
    "অনলাইন আবেদন ও ফলাফল"
]

print("[*] Generating HTML banner template for School Admission Lottery & Written Exam 2027...")
html_content = render_banner_html(
    bg_file=theme["bg"],
    theme=theme,
    category_label=category_label,
    title=title,
    subtitle=subtitle,
    features=features,
    is_english=False,
    custom_tag_text=custom_tag_text
)

# Render via headless browser
browser_bin = get_browser_binary()
with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as tf:
    tf.write(html_content)
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
    print(f"[SUCCESS] PNG rendered: {png_path} ({os.path.getsize(png_path)} bytes)")

    # Compress to WebP (12-20 KB Core Web Vitals target)
    compress_to_target_webp(
        input_path=png_path,
        output_path=webp_path,
        target_min_kb=12,
        target_max_kb=20
    )
    print(f"[SUCCESS] Compressed WebP: {webp_path} ({os.path.getsize(webp_path)} bytes)")

    # Also copy to thumbnails folder with slug name
    slug_thumb_png = os.path.join(THUMBS_DIR, "school-admission-lottery-exam-guide-2027-hero.png")
    slug_thumb_webp = os.path.join(THUMBS_DIR, "school-admission-lottery-exam-guide-2027-hero.webp")
    shutil.copy2(png_path, slug_thumb_png)
    shutil.copy2(webp_path, slug_thumb_webp)
    print("[SUCCESS] Thumbnail assets synchronized.")
finally:
    if os.path.exists(temp_html):
        os.remove(temp_html)
