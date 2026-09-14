#!/usr/bin/env python3
"""
Google Indexing API Automation Tool for HelpTrickBD (www.helptrickbd.com)
Directly notifies Googlebot to crawl and index updated or new pages within 24-48 hours.

Usage:
    python index_now.py --url https://www.helptrickbd.com/2026/01/sample-post.html
    python index_now.py --file urls.txt
    python index_now.py --sitemap https://www.helptrickbd.com/sitemap.xml
    python index_now.py --url https://www.helptrickbd.com/old-post.html --type URL_DELETED
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime
import xml.etree.ElementTree as ET

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

try:
    import requests
    from oauth2client.service_account import ServiceAccountCredentials
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
except ImportError:
    print("\n[!] Missing required libraries. Please install them first:")
    print("    pip install -r requirements.txt\n")
    sys.exit(1)

SCOPES = ["https://www.googleapis.com/auth/indexing"]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
DEFAULT_SERVICE_ACCOUNT_FILE = "service_account.json"
HISTORY_LOG_FILE = "indexing_history.log"


def get_authenticated_service(credentials_path=DEFAULT_SERVICE_ACCOUNT_FILE):
    """Authenticate with Google Cloud using the Service Account JSON file."""
    # Look in current directory, script directory, and tools/indexer
    candidate_paths = [
        credentials_path,
        os.path.join(os.path.dirname(__file__), credentials_path),
        os.path.join("tools", "indexer", credentials_path),
        os.path.join(os.path.dirname(__file__), "service_account.json")
    ]

    actual_path = None
    for p in candidate_paths:
        if p and os.path.exists(p):
            actual_path = p
            break

    if not actual_path:
        print(f"\n[ERROR] Service account file not found in candidates: {candidate_paths}")
        print("Please follow the setup instructions in README.md to place your service_account.json.\n")
        return None

    try:
        credentials = ServiceAccountCredentials.from_json_keyfile_name(actual_path, scopes=SCOPES)
        return credentials
    except Exception as e:
        print(f"[ERROR] Failed to load credentials from {actual_path}: {e}")
        return None


def submit_url(service, url, action_type="URL_UPDATED"):
    """
    Submits a single URL notification to Google Indexing API using googleapiclient.
    action_type: 'URL_UPDATED' or 'URL_DELETED'
    """
    body = {
        "url": url.strip(),
        "type": action_type
    }

    try:
        response = service.urlNotifications().publish(body=body).execute()
        
        notify_time = response.get("urlNotificationMetadata", {}).get("latestUpdate", {}).get("notifyTime", "N/A")
        log_entry = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{action_type}] Status: 200 | URL: {url} | Recorded: {notify_time}\n"
        with open(HISTORY_LOG_FILE, "a", encoding="utf-8") as f:
            f.write(log_entry)

        print(f" [SUCCESS] {action_type} -> {url} (Recorded: {notify_time})")
        return True

    except HttpError as e:
        status_code = e.resp.status if hasattr(e, 'resp') else "Error"
        error_details = str(e)
        log_entry = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{action_type}] Status: {status_code} | URL: {url} | Error: {error_details}\n"
        with open(HISTORY_LOG_FILE, "a", encoding="utf-8") as f:
            f.write(log_entry)

        print(f" [FAILED ({status_code})] {url} -> {error_details}")
        return False
    except Exception as e:
        print(f" [EXCEPTION] {url} -> {e}")
        return False


def fetch_urls_from_sitemap(sitemap_url):
    """Downloads XML sitemap and extracts all <loc> URLs."""
    print(f"[*] Fetching sitemap from: {sitemap_url} ...")
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        res = requests.get(sitemap_url, headers=headers, timeout=15)
        res.raise_for_status()

        root = ET.fromstring(res.content)
        # Handle default namespace
        namespace = ""
        if root.tag.startswith("{"):
            namespace = root.tag.split("}")[0] + "}"

        urls = []
        for elem in root.findall(f".//{namespace}loc"):
            if elem.text and elem.text.strip():
                urls.append(elem.text.strip())

        print(f"[*] Found {len(urls)} URLs in sitemap.")
        return urls
    except Exception as e:
        print(f"[!] Failed to fetch/parse sitemap: {e}")
        return []


def main():
    parser = argparse.ArgumentParser(description="Google Indexing API Automator for HelpTrickBD")
    parser.add_argument("--url", help="Single URL to submit for indexing")
    parser.add_argument("--file", help="File containing list of URLs (one per line)")
    parser.add_argument("--sitemap", help="URL of the XML sitemap to extract URLs from (e.g. https://www.helptrickbd.com/sitemap.xml)")
    parser.add_argument("--type", choices=["URL_UPDATED", "URL_DELETED"], default="URL_UPDATED",
                        help="Action type: URL_UPDATED (default) or URL_DELETED")
    parser.add_argument("--credentials", default=DEFAULT_SERVICE_ACCOUNT_FILE,
                        help="Path to service_account.json credentials file")
    parser.add_argument("--delay", type=float, default=0.5,
                        help="Delay in seconds between batch requests (default: 0.5s)")

    args = parser.parse_args()

    urls_to_process = []

    if args.url:
        urls_to_process.append(args.url.strip())
    elif args.file:
        if not os.path.exists(args.file):
            print(f"[ERROR] URL file not found: {args.file}")
            sys.exit(1)
        with open(args.file, "r", encoding="utf-8") as f:
            urls_to_process = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    elif args.sitemap:
        urls_to_process = fetch_urls_from_sitemap(args.sitemap)
    else:
        # Default prompt if no args provided
        default_file = "urls.txt"
        if os.path.exists(default_file):
            with open(default_file, "r", encoding="utf-8") as f:
                urls_to_process = [line.strip() for line in f if line.strip() and not line.startswith("#")]
            print(f"[*] No specific target provided. Loaded {len(urls_to_process)} URLs from {default_file}.")
        else:
            parser.print_help()
            sys.exit(0)

    if not urls_to_process:
        print("[!] No URLs found to submit.")
        sys.exit(0)

    print(f"\n{'='*60}")
    print(f"  HelpTrickBD - Google Indexing API Batch Submitter")
    print(f"  Total URLs to process: {len(urls_to_process)}")
    print(f"  Action Type: {args.type}")
    print(f"  Credentials: {args.credentials}")
    print(f"{'='*60}\n")

    credentials = get_authenticated_service(args.credentials)
    if not credentials:
        sys.exit(1)

    try:
        service = build("indexing", "v3", credentials=credentials)
    except Exception as e:
        print(f"[ERROR] Failed to build indexing service: {e}")
        sys.exit(1)

    successful = 0
    failed = 0

    for idx, url in enumerate(urls_to_process, 1):
        print(f"[{idx}/{len(urls_to_process)}] Processing: {url}")
        success = submit_url(service, url, action_type=args.type)
        if success:
            successful += 1
        else:
            failed += 1
        time.sleep(args.delay)

    print(f"\n{'-'*60}")
    print(f"Indexing Batch Completed!")
    print(f"  Successful: {successful}")
    print(f"  Failed:     {failed}")
    print(f"  Log file:   {HISTORY_LOG_FILE}")
    print(f"{'-'*60}\n")


if __name__ == "__main__":
    main()
