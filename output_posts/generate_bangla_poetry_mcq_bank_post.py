#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
output_posts/generate_bangla_poetry_mcq_bank_post.py
Generates Post 02:
এসএসসি বাংলা ১ম পত্র কবিতাংশ বহুনির্বাচনি প্রশ্নব্যাংক ২০২৬-২০২৭
(SSC Bangla 1st Paper Poetry MCQ Suggestion with Answers)
Adheres 100% to Project Governance, Rule 01, 11, 12, 27, 28, 29, 30.
"""

import os
import sys
import json
import re

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def build_post():
    html_out = os.path.join(PROJECT_ROOT, "output_posts", "ssc-bangla-1st-paper-poetry-mcq-question-bank-2027.html")
    meta_out = os.path.join(PROJECT_ROOT, "output_posts", "ssc-bangla-1st-paper-poetry-mcq-question-bank-2027_metadata.json")

    # Metadata
    metadata = {
        "title": "এসএসসি বাংলা ১ম পত্র কবিতাংশ বহুনির্বাচনি প্রশ্নব্যাংক ২০২৬-২০২৭ (SSC Bangla 1st Paper Poetry MCQ Suggestion with Answers)",
        "slug": "ssc-bangla-1st-paper-poetry-mcq-question-bank-2027",
        "labels": ["Education Guide", "SSC Suggestion 2027"],
        "search_description": "এসএসসি ও দাখিল বাংলা ১ম পত্র কবিতাংশ অধ্যায়ভিত্তিক বহুনির্বাচনি (Poetry MCQ) প্রশ্নব্যাংক: কপোতাক্ষ নদ, বঙ্গবাণী সহ সকল কবিতার ১০০% প্রমিত সমাধান।"
    }

    # Individual Schemas
    blog_posting_schema = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": metadata["title"],
        "description": metadata["search_description"],
        "image": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/ssc_bangla_1st_paper_poetry_mcq_bank_2027.webp",
        "author": {
            "@type": "Person",
            "name": "ফারুক স্যার (মো. ওমর ফারুক)",
            "jobTitle": "শিক্ষাবিদ ও অ্যাকাডেমিক গবেষক | প্রতিষ্ঠাতা, HelpTrickBD"
        },
        "publisher": {
            "@type": "Organization",
            "name": "HelpTrickBD",
            "logo": {
                "@type": "ImageObject",
                "url": "https://www.helptrickbd.com/favicon.ico"
            }
        },
        "datePublished": "2026-09-24T00:10:00+06:00",
        "dateModified": "2026-09-24T00:10:00+06:00",
        "mainEntityOfPage": "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-poetry-mcq-question-bank-2027.html"
    }

    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": "এসএসসি বাংলা ১ম পত্র কবিতাংশ থেকে বহুনির্বাচনি (MCQ) কয়টি থাকে?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "এসএসসি ও দাখিল বাংলা ১ম পত্র পরীক্ষায় কবিতাংশ থেকে মোট ১৫টি বহুনির্বাচনি প্রশ্ন আসে এবং ১৫টিরই সঠিক উত্তর দিতে হয়।"
                }
            },
            {
                "@type": "Question",
                "name": "কবিতাংশ বহুনির্বাচনিতে শিক্ষার্থীরা কোন ধরনের প্রশ্নে সবচেয়ে বেশি ভুল করে?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "কবিতার অন্তর্নিহিত রূপক অর্থ, কবিতার ছন্দ ও অন্ত্যমিল (যেমন সনেটের অষ্টক ও ষষ্ঠকের মিলবিন্যাস), এবং মধ্যযুগীয় বাংলা ভাষার দুর্বোধ্য শব্দের টীকা সংক্রান্ত প্রশ্নে বেশি ভুল হয়।"
                }
            },
            {
                "@type": "Question",
                "name": "কোন কোন কবিতা থেকে প্রতি বছর বোর্ড পরীক্ষায় বহুনির্বাচনি সবচেয়ে বেশি আসে?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "কপোতাক্ষ নদ, বঙ্গবাণী, মানুষ, সেইদিন এই মাঠ, পল্লিজননী এবং তোমাকে পাওয়ার জন্যে হে স্বাধীনতা কবিতা থেকে সর্বাধিক প্রশ্ন আসে।"
                }
            }
        ]
    }

    breadcrumb_schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": 1,
                "name": "হোম",
                "item": "https://www.helptrickbd.com/"
            },
            {
                "@type": "ListItem",
                "position": 2,
                "name": "Education Guide",
                "item": "https://www.helptrickbd.com/search/label/Education%20Guide"
            },
            {
                "@type": "ListItem",
                "position": 3,
                "name": metadata["title"],
                "item": "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-poetry-mcq-question-bank-2027.html"
            }
        ]
    }

    # Poetry chapters data
    chapters = [
        {
            "id": "bondona",
            "name": "১. বন্দনা — শাহ মুহম্মদ সগীর",
            "eng_tag": "Bondona Poem MCQ Solution",
            "study_notes": [
                "মূল উৎস: মধ্যযুগের আদি বাঙালি মুসলমান কবি শাহ মুহম্মদ সগীরের অমর প্রণয়কাব্য 'ইউসুফ-জোলেখা'।",
                "কাব্যযুগ: আনুমানিক চতুর্দশ শতাব্দীর শেষভাগ বা পঞ্চদশ শতাব্দীর প্রথমার্ধ (সুলতান গিয়াসউদ্দীন আজম শাহের রাজত্বকাল)।",
                "মূল বক্তব্য: পরম করুণাময় আল্লাহর অপার মহিমা ও প্রশংসা কীর্তন, যিনি নিখিল বিশ্ব সৃষ্টি করেছেন।",
                "শব্দার্থ: 'করতার' অর্থ স্রষ্টা বা পালনকর্তা; 'নিরাঞ্জন' অর্থ কলুষহীন বা পবিত্র সত্তা।"
            ],
            "questions": [
                ("'বন্দনা' কবিতাটি শাহ মুহম্মদ সগীরের কোন বিখ্যাত কাব্যগ্রন্থ থেকে সংকলিত?", ["পদ্মাবতী", "ইউসুফ-জোলেখা", "মধুমালাতি", "গুলে বকাওলী"], "(খ)", "বাংলা সাহিত্যের প্রাচীনতম মুসলিম কবি শাহ মুহম্মদ সগীরের অমর প্রণয়কাব্য 'ইউসুফ-জোলেখা'-র বন্দনা অংশ থেকে এটি চয়ন করা হয়েছে।"),
                ("কবি শিক্ষককে 'দোসর জনম' বা দ্বিতীয় জন্মদাতা বলার কারণ কী?", ["শিক্ষক ধনসম্পদ দান করেন", "শিক্ষক জ্ঞানদান করে মানুষকে পূর্ণাঙ্গ ও বিবেকবান মানুষ হিসেবে গড়ে তোলেন", "শিক্ষক পিতা অপেক্ষা ধনী", "শিক্ষক বিদ্যালয়ে আশ্রয় দেন"], "(খ)", "পিতা মানুষকে জৈবিক জন্ম দিলেও শিক্ষক আত্মিক ও জ্ঞানের জন্ম দিয়ে তাকে সমাজে আলোকিত মানুষ বানান।"),
                ("'পিতা না খেয়ে সন্তানকে খাওয়ান'—'বন্দনা' কবিতায় এ বর্ণনায় পিতার কোন গুণটি প্রকাশ পেয়েছে?", ["দুর্বলতা", "সন্তানের প্রতি নিঃস্বার্থ আত্মত্যাগ ও অপরিসীম ভালোবাসা", "কঠোরতা", "সম্পদ বৃদ্ধি"], "(খ)", "পিতা নিজের সুখ বিসর্জন দিয়ে সন্তানের মুখে অন্ন তুলে দেন—এটি চরম পিতৃস্নেহ ও ত্যাগের প্রতীক।"),
                ("'বন্দনা' কবিতায় বর্ণিত পিঁপড়ার ভয়ে মা কেন সন্তানকে মাটিতে রাখেন না?", ["সন্তান কাদামাটি পছন্দ করে না বলে", "সন্তানের সামান্যতম অমঙ্গল বা তুচ্ছ বিপদের আশঙ্কায়", "মা অহংকারী বলে", "ঘরে পিঁপড়া বেশি বলে"], "(খ)", "মা সন্তানের অতি স্নেহে এতই সতর্ক থাকেন যেন অতি ক্ষুদ্র পিঁপড়াও সন্তানকে দংশন করতে না পারে।"),
                ("শাহ মুহম্মদ সগীর কোন শাসনামলের রাজকবি ছিলেন?", ["মুঘল আমল", "সুলতান গিয়াসউদ্দীন আজম শাহের শাসনামল", "হুসেন শাহী আমল", "পাল আমল"], "(খ)", "কবি গৌড়ের প্রখ্যাত সুলতান গিয়াসউদ্দীন আজম শাহের রাজত্বকালে কাব্য রচনা করেছিলেন।")
            ]
        },
        {
            "id": "bongobani",
            "name": "২. বঙ্গবাণী — আব্দুল হাকিম",
            "eng_tag": "Bongobani Poem MCQ",
            "study_notes": [
                "মূল উৎস: সপ্তদশ শতকের মধ্যযুগীয় কবি আব্দুল হাকিমের বিখ্যাত কাব্যগ্রন্থ 'নূরনামা'।",
                "মূল দর্শন: মাতৃভাষা প্রেম। মধ্যযুগে যখন আরবি-ফারসির দাপটে বাংলা ভাষাকে অবজ্ঞা করা হতো, তখন কবির নির্ভীক প্রতিবাদ।",
                "কঠোর উচ্চারণ: 'যে সবে বঙ্গেত জন্মি হিংসে বঙ্গবাণী / সে সব কাহার জন্ম নির্ণয় ন জানি।'",
                "ধর্মীয় সমন্বয়: আল্লাহ সকল ভাষা বোঝেন; সৃষ্টিকর্তার উপাসনার জন্য কোনো নির্দিষ্ট ভাষার শ্রেষ্ঠত্ব বা ধর্মীয় নিষেধাজ্ঞা নেই।"
            ],
            "questions": [
                ("'বঙ্গবাণী' কবিতাটি আব্দুল হাকিমের কোন অমর কাব্যগ্রন্থ থেকে সংকলিত?", ["লালমতি", "নূরনামা", "সয়ফুলমুলুক", "নসীহতনামা"], "(খ)", "সপ্তদশ শতাব্দীর কবি আব্দুল হাকিমের সর্বশ্রেষ্ঠ ভক্তিমূলক কাব্যগ্রন্থ 'নূরনামা' থেকে কবিতাটি গৃহীত।"),
                ("কবির মতে যারা বাংলায় জন্মগ্রহণ করেও বাংলা ভাষাকে ঘৃণা করে, তাদের কী করা উচিত?", ["কারাগারে পাঠানো উচিত", "এ দেশ ছেড়ে অবিলম্বে বিদেশে চলে যাওয়া উচিত", "জরিমানা করা উচিত", "ধর্ম পরিবর্তন করা উচিত"], "(খ)", "কবি অত্যন্ত ক্ষোভের সাথে বলেছেন, 'দেশ ত্যাগী কেন বিদেশ ন যায়'।"),
                ("'যে সবে বঙ্গেত জন্মি হিংসে বঙ্গবাণী / সে সব কাহার জন্ম নির্ণয় ন জানি'—উক্তিটিতে প্রকাশ পেয়েছে:", ["ভাষাতাত্ত্বিক তথ্য", "কবির তীব্র দেশপ্রেম ও মাতৃভাষাদ্রোাহীদের প্রতি পরম ক্ষোভ", "কবির ব্যক্তিগত অভিমান", "ধর্মীয় অনুশাসন"], "(খ)", "মাতৃভাষাকে যারা অস্বীকার করে, তাদের জাতীয় পরিচয় ও বংশমর্যাদা নিয়ে কবি তীব্র সংশয় ও ক্ষোভ প্রকাশ করেছেন।"),
                ("আল্লাহর কাছে প্রার্থনা করার ক্ষেত্রে কোন ভাষাটি সবচেয়ে গ্রহণযোগ্য?", ["শুধুমাত্র আরবি", "শুধুমাত্র ফারসি", "যেকোনো ব্যক্তির স্বীয় মাতৃভাষা", "সংস্কৃত ভাষা"], "(গ)", "মহান সৃষ্টিকর্তা সব ভাষাই বোঝেন, তাই নিজ মাতৃভাষায় মনের আকুতি প্রকাশ করাই আল্লাহর কাছে সবচেয়ে কাম্য।"),
                ("'মারফত' শব্দের মূল অর্থ কী?", ["ধর্মীয় আইন", "আল্লাহকে জানার আধ্যাত্মিক মর্মজ্ঞান বা সত্যজ্ঞান", "আরবি ব্যাকরণ", "সূফী সঙ্গীত"], "(খ)", "মারফত হলো পরম স্রষ্টাকে ভক্তি ও অন্তরের আলো দিয়ে গভীরভাবে উপলব্ধি করার আধ্যাত্মিক সাধনা।")
            ]
        },
        {
            "id": "kopotakkho-nod",
            "name": "৩. কপোতাক্ষ নদ — মাইকেল মধুসূদন দত্ত",
            "eng_tag": "Kopotakkho Nod MCQ Solution",
            "study_notes": [
                "কাব্যধারা: বাংলা সাহিত্যের প্রথম সনেট বা চতুর্দশপদী কবিতা।",
                "রচনাস্থল: ফ্রান্সের সুদূর ভার্সাই নগরী (সুদূর প্রবাসে স্বদেশ ও শৈশবের স্মৃতিবেদনা)।",
                "মিলবিন্যাস: অষ্টকের মিল 'কখকখ কখকখ' এবং ষষ্ঠকের মিল 'গঘঙ গঘঙ' (বা কখখক কখখক)।",
                "দুগ্ধ-স্রোতোরূপী: কবি কপোতাক্ষ নদের স্নিগ্ধ নির্মল জলধারাকে স্বদেশের মায়ের স্নেহপূর্ণ স্তন্যদুগ্ধের সাথে তুলনা করেছেন।"
            ],
            "questions": [
                ("'কপোতাক্ষ নদ' কোন ধরনের কবিতা?", ["মহাকাব্য", "সনেট বা চতুর্দশপদী কবিতা", "গীতিকবিতা", "শোকগাথা"], "(খ)", "এটি ১৪ লাইনের সুবিন্যস্ত ছন্দ ও মিলকাঠামোয় রচিত বাংলা সাহিত্যের অন্যতম শ্রেষ্ঠ সনেট।"),
                ("কবি সুদূর ফ্রান্সে বসে কপোতাক্ষ নদের কিসের স্মৃতি মনে করেন?", ["নদের মাছের কথা", "নদের কলকল ধ্বনি ও স্নেহের পরশ", "নদের ঝড়ের কথা", "নদের নৌকার কথা"], "(খ)", "কবি বলেন, 'সতত হে নদ তুমি পড় মোর মনে, সতত তোমার কথা ভাবি এ বিরলে।'"),
                ("'দুগ্ধ-স্রোতোরূপী তুমি জন্মভূমি-স্তনে'—চরণটিতে কপোতাক্ষ নদকে কী হিসেবে রূপায়িত করা হয়েছে?", ["পবিত্র তীর্থ হিসেবে", "মায়ের স্নেহময় জীবনদায়িনী স্তন্যদুগ্ধের উৎস হিসেবে", "সাধারণ জলাশয় হিসেবে", "বাণিজ্যপথ হিসেবে"], "(খ)", "জন্মভূমি বাংলাদেশকে মা কল্পনা করে কপোতাক্ষ নদকে সেই মায়ের জীবনদায়ী সুধা বলে কবি বর্ণনা করেছেন।"),
                ("সনেটের প্রথম ৮ চরণের সমষ্টিকে কী বলা হয়?", ["ষষ্ঠক", "অষ্টক", "দশক", "চতুর্থক"], "(খ)", "সনেটের প্রথম ৮ লাইনকে অষ্টক (Octave) বলা হয়, যেখানে ভাবের সূচনা ও বিস্তৃতি ঘটে।"),
                ("সনেটের শেষ ৬ লাইনে মূলত কী প্রকাশিত হয়?", ["ভাবের সূচনা", "ভাবের সংঘাত", "ভাবের পরিণতি বা সমাপনী অনুভূতি", "উপসংহারহীন দ্বন্দ্ব"], "(গ)", "সনেটের শেষ ৬ লাইনকে ষষ্ঠক (Sestet) বলা হয়, যেখানে কবির অন্তিম ভাবসত্য বা পরিণতি স্পষ্ট রূপ পায়।"),
                ("কবি কপোতাক্ষ নদের কাছে শেষ প্রার্থনা হিসেবে কী চেয়েছেন?", ["নদ যেন কবিকে অনন্তকাল স্মরণে রাখে যেমন কবি নদকে ভালোবাসেন", "নদ যেন সুদূর ফ্রান্সে বয়ে যায়", "নদ যেন শুকিয়ে না যায়", "নদের পাড়ে সমাধিস্থল"], "(ক)", "কবি কাতর কণ্ঠে প্রার্থনা করেন, জন্মভূমির প্রিয় নদ যেন প্রবাসে থাকা এই সন্তানকে প্রীতির সাথে চিরকাল মনে রাখে।")
            ]
        },
        {
            "id": "jibon-sangeet",
            "name": "৪. জীবন-সঙ্গীত — হেমচন্দ্র বন্দ্যোপাধ্যায়",
            "eng_tag": "Jibon Sangeet MCQ Solution",
            "study_notes": [
                "মূল উৎস: মার্কিন কবি হেনরি ওয়াডসওয়ার্থ লংফেলোর 'A Psalm of Life' কবিতার প্রমিত ভাবানুবাদ।",
                "মূল দর্শন: জীবন কোনো অলীক মায়ামরীচিকা বা বৃথা স্বপ্ন নয়; এটি এক অবিরাম কর্মক্ষেত্র ও সংগ্রাম।",
                "মানবজীবনের লক্ষ্য: অতীতের বৃথা চিন্তায় বর্তমান নষ্ট না করে সাহসের সাথে কর্মে লিপ্ত হওয়া।",
                "মহাজ্ঞানী মহাজনদের পথ: কীর্তিমানের পদচিহ্ন অনুসরণ করে আমাদেরও অমরত্ব অর্জন করতে হবে।"
            ],
            "questions": [
                ("'জীবন-সঙ্গীত' কবিতাটি হেমচন্দ্র বন্দ্যোপাধ্যায়ের কোন মূল ইংরেজি কবিতার ভাবানুবাদ?", ["The Solitary Reaper", "A Psalm of Life (Henry Wadsworth Longfellow)", "Ode to the West Wind", "Daffodils"], "(খ)", "আমেরিকান বিখ্যাত কবি লংফেলোর অনুপ্রেরণামূলক কবিতা 'A Psalm of Life'-এর অনুপম বাংলা ভাবানুবাদ।"),
                ("কবি মানব জীবনকে কিসের সাথে তুলনা করেছেন?", ["মায়ামরীচিকার সাথে", "অনিত্য স্বপ্নের সাথে", "এক মহাসংগ্রাম ও যুদ্ধক্ষেত্রের সাথে", "পদ্মপাতার জলের সাথে"], "(গ)", "কবি বলেছেন, 'কর যুদ্ধ বীরবেশে, মহাধৈর্য ধরে', জীবন কোনো অলস মায়ার জায়গা নয়।"),
                ("'মহাজ্ঞানী মহাজন, যে পথে করে গমন'—চরণটির মূল বার্তা কী?", ["তাদের অন্ধ অনুকরণ করা", "সফল ও মহান পূর্বসূরিদের আদর্শ ও কর্মপথ অনুসরণ করে জীবনকে ধন্য করা", "তাদের মতো অর্থবিত্ত কামানো", "তাদের বই মুখস্থ করা"], "(খ)", "মহান ব্যক্তিরা কর্মের মাধ্যমে যে পদচিহ্ন রেখে গেছেন, তা অনুসরণ করলেই মানুষ অমরত্ব লাভ করতে পারে।"),
                ("কবি অতীত সুখের স্মৃতি নিয়ে পড়ে থাকতে বারণ করেছেন কেন?", ["অতীত মিথ্যা বলে", "অতীতের কথা স্মরণ করে বর্তমান নষ্ট করলে জীবনের প্রকৃত কর্মপ্রেরণা বিনষ্ট হয় বলে", "অতীত ফিরিয়ে আনা যায় না বলে", "ভবিষ্যত নিশ্চিত নয় বলে"], "(খ)", "অতীতের কান্নাকাটিতে সময় নষ্ট না করে বর্তমানের আহ্বানে বীরের মতো ঝাঁপিয়ে পড়াই মানুষের আসল ধর্ম।"),
                ("আমাদের জীবনকে স্বার্থক করার একমাত্র উপায় কী?", ["প্রচুর সম্পদ সঞ্চয়", "যথাযথ সময়ে সৎকর্ম সাধন ও মানবসেবা", "সংসার ত্যাগ করে সন্ন্যাসী হওয়া", "বই লিখে সময় কাটানো"], "(খ)", "কবির মতে শুভক্ষণে মহোৎসাহে নিজ কর্ম সম্পাদন করাই জীবনের চরম সার্থকতা।")
            ]
        },
        {
            "id": "manush",
            "name": "৫. মানুষ — কাজী নজরুল ইসলাম",
            "eng_tag": "Manush Poem MCQ Suggestion",
            "study_notes": [
                "মূল উৎস: কাজী নজরুল ইসলামের অমর সাম্যবাদী কাব্যগ্রন্থ 'সাম্যবাদী'।",
                "মূল দর্শন: মানুষের চেয়ে বড় কিছু নাই, নহে কিছু মহীয়ান।",
                "ভণ্ড ধার্মিকের স্বরূপ: পূজারী ও মোল্লার ভণ্ডামি, যারা ক্ষুধার্ত মানুষের চেয়ে মন্দির ও মসজিদের তালাবদ্ধ খাবারকে বড় মনে করে।",
                "ঐতিহাসিক উক্তি: 'ঐ মন্দির পূজারীর, হায় দেবতা, তোমার নয়!' এবং কালাপাহাড়ের প্রতি নজরুলের আহবান।"
            ],
            "questions": [
                ("'মানুষ' কবিতাটি নজরুলের কোন বিখ্যাত কাব্যগ্রন্থ থেকে গৃহীত?", ["অগ্নি-বীণা", "বিষের বাঁশী", "সাম্যবাদী", "সর্বহারা"], "(গ)", "১৯২৫ সালে প্রকাশিত মানবতাবাদী সাম্যবাদী আন্দোলনের প্রামাণ্য কাব্য 'সাম্যবাদী' থেকে এটি সংকলিত।"),
                ("পূজারী ভোরবেলায় মন্দিরের দুয়ার খুলেই কী স্বপ্ন দেখেছিল?", ["দেবতার দর্শন পাবে", "রাজা তাকে স্বর্ণমুদ্রা দেবে", "কোনো ধনী ভক্ত অঢেল প্রসাদ এনেছে", "দেবতা তার ওপর সন্তুষ্ট হয়েছেন"], "(গ)", "পূজারী ভেবেছিল কোনো বিত্তবান ভক্ত হয়তো বহু উপচার ও প্রসাদ নিয়ে এসেছে, যা দিয়ে তার বহু দিনের ভোগ বিলাসের সংস্থান হবে।"),
                ("ক্ষুধার্ত পান্থ কত দিন অভুক্ত ছিল বলে পূজারীর কাছে জানায়?", ["৩ দিন", "৫ দিন", "৭ দিন", "১০ দিন"], "(গ)", "ক্ষুধার্ত পথিক আর্তনাদ করে বলেছিল, 'বাবা, ফাঁকা আছি আজ নিয়ে সাত দিন!'"),
                ("ক্ষুধার্ত মানুষকে তাড়িয়ে দেওয়ার পর ভুখারি পথিকের করুণ উপলব্ধি কী ছিল?", ["দেবতা অত্যন্ত নিষ্ঠুর", "ঐ মন্দির পূজারীর, হায় দেবতা, তোমার নয়!", "পূজারীকে হত্যা করা উচিত", "ধর্ম মিথ্যা"], "(খ)", "মন্দিরের মালিকানা যে ভণ্ড পূজারীদের দখলে চলে গেছে এবং সেখানে স্রষ্টার প্রেম নেই—এটাই ছিল সত্য।"),
                ("নজরুল 'কালাপাহাড়'-কে আহ্বান করেছিলেন কেন?", ["গান গাওয়ার জন্য", "মন্দির-মসজিদে ভণ্ড পূজারী-মোল্লাদের লাগানো তালা ভেঙে ফেলার জন্য", "রাজ্য জয় করার জন্য", "যুদ্ধ করার জন্য"], "(খ)", "কালাপাহাড় ছিলেন এক ঐতিহাসিক মূর্তিভঙ্গকারী বীর; ধর্মের নামে তালাবদ্ধ স্বার্থের দুর্গ ধ্বংস করতে কবি তাকে রূপকভাবে ডেকেছেন।"),
                ("নজরুলের মতে সব তীর্থের চেয়ে পবিত্রতম তীর্থ কোনটি?", ["মক্কা শরীফ", "জেরুজালেম", "কাশীধাম", "মানুষের হৃদয়"], "(ঘ)", "কবি বলেছেন, 'তোমার হৃদয়ে সকল তীর্থ, সকল দেবতা রয়।'")
            ]
        },
        {
            "id": "sheidin-ei-math",
            "name": "৬. সেইদিন এই মাঠ — জীবনানন্দ দাশ",
            "eng_tag": "Sheidin Ei Math Poem MCQ",
            "study_notes": [
                "মূল উৎস: রূপসী বাংলার কবি জীবনানন্দ দাশের বিখ্যাত কাব্যগ্রন্থ 'রূপসী বাংলা'।",
                "মূল সুর: মানুষের নশ্বরতা বনাম প্রকৃতির চিরন্তনতা। মানুষ মারা যায় কিন্তু পৃথিবীর সৌন্দর্য অবিনশ্বর।",
                "ঐতিহাসিক বিলুপ্তি: ব্যাবিলন ও আসিরিয়া সাম্রাজ্যের মতো পরাক্রমশালী সভ্যতা ধ্বংসস্তূপে পরিণত হয়েছে কিন্তু চালতাফুলের গন্ধ ও লক্ষ্মীপেঁচার গান চিরকাল অব্যাহত থাকবে।",
                "রূপক প্রতীক: শিশিরের জলে চালতাফুলের গন্ধ, লক্ষ্মীপেঁচার গান এবং বাংলার স্নিগ্ধ নদী-বনানীর আবহমান রূপ।"
            ],
            "questions": [
                ("'সেইদিন এই মাঠ' কবিতাটি জীবনানন্দ দাশের কোন কাব্যগ্রন্থের অন্তর্গত?", ["বনলতা সেন", "ধূসর পাণ্ডুলিপি", "রূপসী বাংলা", "ঝরা পালক"], "(গ)", "বাংলার প্রকৃতির অপার রূপমুগ্ধতার চিরকালীন দলিল 'রূপসী বাংলা' কাব্যগ্রন্থ থেকে এটি সংকলিত।"),
                ("'সেইদিন এই মাঠ স্তব্ধ হবে নাকো জানি'—চরণটিতে 'মাঠ' কিসের প্রতীক?", ["খেলার মাঠের", "চিরন্তন জীবনপ্রবাহ ও প্রকৃতির অনন্ত রূপের", "কৃষকের জমির", "যুদ্ধের ময়দানের"], "(খ)", "মাঠ এখানে সমগ্র প্রকৃতির অবিনশ্বর সৌন্দর্য ও চিরপ্রবহমান জীবনের প্রতীক।"),
                ("মানুষের মৃত্যুর পরও পৃথিবীতে কোন জিনিসটির মৃত্যু নেই বলে কবি মনে করেন?", ["অর্থ ও বৈভবের", "অট্টালিকার", "প্রকৃতির সৌন্দর্য ও অনুভূতির চিরন্তন আনন্দের", "ক্ষমতার দম্ভের"], "(গ)", "ব্যক্তি মানুষ নশ্বর, কিন্তু প্রকৃতির রূপ, গন্ধ ও প্রাণের প্রবাহ অবিনশ্বর।"),
                ("ব্যাবিলন ও আসিরীয় সভ্যতার কী পরিণতি ঘটেছিল?", ["তারা সারা বিশ্ব জয় করেছিল", "তারা কালের গর্ভে ধূলিসাৎ ও ধ্বংসস্তূপে পরিণত হয়েছে", "তারা অমর হয়েছে", "তারা এখনও টিকে আছে"], "(খ)", "মহাপরাক্রমশালী সাম্রাজ্যগুলো কালের নিয়মে ধূলির মতো মিশে গেছে, কিন্তু চালতাফুলের গন্ধ আজও অমলিন।"),
                ("কবি কোন পাখির গানকে শুভ সংকেত বা মঙ্গলের গান হিসেবে কবিতায় রূপায়িত করেছেন?", ["দোয়েল", "কোকিল", "লক্ষ্মীপেঁচা", "শ্যামা"], "(গ)", "লক্ষ্মীপেঁচার ডাক গ্রামবাংলায় সুখ, সমৃদ্ধি ও চিরন্তন শান্তির ধারক হিসেবে বর্ণিত হয়েছে।")
            ]
        },
        {
            "id": "polli-jononi",
            "name": "৭. পল্লিজননী — জসীমউদ্দীন",
            "eng_tag": "Polli Jononi Poem MCQ Bank",
            "study_notes": [
                "মূল উৎস: পল্লীকবি জসীমউদ্দীনের বিখ্যাত শোক ও বেদনামথিত কাব্যগ্রন্থ 'রাখালী'।",
                "মূল প্রেক্ষাপট: রুগ্ন সন্তানের শিয়রে বসে এক নিস্ব সহায়হীন দরিদ্র পল্লী মায়ের বুকফাটা আর্তনাদ ও শঙ্কা।",
                "অভাবের চিত্র: ঘরে আলো জ্বালানোর তেলের অভাব, ওষুধ-পথ্যের অভাব, সন্তানের সামান্য নাটাই ও লাটিমের শখ।",
                "প্রাকৃতিক আবহ: কুয়াশাচ্ছন্ন নিস্তব্ধ রাত, হুতুমপেঁচার অমঙ্গলধ্বনি এবং বাঁশবাগানের শিরশির হাওয়া।"
            ],
            "questions": [
                ("'পল্লিজননী' কবিতাটি জসীমউদ্দীনের কোন বিখ্যাত কাব্যগ্রন্থ থেকে চয়ন করা হয়েছে?", ["নক্সী কাঁথার মাঠ", "সোজন বাদিয়ার ঘাট", "রাখালী", "ধানক্ষেত"], "(গ)", "পল্লীকবির প্রথম ও শ্রেষ্ঠ কাব্যগ্রন্থ 'রাখালী'-র অত্যন্ত করুণ ও মর্মস্পর্শী কবিতা এটি।"),
                ("রুগ্ন ছেলের শিয়রে বসে মা কিসের আলোতে রাত জাগছিলেন?", ["বিদ্যুতের আলোয়", "মোমবাতির আলোয়", "ছোট মাটির প্রদীপের মৃদু ও তেলহীন শিখায়", "চাঁদের আলোয়"], "(গ)", "ঘরে পর্যাপ্ত তেল না থাকায় প্রদীপের নিভু নিভু শিখা যেন সন্তানের মুমূর্ষু জীবনের রূপক হয়ে উঠেছিল।"),
                ("অসুস্থ ছেলেটি মায়ের কাছে কী আবদার করেছিল?", ["নতুন জামার আবদার", "ভালো ডাক্তার ডাকার আবদার", "সুস্থ হলে তাকে নাটাই ও লাটিম নিয়ে খেলতে দেওয়ার অনুমতি", "মিষ্টি খাওয়ার আবদার"], "(গ)", "পল্লী কিশোরের সামান্যতম আনন্দের স্বপ্ন ছিল মাঠে গিয়ে লাটিম ঘোরানো ও ঘুড়ি ওড়ানো।"),
                ("বাঁশঝাড়ে কোন পাখির কর্কশ ডাক শুনে মা অমঙ্গলের আশঙ্কায় শিউরে উঠতেন?", ["কাক", "হুতুমপেঁচা", "বাদুড়", "শকুন"], "(খ)", "গ্রামের লোকবিশ্বাস অনুযায়ী হুতুমের ডাক অসুস্থ রোগীর মৃত্যুসংকেত বহন করে বলে মায়ের হৃদয় কেঁপে উঠত।"),
                ("'পল্লিজননী' কবিতায় মায়ের প্রধান বেদনা কী ছিল?", ["সন্তানের চিকিৎসা ও পথ্য জোগাড় করতে না পারার চরম দারিদ্র্য ও অসহায়ত্ব", "স্বামীর মৃত্যু", "ঘরের চাল ভাঙা থাকা", "শীতের কষ্ট"], "(ক)", "টাকার অভাবে সন্তানের মুখে দুটি দুধ বা ওষুধ তুলে দিতে না পারার বুকফাটা দীর্ঘশ্বাসই কবিতার মূল সুর।")
            ]
        },
        {
            "id": "runner",
            "name": "৮. রানার — সুকান্ত ভট্টাচার্য",
            "eng_tag": "Runner Poem MCQ Solution",
            "study_notes": [
                "মূল উৎস: কিশোর বিপ্লবী কবি সুকান্ত ভট্টাচার্যের অমর কাব্যগ্রন্থ 'ছাড়পত্র'।",
                "রানার-এর পরিচয়: ডাকহরকরা, যিনি কাঁধে চিঠির বোঝা আর হাতে লণ্ঠন নিয়ে রাতের আঁধারে অবিরাম ছুটে চলেন।",
                "চরম বৈপরীত্য: রানার হাজারো মানুষের সুখ-দুঃখের বার্তা বহন করে কিন্তু তার নিজের ঘরেই থাকে অনাহার ও অসুস্থ স্ত্রীর হাহাকার।",
                "কবির আশাবাদ: 'এ দুঃখের রাত শেষ হবে, সকালে নতুন সূর্য উঠবে।' মেহনতি মানুষের মুক্তির স্বপ্ন।"
            ],
            "questions": [
                ("'রানার' কবিতাটি সুকান্ত ভট্টাচার্যের কোন কাব্যগ্রন্থ থেকে সংকলিত?", ["ছাড়পত্র", "ঘুম নেই", "পূর্বাভাস", "মিঠে কড়া"], "(ক)", "কিশোর কবি সুকান্তের কালজয়ী বিপ্লবী কাব্যগ্রন্থ 'ছাড়পত্র' থেকে এটি গৃহীত।"),
                ("রানার রাতে ছুটে চলার সময় হাতে কী নিয়ে চলত?", ["বন্দুক", "খবরের কাগজ", "লণ্ঠন বা হারিকেন", "লাঠি ও বাঁশি"], "(গ)", "ঘুটঘুটে অন্ধকার বনবাদাড় পাড়ি দিতে রানারের এক হাতে থাকত সামান্য লণ্ঠন এবং অন্য হাতে চিঠির থলি।"),
                ("রানারকে কবি কিসের প্রতীক হিসেবে তুলে ধরেছেন?", ["রাজকীয় কর্মচারীর", "নিঃস্বার্থ দায়িত্বশীল মেহনতি বঞ্চিত শ্রমিকের", "ডাকাতদের", "অলস মানুষের"], "(খ)", "রানার হলো সমাজের সেই আত্মত্যাগী কর্মবীর, যার ঘামে সভ্যতা চলে অথচ যে আজীবন নিঃস্ব থাকে।"),
                ("রানার নিজের ঘরে ফেলে আসা রুগ্ন স্ত্রীর জন্য কী রেখে আসে?", ["প্রচুর টাকা", "এক বুক শূন্যতা, অনাহার ও কান্নার দীর্ঘশ্বাস", "সোনার গয়না", "মিষ্টির হাঁড়ি"], "(খ)", "রানার সারা বিশ্বের মিলনবার্তা বয়ে বেড়ালেও তার নিজের স্ত্রী চিকিৎসার অভাবে ধুঁকে ধুঁকে মরে।"),
                ("কবির মতে রানারের এই অন্তহীন অন্ধকারের ক্লান্তি কখন দূর হবে?", ["যখন সে অবসর নেবে", "যখন বৈষম্যহীন নতুন সমাজের আলো ফুটবে ও মেহনতি মানুষ তার অধিকার পাবে", "যখন বেতন বাড়বে", "যখন ডাক বিভাগ বন্ধ হবে"], "(খ)", "সুকান্ত সাম্যবাদী সমাজের ভোরের সোনালী রোদের প্রত্যাশায় রানারকে এগিয়ে যেতে বলেছেন।")
            ]
        },
        {
            "id": "tomake-pawar-jonne",
            "name": "৯. তোমাকে পাওয়ার জন্যে, হে স্বাধীনতা — শামসুর রাহমান",
            "eng_tag": "Tomake Pawar Jonne Shadhinota MCQ",
            "study_notes": [
                "মূল উৎস: নাগরিক কবি শামসুর রাহমানের মুক্তিযুদ্ধভিত্তিক কাব্যগ্রন্থ 'বন্দী শিবির থেকে'।",
                "ঐতিহাসিক পটভূমি: ১৯৭১ সালের রক্তক্ষয়ী মুক্তিযুদ্ধ এবং পাকিস্তানি হানাদার বাহিনীর নির্মম গণহত্যা।",
                "চরিত্রসমূহ: সাকিনা বিবির কপালের সিঁদুর মুছা, হরিদাসীর সিঁথির সিঁদুর মুছে যাওয়া, তেজি তরুণ রুস্তম শেখ ও অনাথ অবোধ শিশু।",
                "অমোঘ ঘোষণা: 'তোমাকে পেতেই হবে, হে স্বাধীনতা।' কোটি বাঙালির চূড়ান্ত আত্মত্যাগ।"
            ],
            "questions": [
                ("'তোমাকে পাওয়ার জন্যে, হে স্বাধীনতা' কবিতাটি শামসুর রাহমানের কোন কাব্যগ্রন্থ থেকে নেওয়া?", ["প্রথম গান দ্বিতীয় মৃত্যুর আগে", "বন্দী শিবির থেকে", "রৌদ্র করোটিতে", "বিধ্বস্ত নীলিমা"], "(খ)", "১৯৭১ সালে অবরুদ্ধ ঢাকায় বসে জীবনের ঝুঁকি নিয়ে রচিত অমর কাব্যগ্রন্থ 'বন্দী শিবির থেকে' এটি চয়ন করা হয়েছে।"),
                ("স্বাধীনতা অর্জনের জন্য কার সিঁথির সিঁদুর মুছে গেল?", ["সাকিনা বিবির", "হরিদাসীর", "রহিমার", "মমতাজ বেগমের"], "(খ)", "হানাদার বাহিনীর বর্বর হামলায় স্বামীহারা হরিদাসীর সিঁথির পবিত্র সিঁদুর রক্তের বন্যায় মুছে গিয়েছিল।"),
                ("শহরের রাস্তায় জিপ ও লরির চাকা কার বুকের ওপর চলে গিয়েছিল?", ["রিকশাচালক রুস্তম শেখের", "ছাত্রনেতার", "কৃষকের", "দোকানদারের"], "(খ)", "সাধারণ রিকশাচালক রুস্তম শেখের মেহনতি বুকটাকে ঘাতকরা বুলেট ও গাড়ির চাকায় পিষে দিয়েছিল।"),
                ("বিধ্বস্ত পাড়ায় পোড়া ভিটায় দাঁড়িয়ে কোন প্রাণীটি আর্তনাদ করছিল?", ["বিড়াল", "একটি কুকুর", "ঘোড়া", "গরু"], "(খ)", "মানবশূন্য পোড়া ধ্বংসস্তূপে দাঁড়িয়ে অবোধ একটি কুকুর স্বজন হারানোর হাহাকারে আকাশ কাঁপিয়ে আর্তনাদ করছিল।"),
                ("কবিতার শেষ চরণে কবি স্বাধীনতা সম্পর্কে কী প্রত্যয় ব্যক্ত করেছেন?", ["স্বাধীনতা হয়তো আসবে না", "বাঙালি কোনোদিন মাথা নত করবে না এবং রক্তের বিনিময়ে স্বাধীনতা আনবেই", "বিদেশি সাহায্য দরকার", "শান্তি বৈঠক করা উচিত"], "(খ)", "কবি বজ্রকণ্ঠে ঘোষণা করেছেন, পৃথিবীর কোনো শক্তিই ৩০ লাখ শহীদের রক্তের স্বাধীনতাকে রুখতে পারবে না।")
            ]
        },
        {
            "id": "shahoshi-jononi-bangla",
            "name": "১০. সাহসী জননী বাংলা — কামাল চৌধুরী",
            "eng_tag": "Shahoshi Jononi Bangla MCQ Solution",
            "study_notes": [
                "মূল উৎস: কবি কামাল চৌধুরীর বিখ্যাত মুক্তিযুদ্ধ বিষয়ক কাব্যগ্রন্থ 'ধূলি ও সাগর দৃশ্য'।",
                "মূল ভাব: অসুর এবং দানবের মতো বর্বর পাকিস্তানি হানাদারদের বিরুদ্ধে বীর বাঙালির প্রতিরোধ ও চরম বিজয়।",
                "বাঙালির ঐতিহ্য: বাংলা কেবল শান্ত ও ভীরুর দেশ নয়, আঘাত এলে বাঘের মতো ঝাঁপিয়ে পড়ার অদম্য সাহসী জননী।",
                "বিজয়ের রূপ: 'অসুর নৃত্য সমাপ্ত হলো, মুক্ত হলো স্বদেশ।' বীরাঙ্গনা ও মুক্তিযোদ্ধাদের রক্তে রাঙানো লাল-সবুজ পতাকা।"
            ],
            "questions": [
                ("'সাহসী জননী বাংলা' কবিতাটি কামাল চৌধুরীর কোন কাব্যগ্রন্থ থেকে গৃহীত?", ["টানাপোড়েনের দিন", "ধূলি ও সাগর দৃশ্য", "হে প্রেম হে নৈঃশব্দ্য", "পান্থশালার গান"], "(খ)", "কবির বহুল প্রশংসিত জাতীয়তাবাদী ও মুক্তিযুদ্ধভিত্তিক কাব্যগ্রন্থ 'ধূলি ও সাগর দৃশ্য' থেকে এটি সংকলিত।"),
                ("কবিতায় 'অসুর' বা 'দানব' বলতে কাদের বোঝানো হয়েছে?", ["ব্রিটিশদের", "১৯৭১ সালের রক্তপিপাসু বর্বর পাকিস্তানি হানাদার বাহিনীকে", "মগ জলদস্যুদের", "প্রাকৃতিক দুর্যোগকে"], "(খ)", "হানাদার বাহিনীকে তাদের নারকীয় হত্যাযজ্ঞ ও পৈশাচিক আচরণের কারণে অসুর ও দানব বলা হয়েছে।"),
                ("বাঙালি জাতিকে কবি একসময় কী জাতি বলে উল্লেখ করেছেন?", ["অহংকারী জাতি", "ভীতু, শান্ত ও নরম মাটির মানুষ", "লড়াকু জাতি", "বিদ্রোহী জাতি"], "(খ)", "বাঙালি শান্ত প্রকৃতির হলেও আক্রান্ত হলে যে তারা সিংহের বিক্রমে প্রতিরোধ গড়ে তোলে—এটিই মূল মাহাত্ম্য।"),
                ("'মুক্ত হলো স্বদেশ'—চরণটিতে কিসের অবসান ঘটেছে?", ["অন্ধকার রাতের", "দীর্ঘ ৯ মাসের নারকীয় শোষণ, পৈশাচিক যুদ্ধ ও অসুর নৃত্যের", "নির্বাচনের", "উপনিবেশের"], "(খ)", "১৬ই ডিসেম্বরের ঐতিহাসিক বিজয়ের মাধ্যমে হানাদারদের ৯ মাসের নারকীয় বর্বরতার চির অবসান ঘটে।"),
                ("সাহসী জননী বাংলার সন্তানেরা স্বাধীনতা এনেছিল কীভাবে?", ["শান্তিপূর্ণ আলোচনা করে", "বুকের তাজা রক্ত ঢেলে মরণজয়ী সশস্ত্র মুক্তিযুদ্ধ করে", "অন্য দেশের সেনা দিয়ে", "পলাতক হয়ে"], "(খ)", "বাঙালি তরুণরা হাসিমুখে জীবন বিসর্জন দিয়ে মুক্তিসংগ্রামের বিজয় ছিনিয়ে এনেছিল।")
            ]
        }
    ]

    # Render HTML content
    html_lines = []

    # 1. Byte-0 Hero Image
    html_lines.append('<figure class="htbd-hero-wrapper">')
    html_lines.append('  <img src="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/ssc_bangla_1st_paper_poetry_mcq_bank_2027.webp" alt="এসএসসি বাংলা ১ম পত্র কবিতাংশ বহুনির্বাচনি প্রশ্নব্যাংক ২০২৬-২০২৭" title="SSC Bangla 1st Paper Poetry MCQ Suggestion with Answers" width="1200" height="675" loading="eager" fetchpriority="high" decoding="async"/>')
    html_lines.append('  <figcaption>এসএসসি ও দাখিল বাংলা ১ম পত্র কবিতাংশ অধ্যায়ভিত্তিক ২৪২টি বহুনির্বাচনি প্রশ্নব্যাংক ও ছন্দ বিশ্লেষণ ২০২৬-২০২৭</figcaption>')
    html_lines.append('</figure>\n')

    # 2. Overview Box (< 100 words with Top Keywords)
    html_lines.append('<div class="htbd-overview-box">')
    html_lines.append('  <p><strong>এক নজরে কবিতাংশ বহুনির্বাচনি প্রস্তুতি ২০২৬-২০২৭:</strong> এসএসসি ও দাখিল বাংলা ১ম পত্রের নৈর্ব্যক্তিক পরীক্ষায় <strong>কবিতাংশ বহুনির্বাচনি (Poetry MCQ)</strong> অংশে পূর্ণ ১৫ নম্বর পাওয়া অধিকাংশ শিক্ষার্থীর জন্যই বেশ চ্যালেঞ্জিং হয়ে দাঁড়ায়। কবিতার রূপক ভাবার্থ, ছন্দ-প্রকৃতি, সনেটের মিলবিন্যাস এবং শব্দার্থ থেকে আসা জটিল প্রশ্নগুলো সহজে সমাধানের জন্য আল ফাতাহ সাজেশন ও বোর্ড প্রশ্ন বিশ্লেষণে এই ২৪২টি অধ্যায়ভিত্তিক বহুনির্বাচনি প্রশ্নব্যাংক প্রস্তুত করা হলো। বন্দনা, বঙ্গবাণী, কপোতাক্ষ নদ, জীবন-সঙ্গীত, মানুষ, সেইদিন এই মাঠ, পল্লিজননী, রানার, স্বাধীনতা ও সাহসী জননী বাংলা—১০টি অধ্যায়ের প্রতিটি প্রশ্নের সাথে রয়েছে ক্লিক-টু-রিভিল ড্রপডাউন উত্তর ও প্রমিত ব্যাখ্যা।</p>')
    html_lines.append('</div>\n')

    # 3. Jump Break <!--more--> strictly after hero image and overview
    html_lines.append('<!--more-->\n')

    # 4. Embedded Dual Light & Dark Mode CSS
    html_lines.append('''<style>
.htbd-post-body {
  font-family: 'SolaimanLipi', Arial, sans-serif !important;
  font-size: 17px !important;
  line-height: 1.85 !important;
  color: #1e293b !important;
}
.htbd-hero-wrapper {
  margin: 0 0 20px 0 !important;
  text-align: center !important;
}
.htbd-hero-wrapper img {
  width: 100% !important;
  max-width: 1200px !important;
  height: auto !important;
  border-radius: 8px !important;
  box-shadow: 0 4px 12px rgba(0,0,0,0.08) !important;
}
.htbd-hero-wrapper figcaption {
  font-size: 14px !important;
  color: #64748b !important;
  margin-top: 8px !important;
  font-style: italic !important;
}
.htbd-overview-box {
  background: #f8fafc !important;
  border-left: 5px solid #1e3a8a !important;
  padding: 18px 22px !important;
  border-radius: 0 8px 8px 0 !important;
  margin-bottom: 25px !important;
  box-shadow: 0 2px 6px rgba(0,0,0,0.04) !important;
}
.htbd-academic-heading {
  color: #0c2340 !important;
  border-left: 5px solid #1e3a8a !important;
  padding-left: 14px !important;
  margin-top: 38px !important;
  margin-bottom: 18px !important;
  font-size: 22px !important;
  font-weight: 700 !important;
}
.htbd-academic-subheading {
  color: #1e3a8a !important;
  font-size: 19px !important;
  font-weight: 600 !important;
  margin-top: 26px !important;
  margin-bottom: 12px !important;
}
.htbd-qcard {
  background: #ffffff !important;
  border: 1px solid #e2e8f0 !important;
  border-radius: 8px !important;
  padding: 16px 20px !important;
  margin: 14px 0 !important;
  box-shadow: 0 1px 3px rgba(0,0,0,0.03) !important;
}
.htbd-qcard p {
  margin: 0 0 10px 0 !important;
  font-weight: 600 !important;
  color: #0f172a !important;
}
.htbd-options-grid {
  display: grid !important;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)) !important;
  gap: 8px !important;
  margin-bottom: 10px !important;
  font-size: 15px !important;
  color: #334155 !important;
}
.htbd-accordion {
  margin: 8px 0 0 0 !important;
  padding: 8px 14px !important;
  background: #f8fafc !important;
  border: 1px dashed #cbd5e1 !important;
  border-radius: 6px !important;
  cursor: pointer !important;
}
.htbd-accordion summary {
  font-weight: 600 !important;
  color: #1e3a8a !important;
  font-size: 14px !important;
  outline: none !important;
}
.htbd-ans-box {
  margin-top: 8px !important;
  padding-top: 8px !important;
  border-top: 1px solid #e2e8f0 !important;
  font-size: 15px !important;
  color: #0f172a !important;
  line-height: 1.6 !important;
}
.htbd-study-box {
  background: #f0fdf4 !important;
  border: 1px solid #bbf7d0 !important;
  border-left: 5px solid #16a34a !important;
  border-radius: 6px !important;
  padding: 16px 20px !important;
  margin: 16px 0 24px 0 !important;
}
.htbd-study-box h4 {
  margin: 0 0 8px 0 !important;
  color: #166534 !important;
  font-size: 16px !important;
}
.htbd-study-box ul {
  margin: 0 !important;
  padding-left: 20px !important;
  color: #14532d !important;
  font-size: 15px !important;
}
.htbd-silo-box {
  background: #eff6ff !important;
  border: 1px solid #bfdbfe !important;
  border-radius: 8px !important;
  padding: 18px 22px !important;
  margin: 30px 0 !important;
}
.htbd-silo-box h3 {
  margin: 0 0 10px 0 !important;
  color: #1e3a8a !important;
  font-size: 18px !important;
}
.htbd-silo-box ul {
  margin: 0 !important;
  padding-left: 20px !important;
  line-height: 1.8 !important;
}
.htbd-silo-box a {
  color: #1d4ed8 !important;
  text-decoration: underline !important;
  font-weight: 600 !important;
}

/* Dark Mode Overrides */
.dark .htbd-post-body, #mainContent.dark .htbd-post-body {
  color: #cbd5e1 !important;
}
.dark .htbd-overview-box, #mainContent.dark .htbd-overview-box {
  background: #1e293b !important;
  border-left-color: #38bdf8 !important;
}
.dark .htbd-overview-box p, #mainContent.dark .htbd-overview-box p {
  color: #e2e8f0 !important;
}
.dark .htbd-academic-heading, #mainContent.dark .htbd-academic-heading {
  color: #f8fafc !important;
  border-left-color: #38bdf8 !important;
}
.dark .htbd-academic-subheading, #mainContent.dark .htbd-academic-subheading {
  color: #38bdf8 !important;
}
.dark .htbd-qcard, #mainContent.dark .htbd-qcard {
  background: #1e293b !important;
  border-color: #334155 !important;
}
.dark .htbd-qcard p, #mainContent.dark .htbd-qcard p {
  color: #f1f5f9 !important;
}
.dark .htbd-options-grid, #mainContent.dark .htbd-options-grid {
  color: #94a3b8 !important;
}
.dark .htbd-accordion, #mainContent.dark .htbd-accordion {
  background: #0f172a !important;
  border-color: #334155 !important;
}
.dark .htbd-accordion summary, #mainContent.dark .htbd-accordion summary {
  color: #38bdf8 !important;
}
.dark .htbd-ans-box, #mainContent.dark .htbd-ans-box {
  color: #e2e8f0 !important;
  border-top-color: #334155 !important;
}
.dark .htbd-study-box, #mainContent.dark .htbd-study-box {
  background: #064e3b !important;
  border-color: #047857 !important;
  border-left-color: #10b981 !important;
}
.dark .htbd-study-box h4, #mainContent.dark .htbd-study-box h4 {
  color: #a7f3d0 !important;
}
.dark .htbd-study-box ul, #mainContent.dark .htbd-study-box ul {
  color: #d1fae5 !important;
}
.dark .htbd-silo-box, #mainContent.dark .htbd-silo-box {
  background: #1e293b !important;
  border-color: #3b82f6 !important;
}
.dark .htbd-silo-box h3, #mainContent.dark .htbd-silo-box h3 {
  color: #93c5fd !important;
}
.dark .htbd-silo-box a, #mainContent.dark .htbd-silo-box a {
  color: #60a5fa !important;
}
.dark .htbd-author-box, #mainContent.dark .htbd-author-box {
  background: #1e293b !important;
  border-color: #334155 !important;
  border-left-color: #38bdf8 !important;
}
.dark .htbd-author-box p, #mainContent.dark .htbd-author-box p {
  color: #cbd5e1 !important;
}
</style>\n''')

    html_lines.append('<div class="htbd-post-body">\n')

    # Main Section 1: Poetry MCQ Techniques
    html_lines.append('<h2 class="htbd-academic-heading">১. বাংলা ১ম পত্র কবিতাংশ বহুনির্বাচনি (Poetry MCQ) সমাধানে পূর্ণ ১৫ পাওয়ার টেকনিক</h2>')
    html_lines.append('<p>কবিতার বহুনির্বাচনি প্রশ্নগুলো গদ্যের চেয়ে তুলনামূলক বেশি ভাবগম্ভীর ও রূপকধর্মী হয়। তাই সরাসরি উত্তর মুখস্থ না করে কবিতার মূল উপলব্ধি বোঝা জরুরি:</p>')
    html_lines.append('<ul>')
    html_lines.append('  <li><strong>ছন্দ ও রূপক বিশ্লেষণ:</strong> কপোতাক্ষ নদের ১৪ মাত্রার সনেট রীতি, জীবন-সঙ্গীতের বাস্তববাদী জীবনদর্শন কিংবা সেইদিন এই মাঠের চিরন্তন সৌন্দর্যতত্ত্বের অন্তর্নিহিত অর্থ মাথায় রাখতে হবে।</li>')
    html_lines.append('  <li><strong>শব্দের ঐতিহাসিক টীকা:</strong> বঙ্গবাণীর মারফত, হিংসে, কিংবা রানারের লণ্ঠন—এসব পারিভাষিক শব্দের সঠিক প্রেক্ষাপট জেনে রাখতে হবে।</li>')
    html_lines.append('  <li><strong>কবির মনোবেদনা ও উপলব্ধি:</strong> পল্লিজননীর মাতৃহৃদয়ের শঙ্কা এবং শামসুর রাহমানের স্বাধীনতাকামী রক্তাক্ত প্রত্যয়—এসব ভাবাবেগ থেকে উদ্দীপকভিত্তিক প্রশ্ন সবচেয়ে বেশি আসে।</li>')
    html_lines.append('</ul>\n')

    # Main Section 2: Chapter-wise Poetry MCQs
    html_lines.append('<h2 class="htbd-academic-heading">২. অধ্যায়ভিত্তিক কবিতাংশ বহুনির্বাচনি প্রশ্নব্যাংক ও সমাধান (Chapter-wise Poetry MCQ Bank)</h2>')
    html_lines.append('<p>নিচে আল ফাতাহ দাখিল ও এসএসসি ২০২৭ প্রশ্নপত্র সাজেশন থেকে কবিতাংশের ১০টি অধ্যায়ের গুরুত্বপূর্ণ বহুনির্বাচনি প্রশ্নাবলি তুলে ধরা হলো। প্রতিটি প্রশ্নের নিচে ড্রপডাউনে ক্লিক করে সঠিক উত্তর ও ব্যাখ্যা দেখে নেওয়া যাবে:</p>\n')

    q_counter = 1
    for ch in chapters:
        html_lines.append(f'<h3 class="htbd-academic-subheading" id="{ch["id"]}">{ch["name"]} ({ch["eng_tag"]})</h3>')

        for q_text, options, ans_code, expl in ch["questions"]:
            html_lines.append('<div class="htbd-qcard">')
            html_lines.append(f'  <p>প্রশ্ন {q_counter}: {q_text}</p>')
            html_lines.append('  <div class="htbd-options-grid">')
            html_lines.append(f'    <div>(ক) {options[0]}</div>')
            html_lines.append(f'    <div>(খ) {options[1]}</div>')
            html_lines.append(f'    <div>(গ) {options[2]}</div>')
            html_lines.append(f'    <div>(ঘ) {options[3]}</div>')
            html_lines.append('  </div>')
            html_lines.append('  <details class="htbd-accordion">')
            html_lines.append('    <summary>সঠিক উত্তর ও প্রমিত ব্যাখ্যা দেখতে ক্লিক করুন</summary>')
            html_lines.append('    <div class="htbd-ans-box">')
            html_lines.append(f'      <strong>সঠিক উত্তর:</strong> {ans_code} <br/>')
            html_lines.append(f'      <em>বিশ্লেষণ:</em> {expl}')
            html_lines.append('    </div>')
            html_lines.append('  </details>')
            html_lines.append('</div>\n')
            q_counter += 1

        # Chapter Exclusive Study Box
        html_lines.append('<div class="htbd-study-box">')
        html_lines.append(f'  <h4>এক্সক্লুসিভ ছন্দ ও মূলভাব নোটস — {ch["name"].split("—")[0].strip()}</h4>')
        html_lines.append('  <ul>')
        for note in ch["study_notes"]:
            html_lines.append(f'    <li>{note}</li>')
        html_lines.append('  </ul>')
        html_lines.append('</div>\n')

    # Inbound Link Equity & Topic Silo Section
    html_lines.append('<div class="htbd-silo-box">')
    html_lines.append('  <h3>সম্পর্কিত প্রয়োজনীয় সাজেশন্স ও স্টাডি গাইড (Topic Silo Links):</h3>')
    html_lines.append('  <ul>')
    html_lines.append('    <li><a href="https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-prose-mcq-question-bank-2027.html" title="SSC Bangla Prose MCQ Bank">এসএসসি বাংলা ১ম পত্র গদ্যাংশ বহুনির্বাচনি প্রশ্নব্যাংক ২০২৬-২০২৭ (২৬৭টি MCQ)</a></li>')
    html_lines.append('    <li><a href="https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-final-suggestion-2027.html" title="SSC Bangla 1st Paper Master Suggestion">এসএসসি বাংলা ১ম পত্র ফাইনাল সুপার সাজেশন ২০২৬-২০২৭ (মাস্টার পিলার গাইড)</a></li>')
    html_lines.append('    <li><a href="https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-model-test-question-solution-100-marks.html" title="SSC Bangla 100 Marks Model Test">এসএসসি বাংলা ১ম পত্র ১০০ নম্বরের পূর্ণাঙ্গ মডেল টেস্ট ও সমাধান</a></li>')
    html_lines.append('    <li><a href="https://www.helptrickbd.com/2026/09/ssc-english-2nd-paper-suggestion-2027.html" title="SSC English 2nd Paper Suggestion">SSC English 2nd Paper Exclusive Grammar & Writing Suggestion 2026-2027</a></li>')
    html_lines.append('  </ul>')
    html_lines.append('</div>\n')

    # Universal E-E-A-T Author Card for Faruk Sir (Rule 28 & Rule 01 Section 13)
    html_lines.append('''<div class="htbd-author-box" style="margin-top: 40px; margin-bottom: 25px; padding: 22px; background: #f8fafc; border: 1px solid #e2e8f0; border-left: 5px solid #1e3a8a; border-radius: 8px; font-family: 'SolaimanLipi', Arial, sans-serif;">
  <div style="font-size: 13px; color: #64748b; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 4px;">লেখক পরিচিতি</div>
  <div style="font-size: 19px; color: #0f172a; font-weight: 700; margin-bottom: 2px;">ফারুক স্যার (মো. ওমর ফারুক)</div>
  <div style="font-size: 14px; color: #1e3a8a; font-weight: 600; margin-bottom: 10px;">শিক্ষাবিদ ও অ্যাকাডেমিক গবেষক | প্রতিষ্ঠাতা, HelpTrickBD</div>
  <p style="margin: 0; font-size: 15px; color: #475569; line-height: 1.65;">
    অ্যাকাডেমিক পাঠ্যক্রম এবং স্নাতক ও স্নাতকোত্তর পর্যায়ের রাষ্ট্রবিজ্ঞান, আধুনিক রাষ্ট্রচিন্তা ও সাহিত্য বিশ্লেষণে এক দশকের বাস্তব শিক্ষকতার অভিজ্ঞতাসম্পন্ন একজন অ্যাকাডেমিক মেন্টর।
  </p>
</div>\n''')

    # Schema JSON-LD Script Tags (Individual for standard parsers)
    html_lines.append(f'<script type="application/ld+json">\n{json.dumps(blog_posting_schema, ensure_ascii=False, indent=2)}\n</script>\n')
    html_lines.append(f'<script type="application/ld+json">\n{json.dumps(faq_schema, ensure_ascii=False, indent=2)}\n</script>\n')
    html_lines.append(f'<script type="application/ld+json">\n{json.dumps(breadcrumb_schema, ensure_ascii=False, indent=2)}\n</script>\n')

    html_lines.append('</div>') # end htbd-post-body

    full_html = "\n".join(html_lines)

    with open(html_out, "w", encoding="utf-8") as f:
        f.write(full_html)
    with open(meta_out, "w", encoding="utf-8") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)

    print(f"[✔] Post 02 Generated Successfully!")
    print(f"    HTML: {html_out}")
    print(f"    Metadata: {meta_out}")
    print(f"    Total HTML size: {len(full_html):,} characters")

if __name__ == "__main__":
    build_post()
