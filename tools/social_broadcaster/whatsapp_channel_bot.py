#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HelpTrickBD WhatsApp Channel Automated Safe Broadcaster
-------------------------------------------------------
Automates posting verified, rich educational updates to WhatsApp Channels
using local Chrome browser session with human-like safety pacing.

Features:
- 100% Free & Local: Uses real Chrome with persistent user data directory.
- Rich Preview Guarantee: Pauses 4.5 seconds after pasting so WhatsApp generates
  the large 16:9 featured banner preview card before sending.
- Anti-Ban Safe Pacing: 25-30 second intervals between posts to respect rate limits.
- Resumable: Tracks published posts in `output_posts/whatsapp_broadcast_progress.json`.
- Zero-Emoji Compliance: Follows Helptrickbd governance standard.

Usage:
    python tools/social_broadcaster/whatsapp_channel_bot.py --limit 5
    python tools/social_broadcaster/whatsapp_channel_bot.py --all
    python tools/social_broadcaster/whatsapp_channel_bot.py --dry-run
"""

import os
import sys
import re
import json
import time
import argparse
from datetime import datetime

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
MASTER_MD_PATH = os.path.join(PROJECT_ROOT, "output_posts", "social_unposted_messages_master.md")
PROGRESS_JSON_PATH = os.path.join(PROJECT_ROOT, "output_posts", "whatsapp_broadcast_progress.json")
DEFAULT_PROFILE_DIR = os.path.join(PROJECT_ROOT, ".whatsapp_web_profile")


def copy_to_clipboard(text):
    """Copies text to Windows system clipboard using standard library tkinter."""
    try:
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()
        root.clipboard_clear()
        root.clipboard_append(text)
        root.update()
        root.destroy()
        return True
    except Exception as e:
        print(f"[!] Clipboard copy warning: {e}")
        return False


def load_all_posts():
    """Parses all 112 WhatsApp formatted posts from the master markdown file."""
    if not os.path.exists(MASTER_MD_PATH):
        print(f"[!] Master markdown file not found: {MASTER_MD_PATH}")
        return []

    with open(MASTER_MD_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    sections = content.split("### [WA-")
    posts = []
    for sec in sections[1:]:
        full_sec = "### [WA-" + sec
        m_id = re.search(r"### \[(WA-\d+)\] ([^\r\n]+)", full_sec)
        
        c_start = full_sec.find("```text")
        if c_start != -1:
            nl = full_sec.find("\n", c_start)
            c_end = full_sec.find("```", nl)
            msg = full_sec[nl+1:c_end].strip()
        else:
            msg = ""

        m_url = re.search(r"- \*\*[^\*]+:\*\* (https://[^\r\n]+)", full_sec)
        m_cat = re.search(r"- \*\*ক্যাটাগরি:\*\* ([^\r\n]+)", full_sec)

        if m_id and msg:
            posts.append({
                "id": m_id.group(1),
                "title": m_id.group(2).strip(),
                "url": m_url.group(1).strip() if m_url else "",
                "category": m_cat.group(1).strip() if m_cat else "",
                "message": msg
            })

    return posts


def load_progress():
    """Loads broadcasting progress from JSON."""
    if os.path.exists(PROGRESS_JSON_PATH):
        try:
            with open(PROGRESS_JSON_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"completed_ids": [], "history": []}


def save_progress(progress):
    """Saves broadcasting progress to JSON."""
    progress["last_updated"] = datetime.now().isoformat()
    with open(PROGRESS_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(progress, f, indent=2, ensure_ascii=False)


def find_input_box(driver):
    """Finds the WhatsApp Channel active input box using multiple resilient selectors."""
    from selenium.webdriver.common.by import By

    selectors = [
        "//footer//div[@contenteditable='true']",
        "//div[@contenteditable='true'][@data-tab='10']",
        "//div[@contenteditable='true'][contains(@aria-placeholder, 'update')]",
        "//div[@contenteditable='true'][contains(@aria-placeholder, 'মেসেজ')]",
        "//div[@contenteditable='true'][contains(@aria-placeholder, 'আপডেট')]",
        "//div[@contenteditable='true'][@role='textbox']",
        "//div[@contenteditable='true']"
    ]

    for sel in selectors:
        try:
            elements = driver.find_elements(By.XPATH, sel)
            for el in elements:
                if el.is_displayed() and el.is_enabled():
                    return el
        except Exception:
            continue

    return None


def run_bot(args):
    print("=" * 70)
    print("HelpTrickBD WhatsApp Channel Automated Safe Broadcaster")
    print("=" * 70)

    all_posts = load_all_posts()
    print(f"[*] মাস্টার ফাইল থেকে মোট পোস্ট লোড হয়েছে: {len(all_posts)} টি")

    if not all_posts:
        print("[!] কোনো পোস্ট পাওয়া যায়নি। ফাইল পাথ যাচাই করুন।")
        return

    progress = load_progress()
    if args.reset:
        progress = {"completed_ids": [], "history": []}
        save_progress(progress)
        print("[*] হিস্ট্রি ও প্রগ্রেস রিসেট করা হয়েছে।")

    completed = set(progress.get("completed_ids", []))
    print(f"[*] পূর্বে সম্পন্ন হওয়া পোস্ট: {len(completed)} টি")

    # Filter unposted
    pending_posts = [p for p in all_posts if p["id"] not in completed]
    print(f"[*] বর্তমানে পোস্ট করা বাকি: {len(pending_posts)} টি")

    if not pending_posts:
        print("[*] অভিনন্দন! সব পোস্ট ইতিমধ্যে সফলভাবে প্রেরণ করা হয়েছে।")
        return

    if args.start_from:
        start_idx = 0
        for i, p in enumerate(pending_posts):
            if p["id"] == args.start_from:
                start_idx = i
                break
        pending_posts = pending_posts[start_idx:]

    target_count = len(pending_posts) if args.all else min(args.limit, len(pending_posts))
    queue = pending_posts[:target_count]

    print(f"[*] এই সেশনে পাঠানো হবে: {len(queue)} টি পোস্ট")
    print(f"[*] পোস্টের মাঝে নিরাপদ বিরতি: {args.delay} সেকেন্ড")
    print(f"[*] প্রিভিউ থাম্বনেইল লোডিং ওয়েট: {args.preview_wait} সেকেন্ড")
    print("-" * 70)

    if args.dry_run:
        print("[DRY-RUN] টেস্ট মোড — কোনো মেসেজ পাঠানো হবে না:")
        for idx, item in enumerate(queue, 1):
            print(f"  {idx}. [{item['id']}] {item['title'][:55]}...")
            print(f"     URL: {item['url']}")
        return

    # Initialize Selenium
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.by import By

    print("[*] গুগল ক্রোম ব্রাউজার চালু করা হচ্ছে...")
    os.makedirs(args.profile_dir, exist_ok=True)

    options = Options()
    options.add_argument(f"--user-data-dir={args.profile_dir}")
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--disable-blink-features=AutomationControlled")

    try:
        driver = webdriver.Chrome(options=options)
    except Exception as e:
        print(f"[ERROR] ক্রোম ড্রাইভার চালু করতে ব্যর্থ: {e}")
        return

    try:
        driver.maximize_window()
        print("[*] হোয়াটসঅ্যাপ ওয়েব লোড করা হচ্ছে: https://web.whatsapp.com/")
        driver.get("https://web.whatsapp.com/")

        # Login and Channel Navigation Guide
        print("\n" + "=" * 70)
        print("নির্দেশনা (দয়া করে ব্রাউজারে লক্ষ্য করুন):")
        print("১. যদি কিউআর কোড (QR Code) দেখা যায়, ফোনের হোয়াটসঅ্যাপ দিয়ে স্ক্যান করুন।")
        print("২. লগইন হওয়ার পর আপনার হোয়াটসঅ্যাপ চ্যানেলের (Channel) ওপর ক্লিক করে চ্যানেলটি ওপেন করুন।")
        print("৩. চ্যানেল উইন্ডো ওপেন হলে নিচে কীবোর্ডের [Enter] চাপুন...")
        print("=" * 70 + "\n")

        input(">> চ্যানেল ওপেন করে এখানে [Enter] চাপুন: ")

        print("\n[*] চ্যাট ইনপুট বক্স খোঁজা হচ্ছে...")
        input_box = find_input_box(driver)
        if not input_box:
            print("[!] চ্যাট ইনপুট বক্স স্বয়ংক্রিয়ভাবে পাওয়া যায়নি।")
            print("অনুগ্রহ করে ব্রাউজারে 'Type an update' ইনপুট বক্সে একবার মাউস দিয়ে ক্লিক করুন।")
            input(">> ক্লিক করার পর এখানে [Enter] চাপুন: ")
            input_box = find_input_box(driver)

        if not input_box:
            print("[ERROR] ইনপুট বক্স লোকেট করা যায়নি। স্ক্রিপ্ট স্থগিত করা হলো।")
            return

        print("[OK] ইনপুট বক্স সফলভাবে চিহ্নিত হয়েছে। অটো-পোস্টিং শুরু হচ্ছে...\n")

        success_count = 0
        for idx, post in enumerate(queue, 1):
            print(f"--- [{idx}/{len(queue)}] প্রক্রিয়াকরণ: [{post['id']}] {post['title'][:45]}... ---")
            
            # Step 1: Copy to clipboard
            if not copy_to_clipboard(post["message"]):
                print("[!] ক্লিপবোর্ডে কপি করতে ব্যর্থ, বাদ দেওয়া হলো।")
                continue

            # Step 2: Focus and paste
            try:
                # Re-find input box to avoid stale element reference
                curr_box = find_input_box(driver)
                if curr_box:
                    input_box = curr_box
                input_box.click()
                time.sleep(0.5)

                actions = ActionChains(driver)
                actions.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
                print("    > মেসেজ পেস্ট করা হয়েছে।")

                # Step 3: Wait for rich preview card with thumbnail
                print(f"    > থাম্বনেইল প্রিভিউ কার্ড লোড হতে {args.preview_wait} সেকেন্ড অপেক্ষা করা হচ্ছে...")
                time.sleep(args.preview_wait)

                # Step 4: Send
                actions = ActionChains(driver)
                actions.send_keys(Keys.ENTER).perform()
                time.sleep(1.0)
                print("    > [সফল] পোস্টটি চ্যানেলে প্রেরণ করা হয়েছে!")

                # Step 5: Log progress
                completed.add(post["id"])
                progress["completed_ids"] = sorted(list(completed))
                progress["history"].append({
                    "id": post["id"],
                    "title": post["title"],
                    "url": post["url"],
                    "sent_at": datetime.now().isoformat()
                })
                save_progress(progress)
                success_count += 1

            except Exception as e:
                print(f"    [!] পোস্ট পাঠাতে ত্রুটি: {e}")

            # Safe human delay before next post
            if idx < len(queue):
                print(f"    > পরবর্তী পোস্টের জন্য নিরাপদ বিরতি ({args.delay} সেকেন্ড):", end="", flush=True)
                for remaining in range(int(args.delay), 0, -5):
                    print(f" {remaining}s...", end="", flush=True)
                    time.sleep(min(5, remaining))
                print(" প্রস্তুত।\n")

        print("\n" + "=" * 70)
        print(f"সেশন সমাপ্ত: মোট {success_count} টি পোস্ট সফলভাবে চ্যানেলে সম্প্রচার করা হয়েছে!")
        print(f"বাকি রয়েছে: {len(all_posts) - len(completed)} টি পোস্ট।")
        print("=" * 70)

    finally:
        print("\n[*] ব্রাউজার খোলা রাখা হয়েছে। আপনি নিজে চেক করতে পারেন।")
        input(">> ব্রাউজার বন্ধ করতে এখানে [Enter] চাপুন: ")
        try:
            driver.quit()
        except Exception:
            pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HelpTrickBD WhatsApp Channel Automated Broadcaster")
    parser.add_argument("--limit", type=int, default=5, help="এই সেশনে সর্বোচ্চ কয়টি পোস্ট পাঠানো হবে (ডিফল্ট: ৫)")
    parser.add_argument("--all", action="store_true", help="বাকি থাকা সব পোস্ট একসাথে পাঠানো")
    parser.add_argument("--delay", type=float, default=25.0, help="পোস্টের মাঝে বিরতির সময় (সেকেন্ড)")
    parser.add_argument("--preview-wait", type=float, default=4.5, help="থাম্বনেইল প্রিভিউ লোড হতে অপেক্ষার সময় (সেকেন্ড)")
    parser.add_argument("--start-from", type=str, default=None, help="সুনির্দিষ্ট কোনো পোস্ট আইডি থেকে শুরু করা (যেমন WA-003)")
    parser.add_argument("--reset", action="store_true", help="হিস্ট্রি রিসেট করা")
    parser.add_argument("--dry-run", action="store_true", help="পরীক্ষামূলকভাবে তালিকা দেখা (কোনো পোস্ট হবে না)")
    parser.add_argument("--profile-dir", type=str, default=DEFAULT_PROFILE_DIR, help="ক্রোম প্রোফাইল ডিরেক্টরি")

    args = parser.parse_args()
    run_bot(args)
