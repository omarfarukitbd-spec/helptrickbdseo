#!/usr/bin/env python3
"""
tools/social_broadcaster/telegram_publisher.py
HelpTrickBD Telegram Channel Broadcaster.

Sends high-contrast post updates with hero banner image to Telegram Channel
using the official Telegram Bot API.
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


class TelegramPublisher:
    """Publishes posts to Telegram Channel via Telegram Bot API."""

    API_BASE = "https://api.telegram.org/bot"

    def __init__(self, bot_token: str, channel_id: str):
        self.bot_token = bot_token.strip()
        self.channel_id = channel_id.strip()

    def is_configured(self) -> bool:
        """Checks if valid bot credentials exist."""
        return bool(self.bot_token and self.channel_id and "YOUR_" not in self.bot_token)

    def test_connection(self) -> Dict[str, Any]:
        """Tests bot authentication via getMe endpoint."""
        if not self.is_configured():
            return {"success": False, "message": "টেলিগ্রাম বট টোকেন কনফিগার করা হয়নি।"}

        url = f"{self.API_BASE}{self.bot_token}/getMe"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "HelpTrickBD-Broadcaster/1.0"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                if data.get("ok"):
                    bot_name = data["result"].get("username", "UnknownBot")
                    return {"success": True, "message": f"বট সফলভাবে যুক্ত হয়েছে: @{bot_name}"}
                return {"success": False, "message": f"টেলিগ্রাম এপিআই ত্রুটি: {data.get('description')}"}
        except Exception as e:
            return {"success": False, "message": f"টেলিগ্রাম সংযোগ ব্যর্থ: {str(e)}"}

    def publish_post(self, text: str, image_url: Optional[str] = None) -> Dict[str, Any]:
        """Publishes post to Telegram channel with photo or text."""
        if not self.is_configured():
            return {"success": False, "message": "টেলিগ্রাম বট ক্রেডেনশিয়াল পাওয়া যায়নি।"}

        # If image is available and caption is under 1024 chars, use sendPhoto
        if image_url and len(text) <= 1024:
            endpoint = f"{self.API_BASE}{self.bot_token}/sendPhoto"
            payload = {
                "chat_id": self.channel_id,
                "photo": image_url,
                "caption": text,
                "parse_mode": "HTML"
            }
        else:
            # Fallback to sendMessage (supports up to 4096 chars)
            endpoint = f"{self.API_BASE}{self.bot_token}/sendMessage"
            payload = {
                "chat_id": self.channel_id,
                "text": text,
                "parse_mode": "HTML",
                "disable_web_page_preview": False
            }

        try:
            data_bytes = json.dumps(payload).encode("utf-8")
            req = urllib.request.Request(
                endpoint,
                data=data_bytes,
                headers={
                    "Content-Type": "application/json",
                    "User-Agent": "HelpTrickBD-Broadcaster/1.0"
                }
            )
            with urllib.request.urlopen(req, timeout=15) as resp:
                res_data = json.loads(resp.read().decode("utf-8"))
                if res_data.get("ok"):
                    msg_id = res_data["result"]["message_id"]
                    return {
                        "success": True,
                        "message_id": msg_id,
                        "message": f"টেলিগ্রাম চ্যানেলে সফলভাবে পোস্ট পাবলিশ হয়েছে (মেসেজ আইডি: {msg_id})"
                    }
                return {"success": False, "message": f"টেলিগ্রাম পাবলিশ ত্রুটি: {res_data.get('description')}"}
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8") if e.fp else str(e)
            return {"success": False, "message": f"টেলিগ্রাম এইচটিটিপি ত্রুটি ({e.code}): {err_body}"}
        except Exception as e:
            return {"success": False, "message": f"টেলিগ্রাম পাবলিশিং ব্যর্থ: {str(e)}"}
