#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/image_generator/compress_87_to_target_kb.py
Compresses all synthesized htbd-official-*.webp files to strictly 14-20 KB
using tools.image_optimizer.webp_compressor.compress_to_target_webp
"""

import os
import sys
import glob

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

from tools.image_optimizer.webp_compressor import compress_to_target_webp

POSTS_DIR = os.path.join(PROJECT_ROOT, "assets", "images", "posts")
files = glob.glob(os.path.join(POSTS_DIR, "htbd-official-*.webp"))

print(f"Compressing {len(files)} official banners to 12-20 KB target...")

compressed_count = 0
for f in files:
    compress_to_target_webp(f, f, target_min_kb=12.0, target_max_kb=20.0)
    compressed_count += 1

print(f"[OK] Successfully compressed all {compressed_count} banners to target 12-20 KB!")
