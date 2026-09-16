#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/indexer/pubsub_hub_pinger.py
-----------------------------------
Real-Time Google WebSub (PubSubHubbub) Hub Pinger for Helptrickbd.
Instantly pings Google's real-time feed hubs whenever a post is published or updated,
triggering immediate Googlebot feed ingest within seconds.

Hubs:
1. Google PubSubHubbub Hub: https://pubsubhubbub.appspot.com/publish
2. Superfeedr Hub: https://pubsubhubbub.superfeedr.com/publish
"""

import os
import sys
import requests
from datetime import datetime, timezone

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

HUBS = [
    "https://pubsubhubbub.appspot.com/publish",
    "https://pubsubhubbub.superfeedr.com/publish"
]

FEED_URLS = [
    "https://www.helptrickbd.com/feeds/posts/default",
    "https://www.helptrickbd.com/atom.xml?redirect=false&start-index=1&max-results=500",
    "https://www.helptrickbd.com/sitemap.xml"
]

HEADERS = {
    "User-Agent": "HelpTrickBD-RealtimePinger/2.0 (+https://www.helptrickbd.com)",
    "Content-Type": "application/x-www-form-urlencoded"
}

def ping_hub(hub_url: str, feed_url: str) -> bool:
    """Sends a standardized PubSubHubbub publish notification to the specified hub."""
    payload = {
        "hub.mode": "publish",
        "hub.url": feed_url
    }
    try:
        response = requests.post(hub_url, data=payload, headers=HEADERS, timeout=10)
        # HTTP 204 No Content is the official standard success code for PubSubHubbub
        if response.status_code in (200, 204):
            print(f"   [✔] Success (HTTP {response.status_code}): {feed_url} -> {hub_url.split('/')[2]}")
            return True
        else:
            print(f"   [!] Warning (HTTP {response.status_code}): {hub_url} returned: {response.text[:100]}")
            return False
    except Exception as e:
        print(f"   [✘] Connection Error for {hub_url}: {e}")
        return False

def ping_all_hubs():
    """Pings all designated Google and public WebSub hubs for all feeds."""
    print("=" * 70)
    print("⚡ HELPTRICKBD REAL-TIME GOOGLE WEBSUB (PUBSUBHUBBUB) HUB PINGER")
    print(f"   Timestamp: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print("=" * 70)

    total_pings = 0
    successful_pings = 0

    for feed in FEED_URLS:
        print(f"\n📡 Pinging Feed: {feed}")
        for hub in HUBS:
            total_pings += 1
            if ping_hub(hub, feed):
                successful_pings += 1

    print("\n" + "=" * 70)
    print(f"🎉 PING COMPLETE: {successful_pings}/{total_pings} Hub endpoints notified successfully!")
    print("   Google real-time feed reader has been triggered for instant ingest.")
    print("=" * 70)

if __name__ == "__main__":
    ping_all_hubs()
