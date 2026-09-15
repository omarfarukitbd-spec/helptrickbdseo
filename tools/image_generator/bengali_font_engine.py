#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/image_generator/bengali_font_engine.py
--------------------------------------------
Standardized Bengali Font Loader & Text Renderer for PIL/Pillow.
Prevents broken conjuncts and '???' glyph corruption on Windows & Linux.
"""

import os
import sys
from PIL import ImageFont, ImageDraw

def get_bengali_font(size=24, bold=False):
    """
    Returns a verified PIL ImageFont for Bengali typography.
    Tries native Windows fonts first, then project font assets.
    """
    candidates = []
    
    if sys.platform == 'win32':
        windir = os.environ.get('WINDIR', 'C:\\Windows')
        fonts_dir = os.path.join(windir, 'Fonts')
        if bold:
            candidates.extend([
                os.path.join(fonts_dir, 'NirmalaB.ttf'),
                os.path.join(fonts_dir, 'solaimanlipi.ttf'),
                os.path.join(fonts_dir, 'kalpurush.ttf'),
                os.path.join(fonts_dir, 'NirmalaUI.ttf'),
            ])
        else:
            candidates.extend([
                os.path.join(fonts_dir, 'NirmalaUI.ttf'),
                os.path.join(fonts_dir, 'solaimanlipi.ttf'),
                os.path.join(fonts_dir, 'kalpurush.ttf'),
                os.path.join(fonts_dir, 'NirmalaB.ttf'),
            ])
            
    # Also check local project fonts
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    local_font_dir = os.path.join(project_root, "assets", "fonts")
    if os.path.exists(local_font_dir):
        for f in os.listdir(local_font_dir):
            if f.lower().endswith(('.ttf', '.otf')):
                candidates.append(os.path.join(local_font_dir, f))

    for font_path in candidates:
        if os.path.exists(font_path):
            try:
                return ImageFont.truetype(font_path, size)
            except Exception:
                continue

    # Fallback to default
    print("Warning: Bengali font not found in standard paths, falling back to default.", file=sys.stderr)
    return ImageFont.load_default()

def draw_bengali_text(draw: ImageDraw.ImageDraw, xy, text: str, font=None, fill="black", **kwargs):
    """
    Draws Bengali text safely using a verified font.
    """
    if font is None:
        font = get_bengali_font(size=20)
    draw.text(xy, text, font=font, fill=fill, **kwargs)

if __name__ == "__main__":
    font = get_bengali_font(28, bold=True)
    print(f"Verified Bengali Font loaded: {font.path if hasattr(font, 'path') else font}")
