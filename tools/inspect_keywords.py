import sys, io, json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

with open("Helptrickbd Wp/migration_log.json", "r", encoding="utf-8") as f:
    data = json.load(f)

posts = data.get("posts", [])
print(f"Total posts: {len(posts)}")
for i, p in enumerate(posts[:25]):
    slug = p.get("slug", "")
    kw = p.get("focus_keyword", "")
    title = p.get("title", "")
    print(f"[{i+1}] {slug} -> KW: '{kw}' | Title: {title[:40]}")
