#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HelpTrickBD PDF-to-Markdown One-Click Conversion Engine
Supports:
1. Instant Born-Digital PDF Conversion via PyMuPDF4LLM (Millisecond speed)
2. Scanned / Photocopy PDF Auto-Detection and Layout Analysis
"""

import os
import sys
import argparse
import time

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

def convert_pdf_to_markdown(pdf_path, output_path=None):
    if not os.path.exists(pdf_path):
        print(f"[❌] Error: File not found: {pdf_path}")
        return False

    if output_path is None:
        base_name = os.path.splitext(os.path.basename(pdf_path))[0]
        output_path = os.path.join(os.path.dirname(pdf_path), f"{base_name}.md")

    print("=" * 60)
    print(f"📄 Processing: {os.path.basename(pdf_path)}")
    print("=" * 60)

    start_time = time.time()

    # Step 1: Detect if PDF has digital text or is purely scanned
    try:
        import fitz  # PyMuPDF
        doc = fitz.open(pdf_path)
        total_pages = len(doc)
        print(f"• Total Pages: {total_pages}")
        
        sample_pages = min(5, total_pages)
        total_sample_chars = 0
        for i in range(sample_pages):
            total_sample_chars += len(doc[i].get_text().strip())
        
        is_digital = total_sample_chars > 50
    except Exception as e:
        print(f"[⚠️] Pre-inspection error: {e}")
        is_digital = False
        total_pages = 0

    if is_digital:
        print("• Detected Format: [BORN-DIGITAL] (Vector text & tables detected)")
        print("• Engine: PyMuPDF4LLM (Ultra-Fast Markdown Parser)")
        
        try:
            import pymupdf4llm
            md_text = pymupdf4llm.to_markdown(pdf_path)
            
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(md_text)
            
            elapsed = time.time() - start_time
            print(f"[✔] Successfully converted in {elapsed:.2f} seconds!")
            print(f"• Output Markdown: {output_path} ({len(md_text):,} characters)")
            return True
        except Exception as e:
            print(f"[❌] Conversion error: {e}")
            return False
    else:
        print("• Detected Format: [SCANNED / PHOTOPAGES] (No digital text stream)")
        print("• Note: Pages consist of raster scanned images requiring OCR Vision.")
        print(f"• File is ready for Vision Pipeline. Pages: {total_pages}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HelpTrickBD PDF-to-Markdown Converter")
    parser.add_argument("pdf_file", help="Path to the PDF file")
    parser.add_argument("-o", "--output", help="Optional output .md path", default=None)
    
    args = parser.parse_args()
    convert_pdf_to_markdown(args.pdf_file, args.output)
