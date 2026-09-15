#!/usr/bin/env python3
import glob
import json
import os
import subprocess

REVIVED_DIR = "output_posts/revived_posts"
meta_files = glob.glob(os.path.join(REVIVED_DIR, "*_metadata.json"))

urls = []
for mf in meta_files:
    with open(mf, "r", encoding="utf-8") as f:
        d = json.load(f)
        slug = d.get("slug", "")
        # Get live URL from all_live_posts_catalog.json
        urls.append(slug)

with open("all_live_posts_catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

live_revived_urls = []
for p in catalog:
    for slug in urls:
        if slug in p.get("url", ""):
            live_revived_urls.append(p.get("url"))
            break

live_revived_urls = list(set(live_revived_urls))
print(f"Total revived URLs found in live catalog: {len(live_revived_urls)}")

out_file = "tools/indexer/revived_30_urls.txt"
with open(out_file, "w", encoding="utf-8") as f:
    for u in sorted(live_revived_urls):
        f.write(u + "\n")
print(f"Saved to {out_file}")

# Ping Google Indexing API
res = subprocess.run(["python", "tools/indexer/index_now.py", "--file", out_file], capture_output=True, text=True)
print("IndexNow Output:\n", res.stdout)
if res.stderr:
    print("IndexNow Error:\n", res.stderr)
