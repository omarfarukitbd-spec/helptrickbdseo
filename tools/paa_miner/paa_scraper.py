#!/usr/bin/env python3
"""
tools/paa_miner/paa_scraper.py
Google People Also Ask (PAA) and Autocomplete Long-Tail Query Scraper.
Generates Schema.org FAQPage JSON-LD and clean SolaimanLipi HTML FAQ Cards for Position 0.
"""

import os
import sys
import json
import argparse
import urllib.parse
import requests
from bs4 import BeautifulSoup

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
]


def fetch_google_autocomplete(query: str, lang: str = "bn", country: str = "bd") -> list[str]:
    """Fetches real-time search queries and question phrases from Google Suggest API."""
    url = f"https://suggestqueries.google.com/complete/search?client=chrome&hl={lang}&gl={country}&q={urllib.parse.quote(query)}"
    headers = {"User-Agent": USER_AGENTS[0]}

    try:
        resp = requests.get(url, headers=headers, timeout=8)
        if resp.status_code == 200:
            data = resp.json()
            # data format: [query, [suggestions...], ...]
            if len(data) > 1 and isinstance(data[1], list):
                return [s.strip() for s in data[1] if s.strip()]
    except Exception as e:
        print(f"⚠️ Warning: Autocomplete fetch failed for '{query}': {e}", file=sys.stderr)
    return []


def generate_paa_questions(keyword: str, lang: str = "bn") -> list[dict]:
    """
    Mines PAA & long-tail search questions using question modifiers
    appropriate for Bengali or English queries.
    """
    questions = []
    seen = set()

    if lang == "bn":
        modifiers = [
            f"{keyword} কি",
            f"{keyword} কাকে বলে",
            f"{keyword} কিভাবে",
            f"{keyword} এর নিয়ম",
            f"{keyword} এর বৈশিষ্ট্য",
            f"{keyword} করতে কত টাকা লাগে",
            f"{keyword} এর প্রয়োজনীয় কাগজপত্র",
            f"{keyword} এর সুবিধা কি",
        ]
    else:
        modifiers = [
            f"what is {keyword}",
            f"how to {keyword}",
            f"{keyword} requirements",
            f"{keyword} fees and cost",
            f"{keyword} rules and regulations",
            f"why {keyword} is important",
            f"{keyword} step by step process",
        ]

    # Gather autocomplete questions for root keyword
    root_suggestions = fetch_google_autocomplete(keyword, lang=lang)
    for s in root_suggestions:
        if s.lower() not in seen:
            seen.add(s.lower())
            questions.append({
                "question": s,
                "source": "Google Autocomplete"
            })

    # Gather questions with modifiers
    for mod in modifiers:
        suggestions = fetch_google_autocomplete(mod, lang=lang)
        for s in suggestions:
            if s.lower() not in seen:
                seen.add(s.lower())
                questions.append({
                    "question": s,
                    "source": "PAA Question Modifier"
                })

    return questions[:12]


def generate_faq_schema_and_html(keyword: str, questions: list[dict], lang: str = "bn") -> tuple[dict, str]:
    """
    Generates valid Schema.org FAQPage JSON-LD and clean SolaimanLipi HTML cards.
    """
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": []
    }

    html_cards = []
    html_cards.append('<!-- [START] Helptrickbd Position 0 FAQ Section -->')
    html_cards.append('<div class="htbd-faq-section" style="margin: 35px 0; font-family: \'SolaimanLipi\', sans-serif;">')
    html_cards.append(f'  <h2 style="color: #1a73e8; border-left: 5px solid #1a73e8; padding-left: 14px; font-size: 22px; font-weight: 700; margin-bottom: 20px;">'
                      f'{"প্রায়শই জিজ্ঞাসিত প্রশ্নাবলি (FAQ)" if lang == "bn" else "Frequently Asked Questions (FAQ)"}</h2>')

    for idx, q_item in enumerate(questions[:6], start=1):
        q_text = q_item["question"]
        # Formulate answer placeholder or draft
        if lang == "bn":
            ans_text = f"{q_text} সম্পর্কিত সঠিক তথ্য হলো—বোর্ড ও প্রাতিষ্ঠানিক সর্বশেষ নীতিমালা ২০২৬ অনুযায়ী এটি সম্পূর্ণভাবে অনলাইন ও প্রমিত নিয়মে সম্পন্ন করা যায়।"
        else:
            ans_text = f"Regarding '{q_text}', according to official 2026 guidelines, this procedure can be seamlessly completed following institutional verified steps."

        faq_schema["mainEntity"].append({
            "@type": "Question",
            "name": q_text,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": ans_text
            }
        })

        card_html = f"""  <div class="htbd-faq-item" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 18px 22px; margin-bottom: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
    <h3 style="margin: 0 0 10px 0; font-size: 18.5px; color: #0f172a; font-weight: 700;">
      ❓ {idx}. {q_text}
    </h3>
    <p style="margin: 0; font-size: 16.5px; line-height: 1.8; color: #334155; text-align: justify;">
      {ans_text}
    </p>
  </div>"""
        html_cards.append(card_html)

    # Embed JSON-LD schema into HTML output
    schema_json_str = json.dumps(faq_schema, ensure_ascii=False, indent=2)
    html_cards.append(f'<script type="application/ld+json">\n{schema_json_str}\n</script>')
    html_cards.append('</div>')
    html_cards.append('<!-- [END] Helptrickbd Position 0 FAQ Section -->')

    return faq_schema, "\n".join(html_cards)


def main():
    parser = argparse.ArgumentParser(description="Google PAA & Long-Tail Query Scraper for Helptrickbd")
    parser.add_argument("--keyword", "-k", required=True, help="Target keyword to mine PAA questions for")
    parser.add_argument("--lang", "-l", default="bn", choices=["bn", "en"], help="Language: bn or en (default: bn)")
    parser.add_argument("--output-json", "-j", help="Path to save mined questions JSON")
    parser.add_argument("--output-html", "-o", help="Path to save formatted FAQ HTML snippet")

    args = parser.parse_args()

    print("=" * 65)
    print(f"🔍 Helptrickbd PAA & Question Miner: '{args.keyword}' ({args.lang})")
    print("=" * 65)

    questions = generate_paa_questions(args.keyword, lang=args.lang)
    print(f"✨ Discovered {len(questions)} high-intent questions from Google:")
    for i, q in enumerate(questions, 1):
        print(f"  {i:2d}. {q['question']}")

    faq_schema, faq_html = generate_faq_schema_and_html(args.keyword, questions, lang=args.lang)

    if args.output_json:
        with open(args.output_json, "w", encoding="utf-8") as f:
            json.dump({"keyword": args.keyword, "questions": questions, "schema": faq_schema}, f, ensure_ascii=False, indent=2)
        print(f"\n💾 Saved JSON to: {args.output_json}")

    if args.output_html:
        with open(args.output_html, "w", encoding="utf-8") as f:
            f.write(faq_html)
        print(f"💾 Saved FAQ HTML to: {args.output_html}")
    else:
        print("\n" + "-" * 40 + " Generated FAQ Schema & HTML " + "-" * 40)
        print(faq_html[:600] + "\n... [truncated] ...")


if __name__ == "__main__":
    main()
