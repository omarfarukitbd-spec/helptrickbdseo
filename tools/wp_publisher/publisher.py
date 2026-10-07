#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/wp_publisher/publisher.py
--------------------------------
Master WordPress Publisher for HelpTrickBD.
Replaces the legacy Blogger publishing infrastructure with native
WordPress 6.7+ REST API calls.

Handles:
1. Category & Tag resolution / dynamic creation.
2. WebP Featured Image upload to WordPress Media Library (/wp-json/wp/v2/media).
3. Post creation and updating with clean English permalink slugs (/%postname%/).
4. Direct Rank Math SEO metadata binding (Title, Description, Focus Keyword).
5. Default post status management (safe 'draft' or instant 'publish').
"""

import os
import sys
import json
import mimetypes
from typing import Optional, List, Dict, Any

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.wp_publisher.wp_client import WordPressClient

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")
EXAMPLE_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.example.json")

class WordPressPublisher:
    def __init__(self, config_path: str = CONFIG_PATH):
        self.config = self._load_config(config_path)
        self.client = WordPressClient(
            base_url=self.config.get("wp_url", "https://www.helptrickbd.com"),
            username=self.config.get("wp_user", "admin"),
            app_password=self.config.get("wp_app_password", "")
        )
        self.default_status = self.config.get("default_status", "draft")

    def _load_config(self, path: str) -> dict:
        if not os.path.exists(path):
            if os.path.exists(EXAMPLE_CONFIG_PATH):
                with open(EXAMPLE_CONFIG_PATH, "r", encoding="utf-8") as f:
                    return json.load(f)
            return {
                "wp_url": "https://www.helptrickbd.com",
                "wp_user": "ayesha",
                "wp_app_password": "",
                "default_status": "draft",
                "rank_math_enabled": True
            }
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def test_connection(self) -> dict:
        """Tests WordPress REST API endpoint and authenticates user."""
        res = self.client.get("users/me")
        if res.status_code == 200:
            user_data = res.json()
            return {
                "success": True,
                "user_id": user_data.get("id"),
                "username": user_data.get("name"),
                "roles": user_data.get("roles", [])
            }
        return {
            "success": False,
            "status_code": res.status_code,
            "error": res.text
        }

    def upload_featured_image(self, file_path: str, alt_text: str = "", title: str = "") -> Optional[int]:
        """
        Uploads an image (WebP/PNG/JPG) to the WordPress Media Library and returns the attachment ID.
        """
        if not os.path.exists(file_path):
            print(f"[ERROR] Image not found: {file_path}")
            return None

        filename = os.path.basename(file_path)
        mime_type, _ = mimetypes.guess_type(file_path)
        if not mime_type:
            mime_type = "image/webp" if filename.endswith(".webp") else "image/jpeg"

        with open(file_path, "rb") as f:
            image_data = f.read()

        headers = {
            "Content-Type": mime_type,
            "Content-Disposition": f'attachment; filename="{filename}"'
        }

        # WordPress media endpoint requires binary payload with Content-Disposition header
        res = self.client.request(
            method="POST",
            endpoint="media",
            data=image_data,
            headers=headers
        )

        if res.status_code in (200, 201):
            media = res.json()
            media_id = media.get("id")

            # Update alt text and title if provided
            if alt_text or title:
                patch_payload = {}
                if alt_text:
                    patch_payload["alt_text"] = alt_text
                if title:
                    patch_payload["title"] = title
                self.client.post(f"media/{media_id}", json=patch_payload)

            return media_id

        print(f"[ERROR] Failed to upload media ({res.status_code}): {res.text}")
        return None

    def get_or_create_category(self, name: str, parent_id: Optional[int] = None) -> Optional[int]:
        """Finds existing category by name or creates a new one."""
        clean_name = name.strip()
        res = self.client.get("categories", params={"search": clean_name})
        if res.status_code == 200:
            items = res.json()
            for item in items:
                if item.get("name", "").lower() == clean_name.lower():
                    return item.get("id")

        # Create category
        payload = {"name": clean_name}
        if parent_id:
            payload["parent"] = parent_id

        create_res = self.client.post("categories", json=payload)
        if create_res.status_code in (200, 201):
            return create_res.json().get("id")

        return None

    def get_or_create_tag(self, name: str) -> Optional[int]:
        """Finds existing tag by name or creates a new one."""
        clean_name = name.strip()
        res = self.client.get("tags", params={"search": clean_name})
        if res.status_code == 200:
            items = res.json()
            for item in items:
                if item.get("name", "").lower() == clean_name.lower():
                    return item.get("id")

        # Create tag
        create_res = self.client.post("tags", json={"name": clean_name})
        if create_res.status_code in (200, 201):
            return create_res.json().get("id")

        return None

    def create_post(
        self,
        title: str,
        content: str,
        slug: str,
        categories: Optional[List[int]] = None,
        tags: Optional[List[int]] = None,
        status: Optional[str] = None,
        featured_media_id: Optional[int] = None,
        seo_meta: Optional[Dict[str, Any]] = None
    ) -> dict:
        """
        Creates a new post on WordPress via the REST API with Rank Math SEO support.
        """
        post_status = status or self.default_status
        payload = {
            "title": title,
            "content": content,
            "slug": slug,
            "status": post_status
        }

        if categories:
            payload["categories"] = categories
        if tags:
            payload["tags"] = tags
        if featured_media_id:
            payload["featured_media"] = featured_media_id

        # Attach Rank Math SEO metadata
        if seo_meta and self.config.get("rank_math_enabled", True):
            meta_dict = {}
            if "seo_title" in seo_meta or "title" in seo_meta:
                meta_dict["rank_math_title"] = seo_meta.get("seo_title") or seo_meta.get("title")
            if "seo_description" in seo_meta or "search_desc" in seo_meta:
                meta_dict["rank_math_description"] = seo_meta.get("seo_description") or seo_meta.get("search_desc")
            if "focus_keyword" in seo_meta:
                meta_dict["rank_math_focus_keyword"] = seo_meta.get("focus_keyword")
            
            if meta_dict:
                payload["meta"] = meta_dict

        res = self.client.post("posts", json=payload)
        if res.status_code in (200, 201):
            post_data = res.json()
            post_id = post_data.get("id")
            post_url = post_data.get("link", "")
            return {
                "success": True,
                "id": post_id,
                "url": post_url,
                "status": post_data.get("status"),
                "slug": post_data.get("slug"),
                "edit_url": f"{self.client.base_url}/wp-admin/post.php?post={post_id}&action=edit"
            }

        return {
            "success": False,
            "status_code": res.status_code,
            "error": res.text
        }

    def update_post(self, post_id: int, **kwargs) -> dict:
        """Updates an existing WordPress post."""
        res = self.client.post(f"posts/{post_id}", json=kwargs)
        if res.status_code == 200:
            post_data = res.json()
            return {
                "success": True,
                "id": post_data.get("id"),
                "url": post_data.get("link", ""),
                "status": post_data.get("status")
            }
        return {
            "success": False,
            "status_code": res.status_code,
            "error": res.text
        }
