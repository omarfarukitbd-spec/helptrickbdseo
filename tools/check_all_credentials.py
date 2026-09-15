#!/usr/bin/env python3
"""
HelpTrickBD All-in-One Credentials & API Health Checker
Verifies Blogger API v3 and Google Indexing API connections in 1 second.

Usage:
    python tools/check_all_credentials.py
"""

import os
import sys

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(PROJECT_ROOT, "tools", "blogger_publisher"))
sys.path.append(os.path.join(PROJECT_ROOT, "tools", "indexer"))

def check_blogger():
    print("\n" + "="*60)
    print(" 1. Blogger API v3 Authentication Check")
    print("="*60)
    try:
        from update_post import get_authenticated_service, BLOG_ID
        service = get_authenticated_service()
        if not service:
            print(" [X] FAILED: Blogger credentials or token not found.")
            print("     Required: tools/blogger_publisher/client_secrets.json")
            print("     Required: tools/blogger_publisher/blogger_token.json")
            return False
        
        blog = service.blogs().get(blogId=BLOG_ID).execute()
        print(" [OK] Blogger API Connected Successfully!")
        print(f"      Blog Title: {blog.get('name')}")
        print(f"      Blog URL:   {blog.get('url')}")
        print(f"      Total Posts: {blog.get('posts', {}).get('totalItems')}")
        return True
    except Exception as e:
        print(f" [X] Blogger Error: {e}")
        return False

def check_indexing():
    print("\n" + "="*60)
    print(" 2. Google Indexing API Service Account Check")
    print("="*60)
    try:
        from index_now import get_authenticated_service
        service = get_authenticated_service("service_account.json")
        if not service:
            print(" [X] FAILED: service_account.json not found in root or tools/indexer/")
            return False
        print(" [OK] Google Indexing API Authenticated Successfully!")
        print("      Ready to submit URLs to Googlebot.")
        return True
    except Exception as e:
        print(f" [X] Indexing API Error: {e}")
        return False

def main():
    print("\n" + "#"*60)
    print("  HelpTrickBD Environment & Credentials Health Check")
    print("#"*60)

    blogger_ok = check_blogger()
    indexing_ok = check_indexing()

    print("\n" + "="*60)
    print(" SUMMARY REPORT")
    print("="*60)
    print(f"  Blogger API:        {'[READY]' if blogger_ok else '[FAILED]'}")
    print(f"  Google Indexing:    {'[READY]' if indexing_ok else '[FAILED]'}")
    
    if blogger_ok and indexing_ok:
        print("\n ALL SYSTEMS GO! আপনার পিসি ব্লগারে লাইভ পাবলিশ ও ইনডেক্স করার জন্য ১০০% প্রস্তুত!")
    else:
        print("\n [!] অনুগ্রহ করে উপরের ত্রুটিগুলো চেক করে মিসিং ফাইলগুলো পেস্ট করুন।")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
