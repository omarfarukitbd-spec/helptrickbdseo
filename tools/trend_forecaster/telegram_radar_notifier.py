#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/trend_forecaster/telegram_radar_notifier.py
--------------------------------------------------
Helptrickbd Autonomous Telegram Cloud Alert Engine.

Sends real-time exam routines, emergency educational notices, and 30-45 day SEO
Golden Window actionable recommendations directly to the user's Telegram phone.

Operates:
1. Locally on PC (via tools/trend_forecaster/auto_radar_daemon.py)
2. In GitHub Actions Cloud 24/7 even when PC is completely turned off.

Zero-emoji compliance (Rule 12).
"""

import os
import sys
import json
import argparse
import urllib.request
import urllib.parse
from datetime import datetime

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.trend_forecaster.auto_radar_daemon import run_radar_check

LOCAL_CONFIG_PATH = os.path.join(PROJECT_ROOT, "scratch", "telegram_config.json")


def get_telegram_credentials():
    """
    Retrieves Bot Token and Chat ID from:
    1. Environment variables (GitHub Actions Secrets)
    2. Local configuration file (scratch/telegram_config.json)
    """
    bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")

    if not bot_token or not chat_id:
        if os.path.exists(LOCAL_CONFIG_PATH):
            try:
                with open(LOCAL_CONFIG_PATH, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    bot_token = bot_token or data.get("bot_token")
                    chat_id = chat_id or data.get("chat_id")
            except Exception:
                pass

    return bot_token, chat_id


def save_local_telegram_credentials(bot_token, chat_id):
    os.makedirs(os.path.dirname(LOCAL_CONFIG_PATH), exist_ok=True)
    with open(LOCAL_CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump({"bot_token": bot_token, "chat_id": chat_id}, f, indent=2)


def get_chat_id_from_updates(bot_token):
    """
    Polls getUpdates to find who pressed /start on the bot.
    """
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "HelpTrickBD-Radar/1.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if data.get("ok") and data.get("result"):
                for item in reversed(data["result"]):
                    msg = item.get("message", {}) or item.get("channel_post", {})
                    chat = msg.get("chat", {})
                    if "id" in chat:
                        return str(chat["id"]), chat.get("first_name", "User")
    except Exception as e:
        print(f"[-] getUpdates ত্রুটি: {e}")
    return None, None


def send_telegram_message(bot_token, chat_id, html_text):
    """
    Sends an HTML message via Telegram Bot API.
    """
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": html_text,
        "parse_mode": "HTML",
        "disable_web_page_preview": False
    }
    data = urllib.parse.urlencode(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"User-Agent": "HelpTrickBD-Radar/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            return res.get("ok", False)
    except Exception as e:
        print(f"[-] Telegram API ত্রুটি: {e}")
        return False


def build_radar_alert_html(new_notices, urgent_items, now):
    """
    Builds clean, professional Bengali alert text strictly with zero emojis.
    """
    time_str = now.strftime("%Y-%m-%d | %I:%M %p")
    lines = [
        "<b>[হেল্পট্রিকবিডি ৩৬০-ডিগ্রি এক্সাম রাডার সতর্কবার্তা]</b>",
        f"<b>তারিখ ও সময়:</b> {time_str}",
        "----------------------------------------"
    ]

    if new_notices:
        lines.append("<b>জরুরি নতুন নোটিশ ও রুটিন প্রকাশিত হয়েছে:</b>")
        for idx, n in enumerate(new_notices[:7], 1):
            title = n["title"].replace("<", "&lt;").replace(">", "&gt;")
            source = f"[{n.get('source', 'শিক্ষা বোর্ড')}]"
            pdf_link = n.get("pdf_url")
            if pdf_link:
                lines.append(f"{idx}. {source} {title}\n   <a href=\"{pdf_link}\">[অফিসিয়াল PDF ডাউনলোড]</a>")
            else:
                lines.append(f"{idx}. {source} {title}")
        lines.append("")
    else:
        lines.append("<b>নিয়মিত ট্র্যাকিং আপডেট:</b> নতুন কোনো রুটিন আসেনি।")
        lines.append("")

    if urgent_items:
        lines.append("<b>চলতি মাসের শীর্ষ এসইও গোল্ডেন উইন্ডো (তাৎক্ষণিক পোস্ট করণীয়):</b>")
        for idx, item in enumerate(urgent_items[:3], 1):
            name = item["exam_name"].replace("<", "&lt;").replace(">", "&gt;")
            keywords = ", ".join(item["target_keywords"][:2]).replace("<", "&lt;").replace(">", "&gt;")
            lines.append(f"• <b>{name}</b>")
            lines.append(f"  টার্গেট কি-ওয়ার্ড: <i>{keywords}</i>")
            lines.append(f"  করণীয়: {item['content_blueprint'][:70]}...")
            lines.append("")

    lines.append("----------------------------------------")
    lines.append("<b>অ্যাকশন:</b> পিসি অন করে সবার আগে পোস্ট তৈরি করুন এবং গুগলে ১ নম্বর স্থান নিশ্চিত করুন!")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="HelpTrickBD Telegram Exam Radar Notifier")
    parser.add_argument("--test", action="store_true", help="Send a test message to verify Telegram connection")
    parser.add_argument("--force", action="store_true", help="Force send summary even if no new notice found")
    parser.add_argument("--token", type=str, help="Override Bot Token")
    parser.add_argument("--chat-id", type=str, help="Override Chat ID")
    args = parser.parse_args()

    bot_token, chat_id = get_telegram_credentials()
    if args.token:
        bot_token = args.token
    if args.chat_id:
        chat_id = args.chat_id

    if not bot_token:
        print("[-] ত্রুটি: TELEGRAM_BOT_TOKEN পাওয়া যায়নি।")
        sys.exit(1)

    # Auto-detect chat_id if missing
    if not chat_id:
        print("[*] চ্যাট আইডি খোঁজা হচ্ছে (getUpdates)...")
        detected_id, user_name = get_chat_id_from_updates(bot_token)
        if detected_id:
            chat_id = detected_id
            save_local_telegram_credentials(bot_token, chat_id)
            print(f"[OK] চ্যাট আইডি সফলভাবে শনাক্ত হয়েছে: {chat_id} (ব্যবহারকারী: {user_name})")
        else:
            print("[-] ত্রুটি: চ্যাট আইডি পাওয়া যায়নি। দয়া করে টেলিগ্রামে আপনার বটে গিয়ে /start চাপুন।")
            sys.exit(1)

    now = datetime.now()

    if args.test:
        test_msg = (
            "<b>[হেল্পট্রিকবিডি ক্লাউড এক্সাম রাডার — টেস্ট সফল]</b>\n"
            f"<b>তারিখ:</b> {now.strftime('%Y-%m-%d %I:%M %p')}\n\n"
            "টেলিগ্রাম অ্যালার্ট সিস্টেমের সাথে সংযোগ সফল হয়েছে!\n"
            "এখন থেকে আপনার কম্পিউটার সম্পূর্ণ বন্ধ থাকলেও দিনে ৩ বার ও নতুন রুটিন প্রকাশ হওয়ামাত্র আপনার মোবাইলে এই বটে নোটিফিকেশন চলে আসবে।"
        )
        ok = send_telegram_message(bot_token, chat_id, test_msg)
        if ok:
            print("[SUCCESS] টেস্ট মেসেজ সফলভাবে আপনার টেলিগ্রামে পাঠানো হয়েছে!")
        else:
            print("[-] টেস্ট মেসেজ পাঠানো ব্যর্থ হয়েছে।")
        return

    # Normal execution: scan notices and radar
    new_notices, urgent_items = run_radar_check()

    # Send message if there are new notices OR if forced (scheduled check)
    if new_notices or args.force:
        html_msg = build_radar_alert_html(new_notices, urgent_items, now)
        ok = send_telegram_message(bot_token, chat_id, html_msg)
        if ok:
            print("[SUCCESS] টেলিগ্রামে সফলভাবে এক্সাম রাডার রিপোর্ট পাঠানো হয়েছে!")
        else:
            print("[-] টেলিগ্রাম মেসেজ ডেলিভারি ব্যর্থ হয়েছে।")
    else:
        print("[*] নতুন কোনো নোটিশ না থাকায় টেলিগ্রামে অ্যালার্ট পাঠানো হয়নি (নীরব মোড)।")


if __name__ == "__main__":
    main()
