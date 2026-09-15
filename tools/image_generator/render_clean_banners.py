#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/image_generator/render_clean_banners.py
---------------------------------------------
Generates 100% clean, crisp, emoji-free 16:9 featured banners.
Uses Hind Siliguri Bold / Nirmala UI typography, smooth modern gradients,
and outputs featherweight 10-20 KB WebP files for Core Web Vitals.
"""

import os
import sys
import re
import math
from PIL import Image, ImageDraw, ImageFont

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

from tools.image_generator.bengali_font_engine import get_bengali_font
from tools.image_optimizer.webp_compressor import compress_to_target_webp

POSTS_DIR = os.path.join(PROJECT_ROOT, "assets", "images", "posts")
THUMBS_DIR = os.path.join(PROJECT_ROOT, "assets", "images", "thumbnails")
os.makedirs(POSTS_DIR, exist_ok=True)
os.makedirs(THUMBS_DIR, exist_ok=True)

def strip_emojis(text: str) -> str:
    """Strips all emoji characters and unicode surrogate symbols to prevent [ ] boxes."""
    emoji_pattern = re.compile(
        r"[\U00010000-\U0010FFFF\uD800-\uDBFF\uDC00-\uDFFF\u2600-\u26FF\u2700-\u27BF\uFE00-\uFE0F]"
    )
    # Also strip known icon boxes
    cleaned = emoji_pattern.sub("", text)
    cleaned = re.sub(r"[📌📊📝⚡⭐🛡️🔒🌐🏢💾💻☁️✨👉📘]", "", cleaned)
    return re.sub(r"\s+", " ", cleaned).strip()

def create_gradient(width, height, start_rgb, end_rgb, angle=35):
    base = Image.new("RGB", (width, height), start_rgb)
    top = Image.new("RGB", (width, height), end_rgb)
    mask = Image.new("L", (width, height))
    rad = math.radians(angle)
    cos_v = math.cos(rad)
    sin_v = math.sin(rad)
    max_proj = width * abs(cos_v) + height * abs(sin_v)
    
    mask_data = []
    for y in range(height):
        for x in range(width):
            p = x * cos_v + y * sin_v
            factor = max(0.0, min(1.0, p / max_proj))
            mask_data.append(int(factor * 255))
            
    mask.putdata(mask_data)
    return Image.composite(top, base, mask)

def wrap_text(text, font, max_width, draw):
    words = text.split()
    lines = []
    curr = []
    for w in words:
        test = " ".join(curr + [w])
        bbox = draw.textbbox((0, 0), test, font=font)
        if bbox[2] - bbox[0] <= max_width:
            curr.append(w)
        else:
            if curr:
                lines.append(" ".join(curr))
            curr = [w]
    if curr:
        lines.append(" ".join(curr))
    return lines

def render_banner(
    filename,
    category_name,
    title,
    subtitle,
    features,
    start_rgb=(12, 35, 64),
    end_rgb=(28, 85, 155),
    accent_rgb=(235, 175, 40)
):
    width, height = 1200, 675
    img = create_gradient(width, height, start_rgb, end_rgb)
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # Clean all text inputs of any emoji
    clean_cat = strip_emojis(category_name)
    clean_title = strip_emojis(title)
    clean_sub = strip_emojis(subtitle)
    clean_features = [strip_emojis(f) for f in features]

    # Subtle modern geometric accents
    draw.rectangle([30, 30, width - 30, height - 30], outline=(255, 255, 255, 30), width=2)
    draw.rectangle([36, 36, width - 36, height - 36], outline=(255, 255, 255, 15), width=1)

    # Fonts
    brand_font = get_bengali_font(22, bold=False)
    cat_font = get_bengali_font(22, bold=True)
    title_font = get_bengali_font(52, bold=True)
    sub_font = get_bengali_font(26, bold=False)
    pill_font = get_bengali_font(21, bold=True)
    footer_font = get_bengali_font(18, bold=False)

    # Brand badge (Top Left)
    draw.rounded_rectangle([60, 55, 360, 100], radius=22, fill=(255, 255, 255, 30), outline=(255, 255, 255, 70), width=1)
    draw.text((82, 65), "HelpTrickBD | helptrickbd.com", fill=(255, 255, 255, 240), font=brand_font)

    # Category badge (Top Right)
    cat_bbox = draw.textbbox((0, 0), clean_cat, font=cat_font)
    cat_w = cat_bbox[2] - cat_bbox[0]
    badge_x1 = width - 60 - cat_w - 44
    draw.rounded_rectangle([badge_x1, 55, width - 60, 100], radius=22, fill=(accent_rgb[0], accent_rgb[1], accent_rgb[2], 235))
    draw.text((badge_x1 + 22, 64), clean_cat, fill=(15, 23, 42), font=cat_font)

    # Main Card
    card_x1, card_y1, card_x2, card_y2 = 60, 135, width - 60, 550
    draw.rounded_rectangle([card_x1, card_y1, card_x2, card_y2], radius=16, fill=(0, 0, 0, 65), outline=(255, 255, 255, 35), width=2)

    # Title
    lines = wrap_text(clean_title, title_font, card_x2 - card_x1 - 80, draw)
    title_y = card_y1 + 45
    line_h = 74
    for line in lines:
        draw.text((card_x1 + 42, title_y + 3), line, fill=(0, 0, 0, 140), font=title_font)
        draw.text((card_x1 + 40, title_y), line, fill=(255, 255, 255, 255), font=title_font)
        title_y += line_h

    # Subtitle
    if clean_sub:
        title_y += 8
        draw.text((card_x1 + 42, title_y + 2), clean_sub, fill=(0, 0, 0, 120), font=sub_font)
        draw.text((card_x1 + 40, title_y), clean_sub, fill=(224, 242, 254, 240), font=sub_font)

    # Feature Pills (Bottom of Card) — Clean without tofu boxes
    pill_x = card_x1 + 40
    pill_y = card_y2 - 68
    for feat in clean_features:
        fb = draw.textbbox((0, 0), feat, font=pill_font)
        fw = fb[2] - fb[0]
        draw.rounded_rectangle([pill_x, pill_y, pill_x + fw + 32, pill_y + 44], radius=12, fill=(255, 255, 255, 28), outline=(255, 255, 255, 65), width=1)
        draw.text((pill_x + 16, pill_y + 9), feat, fill=(255, 255, 255, 245), font=pill_font)
        pill_x += fw + 46

    # Bottom Footer Note
    draw.text((65, 600), "© HelpTrickBD Smart Education Platform | সর্বস্বত্ব সংরক্ষিত ২০২৬", fill=(255, 255, 255, 160), font=footer_font)
    draw.text((width - 340, 600), "১০০% সিলেবাস ও পরীক্ষা সহায়ক", fill=(accent_rgb[0], accent_rgb[1], accent_rgb[2], 220), font=footer_font)

    # Composite & Save
    final_img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    
    base_name = os.path.splitext(filename)[0]
    png_path = os.path.join(POSTS_DIR, f"{base_name}.png")
    webp_path = os.path.join(POSTS_DIR, f"{base_name}.webp")
    jpg_path = os.path.join(POSTS_DIR, f"{base_name}.jpg")

    final_img.save(png_path, "PNG")
    final_img.save(jpg_path, "JPEG", quality=92)
    compress_to_target_webp(png_path, webp_path, target_min_kb=10.0, target_max_kb=20.0)

    # Also sync to thumbnails folder
    import shutil
    shutil.copy2(png_path, os.path.join(THUMBS_DIR, f"{base_name}.png"))
    shutil.copy2(webp_path, os.path.join(THUMBS_DIR, f"{base_name}.webp"))
    shutil.copy2(jpg_path, os.path.join(THUMBS_DIR, f"{base_name}.jpg"))

    size_kb = os.path.getsize(webp_path) / 1024.0
    print(f"  [✔] Generated clean banner: {base_name}.webp ({size_kb:.1f} KB)")
    return webp_path

def generate_all_targets():
    print("=" * 70)
    print("🎨 REGENERATING 4 SILO THUMBNAILS + HASON RAJA BANNER (ZERO TOFU BOXES)")
    print("=" * 70)

    # 1. Primary Teacher Viva
    render_banner(
        filename="primary-teacher-viva-guide-banner.png",
        category_name="চাকরির প্রস্তুতি",
        title="সরকারি প্রাথমিক শিক্ষক নিয়োগ ও ভাইভা প্রস্তুতি গাইডলাইন",
        subtitle="ড্রেস কোড, সাধারণ জিজ্ঞাসা ও আত্মবিশ্বাসী ভাইভা সহায়িকা",
        features=["ভাইভা বোর্ডের প্রস্তুতি", "পোশাক ও ড্রেস কোড", "কমন প্রশ্নাবলি", "সংস্করণ ২০২৬"],
        start_rgb=(6, 78, 59),     # Deep Emerald
        end_rgb=(16, 185, 129),    # Fresh Green
        accent_rgb=(250, 204, 21)   # Yellow Gold
    )

    # 2. BCS Preliminary Marks
    render_banner(
        filename="bcs-preliminary-marks-booklist-banner.png",
        category_name="বিসিএস প্রস্তুতি",
        title="বিসিএস প্রিলিমিনারি ২০০ নম্বরের বিষয়ভিত্তিক মানবণ্টন ও বুক লিস্ট",
        subtitle="প্রথমবারে পাসের সেরা প্রস্তুতি ও বিষয়ভিত্তিক বই তালিকা",
        features=["২০০ নম্বরের সিলেবাস", "বিষয়ভিত্তিক মানবণ্টন", "সেরা রেফারেন্স বই", "সংস্করণ ২০২৬"],
        start_rgb=(15, 23, 42),    # Deep Slate
        end_rgb=(30, 58, 138),     # Navy Blue
        accent_rgb=(245, 158, 11)   # Amber
    )

    # 3. Cloud Computing Guide
    render_banner(
        filename="cloud-computing-guide-banner.png",
        category_name="তথ্য ও যোগাযোগ প্রযুক্তি",
        title="ক্লাউড কম্পিউটিং কি? প্রকারভেদ, সুবিধা ও বাস্তব ব্যবহার",
        subtitle="IaaS, PaaS ও SaaS মডেলের তুলনামূলক সহজ পাঠ্যপুস্তক গাইড",
        features=["ক্লাউড সার্ভিস মডেল", "প্রাইভেট ও পাবলিক ক্লাউড", "এডব্লিউএস ও গুগল ড্রাইভ", "সংস্করণ ২০২৬"],
        start_rgb=(49, 46, 129),   # Indigo
        end_rgb=(99, 102, 241),    # Light Indigo
        accent_rgb=(56, 189, 248)   # Sky Blue
    )

    # 4. Computer Virus & Cyber Security
    render_banner(
        filename="computer-virus-cyber-security-banner.png",
        category_name="আইসিটি ও সাইবার নিরাপত্তা",
        title="কম্পিউটার ভাইরাস ও সাইবার নিরাপত্তা গাইডলাইন",
        subtitle="ম্যালওয়্যার, র‍্যানসমওয়্যার ও ফিশিং থেকে পিসি ও ডাটা সুরক্ষার উপায়",
        features=["ভাইরাস বনাম ম্যালওয়্যার", "টু-ফ্যাক্টর নিরাপত্তা", "ডাটা ব্যাকআপ টিপস", "সংস্করণ ২০২৬"],
        start_rgb=(15, 23, 42),    # Dark Tech
        end_rgb=(14, 116, 144),    # Cyan
        accent_rgb=(56, 189, 248)   # Bright Cyan
    )

    # 5. HASON RAJA CLASS 6 ENGLISH GUIDE (Fixing Missing Thumbnail!)
    render_banner(
        filename="hason-raja-class6-english-guide-banner.png",
        category_name="Class 6 English",
        title="Hason Raja Was Born in 1854 | Class 6 English Seen Comprehension",
        subtitle="Textbook Passage, Bengali Translation, Word Meanings & Model Questions",
        features=["Seen Comprehension", "Bengali Meaning", "Vocabulary & Synonyms", "Model Q&A 2026"],
        start_rgb=(30, 27, 75),    # Academic Violet
        end_rgb=(79, 70, 229),     # Royal Purple
        accent_rgb=(250, 204, 21)   # Gold Accent
    )

    print("\n" + "=" * 70)
    print("🎉 ALL 5 BANNERS REGENERATED CLEANLY WITH 10-20 KB WEBP & ZERO TOFU BOXES!")
    print("=" * 70)

if __name__ == "__main__":
    generate_all_targets()
