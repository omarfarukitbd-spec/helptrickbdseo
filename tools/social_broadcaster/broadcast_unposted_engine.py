#!/usr/bin/env python3
"""
tools/social_broadcaster/broadcast_unposted_engine.py
HelpTrickBD Resilient Social Broadcaster Engine for Unposted Posts.

Reads unposted posts from output_posts/social_audit_data.json and broadcasts
them sequentially to Facebook Page (via Make.com gateway) and Telegram Channel
in chronological order (oldest to newest) with anti-spam rate limiting.
Updates state after every single post. Strictly zero-emoji compliant.
"""

import os
import sys
import time
import json
import argparse
from datetime import datetime
from typing import Dict, Any, List

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(MODULE_DIR, "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.social_broadcaster.telegram_publisher import TelegramPublisher
from tools.social_broadcaster.facebook_publisher import FacebookPublisher

CONFIG_FILE = os.path.join(MODULE_DIR, "social_credentials.json")
AUDIT_DATA_FILE = os.path.join(PROJECT_ROOT, "output_posts", "social_audit_data.json")
MASTER_MD_FILE = os.path.join(PROJECT_ROOT, "output_posts", "social_unposted_messages_master.md")


def load_config() -> Dict[str, Any]:
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def load_audit_data() -> List[Dict[str, Any]]:
    if os.path.exists(AUDIT_DATA_FILE):
        with open(AUDIT_DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_audit_data(data: List[Dict[str, Any]]) -> None:
    with open(AUDIT_DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    parser = argparse.ArgumentParser(description="HelpTrickBD Unposted Social Broadcaster Engine")
    parser.add_argument("--batch-size", type=int, default=None, help="একবারে কয়টি পোস্ট ব্রডকাস্ট করা হবে (ডিফল্ট: সব বাকি পোস্ট)")
    parser.add_argument("--delay", type=int, default=12, help="প্রতিটি পোস্টের মধ্যবর্তী বিরতি সেকেন্ডে (ডিফল্ট: ১২)")
    parser.add_argument("--facebook-only", action="store_true", help="শুধুমাত্র ফেসবুক পেজে পোস্ট করবে")
    parser.add_argument("--telegram-only", action="store_true", help="শুধুমাত্র টেলিগ্রাম চ্যানেলে পোস্ট করবে")
    parser.add_argument("--dry-run", action="store_true", help="শুধুমাত্র প্রিভিউ দেখাবে, লাইভ পাঠাবে না")
    args = parser.parse_args()

    config = load_config()
    tg_cfg = config.get("telegram", {})
    fb_cfg = config.get("facebook", {})

    tg_pub = TelegramPublisher(tg_cfg.get("bot_token", ""), tg_cfg.get("channel_id", ""))
    fb_pub = FacebookPublisher(
        page_id=fb_cfg.get("page_id", ""),
        page_access_token=fb_cfg.get("page_access_token", ""),
        make_webhook_url=fb_cfg.get("make_webhook_url", "")
    )

    records = load_audit_data()
    if not records:
        print("কোনো অডিট ডাটা পাওয়া যায়নি। output_posts/social_audit_data.json পরীক্ষা করুন।")
        return

    # Find unposted records
    # Note: records are in newest-to-oldest order in the file, so reversing gives oldest-to-newest
    unposted_indices = []
    for idx, r in enumerate(records):
        needs_fb = not r.get("posted_facebook", False) and not args.telegram_only
        needs_tg = not r.get("posted_telegram", False) and not args.facebook_only
        if needs_fb or needs_tg:
            unposted_indices.append(idx)

    total_unposted = len(unposted_indices)
    print("=" * 65)
    print(" হেল্পট্রিকবিডি সোশ্যাল ব্রডকাস্ট ইঞ্জিন (Facebook & Telegram)")
    print("=" * 65)
    print(f"মোট ব্রডকাস্ট বাকি রয়েছে: {total_unposted}টি পোস্ট")

    if total_unposted == 0:
        print("সব পোস্ট ইতিমধ্যেই ফেসবুক এবং টেলিগ্রামে প্রকাশিত হয়েছে। নতুন কোনো পোস্ট বাকি নেই।")
        return

    # Reverse to post in chronological order (oldest first)
    target_indices = list(reversed(unposted_indices))
    if args.batch_size is not None and args.batch_size > 0:
        target_indices = target_indices[:args.batch_size]

    batch_total = len(target_indices)
    print(f"বর্তমান ব্যাচে প্রক্রিয়াকরণ করা হবে: {batch_total}টি পোস্ট")
    print(f"প্রতিটি পোস্টের মধ্যবর্তী বিরতি: {args.delay} সেকেন্ড\n")

    success_count = 0
    fail_count = 0

    for i, idx in enumerate(target_indices, 1):
        r = records[idx]
        import html
        raw_title = r.get("title", "")
        title = html.unescape(raw_title)
        url = r.get("url", "")
        category = r.get("category", "")
        hero_image = r.get("hero_image", "")
        copy_data = r.get("copy", {})

        fb_message = html.unescape(copy_data.get("facebook", ""))
        tg_text = html.unescape(copy_data.get("telegram", ""))
        btn_text = html.unescape(copy_data.get("button_text", ""))

        print(f"[{i}/{batch_total}] প্রসেস করা হচ্ছে: {title}")
        print(f"  ক্যাটাগরি: {category}")
        print(f"  ইউআরএল: {url}")
        print(f"  ইমেজ: {hero_image or 'পাওয়া যায়নি'}")

        if args.dry_run:
            print("  [ড্রাই-রান মোড]: কোনো ডেটা পাঠানো হয়নি।")
            print("-" * 50)
            continue

        fb_ok = r.get("posted_facebook", False)
        tg_ok = r.get("posted_telegram", False)

        # 1. Facebook Broadcast
        if not args.telegram_only and not fb_ok:
            try:
                fb_res = fb_pub.publish_post(
                    message=fb_message,
                    link=url,
                    image_url=hero_image,
                    post_type="link",
                    title=title
                )
                if fb_res.get("success"):
                    r["posted_facebook"] = True
                    r["facebook_result"] = fb_res.get("message", "পাবলিশ সম্পন্ন")
                    r["facebook_timestamp"] = datetime.now().isoformat()
                    fb_ok = True
                    print(f"  [ফেসবুক]: {fb_res.get('message')}")
                else:
                    print(f"  [ফেসবুক ত্রুটি]: {fb_res.get('message')}")
            except Exception as e:
                print(f"  [ফেসবুক ব্যর্থ]: {str(e)}")

        # 2. Telegram Broadcast
        if not args.facebook_only and not tg_ok:
            try:
                tg_res = tg_pub.publish_post(
                    text=tg_text,
                    image_url=hero_image,
                    button_text=btn_text,
                    button_url=url
                )
                if tg_res.get("success"):
                    r["posted_telegram"] = True
                    r["telegram_msg_id"] = tg_res.get("message_id")
                    r["telegram_result"] = tg_res.get("message", "পাবলিশ সম্পন্ন")
                    r["telegram_timestamp"] = datetime.now().isoformat()
                    tg_ok = True
                    print(f"  [টেলিগ্রাম]: {tg_res.get('message')}")
                else:
                    print(f"  [টেলিগ্রাম ত্রুটি]: {tg_res.get('message')}")
            except Exception as e:
                print(f"  [টেলিগ্রাম ব্যর্থ]: {str(e)}")

        if fb_ok and tg_ok:
            success_count += 1
        else:
            fail_count += 1

        # Save state immediately to ensure zero data loss
        records[idx] = r
        save_audit_data(records)

        print("-" * 50)

        # Anti-spam delay between posts
        if i < batch_total and not args.dry_run:
            time.sleep(args.delay)

    print("\n" + "=" * 65)
    print(" ব্যাচ ব্রডকাস্ট ফলাফল সারসংক্ষেপ")
    print("=" * 65)
    print(f"সফলভাবে পোস্ট হয়েছে: {success_count}টি")
    if fail_count > 0:
        print(f"ব্যর্থ বা আংশিক সম্পন্ন: {fail_count}টি")

    # Count overall remaining
    remaining = sum(1 for rec in records if not rec.get("posted_facebook", False) or not rec.get("posted_telegram", False))
    print(f"সর্বমোট এখনও বাকি রয়েছে: {remaining}টি পোস্ট")


if __name__ == "__main__":
    main()
