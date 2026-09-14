#!/usr/bin/env python3
"""
HelpTrickBD PDF Content Extractor & Normalizer
Extracts clean, structured text and chapters from academic PDFs, notes, and books.

Usage:
    python pdf_extractor.py --pdf input_pdfs/sample.pdf
    python pdf_extractor.py --pdf input_pdfs/sample.pdf --start-page 1 --end-page 10
"""

import argparse
import os
import re
import sys

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

try:
    import pdfplumber
    import pypdf
except ImportError:
    print("[!] Missing pypdf or pdfplumber. Run: pip install pypdf pdfplumber")
    sys.exit(1)


def clean_extracted_text(raw_text):
    """Cleans up PDF extraction artifacts, line breaks, and whitespace."""
    if not raw_text:
        return ""
    
    # Remove multiple sequential spaces
    cleaned = re.sub(r"[ \t]+", " ", raw_text)
    # Fix broken hyphenated words across lines
    cleaned = re.sub(r"(\w+)-\n(\w+)", r"\1\2", cleaned)
    # Normalize multiple linebreaks
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.strip()


def extract_pdf_content(pdf_path, start_page=1, end_page=None, output_txt=None):
    if not os.path.exists(pdf_path):
        print(f"[ERROR] PDF file not found: {pdf_path}")
        return None

    print(f"[*] Opening PDF: {pdf_path} ...")
    extracted_pages = []
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            total_pages = len(pdf.pages)
            print(f"[*] Total Pages in PDF: {total_pages}")
            
            end = min(end_page, total_pages) if end_page else total_pages
            start = max(1, start_page)

            for page_num in range(start - 1, end):
                page = pdf.pages[page_num]
                text = page.extract_text() or ""
                cleaned = clean_extracted_text(text)
                if cleaned:
                    extracted_pages.append({
                        "page_number": page_num + 1,
                        "text": cleaned
                    })
                print(f"    Extracted page {page_num + 1}/{end} ({len(cleaned.split())} words)")

    except Exception as e:
        print(f"[!] pdfplumber extraction failed: {e}. Falling back to pypdf...")
        try:
            reader = pypdf.PdfReader(pdf_path)
            total_pages = len(reader.pages)
            end = min(end_page, total_pages) if end_page else total_pages
            start = max(1, start_page)
            for page_num in range(start - 1, end):
                text = reader.pages[page_num].extract_text() or ""
                cleaned = clean_extracted_text(text)
                if cleaned:
                    extracted_pages.append({
                        "page_number": page_num + 1,
                        "text": cleaned
                    })
        except Exception as e2:
            print(f"[ERROR] PDF extraction failed completely: {e2}")
            return None

    all_text = "\n\n--- [PAGE BREAK] ---\n\n".join([p["text"] for p in extracted_pages])
    total_words = len(all_text.split())
    print(f"\n[OK] Extracted {len(extracted_pages)} pages, total ~{total_words} words.")

    if not output_txt:
        base_name = os.path.splitext(os.path.basename(pdf_path))[0]
        output_txt = os.path.join(os.path.dirname(pdf_path), f"{base_name}_extracted.txt")

    with open(output_txt, "w", encoding="utf-8") as f:
        f.write(all_text)

    print(f"[OK] Saved clean text to: {output_txt}")
    return output_txt


def main():
    parser = argparse.ArgumentParser(description="HelpTrickBD PDF Content Extractor")
    parser.add_argument("--pdf", required=True, help="Path to source PDF file")
    parser.add_argument("--start-page", type=int, default=1, help="Start page number (1-indexed)")
    parser.add_argument("--end-page", type=int, default=None, help="End page number")
    parser.add_argument("--output", help="Path to save extracted plain text")

    args = parser.parse_args()
    extract_pdf_content(args.pdf, args.start_page, args.end_page, args.output)


if __name__ == "__main__":
    main()
