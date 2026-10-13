import json, sys

sys.stdout.reconfigure(encoding='utf-8')

def audit():
    with open("reports/rank_math_test_report.json", "r", encoding="utf-8") as f:
        posts = json.load(f)
        
    print(f"Total posts: {len(posts)}")
    curated_needed = []
    for i, p in enumerate(posts, 1):
        pid = p.get("id")
        slug = p.get("slug")
        kw = p.get("primary_keyword", "")
        title = p.get("native_title", "")
        
        # Check if keyword has issues (truncated, duplicate words, ends with conjunction, etc.)
        ends_with_bad = any(kw.endswith(bad) for bad in [" ও", " এবং", " এর", " তে", " জন্য", " সালের", " জরুরি", " রাজনৈতিক", " ঐতিহ্য ঐতিহ্যের"])
        too_short_or_awkward = len(kw.split()) < 2 or "ঐতিহ্যের" in kw or "সাজেশন পরীক্ষা" in kw or kw.endswith("Right") or kw.endswith("Preposition")
        
        print(f"[{i:03d}] ID:{pid:3d} | SLUG: {slug[:40]:40s} | KW: '{kw}'")
        if ends_with_bad or too_short_or_awkward:
            curated_needed.append((pid, slug, kw))

    print(f"\nPotential improvement candidates: {len(curated_needed)}")

if __name__ == "__main__":
    audit()
