#!/usr/bin/env python3
"""
tools/social_card_generator/social_card_builder.py
HelpTrickBD Professional Social Share Card & OpenGraph Asset Builder.

Generates high-contrast, click-magnetic 1200x630 (OG standard) social preview cards
for Facebook, WhatsApp, LinkedIn, Twitter/X link sharing.
Automatically compresses the output to strictly 10-20 KB WebP for ultra-fast Core Web Vitals.
Generates complete SEO OpenGraph & Twitter Card HTML meta tags.
"""

import os
import sys
import argparse
import math
from typing import List, Optional, Tuple
from PIL import Image, ImageDraw, ImageFont, ImageFilter

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

# Ensure project root in sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.image_optimizer.webp_compressor import compress_to_target_webp

FONT_BOLD = os.path.join(PROJECT_ROOT, "assets", "fonts", "HindSiliguri-Bold.ttf")
FONT_REGULAR = os.path.join(PROJECT_ROOT, "assets", "fonts", "NotoSansBengali.ttf")
BG_DIR = os.path.join(PROJECT_ROOT, "Thumbnail BG")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "assets", "images", "social_cards")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def create_gradient_canvas(
    width: int = 1200,
    height: int = 630,
    start_color: Tuple[int, int, int] = (15, 23, 42),   # Slate 900
    end_color: Tuple[int, int, int] = (30, 41, 59),     # Slate 800
    accent_glow: Tuple[int, int, int] = (14, 165, 233)  # Sky 500
) -> Image.Image:
    """Creates a sleek, modern dark gradient canvas with ambient radial glow."""
    base = Image.new("RGB", (width, height), start_color)
    top = Image.new("RGB", (width, height), end_color)
    mask = Image.new("L", (width, height))
    mask_data = []

    angle_rad = math.radians(40)
    cos_a, sin_a = math.cos(angle_rad), math.sin(angle_rad)
    max_d = width * abs(cos_a) + height * abs(sin_a)

    for y in range(height):
        for x in range(width):
            proj = x * cos_a + y * sin_a
            factor = max(0.0, min(1.0, proj / max_d))
            mask_data.append(int(factor * 255))
    mask.putdata(mask_data)
    canvas = Image.composite(top, base, mask)

    # Ambient radial glow top-right
    glow = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    gx, gy, gr = width - 150, 100, 320
    for r in range(gr, 0, -8):
        alpha = int(35 * (1.0 - (r / gr) ** 1.5))
        glow_draw.ellipse(
            [gx - r, gy - r, gx + r, gy + r],
            fill=(accent_glow[0], accent_glow[1], accent_glow[2], alpha)
        )
    canvas = Image.alpha_composite(canvas.convert("RGBA"), glow).convert("RGB")
    return canvas


def wrap_text_bengali(text: str, font: ImageFont.FreeTypeFont, max_width: int, draw: ImageDraw.Draw) -> List[str]:
    """Wraps text cleanly within max_width."""
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


def generate_social_card(
    title: str,
    category: str = "শিক্ষা ও ক্যারিয়ার",
    read_time: str = "৫ মিনিট পাঠ",
    filename: Optional[str] = None,
    custom_bg_name: Optional[str] = None,
    site_brand: str = "HelpTrickBD.com",
    edition_text: str = "২০২৬ বিশেষ গাইড"
) -> Tuple[str, str, float]:
    """
    Builds a 1200x630 social card and compresses it to 10-20 KB WebP.
    
    Returns:
        (high_res_png_path, optimized_webp_path, webp_size_kb)
    """
    width, height = 1200, 630
    
    # Background choice
    if custom_bg_name:
        bg_path = os.path.join(BG_DIR, custom_bg_name)
        if os.path.exists(bg_path):
            with Image.open(bg_path) as bg_img:
                canvas = bg_img.convert("RGB").resize((width, height), Image.Resampling.LANCZOS)
                # Darken slightly for readability
                overlay_dark = Image.new("RGBA", (width, height), (15, 23, 42, 160))
                canvas = Image.alpha_composite(canvas.convert("RGBA"), overlay_dark).convert("RGB")
        else:
            canvas = create_gradient_canvas(width, height)
    else:
        canvas = create_gradient_canvas(width, height)

    # Drawing layer
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # Decorative Border / Card Frame
    pad = 24
    draw.rounded_rectangle([pad, pad, width - pad, height - pad], radius=16, outline=(255, 255, 255, 35), width=2)
    draw.rounded_rectangle([pad + 6, pad + 6, width - pad - 6, height - pad - 6], radius=12, outline=(255, 255, 255, 15), width=1)

    # Fonts
    font_path_bold = FONT_BOLD if os.path.exists(FONT_BOLD) else FONT_REGULAR
    font_path_reg = FONT_REGULAR if os.path.exists(FONT_REGULAR) else FONT_BOLD

    font_brand = ImageFont.truetype(font_path_bold, 24)
    font_cat = ImageFont.truetype(font_path_bold, 22)
    font_title = ImageFont.truetype(font_path_bold, 50)
    font_meta = ImageFont.truetype(font_path_reg, 22)

    # 1. Header Bar
    # Brand Pill (Left)
    draw.rounded_rectangle([60, 50, 310, 95], radius=12, fill=(14, 165, 233, 40), outline=(14, 165, 233, 140), width=1)
    draw.text((78, 58), f"🌐 {site_brand}", fill=(255, 255, 255, 245), font=font_brand)

    # Category Pill (Right)
    cat_text = f"🏷️ {category}"
    cbox = draw.textbbox((0, 0), cat_text, font=font_cat)
    c_w = cbox[2] - cbox[0]
    draw.rounded_rectangle([width - 80 - c_w - 30, 50, width - 60, 95], radius=12, fill=(245, 158, 11, 40), outline=(245, 158, 11, 140), width=1)
    draw.text((width - 80 - c_w - 15, 58), cat_text, fill=(253, 230, 138, 245), font=font_cat)

    # 2. Main Title (Wrapped with high contrast and text drop-shadow)
    max_title_w = width - 150
    title_lines = wrap_text_bengali(title, font_title, max_title_w, draw)
    
    # Vertically center title area
    line_h = 68
    total_title_h = len(title_lines) * line_h
    start_y = max(160, int((height - total_title_h) / 2) - 30)

    for i, line in enumerate(title_lines):
        ly = start_y + (i * line_h)
        # Drop shadow for readable contrast against any background
        draw.text((67, ly + 3), line, fill=(0, 0, 0, 180), font=font_title)
        draw.text((65, ly), line, fill=(255, 255, 255, 255), font=font_title)

    # 3. Highlight Accent Line
    sep_y = start_y + total_title_h + 20
    draw.line([(65, sep_y), (260, sep_y)], fill=(14, 165, 233, 220), width=4)

    # 4. Footer Badges & Meta
    footer_y = height - 95
    # Read time pill
    rt_text = f"⏱️ {read_time}"
    rt_box = draw.textbbox((0, 0), rt_text, font=font_meta)
    rt_w = rt_box[2] - rt_box[0]
    draw.rounded_rectangle([65, footer_y, 65 + rt_w + 24, footer_y + 40], radius=8, fill=(255, 255, 255, 20), outline=(255, 255, 255, 50), width=1)
    draw.text((77, footer_y + 8), rt_text, fill=(226, 232, 240, 240), font=font_meta)

    # Edition badge
    ed_x = 65 + rt_w + 40
    ed_text = f"⭐ {edition_text}"
    ed_box = draw.textbbox((0, 0), ed_text, font=font_meta)
    ed_w = ed_box[2] - ed_box[0]
    draw.rounded_rectangle([ed_x, footer_y, ed_x + ed_w + 24, footer_y + 40], radius=8, fill=(16, 185, 129, 35), outline=(16, 185, 129, 120), width=1)
    draw.text((ed_x + 12, footer_y + 8), ed_text, fill=(167, 243, 208, 240), font=font_meta)

    # Right footer attribution
    draw.text((width - 320, footer_y + 8), "🔗 helptrickbd.com", fill=(148, 163, 184, 220), font=font_brand)

    # Compose final image
    final_img = Image.alpha_composite(canvas.convert("RGBA"), overlay).convert("RGB")
    
    if not filename:
        clean_name = "".join(c if c.isalnum() else "_" for c in title[:30]).strip("_")
        filename = f"card_{clean_name}.png"

    png_path = os.path.join(OUTPUT_DIR, filename)
    final_img.save(png_path, format="PNG", optimize=True)

    # Auto-compress to strict 10-20 KB WebP
    webp_path = os.path.splitext(png_path)[0] + ".webp"
    compressed_path, final_size_kb = compress_to_target_webp(
        png_path,
        webp_path,
        target_min_kb=10.0,
        target_max_kb=20.0,
        max_width=1200,
        max_height=630
    )

    return png_path, compressed_path, final_size_kb


def generate_og_tags(
    title: str,
    description: str,
    image_url: str,
    canonical_url: str,
    category: str = "Article",
    site_name: str = "HelpTrickBD"
) -> str:
    """Returns clean, fully validated OpenGraph and Twitter Card HTML meta tags."""
    return f"""<!-- OpenGraph & Twitter Card SEO Meta Tags (Generated by HelpTrickBD Suite) -->
<meta property="og:type" content="article" />
<meta property="og:site_name" content="{site_name}" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{description}" />
<meta property="og:url" content="{canonical_url}" />
<meta property="og:image" content="{image_url}" />
<meta property="og:image:secure_url" content="{image_url}" />
<meta property="og:image:type" content="image/webp" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:image:alt" content="{title}" />
<meta property="article:section" content="{category}" />

<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{title}" />
<meta name="twitter:description" content="{description}" />
<meta name="twitter:image" content="{image_url}" />
<meta name="twitter:image:alt" content="{title}" />
"""


def main():
    parser = argparse.ArgumentParser(description="HelpTrickBD Social Share Card & OpenGraph Builder")
    parser.add_argument("--title", "-t", type=str, default="পুরুষতন্ত্র কাকে বলে? সংজ্ঞা, বৈশিষ্ট্য, প্রভাব ও সহজ ব্যাখ্যা", help="Post Bengali Title")
    parser.add_argument("--category", "-c", type=str, default="সমাজবিজ্ঞান ও রাষ্ট্রবিজ্ঞান", help="Article Category")
    parser.add_argument("--read_time", "-r", type=str, default="৬ মিনিট পাঠ", help="Reading time string")
    parser.add_argument("--bg", type=str, default=None, help="Optional background image filename from 'Thumbnail BG/'")
    parser.add_argument("--output", "-o", type=str, default=None, help="Output filename (PNG)")
    parser.add_argument("--url", type=str, default="https://www.helptrickbd.com/sample-post.html", help="Post URL for meta tag generation")
    parser.add_argument("--desc", type=str, default="সহজ ও প্রাঞ্জল ভাষায় পুরুষতন্ত্রের পূর্ণাঙ্গ সংজ্ঞা ও বিশদ আলোচনা।", help="Meta Description")

    args = parser.parse_args()

    print(f"\n=======================================================")
    print(f"  HelpTrickBD Social Card Generator (10-20KB WebP)")
    print(f"=======================================================")
    print(f"  Title: {args.title}")
    print(f"  Category: {args.category}")
    print(f"  Read Time: {args.read_time}")

    png_path, webp_path, size_kb = generate_social_card(
        title=args.title,
        category=args.category,
        read_time=args.read_time,
        filename=args.output,
        custom_bg_name=args.bg
    )

    print(f"\n[+] Master PNG Saved: {png_path}")
    print(f"[⚡] Ultra WebP Generated: {webp_path} ({size_kb:.2f} KB) - Perfect for CWV & Fast Link Previews!")

    # Print OG tags snippet
    img_filename = os.path.basename(webp_path)
    mock_img_url = f"https://www.helptrickbd.com/images/{img_filename}"
    og_html = generate_og_tags(
        title=args.title,
        description=args.desc,
        image_url=mock_img_url,
        canonical_url=args.url,
        category=args.category
    )

    print("\n--- Generated OpenGraph HTML Meta Block ---")
    print(og_html)


if __name__ == "__main__":
    main()
