import json
import sys

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

with open("site_full_360_audit.json", encoding="utf-8") as f:
    d = json.load(f)

print("=== 13 DUPLICATE TOC POSTS ===")
for i, p in enumerate(d["duplicate_toc"], 1):
    print(f"{i}. [{p['id']}] {p['title']}")

print("\n=== 5 THIN POSTS (< 600 WORDS) ===")
for i, p in enumerate(d["thin_posts"], 1):
    print(f"{i}. [{p['id']}] ({p['words']} words) {p['title']}")
    print(f"   URL: {p['url']}")

print("\n=== 4 MISSING BANNER POSTS ===")
for i, p in enumerate(d["missing_banner"], 1):
    print(f"{i}. [{p['id']}] {p['title']}")
