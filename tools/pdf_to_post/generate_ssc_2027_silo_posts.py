#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/pdf_to_post/generate_ssc_2027_silo_posts.py
--------------------------------------------------
Master pipeline generator for all 5 SSC 2027 English 1st Paper Silo Posts.
Uses modular builders for Part 01 through Part 05:
  Part 01: silo_01_builder.py (Seen Passage Q1-3)
  Part 02: silo_02_builder.py (Unseen Passage & Summary Q4-5)
  Part 03: silo_03_builder.py (Sentence Matching & Re-arrange Q6-7)
  Part 04: silo_04_builder.py (Poems & Stories Q/A Q8-9)
  Part 05: silo_05_builder.py (Completing Story & Dialogue Writing Q10-11)
"""

import os
import sys
import json

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Ensure local directory is on python path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from silo_01_builder import build_post as build_silo_01
from silo_02_builder import build_post as build_silo_02
from silo_03_builder import build_post as build_silo_03
from silo_04_builder import build_post as build_silo_04
from silo_05_builder import build_post as build_silo_05

PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))
RAW_POSTS_DIR = os.path.join(PROJECT_ROOT, "scratch", "raw_posts")
os.makedirs(RAW_POSTS_DIR, exist_ok=True)

def main():
    builders = [
        ("silo_01_seen_passage", build_silo_01),
        ("silo_02_unseen_summary", build_silo_02),
        ("silo_03_matching_rearrange", build_silo_03),
        ("silo_04_poems_stories", build_silo_04),
        ("silo_05_story_dialogue", build_silo_05),
    ]

    print("=" * 70)
    print("SSC 2027 ENGLISH SILO SERIES — MODULAR CONTENT PIPELINE")
    print("=" * 70)

    generated = []
    for file_prefix, builder_fn in builders:
        slug, html_content, metadata = builder_fn()
        html_path = os.path.join(RAW_POSTS_DIR, f"ssc_2027_{file_prefix}.html")
        meta_path = os.path.join(RAW_POSTS_DIR, f"ssc_2027_{file_prefix}.json")

        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)

        word_count = len(html_content.split())
        print(f"  [OK] {slug}")
        print(f"       File: {html_path} ({word_count:,} words, {len(html_content):,} chars)")
        print(f"       Meta: {meta_path}")
        generated.append({"slug": slug, "html_path": html_path, "meta_path": meta_path, "word_count": word_count})

    print("\n" + "=" * 70)
    print(f"Successfully generated all {len(generated)} silo posts in: {RAW_POSTS_DIR}")
    print("=" * 70)
    return generated

if __name__ == "__main__":
    main()
