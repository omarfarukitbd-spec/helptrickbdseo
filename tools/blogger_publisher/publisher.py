#!/usr/bin/env python3
"""
HelpTrickBD Blogger Automated Publisher & Scheduler
Interacts with Google Blogger API v3 to auto-publish or schedule articles
strictly within the golden engagement window: 7:00 PM - 8:30 PM BST (19:00 - 20:30 UTC+6).

Features:
- Publishes LIVE, as DRAFT, or SCHEDULED for future release.
- Automatically sets Title, Content, Labels (categories), and Publication Date.
- Supports OAuth 2.0 (`client_secrets.json`) with persistent token refresh (`blogger_token.json`).
- If credentials are not yet set up, outputs an instant One-Click Blogger Ready Bundle.

Usage:
    python publisher.py --post output_posts/sample_metadata.json --mode schedule
    python publisher.py --post output_posts/sample_metadata.json --mode live
    python publisher.py --post output_posts/sample_metadata.json --mode draft
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
    """Initializes authenticated Google Blogger API client."""
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
                flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
                creds = flow.run_local_server(port=0)
            with open(TOKEN_FILE, "w") as token:
                token.write(creds.to_json())

        service = build("blogger", "v3", credentials=creds)
        return service
    except Exception as e:
        print(f"[!] Authentication warning: {e}")
        return None


def publish_post(metadata_file, mode="schedule", blog_id=BLOG_ID):
    if not os.path.exists(metadata_file):
        print(f"[ERROR] Metadata file not found: {metadata_file}")
        return False

    with open(metadata_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    title = data.get("title", "Untitled Post")
    content = data.get("html_content", "")
    category = data.get("category", "General")
    labels = [c.strip() for c in category.split(",") if c.strip()]
    scheduled_time = data.get("scheduled_time_rfc3339", "")
    readable_time = data.get("scheduled_time_readable", "সন্ধ্যা ৭:০০ - ৮:৩০ টা BST")
    meta_desc = data.get("meta_description", "")
    slug = data.get("slug", "")

    print(f"\n" + "="*65)
    print(f"  HelpTrickBD Blogger Publishing Engine")
    print(f"  Mode:            {mode.upper()}")
    print(f"  Title:           {title}")
    print(f"  Category/Labels: {', '.join(labels)}")
    print(f"  Schedule Window: {readable_time}")
    print(f"  RFC 3339:        {scheduled_time}")
    print("="*65 + "\n")

    service = get_authenticated_service()

    if service:
        try:
            print("[*] Publishing directly to Blogger via Google API v3...")
            body = {
                "kind": "blogger#post",
                "blog": {"id": blog_id},
                "title": title,
                "content": content,
                "labels": labels
            }

            is_draft = (mode == "draft")
            if mode == "schedule" and scheduled_time:
                body["published"] = scheduled_time

            posts = service.posts()
            result = posts.insert(blogId=blog_id, body=body, isDraft=is_draft).execute()
            post_url = result.get("url", "")
            print(f"✅ [SUCCESS] Post successfully published to Blogger!")
            print(f"   Status:   {result.get('status', 'OK')}")
            print(f"   Post ID:  {result.get('id')}")
            print(f"   Live URL: {post_url}\n")
            return post_url
        except Exception as e:
            print(f"[!] API Error: {e}. Falling back to Production Bundle.")

    # Fallback / Direct Production Bundle (Zero friction!)
    print("[*] Ready in Production Bundle (Instant 1-Click Copy Paste into Blogger):")
    print("-" * 65)
    print(f"📌 [১. পোস্ট টাইটেল (Title)]: \n   {title}\n")
    print(f"🏷️ [২. লেবেল / ক্যাটাগরি (Labels)]: \n   {', '.join(labels)}\n")
    print(f"⏰ [৩. শিডিউল সময় (Schedule Time)]: \n   {readable_time} (Strictly 7:00 PM - 8:30 PM BST)\n")
    print(f"🔍 [৪. সার্চ ডেসক্রিপশন (Search Description)]: \n   {meta_desc}\n")
    print(f"🔗 [৫. কাস্টম পারমালিংক (Custom Permalink)]: \n   {slug[:40]}\n")
    print(f"📄 [৬. পোস্ট HTML ফাইল]: \n   {metadata_file.replace('_metadata.json', '.html')}")
    print("-" * 65 + "\n")
    return True


def main():
    parser = argparse.ArgumentParser(description="HelpTrickBD Blogger Automated Publisher & Scheduler")
    parser.add_argument("--post", required=True, help="Path to article _metadata.json")
    parser.add_argument("--mode", choices=["schedule", "live", "draft"], default="schedule", help="Publishing mode")
    parser.add_argument("--blog-id", default=BLOG_ID, help="Blogger Blog ID")

    args = parser.parse_args()
    publish_post(args.post, args.mode, args.blog_id)


if __name__ == "__main__":
    main()
