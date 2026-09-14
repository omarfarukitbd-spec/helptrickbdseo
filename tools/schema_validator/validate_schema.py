#!/usr/bin/env python3
"""
HelpTrickBD Schema Markup & Structured Data Validator
Validates Google Article & BlogPosting JSON-LD schemas according to Schema.org standards.

Usage:
    python validate_schema.py --url https://www.helptrickbd.com/2026/01/sarbobhoumotto-ki-songga-boishisto-o-prokarved.html
"""

import argparse
import json
import sys

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("[!] Missing requests/bs4. Run: pip install requests beautifulsoup4")
    sys.exit(1)


REQUIRED_ARTICLE_FIELDS = [
    ("headline", "Article title / headline"),
    ("image", "Featured thumbnail image URL"),
    ("datePublished", "Original publication date (ISO 8601)"),
    ("dateModified", "Last updated date (ISO 8601)"),
    ("author", "Author information (Person entity)"),
    ("publisher", "Publisher organization entity with logo"),
    ("mainEntityOfPage", "Canonical URL of the article")
]


def validate_schema(url):
    print(f"[*] Validating Schema on: {url} ...\n")
    try:
        res = requests.get(url, timeout=12)
        soup = BeautifulSoup(res.text, "html.parser")

        schemas_found = []
        for script in soup.find_all("script", type="application/ld+json"):
            try:
                data = json.loads(script.string)
                schemas_found.append(data)
            except Exception:
                continue

        if not schemas_found:
            print("❌ [ERROR] Zero JSON-LD schemas found on this page!")
            return

        print(f"[*] Found {len(schemas_found)} JSON-LD structured data block(s).\n")

        # Flatten @graph if present
        all_entities = []
        for s in schemas_found:
            if "@graph" in s and isinstance(s["@graph"], list):
                all_entities.extend(s["@graph"])
            else:
                all_entities.append(s)

        article_schema = None
        for item in all_entities:
            t = item.get("@type", "")
            if t in ["Article", "BlogPosting", "NewsArticle"]:
                article_schema = item
                break

        if not article_schema:
            print("⚠️ [WARNING] No 'Article' or 'BlogPosting' schema found on this post.")
            types_found = [item.get('@type', 'Unknown') for item in all_entities]
            print(f"    Entities found: {types_found}")
            print("\n👉 ACTION REQUIRED: Inject 'templates/technical_seo/theme_schema_and_meta.xml' into your Blogger Theme!")
            return

        print(f"✅ Found Schema Type: '{article_schema.get('@type')}'")
        print("-" * 55)

        passed = 0
        for field, desc in REQUIRED_ARTICLE_FIELDS:
            if field in article_schema and article_schema[field]:
                print(f"✅ [{field}]: {desc} (Present)")
                passed += 1
            else:
                print(f"❌ [{field}]: {desc} (MISSING)")

        print("-" * 55)
        print(f"Schema Health: {passed}/{len(REQUIRED_ARTICLE_FIELDS)} required fields present.")

    except Exception as e:
        print(f"[!] Error validating schema: {e}")


def main():
    parser = argparse.ArgumentParser(description="HelpTrickBD Schema Validator")
    parser.add_argument("--url", default="https://www.helptrickbd.com/2026/01/sarbobhoumotto-ki-songga-boishisto-o-prokarved.html", help="URL to test")
    args = parser.parse_args()

    validate_schema(args.url)


if __name__ == "__main__":
    main()
