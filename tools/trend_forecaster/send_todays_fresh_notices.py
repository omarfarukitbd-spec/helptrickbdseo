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
    build_breaking_notice_card
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
            "title": "২০২৫ সালের ডিগ্রী (পাস) ও সার্টিফিকেট কোর্সের ২য় বর্ষের ইনকোর্স পরীক্ষার নম্বর অনলাইনে এন্ট্রির সময় বৃদ্ধি সংক্রান্ত বিজ্ঞপ্তি।",
            "pdf_url": "https://www.nu.ac.bd/uploads/notices/notice_6069_pub_date_01102026.pdf",
            "pub_date": "2026-10-01",
            "category": "ডিগ্রি ও সার্টিফিকেট কোর্স",
            "callback": "draft_nu_degree",
            "button_text": "১-ক্লিকে ড্রাফট তৈরি করুন (ডিগ্রি ২য় বর্ষ)"
        },
        {
            "source": "জাতীয় বিশ্ববিদ্যালয় (NU Official)",
            "title": "২০২৫ ও ২০২৬ সালের এলএলবি প্রথম পর্ব পরীক্ষার ফরম পূরণের সময় বৃদ্ধি সংক্রান্ত বিজ্ঞপ্তি।",
            "pdf_url": "https://www.nu.ac.bd/uploads/notices/notice_2084_pub_date_01102026.PDF",
            "pub_date": "2026-10-01",
            "category": "প্রফেশনাল কোর্স (LLB)",
            "callback": "draft_nu_llb",
            "button_text": "১-ক্লিকে ড্রাফট তৈরি করুন (এলএলবি ১ম পর্ব)"
        }
    ]

    intro_text = (
        "<b>[হেল্পট্রিকবিডি ৩৬০-ডিগ্রি ব্রেকিং এক্সাম রাডার — আজকের নতুন নোটিশ]</b>\n"
        f"<b>তারিখ ও সময়:</b> {time_str} (বাংলাদেশ মান সময়)\n"
        "<b>উৎস:</b> জাতীয় বিশ্ববিদ্যালয় অফিসিয়াল নোটিশ পোর্টাল (nu.ac.bd)\n\n"
        "আজকে প্রকাশিত নতুন নোটিশের ওপর সাইট কভারেজ অডিট ও পূর্ণাঙ্গ এসইও প্যাকেজ নিচে প্রেরণ করা হলো:"
    )
    send_card(bot_token, chat_id, intro_text)
    time.sleep(1)

    for idx, n in enumerate(todays_notices, 1):
        card_text, post_url, pdf_url = build_breaking_notice_card(n, idx)
        
        # Build individual markup
        keyboard = [
            [
                {"text": n["button_text"], "callback_data": n["callback"]}
            ],
            [
                {"text": "অফিসিয়াল PDF ডাউনলোড", "url": n["pdf_url"]},
                {"text": "Blogger Admin Panel", "url": "https://www.blogger.com/blog/posts/8468755675548028711"}
            ]
        ]
        markup = {"inline_keyboard": keyboard}
        ok = send_card(bot_token, chat_id, card_text, reply_markup=markup)
        if ok:
            print(f"[SUCCESS] নোটিশ #{idx} ({n['category']}) সফলভাবে টেলিগ্রামে ডেলিভারি সম্পন্ন!")
        time.sleep(1)

if __name__ == "__main__":
    main()
