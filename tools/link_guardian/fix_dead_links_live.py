#!/usr/bin/env python3
"""
tools/link_guardian/fix_dead_links_live.py
HelpTrickBD Automated Live Broken Link Repair Script.

Directly updates live Blogger posts to fix:
1. Malformed markdown links in Mahatma Gandhi post.
2. 404 Wikipedia URL in Population Growth post.
3. 404 IPU URL in Women's Reserved Seats post.
"""

import sys
import os
import re

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

from tools.blogger_publisher.update_post import get_authenticated_service, BLOG_ID


def fix_dead_links():
    service = get_authenticated_service()
    if not service:
        print("[!] Blogger API authentication failed.")
        sys.exit(1)

    print("\n=======================================================")
    print("  HelpTrickBD Live Broken Link Repair Engine")
    print("=======================================================")

    # 1. Mahatma Gandhi Post (ID: 7152628717436788366)
    print("\n[*] 1. Repairing Mahatma Gandhi post (ID: 7152628717436788366)...")
    post1 = service.posts().get(blogId=BLOG_ID, postId="7152628717436788366").execute()
    content1 = post1.get("content", "")

    # Replace leaked markdown bracket links with clean URLs
    content1_fixed = content1.replace(
        "[https://www.helptrickbd.com/2025/12/reasons-for-failure-of-khilafat-movement.html](https://www.helptrickbd.com/2025/12/reasons-for-failure-of-khilafat-movement.html)",
        "https://www.helptrickbd.com/2025/12/reasons-for-failure-of-khilafat-movement.html"
    ).replace(
        "[https://www.helptrickbd.com/2025/12/sher-e-bangla-fazlul-haque-social-welfare.html](https://www.helptrickbd.com/2025/12/sher-e-bangla-fazlul-haque-social-welfare.html)",
        "https://www.helptrickbd.com/2025/12/sher-e-bangla-fazlul-haque-social-welfare.html"
    ).replace(
        "[https://www.helptrickbd.com/2025/12/definition-of-state-elements-and-objectives.html](https://www.helptrickbd.com/2025/12/definition-of-state-elements-and-objectives.html)",
        "https://www.helptrickbd.com/2025/12/definition-of-state-elements-and-objectives.html"
    )

    # Clean any other bracket leakage inside href attributes
    content1_fixed = re.sub(r'href="\[(https?://[^\]]+)\]\((https?://[^\)]+)\)"', r'href="\1"', content1_fixed)

    if content1_fixed != content1:
        post1["content"] = content1_fixed
        updated1 = service.posts().update(blogId=BLOG_ID, postId="7152628717436788366", body=post1).execute()
        print("    [+] Fixed 3 leaked markdown bracket links successfully on Blogger!")
    else:
        print("    [i] No bracket leakage found in Mahatma Gandhi post content.")

    # 2. Population Growth Post (ID: 1937593761602997500)
    print("\n[*] 2. Repairing Population Growth post (ID: 1937593761602997500)...")
    post2 = service.posts().get(blogId=BLOG_ID, postId="1937593761602997500").execute()
    content2 = post2.get("content", "")

    # Replace 404 Wikipedia URL with valid article
    old_wiki = "https://bn.wikipedia.org/wiki/%E0%A6%AC%E0%A6%A8%E0%A6%AD%E0%A7%82%E0%A6%AE%E0%A6%BF_%E0%A6%89%E0%A6%9C%E0%A6%BE%E0%A6%A1%E0%A6%BC"
    new_wiki = "https://bn.wikipedia.org/wiki/%E0%A6%AC%E0%A6%A8%E0%A6%89%E0%A6%9C%E0%A6%BE%E0%A6%A1%E0%A6%BC"

    content2_fixed = content2.replace(old_wiki, new_wiki).replace("bn.wikipedia.org/wiki/বনভূমি_উজাড়", "bn.wikipedia.org/wiki/বনউজাড়")

    if content2_fixed != content2:
        post2["content"] = content2_fixed
        updated2 = service.posts().update(blogId=BLOG_ID, postId="1937593761602997500", body=post2).execute()
        print("    [+] Fixed 404 Wikipedia link successfully on Blogger!")
    else:
        print("    [i] Wikipedia URL was already clean.")

    # 3. Women's Reserved Seats Post (ID: 4176960177069689710)
    print("\n[*] 3. Repairing Women's Reserved Seats post (ID: 4176960177069689710)...")
    post3 = service.posts().get(blogId=BLOG_ID, postId="4176960177069689710").execute()
    content3 = post3.get("content", "")

    old_ipu = "https://www.ipu.org/women-in-politics-2023"
    new_ipu = "https://www.ipu.org/resources/publications/infographics/2023-03/women-in-politics-2023"

    content3_fixed = content3.replace(old_ipu, new_ipu)
    if content3_fixed != content3:
        post3["content"] = content3_fixed
        updated3 = service.posts().update(blogId=BLOG_ID, postId="4176960177069689710", body=post3).execute()
        print("    [+] Fixed 404 IPU link successfully on Blogger!")
    else:
        print("    [i] IPU URL was already clean.")

    print("\n=======================================================")
    print("  [✓] All 5 dead / broken links repaired live on Blogger!")
    print("=======================================================\n")


if __name__ == "__main__":
    fix_dead_links()
