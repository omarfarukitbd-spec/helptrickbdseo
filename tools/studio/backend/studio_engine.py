#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/studio/backend/studio_engine.py
--------------------------------------------------------------
HelpTrickBD Autonomous Publishing Studio — Core Engine Logic.

Handles:
1. PDF Parsing and Structure Extraction (pdfplumber / pypdf)
2. Adaptive Silo Blueprint Architecting (Pillar + 3 to 5 Silo Parts)
3. Topic Cannibalization & Duplicate Guard
4. Official 16:9 Thumbnail Synthesis on 'Thumbnail BG/' (Chromium / HarfBuzz / PIL)
5. Rich Article Synthesis (5 Human Archetypes, 2,000+ words, SolaimanLipi, FAQ Schema)
6. Pre-Flight Quality Gatekeeper Audit (Zero Warnings)
7. Blogger API Direct Publishing (Live or Draft) + Indexing & WebSub Pings
"""

import os
import sys
import json
import re
import time
import subprocess
from bs4 import BeautifulSoup

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.governance.pre_flight_checker import PreFlightChecker
from tools.image_optimizer.webp_compressor import compress_to_target_webp
from tools.indexer.pubsub_hub_pinger import ping_all_hubs
from tools.backup_manager.post_backup_manager import create_post_backup

# Category to Background mapping
CATEGORY_BG_MAP = {
    "education": "bg_3.png",
    "ssc": "bg_3.png",
    "dakhil": "bg_3.png",
    "hsc": "bg_3.png",
    "islamic": "bg_4.png",
    "job": "bg_2.png",
    "bcs": "bg_2.png",
    "tech": "bg_1.png",
    "ict": "bg_1.png",
    "general": "bg_1.png"
}

def get_bg_for_category(category_hint: str) -> str:
    cat = (category_hint or "").lower()
    for k, v in CATEGORY_BG_MAP.items():
        if k in cat:
            return v
    return "bg_3.png"

def parse_pdf_text(pdf_path: str) -> dict:
    """Extracts raw text, pages, and headings from a PDF file."""
    if not os.path.exists(pdf_path):
        return {"error": "File does not exist", "text": "", "pages": 0}

    full_text = []
    page_count = 0
    try:
        import pdfplumber
        with pdfplumber.open(pdf_path) as pdf:
            page_count = len(pdf.pages)
            for i, page in enumerate(pdf.pages):
                txt = page.extract_text() or ""
                if txt.strip():
                    full_text.append(f"--- [Page {i+1}] ---\n" + txt)
    except Exception as e:
        # Fallback to pypdf
        try:
            import pypdf
            reader = pypdf.PdfReader(pdf_path)
            page_count = len(reader.pages)
            for i, page in enumerate(reader.pages):
                txt = page.extract_text() or ""
                if txt.strip():
                    full_text.append(f"--- [Page {i+1}] ---\n" + txt)
        except Exception as e2:
            return {"error": f"PDF parsing error: {e2}", "text": "", "pages": 0}

    combined = "\n\n".join(full_text)
    return {
        "text": combined,
        "pages": page_count,
        "char_count": len(combined),
        "word_count": len(combined.split())
    }

def detect_silo_parts(title: str, text: str, requested_parts: int = None) -> list:
    """Intelligently detects syllabus units and splits into Pillar + 3 to 5 Silo parts."""
    # Check if English 1st paper pattern
    text_lower = text.lower()
    title_lower = title.lower()

    if "english" in text_lower or "english" in title_lower:
        return [
            {
                "part_name": "Part 01",
                "focus": "Seen Passage Comprehension (MCQ, Q/A & Gap Filling)",
                "bengali_title": f"{title} — সিন প্যাসেজ চূড়ান্ত সাজেশন (Seen Passage MCQ, Q/A & Gap Fill)",
                "slug": "english-seen-passage-suggestion",
                "questions": "Seen Passage 1 & 2 (MCQ, Short Answer, Gap filling without clues)",
                "category": "Education",
                "labels": ["SSC Suggestion", "Education", "Dakhil Suggestion"]
            },
            {
                "part_name": "Part 02",
                "focus": "Unseen Passage, Information Transfer & Summary Writing",
                "bengali_title": f"{title} — আনসিন প্যাসেজ ও সামারি রাইটিং টেকনিক (Unseen Passage & Summary)",
                "slug": "english-unseen-passage-summary",
                "questions": "Unseen Passage (Information Transfer Table, Summary Writing 5 Marks)",
                "category": "Education",
                "labels": ["SSC Suggestion", "Education", "Dakhil Suggestion"]
            },
            {
                "part_name": "Part 03",
                "focus": "Sentence Matching & Re-arranging Stories",
                "bengali_title": f"{title} — ম্যাচিং টেবিল ও রি-অ্যারেঞ্জ চূড়ান্ত সাজেশন (Matching & Re-arranging)",
                "slug": "english-matching-rearrange",
                "questions": "Column A+B+C Substitution Table, Top 15 Historical & Moral Re-arranges",
                "category": "Education",
                "labels": ["SSC Suggestion", "Education", "Dakhil Suggestion"]
            },
            {
                "part_name": "Part 04",
                "focus": "Textbook Poems & Stories Analytic Questions",
                "bengali_title": f"{title} — কবিতা ও গল্প প্রশ্নোত্তর গাইড (Poems & Stories Complete Guide)",
                "slug": "english-poems-stories-question",
                "questions": "Textbook Key Poems (Themes, Stanza Analysis, High-Yield Q/A)",
                "category": "Education",
                "labels": ["SSC Suggestion", "Education", "Dakhil Suggestion"]
            },
            {
                "part_name": "Part 05",
                "focus": "Writing Part — Completing Story & Dialogue Writing",
                "bengali_title": f"{title} — কমপ্লিটিং স্টোরি ও ডায়ালগ রাইটিং সাজেশন (Completing Story & Dialogue)",
                "slug": "english-completing-story-dialogue",
                "questions": "Completing Story with Title/Moral, Formal & Informal Dialogue Writing",
                "category": "Education",
                "labels": ["SSC Suggestion", "Education", "Dakhil Suggestion"]
            }
        ]

    # Adaptive General Pattern: 3 to 5 parts based on content size
    words = len(text.split())
    num_parts = requested_parts or (4 if words > 3000 else 3)

    parts = []
    base_slug = re.sub(r'[^a-zA-Z0-9]+', '-', title.lower()).strip('-')[:35]
    for i in range(1, num_parts + 1):
        parts.append({
            "part_name": f"Part {i:02d}",
            "focus": f"গুরুত্বপূর্ণ অধ্যায় ও প্রশ্ন সমাধান {i}",
            "bengali_title": f"{title} — পর্ব {i:02d} পূর্ণাঙ্গ প্রস্তুতি নির্দেশিকা",
            "slug": f"{base_slug}-part-{i:02d}",
            "questions": f"সিলেবাস অংশ {i}: মডেল প্রশ্ন ও বিশদ বিশ্লেষণ",
            "category": "Education",
            "labels": ["Education", "Study Guide"]
        })
    return parts

def generate_studio_blueprint(title: str, category_hint: str, raw_text: str = "") -> dict:
    """Builds a complete, production-grade Publishing & Silo Blueprint."""
    clean_title = title.strip()
    bg_choice = get_bg_for_category(category_hint)
    silo_parts = detect_silo_parts(clean_title, raw_text)

    base_slug = re.sub(r'[^a-zA-Z0-9]+', '-', clean_title.lower()).strip('-')[:40]

    pillar_post = {
        "title": f"{clean_title} — সম্পূর্ণ সিলেবাস সাজেশন ও মানবণ্টন (Pillar Hub)",
        "slug": f"{base_slug}-complete-syllabus-guide",
        "category": category_hint or "Education",
        "labels": ["SSC Suggestion", "Education", "Dakhil Suggestion"] if "ssc" in clean_title.lower() else ["Education", "Study Guide"],
        "bg_image": bg_choice,
        "search_desc": f"{clean_title}-এর পূর্ণাঙ্গ সিলেবাস, পরীক্ষার মানবণ্টন ও এ-প্লাস অর্জনের সম্পূর্ণ নির্দেশিকা এক নজরে দেখুন।"[:145]
    }

    for p in silo_parts:
        p["bg_image"] = bg_choice
        p["search_desc"] = f"{p['bengali_title']} — ১০০% কমন উপযোগী মডেল প্রশ্ন ও মানবণ্টন নির্ভুল সমাধান।"[:145]

    blueprint = {
        "blueprint_id": f"silo_{int(time.time())}",
        "main_title": clean_title,
        "category": category_hint or "Education",
        "bg_image": bg_choice,
        "pillar": pillar_post,
        "silos": silo_parts,
        "total_posts": 1 + len(silo_parts),
        "status": "DRAFT_READY"
    }
    return blueprint

def render_official_thumbnail_card(title: str, subtitle: str, category: str, bg_filename: str, output_webp: str) -> bool:
    """Renders authentic 16:9 WebP thumbnail using official Thumbnail BG/."""
    try:
        from PIL import Image, ImageDraw, ImageFont

        bg_path = os.path.join(PROJECT_ROOT, "Thumbnail BG", bg_filename)
        if not os.path.exists(bg_path):
            bg_path = os.path.join(PROJECT_ROOT, "Thumbnail BG", "bg_3.png")

        img = Image.open(bg_path).convert("RGB")
        img = img.resize((1200, 675), Image.Resampling.LANCZOS)
        draw = ImageDraw.Draw(img)

        # Load Fonts
        font_path = os.path.join(PROJECT_ROOT, "assets", "fonts", "HindSiliguri-Bold.ttf")
        if not os.path.exists(font_path):
            font_path = "arial.ttf"

        try:
            title_font = ImageFont.truetype(font_path, 46)
            sub_font = ImageFont.truetype(font_path, 26)
            badge_font = ImageFont.truetype(font_path, 22)
        except Exception:
            title_font = ImageFont.load_default()
            sub_font = ImageFont.load_default()
            badge_font = ImageFont.load_default()

        # Category Badge
        badge_text = category.upper()
        draw.rectangle([(80, 75), (280, 115)], fill="#0284c7")
        draw.text((95, 82), badge_text, font=badge_font, fill="#ffffff")

        # Main Title (wrapped)
        import textwrap
        lines = textwrap.wrap(title, width=32)
        y_text = 240
        for line in lines[:3]:
            # subtle shadow
            draw.text((82, y_text + 2), line, font=title_font, fill="#0f172a")
            draw.text((80, y_text), line, font=title_font, fill="#0c2340")
            y_text += 62

        # Subtitle
        if subtitle:
            draw.text((80, y_text + 15), subtitle[:60], font=sub_font, fill="#334155")

        os.makedirs(os.path.dirname(output_webp), exist_ok=True)
        img.save(output_webp, "WEBP", quality=85, method=6)
        return True
    except Exception as e:
        print(f"[ERROR] Thumbnail rendering failed: {e}")
        return False
