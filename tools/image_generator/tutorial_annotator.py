#!/usr/bin/env python3
"""
HelpTrickBD - Tutorial Screenshot Annotator Tool
Adds high-contrast visual markers, red highlight bounding boxes, pointer arrows,
and numbered step badges to tutorial interface screenshots so users can clearly see
where to click on any website, portal, or software interface.
"""

import math
import os
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
FONT_PATH = os.path.join(PROJECT_ROOT, "assets", "fonts", "NotoSansBengali.ttf")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "assets", "images", "tutorials")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def get_font(size=20):
    """Loads font safely or falls back to default."""
    if os.path.exists(FONT_PATH):
        try:
            return ImageFont.truetype(FONT_PATH, size)
        except Exception:
            pass
    return ImageFont.load_default()


def draw_arrow(draw, start, end, fill="#dc2626", width=4, arrow_len=18, arrow_angle=30):
    """Draws a crisp directional arrow from start to end."""
    draw.line([start, end], fill=fill, width=width)
    
    # Calculate arrowhead angle
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    angle = math.atan2(dy, dx)
    
    rad1 = angle + math.pi - math.radians(arrow_angle)
    rad2 = angle + math.pi + math.radians(arrow_angle)
    
    p1 = (end[0] + arrow_len * math.cos(rad1), end[1] + arrow_len * math.sin(rad1))
    p2 = (end[0] + arrow_len * math.cos(rad2), end[1] + arrow_len * math.sin(rad2))
    
    draw.polygon([end, p1, p2], fill=fill)


def annotate_screenshot(
    image_input,
    target_box,
    step_number=1,
    action_label="এখানে ক্লিক করুন",
    output_filename=None,
    marker_color="#dc2626",      # Vibrant Red
    badge_bg="#b91c1c",          # Deep Crimson Red
    badge_text_color="#ffffff",
    draw_pointer_arrow=True,
    arrow_start_offset=(-60, -50),
):
    """
    Annotates an original interface image with:
    - Glowing rounded red box around the click target
    - Numbered pill badge (e.g. '❶ ধাপ ১: এখানে ক্লিক করুন')
    - Directional arrow pointing directly at the button/link
    
    target_box: tuple of (x1, y1, x2, y2) defining the clickable button/area.
    """
    if isinstance(image_input, str):
        base_img = Image.open(image_input).convert("RGBA")
    else:
        base_img = image_input.convert("RGBA")

    w, h = base_img.size
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    x1, y1, x2, y2 = target_box
    pad = 4
    x1 -= pad
    y1 -= pad
    x2 += pad
    y2 += pad

    # 1. Draw semi-transparent focus ring / outer glow
    glow_box = [x1 - 3, y1 - 3, x2 + 3, y2 + 3]
    draw.rounded_rectangle(glow_box, radius=8, outline=(220, 38, 38, 90), width=4)

    # 2. Main High-contrast Target Click Box
    draw.rounded_rectangle([x1, y1, x2, y2], radius=6, outline=marker_color, width=3)

    # 3. Floating Step Badge (Pill)
    font_bold = get_font(size=18)
    badge_text = f"● ধাপ {step_number}: {action_label}" if "ধাপ" not in action_label else f"● {action_label}"
    
    bbox = draw.textbbox((0, 0), badge_text, font=font_bold)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    
    badge_pad_x = 14
    badge_pad_y = 8
    badge_total_w = text_w + (badge_pad_x * 2)
    badge_total_h = text_h + (badge_pad_y * 2)

    # Decide badge position (above target if space allows, otherwise below)
    if y1 - badge_total_h - 15 > 10:
        bx1 = max(10, min(x1, w - badge_total_w - 10))
        by1 = y1 - badge_total_h - 14
    else:
        bx1 = max(10, min(x1, w - badge_total_w - 10))
        by1 = y2 + 14

    bx2 = bx1 + badge_total_w
    by2 = by1 + badge_total_h

    # Drop shadow for badge
    draw.rounded_rectangle([bx1 + 2, by1 + 2, bx2 + 2, by2 + 2], radius=8, fill=(0, 0, 0, 90))
    # Main badge background
    draw.rounded_rectangle([bx1, by1, bx2, by2], radius=8, fill=badge_bg, outline="#ffffff", width=2)
    # Badge text
    draw.text((bx1 + badge_pad_x, by1 + badge_pad_y - 2), badge_text, fill=badge_text_color, font=font_bold)

    # 4. Optional Arrow pointing from badge to target
    if draw_pointer_arrow:
        arrow_start = (bx1 + badge_total_w // 2, by2 if by1 < y1 else by1)
        arrow_end = ((x1 + x2) // 2, y1 if by1 < y1 else y2)
        draw_arrow(draw, arrow_start, arrow_end, fill=marker_color, width=3, arrow_len=14)

    # Combine overlay with base image
    annotated = Image.alpha_composite(base_img, overlay).convert("RGB")

    if output_filename:
        if not output_filename.endswith((".png", ".jpg", ".webp")):
            output_filename += ".png"
        out_path = os.path.join(OUTPUT_DIR, output_filename)
        annotated.save(out_path, optimize=True)
        print(f"✅ Annotated Tutorial Image Saved: {out_path}")
        return out_path

    return annotated


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


def annotate_with_html(
    image_path,
    target_box,
    step_number=1,
    action_label="এখানে ক্লিক করুন",
    output_filename=None,
    color="#dc2626",
):
    """
    Overlays a glowing click-target box, red badge, and pointer using Chrome Headless.
    Ensures 100% flawless Bengali typography (Hind Siliguri) and high-DPI quality.
    target_box: (x1, y1, x2, y2)
    """
    import subprocess
    import tempfile

    if not CHROME_PATH:
        # Fallback to PIL
        return annotate_screenshot(image_path, target_box, step_number, action_label, output_filename)

    with Image.open(image_path) as im:
        img_w, img_h = im.size

    x1, y1, x2, y2 = target_box
    w = x2 - x1
    h = y2 - y1

    # Position badge above target if space exists, else below
    badge_top = (y1 - 42) if y1 > 50 else (y2 + 15)
    badge_left = max(10, x1)

    abs_img_path = os.path.abspath(image_path).replace(os.sep, "/")

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@600;700&display=swap" rel="stylesheet">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: {img_w}px;
    height: {img_h}px;
    overflow: hidden;
    position: relative;
    background: transparent;
    font-family: 'Hind Siliguri', sans-serif;
  }}
  .bg-img {{
    position: absolute;
    top: 0;
    left: 0;
    width: {img_w}px;
    height: {img_h}px;
    display: block;
  }}
  .click-box {{
    position: absolute;
    left: {x1 - 4}px;
    top: {y1 - 4}px;
    width: {w + 8}px;
    height: {h + 8}px;
    border: 3px solid {color};
    border-radius: 8px;
    box-shadow: 0 0 0 3px rgba(220, 38, 38, 0.3), 0 4px 14px rgba(220, 38, 38, 0.45);
    z-index: 10;
    pointer-events: none;
  }}
  .step-pill {{
    position: absolute;
    left: {badge_left}px;
    top: {badge_top}px;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: {color};
    color: #ffffff;
    padding: 6px 16px;
    border-radius: 24px;
    border: 2px solid #ffffff;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.28);
    font-size: 16px;
    font-weight: 700;
    z-index: 20;
  }}
  .arrow-down {{
    position: absolute;
    left: {x1 + (w // 2) - 8}px;
    top: {y1 - 14}px;
    width: 0;
    height: 0;
    border-left: 8px solid transparent;
    border-right: 8px solid transparent;
    border-top: 12px solid {color};
    z-index: 25;
  }}
</style>
</head>
<body>
  <img class="bg-img" src="file:///{abs_img_path}">
  <div class="click-box"></div>
  <div class="step-pill">
    <span>● ধাপ {step_number}:</span>
    <span>{action_label}</span>
  </div>
  <div class="arrow-down"></div>
</body>
</html>"""

    if not output_filename:
        output_filename = f"annotated_step_{step_number}.png"
    if not output_filename.endswith((".png", ".jpg", ".webp")):
        output_filename += ".png"

    out_path = os.path.join(OUTPUT_DIR, output_filename)

    with tempfile.NamedTemporaryFile(suffix=".html", delete=False, mode="w", encoding="utf-8") as tf:
        tf.write(html)
        temp_html = tf.name

    try:
        cmd = [
            CHROME_PATH,
            "--headless=new",
            "--disable-gpu",
            "--hide-scrollbars",
            f"--window-size={img_w},{img_h}",
            f"--screenshot={out_path}",
            f"file:///{temp_html.replace(os.sep, '/')}",
        ]
        subprocess.run(cmd, check=True, capture_output=True)

        with Image.open(out_path) as im:
            im.save(out_path, optimize=True)

        print(f"✅ High-DPI Tutorial Screenshot Created: {out_path}")
        return out_path
    finally:
        if os.path.exists(temp_html):
            os.remove(temp_html)


if __name__ == "__main__":
    print("Tutorial Screenshot Annotator Ready.")

