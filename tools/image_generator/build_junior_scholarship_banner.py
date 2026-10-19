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

png_path = os.path.join(POSTS_DIR, "class_8_junior_scholarship_exam_routine_2026.png")
webp_path = os.path.join(POSTS_DIR, "class_8_junior_scholarship_exam_routine_2026.webp")

theme = CATEGORY_CONFIGS["Education Guide"]
category_label = "শিক্ষা সহায়িকা ও জুনিয়র বৃত্তি গাইড"
custom_tag_text = "৮ম শ্রেণি ও দাখিল জুনিয়র বৃত্তি ২০২৬ চূড়ান্ত নির্দেশিকা"
title = "৮ম শ্রেণির জুনিয়র বৃত্তি পরীক্ষা ২০২৬"
subtitle = "পরীক্ষার রুটিন • ২০০ নম্বরের চূড়ান্ত মানবণ্টন ও সুপার সাজেশন"
features = [
    "৪ বিষয় ২০০ নম্বর",
    "ট্যালেন্টপুল বৃত্তি কৌশল",
    "নভেম্বর-ডিসেম্বর শুরু",
    "অফিসিয়াল PDF রুটিন"
]

print("[*] Generating HTML banner template for Class 8 Junior Scholarship Exam 2026...")
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
    slug_thumb_png = os.path.join(THUMBS_DIR, "class-8-junior-scholarship-exam-routine-suggestion-2026-hero.png")
    slug_thumb_webp = os.path.join(THUMBS_DIR, "class-8-junior-scholarship-exam-routine-suggestion-2026-hero.webp")
    shutil.copy2(png_path, slug_thumb_png)
    shutil.copy2(webp_path, slug_thumb_webp)
    print("[SUCCESS] Thumbnail assets synchronized.")
finally:
    if os.path.exists(temp_html):
        os.remove(temp_html)
