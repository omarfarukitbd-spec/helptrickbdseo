import csv
import urllib.parse
import os
import re

CSV_PATH = "data/gsc_benchmarks/gsc_404_export.csv"
OUTPUT_MAPPING_CSV = "data/gsc_benchmarks/blogger_custom_redirects_301.csv"
OUTPUT_SUMMARY_MD = "data/gsc_benchmarks/404_redirect_analysis.md"

def clean_path(raw_url):
    parsed = urllib.parse.urlparse(raw_url.strip())
    path = parsed.path
    if not path.startswith("/"):
        path = "/" + path
    return path

def smart_target(path):
    p = path.lower()
    
    # 1. Dakhil suggestions
    if "dakhil" in p or "fiqh" in p or "aqaid" in p or "quran" in p:
        return "/search/label/Dakhil%20Suggestion"
    
    # 2. SSC English & Study Guides
    if "ssc" in p or "english" in p:
        return "/2026/09/ssc-english-1st-paper-suggestion-2027.html"
        
    # 3. Class 5, 7, 8, 9, 10 Guides
    if any(k in p for k in ["class-", "guide", "text-book", "annual-exam", "panjeree"]):
        return "/search/label/Education"
        
    # 4. Political Science
    if any(k in p for k in ["political", "rastro", "sorkar", "songsod", "sarbobhoumotto"]):
        return "/search/label/Political%20Science"
        
    # 5. Economics
    if any(k in p for k in ["economy", "budget", "inflation", "remittance", "shilpo"]):
        return "/search/label/Economics"
        
    # 6. Islamic
    if any(k in p for k in ["islam", "hadith", "sunnah", "nabi", "milad"]):
        return "/search/label/Islamic"
        
    # 7. Technology
    if any(k in p for k in ["tech", "computer", "phone", "internet", "android"]):
        return "/search/label/Technology"
        
    # Fallback to home page
    return "/"

def main():
    if not os.path.exists(CSV_PATH):
        print(f"Error: {CSV_PATH} not found")
        return

    raw_urls = []
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            if row:
                raw_urls.append(row[0])

    print(f"Total raw 404 URLs from GSC: {len(raw_urls)}")

    # Clean paths and deduplicate
    path_map = {}
    for u in raw_urls:
        clean_p = clean_path(u)
        if clean_p and clean_p != "/":
            if clean_p not in path_map:
                path_map[clean_p] = smart_target(clean_p)

    print(f"Unique relative paths to redirect: {len(path_map)}")

    # Write Blogger CSV (Blogger supports Custom Redirects in format From -> To, Permanent: Yes)
    with open(OUTPUT_MAPPING_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["From (Relative URL)", "To (Destination)", "Type", "Permanent (301)"])
        for from_p, to_p in sorted(path_map.items()):
            writer.writerow([from_p, to_p, "301 Permanent", "Yes"])

    # Categorize destinations for reporting
    cat_counts = {}
    for from_p, to_p in path_map.items():
        cat_counts[to_p] = cat_counts.get(to_p, 0) + 1

    # Write summary markdown
    with open(OUTPUT_SUMMARY_MD, "w", encoding="utf-8") as f:
        f.write("# হেল্পট্রিকবিডি: ১১১টি ৪০৪ লিঙ্কের ৩০১ পার্মানেন্ট রিডাইরেক্ট ম্যাপিং রিপোর্ট\n\n")
        f.write(f"- **মোট র-ইউআরএল:** {len(raw_urls)} টি\n")
        f.write(f"- **অনন্য আপেক্ষিক পাথ (Unique Relative Paths):** {len(path_map)} টি\n")
        f.write(f"- **রিডাইরেক্ট টাইপ:** ৩০১ পার্মানেন্ট রিডাইরেক্ট (Permanent: Yes)\n\n")
        f.write("## ১. গন্তব্য ক্যাটাগরি ও পোস্টভিত্তিক পরিসংখ্যান\n\n")
        f.write("| গন্তব্য ইউআরএল (Destination URL) | রিডাইরেক্ট হওয়া লিঙ্কের সংখ্যা |\n")
        f.write("| :--- | :--- |\n")
        for dest, cnt in sorted(cat_counts.items(), key=lambda x: x[1], reverse=True):
            f.write(f"| `{dest}` | {cnt} টি |\n")
        f.write("\n## ২. সম্পূর্ণ রিডাইরেক্ট রুলস তালিকা (শীর্ষ ২০টি নমুনা)\n\n")
        f.write("| উৎস পাথ (From) | গন্তব্য (To) | পার্মানেন্ট |\n")
        f.write("| :--- | :--- | :--- |\n")
        for from_p, to_p in sorted(path_map.items())[:25]:
            f.write(f"| `{from_p}` | `{to_p}` | Yes |\n")
        f.write("\n*(সম্পূর্ণ তালিকা `data/gsc_benchmarks/blogger_custom_redirects_301.csv`-এ সংরক্ষিত)*\n")

    print(f"Successfully generated: {OUTPUT_MAPPING_CSV}")
    print(f"Successfully generated: {OUTPUT_SUMMARY_MD}")

if __name__ == "__main__":
    main()
