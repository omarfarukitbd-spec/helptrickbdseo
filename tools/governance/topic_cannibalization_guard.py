#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/governance/topic_cannibalization_guard.py
------------------------------------------------
HelpTrickBD Anti-Cannibalization & Duplicate Content Guard
Checks proposed topics, questions, or PDF content against all 86+ live posts
on HelpTrickBD to strictly prevent Keyword Cannibalization and duplicate posts.

Features:
1. Tokenizes and cleans candidate questions/topics (Bengali & English).
2. Calculates semantic and keyword overlap with all_live_posts_catalog.json.
3. Automatically flags existing topics with exact live URLs.
4. Generates a clear verdict: WHICH topics to skip, and WHICH new topics to create.
"""

import os
import sys
import re
import json
import argparse

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CATALOG_PATH = os.path.join(PROJECT_ROOT, "all_live_posts_catalog.json")

# Meaningless stopwords to exclude from matching
STOPWORDS = {
    "ও", "এবং", "বা", "কি", "কী", "কাকে", "বলে", "এর", "তে", "এ", "থেকে", "দিয়ে",
    "জন্য", "নিয়ে", "সম্পর্কে", "বিস্তারিত", "নিয়ম", "পদ্ধতি", "সহজ", "২০২৪", "২০২৫", "২০২৬",
    "the", "a", "an", "and", "or", "in", "on", "at", "to", "for", "of", "with", "is", "what", "how",
    "ব্যাখ্যা", "কর", "করো", "লেখ", "লেখো", "আলোচনা", "বর্ণনা", "বলতে", "সংজ্ঞা", "বৈশিষ্ট্য",
    "ছিল", "থাকে", "হলো", "হলে", "হতে", "হওয়ার", "লাভের", "সমূহ", "কীভাবে"
}

def clean_and_tokenize(text: str) -> set:
    """Extracts meaningful keyword tokens with Bengali Unicode support & root forms."""
    words = re.findall(r"[a-zA-Z0-9_\u0980-\u09FF]+", text.lower())
    tokens = set()
    for w in words:
        if w not in STOPWORDS and len(w) > 2:
            tokens.add(w)
            # Add root forms by stripping common Bengali inflections
            for suffix in ["সমূহের", "সমূহ", "গুলোর", "গুলো", "টিতে", "টির", "টি", "দের", "ের", "ার", "তে", "ে"]:
                if len(w) > len(suffix) + 3 and w.endswith(suffix):
                    tokens.add(w[:-len(suffix)])
    return tokens

def calculate_similarity(candidate_tokens: set, post_tokens: set) -> float:
    """Calculates weighted keyword overlap score."""
    if not candidate_tokens or not post_tokens:
        return 0.0
    common = candidate_tokens.intersection(post_tokens)
    # Score based on candidate coverage
    return len(common) / len(candidate_tokens)

def load_live_catalog():
    """Loads all live posts from catalog."""
    if not os.path.exists(CATALOG_PATH):
        return []
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def check_topic_against_live_posts(candidate_title: str, threshold: float = 0.50):
    """
    Checks a proposed topic against all live posts.
    Returns: (is_duplicate: bool, matches: list)
    """
    catalog = load_live_catalog()
    candidate_tokens = clean_and_tokenize(candidate_title)
    
    matches = []
    for post in catalog:
        post_title = post.get("title", "")
        post_url = post.get("url", "")
        post_tokens = clean_and_tokenize(post_title + " " + post_url)
        
        sim = calculate_similarity(candidate_tokens, post_tokens)
        if sim >= threshold:
            matches.append({
                "title": post_title,
                "url": post_url,
                "id": post.get("id"),
                "similarity": round(sim * 100, 1),
                "common_keywords": list(candidate_tokens.intersection(post_tokens))
            })
            
    matches.sort(key=lambda x: x["similarity"], reverse=True)
    is_duplicate = len(matches) > 0
    return is_duplicate, matches

def scan_topics_list(topic_list: list, threshold: float = 0.50):
    """
    Scans a list of proposed topics/questions.
    Categorizes into:
      - covered_topics (ALREADY EXIST -> SKIP)
      - fresh_topics (NEW -> APPROVED)
    """
    covered = []
    fresh = []
    
    for idx, topic in enumerate(topic_list, 1):
        is_dup, matches = check_topic_against_live_posts(topic, threshold=threshold)
        if is_dup:
            covered.append({
                "index": idx,
                "topic": topic,
                "best_match": matches[0]
            })
        else:
            fresh.append({
                "index": idx,
                "topic": topic
            })
            
    return covered, fresh

def print_audit_report(covered: list, fresh: list):
    """Prints a clear, human-readable Bengali audit report."""
    print("\n" + "=" * 75)
    print("🛡️ HELPTRICKBD — কন্টেন্ট ক্যানিব্যালাইজেশন ও ডুপ্লিকেট টপিক অডিট রিপোর্ট")
    print("=" * 75)
    
    if covered:
        print(f"\n⚠️  বিদ্যমান টপিক ({len(covered)} টি) — [ এগুলোর ওপর নতুন পোস্ট তৈরি নিষিদ্ধ / স্কিপ ]: ")
        for c in covered:
            match = c["best_match"]
            print(f"  ❌ [{c['index']}] প্রস্তাবিত বিষয়: {c['topic']}")
            print(f"     ➔ বিদ্যমান লাইভ পোস্ট: {match['title']}")
            print(f"     ➔ লাইভ ইউআরএল: {match['url']}")
            print(f"     ➔ মিলের মাত্রা (Similarity): {match['similarity']}% (সাধারণ কী-ওয়ার্ড: {', '.join(match['common_keywords'])})")
            print("     ➔ অ্যাকশন: স্কিপ (Skip) করুন, যাতে কী-ওয়ার্ড ক্যানিব্যালাইজেশন না ঘটে।\n")
    else:
        print("\n✅ কোনো বিদ্যমান ডুপ্লিকেট টপিক পাওয়া যায়নি (0 Duplicates)!")
        
    if fresh:
        print(f"\n✨ নতুন ও অনুত্তরিত টপিক ({len(fresh)} টি) — [ এগুলোর ওপর নতুন পোস্ট তৈরি অনুমোদিত ]: ")
        for f in fresh:
            print(f"  ✔ [{f['index']}] {f['topic']} ➔ (অনুমোদিত — সেফ টু পাবলিশ)")
    else:
        print("\n[!] কোনো নতুন টপিক পাওয়া যায়নি। সব টপিকই ইতিমধ্যে সাইটে বিদ্যমান।")
        
    print("\n" + "=" * 75)

def extract_topics_from_pdf(pdf_path: str) -> list:
    """Extracts candidate questions or topic lines from a PDF file."""
    if not os.path.exists(pdf_path):
        print(f"Error: PDF file not found at {pdf_path}")
        return []
    
    extracted_text = ""
    try:
        import pypdf
        reader = pypdf.PdfReader(pdf_path)
        for page in reader.pages:
            t = page.extract_text()
            if t:
                extracted_text += t + "\n"
    except Exception as e:
        print(f"Warning: pypdf failed to read ({e}), trying pdfplumber...")
        try:
            import pdfplumber
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    t = page.extract_text()
                    if t:
                        extracted_text += t + "\n"
        except Exception as e2:
            print(f"Error reading PDF: {e2}")
            return []

    if not extracted_text.strip():
        print("Note: The PDF seems to be image-based or contains no selectable text. Please provide topics via text or OCR.")
        return []

    # Split lines and look for questions / numbered topics
    lines = [line.strip() for line in extracted_text.splitlines() if line.strip()]
    candidate_topics = []
    
    for line in lines:
        # Match lines with question mark, or starting with serial numbers
        if "?" in line or "？" in line or re.match(r"^(\d+|[১-৯]+|[a-zA-Z]|[ক-হ])[\.\-\)]\s*", line):
            # Clean leading serial numbers
            clean_line = re.sub(r"^(\d+|[১-৯]+|[a-zA-Z]|[ক-হ])[\.\-\)]\s*", "", line).strip()
            if len(clean_line) > 5 and clean_line not in candidate_topics:
                candidate_topics.append(clean_line)
                
    if not candidate_topics:
        # Fallback to non-empty lines with at least 4 words
        for line in lines:
            if len(line.split()) >= 4 and len(line) > 15:
                candidate_topics.append(line)
                
    return candidate_topics

def extract_topics_from_file(file_path: str) -> list:
    """Extracts topics from a .txt or .json file."""
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return []
    if file_path.endswith(".json"):
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return [str(item) for item in data]
            return []
    else:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
            return lines

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HelpTrickBD Anti-Cannibalization & Duplicate Topic Guard")
    parser.add_argument("--topics", nargs="+", help="List of candidate topics to evaluate")
    parser.add_argument("--pdf", type=str, help="Path to PDF file containing questions/topics")
    parser.add_argument("--file", type=str, help="Path to .txt or .json file containing questions")
    parser.add_argument("--threshold", type=float, default=0.50, help="Similarity threshold (default: 0.50)")
    parser.add_argument("--test", action="store_true", help="Run test on sample topics")
    args = parser.parse_args()
    
    candidate_list = []
    
    if args.test:
        candidate_list = [
            "বাংলাদেশে রাজনৈতিক সহিংসতার কারণ ও প্রতিকার কী?",
            "জাতিসংঘের সদস্যপদ লাভে বাংলাদেশের কী কী বাধা ছিল?",
            "বাংলাদেশের পররাষ্ট্রনীতির মূল বৈশিষ্ট্যসমূহ কী কী?",
            "সার্বভৌমত্ব কাকে বলে ও এর বৈশিষ্ট্য",
            "মুক্তিযুদ্ধে ৭ই মার্চের ভাষণের ঐতিহাসিক গুরুত্ব"
        ]
    elif args.pdf:
        candidate_list = extract_topics_from_pdf(args.pdf)
    elif args.file:
        candidate_list = extract_topics_from_file(args.file)
    elif args.topics:
        candidate_list = args.topics
    else:
        print("Usage:")
        print("  python topic_cannibalization_guard.py --topics 'টপিক ১' 'টপিক ২'")
        print("  python topic_cannibalization_guard.py --pdf <PATH_TO_PDF>")
        print("  python topic_cannibalization_guard.py --file <PATH_TO_TXT_OR_JSON>")
        print("  python topic_cannibalization_guard.py --test")
        sys.exit(0)
        
    if candidate_list:
        covered, fresh = scan_topics_list(candidate_list, threshold=args.threshold)
        print_audit_report(covered, fresh)
    else:
        print("No topics found to evaluate.")
