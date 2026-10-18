import os
import sys
import subprocess
import tempfile
import shutil

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

png_path = os.path.join(POSTS_DIR, "ssc_2027_test_exam_form_fill_up_guide.png")
webp_path = os.path.join(POSTS_DIR, "ssc_2027_test_exam_form_fill_up_guide.webp")

theme = CATEGORY_CONFIGS["Education Guide"]  # Uses bg_3.png (Teal/Emerald School Notice)
category_label = "শিক্ষা বোর্ড নোটিশ • এসএসসি ২০২৭"
custom_tag_text = "নির্বাচনী পরীক্ষা ও ফরম পূরণ • অফিশিয়াল ডেডলাইন"
title = "এসএসসি ২০২৭ নির্বাচনী পরীক্ষা ও ফরম পূরণ নির্দেশিকা"
subtitle = "বোর্ড ফি বিজ্ঞান ২,৪৩৫ ও মানবিক ২,৩১৫ টাকা • ১৬–২৯ নভেম্বর ফরম পূরণ"
features = [
    "১৬–২৯ নভেম্বর ফরম পূরণ",
    "বিজ্ঞান ২,৪৩৫ ও মানবিক ২,৩১৫",
    "জিপিএ উন্নয়ন নীতিমালা",
    "অফিসিয়াল বোর্ড বিজ্ঞপ্তি"
]

print("[*] Generating HTML banner template for SSC 2027 Form Fill Up Guide...")
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

    # Compress to WebP (12-20 KB)
    compress_to_target_webp(
        input_path=png_path,
        output_path=webp_path,
        target_min_kb=12,
        target_max_kb=20
    )
    print(f"[SUCCESS] Compressed WebP: {webp_path} ({os.path.getsize(webp_path)} bytes)")

    # Also copy to thumbnails folder
    shutil.copy2(png_path, os.path.join(THUMBS_DIR, "ssc-2027-test-exam-form-fill-up-guide-hero.png"))
    shutil.copy2(webp_path, os.path.join(THUMBS_DIR, "ssc-2027-test-exam-form-fill-up-guide-hero.webp"))
    print("[SUCCESS] Thumbnail assets synchronized.")
finally:
    if os.path.exists(temp_html):
        os.remove(temp_html)
