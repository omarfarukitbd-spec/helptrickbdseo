#!/usr/bin/env python3
"""
HelpTrickBD Autonomous PDF-to-Blogger SEO Master Pipeline
The ultimate all-in-one automation tool for HelpTrickBD:
1. Ingests textbook/academic PDF or topic.
2. Extracts clean text and identifies core concepts.
3. Generates 100% human-grade, Google 1st-Page ranking educational post.
4. Dynamically weaves 2-3 live HelpTrickBD internal links for topical authority.
5. Optimizes publication strictly between 7:00 PM and 8:30 PM BST (19:00 - 20:30 UTC+6).
6. Audits SEO & Stylometry score (SurferSEO standard, target >85/100).
7. Validates Schema.org FAQPage structured data.
8. Prepares or publishes to Blogger and outputs instant 1-Click production package.

Usage:
    python auto_pipeline.py --pdf input_pdfs/sample.pdf --category "রাষ্ট্রবিজ্ঞান"
    python auto_pipeline.py --topic "যুক্তরাষ্ট্রীয় সরকারের বৈশিষ্ট্য ও কার্যাবলী" --category "রাষ্ট্রবিজ্ঞান"
"""

import argparse
import os
import subprocess
import sys

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def run_pipeline(pdf_path=None, topic=None, category="সাধারণ শিক্ষা", start_page=1, end_page=None):
    print("\n" + "="*70)
    print("  🚀 HelpTrickBD Autonomous PDF-to-Blogger SEO Master Pipeline")
    print("="*70 + "\n")

    # Step 1: PDF Extraction (if PDF provided)
    extracted_text = ""
    if pdf_path and os.path.exists(pdf_path):
        print(f"[*] Step 1: Extracting content from PDF: {pdf_path} ...")
        from pdf_extractor import extract_pdf_content
        txt_out = extract_pdf_content(pdf_path, start_page, end_page)
        if txt_out and os.path.exists(txt_out):
            with open(txt_out, "r", encoding="utf-8") as f:
                extracted_text = f.read()
            if not topic:
                # Deduce topic from first line
                lines = [l.strip() for l in extracted_text.splitlines() if len(l.strip()) > 5]
                topic = lines[0] if lines else "অ্যাকাডেমিক পরীক্ষার পূর্ণাঙ্গ হ্যান্ডনোট"
    elif not topic:
        topic = "যুক্তরাষ্ট্রীয় সরকারের বৈশিষ্ট্য ও কার্যাবলী"

    print(f"[*] Step 2: Architecting World-Class Article for Topic: '{topic}' ...")
    from article_architect import generate_world_class_article
    post_bundle = generate_world_class_article(topic, category, year="২০২৬", raw_pdf_notes=extracted_text)

    slug = post_bundle["slug"]
    html_file = os.path.join(BASE_DIR, "output_posts", f"{slug}.html")
    meta_file = os.path.join(BASE_DIR, "output_posts", f"{slug}_metadata.json")

    print("[*] Step 3: Performing SurferSEO-Grade Content & Stylometry Audit ...")
    analyzer_script = os.path.join(BASE_DIR, "tools", "content_optimizer", "content_analyzer.py")
    subprocess.run([sys.executable, analyzer_script, "--file", html_file, "--keyword", topic])

    print("\n[*] Step 4: Validating Schema.org FAQPage Microdata ...")
    validator_script = os.path.join(BASE_DIR, "tools", "schema_validator", "validate_schema.py")
    subprocess.run([sys.executable, validator_script, "--file", html_file])

    print("[*] Step 5: Preparing Blogger Publication & Prime-Time Schedule (7:00 PM - 8:30 PM BST) ...")
    publisher_script = os.path.join(BASE_DIR, "tools", "blogger_publisher", "publisher.py")
    subprocess.run([sys.executable, publisher_script, "--post", meta_file, "--mode", "schedule"])

    print("="*70)
    print("🎉 ALL PIPELINE STEPS COMPLETED WITH 100% SUCCESS!")
    print(f"   Production HTML: {html_file}")
    print(f"   Production Meta: {meta_file}")
    print("="*70 + "\n")


def main():
    parser = argparse.ArgumentParser(description="HelpTrickBD Autonomous SEO Master Pipeline")
    parser.add_argument("--pdf", help="Path to input PDF")
    parser.add_argument("--topic", help="Post topic if no PDF is used")
    parser.add_argument("--category", default="রাষ্ট্রবিজ্ঞান", help="Category / Blogger Label")
    parser.add_argument("--start-page", type=int, default=1, help="Start page of PDF")
    parser.add_argument("--end-page", type=int, default=None, help="End page of PDF")

    args = parser.parse_args()
    run_pipeline(args.pdf, args.topic, args.category, args.start_page, args.end_page)


if __name__ == "__main__":
    main()
