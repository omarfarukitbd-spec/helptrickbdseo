#!/usr/bin/env python3
"""
tools/social_broadcaster/batch_broadcaster.py
HelpTrickBD Batch Social Broadcaster for Facebook & Telegram.

Fetches the latest published posts from Blogger API v3 and broadcasts them
sequentially to Facebook Page and Telegram Channel with rate-limit protection.
Strictly zero-emoji compliant.
"""

import os
import sys
import time
import json
import argparse
from typing import List, Dict, Any, Optional
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
from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID

CONFIG_FILE = os.path.join(MODULE_DIR, "social_credentials.json")


def load_config() -> Dict[str, Any]:
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {}


def extract_hero_image(html_content: str, post_images: Optional[List[Dict[str, Any]]] = None) -> Optional[str]:
    if post_images and len(post_images) > 0:
        return post_images[0].get("url")
    if not html_content:
        return None
    soup = BeautifulSoup(html_content, "html.parser")
    img = soup.find("img")
    if img and img.get("src"):
        return img["src"]
    return None


def fetch_latest_posts(limit: int = 20) -> List[Dict[str, Any]]:
    service = get_authenticated_service()
    if not service:
        raise RuntimeError("ব্লগার সার্ভিস অথেনটিকেশন ব্যর্থ হয়েছে। client_secrets.json বা blogger_token.json পরীক্ষা করুন।")
    
    posts_resp = service.posts().list(
        blogId=BLOG_ID,
        status="LIVE",
        maxResults=limit,
        fetchImages=True
    ).execute()
    
    return posts_resp.get("items", [])


def main():
    parser = argparse.ArgumentParser(description="HelpTrickBD Batch Social Broadcaster")
    parser.add_argument("--limit", type=int, default=20, help="কয়টি সাম্প্রতিক পোস্ট পাবলিশ করা হবে (ডিফল্ট: ২০)")
    parser.add_argument("--delay", type=int, default=15, help="প্রতিটি পোস্টের মধ্যবর্তী বিরতি সেকেন্ডে (ডিফল্ট: ১৫)")
    parser.add_argument("--dry-run", action="store_true", help="শুধুমাত্র প্রিভিউ দেখাবে, লাইভ পাঠাবে না")
    parser.add_argument("--reverse", action="store_true", help="পুরনো থেকে নতুনের ক্রমানুসারে পাবলিশ করবে (Chronological order)")
    parser.add_argument("--single-index", type=int, default=None, help="নির্দিষ্ট একটি পোস্ট পাবলিশ করতে (১-২০)")
    parser.add_argument("--start-index", type=int, default=1, help="শুরুর পোস্ট ইনডেক্স (১-ভিত্তিক)")
    parser.add_argument("--end-index", type=int, default=None, help="শেষ পোস্ট ইনডেক্স (১-ভিত্তিক)")
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

    print("=" * 65)
    print(" হেল্পট্রিকবিডি ব্যাচ সোশ্যাল ব্রডকাস্টার (Facebook & Telegram)")
    print("=" * 65)
    print(f"ব্লগার থেকে সাম্প্রতিক {args.limit}টি লাইভ পোস্ট সংগ্রহ করা হচ্ছে...\n")

    posts = fetch_latest_posts(limit=args.limit)
    if not posts:
        print("কোনো লাইভ পোস্ট পাওয়া যায়নি।")
        return

    if args.single_index is not None:
        idx = args.single_index - 1
        if 0 <= idx < len(posts):
            posts = [posts[idx]]
        else:
            print(f"ভুল ইনডেক্স দেওয়া হয়েছে। ১ থেকে {len(posts)} এর মধ্যে হতে হবে।")
            return
    else:
        start_idx = max(0, args.start_index - 1)
        end_idx = args.end_index if args.end_index is not None else len(posts)
        posts = posts[start_idx:end_idx]

    # If reverse is requested, publish from oldest to newest
    if args.reverse:
        posts = list(reversed(posts))

    generator = SocialCopyGenerator()

    total = len(posts)
    print(f"মোট {total}টি পোস্ট প্রসেস করার জন্য প্রস্তুত করা হয়েছে।\n")

    for i, post in enumerate(posts, 1):
        title = post.get("title", "")
        post_url = post.get("url", "")
        html_content = post.get("content", "")
        labels = post.get("labels", [])
        post_images = post.get("images", [])
        hero_image = extract_hero_image(html_content, post_images)

        generated = generator.generate_all(
            title=title,
            post_url=post_url,
            html_content=html_content,
            labels=labels,
            hero_image=hero_image
        )

        print(f"[{i}/{total}] প্রসেস করা হচ্ছে: {title}")
        print(f"লিংক: {post_url}")
        print(f"ছবি: {hero_image or 'পাওয়া যায়নি'}")

        if args.dry_run:
            print(f"ফেসবুক টেক্সট দৈর্ঘ্য: {len(generated['facebook'])} অক্ষর")
            print(f"টেলিগ্রাম টেক্সট দৈর্ঘ্য: {len(generated['telegram'])} অক্ষর")
            print("-" * 50)
            continue

        # 1. Facebook Broadcast (Default: Clickable 16:9 Link Preview Card via Make Verified Gateway)
        if fb_cfg.get("enabled", True) and fb_pub.is_configured():
            fb_res = fb_pub.publish_post(
                message=generated["facebook"],
                link=post_url,
                image_url=hero_image,
                post_type="link",
                title=title
            )
            print(f"  [ফেসবুক]: {fb_res['message']}")
        else:
            print("  [ফেসবুক]: নিষ্ক্রিয় বা কনফিগার করা নেই।")

        # 2. Telegram Broadcast (With interactive inline button & generous spacing)
        if tg_cfg.get("enabled", True) and tg_pub.is_configured():
            tg_res = tg_pub.publish_post(
                text=generated["telegram"],
                image_url=hero_image,
                button_text=generated.get("button_text"),
                button_url=post_url
            )
            print(f"  [টেলিগ্রাম]: {tg_res['message']}")
        else:
            print("  [টেলিগ্রাম]: নিষ্ক্রিয় বা কনফিগার করা নেই।")

        print("-" * 50)

        # Delay between posts to protect page from spam rate limit
        if i < total and not args.dry_run:
            print(f"অ্যান্টি-স্প্যাম সেফটি বিরতি: {args.delay} সেকেন্ড অপেক্ষা করা হচ্ছে...\n")
            time.sleep(args.delay)

    print("\nব্রডকাস্ট প্রক্রিয়া সম্পূর্ণ হয়েছে।")


if __name__ == "__main__":
    main()
