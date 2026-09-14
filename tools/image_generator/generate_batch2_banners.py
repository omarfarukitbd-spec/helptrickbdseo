#!/usr/bin/env python3
"""
Generate 10 high-res 16:9 featured banners for Batch 2 posts
"""

import os
import sys

sys.path.append(os.path.dirname(__file__))
from render_banner import render_banner

BATCH_2_BANNERS = [
    {
        "filename": "certificate-correction-banner.png",
        "category_badge": "📄 শিক্ষাবোর্ড ও সনদপত্র গাইড",
        "title": "ঘরে বসেই সার্টিফিকেট নাম ও বয়স সংশোধনের সঠিক নিয়ম (২০২৬)",
        "subtitle": "জেএসসি, এসএসসি ও এইচএসসি সার্টিফিকেটের ভুল সংশোধনের পূর্ণাঙ্গ অনলাইন আবেদন পদ্ধতি",
        "features": ["📌 ১. প্রয়োজনীয় কাগজপত্র তালিকা", "📊 বোর্ড ফি ও প্রক্রিয়াকরণ সময়", "📝 হলফনামা ও পত্রিকার বিজ্ঞাপন", "⚡ শতভাগ নির্ভুল গাইডলাইন"],
        "gradient_colors": "linear-gradient(135deg, #0d47a1 0%, #1565c0 50%, #00838f 100%)",
        "accent_color": "#ffca28"
    },
    {
        "filename": "ssc-exam-instructions-banner.png",
        "category_badge": "🎯 এসএসসি ও সমমান পরীক্ষা ২০২৬",
        "title": "এসএসসি পরীক্ষার্থীদের জন্য জরুরি নিয়মাবলি ও নির্দেশিকা (২০২৬)",
        "subtitle": "ওএমআর শিট পূরণ, সময় ব্যবস্থাপনা, পরীক্ষার হলের সতর্কতা ও জিপিএ ৫ পাওয়ার কৌশল",
        "features": ["📌 ১. ওএমআর পূরণের নিয়ম", "📊 বিভাগভিত্তিক সময় বণ্টন", "📝 পরীক্ষার হলের নিয়মাবলি", "⚡ গোল্ডেন এ+ কৌশল"],
        "gradient_colors": "linear-gradient(135deg, #bf360c 0%, #d84315 50%, #f4511e 100%)",
        "accent_color": "#ffe082"
    },
    {
        "filename": "hason-raja-biography-banner.png",
        "category_badge": "🎶 বাংলা সাহিত্য ও লোকসঙ্গীত",
        "title": "মরমী কবি হাসন রাজার জীবনী, দর্শন ও অমর গানের রূপরেখা",
        "subtitle": "দেহতত্ত্ব, আত্মশুদ্ধি, বাউল দর্শন ও বাংলা লোকসাহিত্যে হাসন রাজার কালজয়ী অবদান",
        "features": ["📌 ১. মরমী জীবন দর্শন", "📊 হাসন উদাস ও বিখ্যাত গান", "📝 বোর্ড পরীক্ষার মডেল উত্তর", "⚡ সংস্করণ ২০২৬"],
        "gradient_colors": "linear-gradient(135deg, #3e2723 0%, #4e342e 50%, #5d4037 100%)",
        "accent_color": "#ffcc80"
    },
    {
        "filename": "livestock-research-institute-banner.png",
        "category_badge": "🐄 প্রাণিসম্পদ ও কৃষি গবেষণা",
        "title": "বাংলাদেশ প্রাণিসম্পদ গবেষণা ইনস্টিটিউট (BLRI): কার্যক্রম ও ভূমিকা",
        "subtitle": "উন্নত জাতের পশুপাখি উদ্ভাবন, টিকা উৎপাদন, গ্রামীণ অর্থনীতি ও কর্মসংস্থান সহায়িকা",
        "features": ["📌 ১. বিএলআরআই-এর উদ্ভাবন", "📊 মাংস ও দুগ্ধ উৎপাদন প্রযুক্তি", "📝 বিসিএস কৃষি ও ভাইভা", "⚡ সংস্করণ ২০২৬"],
        "gradient_colors": "linear-gradient(135deg, #1b5e20 0%, #2e7d32 50%, #388e3c 100%)",
        "accent_color": "#c8e6c9"
    },
    {
        "filename": "vidyasagar-social-reform-banner.png",
        "category_badge": "📜 সমাজ সংস্কার ও বাংলা গদ্য",
        "title": "সমাজ সংস্কার ও বাংলা সাহিত্যে ঈশ্বরচন্দ্র বিদ্যাসাগরের অবদান",
        "subtitle": "বিধবা বিবাহ আইন প্রবর্তন, নারী শিক্ষা বিস্তার ও বাংলা গদ্যের জনক হিসেবে অমর কীর্তি",
        "features": ["📌 ১. বিধবা বিবাহ আন্দোলন ১৮৫৬", "📊 নারী শিক্ষার অগ্রদূত", "📝 বিসিএস ও বিশ্ববিদ্যালয় স্পেশাল", "⚡ সংস্করণ ২০২৬"],
        "gradient_colors": "linear-gradient(135deg, #311b92 0%, #4527a0 50%, #512da8 100%)",
        "accent_color": "#b39ddb"
    },
    {
        "filename": "population-change-factors-banner.png",
        "category_badge": "📊 ভূগোল ও সমাজতত্ত্ব",
        "title": "জনসংখ্যা পরিবর্তনের কারণ, প্রভাব ও প্রধান নিয়ামকসমূহ (২০২৬)",
        "subtitle": "জন্মহার, মৃত্যুহার, অভিবাসন, ডেমোগ্রাফিক ডিভিডেন্ড ও বাংলাদেশের জনসংখ্যা সংকট",
        "features": ["📌 ১. পরিবর্তনের ৩টি প্রধান নিয়ামক", "📊 মালথাসের জনসংখ্যা তত্ত্ব", "📝 বিসিএস ও অনার্স গাইড", "⚡ সংস্করণ ২০২৬"],
        "gradient_colors": "linear-gradient(135deg, #004d40 0%, #00695c 50%, #00796b 100%)",
        "accent_color": "#80cbc4"
    },
    {
        "filename": "reserved-women-seats-banner.png",
        "category_badge": "🏛️ বাংলাদেশ সংবিধান ও সংসদ",
        "title": "জাতীয় সংসদে নারীদের সংরক্ষিত আসন: গুরুত্ব, যৌক্তিকতা ও বিতর্ক",
        "subtitle": "সংবিধানের ৬৫(৩) অনুচ্ছেদ, ৫০টি সংরক্ষিত আসন ও সরাসরি নির্বাচনের দাবি বিশ্লেষণ",
        "features": ["📌 ১. সাংবিধানিক পটভূমি", "📊 সংরক্ষিত আসনের বিবর্তন ছক", "📝 বিসিএস ও রাষ্ট্রবিজ্ঞান গাইড", "⚡ সংস্করণ ২০২৬"],
        "gradient_colors": "linear-gradient(135deg, #880e4f 0%, #ad1457 50%, #c2185b 100%)",
        "accent_color": "#f8bbd0"
    },
    {
        "filename": "child-socialization-banner.png",
        "category_badge": "👶 সমাজবিজ্ঞান ও শিশু বিকাশ",
        "title": "শিশুর সামাজিকীকরণ প্রক্রিয়া ও খেলার সাথীদের ভূমিকা (২০২৬)",
        "subtitle": "পরিবার, বিদ্যালয়, খেলার দল ও ডিজিটাল মিডিয়ার প্রভাবের পূর্ণাঙ্গ সমাজতাত্ত্বিক বিশ্লেষণ",
        "features": ["📌 ১. সামাজিকীকরণের মাধ্যমসমূহ", "📊 সমবয়সী দলের ইতিবাচক প্রভাব", "📝 অনার্স ও সমাজবিজ্ঞান হ্যান্ডনোট", "⚡ সংস্করণ ২০২৬"],
        "gradient_colors": "linear-gradient(135deg, #e65100 0%, #ef6c00 50%, #f57c00 100%)",
        "accent_color": "#ffe0b2"
    },
    {
        "filename": "computer-definition-history-banner.png",
        "category_badge": "💻 তথ্য ও যোগাযোগ প্রযুক্তি (ICT)",
        "title": "কম্পিউটার কাকে বলে? সংজ্ঞা, ইতিহাস, বৈশিষ্ট্য ও প্রজন্ম (২০২৬)",
        "subtitle": "এবাকাস থেকে আধুনিক সুপার কম্পিউটার ও কৃত্রিম বুদ্ধিমত্তা: এইচএসসি ও বিসিএস আইসিটি",
        "features": ["📌 ১. কম্পিউটারের মৌলিক গঠন", "📊 ১ম থেকে ৫ম প্রজন্ম তুলনামূলক ছক", "📝 বিসিএস ও জব প্রিলি স্পেশাল", "⚡ সংস্করণ ২০২৬"],
        "gradient_colors": "linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0284c7 100%)",
        "accent_color": "#38bdf8"
    },
    {
        "filename": "namta-1-to-20-banner.png",
        "category_badge": "🔢 প্রাথমিক ও মৌলিক গণিত",
        "title": "নামতা ১ থেকে ২০ পর্যন্ত: সহজে মুখস্থ করার কৌশল ও চার্ট (২০২৬)",
        "subtitle": "বাংলা ও ইংরেজিতে ১ থেকে ২০-এর গুণের নামতা, ম্যাজিক ট্রিকস ও প্র্যাকটিস শিট",
        "features": ["📌 ১. ১ থেকে ২০ পূর্ণাঙ্গ চার্ট", "📊 সহজে মনে রাখার গণিত কৌশল", "📝 প্রাইমারি ও জব ম্যাথ ফাউন্ডেশন", "⚡ সংস্করণ ২০২৬"],
        "gradient_colors": "linear-gradient(135deg, #4a148c 0%, #6a1b9a 50%, #8e24aa 100%)",
        "accent_color": "#ffd54f"
    }
]

def main():
    print(f"Generating {len(BATCH_2_BANNERS)} banners for Batch 2...")
    for b in BATCH_2_BANNERS:
        render_banner(
            filename=b["filename"],
            category_badge=b["category_badge"],
            title=b["title"],
            subtitle=b["subtitle"],
            features=b["features"],
            gradient_colors=b["gradient_colors"],
            accent_color=b["accent_color"]
        )
    print("Batch 2 banners generated successfully!")

if __name__ == "__main__":
    main()
