#!/usr/bin/env python3
"""
tools/social_broadcaster/broadcaster.py
HelpTrickBD Master Social Broadcaster CLI.

Coordinates the automated publishing flow across Telegram, Facebook Page,
and WhatsApp Channel with mandatory terminal preview and confirmation.
Strictly zero-emoji compliant.
"""

import os
import sys
import json
import argparse
import urllib.request
from typing import Dict, Any, Optional
from bs4 import BeautifulSoup

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

# Ensure project root in path
MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(MODULE_DIR, "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.social_broadcaster.social_copy_generator import SocialCopyGenerator
from tools.social_broadcaster.telegram_publisher import TelegramPublisher
from tools.social_broadcaster.facebook_publisher import FacebookPublisher
from tools.social_broadcaster.whatsapp_helper import WhatsAppHelper

CONFIG_FILE = os.path.join(MODULE_DIR, "social_credentials.json")
TEMPLATE_FILE = os.path.join(MODULE_DIR, "social_credentials.template.json")


def load_config() -> Dict[str, Any]:
    """Loads social credentials from config file or returns default structure."""
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass

    if os.path.exists(TEMPLATE_FILE):
        try:
            with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass

    return {
        "telegram": {"bot_token": "", "channel_id": "@helptrickbd_official", "enabled": True},
        "facebook": {"page_id": "", "page_access_token": "", "enabled": True},
        "whatsapp": {"channel_name": "HelpTrickBD", "channel_link": "https://whatsapp.com/channel/0029Vb956jgCHDyrx1wkUh2a", "mode": "one_click_web", "enabled": true}
    }


def fetch_live_post_details(url: str) -> Dict[str, Any]:
    """Fetches title, html content, and hero image from live URL."""
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode("utf-8")

    soup = BeautifulSoup(html, "html.parser")
    title_tag = soup.find("h1", class_="post-title") or soup.find("title")
    title = title_tag.get_text(strip=True) if title_tag else "HelpTrickBD Article"
    # Clean up standard site suffix if in title
    title = title.split(" - HelpTrickBD")[0].strip()

    # Find hero image
    hero_image = ""
    og_img = soup.find("meta", property="og:image")
    if og_img and og_img.get("content"):
        hero_image = og_img["content"]
    else:
        first_img = soup.find("div", class_="post-body")
        if first_img:
            img_tag = first_img.find("img")
            if img_tag and img_tag.get("src"):
                hero_image = img_tag["src"]

    body_tag = soup.find("div", class_="post-body") or soup
    body_html = str(body_tag)

    return {
        "title": title,
        "url": url,
        "hero_image": hero_image,
        "html_content": body_html
    }


def display_preview(data: Dict[str, str], hero_image: str):
    """Displays human-readable preview before broadcasting."""
    line = "=" * 70
    subline = "-" * 70
    print("\n" + line)
    print(" হেল্পট্রিকবিডি সোশ্যাল পোস্ট প্রিভিউ (Social Post Preview)")
    print(line)
    print(f"শিরোনাম: {data['title']}")
    print(f"পোস্ট লিংক: {data['post_url']}")
    print(f"কনটেন্ট ধরন (Archetype): {data['archetype']}")
    print(f"থাম্বনেইল ইমেজ: {hero_image or 'পাওয়া যায়নি (ডিফল্ট কার্ড ব্যবহৃত হবে)'}")
    print(subline)

    print("\n[১. ফেসবুক পেজ পোস্ট প্রিভিউ]:")
    print("-" * 35)
    print(data["facebook"])

    print("\n[২. টেলিগ্রাম চ্যানেল পোস্ট প্রিভিউ]:")
    print("-" * 35)
    print(data["telegram"])

    print("\n[৩. হোয়াটসঅ্যাপ চ্যানেল পোস্ট প্রিভিউ]:")
    print("-" * 35)
    print(data["whatsapp"])
    print(line + "\n")


def main():
    parser = argparse.ArgumentParser(description="HelpTrickBD Social Broadcaster Master CLI")
    parser.add_argument("--post-url", help="লাইভ পোস্টের সম্পূর্ণ ইউআরএল")
    parser.add_argument("--post-file", help="লোকাল পোস্ট এইচটিএমএল ফাইলের পাথ")
    parser.add_argument("--title", help="পোস্টের কাস্টম শিরোনাম (ঐচ্ছিক)")
    parser.add_argument("--hero-image", help="ব্যানার বা থাম্বনেইল ছবির ইউআরএল (ঐচ্ছিক)")
    parser.add_argument("--labels", help="কমা দিয়ে পৃথক করা লেবেলসমূহ (ঐচ্ছিক)")
    parser.add_argument("--dry-run", action="store_true", help="কোনো নেটওয়ার্কে না পাঠিয়ে শুধুমাত্র প্রিভিউ প্রদর্শন")
    parser.add_argument("--auto-confirm", action="store_true", help="প্রিভিউ কনফার্মেশন প্রম্পট ছাড়া সরাসরি পোস্ট")
    parser.add_argument("--check-config", action="store_true", help="এপিআই সংযোগ ও কনফিগারেশন স্ট্যাটাস পরীক্ষা")

    args = parser.parse_args()
    config = load_config()

    if args.check_config:
        print("\n--- এপিআই কনফিগারেশন ও সংযোগ পরীক্ষা ---")
        tg_pub = TelegramPublisher(
            config.get("telegram", {}).get("bot_token", ""),
            config.get("telegram", {}).get("channel_id", "")
        )
        tg_status = tg_pub.test_connection()
        print(f"টেলিগ্রাম স্ট্যাটাস: {tg_status['message']}")

        fb_pub = FacebookPublisher(
            config.get("facebook", {}).get("page_id", ""),
            config.get("facebook", {}).get("page_access_token", "")
        )
        fb_status = fb_pub.test_connection()
        print(f"ফেসবুক স্ট্যাটাস: {fb_status['message']}")
        print("হোয়াটসঅ্যাপ স্ট্যাটাস: ১-ক্লিক নিরাপদ মোড সক্রিয় (ব্যান-রিস্ক জিরো)")
        return

    if not args.post_url and not args.post_file:
        print("ত্রুটি: অনুগ্রহ করে --post-url অথবা --post-file প্রদান করুন।")
        print("সাহায্য দেখতে: python tools/social_broadcaster/broadcaster.py --help")
        return

    title = args.title or ""
    post_url = args.post_url or "https://www.helptrickbd.com/"
    hero_image = args.hero_image or ""
    html_content = ""
    labels = [lbl.strip() for lbl in args.labels.split(",")] if args.labels else []

    if args.post_file:
        if os.path.exists(args.post_file):
            with open(args.post_file, "r", encoding="utf-8") as f:
                html_content = f.read()
            if not title:
                soup = BeautifulSoup(html_content, "html.parser")
                h1 = soup.find("h1")
                title = h1.get_text(strip=True) if h1 else os.path.basename(args.post_file)
        else:
            print(f"ত্রুটি: ফাইল পাওয়া যায়নি: {args.post_file}")
            return
    elif args.post_url:
        print(f"লাইভ পোস্ট থেকে তথ্য সংগ্রহ করা হচ্ছে: {args.post_url} ...")
        try:
            live_data = fetch_live_post_details(args.post_url)
            if not title:
                title = live_data["title"]
            if not hero_image:
                hero_image = live_data["hero_image"]
            html_content = live_data["html_content"]
        except Exception as e:
            print(f"পোস্ট তথ্য সংগ্রহে ত্রুটি: {str(e)}")
            if not title:
                title = "HelpTrickBD Special Update"

    # Generate Social Copy
    generator = SocialCopyGenerator()
    generated = generator.generate_all(
        title=title,
        post_url=post_url,
        html_content=html_content,
        labels=labels,
        hero_image=hero_image
    )

    # Display Preview (Mandatory before publishing)
    display_preview(generated, hero_image)

    if args.dry_run:
        print("[ড্রাইডান মোড সম্পন্ন] কোনো সোশ্যাল চ্যানেলে ডেটা পাঠানো হয়নি।")
        return

    if not args.auto_confirm:
        confirm = input("আপনি কি এই পোস্টটি সোশ্যাল চ্যানেলগুলোতে পাবলিশ করতে চান? (y/n): ").strip().lower()
        if confirm != "y":
            print("পাবলিশিং বাতিল করা হয়েছে।")
            return

    print("\nসোশ্যাল চ্যানেলসমূহে ব্রডকাস্ট শুরু হচ্ছে...")

    # 1. Telegram Broadcast
    tg_cfg = config.get("telegram", {})
    if tg_cfg.get("enabled", True):
        tg_pub = TelegramPublisher(tg_cfg.get("bot_token", ""), tg_cfg.get("channel_id", ""))
        tg_res = tg_pub.publish_post(generated["telegram"], hero_image)
        print(f"[টেলিগ্রাম]: {tg_res['message']}")
    else:
        print("[টেলিগ্রাম]: নিষ্ক্রিয় করা রয়েছে।")

    # 2. Facebook Page Broadcast
    fb_cfg = config.get("facebook", {})
    if fb_cfg.get("enabled", True):
        fb_pub = FacebookPublisher(fb_cfg.get("page_id", ""), fb_cfg.get("page_access_token", ""))
        fb_res = fb_pub.publish_post(generated["facebook"], post_url, hero_image)
        print(f"[ফেসবুক]: {fb_res['message']}")
    else:
        print("[ফেসবুক]: নিষ্ক্রিয় করা রয়েছে।")

    # 3. WhatsApp Channel 1-Click Broadcast
    wa_cfg = config.get("whatsapp", {})
    if wa_cfg.get("enabled", True):
        wa_helper = WhatsAppHelper(wa_cfg.get("channel_link", "https://whatsapp.com/channel/0029Vb956jgCHDyrx1wkUh2a"))
        wa_res = wa_helper.trigger_broadcast(generated["whatsapp"])
        print(f"[হোয়াটসঅ্যাপ]: {wa_res['message']}")
    else:
        print("[হোয়াটসঅ্যাপ]: নিষ্ক্রিয় করা রয়েছে।")

    print("\nব্রডকাস্ট প্রক্রিয়া সফলভাবে সম্পন্ন হয়েছে।\n")


if __name__ == "__main__":
    main()
