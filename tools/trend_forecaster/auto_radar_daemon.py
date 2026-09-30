#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/trend_forecaster/auto_radar_daemon.py
-------------------------------------------
Helptrickbd Autonomous 3-Times-a-Day Exam Radar & Instant Notice Alert System.

Features:
- Scans Bangladesh Education Boards, National University, BTEB, PSC, NTRCA live feeds.
- Detects NEW notices that were published since the last scan.
- Triggers a native Windows Toast notification banner on the user's desktop immediately.
- Updates bd_exam_seo_radar_report.md with urgent actions.
- Tracks history in scratch/seen_radar_notices.json.

Zero-emoji compliance (Rule 12).
"""

import os
import sys
import json
import time
import hashlib
import subprocess
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

from tools.trend_forecaster.bd_exam_early_radar import (
    fetch_all_tier_live_notices,
    evaluate_360_degree_radar,
    generate_360_master_report,
    OUTPUT_REPORT
)
from tools.trend_forecaster.official_board_scraper import fetch_all_official_board_notices

SEEN_NOTICES_FILE = os.path.join(PROJECT_ROOT, "tools", "trend_forecaster", "seen_radar_notices.json")


def load_seen_notices():
    if os.path.exists(SEEN_NOTICES_FILE):
        try:
            with open(SEEN_NOTICES_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def save_seen_notices(data):
    os.makedirs(os.path.dirname(SEEN_NOTICES_FILE), exist_ok=True)
    with open(SEEN_NOTICES_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def make_notice_hash(notice):
    raw = f"{notice['title']}_{notice.get('pub_date', '')}"
    return hashlib.md5(raw.encode("utf-8")).hexdigest()


def send_windows_toast_alert(title, message):
    """
    Sends a native Windows Toast notification using PowerShell.
    """
    safe_title = title.replace('"', '`"').replace("'", "''")
    safe_msg = message.replace('"', '`"').replace("'", "''")
    
    ps_cmd = f"""
    [Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] > $null
    $template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02)
    $textNodes = $template.GetElementsByTagName('text')
    $textNodes.Item(0).AppendChild($template.CreateTextNode('{safe_title}')) > $null
    $textNodes.Item(1).AppendChild($template.CreateTextNode('{safe_msg}')) > $null
    $toast = [Windows.UI.Notifications.ToastNotification]::new($template)
    [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier('HelpTrickBD Exam Radar').Show($toast)
    """
    try:
        subprocess.run(["powershell", "-NoProfile", "-Command", ps_cmd], capture_output=True, timeout=5)
    except Exception:
        pass


def run_radar_check():
    """
    Runs a single scan for new routines and notices.
    Returns: (list_of_new_notices, urgent_golden_window_items)
    """
    now = datetime.now()
    seen_db = load_seen_notices()
    
    print("=" * 72)
    print("  HELPTRICKBD 3-TIMES-DAILY EXAM RADAR MONITOR")
    print(f"  চলতি সময়: {now.strftime('%Y-%m-%d %I:%M %p')}")
    print("=" * 72)

    print("[*] অফিসিয়াল শিক্ষা বোর্ড ও বিশ্ববিদ্যালয়ের নোটিশ পোর্টাল স্ক্র্যাপ করা হচ্ছে...")
    official_notices = fetch_all_official_board_notices()
    print(f"[OK] {len(official_notices)}টি অফিসিয়াল নোটিশ ও PDF সরাসরি সংগ্রহ করা হয়েছে।")

    print("[*] সর্বশেষ সংবাদ ও প্রেস বিজ্ঞপ্তি স্ক্যান করা হচ্ছে...")
    news_notices = fetch_all_tier_live_notices()
    
    # Combined notices, official first
    all_notices = official_notices + news_notices
    
    new_notices = []
    keywords_of_interest = ["রুটিন", "routine", "তারিখ", "পরীক্ষা", "ফরম পূরণ", "বিজ্ঞপ্তি", "সংশোধিত", "ভর্তি", "সার্কুলার", "ফলাফল", "রেজাল্ট", "কেন্দ্র"]

    for n in all_notices:
        n_hash = make_notice_hash(n)
        if n_hash not in seen_db:
            is_urgent = any(kw in n["title"].lower() for kw in keywords_of_interest)
            n["is_urgent"] = is_urgent
            new_notices.append(n)
            seen_db[n_hash] = {
                "title": n["title"],
                "pub_date": n.get("pub_date", ""),
                "first_seen": now.strftime("%Y-%m-%d %H:%M:%S")
            }

    print(f"[OK] মোট {len(all_notices)}টি নোটিশের মধ্যে {len(new_notices)}টি নতুন নোটিশ শনাক্ত হয়েছে।")

    # Evaluate 30-45 day Golden Window
    radar_results = evaluate_360_degree_radar(now.month)
    generate_360_master_report(radar_results, all_notices, now)
    save_seen_notices(seen_db)

    # If new urgent notices found, trigger Windows Toast Notification
    if new_notices:
        urgent_items = [n for n in new_notices if n.get("is_urgent")]
        if urgent_items:
            first = urgent_items[0]["title"]
            send_windows_toast_alert(
                "নতুন পরীক্ষার রুটিন/নোটিশ প্রকাশিত হয়েছে!",
                f"{first[:90]}... দ্রুত পোস্ট প্রস্তুত করুন!"
            )
            print(f"[ALERT] নতুন জরুরি নোটিশ শনাক্ত হয়েছে: {first}")

    return new_notices, all_notices, [r for r in radar_results if r["urgency_score"] <= 2]


if __name__ == "__main__":
    new_notices, all_notices, urgent_items = run_radar_check()
    if new_notices:
        print("\n[*] নতুন শনাক্তকৃত নোটিশসমূহ:")
        for idx, n in enumerate(new_notices, 1):
            print(f"  {idx}. {n['title']} ({n.get('pub_date', '')})")
    else:
        print("\n[*] পূর্ববর্তী স্ক্যানের তুলনায় নতুন কোনো নোটিশ নেই। সিস্টেম নিয়মিত নজরদারি করছে।")
