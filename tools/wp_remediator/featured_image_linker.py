#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/wp_remediator/featured_image_linker.py
--------------------------------------------
Automated Featured Image Linker for HelpTrickBD WordPress site.
Identifies the hero image from post HTML, ensures it exists in the WordPress
Media Library, and binds it as the post's native featured_media.
Zero-Emoji compliance (Rule 12).
"""

import os
import re
import sys
import json
import requests
from typing import Dict, Any, Optional
from bs4 import BeautifulSoup

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.wp_publisher.publisher import WordPressPublisher

POST_IMAGES_DIR = os.path.join(PROJECT_ROOT, "assets", "images", "posts")
SCRATCH_IMG_DIR = os.path.join(PROJECT_ROOT, "scratch", "downloaded_thumbnails")

class FeaturedImageLinker:
    def __init__(self, publisher: Optional[WordPressPublisher] = None):
        self.publisher = publisher or WordPressPublisher()
        self.client = self.publisher.client
        self.media_cache: Dict[str, int] = {}
        os.makedirs(SCRATCH_IMG_DIR, exist_ok=True)

    def extract_hero_image_info(self, raw_html: str) -> Optional[Dict[str, str]]:
        """Extracts the first image from post content as the hero image."""
        if not raw_html or "<img" not in raw_html:
            return None

        soup = BeautifulSoup(raw_html, "html.parser")
        first_img = soup.find("img")
        if not first_img or not first_img.get("src"):
            return None

        src = first_img["src"].strip()
        alt = first_img.get("alt", "").strip()
        title = first_img.get("title", "").strip()

        # Extract filename from URL (strip query parameters)
        clean_url = src.split("?")[0].split("#")[0]
        filename = os.path.basename(clean_url)

        return {
            "src": src,
            "filename": filename,
            "alt": alt,
            "title": title
        }

    def resolve_local_image_path(self, hero_info: Dict[str, str]) -> Optional[str]:
        """Finds local image file or downloads from CDN to scratch folder."""
        filename = hero_info["filename"]
        src = hero_info["src"]

        # 1. Check local assets/images/posts/
        local_path = os.path.join(POST_IMAGES_DIR, filename)
        if os.path.exists(local_path) and os.path.getsize(local_path) > 1000:
            return local_path

        # 1b. Check if WebP alternative exists locally
        base_name, _ = os.path.splitext(filename)
        webp_candidate = os.path.join(POST_IMAGES_DIR, f"{base_name}.webp")
        if os.path.exists(webp_candidate) and os.path.getsize(webp_candidate) > 1000:
            return webp_candidate

        # 2. Check scratch folder
        scratch_path = os.path.join(SCRATCH_IMG_DIR, filename)
        if os.path.exists(scratch_path) and os.path.getsize(scratch_path) > 1000:
            return scratch_path

        # 3. Download from remote URL
        if src.startswith("http://") or src.startswith("https://"):
            try:
                headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
                res = requests.get(src, headers=headers, timeout=15)
                if res.status_code == 200 and len(res.content) > 1000:
                    with open(scratch_path, "wb") as f:
                        f.write(res.content)
                    return scratch_path
            except Exception as e:
                print(f"[WARN] Failed to download hero image from {src}: {e}")

        return None

    def get_or_upload_media(self, local_path: str, alt_text: str = "", title: str = "") -> Optional[int]:
        """Uploads image to WordPress media library or retrieves cached media ID."""
        filename = os.path.basename(local_path)

        if filename in self.media_cache:
            return self.media_cache[filename]

        # Check if media with this slug/filename already exists on WordPress
        clean_slug = os.path.splitext(filename)[0]
        res = self.client.get("media", params={"search": clean_slug, "per_page": 5})
        if res.status_code == 200:
            media_items = res.json()
            for item in media_items:
                source_url = item.get("source_url", "")
                if filename in source_url or clean_slug in item.get("slug", ""):
                    media_id = item.get("id")
                    self.media_cache[filename] = media_id
                    return media_id

        # Upload new media
        media_id = self.publisher.upload_featured_image(
            file_path=local_path,
            alt_text=alt_text,
            title=title
        )

        if media_id:
            self.media_cache[filename] = media_id
            return media_id

        return None
