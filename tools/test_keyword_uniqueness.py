import sys, io, json, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

with open("Helptrickbd Wp/migration_log.json", "r", encoding="utf-8") as f:
    data = json.load(f)

posts = data.get("posts", [])

def normalize_bengali(text: str) -> str:
    if not text:
        return ""
    import unicodedata
    t = unicodedata.normalize("NFC", text)
    t = t.replace("\u09af\u09bc", "\u09df")
    return t

used_keywords = set()
results = []

for i, p in enumerate(posts):
    slug = p.get("slug", "").strip()
    title = normalize_bengali(p.get("title", "").strip())
    kw = normalize_bengali(p.get("focus_keyword", "").strip())

    # Intelligent specific keyword refinement based on slug and title
    if "part-1" in slug or "পর্ব-১" in title or "পর্ব ১" in title:
        if "পর্ব ১" not in kw and "Part 1" not in kw:
            kw = f"{kw} পর্ব ১"
    elif "part-2" in slug or "পর্ব-২" in title or "পর্ব ২" in title:
        if "পর্ব ২" not in kw and "Part 2" not in kw:
            kw = f"{kw} পর্ব ২"
    elif "part-3" in slug or "পর্ব-৩" in title or "পর্ব ৩" in title:
        if "পর্ব ৩" not in kw and "Part 3" not in kw:
            kw = f"{kw} পর্ব ৩"
    elif "model-test" in slug or "মডেল টেস্ট" in title:
        if "মডেল টেস্ট" not in kw and "Model Test" not in kw:
            kw = f"{kw} মডেল টেস্ট"
    elif "final-suggestion" in slug or "ফাইনাল সাজেশন" in title:
        if "ফাইনাল সাজেশন" not in kw and "Final Suggestion" not in kw:
            kw = f"{kw} ফাইনাল সাজেশন"
    elif "routine" in slug or "রুটিন" in title:
        if "রুটিন" not in kw and "Routine" not in kw:
            kw = f"{kw} পরীক্ষার রুটিন"
    elif "in-course" in slug or "ইনকোর্স" in title:
        if "ইনকোর্স" not in kw:
            kw = f"{kw} ইনকোর্স নম্বর"
    elif "marks-distribution" in slug or "মানবণ্টন" in title:
        if "মানবণ্টন" not in kw:
            kw = f"{kw} মানবণ্টন"

    # Specific topic detection if kw is too generic (e.g. 'আমাদের নতুন গৌরবগাথা')
    if "আমাদের নতুন গৌরবগাথা" in title and "গৌরবগাথা" not in kw:
        kw = "আমাদের নতুন গৌরবগাথা সৃজনশীল প্রশ্ন"
    elif "bagdhara" in slug or "বাগধারা" in title:
        kw = "বিসিএস বাংলা ব্যাকরণ বাগধারা"
    elif "karak" in slug or "কারক" in title:
        kw = "কারক ও বিভক্তি নির্ণয়ের সহজ নিয়ম"
    elif "shondhi" in slug or "সন্ধি" in title:
        kw = "সন্ধি বিচ্ছেদ করার নিয়মাবলী"

    # If still collision, disambiguate with unique word from title
    if kw in used_keywords:
        clean_t = re.sub(r"[\(\)\[\]\{\}\-\|\:\,\.\?\!]", " ", title)
        title_words = [w for w in clean_t.split() if len(w) > 3 and w not in kw and w not in ["জাতীয়", "বিশ্ববিদ্যালয়", "পরীক্ষার", "সম্পর্কে", "বিস্তারিত"]]
        if title_words:
            kw = f"{kw} {title_words[0]}"
        else:
            kw = f"{kw} ২০২৬"

    used_keywords.add(kw)
    results.append((slug, kw, title[:35]))

print(f"Total Unique Keywords: {len(used_keywords)} out of {len(posts)} posts")
duplicates = len(posts) - len(used_keywords)
print(f"Total Duplicates: {duplicates}")

print("\n--- Sample Refined High-Intent Keywords ---")
for slug, kw, t in results[10:30]:
    print(f"{slug} -> KW: '{kw}' | Title: {t}")
