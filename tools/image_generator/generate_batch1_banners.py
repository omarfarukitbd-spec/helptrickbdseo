#!/usr/bin/env python3
"""
Generate all 16:9 featured banners for Batch 1 posts using render_banner
"""

import os
import sys

sys.path.append(os.path.dirname(__file__))
from render_banner import render_banner

BATCH_1_BANNERS = [
    {
        "filename": "patriarchy-definition-impact-banner.png",
        "category_badge": "🎓 সমাজবিজ্ঞান ও রাষ্ট্রবিজ্ঞান",
        "title": "পিতৃতন্ত্র কাকে বলে? সংজ্ঞা, বৈশিষ্ট্য, প্রভাব ও নারীবাদী তত্ত্ব",
        "subtitle": "অনার্স ও মাস্টার্স সমাজবিজ্ঞান এবং রাষ্ট্রবিজ্ঞান বিষয়ের পূর্ণাঙ্গ স্পেশাল হ্যান্ডনোট",
        "features": ["📌 ১. প্রামাণ্য সংজ্ঞা ও পরিধি", "📊 সামাজিক কাঠামো ও প্রভাব", "📝 বিসিএস মডেল টেস্ট", "⚡ সংস্করণ ২০২৬"],
        "gradient_colors": "linear-gradient(135deg, #2e0854 0%, #4a148c 50%, #6a1b9a 100%)",
        "accent_color": "#ffca28"
    },
    {
        "filename": "ngos-womens-empowerment-banner.png",
        "category_badge": "🌱 সামাজিক উন্নয়ন ও অর্থনীতি",
        "title": "নারী ক্ষমতায়নে এনজিও (NGO)-এর ভূমিকা ও অবদান",
        "subtitle": "ক্ষুদ্রঋণ, নারীর আর্থ-সামাজিক সক্ষমতা বৃদ্ধি ও স্বাবলম্বী বাংলাদেশ গড়ার রূপরেখা",
        "features": ["📌 ১. গ্রামীণ উন্নয়ন ও শিক্ষা", "📊 ক্ষুদ্রঋণের বাস্তব প্রভাব", "📝 বিসিএস ও ভাইভা প্রস্তুতি", "⚡ সংস্করণ ২০২৬"],
        "gradient_colors": "linear-gradient(135deg, #004d40 0%, #00695c 50%, #00897b 100%)",
        "accent_color": "#80cbc4"
    },
    {
        "filename": "womens-rights-movement-banner.png",
        "category_badge": "✊ ইতিহাস ও অধিকার আন্দোলন",
        "title": "নারী আন্দোলন: অস্তিত্ব রক্ষার লড়াই ও অধিকার প্রতিষ্ঠার ইতিহাস",
        "subtitle": "বেগম রোকেয়া থেকে সমকালীন ভোটাধিকার, সমতা ও আইনি সুরক্ষা আন্দোলনের রূপরেখা",
        "features": ["📌 ১. ঐতিহাসিক প্রেক্ষাপট", "📊 ৩টি তরঙ্গের আন্দোলন বিশ্লেষণ", "📝 অনার্স মডেল প্রশ্নোত্তর", "⚡ সংস্করণ ২০২৬"],
        "gradient_colors": "linear-gradient(135deg, #880e4f 0%, #ad1457 50%, #c2185b 100%)",
        "accent_color": "#f48fb1"
    },
    {
        "filename": "recent-nationalism-banner.png",
        "category_badge": "🌐 আন্তর্জাতিক সম্পর্ক ও রাষ্ট্রনীতি",
        "title": "সাম্প্রতিক জাতীয়তাবাদ বলতে কী বোঝায়? সংজ্ঞা, বিবর্তন ও রূপ",
        "subtitle": "বিশ্বায়ন বনাম উগ্র জাতীয়তাবাদ, ভূরাজনীতি ও বিশ্বশান্তির সমকালীন তাত্ত্বিক বিশ্লেষণ",
        "features": ["📌 ১. আধুনিক জাতীয়তাবাদের সংজ্ঞা", "📊 বিশ্বায়ন ও ভূরাজনীতি", "📝 বিসিএস ও অনার্স গাইড", "⚡ সংস্করণ ২০২৬"],
        "gradient_colors": "linear-gradient(135deg, #1a237e 0%, #0d47a1 50%, #01579b 100%)",
        "accent_color": "#4fc3f7"
    },
    {
        "filename": "recent-political-thought-banner.png",
        "category_badge": "📚 মাস্টার্স রাষ্ট্রবিজ্ঞান স্পেশাল",
        "title": "সাম্প্রতিক রাষ্ট্রচিন্তা ফাইনাল সুপার সাজেশন (২০২৬)",
        "subtitle": "জাতীয় বিশ্ববিদ্যালয় মাস্টার্স ও অনার্স শেষ বর্ষ পরীক্ষার ১০০% কমন মডেল হ্যান্ডনোট",
        "features": ["📌 ১. ক, খ ও গ-বিভাগ সাজেশন", "📊 বিগত ১০ বছরের প্রশ্ন বিশ্লেষণ", "📝 পূর্ণাঙ্গ উত্তর নির্দেশিকা", "⚡ শতভাগ কমন ২০২৬"],
        "gradient_colors": "linear-gradient(135deg, #bf360c 0%, #d84315 50%, #e64a19 100%)",
        "accent_color": "#ffcc80"
    },
    {
        "filename": "social-change-political-dev-banner.png",
        "category_badge": "📈 সমাজ পরিবর্তন ও উন্নয়ন তত্ত্ব",
        "title": "সামাজিক পরিবর্তন ও রাজনৈতিক উন্নয়ন: সুপার সাজেশন ও হ্যান্ডনোট",
        "subtitle": "নগরায়ন, আধুনিকায়ন তত্ত্ব ও গণতান্ত্রিক রূপান্তরের পূর্ণাঙ্গ অধ্যায়ভিত্তিক সমাধান",
        "features": ["📌 ১. আধুনিকায়ন ও উন্নয়ন তত্ত্ব", "📊 সামাজিক পরিবর্তনের প্রভাবক", "📝 মাস্টার্স ফাইনাল স্পেশাল", "⚡ সংস্করণ ২০২৬"],
        "gradient_colors": "linear-gradient(135deg, #263238 0%, #37474f 50%, #455a64 100%)",
        "accent_color": "#80d8ff"
    },
    {
        "filename": "bcs-job-preparation-guide-banner.png",
        "category_badge": "🎯 বিসিএস ও সরকারি চাকরি প্রস্তুতি",
        "title": "চাকরি ও বিসিএস প্রিলিমিনারি প্রস্তুতির সহজ ও পূর্ণাঙ্গ গাইডলাইন",
        "subtitle": "প্রথমবারই প্রিলি ও লিখিত পাসের প্রমাণিত রুটিন, বইয়ের তালিকা ও সময় ব্যবস্থাপনা কৌশল",
        "features": ["📌 ১. বিষয়ভিত্তিক নম্বর বণ্টন", "📊 ২০০ নম্বরের পূর্ণাঙ্গ স্ট্র্যাটেজি", "📝 বইয়ের তালিকা ও রুটিন", "⚡ সফলতার স্পেশাল রোডম্যাপ"],
        "gradient_colors": "linear-gradient(135deg, #0d47a1 0%, #1976d2 50%, #0288d1 100%)",
        "accent_color": "#ffd54f"
    },
    {
        "filename": "political-science-book-list-banner.png",
        "category_badge": "📖 অনার্স রাষ্ট্রবিজ্ঞান বুক লিস্ট",
        "title": "অনার্স রাষ্ট্রবিজ্ঞান ১ম থেকে ৪র্থ বর্ষের রেফারেন্স বইয়ের পূর্ণাঙ্গ তালিকা",
        "subtitle": "জাতীয় বিশ্ববিদ্যালয় ও ঢাকা বিশ্ববিদ্যালয় অধিভুক্ত ৭ কলেজের সেরা লেখকদের বইয়ের তালিকা",
        "features": ["📌 ১. ১ম থেকে ৪র্থ বর্ষের সিলেবাস", "📊 সেরা লেখক ও প্রকাশনী তালিকা", "📝 ভালো ফলাফলের স্ট্র্যাটেজি", "⚡ সংস্করণ ২০২৬"],
        "gradient_colors": "linear-gradient(135deg, #1b5e20 0%, #2e7d32 50%, #388e3c 100%)",
        "accent_color": "#a5d6a7"
    },
    {
        "filename": "modern-political-thought-sheet-banner.png",
        "category_badge": "📝 মাস্টার্স রাষ্ট্রবিজ্ঞান প্রশ্নব্যাংক",
        "title": "আধুনিক রাষ্ট্রচিন্তা বিগত সালের প্রশ্ন সমাধান ও উত্তরপত্র হ্যান্ডনোট",
        "subtitle": "জাতীয় বিশ্ববিদ্যালয় অনার্স ও মাস্টার্স পরীক্ষার প্রশ্ন ও সর্বোচ্চ নম্বর পাওয়ার সাজানো উত্তর",
        "features": ["📌 ১. সাজানো বর্ণনামূলক উত্তর", "📊 ম্যাকিয়াভেলি, হব্‌স ও লক", "📝 পরীক্ষায় A+ পাওয়ার কৌশল", "⚡ সংস্করণ ২০২৬"],
        "gradient_colors": "linear-gradient(135deg, #3e2723 0%, #4e342e 50%, #5d4037 100%)",
        "accent_color": "#ffab91"
    }
]

def main():
    print("Generating 9 banners for Batch 1...")
    for b in BATCH_1_BANNERS:
        render_banner(
            filename=b["filename"],
            category_badge=b["category_badge"],
            title=b["title"],
            subtitle=b["subtitle"],
            features=b["features"],
            gradient_colors=b["gradient_colors"],
            accent_color=b["accent_color"]
        )
    print("All 9 banners generated successfully!")

if __name__ == "__main__":
    main()
