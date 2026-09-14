#!/usr/bin/env python3
"""
Generate 10 high-res 16:9 featured banners for Batch 3 posts
"""

import os
import sys

sys.path.append(os.path.dirname(__file__))
from render_banner import render_banner

BATCH_3_BANNERS = [
    {
        "filename": "marhaba-qasida-banner.png",
        "category_badge": "🕌 ইসলামী সাহিত্য ও ক্বাসিদা",
        "title": "মারহাবা ইয়া মারহাবা ক্বাসিদা: তাৎপর্য, ব্যাখ্যা ও পূর্ণাঙ্গ লিরিক্স (২০২৬)",
        "subtitle": "মিলাদ মাহফিলের বিখ্যাত নাত-এ-রাসূল, আরবী-উর্দু শব্দের অর্থ ও ধর্মীয় ভাববস্তু",
        "features": ["📌 ১. ক্বাসিদার পটভূমি", "📊 নাতিয়া সাহিত্যের ইতিহাস", "📝 বিশুদ্ধ উচ্চারণ ও অর্থ", "⚡ পূর্ণাঙ্গ লিরিক্স ২০২৬"],
        "gradient_colors": "linear-gradient(135deg, #004d40 0%, #00695c 50%, #00796b 100%)",
        "accent_color": "#ffca28"
    },
    {
        "filename": "allah-allahu-qasida-banner.png",
        "category_badge": "🕌 সুফি সঙ্গীত ও আধ্যাত্মিকতা",
        "title": "আল্লাহ আল্লাহ আল্লাহু লা ইলাহা ইল্লা হু: যিকিরের মহিমা ও অর্থ (২০২৬)",
        "subtitle": "তাওহিদের গভীর তত্ত্ব, আত্মশুদ্ধি, সুফি সাধনার ঐতিহ্য ও পূর্ণাঙ্গ লিরিক্স হ্যান্ডনোট",
        "features": ["📌 ১. তাওহিদ ও যিকরুল্লাহ", "📊 আধ্যাত্মিক ভাববস্তু", "📝 বিশুদ্ধ পাঠ ও অর্থ", "⚡ সংস্করণ ২০২৬"],
        "gradient_colors": "linear-gradient(135deg, #1b5e20 0%, #2e7d32 50%, #388e3c 100%)",
        "accent_color": "#c8e6c9"
    },
    {
        "filename": "allahumma-salli-qasida-banner.png",
        "category_badge": "🕌 দুরুদ শরীফ ও ক্বাসিদা",
        "title": "আল্লাহুম্মা সাল্লি আলা সাইয়্যিদিনা মুহাম্মাদ: ফজিলত ও ক্বাসিদা হ্যান্ডনোট",
        "subtitle": "রাসূলুল্লাহ (সা.)-এর প্রতি দুরুদ ও সালাতের গুরুত্ব, সহীহ হাদিস ও পূর্ণাঙ্গ লিরিক্স",
        "features": ["📌 ১. দুরুদের ফজিলত ও হাদিস", "📊 শব্দের অর্থ ও ব্যাকরণ", "📝 মিলাদ মাহফিলের আদব", "⚡ সংস্করণ ২০২৬"],
        "gradient_colors": "linear-gradient(135deg, #0d47a1 0%, #1565c0 50%, #00838f 100%)",
        "accent_color": "#ffd54f"
    },
    {
        "filename": "milad-salatun-qasida-banner.png",
        "category_badge": "🕌 সালাত ও সালাম",
        "title": "সালাতুন ইয়া রাসুলুল্লাহ আলাইকুম: ঐতিহাসিক প্রেক্ষিত ও পূর্ণাঙ্গ লিরিক্স",
        "subtitle": "প্রিয় নবী (সা.)-এর প্রতি ভক্তি ও ভালোবাসার কালজয়ী নাতিয়া ক্বাসিদা ও শানে রিসালাত",
        "features": ["📌 ১. ঐতিহাসিক প্রেক্ষাপট", "📊 শানে রিসালাত তত্ত্ব", "📝 পূর্ণাঙ্গ নাতিয়া লিরিক্স", "⚡ সংস্করণ ২০২৬"],
        "gradient_colors": "linear-gradient(135deg, #311b92 0%, #4527a0 50%, #512da8 100%)",
        "accent_color": "#e1bee7"
    },
    {
        "filename": "computer-history-part2-banner.png",
        "category_badge": "💻 তথ্য ও যোগাযোগ প্রযুক্তি (ICT)",
        "title": "কম্পিউটারের ইতিহাস: এবাকাস থেকে ইন্টিগ্রেটেড সার্কিট (পার্ট-২)",
        "subtitle": "প্যাসকেলাইন, চার্লস ব্যাবেজের অ্যানালিটিক্যাল ইঞ্জিন, এনিয়াক ও ট্রানজিস্টর বিপ্লব",
        "features": ["📌 ১. আদি গণনাকারী যন্ত্র", "📊 আবিষ্কারের কালানুক্রমিক ছক", "📝 বিসিএস ও এইচএসসি আইসিটি", "⚡ সংস্করণ ২০২৬"],
        "gradient_colors": "linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0284c7 100%)",
        "accent_color": "#38bdf8"
    },
    {
        "filename": "computer-generations-part3-banner.png",
        "category_badge": "💻 তথ্য ও যোগাযোগ প্রযুক্তি (ICT)",
        "title": "কম্পিউটারের প্রজন্ম: ১ম থেকে ৫ম প্রজন্মের প্রযুক্তিগত তুলনা (পার্ট-৩)",
        "subtitle": "ভ্যাকুয়াম টিউব থেকে মাইক্রোপ্রসেসর ও কৃত্রিম বুদ্ধিমত্তা (AI): পূর্ণাঙ্গ স্টাডি গাইড",
        "features": ["📌 ১. হার্ডওয়্যার ও মেমোরি রূপান্তর", "📊 ৫টি প্রজন্মের তুলনামূলক ছক", "📝 বিসিএস প্রিলি স্পেশাল", "⚡ সংস্করণ ২০২৬"],
        "gradient_colors": "linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #4338ca 100%)",
        "accent_color": "#a5b4fc"
    },
    {
        "filename": "computer-types-part4-banner.png",
        "category_badge": "💻 তথ্য ও যোগাযোগ প্রযুক্তি (ICT)",
        "title": "কম্পিউটারের প্রকারভেদ: অ্যানালগ, ডিজিটাল, হাইব্রিড ও সুপার কম্পিউটার",
        "subtitle": "কাজের প্রকৃতি ও আকারভেদে কম্পিউটারের সম্পূর্ণ শ্রেণিবিভাগ ও বাস্তব উদাহরণ",
        "features": ["📌 ১. কাজের প্রকৃতিভিত্তিক ৩ ভাগ", "📊 আকারভিত্তিক ৪ ভাগ", "📝 বিসিএস ও জব স্পেশাল", "⚡ সংস্করণ ২০২৬"],
        "gradient_colors": "linear-gradient(135deg, #18181b 0%, #27272a 50%, #059669 100%)",
        "accent_color": "#34d399"
    },
    {
        "filename": "political-economy-banner.png",
        "category_badge": "📈 রাষ্ট্রবিজ্ঞান ও অর্থনীতি",
        "title": "রাজনৈতিক অর্থনীতি কাকে বলে? সংজ্ঞা, পরিধি ও তাত্ত্বিক কাঠামো (২০২৬)",
        "subtitle": "অ্যাডাম স্মিথ, ডেভিড রিকার্ডো, কার্ল মার্কস ও সমকালীন বৈশ্বিক রাজনৈতিক অর্থনীতি",
        "features": ["📌 ১. প্রামাণ্য সংজ্ঞা ও পরিধি", "📊 ক্লাসিক্যাল বনাম মার্কসীয় তত্ত্ব", "📝 অনার্স ও মাস্টার্স হ্যান্ডনোট", "⚡ সংস্করণ ২০২৬"],
        "gradient_colors": "linear-gradient(135deg, #3e2723 0%, #4e342e 50%, #5d4037 100%)",
        "accent_color": "#ffcc80"
    },
    {
        "filename": "industrial-nationalization-banner.png",
        "category_badge": "🏭 বাংলাদেশ অর্থনীতি ও শিল্প",
        "title": "বাংলাদেশে শিল্প জাতীয়করণের ইতিহাস, পটভূমি, সমস্যা ও প্রভাব (২০২৬)",
        "subtitle": "১৯৭২ সালের জাতীয়করণ আদেশ, পাট-বস্ত্র শিল্পের সংকট, বিরাষ্ট্রীয়করণ নীতি ও পর্যালোচনা",
        "features": ["📌 ১. জাতীয়করণের ঐতিহাসিক পটভূমি", "📊 পাট ও বস্ত্র শিল্পের সংকট", "📝 বিসিএস ও অর্থনীতি গাইড", "⚡ সংস্করণ ২০২৬"],
        "gradient_colors": "linear-gradient(135deg, #bf360c 0%, #d84315 50%, #e64a19 100%)",
        "accent_color": "#ffe082"
    },
    {
        "filename": "government-political-parties-banner.png",
        "category_badge": "🏛️ রাষ্ট্রবিজ্ঞান ও গণতন্ত্র",
        "title": "সরকার ও রাজনৈতিক দল: ধারণা, সম্পর্ক ও বাংলাদেশে গণতান্ত্রিক চর্চা (২০২৬)",
        "subtitle": "রাজনৈতিক দলের সংজ্ঞা, শ্রেণিবিভাগ, সুশাসনের অপরিহার্য ভূমিকা ও নির্বাচনী ব্যবস্থা",
        "features": ["📌 ১. রাজনৈতিক দলের মৌলিক কাজ", "📊 সরকার বনাম রাজনৈতিক দল ছক", "📝 বিসিএস ও অনার্স হ্যান্ডনোট", "⚡ সংস্করণ ২০২৬"],
        "gradient_colors": "linear-gradient(135deg, #0d47a1 0%, #1565c0 50%, #1976d2 100%)",
        "accent_color": "#ffca28"
    }
]

def main():
    print(f"Generating {len(BATCH_3_BANNERS)} banners for Batch 3...")
    for b in BATCH_3_BANNERS:
        render_banner(
            filename=b["filename"],
            category_badge=b["category_badge"],
            title=b["title"],
            subtitle=b["subtitle"],
            features=b["features"],
            gradient_colors=b["gradient_colors"],
            accent_color=b["accent_color"]
        )
    print("Batch 3 banners generated successfully!")

if __name__ == "__main__":
    main()
