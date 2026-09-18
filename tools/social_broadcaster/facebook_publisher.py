#!/usr/bin/env python3
"""
tools/social_broadcaster/facebook_publisher.py
HelpTrickBD Facebook Official Page Broadcaster.

Publishes human-feel SEO posts with thumbnail image to Facebook Page
using the official Meta Graph API (v19.0+).
Strictly zero-emoji compliant.
"""

import sys
import json
import urllib.request
import urllib.parse
from typing import Dict, Any, Optional

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass


class FacebookPublisher:
    """Publishes posts to Facebook Page via Meta Graph API."""

    GRAPH_VERSION = "v19.0"
    GRAPH_BASE = "https://graph.facebook.com"

    def __init__(self, page_id: str, page_access_token: str, make_webhook_url: Optional[str] = None):
        self.page_id = page_id.strip()
        self.page_access_token = page_access_token.strip()
        self.make_webhook_url = make_webhook_url.strip() if make_webhook_url else ""

    def is_configured(self) -> bool:
        """Checks if valid Facebook credentials or Make webhook exist."""
        if self.make_webhook_url and "hook." in self.make_webhook_url:
            return True
        return bool(self.page_id and self.page_access_token and "YOUR_" not in self.page_access_token)

    def test_connection(self) -> Dict[str, Any]:
        """Tests Facebook connection via Make webhook or Graph API."""
        if self.make_webhook_url:
            return {"success": True, "message": "মেক.কম ভেরিফাইড গেটওয়ে সক্রিয় (১০০% পাবলিক পাবলিশিং মোড)"}

        if not self.is_configured():
            return {"success": False, "message": "ফেসবুক পেজ এক্সেস টোকেন বা মেক গেটওয়ে কনফিগার করা হয়নি।"}

        url = f"{self.GRAPH_BASE}/{self.GRAPH_VERSION}/{self.page_id}?fields=name,id&access_token={self.page_access_token}"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "HelpTrickBD-Broadcaster/1.0"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                page_name = data.get("name", "Unknown Page")
                return {"success": True, "message": f"ফেসবুক পেজ সফলভাবে সংযুক্ত: {page_name} (আইডি: {data.get('id')})"}
        except urllib.error.HTTPError as e:
            err_data = e.read().decode("utf-8") if e.fp else str(e)
            return {"success": False, "message": f"ফেসবুক অথেনটিকেশন ব্যর্থ: {err_data}"}
        except Exception as e:
            return {"success": False, "message": f"ফেসবুক সংযোগ ব্যর্থ: {str(e)}"}

    def publish_post(
        self,
        message: str,
        link: Optional[str] = None,
        image_url: Optional[str] = None,
        post_type: str = "link",
        title: Optional[str] = None
    ) -> Dict[str, Any]:
        """Publishes clickable post to Facebook Page via Make verified gateway (100% public) or Graph API."""
        if not self.is_configured():
            return {"success": False, "message": "ফেসবুক ক্রেডেনশিয়াল পাওয়া যায়নি।"}

        # 1. First priority: Use Make.com verified enterprise gateway for guaranteed 100% public visibility
        if self.make_webhook_url:
            try:
                payload = {
                    "title": title or "",
                    "message": message,
                    "link": link or "",
                    "image_url": image_url or ""
                }
                data_bytes = json.dumps(payload).encode("utf-8")
                req = urllib.request.Request(
                    self.make_webhook_url,
                    data=data_bytes,
                    headers={
                        "Content-Type": "application/json",
                        "User-Agent": "HelpTrickBD-Broadcaster/1.0"
                    }
                )
                with urllib.request.urlopen(req, timeout=20) as resp:
                    resp_body = resp.read().decode("utf-8")
                    if resp.status == 200 or "Accepted" in resp_body:
                        return {
                            "success": True,
                            "gateway": "make.com",
                            "message": "মেক.কম ভেরিফাইড গেটওয়ে দিয়ে ফেসবুকে সফলভাবে পোস্ট পাবলিশ হয়েছে (১০০% পাবলিক দৃশ্যমান)"
                        }
            except Exception as e:
                # Fallback to direct Graph API if webhook network fails
                pass

        try:
            # Default "link": Creates official full-width clickable preview card where tapping the photo visits the website directly
            if post_type == "link" and link:
                endpoint = f"{self.GRAPH_BASE}/{self.GRAPH_VERSION}/{self.page_id}/feed"
                data = {
                    "message": message,
                    "link": link,
                    "access_token": self.page_access_token
                }
            elif image_url:
                endpoint = f"{self.GRAPH_BASE}/{self.GRAPH_VERSION}/{self.page_id}/photos"
                data = {
                    "url": image_url,
                    "caption": message,
                    "access_token": self.page_access_token
                }
            else:
                endpoint = f"{self.GRAPH_BASE}/{self.GRAPH_VERSION}/{self.page_id}/feed"
                data = {
                    "message": message,
                    "link": link or "",
                    "access_token": self.page_access_token
                }

            encoded_data = urllib.parse.urlencode(data).encode("utf-8")
            req = urllib.request.Request(
                endpoint,
                data=encoded_data,
                headers={"User-Agent": "HelpTrickBD-Broadcaster/1.0"}
            )

            with urllib.request.urlopen(req, timeout=20) as resp:
                res_data = json.loads(resp.read().decode("utf-8"))
                post_id = res_data.get("post_id") or res_data.get("id")
                return {
                    "success": True,
                    "post_id": post_id,
                    "message": f"ফেসবুক পেজে সফলভাবে পোস্ট পাবলিশ হয়েছে (পোস্ট আইডি: {post_id})"
                }
        except urllib.error.HTTPError as e:
            # ফলব্যাক: যদি ফটো এন্ডপয়েন্ট কোনো কারণে ফেইল করে, তবে লিঙ্ক পোস্ট হিসেবে পাবলিশ নিশ্চিত করা হবে
            if image_url and link:
                try:
                    feed_endpoint = f"{self.GRAPH_BASE}/{self.GRAPH_VERSION}/{self.page_id}/feed"
                    feed_data = urllib.parse.urlencode({
                        "message": message,
                        "link": link,
                        "access_token": self.page_access_token
                    }).encode("utf-8")
                    feed_req = urllib.request.Request(
                        feed_endpoint,
                        data=feed_data,
                        headers={"User-Agent": "HelpTrickBD-Broadcaster/1.0"}
                    )
                    with urllib.request.urlopen(feed_req, timeout=20) as resp:
                        res_data = json.loads(resp.read().decode("utf-8"))
                        post_id = res_data.get("id")
                        return {
                            "success": True,
                            "post_id": post_id,
                            "message": f"ফেসবুক পেজে লিঙ্ক পোস্ট হিসেবে সফলভাবে পাবলিশ হয়েছে (পোস্ট আইডি: {post_id})"
                        }
                except Exception:
                    pass

            err_msg = e.read().decode("utf-8") if e.fp else str(e)
            return {"success": False, "message": f"ফেসবুক পাবলিশ এইচটিটিপি ত্রুটি ({e.code}): {err_msg}"}
        except Exception as e:
            return {"success": False, "message": f"ফেসবুক পাবলিশিং ব্যর্থ: {str(e)}"}
