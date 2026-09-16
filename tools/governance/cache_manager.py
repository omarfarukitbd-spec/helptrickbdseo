#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/governance/cache_manager.py
---------------------------------
Automated CDN Cache Invalidation and Image Purge Engine for HelpTrickBD.

Solves the two caching challenges:
1. jsDelivr Edge Cache Invalidation: Automatically hits the jsDelivr Purge API
   to instantly clear CDN edge cache across Cloudflare and Fastly worldwide.
2. Google Blogger Image Proxy Invalidation: Explains and generates cache-busting
   versioned URLs (?v=YYYYMMDD) so Google's 'blogger_img_proxy' and client browsers
   never serve stale, outdated images.
"""

import sys
import io
import json
import urllib.request
import urllib.error

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

REPO_USER = "omarfarukitbd-spec"
REPO_NAME = "helptrickbdseo"
BRANCH = "main"

def purge_jsdelivr_file(relative_path: str):
    """
    Purges a specific file from jsDelivr CDN edge cache.
    relative_path example: 'assets/images/posts/caretaker-government-free-fair-election-banner.webp'
    """
    clean_path = relative_path.lstrip("/").replace("\\", "/")
    purge_url = f"https://purge.jsdelivr.net/gh/{REPO_USER}/{REPO_NAME}@{BRANCH}/{clean_path}"
    
    print(f"[*] Requesting Purge: {purge_url}")
    try:
        req = urllib.request.Request(purge_url, headers={"User-Agent": "HelpTrickBD-CacheManager/1.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            status = data.get("status", "unknown")
            providers = data.get("paths", {}).get(f"/gh/{REPO_USER}/{REPO_NAME}@{BRANCH}/{clean_path}", {}).get("providers", {})
            print(f"  [✔] Purge Status: {status.upper()} | Providers: {providers}")
            return True
    except urllib.error.HTTPError as e:
        print(f"  [!] HTTP Error {e.code}: {e.read().decode('utf-8', errors='ignore')}")
        return False
    except Exception as e:
        print(f"  [!] Purge Error: {e}")
        return False

def get_cache_busted_url(cdn_url: str, version_tag: str) -> str:
    """
    Appends a cache-busting query parameter so Google's image proxy
    and browser caches are forced to fetch the new version immediately.
    """
    sep = "&" if "?" in cdn_url else "?"
    return f"{cdn_url}{sep}v={version_tag}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python tools/governance/cache_manager.py <RELATIVE_PATH_OR_FILENAME>")
        print("Example: python tools/governance/cache_manager.py assets/images/posts/caretaker-government-free-fair-election-banner.webp")
        sys.exit(1)
        
    target = sys.argv[1]
    if not target.startswith("assets/"):
        target = f"assets/images/posts/{target}"
    purge_jsdelivr_file(target)
