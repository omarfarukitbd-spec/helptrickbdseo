#!/usr/bin/env python3
"""
HelpTrickBD - Generate 5 Category Sample Thumbnails
Demonstrates the 1:1 category mapping using the user-provided backgrounds in Thumbnail BG/
"""

import os
import sys

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

sys.path.append(os.path.dirname(__file__))
from thumbnail_generator import generate_thumbnail

SAMPLES = [
    {
        "category": "Political Science",
        "title": "পুরুষতন্ত্র কাকে বলে? সমাজতাত্ত্বিক সংজ্ঞা, উৎপত্তি, বৈশিষ্ট্য ও প্রভাব",
        "subtitle": "অনার্স রাষ্ট্রবিজ্ঞান ও সমাজবিজ্ঞান পূর্ণাঙ্গ হ্যান্ডনোট",
        "filename": "sample_political_science.png",
    },
    {
        "category": "Islamic Article",
        "title": "আল্লাহুম্মা সাল্লি আলা সাইয়্যিদিনা মুহাম্মাদ: দরূদ শরীফের ফজিলত ও ক্বাসিদা",
        "subtitle": "সহীহ হাদিসের সনদ, আরবি অর্থ ও পূর্ণাঙ্গ বাংলা লিরিক্স",
        "filename": "sample_islamic_article.png",
    },
    {
        "category": "Education Guide",
        "title": "Hason Raja: Class 6 English Seen Comprehension & Study Guide",
        "subtitle": "Text Analysis, Vocabulary Grid, MCQs & Short Questions",
        "filename": "sample_education_guide.png",
    },
    {
        "category": "Job Study Article",
        "title": "বিসিএস ও সরকারি চাকরির প্রস্তুতি: সাধারণ জ্ঞান ও স্পেশাল মডেল টেস্ট",
        "subtitle": "প্রিলিমিনারি ও লিখিত পরীক্ষার সিলেবাসভিত্তিক পূর্ণাঙ্গ গাইডলাইন",
        "filename": "sample_job_study.png",
    },
    {
        "category": "ICT Guide",
        "title": "কম্পিউটারের প্রজন্ম: ১ম থেকে ৫ম প্রজন্মের প্রযুক্তিগত পূর্ণাঙ্গ ইতিহাস",
        "subtitle": "ভ্যাকুয়াম টিউব থেকে কৃত্রিম বুদ্ধিমত্তা (AI) প্রযুক্তির তুলনা",
        "filename": "sample_ict_guide.png",
    },
]


def main():
    print("=" * 70)
    print("🚀 Generating 5 Category Sample Thumbnails with Custom Backgrounds...")
    print("=" * 70)

    generated_paths = []
    for s in SAMPLES:
        path = generate_thumbnail(
            title=s["title"],
            category=s["category"],
            subtitle=s["subtitle"],
            output_filename=s["filename"],
        )
        generated_paths.append(path)

    print("=" * 70)
    print(f"🎉 Successfully Generated {len(generated_paths)} Sample Thumbnails!")
    for p in generated_paths:
        print(f" - {p}")
    print("=" * 70)


if __name__ == "__main__":
    main()
