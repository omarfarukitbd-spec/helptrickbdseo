#!/usr/bin/env python3
"""
HelpTrickBD Professional 16:9 Banner & Thumbnail Generator
Creates high-resolution (1200x675) educational banner cards for Blogger posts
with custom topic gradients, clean typography, category badges, feature pills, and brand marks.
"""

import math
import os
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "assets", "fonts", "NotoSansBengali.ttf"))
OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "assets", "images", "posts"))
os.makedirs(OUTPUT_DIR, exist_ok=True)


def create_linear_gradient(width, height, start_color, end_color, angle_deg=35):
    """Creates a smooth linear gradient background."""
    base = Image.new("RGB", (width, height), start_color)
    top = Image.new("RGB", (width, height), end_color)
    mask = Image.new("L", (width, height))
    mask_data = []

    rad = math.radians(angle_deg)
    cos_val = math.cos(rad)
    sin_val = math.sin(rad)

    # Normalize across diagonal
    max_proj = width * abs(cos_val) + height * abs(sin_val)

    for y in range(height):
        for x in range(width):
            proj = (x * cos_val + y * sin_val)
            factor = max(0.0, min(1.0, proj / max_proj))
            mask_data.append(int(factor * 255))

    mask.putdata(mask_data)
    return Image.composite(top, base, mask)


def draw_geometric_accents(draw, width, height, accent_color=(255, 255, 255, 20)):
    """Draws subtle modern geometric lines and circular glow accents."""
    # Diagonal subtle lines
    for i in range(-height, width + height, 80):
        draw.line([(i, 0), (i + height, height)], fill=accent_color, width=1)
    
    # Outer decorative corner markers
    padding = 24
    draw.rectangle([padding, padding, width - padding, height - padding], outline=(255, 255, 255, 45), width=2)
    draw.rectangle([padding + 6, padding + 6, width - padding - 6, height - padding - 6], outline=(255, 255, 255, 20), width=1)


def wrap_text(text, font, max_width, draw):
    """Wraps Bengali text to fit within max_width."""
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        test_line = " ".join(current_line + [word])
        bbox = draw.textbbox((0, 0), test_line, font=font)
        w = bbox[2] - bbox[0]
        if w <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(" ".join(current_line))
            current_line = [word]
    if current_line:
        lines.append(" ".join(current_line))
    return lines


def generate_banner(
    filename,
    category_text,
    title_text,
    subtitle_text,
    features,
    start_color=(15, 32, 67),     # Deep Navy
    end_color=(40, 116, 240),     # Vibrant Blue
    accent_color=(255, 193, 7)    # Gold
):
    """Generates and saves a 1200x675 16:9 featured banner."""
    width, height = 1200, 675
    img = create_linear_gradient(width, height, start_color, end_color)
    
    # Overlay for RGBA drawing
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # Decorative geometry
    draw_geometric_accents(draw, width, height, accent_color=(255, 255, 255, 16))

    # Top Brand Bar
    brand_font = ImageFont.truetype(FONT_PATH, 24)
    cat_font = ImageFont.truetype(FONT_PATH, 22)
    title_font = ImageFont.truetype(FONT_PATH, 54)
    sub_font = ImageFont.truetype(FONT_PATH, 26)
    feat_font = ImageFont.truetype(FONT_PATH, 20)

    # Brand pill (Top Left)
    draw.rounded_rectangle([60, 50, 370, 95], radius=22, fill=(255, 255, 255, 35), outline=(255, 255, 255, 80), width=1)
    draw.text((80, 58), "HelpTrickBD | helptrickbd.com", fill=(255, 255, 255, 230), font=brand_font)

    # Category badge (Top Right)
    cat_bbox = draw.textbbox((0, 0), category_text, font=cat_font)
    cat_w = cat_bbox[2] - cat_bbox[0]
    badge_x1 = width - 60 - cat_w - 40
    badge_x2 = width - 60
    draw.rounded_rectangle([badge_x1, 50, badge_x2, 95], radius=22, fill=(accent_color[0], accent_color[1], accent_color[2], 230))
    draw.text((badge_x1 + 20, 58), category_text, fill=(20, 20, 20), font=cat_font)

    # Center Glass Card
    card_x1, card_y1, card_x2, card_y2 = 60, 130, width - 60, 540
    draw.rounded_rectangle([card_x1, card_y1, card_x2, card_y2], radius=16, fill=(0, 0, 0, 60), outline=(255, 255, 255, 40), width=2)

    # Title rendering (with drop shadow)
    lines = wrap_text(title_text, title_font, card_x2 - card_x1 - 80, draw)
    title_y = card_y1 + 45
    line_height = 76

    for line in lines:
        # Shadow
        draw.text((card_x1 + 42, title_y + 3), line, fill=(0, 0, 0, 140), font=title_font)
        # Main text
        draw.text((card_x1 + 40, title_y), line, fill=(255, 255, 255, 255), font=title_font)
        title_y += line_height

    # Subtitle
    if subtitle_text:
        title_y += 10
        draw.text((card_x1 + 42, title_y + 2), subtitle_text, fill=(0, 0, 0, 120), font=sub_font)
        draw.text((card_x1 + 40, title_y), subtitle_text, fill=(220, 235, 255, 240), font=sub_font)

    # Feature Badges at Bottom of Card
    badge_x = card_x1 + 40
    badge_y = card_y2 - 65
    for feat in features:
        fb = draw.textbbox((0, 0), feat, font=feat_font)
        fw = fb[2] - fb[0]
        draw.rounded_rectangle([badge_x, badge_y, badge_x + fw + 28, badge_y + 40], radius=12, fill=(255, 255, 255, 25), outline=(255, 255, 255, 60), width=1)
        draw.text((badge_x + 14, badge_y + 8), feat, fill=(255, 255, 255, 240), font=feat_font)
        badge_x += fw + 44

    # Bottom Footer Note
    draw.text((65, 595), "© HelpTrickBD Smart Education Platform | সর্বস্বত্ব সংরক্ষিত ২০২৬", fill=(255, 255, 255, 160), font=feat_font)
    draw.text((width - 320, 595), "⭐ ১০০% সিলেবাস ও পরীক্ষা সহায়ক", fill=(accent_color[0], accent_color[1], accent_color[2], 220), font=feat_font)

    # Merge overlay
    final_img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    out_file = os.path.join(OUTPUT_DIR, filename)
    final_img.save(out_file, quality=92)
    print(f"  [+] Banner generated: {out_file} ({os.path.getsize(out_file)} bytes)")

    # Auto-generate ultra-optimized 10-20 KB WebP for Core Web Vitals
    try:
        sys_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        if sys_path not in sys.path:
            sys.path.insert(0, sys_path)
        from tools.image_optimizer.webp_compressor import compress_to_target_webp
        webp_file = os.path.splitext(out_file)[0] + ".webp"
        compress_to_target_webp(out_file, webp_file, target_min_kb=10.0, target_max_kb=20.0)
        print(f"  [⚡ WebP] 10-20KB Optimized: {webp_file} ({os.path.getsize(webp_file) / 1024.0:.1f} KB)")
    except Exception as e:
        print(f"  [!] WebP compression skipped: {e}")
    return out_file


if __name__ == "__main__":
    test_out = generate_banner(
        "test-banner.jpg",
        "🎓 রাষ্ট্রবিজ্ঞান স্পেশাল",
        "পিতৃতন্ত্র কাকে বলে? সংজ্ঞা, বৈশিষ্ট্য, প্রভাব ও নারীবাদী তত্ত্ব",
        "অনার্স ও মাস্টার্স সমাজবিজ্ঞান এবং রাষ্ট্রবিজ্ঞান বিষয়ের পূর্ণাঙ্গ স্পেশাল হ্যান্ডনোট",
        ["📌 প্রামাণ্য সংজ্ঞা", "📊 প্রভাব ও বিশ্লেষণ", "📝 বিসিএস মডেল টেস্ট", "⚡ সংস্করণ ২০২৬"],
        start_color=(38, 12, 64),
        end_color=(136, 14, 79),
        accent_color=(255, 213, 79)
    )
    print("Test banner ready:", test_out)
