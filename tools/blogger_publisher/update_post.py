#!/usr/bin/env python3
"""
HelpTrickBD Automated Blogger Post Updater Engine
Finds existing posts on HelpTrickBD by URL slug or title and updates their
HTML content, title, and labels directly via Google Blogger API v3.

Usage:
    python update_post.py --file output_posts/revived_posts/history-of-bangladesh.html --slug "history-of-bangladesh"
"""

import argparse
import json
import os
import sys

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

BLOG_ID = "1975983966532887960"
SCOPES = ["https://www.googleapis.com/auth/blogger"]
CREDENTIALS_FILE = os.path.join(os.path.dirname(__file__), "client_secrets.json")
TOKEN_FILE = os.path.join(os.path.dirname(__file__), "blogger_token.json")


def get_authenticated_service():
    if not os.path.exists(CREDENTIALS_FILE) and not os.path.exists(TOKEN_FILE):
        return None
    try:
        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
        from googleapiclient.discovery import build

        creds = None
        if os.path.exists(TOKEN_FILE):
            creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
            
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                print("\n" + "="*70)
                print("  🌐 আপনার ব্রাউজারে একটি Google লগইন পেজ ওপেন হচ্ছে...")
                print("  👉 অনুগ্রহ করে 'arafatunnesa.feni@gmail.com' সিলেক্ট করে 'Continue' বা 'Allow' দিন।")
                print("  (এটি কেবল ১ বার করতে হবে, পরবর্তীতে সব অটোমেটিক হবে)")
                print("="*70 + "\n")
                flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
                creds = flow.run_local_server(port=0)
            with open(TOKEN_FILE, "w") as token:
                token.write(creds.to_json())

        return build("blogger", "v3", credentials=creds)
    except Exception as e:
        print(f"[!] Authentication Error: {e}")
        return None


def find_post_id_by_slug_or_title(service, slug, title=""):
    """Search for the post on Blogger to retrieve its unique postId."""
    print(f"[*] Searching Blogger for post matching slug '{slug}'...")
    try:
        posts_service = service.posts()
        request = posts_service.list(blogId=BLOG_ID, maxResults=100)
        while request:
            response = request.execute()
            for post in response.get("items", []):
                post_url = post.get("url", "")
                post_title = post.get("title", "")
                if slug in post_url or (title and title in post_title):
                    print(f"✅ Found matching post on Blogger!")
                    print(f"   Post ID: {post['id']}")
                    print(f"   URL:     {post_url}")
                    return post["id"], post
            request = posts_service.list_next(request, response)
        print(f"[!] Post with slug '{slug}' not found on Blogger.")
        return None, None
    except Exception as e:
        print(f"[!] Search Error: {e}")
        return None, None


def update_post_on_blogger(metadata_file_or_html, slug=None, post_id=None):
    service = get_authenticated_service()
    if not service:
        print("\n" + "="*70)
        print("  🔑 Blogger OAuth 2.0 Client Secret Needed")
        print("="*70)
        print("Blogger-এ সরাসরি পোস্ট আপডেট করতে `client_secrets.json` ফাইলটি প্রয়োজন।")
        print(f"ফাইলটি এই লোকেশনে রাখুন:\n  {CREDENTIALS_FILE}\n")
        print("গুগল ক্লাউড কনসোল থেকে Credentials > OAuth client ID (Desktop app) ডাউনলোড করে এখানে সেভ করুন।")
        print("="*70 + "\n")
        return False

    # Load content
    base = metadata_file_or_html.replace(".html", "").replace("_metadata.json", "")
    html_file = f"{base}.html"
    meta_file = f"{base}_metadata.json"

    title = "Updated Post"
    content = ""
    labels = []

    if os.path.exists(meta_file):
        with open(meta_file, "r", encoding="utf-8") as f:
            mdata = json.load(f)
            title = mdata.get("title", title)
            content = mdata.get("html_content", "")
            cat = mdata.get("category", "")
            labels = [c.strip() for c in cat.split(",") if c.strip()]
    if not content and os.path.exists(html_file):
        with open(html_file, "r", encoding="utf-8") as f:
            content = f.read()
        # Auto-extract <title> from HTML if not set via metadata
        if title == "Updated Post":
            import re
            m = re.search(r"<title>(.*?)</title>", content, re.IGNORECASE | re.DOTALL)
            if m:
                title = m.group(1).strip()
                print(f"[*] Auto-extracted title from HTML: {title}")

    if not post_id:
        post_id, original_post = find_post_id_by_slug_or_title(service, slug, title)
    else:
        try:
            original_post = service.posts().get(blogId=BLOG_ID, postId=post_id).execute()
        except Exception:
            original_post = None

    if not post_id:
        print(f"[ERROR] Could not find post on Blogger with slug: {slug}")
        return False

    # If title is still default placeholder, preserve original post title
    if title == "Updated Post" and original_post and original_post.get("title"):
        title = original_post.get("title")

    print(f"[*] Updating Post ID {post_id} on Blogger...")
    try:
        body = {
            "title": title,
            "content": content
        }
        if labels:
            body["labels"] = labels

        updated = service.posts().patch(blogId=BLOG_ID, postId=post_id, body=body).execute()
        print("\n" + "="*70)
        print("🎉 [SUCCESS] পোস্টটি সরাসরি ব্লগারে সফলভাবে আপডেট করা হয়েছে!")
        print(f"  Title:     {updated.get('title')}")
        print(f"  Live URL:  {updated.get('url')}")
        print(f"  Updated:   {updated.get('updated')}")
        print("="*70 + "\n")
        return True
    except Exception as e:
        print(f"[!] Update Error: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="HelpTrickBD Automated Blogger Post Updater")
    parser.add_argument("--file", required=True, help="Path to updated HTML or metadata JSON")
    parser.add_argument("--slug", required=False, default=None, help="Slug of the post (e.g. 'history-of-bangladesh')")
    parser.add_argument("--post_id", required=False, default=None, help="Direct Blogger Post ID")

    args = parser.parse_args()
    update_post_on_blogger(args.file, args.slug, post_id=args.post_id)


if __name__ == "__main__":
    main()
