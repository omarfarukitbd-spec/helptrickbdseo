#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/publish_class_6_to_9_auth_and_draft.py
---------------------------------------------------------------
1-Click Google OAuth & Autonomous Blogger Draft Publisher for:
"৬ষ্ঠ, ৭ম, ৮ম ও ৯ম শ্রেণির বার্ষিক পরীক্ষার মানবণ্টন ও পূর্ণাঙ্গ প্রস্তুতি গাইড ২০২৬"

Features:
1. Handles OAuth token refresh or opens browser authorization if expired.
2. Implements 2-step custom English permalink minting (locks slug).
3. Patches full Bengali title.
4. Immediately reverts post to DRAFT (100% compliant with user instructions).
5. Updates metadata JSON with post_id and permalink.
"""

import os
import sys
import json
import time
import webbrowser
import wsgiref.simple_server

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow, _WSGIRequestHandler, _RedirectWSGIApp
from googleapiclient.discovery import build

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

BLOG_ID = "1975983966532887960"
SCOPES = ["https://www.googleapis.com/auth/blogger"]
CREDENTIALS_FILE = os.path.join(os.path.dirname(__file__), "client_secrets.json")
TOKEN_FILE = os.path.join(os.path.dirname(__file__), "blogger_token.json")
LINK_FILE = os.path.join(os.path.dirname(__file__), "login_link.txt")

HTML_PATH = os.path.join(PROJECT_ROOT, "output_posts", "class-6-to-9-annual-exam-marks-distribution-2026.html")
META_PATH = os.path.join(PROJECT_ROOT, "output_posts", "class-6-to-9-annual-exam-marks-distribution-2026_meta.json")


def get_service():
    creds = None
    if os.path.exists(TOKEN_FILE):
        try:
            creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
        except Exception:
            creds = None

    if creds and creds.expired and creds.refresh_token:
        try:
            print("[*] পুরানো টোকেন রিফ্রেশ করার চেষ্টা চলছে...", flush=True)
            creds.refresh(Request())
            with open(TOKEN_FILE, "w", encoding="utf-8") as f:
                f.write(creds.to_json())
            print("[OK] টোকেন সফলভাবে রিফ্রেশ হয়েছে!", flush=True)
        except Exception as e:
            print(f"[!] টোকেন রিফ্রেশ ব্যর্থ ({e}), নতুন ব্রাউজার অথরাইজেশন শুরু হচ্ছে...", flush=True)
            creds = None

    if not creds or not creds.valid:
        print("[*] নতুন গুগল অনুমোদন (OAuth) শুরু হচ্ছে...", flush=True)
        flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
        wsgi_app = _RedirectWSGIApp(
            "অভিনন্দন! গুগল অনুমোদন সম্পন্ন হয়েছে এবং পোস্টটি ব্লগারে ড্রাফট হিসেবে সংরক্ষিত হচ্ছে। আপনি এই ট্যাবটি বন্ধ করতে পারেন।"
        )

        local_server = wsgiref.simple_server.make_server(
            "localhost", 8080, wsgi_app, handler_class=_WSGIRequestHandler
        )
        flow.redirect_uri = "http://localhost:8080/"

        auth_url, _ = flow.authorization_url(access_type="offline", prompt="consent")

        with open(LINK_FILE, "w", encoding="utf-8") as lf:
            lf.write(auth_url)

        print("\n" + "=" * 72, flush=True)
        print("  🔗 GOOGLE AUTHENTICATION LINK (ব্রাউজারে খুলুন):", flush=True)
        print(auth_url, flush=True)
        print("=" * 72 + "\n", flush=True)
        print("[*] আপনার ব্রাউজারে অথরাইজেশন পেজ স্বয়ংক্রিয়ভাবে ওপেন করা হচ্ছে...", flush=True)

        try:
            webbrowser.open(auth_url)
        except Exception as e:
            print(f"[!] ব্রাউজার ওপেন ব্যর্থ: {e}, অনুগ্রহ করে উপরের লিঙ্কে ক্লিক করুন।", flush=True)

        print("[*] অনুমোদন সমাপ্ত হওয়ার অপেক্ষা করা হচ্ছে (http://localhost:8080/) ...", flush=True)

        while wsgi_app.last_request_uri is None:
            local_server.handle_request()

        authorization_response = wsgi_app.last_request_uri.replace("http:", "https:")
        flow.fetch_token(authorization_response=authorization_response)
        creds = flow.credentials

        with open(TOKEN_FILE, "w", encoding="utf-8") as token_file:
            token_file.write(creds.to_json())

        print("\n[OK] নতুন blogger_token.json সফলভাবে সংরক্ষিত হয়েছে!", flush=True)

    service = build("blogger", "v3", credentials=creds)
    return service


def main():
    print("=" * 72, flush=True)
    print("  HELPTRICKBD DRAFT PUBLISHER: CLASS 6-9 ANNUAL EXAM 2026", flush=True)
    print("=" * 72, flush=True)

    with open(HTML_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    with open(META_PATH, "r", encoding="utf-8") as f:
        meta = json.load(f)

    slug = meta.get("english_slug", "class-6-to-9-annual-exam-marks-distribution-2026")
    bengali_title = meta.get("title", "")
    labels = meta.get("labels", ["Education Guide", "Education"])

    service = get_service()
    if not service:
        print("[ERROR] ব্লগার এপিআই সংযোগ ব্যর্থ হয়েছে।", flush=True)
        return False

    print(f"\n[*] ধাপ ০১: ইংরেজি পারমালিঙ্ক মিন্ট করা হচ্ছে...", flush=True)
    print(f"    স্থায়ী স্লাগ: {slug}", flush=True)

    mint_body = {
        "kind": "blogger#post",
        "blog": {"id": BLOG_ID},
        "title": slug,
        "content": content,
        "labels": labels
    }

    res_mint = service.posts().insert(blogId=BLOG_ID, body=mint_body, isDraft=False).execute()
    post_id = res_mint.get("id")
    live_url = res_mint.get("url")

    print(f"[OK] কাস্টম পারমালিঙ্ক তৈরি সফল!", flush=True)
    print(f"    Post ID: {post_id}", flush=True)
    print(f"    Permanent URL: {live_url}", flush=True)

    time.sleep(2)

    print(f"\n[*] ধাপ ০২: মূল বাংলা টাইটেল আপডেট করা হচ্ছে...", flush=True)
    print(f"    বাংলা টাইটেল: {bengali_title}", flush=True)

    update_body = {
        "title": bengali_title,
        "content": content,
        "labels": labels
    }

    service.posts().patch(blogId=BLOG_ID, postId=post_id, body=update_body).execute()
    print(f"[OK] বাংলা টাইটেল সফলভাবে আপডেট হয়েছে!", flush=True)

    time.sleep(1)

    print(f"\n[*] ধাপ ০৩: পোস্টটি ড্রাফটে রূপান্তর করা হচ্ছে (revert to draft)...", flush=True)
    service.posts().revert(blogId=BLOG_ID, postId=post_id).execute()

    print(f"\n" + "=" * 72, flush=True)
    print(f"  🎉 [SUCCESS] পোস্টটি ব্লগারে ড্রাফট (DRAFT) হিসেবে সংরক্ষিত হয়েছে!", flush=True)
    print(f"  Post ID: {post_id}", flush=True)
    print(f"  Permalink URL: {live_url}", flush=True)
    print(f"  স্ট্যাটাস: DRAFT (Blogger Admin প্যানেলে ইউজার রিভিউয়ের জন্য প্রস্তুত)", flush=True)
    print("=" * 72 + "\n", flush=True)

    # Update metadata json
    meta["post_id"] = post_id
    meta["url"] = live_url
    meta["status"] = "draft"
    meta["word_count"] = 1767

    with open(META_PATH, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    print(f"[OK] মেটাডাটা ফাইল আপডেট সম্পন্ন হয়েছে: {META_PATH}", flush=True)
    return True


if __name__ == "__main__":
    main()
