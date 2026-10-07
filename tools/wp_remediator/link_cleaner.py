#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/wp_remediator/link_cleaner.py
-----------------------------------
Automated Internal Legacy Link Cleaner for HelpTrickBD WordPress site.
Converts Blogger-era internal URLs (.html) into clean WordPress permalinks (/%postname%/).
Zero-Emoji compliance (Rule 12).
"""

import os
import re
import sys
import json
from typing import Tuple, List, Dict, Any
from bs4 import BeautifulSoup

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

MIGRATION_LOG_PATH = os.path.join(PROJECT_ROOT, "Helptrickbd Wp", "migration_log.json")

# Special manual alias mappings identified during migration
KNOWN_ALIASES = {
    "ssc-english-2nd-paper-suggestion-2027": "ssc-english-2nd-paper-final-suggestion",
    "bcs-preliminary-marks-distribution-booklist": "bcs-preliminary-marks-distribution_01436475916",
    "remittance-importance": "what-is-remittance-importance-economy-obstacles",
    "basic-economy-problems-bd": "bangladesh-basic-economy-features-problems-solutions",
    "budget-importance": "what-is-budget-importance-role-economy",
    "nu-cgpa-calculator": "nu-cgpa-calculator",
    "bangladesh-population-features": "bangladesh-population-features-trends-challenges",
    "computer-types": "computer-types-classification-analog-digital-hybrid",
    "computer-generations": "computer-generations-first-to-fifth-technology",
    "computer-history": "computer-history-abacus-to-modern-processors",
    "computer-definition": "what-is-computer-definition-functions-components",
    "alim-exam-routine": "alim-exam-routine-2025-madrasah-board"
}

class InternalLinkCleaner:
    def __init__(self, migration_log_path: str = MIGRATION_LOG_PATH):
        self.migration_log_path = migration_log_path
        self.slug_map = self._build_slug_map()

    def _build_slug_map(self) -> Dict[str, str]:
        """Builds lookup table of old slugs to clean WordPress slugs."""
        slug_map = dict(KNOWN_ALIASES)
        if os.path.exists(self.migration_log_path):
            try:
                with open(self.migration_log_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    for p in data.get("posts", []):
                        slug = p.get("slug")
                        if slug:
                            # Map identity
                            slug_map[slug] = slug
                            # Also map normalized versions
                            norm = slug.replace("-", "")
                            slug_map[norm] = slug
            except Exception as e:
                print(f"[WARN] Could not parse migration_log.json: {e}")
        return slug_map

    def clean_content(self, html_content: str) -> Tuple[str, int, List[Dict[str, str]]]:
        """
        Parses HTML and rewrites legacy .html links to modern WordPress permalinks.
        Returns: (new_html, count_of_changes, change_log)
        """
        if not html_content or ".html" not in html_content:
            return html_content, 0, []

        soup = BeautifulSoup(html_content, "html.parser")
        changes = []
        replaced_count = 0

        # Pattern for extracting slug from Blogger URLs
        # Matches:
        # https://www.helptrickbd.com/2026/09/slug.html
        # https://helptrickbd.com/p/slug.html
        # /p/slug.html
        # /2026/09/slug.html
        # /slug.html
        blogger_pattern = re.compile(
            r"^(?:https?://(?:www\.)?helptrickbd\.com)?(?:/p/|/\d{4}/\d{2}/|/)?([a-zA-Z0-9_-]+)\.html(?:[?#].*)?$"
        )

        for a_tag in soup.find_all("a", href=True):
            href = a_tag["href"].strip()
            # Only process helptrickbd.com internal links or relative links ending in .html
            if "helptrickbd.com" not in href and not href.startswith("/") and not href.endswith(".html"):
                continue

            match = blogger_pattern.match(href)
            if match:
                old_slug = match.group(1)
                
                # Resolve target clean slug
                target_slug = self.slug_map.get(old_slug, old_slug)
                # Fallback check for normalized key
                if target_slug == old_slug and old_slug.replace("-", "") in self.slug_map:
                    target_slug = self.slug_map[old_slug.replace("-", "")]

                # Construct clean modern WordPress URL
                new_href = f"https://www.helptrickbd.com/{target_slug}/"

                if href != new_href:
                    a_tag["href"] = new_href
                    replaced_count += 1
                    changes.append({
                        "original": href,
                        "rewritten": new_href,
                        "anchor_text": a_tag.get_text(strip=True)[:40]
                    })

        new_html = str(soup) if replaced_count > 0 else html_content
        return new_html, replaced_count, changes
