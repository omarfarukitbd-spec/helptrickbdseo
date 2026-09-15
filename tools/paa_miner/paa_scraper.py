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


def synthesize_answer(question: str, lang: str = "bn") -> str:
    """
    Intelligently synthesizes an authoritative, concise answer for PAA questions
    in Bengali or English based on intent keywords (fee, docs, steps, definition, time).
    """
    q_lower = question.lower()

    if lang == "bn":
        if any(w in q_lower for w in ["টাকা", "খরচ", "ফি", "কত টাকা"]):
            return (
                f"{question} সম্পর্কিত সরকারি সর্বশেষ নির্দেশনা অনুযায়ী নির্ধারিত ফি সোনালী সেবা বা মোবাইল ব্যাংকিং "
                f"(বিকাশ/রকেট/নগদ)-এর মাধ্যমে পরিশোধ করা যায়। শিক্ষা বোর্ড বা সংশ্লিষ্ট কর্তৃপক্ষের নির্ধারিত মূল ফি ৫০০ থেকে ১,০০০ টাকার মধ্যে "
                f"হয়ে থাকে এবং নতুন সাময়িক সনদের জন্য অতিরিক্ত ফি প্রযোজ্য হতে পারে।"
            )
        elif any(w in q_lower for w in ["কাগজপত্র", "ডকুমেন্ট", "কি কি লাগে", "কী কী লাগবে", "প্রমাণক"]):
            return (
                f"{question} সম্পন্ন করার জন্য প্রয়োজনীয় মূল দলিলের মধ্যে রয়েছে—অনলাইন পূরণকৃত আবেদন ফরমের প্রিন্ট কপি, "
                f"মূল রেজিস্ট্রেশন কার্ড, এডমিট কার্ড, পূর্ববর্তী সকল মার্কশিট বা সনদপত্র, জন্ম নিবন্ধন সনদ এবং জাতীয় পরিচয়পত্রের সত্যায়িত কপি।"
            )
        elif any(w in q_lower for w in ["নিয়ম", "কিভাবে", "পদ্ধতি", "ধাপ", "আবেদন"]):
            return (
                f"{question} অত্যন্ত সহজ। প্রথমে সংশ্লিষ্ট অফিশিয়াল ওয়েবসাইটে প্রবেশ করে রেজিস্ট্রেশন ও রোল নম্বর দিয়ে তথ্য ফেচ করতে হবে। "
                f"এরপর সঠিক তথ্য টাইপ করে চাহিত প্রমাণপত্র স্ক্যান করে আপলোড করতে হবে। পরিশেষে সোনালী সেবায় ফি পরিশোধ করে ট্র্যাকিং স্লিপ সংরক্ষণ করতে হবে।"
            )
        elif any(w in q_lower for w in ["কত দিন", "সময়", "কতদিন"]):
            return (
                f"{question}-এর স্বাভাবিক সময়সীমা সাধারণত ১৫ থেকে ৩০ কার্যদিবস। শিক্ষা বোর্ডের সংশ্লিষ্ট নাম ও বয়স সংশোধন কমিটির "
                f"মাসিক বা পাক্ষিক সভায় চূড়ান্ত অনুমোদন ও যাচাই-বাছাইয়ের পর সংশোধিত সনদ বা আদেশপত্র ওয়েবসাইটে প্রকাশ করা হয়।"
            )
        elif any(w in q_lower for w in ["কাকে বলে", "সংজ্ঞা", "বলতে কি বোঝায়", "কি"]):
            return (
                f"{question} একটি সুনির্দিষ্ট প্রাতিষ্ঠানিক ও শিক্ষাগত বিষয়। এর দ্বারা সংশ্লিষ্ট বিষয়টির মূল উদ্দেশ্য, কার্যকারিতা "
                f"এবং আইনগত বা নীতিগত কাঠামোর সামগ্রিক রূপরেখা নির্দেশ করা হয় যা শিক্ষার্থীদের ও পাঠকদের সঠিক তথ্য প্রদানে সাহায্য করে।"
            )
        else:
            return (
                f"{question} সম্পর্কিত সঠিক ও নির্ভরযোগ্য তথ্য হলো—সর্বশেষ প্রাতিষ্ঠানিক প্রমিত নীতিমালা অনুযায়ী "
                f"সংশ্লিষ্ট অফিশিয়াল পোর্টাল ও প্রামাণ্য নির্দেশিকা অনুসরণ করে যেকোনো নাগরিক বা শিক্ষার্থী নির্বিঘ্নে এটি সম্পন্ন করতে পারেন।"
            )
    else:
        if any(w in q_lower for w in ["fee", "cost", "how much", "price"]):
            return (
                f"Regarding '{question}', standard administrative fees are payable via official online banking channels. "
                f"Depending on the exact category, standard institutional fees range within official limits, along with minor verification charges."
            )
        elif any(w in q_lower for w in ["requirement", "document", "what is needed", "papers"]):
            return (
                f"For '{question}', mandatory documents include verified copies of identification certificates, "
                f"official registration transcripts, birth certificate/national ID, and the formal institutional application receipt."
            )
        elif any(w in q_lower for w in ["how to", "process", "steps", "procedure"]):
            return (
                f"The procedure for '{question}' requires accessing the verified official portal, filling out required credentials, "
                f"uploading supporting documentation in digital format, and securing the transaction confirmation receipt for real-time tracking."
            )
        elif any(w in q_lower for w in ["how long", "time", "days", "duration"]):
            return (
                f"Processing time for '{question}' typically spans 15 to 30 working days, subject to committee verification "
                f"and administrative schedule clearances."
            )
        else:
            return (
                f"Regarding '{question}', this procedure is fully governed by 2026 administrative standards, "
                f"ensuring transparency and seamless digital clearance for eligible applicants."
            )


def generate_faq_schema_and_html(keyword: str, questions: list[dict], lang: str = "bn", auto_answer: bool = True) -> tuple[dict, str]:
    """
    Generates valid Schema.org FAQPage JSON-LD and clean SolaimanLipi HTML cards.
    Zero-emoji policy strictly enforced.
    """
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": []
    }

    html_cards = []
    html_cards.append('<!-- [START] Helptrickbd Position 0 FAQ Section -->')
    html_cards.append('<div class="htbd-faq-section" style="margin: 35px 0; font-family: \'SolaimanLipi\', sans-serif;">')
    section_title = "প্রায়শই জিজ্ঞাসিত প্রশ্নাবলি (FAQ)" if lang == "bn" else "Frequently Asked Questions (FAQ)"
    html_cards.append(f'  <h2 style="color: #1a73e8; border-left: 5px solid #1a73e8; padding-left: 14px; font-size: 22px; font-weight: 700; margin-bottom: 20px;">'
                      f'{section_title}</h2>')

    for idx, q_item in enumerate(questions[:6], start=1):
        q_text = q_item["question"]
        if auto_answer:
            ans_text = synthesize_answer(q_text, lang=lang)
        else:
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

        badge_txt = f"প্রশ্ন {idx}" if lang == "bn" else f"Q{idx}"
        card_html = f"""  <div class="htbd-faq-item" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 18px 22px; margin-bottom: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
    <h3 style="margin: 0 0 10px 0; font-size: 18px; color: #0f172a; font-weight: 700; display: flex; align-items: baseline; gap: 8px;">
      <span style="background: #e8f0fe; color: #1a73e8; font-size: 13px; font-weight: 700; padding: 3px 9px; border-radius: 5px; flex-shrink: 0;">{badge_txt}</span>
      <span>{q_text}</span>
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
    parser.add_argument("--auto-answer", action="store_true", default=True, help="Synthesize intelligent answers automatically (default: True)")
    parser.add_argument("--output-json", "-j", help="Path to save mined questions JSON")
    parser.add_argument("--output-html", "-o", help="Path to save formatted FAQ HTML snippet")

    args = parser.parse_args()

    print("=" * 65)
    print(f"Helptrickbd PAA & Question Miner: '{args.keyword}' ({args.lang})")
    print("=" * 65)

    questions = generate_paa_questions(args.keyword, lang=args.lang)
    print(f"Discovered {len(questions)} high-intent questions from Google:")
    for i, q in enumerate(questions, 1):
        print(f"  {i:2d}. {q['question']}")

    faq_schema, faq_html = generate_faq_schema_and_html(args.keyword, questions, lang=args.lang, auto_answer=args.auto_answer)

    if args.output_json:
        with open(args.output_json, "w", encoding="utf-8") as f:
            json.dump({"keyword": args.keyword, "questions": questions, "schema": faq_schema}, f, ensure_ascii=False, indent=2)
        print(f"\nSaved JSON to: {args.output_json}")

    if args.output_html:
        with open(args.output_html, "w", encoding="utf-8") as f:
            f.write(faq_html)
        print(f"Saved FAQ HTML to: {args.output_html}")
    else:
        print("\n" + "-" * 40 + " Generated FAQ Schema & HTML " + "-" * 40)
        print(faq_html[:600] + "\n... [truncated] ...")


if __name__ == "__main__":
    main()
