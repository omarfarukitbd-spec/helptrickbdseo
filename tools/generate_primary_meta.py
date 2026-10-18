import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output_posts")
os.makedirs(OUTPUT_DIR, exist_ok=True)

html_path = os.path.join(OUTPUT_DIR, "primary-scholarship-exam-routine-2026.html")
meta_path = os.path.join(OUTPUT_DIR, "primary-scholarship-exam-routine-2026_meta.json")

# Metadata
meta_data = {
    "title": "প্রাথমিক বৃত্তি পরীক্ষার রুটিন 2026: পরীক্ষার মানবণ্টন ও Best Complete Guide (PDF সহ)",
    "slug": "primary-scholarship-exam-routine-2026",
    "categories": [
        "Education Guide"
    ],
    "tags": [
        "প্রাথমিক বৃত্তি পরীক্ষা ২০২৬",
        "Class 5 Scholarship",
        "প্রাথমিক শিক্ষা অধিদপ্তর",
        "Primary Scholarship Routine 2026",
        "বৃত্তি পরীক্ষার মানবণ্টন"
    ],
    "focus_keyword": "প্রাথমিক বৃত্তি পরীক্ষার রুটিন 2026, primary scholarship exam routine 2026",
    "meta_description": "প্রাথমিক বৃত্তি পরীক্ষার রুটিন 2026 ও সময়সূচি প্রকাশিত হয়েছে। ২০ ডিসেম্বর শুরু হওয়া পরীক্ষার মানবণ্টন, বিষয়ভিত্তিক সিলেবাস ও অফিসিয়াল PDF ডাউনলোড গাইডলাইন।",
    "banner_url": "https://www.helptrickbd.com/wp-content/uploads/2026/10/primary_scholarship_exam_routine_2026.webp",
    "banner_path": "assets/images/posts/primary_scholarship_exam_routine_2026.webp",
    "featured_media_id": 15902,
    "pdf_url": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/pdf/primary/primary_scholarship_exam_routine_2026.pdf",
    "pdf_path": "assets/pdf/primary/primary_scholarship_exam_routine_2026.pdf"
}

with open(meta_path, "w", encoding="utf-8") as f:
    json.dump(meta_data, f, ensure_ascii=False, indent=2)
print(f"[SUCCESS] Metadata saved: {meta_path}")
