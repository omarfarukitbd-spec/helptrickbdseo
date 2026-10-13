with open("tools/wp_remediator/rank_math_bulk_optimizer.py", "r", encoding="utf-8") as f:
    text = f.read()

target = """            if limit and len(posts) >= limit:
                posts = posts[:limit]
                break
     def extract_clean_focus_keyword(self, title: str, slug: str) -> str:"""

replacement = """            if limit and len(posts) >= limit:
                posts = posts[:limit]
                break
            total_pages = int(res.headers.get("X-WP-TotalPages", 1))
            if page >= total_pages:
                break
            page += 1
            time.sleep(0.2)

        return posts

    def normalize_bengali(self, text: str) -> str:
        \"\"\"Normalizes Bengali text, handling composed characters and yya variations consistently.\"\"\"
        if not text:
            return ""
        import unicodedata
        t = unicodedata.normalize("NFC", text)
        t = t.replace("\\u09af\\u09bc", "\\u09df")
        return t

    def extract_clean_focus_keyword(self, title: str, slug: str) -> str:"""

if target in text:
    new_text = text.replace(target, replacement, 1)
    with open("tools/wp_remediator/rank_math_bulk_optimizer.py", "w", encoding="utf-8") as out:
        out.write(new_text)
    print("Fixed target replacement!")
else:
    print("Target not found!")
