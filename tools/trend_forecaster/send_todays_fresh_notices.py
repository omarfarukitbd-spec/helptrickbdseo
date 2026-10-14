#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/trend_forecaster/send_todays_fresh_notices.py
--------------------------------------------------
Dispatches today's fresh official notices (Degree 2nd Year In-course, LLB 1st Part)
to Faruk Sir's Telegram with complete 7-point intelligence and interactive buttons.
Strictly Zero Emojis (Rule 12).
"""

import os
import sys
import json
import time
import urllib.request
import urllib.parse
import urllib.error
from datetime import datetime, timezone, timedelta

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.trend_forecaster.telegram_radar_notifier import (
    get_telegram_credentials,
    build_single_bulletin_digest
)

def send_card(bot_token, chat_id, card_text, reply_markup=None):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": card_text,
        "parse_mode": "HTML",
        "disable_web_page_preview": False
    }
    if reply_markup:
        payload["reply_markup"] = json.dumps(reply_markup)

    data = urllib.parse.urlencode(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"User-Agent": "HelpTrickBD-Radar/2.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8")).get("ok", False)
    except urllib.error.HTTPError as e:
        print(f"[-] Telegram HTTPError: {e.read().decode('utf-8')}")
        return False
    except Exception as e:
        print(f"[-] Error: {e}")
        return False

def main():
    bot_token, chat_id = get_telegram_credentials()
    if not bot_token or not chat_id:
        print("[-] Telegram credentials missing.")
        sys.exit(1)

    utc_now = datetime.now(timezone.utc)
    bd_now = utc_now + timedelta(hours=6)
    time_str = bd_now.strftime("%Y-%m-%d | %I:%M %p")

    todays_notices = [
        {
            "source": "জাতীয় বিশ্ববিদ্যালয় (NU Official)",
            "portal_url": "https://www.nu.ac.bd/",
            "title": "২০২৫ সালের ডিগ্রী (পাস) ও সার্টিফিকেট কোর্সের ২য় বর্ষের ইনকোর্স পরীক্ষার নম্বর অনলাইনে এন্ট্রির সময় বৃদ্ধি সংক্রান্ত বিজ্ঞপ্তি।",
            "pdf_url": "https://www.nu.ac.bd/uploads/notices/notice_6069_pub_date_01102026.pdf",
            "pub_date": "2026-10-01",
            "category": "ডিগ্রি ও সার্টিফিকেট কোর্স",
            "callback": "draft_nu_degree",
            "button_text": "১-ক্লিকে ড্রাফট তৈরি করুন (ডিগ্রি ২য় বর্ষ)"
        },
        {
            "source": "জাতীয় বিশ্ববিদ্যালয় (NU Official)",
            "portal_url": "https://www.nu.ac.bd/",
            "title": "২০২৫ ও ২০২৬ সালের এলএলবি প্রথম পর্ব পরীক্ষার ফরম পূরণের সময় বৃদ্ধি সংক্রান্ত বিজ্ঞপ্তি।",
            "pdf_url": "https://www.nu.ac.bd/uploads/notices/notice_2084_pub_date_01102026.PDF",
            "pub_date": "2026-10-01",
            "category": "প্রফেশনাল কোর্স (LLB)",
            "callback": "draft_nu_llb",
            "button_text": "১-ক্লিকে ড্রাফট তৈরি করুন (এলএলবি ১ম পর্ব)"
        }
    ]

    bulletin_text, reply_markup = build_single_bulletin_digest(todays_notices, bd_now)
    ok = send_card(bot_token, chat_id, bulletin_text, reply_markup=reply_markup)
    if ok:
        print(f"[SUCCESS] {len(todays_notices)}টি নোটিশের একক বুলেটিন সফলভাবে টেলিগ্রামে ডেলিভারি সম্পন্ন!")
    else:
        print("[-] টেলিগ্রাম বুলেটিন পাঠানো ব্যর্থ হয়েছে।")

if __name__ == "__main__":
    main()
