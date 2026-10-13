import json, sys, glob, os

sys.stdout.reconfigure(encoding='utf-8')

def inspect_all():
    files = glob.glob("backups/rank_math_backups/*.json")
    print(f"Total backups found: {len(files)}")
    
    posts_data = []
    for f in sorted(files, key=lambda x: int(os.path.basename(x).replace("post_", "").replace("_backup.json", "")) if os.path.basename(x).replace("post_", "").replace("_backup.json", "").isdigit() else 0):
        with open(f, "r", encoding="utf-8") as fp:
            d = json.load(fp)
            pid = d.get("id")
            slug = d.get("slug")
            raw_title = d.get("title", {}).get("raw", "")
            posts_data.append({"id": pid, "slug": slug, "raw_title": raw_title})
            
    with open("reports/all_134_posts_manifest.json", "w", encoding="utf-8") as out:
        json.dump(posts_data, out, ensure_ascii=False, indent=2)
    print(f"Saved {len(posts_data)} posts to reports/all_134_posts_manifest.json")

if __name__ == "__main__":
    inspect_all()
