import os
import sys
import subprocess
import tempfile
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

png_path = os.path.join(POSTS_DIR, "primary_scholarship_exam_routine_2026.png")
webp_path = os.path.join(POSTS_DIR, "primary_scholarship_exam_routine_2026.webp")

theme = CATEGORY_CONFIGS["Education Guide"]
category_label = "শিক্ষা সহায়িকা ও স্টাডি গাইড"
custom_tag_text = "৫ম শ্রেণি প্রাথমিক শিক্ষা অধিদপ্তর স্পেশাল গাইডলাইন"
title = "প্রাথমিক বৃত্তি পরীক্ষার রুটিন 2026"
subtitle = "২০ ডিসেম্বর পরীক্ষা • ১০০ নম্বরের চূড়ান্ত মানবণ্টন ও প্রস্তুতি কৌশল"
features = [
    "৪ বিষয় ১০০ নম্বর",
    "ট্যালেন্টপুল বৃত্তি কৌশল",
    "২০ ডিসেম্বর শুরু",
    "অফিসিয়াল PDF রুটিন"
]

print("[*] Generating HTML banner template for Primary Scholarship Exam 2026...")
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

    # Compress to WebP
    compress_to_target_webp(
        input_path=png_path,
        output_path=webp_path,
        target_min_kb=12,
        target_max_kb=20
    )
    print(f"[SUCCESS] Compressed WebP: {webp_path} ({os.path.getsize(webp_path)} bytes)")

    # Also copy to thumbnails folder
    import shutil
    shutil.copy2(png_path, os.path.join(THUMBS_DIR, "primary-scholarship-exam-routine-2026-hero.png"))
    shutil.copy2(webp_path, os.path.join(THUMBS_DIR, "primary-scholarship-exam-routine-2026-hero.webp"))
    print("[SUCCESS] Thumbnail assets synchronized.")
finally:
    if os.path.exists(temp_html):
        os.remove(temp_html)
