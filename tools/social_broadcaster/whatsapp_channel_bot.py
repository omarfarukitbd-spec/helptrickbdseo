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
- Verified Paste & Send Button Click: Ensures text is really inserted and clicks
  the green Send button (paper plane icon) rather than relying on Enter key.
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


def cleanup_orphaned_chrome(profile_dir):
    """Gracefully terminates any leftover Chrome processes using this profile to prevent launch crashes."""
    import subprocess
    prof_name = os.path.basename(profile_dir)
    ps_cmd = f"""
    $processes = Get-CimInstance Win32_Process -Filter "Name = 'chrome.exe'"
    foreach ($p in $processes) {{
        if ($p.CommandLine -like "*{prof_name}*") {{
            Stop-Process -Id $p.ProcessId -Force
        }}
    }}
    """
    try:
        subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-Command", ps_cmd], capture_output=True, timeout=8)
        time.sleep(1)
    except Exception:
        pass

    for lock in ["SingletonLock", "SingletonCookie", "SingletonSocket", "lockfile"]:
        lp = os.path.join(profile_dir, lock)
        if os.path.exists(lp):
            try:
                os.remove(lp)
            except Exception:
                pass


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

    # Strategy 1: Check currently focused / active element
    try:
        active = driver.switch_to.active_element
        if active and active.is_displayed():
            ce = active.get_attribute("contenteditable")
            role = active.get_attribute("role")
            if ce == "true" or role == "textbox":
                return active
    except Exception:
        pass

    # Strategy 2: JavaScript querySelector for any contenteditable element
    try:
        js_elem = driver.execute_script("""
            var el = document.querySelector('footer div[contenteditable="true"]') ||
                     document.querySelector('div[contenteditable="true"][data-tab="10"]') ||
                     document.querySelector('div[contenteditable="true"][role="textbox"]') ||
                     document.querySelector('div[contenteditable="true"]');
            return el;
        """)
        if js_elem and js_elem.is_displayed():
            return js_elem
    except Exception:
        pass

    # Strategy 3: Resilient XPath selectors
    selectors = [
        "//footer//div[@contenteditable='true']",
        "//div[@contenteditable='true'][@data-tab='10']",
        "//div[@contenteditable='true'][@role='textbox']",
        "//div[@contenteditable='true']",
        "//p[contains(@class, 'selectable-text')]",
        "//*[contains(@aria-placeholder, 'update')]",
        "//*[contains(@aria-placeholder, 'আপডেট')]"
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


def paste_message_verified(driver, input_box, text):
    """
    Inserts text with 100% preservation of paragraphs, empty blank lines,
    bullet points, bold markdown, and links in WhatsApp Web channels.
    Combines OS clipboard paste (pyautogui) and Selenium Shift+Enter fallback.
    """
    import pyperclip
    from selenium.webdriver.common.keys import Keys

    # 1. Copy text to OS clipboard
    try:
        pyperclip.copy(text)
    except Exception:
        pass

    # 2. Focus input box
    try:
        driver.execute_script("arguments[0].focus();", input_box)
        time.sleep(0.2)
        input_box.click()
        time.sleep(0.2)
    except Exception:
        pass

    # 3. Clear old text
    try:
        driver.execute_script("""
            var el = arguments[0];
            el.focus();
            document.execCommand('selectAll', false, null);
            document.execCommand('delete', false, null);
        """, input_box)
        time.sleep(0.2)
    except Exception:
        pass

    # Method 1: Try OS Hardware Paste (pyautogui hotkey ctrl+v)
    pasted_with_pyautogui = False
    try:
        import pyautogui
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.6)
        check_val = driver.execute_script("return arguments[0].innerText || arguments[0].textContent || '';", input_box)
        if check_val and '\n' in check_val and len(check_val.strip()) > 30:
            pasted_with_pyautogui = True
    except Exception:
        pasted_with_pyautogui = False

    # Method 2: If OS paste did not yield multiline content, use Atomic Line insertion + Selenium Shift+Enter
    if not pasted_with_pyautogui:
        try:
            # Clear again to prevent duplicate text
            driver.execute_script("""
                var el = arguments[0];
                el.focus();
                document.execCommand('selectAll', false, null);
                document.execCommand('delete', false, null);
            """, input_box)
            time.sleep(0.2)

            lines = text.split('\n')
            for i, line in enumerate(lines):
                clean_line = line.strip('\r')
                if clean_line:
                    # Atomically insert text (preserves Bengali ligatures and special chars)
                    driver.execute_script("document.execCommand('insertText', false, arguments[0]);", clean_line)
                    time.sleep(0.02)
                if i < len(lines) - 1:
                    # Send Shift+Enter to trigger Lexical's KEY_ENTER_COMMAND / paragraph break
                    input_box.send_keys(Keys.SHIFT, Keys.ENTER)
                    time.sleep(0.04)

            time.sleep(0.3)
        except Exception as e:
            print(f"    [!] টেক্সট ইনসার্ট করতে সমস্যা: {e}")
            return False

    final_val = driver.execute_script("return arguments[0].innerText || arguments[0].textContent || '';", input_box)
    return bool(final_val.strip())




def click_send_button(driver, input_box):
    """Finds and clicks the WhatsApp Channel green Send button, with fallback to Enter."""
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys

    send_selectors = [
        "//span[@data-icon='send']/ancestor::button",
        "//span[@data-icon='send']",
        "//button[@aria-label='Send']",
        "//button[contains(@aria-label, 'সেন্ড')]",
        "//button[contains(@aria-label, 'পাঠান')]",
        "//span[@data-icon='send-refreshed']/ancestor::button",
        "//footer//button[contains(@class, 'send')]"
    ]

    for sel in send_selectors:
        try:
            btns = driver.find_elements(By.XPATH, sel)
            for b in btns:
                if b.is_displayed():
                    b.click()
                    return True
        except Exception:
            continue

    # Fallback: Press ENTER on input_box
    try:
        input_box.send_keys(Keys.ENTER)
        return True
    except Exception:
        pass

    return False


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

    # Clean up any lingering Chrome from previous runs
    print("[*] পূর্বের কোনো উইন্ডো থাকলে তা পরিষ্কার করা হচ্ছে...")
    cleanup_orphaned_chrome(args.profile_dir)

    # Initialize Selenium
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

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

            # Step 1: Verified paste
            pasted = paste_message_verified(driver, input_box, post["message"])
            if not pasted:
                print("    [!] মেসেজ পেস্ট নিশ্চিত করা যায়নি। বাদ দেওয়া হলো।")
                continue
            print("    > মেসেজ সফলভাবে পেস্ট হয়েছে।")

            # Step 2: Wait for rich preview card with thumbnail
            print(f"    > থাম্বনেইল প্রিভিউ কার্ড লোড হতে {args.preview_wait} সেকেন্ড অপেক্ষা করা হচ্ছে...")
            time.sleep(args.preview_wait)

            # Step 3: Send via green Send button click (or Enter fallback)
            sent = click_send_button(driver, input_box)
            if sent:
                time.sleep(1.0)
                print("    > [সফল] পোস্টটি চ্যানেলে প্রেরণ করা হয়েছে!")
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
            else:
                print("    [!] সেন্ড বাটন ক্লিক করতে ব্যর্থ হয়েছে।")

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
