#!/usr/bin/env python3
"""
Blogger 301 Custom Redirect Generator for HelpTrickBD (www.helptrickbd.com)
Converts 404 URL exports from Google Search Console into Blogger Custom Redirect format
to eliminate crawl budget destruction and heal site authority.

Usage:
    python generate_redirects.py --input gsc_404_urls.txt --default-to /
    python generate_redirects.py --input gsc_404_export.csv
"""

import argparse
import csv
import os
import re
from urllib.parse import urlparse


def clean_url_to_path(url_str):
    """Strips domain from URL, leaving relative path for Blogger."""
    url_str = url_str.strip()
    if not url_str:
        return None
    parsed = urlparse(url_str)
    path = parsed.path
    if not path.startswith("/"):
        path = "/" + path
    return path


def smart_target_category(path):
    """
    Intelligently determines target redirect based on keywords in the slug.
    Falls back to home page '/' if no topic matched.
    """
    path_lower = path.lower()
    
    if any(k in path_lower for k in ["political", "rastro", "sorkar", "sarbobhoumotto", "songsod"]):
        return "/search/label/Political%20Science"
    elif any(k in path_lower for k in ["economy", "budget", "inflation", "remittance", "shilpo"]):
        return "/search/label/Economics"
    elif any(k in path_lower for k in ["islam", "hadith", "quran", "nabi", "milad"]):
        return "/search/label/Islamic"
    elif any(k in path_lower for k in ["computer", "technology", "generations"]):
        return "/search/label/Technology"
    elif any(k in path_lower for k in ["history", "gandhi", "rammohan", "vidyasagar"]):
        return "/search/label/History"
    else:
        return "/"


def process_redirects(input_file, default_target="/", output_csv="blogger_redirects_output.csv"):
    if not os.path.exists(input_file):
        print(f"[ERROR] Input file not found: {input_file}")
        return

    redirects = []

    with open(input_file, "r", encoding="utf-8", errors="ignore") as f:
        # Check if CSV or plain text
        first_line = f.readline()
        f.seek(0)

        if "," in first_line:
            reader = csv.reader(f)
            for row in reader:
                if not row:
                    continue
                # Look for URL in columns
                for col in row:
                    if col.startswith("http") or col.startswith("/"):
                        path = clean_url_to_path(col)
                        if path and path != "/":
                            target = smart_target_category(path) if default_target == "auto" else default_target
                            redirects.append((path, target))
                        break
        else:
            for line in f:
                path = clean_url_to_path(line)
                if path and path != "/":
                    target = smart_target_category(path) if default_target == "auto" else default_target
                    redirects.append((path, target))

    # Remove duplicates
    unique_redirects = list(dict.fromkeys(redirects))

    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["From (Relative URL)", "To (Destination)", "Type", "Permanent (301)"])
        for from_p, to_p in unique_redirects:
            writer.writerow([from_p, to_p, "301 Redirect", "Yes"])

    print(f"\n{'='*60}")
    print(f"  Blogger 301 Redirect Generator Completed")
    print(f"  Total 404 URLs Processed: {len(unique_redirects)}")
    print(f"  Output saved to: {output_csv}")
    print(f"{'='*60}\n")
    print("How to apply in Blogger:")
    print("1. Go to Blogger Dashboard > Settings.")
    print("2. Scroll down to 'Errors and redirects' section.")
    print("3. Click on 'Custom redirects' > 'ADD'.")
    print("4. Paste 'From' and 'To' URLs, check 'Permanent' checkbox, and click Save.")
    print("   (This stops Google from reporting 404s and passes link equity!)\n")


def main():
    parser = argparse.ArgumentParser(description="Blogger 301 Custom Redirect Generator")
    parser.add_argument("--input", default="gsc_404_urls.txt", help="Path to txt or csv file containing 404 URLs")
    parser.add_argument("--default-to", default="auto", help="Default target URL ('auto' for smart category or '/' for home)")
    parser.add_argument("--output", default="blogger_redirects_output.csv", help="Path to output CSV")
    args = parser.parse_args()

    process_redirects(args.input, args.default_to, args.output)


if __name__ == "__main__":
    main()
