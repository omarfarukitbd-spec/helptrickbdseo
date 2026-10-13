import json, sys

def full_export():
    with open("reports/rank_math_test_report.json", "r", encoding="utf-8") as f:
        posts = json.load(f)
        
    lines = []
    lines.append("| No | ID | Slug | Focus Keyword | Native Title |")
    lines.append("|---|---|---|---|---|")
    for i, p in enumerate(posts, 1):
        pid = p.get("id")
        slug = p.get("slug", "")
        kw = p.get("primary_keyword", "")
        title = p.get("native_title", "")
        lines.append(f"| {i} | {pid} | `{slug}` | **{kw}** | {title} |")
        
    with open("reports/keyword_audit_table.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Exported {len(posts)} rows to reports/keyword_audit_table.md")

if __name__ == "__main__":
    full_export()
