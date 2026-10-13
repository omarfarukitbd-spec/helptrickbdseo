import sys

with open("tools/wp_remediator/rank_math_bulk_optimizer.py", "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

# Let's inspect where the duplicate occurs and fix it cleanly
idx1 = text.find("def generate_optimized_seo_title")
idx2 = text.find("def optimize_content")

if idx1 != -1 and idx2 != -1:
    clean_replacement = """    def generate_optimized_seo_title(self, raw_title: str, focus_keyword: str) -> str:
        \"\"\"
        Guarantees ALL Title Readability tests pass with 100% GREEN score:
        1. titleStartsWithKeyword: Focus Keyword placed at the very start
        2. titleSentiment: Contains 'Best' (Rank Math positive sentiment trigger)
        3. titleHasPowerWords: Contains 'Best' and 'Guide' (Rank Math power word triggers)
        4. titleHasNumber: Contains '2026'
        5. keywordInTitle: Focus keyword is present
        \"\"\"
        title = self.normalize_bengali(raw_title.strip())
        focus_kw = self.normalize_bengali(focus_keyword.strip())

        title = re.sub(r"\\s*(?:২০২৫|২০২৬|২০২৭|2025|2026|2027)\\s*", " ", title)
        title = re.sub(r"\\s*&#038;\\s*", " ও ", title)
        title = re.sub(r"\\[.*?\\]|\\(.*?\\)", "", title)
        title = re.sub(r"\\s*[-|:]\\s*Best Complete Guide\\s*\\d*", "", title, flags=re.IGNORECASE)
        title = re.sub(r"\\s+", " ", title).strip()

        clean_body = re.sub(re.escape(focus_kw), "", title, flags=re.IGNORECASE).strip(" -|:፣")
        clean_body = re.sub(r"^(?:জাতীয় বিশ্ববিদ্যালয়|বাংলাদেশ)\\s*", "", clean_body).strip(" -|:፣")
        clean_body = re.sub(r"^(?:SSC English 2nd Paper Suggestion|SSC English 1st Paper Suggestion|SSC Bangla 1st Paper|SSC 2nd Paper)\\s*", "", clean_body, flags=re.IGNORECASE).strip(" -|:፣")
        if not clean_body or len(clean_body) < 4:
            clean_body = "পূর্ণাঙ্গ প্রস্তুতি ও নিয়মাবলী"

        seo_title = f"{focus_kw}: {clean_body} - Best Complete Guide 2026"
        seo_title = re.sub(r"\\s*[-|:]\\s*[-|:]\\s*", " - ", seo_title)
        seo_title = re.sub(r"\\s+", " ", seo_title).strip()
        return seo_title

    def generate_native_wp_title(self, raw_title: str, focus_keyword: str) -> str:
        \"\"\"
        Constructs the native Gutenberg post title starting with the focus keyword
        and containing [Best Guide 2026] to pass Gutenberg client-side checks.
        \"\"\"
        title = self.normalize_bengali(raw_title.strip())
        focus_kw = self.normalize_bengali(focus_keyword.strip())

        title = re.sub(r"\\s*(?:২০২৫|২০২৬|২০২৭|2025|2026|2027)\\s*", " ", title)
        title = re.sub(r"\\s*&#038;\\s*", " ও ", title)
        title = re.sub(r"\\[.*?\\]|\\(.*?\\)", "", title)
        title = re.sub(r"\\s*[-|:]\\s*Best Complete Guide\\s*\\d*", "", title, flags=re.IGNORECASE)
        title = re.sub(r"\\s+", " ", title).strip()

        clean_body = re.sub(re.escape(focus_kw), "", title, flags=re.IGNORECASE).strip(" -|:፣")
        clean_body = re.sub(r"^(?:জাতীয় বিশ্ববিদ্যালয়|বাংলাদেশ)\\s*", "", clean_body).strip(" -|:軻")
        clean_body = re.sub(r"^(?:SSC English 2nd Paper Suggestion|SSC English 1st Paper Suggestion|SSC Bangla 1st Paper|SSC 2nd Paper)\\s*", "", clean_body, flags=re.IGNORECASE).strip(" -|:፣")
        if not clean_body or len(clean_body) < 4:
            clean_body = "পূর্ণাঙ্গ প্রস্তুতি নির্দেশিকা"

        wp_title = f"{focus_kw}: {clean_body} - Best Complete Guide 2026"
        wp_title = re.sub(r"\\s*[-|:]\\s*[-|:]\\s*", " - ", wp_title)
        wp_title = re.sub(r"\\s+", " ", wp_title).strip()
        return wp_title

"""
    new_text = text[:idx1] + clean_replacement + text[idx2:]
    with open("tools/wp_remediator/rank_math_bulk_optimizer.py", "w", encoding="utf-8") as out:
        out.write(new_text)
    print("Successfully rewritten!")
else:
    print("Indices not found:", idx1, idx2)
