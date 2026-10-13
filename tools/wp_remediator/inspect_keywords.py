import json, sys

sys.stdout.reconfigure(encoding='utf-8')

def inspect_report():
    with open("reports/rank_math_test_report.json", "r", encoding="utf-8") as f:
        posts = json.load(f)
    print(f"Total posts: {len(posts)}")
    for i, p in enumerate(posts[:40], 1):
        pid = p.get("id")
        slug = p.get("slug")
        kw = p.get("primary_keyword")
        title = p.get("native_title", "")[:50]
        print(f"[{i:02d}] ID:{pid} | KW: '{kw}' | Title: {title}")

if __name__ == "__main__":
    inspect_report()
