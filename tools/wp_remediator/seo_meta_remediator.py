#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/wp_remediator/seo_meta_remediator.py
-----------------------------------------
Automated Rank Math SEO Metadata Remediator for HelpTrickBD WordPress site.
Generates clean 140-155 character Bengali meta descriptions and attaches
pre-curated focus keywords from migration_log.json.
Zero-Emoji compliance (Rule 12).
"""

import os
import re
import sys
import json
from typing import Dict, Any, Optional
from bs4 import BeautifulSoup

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

MIGRATION_LOG_PATH = os.path.join(PROJECT_ROOT, "Helptrickbd Wp", "migration_log.json")

class SeoMetaRemediator:
    def __init__(self, migration_log_path: str = MIGRATION_LOG_PATH):
        self.migration_log_path = migration_log_path
        self.log_posts_by_slug = {}
        self.log_posts_by_title = {}
        self._load_migration_log()

    def _load_migration_log(self):
        """Loads migration log index for fast lookup of focus keywords."""
        if not os.path.exists(self.migration_log_path):
            return
        try:
            with open(self.migration_log_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for p in data.get("posts", []):
                    slug = p.get("slug", "")
                    title = p.get("title", "")
                    if slug:
                        self.log_posts_by_slug[slug] = p
                    if title:
                        self.log_posts_by_title[title.strip()] = p
        except Exception as e:
            print(f"[WARN] Error loading migration log for SEO metadata: {e}")

    def generate_meta_description(self, raw_html: str, target_length: int = 150) -> str:
        """
        Generates a clean 130-155 character Bengali meta description from the post content.
        Ensures sentences are not cut awkwardly mid-word.
        """
        soup = BeautifulSoup(raw_html, "html.parser")
        
        # Remove script, style, table tags, and blockquotes
        for elem in soup(["script", "style", "table", "pre", "code"]):
            elem.decompose()

        # Try to find text from paragraphs
        paragraphs = soup.find_all("p")
        text_corpus = ""
        for p in paragraphs:
            clean_p = p.get_text(" ", strip=True)
            # Skip very short paragraphs or author tags
            if len(clean_p) > 40:
                text_corpus += clean_p + " "
                if len(text_corpus) >= 300:
                    break

        if not text_corpus:
            text_corpus = soup.get_text(" ", strip=True)

        # Normalize whitespace
        text_corpus = re.sub(r"\s+", " ", text_corpus).strip()

        if len(text_corpus) <= target_length:
            return text_corpus

        # Split into Bengali sentences by '।'
        sentences = [s.strip() for s in text_corpus.split("।") if s.strip()]
        candidate = ""

        for s in sentences:
            if not candidate:
                candidate = s
            elif len(candidate) + len(s) + 2 <= target_length + 15:
                candidate += "। " + s
            else:
                break

        if len(candidate) >= 80:
            if not candidate.endswith("।"):
                candidate += "।"
            return candidate

        # Fallback word-boundary slice
        sliced = text_corpus[:target_length]
        last_space = sliced.rfind(" ")
        if last_space > 80:
            sliced = sliced[:last_space]

        return sliced.strip() + "..."

    def resolve_focus_keyword(self, post: Dict[str, Any]) -> str:
        """Finds or derives the optimal focus keyword for Rank Math."""
        slug = post.get("slug", "")
        title = post.get("title", {}).get("rendered", "") if isinstance(post.get("title"), dict) else str(post.get("title", ""))
        title = title.replace("&#8217;", "'").replace("&#038;", "&").strip()

        # 1. Lookup in migration log
        matched_log = self.log_posts_by_slug.get(slug) or self.log_posts_by_title.get(title)
        if matched_log and matched_log.get("focus_keyword"):
            return matched_log.get("focus_keyword").strip()

        # 2. Extract from title before separator (| or -)
        parts = re.split(r"[|\-–—:]", title)
        if parts:
            kw = parts[0].strip()
            # Remove year like 2025/2026
            kw = re.sub(r"\b202[4-9]\b", "", kw).strip()
            if len(kw) > 5:
                return kw

        return title[:50]

    def build_rank_math_meta(self, post: Dict[str, Any]) -> Dict[str, str]:
        """Builds Rank Math postmeta dictionary."""
        content = post.get("content", {}).get("rendered", "") if isinstance(post.get("content"), dict) else str(post.get("content", ""))
        meta_desc = self.generate_meta_description(content)
        focus_kw = self.resolve_focus_keyword(post)

        return {
            "rank_math_title": "%title% %sep% %sitename%",
            "rank_math_description": meta_desc,
            "rank_math_focus_keyword": focus_kw
        }
