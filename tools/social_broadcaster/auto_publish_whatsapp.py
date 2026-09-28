#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/social_broadcaster/auto_publish_whatsapp.py
-------------------------------------------------
HelpTrickBD 100% Autonomous WhatsApp Channel Auto-Publishing System.

Allows the AI Agent or Site Admin to publish educational updates directly
to the official HelpTrickBD WhatsApp Channel without manual intervention.

Features:
- 100% Autonomous: Automatically checks session, opens channel, pastes, waits for 16:9 preview, and sends.
- Safe Human Pacing: Anti-ban 25-second delay between posts.
- Rich Preview Guarantee: 4.5s wait ensures featured image preview loads.
- Resumable: Tracks published IDs in output_posts/whatsapp_broadcast_progress.json.
- Zero-Emoji Compliance: Follows Helptrickbd governance standard.

Usage:
    python tools/social_broadcaster/auto_publish_whatsapp.py --start-from WA-113 --limit 5
    python tools/social_broadcaster/auto_publish_whatsapp.py --limit 10
    python tools/social_broadcaster/auto_publish_whatsapp.py --all
    python tools/social_broadcaster/auto_publish_whatsapp.py --dry-run
"""

import os
import sys
import argparse

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.social_broadcaster.whatsapp_channel_bot import run_bot


def main():
    parser = argparse.ArgumentParser(
        description="HelpTrickBD 100% Autonomous WhatsApp Channel Auto-Publisher"
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=5,
        help="এই সেশনে সর্বোচ্চ কয়টি পোস্ট স্বয়ংক্রিয়ভাবে পাঠানো হবে (ডিফল্ট: ৫)"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="বাকি থাকা সব আনপোস্টেড আর্টিকেল একসাথে পাঠানো"
    )
    parser.add_argument(
        "--start-from",
        type=str,
        default=None,
        help="সুনির্দিষ্ট কোনো পোস্ট আইডি থেকে শুরু করা (যেমন: WA-113)"
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=25.0,
        help="পোস্টগুলোর মধ্যবর্তী নিরাপদ বিরতির সময় সেকেন্ডে (ডিফল্ট: ২৫)"
    )
    parser.add_argument(
        "--preview-wait",
        type=float,
        default=4.5,
        help="থাম্বনেইল রিচ প্রিভিউ লোড হতে অপেক্ষার সময় সেকেন্ডে (ডিফল্ট: ৪.৫)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="টেস্ট মোড — মেসেজ প্রিভিউ দেখাবে কিন্তু লাইভ পাঠাবে না"
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="ম্যানুয়াল মোড (টার্মিনাল থেকে প্রতিটি ধাপে নিশ্চিত করতে চাইলে)"
    )
    parser.add_argument(
        "--reset",
        action="store_true",
        help="হিস্ট্রি ও প্রগ্রেস রিসেট করা"
    )
    parser.add_argument(
        "--profile-dir",
        type=str,
        default=os.path.join(PROJECT_ROOT, ".whatsapp_web_profile"),
        help="ক্রোম সেশন প্রোফাইল পাথ"
    )

    args = parser.parse_args()

    # Default to auto mode unless user explicitly asked for interactive
    args.auto = not args.interactive

    print("=" * 72)
    print("  হেল্পট্রিকবিডি হোয়াটসঅ্যাপ চ্যানেল অটোনোমাস অটো-পাবলিশার")
    print("=" * 72)
    if args.auto:
        print("[*] মোড: জিরো-হ্যান্ডস অটোনোমাস অটো-পাইলট (কোনো কীবোর্ড প্রেস ছাড়াই)")
    else:
        print("[*] মোড: ম্যানুয়াল ইন্টারঅ্যাক্টিভ")

    run_bot(args)


if __name__ == "__main__":
    main()
