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


def validate_schema_from_soup(soup, source_name):
    print(f"[*] Validating Schema on: {source_name} ...\n")
    schemas_found = []
    for script in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(script.string)
            schemas_found.append(data)
        except Exception:
            continue

    if not schemas_found:
        print("❌ [ERROR] Zero JSON-LD schemas found!")
        return

    print(f"[*] Found {len(schemas_found)} JSON-LD structured data block(s).\n")

    # Flatten @graph if present
    all_entities = []
    for s in schemas_found:
        if "@graph" in s and isinstance(s["@graph"], list):
            all_entities.extend(s["@graph"])
        else:
            all_entities.append(s)

    for item in all_entities:
        t = item.get("@type", "")
        if t in ["Article", "BlogPosting", "NewsArticle"]:
            print(f"✅ Found Schema Type: '{t}'")
            print("-" * 55)
            passed = 0
            for field, desc in REQUIRED_ARTICLE_FIELDS:
                if field in item and item[field]:
                    print(f"✅ [{field}]: {desc} (Present)")
                    passed += 1
                else:
                    print(f"❌ [{field}]: {desc} (MISSING)")
            print("-" * 55)
            print(f"Article Schema Health: {passed}/{len(REQUIRED_ARTICLE_FIELDS)} required fields present.\n")

        elif t == "FAQPage":
            print(f"✅ Found Schema Type: 'FAQPage' (Rich Results Enabled)")
            print("-" * 55)
            main_entity = item.get("mainEntity", [])
            print(f"✅ Question Count: {len(main_entity)} FAQs configured.")
            for i, q in enumerate(main_entity, 1):
                q_name = q.get('name', 'Untitled')
                a_text = q.get('acceptedAnswer', {}).get('text', '')[:45]
                print(f"   Q{i}: {q_name}")
                print(f"   A{i}: {a_text}...")
            print("-" * 55 + "\n")


def validate_schema(url=None, file_path=None):
    try:
        if file_path:
            with open(file_path, "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f.read(), "html.parser")
            validate_schema_from_soup(soup, file_path)
        elif url:
            res = requests.get(url, timeout=12)
            soup = BeautifulSoup(res.text, "html.parser")
            validate_schema_from_soup(soup, url)
    except Exception as e:
        print(f"[!] Error validating schema: {e}")


def main():
    parser = argparse.ArgumentParser(description="HelpTrickBD Schema Validator")
    parser.add_argument("--url", help="URL to test")
    parser.add_argument("--file", help="Local HTML file to test")
    args = parser.parse_args()

    if args.file:
        validate_schema(file_path=args.file)
    elif args.url:
        validate_schema(url=args.url)
    else:
        validate_schema(url="https://www.helptrickbd.com/2026/01/sarbobhoumotto-ki-songga-boishisto-o-prokarved.html")


if __name__ == "__main__":
    main()
