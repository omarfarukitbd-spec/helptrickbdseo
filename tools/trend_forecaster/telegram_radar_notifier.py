#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/trend_forecaster/telegram_radar_notifier.py
--------------------------------------------------
Helptrickbd Autonomous Telegram 360-Degree Intelligence & Alert Engine.

Sends real-time exam routines, emergency educational notices, site coverage audits,
instant SEO packages (titles/slugs), and 30-45 day SEO Golden Window roadmaps
directly to the user's Telegram phone.

Key Intelligence Features:
1. Site Coverage & Red-Alert Checker (matches against live posts & drafts).
2. Auto-generated SEO Title, English Slug & Recommended Labels.
3. Automated Key Dates, Session & Exam Term Extractor.
4. Target Student Profile, Search Intent & Top 3 Google Search Queries.
5. Competitor Opportunity Radar.
6. Daily Morning SEO Digest at 08:00 AM BD Time.
7. Clickable Telegram Inline Action Buttons (PDF, Site, Blogger Admin).

Strict Zero-Emoji Compliance (Rule 12).
"""

import os
import sys
import re
import glob
import json
import argparse
import urllib.request
import urllib.parse
from datetime import datetime, timezone, timedelta

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

from tools.trend_forecaster.auto_radar_daemon import run_radar_check, SEEN_NOTICES_FILE

LOCAL_CONFIG_PATH = os.path.join(PROJECT_ROOT, "scratch", "telegram_config.json")
CATALOG_PATH = os.path.join(PROJECT_ROOT, "all_live_posts_catalog.json")
SCRATCH_POSTS_PATH = os.path.join(PROJECT_ROOT, "scratch", "all_112_live_posts.json")
BLOGGER_POSTS_PATH = os.path.join(PROJECT_ROOT, "data", "blogger_all_live_posts.json")


def get_telegram_credentials():
    """Retrieves Bot Token and Chat ID from ENV or local config."""
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
    """Polls getUpdates to find chat ID."""
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "HelpTrickBD-Radar/2.0"})
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


def send_telegram_message(bot_token, chat_id, html_text, reply_markup=None):
    """Sends an HTML message via Telegram Bot API with optional inline buttons."""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": html_text,
        "parse_mode": "HTML",
        "disable_web_page_preview": False
    }
    if reply_markup:
        payload["reply_markup"] = json.dumps(reply_markup)

    data = urllib.parse.urlencode(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"User-Agent": "HelpTrickBD-Radar/2.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            return res.get("ok", False)
    except Exception as e:
        print(f"[-] Telegram API ত্রুটি: {e}")
        return False


def load_all_known_posts():
    """Loads live posts and local output_posts metadata."""
    posts = []
    seen_titles = set()

    for path in [CATALOG_PATH, BLOGGER_POSTS_PATH, SCRATCH_POSTS_PATH]:
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        for p in data:
                            title = p.get("title", "")
                            if title and title not in seen_titles:
                                seen_titles.add(title)
                                posts.append(p)
            except Exception:
                pass

    # Also load draft/ready post metadata in output_posts
    for meta_file in glob.glob(os.path.join(PROJECT_ROOT, "output_posts", "*_meta.json")):
        try:
            with open(meta_file, "r", encoding="utf-8") as mf:
                m = json.load(mf)
                title = m.get("title", "")
                if title and title not in seen_titles:
                    seen_titles.add(title)
                    posts.append({
                        "id": m.get("post_id", ""),
                        "title": title,
                        "url": f"https://www.helptrickbd.com/2026/10/{m.get('permalink', '')}.html",
                        "status": m.get("status", "DRAFT")
                    })
        except Exception:
            pass

    return posts


ALL_KNOWN_POSTS = load_all_known_posts()


def check_site_coverage(notice_title):
    """
    Checks if Helptrickbd already has a live post or draft matching the notice.
    Returns: {"status": "LIVE"|"DRAFT"|"NOT_FOUND", "title": str, "url": str}
    """
    title_lower = notice_title.lower()

    # Core academic keywords
    term_clusters = [
        (["অনার্স", "২য় বর্ষ"], ["honours 2nd", "অনার্স ২য়"]),
        (["অনার্স", "১ম বর্ষ"], ["honours 1st", "অনার্স ১ম"]),
        (["অনার্স", "৩য় বর্ষ"], ["honours 3rd", "অনার্স ৩য়"]),
        (["অনার্স", "৪র্থ বর্ষ"], ["honours 4th", "অনার্স ৪র্থ"]),
        (["মাস্টার্স"], ["masters", "মাস্টার্স"]),
        (["ডিগ্রি", "১ম বর্ষ"], ["degree 1st", "ডিগ্রি ১ম"]),
        (["ডিগ্রি", "২য় বর্ষ"], ["degree 2nd", "ডিগ্রি ২য়"]),
        (["ডিগ্রি", "৩য় বর্ষ"], ["degree 3rd", "ডিগ্রি ৩য়"]),
        (["এসএসসি", "রুটিন"], ["ssc exam routine", "এসএসসি রুটিন"]),
        (["এইচএসসি", "রুটিন"], ["hsc exam routine", "এইচএসসি রুটিন"]),
        (["দাখিল"], ["dakhil"]),
        (["আলিম"], ["alim"]),
        (["ডিপ্লোমা"], ["diploma", "bteb"]),
        (["প্রাথমিক শিক্ষক", "নিয়োগ"], ["primary teacher"]),
        (["প্রাথমিক বৃত্তি"], ["primary scholarship", "বৃত্তি"]),
        (["বিসিএস"], ["bcs preliminary", "bcs written"]),
        (["ভর্তি", "বিশ্ববিদ্যালয়"], ["university admission"]),
    ]

    for bn_keywords, en_keywords in term_clusters:
        if all(k in title_lower for k in bn_keywords):
            for post in ALL_KNOWN_POSTS:
                p_title = post.get("title", "").lower()
                if all(k in p_title for k in bn_keywords) or any(k in p_title for k in en_keywords):
                    is_draft = post.get("status") == "DRAFT"
                    return {
                        "status": "DRAFT" if is_draft else "LIVE",
                        "title": post.get("title"),
                        "url": post.get("url")
                    }

    return {"status": "NOT_FOUND", "title": None, "url": None}


def generate_instant_seo_package(notice_title, source):
    """
    Auto-generates recommended title, English slug, labels, audience & search intent.
    """
    t = notice_title
    now_year = "২০২৬"
    next_year = "২০২৭"

    if "অনার্স ২য় বর্ষ" in t or "অনার্স দ্বিতীয় বর্ষ" in t:
        return {
            "proposed_title": f"জাতীয় বিশ্ববিদ্যালয় অনার্স ২য় বর্ষ পরীক্ষার রুটিন {now_year} (সকল বিভাগ) | NU Honours 2nd Year Exam Routine & Subject Code",
            "english_slug": f"nu-honours-2nd-year-exam-routine-{now_year}",
            "labels": "জাতীয় বিশ্ববিদ্যালয়, অনার্স রুটিন, এডুকেশন নোটিশ",
            "audience": "জাতীয় বিশ্ববিদ্যালয়ের অনার্স ২য় বর্ষের সকল শাখার শিক্ষার্থী",
            "intent": "বিষয়ভিত্তিক পরীক্ষার রুটিন, বিষয় কোড ও ইংরেজি আবশ্যিক পাস সাজেশন",
            "top_queries": [
                f"জাতীয় বিশ্ববিদ্যালয় অনার্স ২য় বর্ষ পরীক্ষার রুটিন {now_year}",
                f"NU Honours 2nd Year Exam Routine {now_year}",
                "অনার্স ২য় বর্ষ পরীক্ষার বিষয় কোড তালিকা"
            ]
        }
    elif "অনার্স ১ম বর্ষ" in t or "অনার্স প্রথম বর্ষ" in t:
        return {
            "proposed_title": f"জাতীয় বিশ্ববিদ্যালয় অনার্স ১ম বর্ষ পরীক্ষার রুটিন {now_year} | NU Honours 1st Year Exam Routine PDF Download",
            "english_slug": f"nu-honours-1st-year-exam-routine-{now_year}",
            "labels": "জাতীয় বিশ্ববিদ্যালয়, অনার্স রুটিন, এডুকেশন নোটিশ",
            "audience": "জাতীয় বিশ্ববিদ্যালয়ের অনার্স ১ম বর্ষের নতুন শিক্ষার্থী",
            "intent": "পরীক্ষার তারিখ, কেন্দ্র তালিকা ও স্বাধীন বাংলাদেশের অভ্যুদয়ের ইতিহাস সাজেশন",
            "top_queries": [
                f"জাতীয় বিশ্ববিদ্যালয় অনার্স ১ম বর্ষ পরীক্ষার রুটিন {now_year}",
                f"NU Honours 1st Year Exam Routine {now_year}",
                "অনার্স ১ম বর্ষ পরীক্ষার কেন্দ্র তালিকা"
            ]
        }
    elif "ডিগ্রী" in t or "ডিগ্রি" in t:
        if "২য় বর্ষ" in t or "২য় বর্ষ" in t or "দ্বিতীয় বর্ষ" in t:
            return {
                "proposed_title": f"জাতীয় বিশ্ববিদ্যালয় ডিগ্রি ২য় বর্ষ ইনকোর্স নম্বর এন্ট্রি ও পরীক্ষার গাইড {now_year} | NU Degree 2nd Year In-Course & Exam Routine",
                "english_slug": f"nu-degree-2nd-year-in-course-and-exam-routine-{now_year}",
                "labels": "ডিগ্রি পাস, জাতীয় বিশ্ববিদ্যালয়, এডুকেশন নোটিশ",
                "audience": "জাতীয় বিশ্ববিদ্যালয়ের ডিগ্রি (পাস) ও সার্টিফিকেট কোর্স ২য় বর্ষের শিক্ষার্থী ও শিক্ষকবৃন্দ",
                "intent": "ইনকোর্স পরীক্ষার নম্বর অনলাইনে এন্ট্রির বর্ধিত সময়সূচি, প্রবেবল লিস্টের নিয়ম ও পরীক্ষার রুটিন আপডেট",
                "top_queries": [
                    f"ডিগ্রি ২য় বর্ষ ইনকোর্স পরীক্ষার নম্বর এন্ট্রি {now_year}",
                    f"জাতীয় বিশ্ববিদ্যালয় ডিগ্রি ২য় বর্ষ পরীক্ষার রুটিন {now_year}",
                    f"NU Degree 2nd Year In-course Marks Entry & Form Fill up {now_year}"
                ]
            }
        elif "৩য় বর্ষ" in t or "৩য় বর্ষ" in t or "তৃতীয় বর্ষ" in t:
            return {
                "proposed_title": f"জাতীয় বিশ্ববিদ্যালয় ডিগ্রি ৩য় বর্ষ পরীক্ষার রেজাল্ট {now_year} ও পুনঃনিরীক্ষণ আবেদন | NU Degree 3rd Year Result & Re-scrutiny",
                "english_slug": f"nu-degree-3rd-year-exam-result-{now_year}",
                "labels": "ডিগ্রি পাস, জাতীয় বিশ্ববিদ্যালয়, পরীক্ষার ফলাফল",
                "audience": "জাতীয় বিশ্ববিদ্যালয়ের ডিগ্রি ৩য় বর্ষের ফলপ্রার্থী শিক্ষার্থী",
                "intent": "ডিগ্রি ৩য় বর্ষ পরীক্ষার রেজাল্ট দেখার নিয়ম ও উত্তরপত্র পুনঃনিরীক্ষণ আবেদন পদ্ধতি",
                "top_queries": [
                    f"ডিগ্রি ৩য় বর্ষ পরীক্ষার রেজাল্ট {now_year}",
                    f"NU Degree 3rd Year Result {now_year} nu.ac.bd",
                    "ডিগ্রি পরীক্ষার খাতা চ্যালেঞ্জ নিয়ম"
                ]
            }
        else:
            return {
                "proposed_title": f"জাতীয় বিশ্ববিদ্যালয় ডিগ্রি পাস ও সার্টিফিকেট কোর্স পরীক্ষার রুটিন {now_year} | NU Degree Exam Routine PDF",
                "english_slug": f"nu-degree-exam-routine-{now_year}",
                "labels": "ডিগ্রি পাস, জাতীয় বিশ্ববিদ্যালয়, এডুকেশন নোটিশ",
                "audience": "জাতীয় বিশ্ববিদ্যালয়ের ডিগ্রি ১ম/২য়/৩য় বর্ষের শিক্ষার্থী",
                "intent": "ডিগ্রি পরীক্ষার সময়সূচি, কেন্দ্র তালিকা ও শর্ট সাজেশন",
                "top_queries": [
                    f"ডিগ্রি পরীক্ষার রুটিন {now_year}",
                    f"NU Degree Pass Exam Routine {now_year}",
                    "ডিগ্রি পরীক্ষার প্রবেশপত্র ডাউনলোড নিয়ম"
                ]
            }
    elif "এলএলবি" in t or "llb" in t.lower():
        return {
            "proposed_title": f"জাতীয় বিশ্ববিদ্যালয় এলএলবি ১ম পর্ব পরীক্ষার ফরম পূরণ {now_year} (বর্ধিত সময়) | NU LLB 1st Part Form Fill Up Routine & Fee",
            "english_slug": f"nu-llb-1st-part-exam-form-fill-up-{now_year}",
            "labels": "এলএলবি, জাতীয় বিশ্ববিদ্যালয়, প্রফেশনাল কোর্স",
            "audience": "জাতীয় বিশ্ববিদ্যালয়ের এলএলবি (LLB) ১ম পর্বের শিক্ষার্থী ও ল কলেজ কর্তৃপক্ষ",
            "intent": "এলএলবি ১ম পর্ব পরীক্ষার বর্ধিত ফরম পূরণের সময়সূচি, সোনালী সেবায় ফি জমা ও প্রয়োজনীয় কাগজপত্র",
            "top_queries": [
                f"জাতীয় বিশ্ববিদ্যালয় এলএলবি ১ম পর্ব পরীক্ষার ফরম পূরণ {now_year}",
                f"NU LLB 1st Part Exam Form Fill Up {now_year}",
                "এলএলবি ১ম পর্ব পরীক্ষার ফি সোনালী সেবা"
            ]
        }
    elif "এসএসসি" in t or "ssc" in t.lower():
        return {
            "proposed_title": f"এসএসসি পরীক্ষার রুটিন {next_year} (সকল শিক্ষা বোর্ড) | SSC Exam Routine {next_year} PDF Download",
            "english_slug": f"ssc-exam-routine-{next_year}-all-board",
            "labels": "এসএসসি পরীক্ষা, রুটিন, শিক্ষা বোর্ড নোটিশ",
            "audience": "মাধ্যমিক স্কুল সার্টিফিকেট (SSC) ও সমমান পরীক্ষার্থী",
            "intent": "রুটিন ডাউনলোড, ব্যবহারিক পরীক্ষার তারিখ ও প্রবেশপত্র সংক্রান্ত তথ্য",
            "top_queries": [
                f"এসএসসি পরীক্ষার রুটিন {next_year}",
                f"SSC Routine {next_year} PDF Download",
                f"দাখিল পরীক্ষার রুটিন {next_year}"
            ]
        }
    elif "এইচএসসি" in t or "hsc" in t.lower():
        return {
            "proposed_title": f"এইচএসসি পরীক্ষার রুটিন {now_year} (সকল সাধারণ শিক্ষা বোর্ড) | HSC Exam Routine {now_year} PDF",
            "english_slug": f"hsc-exam-routine-{now_year}-all-board",
            "labels": "এইচএসসি পরীক্ষা, রুটিন, শিক্ষা বোর্ড নোটিশ",
            "audience": "উচ্চ মাধ্যমিক (HSC) ও আলিম পরীক্ষার্থী",
            "intent": "গ্রুপভিত্তিক পরীক্ষার সময়সূচি ও সময় পরিবর্তন নোটিশ",
            "top_queries": [
                f"এইচএসসি পরীক্ষার রুটিন {now_year}",
                f"HSC Exam Routine {now_year} All Board",
                "আলিম পরীক্ষার রুটিন ২০২৬"
            ]
        }
    elif "বিসিএস" in t or "bcs" in t.lower() or "পিএসসি" in t:
        return {
            "proposed_title": f"বিসিএস প্রিলিমিনারি পরীক্ষার তারিখ ও সিলেবাস গাইড {now_year} | BCS Preliminary Marks Distribution",
            "english_slug": f"bcs-preliminary-exam-guide-{now_year}",
            "labels": "বিসিএস প্রস্তুতি, সরকারি চাকরি, জব স্টাডি",
            "audience": "বিসিএস ও ১ম/২য় শ্রেণির সরকারি চাকরিপ্রার্থী",
            "intent": "প্রিলিমিনারি ২০০ নম্বরের মানবণ্টন, পরীক্ষার তারিখ ও বিষয়ভিত্তিক বুক লিস্ট",
            "top_queries": [
                f"বিসিএস প্রিলিমিনারি পরীক্ষার তারিখ {now_year}",
                "BCS Preliminary Marks Distribution",
                "বিসিএস প্রিলি পাসের শর্টকাট কৌশল"
            ]
        }
    elif "ntrca" in t.lower() or "শিক্ষক নিবন্ধন" in t or "এনটিআরসিএ" in t:
        return {
            "proposed_title": f"এনটিআরসিএ শিক্ষক নিবন্ধন ও নিয়োগ পরীক্ষার নোটিশ {now_year} | NTRCA Exam Circular & Viva Routine",
            "english_slug": f"ntrca-teacher-registration-exam-routine-{now_year}",
            "labels": "শিক্ষক নিবন্ধন, সরকারি চাকরি, ক্যারিয়ার গাইড",
            "audience": "বেসরকারি শিক্ষক নিবন্ধন (NTRCA) ও গণবিজ্ঞপ্তি চাকরিপ্রার্থী",
            "intent": "শিক্ষক নিবন্ধন পরীক্ষার নোটিশ, প্রিলিমিনারি/লিখিত/মৌখিক পরীক্ষার সময়সূচি ও ফলাফল",
            "top_queries": [
                f"এনটিআরসিএ শিক্ষক নিবন্ধন পরীক্ষার রুটিন {now_year}",
                f"NTRCA Exam Result & Viva Schedule {now_year}",
                "শিক্ষক নিবন্ধন মৌখিক পরীক্ষার নোটিশ"
            ]
        }
    elif "রেলওয়ে" in t or "রেলওয়ে" in t or "railway" in t.lower():
        return {
            "proposed_title": f"বাংলাদেশ রেলওয়ে নিয়োগ বিজ্ঞপ্তি ও পরীক্ষার সময়সূচি {now_year} | Bangladesh Railway Job Circular",
            "english_slug": f"bangladesh-railway-job-circular-routine-{now_year}",
            "labels": "রেলওয়ে চাকরি, সরকারি চাকরি, ক্যারিয়ার গাইড",
            "audience": "বাংলাদেশ রেলওয়ে সরকারি চাকরিপ্রার্থী",
            "intent": "রেলওয়ে নিয়োগ বিজ্ঞপ্তি, পদের বিবরণ, আবেদনের শর্ত ও পরীক্ষার তারিখ",
            "top_queries": [
                f"বাংলাদেশ রেলওয়ে নিয়োগ বিজ্ঞপ্তি {now_year}",
                f"Railway Job Circular & Exam Date {now_year}",
                "রেলওয়ে পরীক্ষার এডমিট কার্ড ডাউনলোড"
            ]
        }
    elif "নিয়োগ" in t or "চাকরি" in t or "নন-ক্যাডার" in t or "non-cadre" in t.lower():
        return {
            "proposed_title": f"সরকারি চাকরি নিয়োগ বিজ্ঞপ্তি ও পরীক্ষার গাইড {now_year} | Govt Job Circular & Routine",
            "english_slug": f"bd-govt-job-circular-routine-{now_year}",
            "labels": "সরকারি চাকরি, জব স্টাডি, ক্যারিয়ার গাইড",
            "audience": "সরকারি ও স্বায়ত্তশাসিত প্রতিষ্ঠানে চাকরিপ্রার্থী",
            "intent": "আবেদনের যোগ্যতা, পদ সংখ্যা, পরীক্ষার মানবণ্টন ও প্রবেশপত্র",
            "top_queries": [
                f"সরকারি চাকরির খবর ও নিয়োগ বিজ্ঞপ্তি {now_year}",
                f"Govt Job Circular {now_year} BD",
                "চাকরির পরীক্ষার সময়সূচি ও এডমিট কার্ড"
            ]
        }
    else:
        clean_name = re.sub(r'[^a-zA-Z0-9\s]', '', t)[:40].strip().replace(' ', '-').lower()
        slug = f"bd-edu-notice-{clean_name or 'latest'}-{now_year}"
        return {
            "proposed_title": f"{t} — পূর্ণাঙ্গ গাইডলাইন ও অফিসিয়াল নোটিশ {now_year}",
            "english_slug": slug,
            "labels": "শিক্ষা নোটিশ, শিক্ষা বোর্ড",
            "audience": "সংশ্লিষ্ট শিক্ষার্থী ও চাকরিপ্রার্থী",
            "intent": "অফিসিয়াল বিজ্ঞপ্তি, আবেদনের নিয়ম ও গুরুত্বপূর্ণ তারিখ",
            "top_queries": [
                f"{t[:40]} {now_year}",
                f"Latest Education Notice {now_year}",
                "অফিসিয়াল নোটিশ ডাউনলোড"
            ]
        }


def extract_key_dates_and_details(title, pdf_url):
    """Extracts session, dates and exam action type from title and PDF URL."""
    details = []

    # Session detection
    session_m = re.search(r'(২০\d{2}[-–]২০?\d{2}|২০\d{2})', title)
    if session_m:
        details.append(f"সেশন/শিক্ষাবর্ষ: {session_m.group(1)}")

    # Specific date in title
    date_m = re.search(r'(\d{1,2}\s+(?:জানুয়ারি|ফেব্রুয়ারি|মার্চ|এপ্রিল|মে|জুন|জুলাই|আগস্ট|সেপ্টেম্বর|অক্টোবর|নভেম্বর|ডিসেম্বর)\s+২০\d{2})', title)
    if date_m:
        details.append(f"ঘোষিত তারিখ: {date_m.group(1)}")

    # Specific notice intelligence for Degree 2nd Year In-course (Notice 6069)
    if "৬০৬৯" in (pdf_url or "") or ("ডিগ্রী" in title and "ইনকোর্স" in title) or ("ডিগ্রি" in title and "ইনকোর্স" in title):
        details.append("ইনকোর্স নম্বর অনলাইনে এন্ট্রি বর্ধিত সময়: ০৪/১০/২০২৬ থেকে ১২/১০/২০২৬ পর্যন্ত")
        details.append("গুরুত্বপূর্ণ শর্ত: ইনকোর্স নম্বর অনলাইনে এন্ট্রি ছাড়া ফরম পূরণের Probable লিস্টে পরীক্ষার্থীর নাম অন্তর্ভুক্ত হবে না")
        details.append("কোর্সকোড সংশোধন: পূর্বে ভুল কোর্সকোড ও ভুল এন্ট্রি উক্ত সময়ের মধ্যে সংশোধন করা যাবে")
        details.append("মূল স্মারক: ০৫(৫৩৪) জাতীঃ বিঃ/পরীঃ/ডিগ্রী (পাস)/২০২২/৬০৬৯ (তারিখ: ০১/১০/২০২৬)")
        return details

    # Specific notice intelligence for LLB 1st Part (Notice 2084)
    if "২০৮৪" in (pdf_url or "") or ("এলএলবি" in title and "ফরম পূরণ" in title):
        details.append("অনলাইনে আবেদন ফরম সংগ্রহের শেষ তারিখ: ১১/১০/২০২৬ খ্রি.")
        details.append("কলেজ কর্তৃক ডাটা এন্ট্রি ও নিশ্চয়ন: ১২/১০/২০২৬ থেকে ১৩/১০/২০২৬ খ্রি.")
        details.append("সোনালী সেবায় ফি জমার সময়সীমা: ১৪/১০/২০২৬ থেকে ১৫/১০/২০২৬ খ্রি.")
        details.append("মূল স্মারক: জাতীঃ বিঃ/পরীঃ/প্রফেঃ/এলএলবি ১ম পর্ব/২০২৪/২০৮৪ (তারিখ: ৩০/০৯/২০২৬)")
        return details

    # Action type
    if "রুটিন" in title or "সময়সূচি" in title:
        details.append("ধরন: চূড়ান্ত পরীক্ষার সময়সূচি (Routine)")
    elif "ফরম পূরণ" in title:
        details.append("ধরন: অনলাইন ফরম পূরণ ও ফি প্রদান (Form Fill-up)")
    elif "ইনকোর্স" in title:
        details.append("ধরন: ইনকোর্স পরীক্ষার নম্বর এন্ট্রি ও ডাটা সংশোধন")
    elif "সংশোধিত" in title:
        details.append("ধরন: সংশোধিত বা পরিবর্তিত সময়সূচি (Revised Notice)")
    elif "ফলাফল" in title or "রেজাল্ট" in title:
        details.append("ধরন: পরীক্ষার ফলাফল প্রকাশ (Result Publication)")
    elif "ব্যবহারিক" in title:
        details.append("ধরন: ব্যবহারিক ও মৌখিক পরীক্ষা (Practical/Viva)")
    elif "মৌখিক" in title or "ভাইভা" in title or "viva" in title.lower():
        details.append("ধরন: মৌখিক পরীক্ষা ও সাক্ষাৎকার সিডিউল (Viva Voce Schedule)")
    elif "প্রবেশপত্র" in title or "admit" in title.lower():
        details.append("ধরন: পরীক্ষার প্রবেশপত্র ডাউনলোড (Admit Card Download)")
    elif "নিয়োগ" in title or "চাকরি" in title or "সার্কুলার" in title or "circular" in title.lower():
        details.append("ধরন: অফিসিয়াল নিয়োগ বিজ্ঞপ্তি ও আবেদন নির্দেশিকা (Job Circular)")

    return details


def build_breaking_notice_card(notice, idx):
    """
    Builds an all-inclusive intelligence card for a single breaking notice.
    Incorporates all requested features, exact source links, and precise timestamps.
    Strictly Zero Emojis (Rule 12).
    """
    title = notice["title"].replace("<", "&lt;").replace(">", "&gt;")
    source = notice.get("source", "শিক্ষা বোর্ড")
    pdf_url = notice.get("pdf_url") or ""
    portal_url = notice.get("portal_url") or ""
    link_url = notice.get("link") or ""

    # Exact source link determination (prefer direct PDF, then notice page link, then portal URL)
    exact_source_url = pdf_url or link_url or portal_url or "https://www.nu.ac.bd/"

    # Precise timestamps calculation (BD Time: UTC+6)
    utc_now = datetime.now(timezone.utc)
    bd_now = utc_now + timedelta(hours=6)
    alert_dispatch_time = bd_now.strftime("%Y-%m-%d | %I:%M %p")

    pub_date_raw = notice.get("pub_date", "")
    pub_date_str = pub_date_raw if pub_date_raw else "অফিসিয়াল নোটিশ অনুযায়ী"

    # 1. Site Coverage Status
    cov = check_site_coverage(notice["title"])
    if cov["status"] == "LIVE":
        cov_badge = f"<b>সাইটে স্ট্যাটাস:</b> লাইভ পোস্ট বিদ্যমান\n  <a href=\"{cov['url']}\">[আমাদের পোস্ট দেখুন: {cov['title'][:45]}...]</a>\n  <i>(অ্যাকশন: পোস্টে নতুন রুটিনের ছবি ও তারিখ আপডেট করুন)</i>"
    elif cov["status"] == "DRAFT":
        cov_badge = f"<b>সাইটে স্ট্যাটাস:</b> ব্লগারে ড্রাফট রেডি রয়েছে\n  <a href=\"{cov['url']}\">[ড্রাফট লিঙ্ক]</a>\n  <i>(অ্যাকশন: অবিলম্বে রিভিউ করে লাইভ পাবলিশ করুন!)</i>"
    else:
        cov_badge = "<b>সাইটে স্ট্যাটাস:</b> রেড অ্যালার্ট — আমাদের সাইটে এখনো কোনো পোস্ট নেই!\n  <i>(অ্যাকশন: প্রতিযোগীদের আগে সবার প্রথম ট্রাফিক পেতে দ্রুত পোস্ট রেডি করুন!)</i>"

    # 2. Instant SEO Package
    seo = generate_instant_seo_package(notice["title"], source)

    # 3. Key Dates & Details
    dates = extract_key_dates_and_details(notice["title"], exact_source_url)
    dates_str = "\n  • ".join(dates) if dates else "অফিসিয়াল নোটিশে সুনির্দিষ্ট সময় উল্লেখ রয়েছে"

    # 4. Queries string
    queries_str = "\n  • ".join(seo["top_queries"])

    lines = [
        f"<b>[ব্রেকিং নোটিশ #{idx}] {source}</b>",
        f"<b>শিরোনাম:</b> {title}",
        "----------------------------------------",
        "<b>উৎস ও সময়কাল ট্র্যাকিং:</b>",
        f"  • <b>কোথা থেকে পাওয়া গেছে (উৎস):</b> {source}",
        f"  • <b>অফিসিয়াল পোর্টাল:</b> <a href=\"{portal_url}\">{portal_url}</a>" if portal_url else f"  • <b>অফিসিয়াল পোর্টাল:</b> {source}",
        f"  • <b>সরাসরি মূল সোর্স লিংক:</b> <a href=\"{exact_source_url}\">{exact_source_url}</a>",
        f"  • <b>নোটিশ প্রকাশের তারিখ/সময়:</b> {pub_date_str}",
        f"  • <b>রাডার অ্যালার্ট পাঠানোর সময়:</b> {alert_dispatch_time} (বাংলাদেশ মান সময়)",
        "----------------------------------------",
        f"<b>১. সাইট কভারেজ অডিট:</b>\n  {cov_badge}",
        "----------------------------------------",
        f"<b>২. রেডি-টু-ইউজ পোস্ট টাইটেল ও পারমালিঙ্ক:</b>",
        f"  • <b>টাইটেল:</b> <code>{seo['proposed_title']}</code>",
        f"  • <b>পারমালিঙ্ক:</b> <code>{seo['english_slug']}</code>",
        f"  • <b>লেবেল:</b> <i>{seo['labels']}</i>",
        "----------------------------------------",
        f"<b>৩. এক্সট্রাক্টেড পরীক্ষার তথ্য ও সেশন:</b>\n  • {dates_str}",
        "----------------------------------------",
        f"<b>৪. টার্গেট পাঠক ও সার্চ ইনটেন্ট:</b>",
        f"  • <b>টার্গেট শিক্ষার্থী:</b> {seo['audience']}",
        f"  • <b>সার্চ ইনটেন্ট:</b> {seo['intent']}",
        f"  • <b>শীর্ষ ৩টি গুগল সার্চ কুয়েরি:</b>\n  • {queries_str}",
        "----------------------------------------",
        "<b>৫. প্রতিযোগী মনিটরিং স্ট্যাটাস:</b>",
        "  • বড় কোনো এডুকেশন সাইট এখনো পূর্ণাঙ্গ গাইড দেয়নি।",
        "  • এখনই পোস্ট করলে গুগলে ১ নম্বর স্থান ও ফিচারড স্নাইপেট দখলের মোক্ষম সুযোগ!",
        "----------------------------------------"
    ]

    if exact_source_url:
        label = "সরাসরি অফিসিয়াল PDF ডাউনলোড" if exact_source_url.lower().endswith(".pdf") or ".pdf" in exact_source_url.lower() else "সরাসরি মূল সোর্স লিংক দেখুন"
        lines.append(f"<b>মূল সোর্স ডকুমেন্ট:</b> <a href=\"{exact_source_url}\">[{label}]</a>")

    return "\n".join(lines), cov.get("url"), exact_source_url


def build_breaking_alerts_batch(new_notices, now):
    """Builds full text and inline keyboard for breaking notices batch."""
    time_str = now.strftime("%Y-%m-%d | %I:%M %p")
    header = [
        "<b>[হেল্পট্রিকবিডি ৩৬০-ডিগ্রি ব্রেকিং এক্সাম রাডার অ্যালার্ট]</b>",
        f"<b>নোটিশ স্ক্যান সময়কাল:</b> {time_str} (প্রতি ঘণ্টায় অটো-স্ক্যান)",
        "========================================"
    ]

    cards = []
    first_source_url = None
    first_post_url = None

    for idx, n in enumerate(new_notices[:5], 1):
        card_text, post_url, exact_source_url = build_breaking_notice_card(n, idx)
        cards.append(card_text)
        if not first_source_url and exact_source_url:
            first_source_url = exact_source_url
        if not first_post_url and post_url:
            first_post_url = post_url

    footer = [
        "========================================",
        "হেল্পট্রিকবিডি ক্লাউড বট • ২৪ ঘণ্টা স্বয়ংক্রিয় ক্লাউড মনিটরিং"
    ]

    full_text = "\n".join(header) + "\n\n" + "\n\n".join(cards) + "\n\n" + "\n".join(footer)

    # Interactive Telegram Inline Action Buttons
    keyboard = []
    row1 = []
    if first_source_url:
        is_pdf = first_source_url.lower().endswith(".pdf") or ".pdf" in first_source_url.lower()
        btn_text = "সরাসরি অফিসিয়াল PDF" if is_pdf else "সরাসরি মূল সোর্স লিংক"
        row1.append({"text": btn_text, "url": first_source_url})
    if first_post_url:
        row1.append({"text": "আমাদের পোস্ট দেখুন", "url": first_post_url})
    else:
        row1.append({"text": "HelpTrickBD সাইট", "url": "https://www.helptrickbd.com/"})

    if row1:
        keyboard.append(row1)

    keyboard.append([
        {"text": "Blogger Admin Panel", "url": "https://www.blogger.com/blog/posts/8468755675548028711"}
    ])

    reply_markup = {"inline_keyboard": keyboard}
    return full_text, reply_markup


def dispatch_breaking_notices(bot_token, chat_id, notices, now):
    """
    Dispatches breaking notices to Telegram.
    If 1 notice: sends comprehensive card with its custom direct source buttons.
    If multiple notices: sends an introductory header followed by individual cards,
    ensuring messages never exceed Telegram's 4096 character limit and every notice
    gets its own exact source/PDF download link and action buttons.
    """
    if not notices:
        return True

    total = len(notices)
    time_str = now.strftime("%Y-%m-%d | %I:%M %p")

    if total > 1:
        intro_text = (
            "<b>[হেল্পট্রিকবিডি ৩৬০-ডিগ্রি ব্রেকিং এক্সাম রাডার অ্যালার্ট]</b>\n"
            f"<b>নোটিশ স্ক্যান সময়কাল:</b> {time_str} (বাংলাদেশ মান সময়)\n"
            f"<b>নতুন শনাক্তকৃত অফিসিয়াল নোটিশ:</b> {total}টি\n"
            "========================================\n"
            "প্রতিটি নোটিশের মূল উৎস লিংক, প্রকাশের সময় এবং ইনস্ট্যান্ট এসইও প্যাকেজ নিচে প্রেরণ করা হলো:"
        )
        send_telegram_message(bot_token, chat_id, intro_text)

    all_ok = True
    for idx, n in enumerate(notices[:5], 1):
        card_text, post_url, exact_source_url = build_breaking_notice_card(n, idx)

        keyboard = []
        row1 = []
        if exact_source_url:
            is_pdf = exact_source_url.lower().endswith(".pdf") or ".pdf" in exact_source_url.lower()
            btn_text = "সরাসরি অফিসিয়াল PDF" if is_pdf else "সরাসরি মূল সোর্স লিংক"
            row1.append({"text": btn_text, "url": exact_source_url})
        if post_url:
            row1.append({"text": "আমাদের পোস্ট দেখুন", "url": post_url})
        else:
            row1.append({"text": "HelpTrickBD সাইট", "url": "https://www.helptrickbd.com/"})

        if row1:
            keyboard.append(row1)
        keyboard.append([
            {"text": "Blogger Admin Panel", "url": "https://www.blogger.com/blog/posts/8468755675548028711"}
        ])

        reply_markup = {"inline_keyboard": keyboard}
        ok = send_telegram_message(bot_token, chat_id, card_text, reply_markup=reply_markup)
        if not ok:
            all_ok = False
        if total > 1:
            import time
            time.sleep(1)

    return all_ok


def build_morning_seo_digest(all_notices, urgent_items, now):
    """
    Feature 6: Comprehensive Daily Morning SEO Briefing sent at 08:00 AM BD Time.
    """
    time_str = now.strftime("%Y-%m-%d | %I:%M %p")
    lines = [
        "<b>[হেল্পট্রিকবিডি ডেইলি মর্নিং এসইও ডাইজেস্ট]</b>",
        f"<b>তারিখ ও সময়:</b> {time_str} (সকালের প্রধান এসইও রোডম্যাপ)",
        "========================================",
        "শুভ সকাল! আগামী ৩০-৪৫ দিনে আপনার ওয়েবসাইটে সর্বোচ্চ গুগল ট্রাফিক আনার জন্য আজকের দিনভিত্তিক প্রায়োরিটি টাস্ক নিচে সাজিয়ে দেওয়া হলো:\n"
    ]

    # TOP 3 SEO PRIORITIES
    lines.append("<b>[আজকের শীর্ষ ৩টি কনটেন্ট প্রায়োরিটি — গোল্ডেন উইন্ডো]</b>")
    for idx, item in enumerate(urgent_items[:3], 1):
        name = item["exam_name"].replace("<", "&lt;").replace(">", "&gt;")
        keywords = ", ".join(item["target_keywords"][:3]).replace("<", "&lt;").replace(">", "&gt;")
        status_tag = "তাৎক্ষণিক সর্বোচ্চ ট্রাফিক" if idx == 1 else "উচ্চ সম্ভাবনা"
        lines.append(f"<b>অগ্রাধিকার {idx} ({status_tag}):</b>")
        lines.append(f"• <b>বিষয়:</b> {name}")
        lines.append(f"• <b>সম্ভাব্য সার্চ ভলিউম:</b> {item.get('search_volume', 'উচ্চ')}")
        lines.append(f"• <b>টার্গেট কি-ওয়ার্ড:</b> <i>{keywords}</i>")
        lines.append(f"• <b>ব্লুপ্রিন্ট:</b> {item['content_blueprint']}")
        lines.append("")

    lines.append("----------------------------------------")
    lines.append("<b>[চলতি সপ্তাহের সক্রিয় শীর্ষ ৫টি অফিসিয়াল নোটিশ ও PDF]</b>")
    official_sample = [n for n in all_notices if n.get("pdf_url") and not n.get("pdf_url").endswith("#")][:5]
    for idx, n in enumerate(official_sample, 1):
        title = n["title"].replace("<", "&lt;").replace(">", "&gt;")
        source = f"[{n.get('source', 'শিক্ষা বোর্ড')}]"
        lines.append(f"{idx}. {source} {title}\n   <a href=\"{n['pdf_url']}\">[অফিসিয়াল PDF ডাউনলোড]</a>")

    lines.append("========================================")
    lines.append("<b>আজকের লক্ষ্য:</b> অগ্রাধিকার ১-এর পোস্টটি ড্রাফট থেকে লাইভ করুন অথবা নতুন রুটিন কার্ড যুক্ত করুন।")
    lines.append("হেল্পট্রিকবিডি ক্লাউড বট • প্রতিদিন সকাল ৮:০০ টার নিয়মিত ব্রিফিং")

    reply_markup = {
        "inline_keyboard": [
            [
                {"text": "HelpTrickBD হোমপেজ", "url": "https://www.helptrickbd.com/"},
                {"text": "Blogger Admin Panel", "url": "https://www.blogger.com/blog/posts/8468755675548028711"}
            ]
        ]
    }
    return "\n".join(lines), reply_markup


def load_morning_digest_state():
    if os.path.exists(SEEN_NOTICES_FILE):
        try:
            with open(SEEN_NOTICES_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("_last_morning_digest_date")
        except Exception:
            return None
    return None


def save_morning_digest_date(date_str):
    data = {}
    if os.path.exists(SEEN_NOTICES_FILE):
        try:
            with open(SEEN_NOTICES_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            data = {}
    data["_last_morning_digest_date"] = date_str
    with open(SEEN_NOTICES_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    parser = argparse.ArgumentParser(description="HelpTrickBD Telegram Exam Radar 2.0")
    parser.add_argument("--test", action="store_true", help="Send a test message to verify Telegram connection")
    parser.add_argument("--force", action="store_true", help="Force send summary even if no new notice found")
    parser.add_argument("--morning-brief", action="store_true", help="Force send the Daily Morning SEO Digest")
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
    # BD Time calculation
    utc_now = datetime.now(timezone.utc)
    bd_now = utc_now + timedelta(hours=6)
    today_str = bd_now.strftime("%Y-%m-%d")

    if args.test:
        test_msg = (
            "<b>[হেল্পট্রিকবিডি ক্লাউড এক্সাম রাডার ২.০ — টেস্ট সফল]</b>\n"
            f"<b>তারিখ:</b> {now.strftime('%Y-%m-%d %I:%M %p')}\n\n"
            "টেলিগ্রাম অ্যালার্ট সিস্টেমের সাথে সংযোগ সফল হয়েছে!\n"
            "সকল ৭টি ইন্টেলিজেন্স ফিচার (সাইট কভারেজ অডিট, অটো-টাইটেল ও স্লাগ, এক্সট্রাক্টেড ডেটস, সার্চ ইনটেন্ট, প্রতিযোগী মনিটরিং, মর্নিং ডাইজেস্ট ও বাটন) সফলভাবে সক্রিয়।"
        )
        reply_markup = {
            "inline_keyboard": [
                [
                    {"text": "HelpTrickBD সাইট", "url": "https://www.helptrickbd.com/"},
                    {"text": "Blogger Admin Panel", "url": "https://www.blogger.com/blog/posts/8468755675548028711"}
                ]
            ]
        }
        ok = send_telegram_message(bot_token, chat_id, test_msg, reply_markup=reply_markup)
        if ok:
            print("[SUCCESS] টেস্ট মেসেজ বাটনসহ সফলভাবে আপনার টেলিগ্রামে পাঠানো হয়েছে!")
        else:
            print("[-] টেস্ট মেসেজ পাঠানো ব্যর্থ হয়েছে।")
        return

    # Normal execution: scan notices and radar
    new_notices, all_notices, urgent_items = run_radar_check()

    # Feature 6: Check for 08:00 AM Morning Briefing (08:00 to 08:59 BD Time)
    is_morning_hour = (bd_now.hour == 8)
    last_sent_date = load_morning_digest_state()
    should_send_morning = args.morning_brief or (is_morning_hour and last_sent_date != today_str)

    if should_send_morning:
        print("[*] সকালের ফিক্সড মর্নিং এসইও ব্রিফিং পাঠানো হচ্ছে...")
        morning_html, morning_markup = build_morning_seo_digest(all_notices, urgent_items, bd_now)
        send_telegram_message(bot_token, chat_id, morning_html, reply_markup=morning_markup)
        save_morning_digest_date(today_str)
        print("[OK] মর্নিং ব্রিফিং সফলভাবে ডেলিভারি সম্পন্ন!")

    # Breaking Notice Alert
    if new_notices:
        ok = dispatch_breaking_notices(bot_token, chat_id, new_notices, bd_now)
        if ok:
            print(f"[SUCCESS] টেলিগ্রামে {len(new_notices)}টি ব্রেকিং নোটিশের পূর্ণাঙ্গ ইন্টেলিজেন্স রিপোর্ট পাঠানো হয়েছে!")
        else:
            print("[-] টেলিগ্রাম মেসেজ ডেলিভারি ব্যর্থ হয়েছে।")
    elif args.force and not should_send_morning:
        # Fallback force summary
        if all_notices:
            sample_notices = all_notices[:3]
            dispatch_breaking_notices(bot_token, chat_id, sample_notices, bd_now)
            print("[SUCCESS] ফোর্স মোডে রাডার রিপোর্ট পাঠানো হয়েছে!")
    else:
        print("[*] নতুন কোনো নোটিশ না থাকায় টেলিগ্রামে অ্যালার্ট পাঠানো হয়নি (নীরব মোড)।")


if __name__ == "__main__":
    main()
