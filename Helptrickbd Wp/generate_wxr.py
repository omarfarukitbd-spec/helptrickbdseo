import json
import re
import html
import datetime
import os
import sys
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

INPUT_JSON = "C:/Users/omarf/.gemini/antigravity-ide/brain/82e71ff7-e9ff-4426-b9cd-63baa3864ab4/scratch/full_blogger_posts.json"
WORKSPACE_DIR = "d:/android/Project/Helptrickbd Wp"

SITE_URL = "https://www.helptrickbd.com"
SITE_TITLE = "Help Trick BD"

with open(INPUT_JSON, "r", encoding="utf-8") as f:
    posts = json.load(f)

print(f"Loaded {len(posts)} full posts from cache.")

def parse_iso_date(iso_str):
    """
    Parses '2026-10-03T14:21:12.000+06:00'
    Returns (local_date_str, gmt_date_str, rfc2822_str)
    """
    if not iso_str:
        now = datetime.datetime.now(datetime.timezone.utc)
        return now.strftime("%Y-%m-%d %H:%M:%S"), now.strftime("%Y-%m-%d %H:%M:%S"), now.strftime("%a, %d %b %Y %H:%M:%S +0000")
    
    m = re.match(r'(\d{4}-\d{2}-\d{2})T(\d{2}:\d{2}:\d{2})(?:\.\d+)?([+-]\d{2}:\d{2}|Z)?', iso_str)
    if m:
        date_part, time_part, tz_part = m.groups()
        dt_str = f"{date_part} {time_part}"
        dt = datetime.datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
        
        if tz_part and tz_part != "Z":
            sign = 1 if tz_part[0] == '+' else -1
            tz_hours = int(tz_part[1:3])
            tz_minutes = int(tz_part[4:6])
            offset = datetime.timedelta(hours=tz_hours, minutes=tz_minutes)
            if sign > 0:
                dt_gmt = dt - offset
            else:
                dt_gmt = dt + offset
        else:
            dt_gmt = dt
            
        rfc2822_str = dt_gmt.strftime("%a, %d %b %Y %H:%M:%S +0000")
        return dt.strftime("%Y-%m-%d %H:%M:%S"), dt_gmt.strftime("%Y-%m-%d %H:%M:%S"), rfc2822_str
        
    fallback = iso_str[:19].replace('T', ' ')
    return fallback, fallback, datetime.datetime.now(datetime.timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")

def clean_text_for_seo(text):
    clean = re.sub(r'<[^>]+>', ' ', text)
    clean = html.unescape(clean)
    clean = re.sub(r'\s+', ' ', clean).strip()
    return clean

def extract_meta_description(title, content):
    clean_content = re.sub(r'<figure.*?</figure>', '', content, flags=re.DOTALL)
    clean_content = re.sub(r'<style.*?</style>', '', clean_content, flags=re.DOTALL)
    clean_content = re.sub(r'<script.*?</script>', '', clean_content, flags=re.DOTALL)
    clean = clean_text_for_seo(clean_content)
    if len(clean) > 155:
        desc = clean[:155]
        last_space = desc.rfind(' ')
        if last_space > 100:
            desc = desc[:last_space]
        return desc + "..."
    if len(clean) < 50:
        return f"{title} সম্পর্কে বিস্তারিত নির্দেশিকা, নিয়মাবলী ও সম্পূর্ণ গাইডলাইন জানুন Help Trick BD-তে।"
    return clean

def extract_focus_keyword(title):
    t = html.unescape(title.strip())
    
    # 1. High-Intent Direct Keyword Patterns
    if "বার্ষিক পরীক্ষার মানবণ্টন" in t:
        return "বার্ষিক পরীক্ষার মানবণ্টন ও প্রস্তুতি"
    if "পাবলিক বিশ্ববিদ্যালয় ভর্তি যোগ্যতা" in t:
        return "পাবলিক বিশ্ববিদ্যালয় ভর্তি যোগ্যতা ২০২৬"
    if "অনার্স ২য় বর্ষ পরীক্ষার রুটিন" in t or "অনার্স ২য় বর্ষ পরীক্ষার রুটিন" in t:
        return "অনার্স ২য় বর্ষ পরীক্ষার রুটিন"
    if "অনার্স ২য় বর্ষ পরীক্ষার গাইড" in t or "অনার্স ২য় বর্ষ পরীক্ষার গাইড" in t:
        return "অনার্স ২য় বর্ষ পরীক্ষার গাইড"
    if "ডিগ্রি ২য় বর্ষ ইনকোর্স" in t or "ডিগ্রি ২য় বর্ষ ইনকোর্স" in t:
        return "ডিগ্রি ২য় বর্ষ ইনকোর্স নম্বর এন্ট্রি"
    if "ডিগ্রি ২য় বর্ষ" in t or "ডিগ্রি ২য় বর্ষ" in t:
        return "ডিগ্রি ২য় বর্ষ পরীক্ষার গাইড"
    if "পরীক্ষা ডিজিটালাইজেশন" in t:
        return "জাতীয় বিশ্ববিদ্যালয় পরীক্ষা ডিজিটালাইজেশন"
    if "অনলাইন ফর্ম পূরণ" in t or "ফর্ম পূরণ" in t:
        return "অনার্স ২য় বর্ষ ফর্ম পূরণ"
    if "প্রমোশনের নিয়মাবলী" in t or "প্রমোশনের নিয়মাবলী" in t:
        return "অনার্স প্রমোশনের নিয়মাবলী"
    if "ইনকোর্স নম্বর এন্ট্রি" in t:
        return "ডিগ্রি ইনকোর্স নম্বর এন্ট্রি"

    # SSC & Dakhil
    if "বাংলা ১ম পত্র" in t or "Bangla 1st Paper" in t:
        if "কবিতাংশ" in t:
            if "বহুনির্বাচনি" in t or "MCQ" in t:
                return "এসএসসি বাংলা ১ম পত্র কবিতাংশ MCQ"
            return "এসএসসি বাংলা ১ম পত্র কবিতাংশ সৃজনশীল"
        elif "গদ্যাংশ" in t:
            if "বহুনির্বাচনি" in t or "MCQ" in t:
                return "এসএসসি বাংলা ১ম পত্র গদ্যাংশ MCQ"
            return "এসএসসি বাংলা ১ম পত্র গদ্যাংশ সৃজনশীল"
        elif "মডেল টেস্ট" in t:
            return "এসএসসি বাংলা ১ম পত্র মডেল টেস্ট"
        elif "সংক্ষিপ্ত প্রশ্নব্যাংক" in t or "SAQ" in t:
            return "এসএসসি বাংলা ১ম পত্র সংক্ষিপ্ত প্রশ্ন"
        elif "বহুনির্বাচনি" in t or "MCQ" in t:
            return "এসএসসি বাংলা ১ম পত্র MCQ"
        return "এসএসসি বাংলা ১ম পত্র সাজেশন"

    if "SSC English 2nd Paper" in t:
        return "SSC English 2nd Paper Suggestion"
    if "Suffix and Prefix" in t:
        return "SSC Suffix and Prefix Rules"
    if "Sentence Connectors" in t:
        return "SSC Sentence Connectors Rules"
    if "Tag Questions" in t:
        return "SSC Tag Questions Rules"
    if "Changing Sentences" in t:
        return "SSC Changing Sentences Rules"
    if "Right Form of Verbs" in t:
        return "SSC Right Form of Verbs Suggestion"
    if "Substitution Table" in t:
        return "SSC Substitution Table Suggestion"
    if "Preposition" in t:
        return "SSC Preposition & Gap Filling"
    if "Seen Passage" in t:
        return "SSC English Seen Passage Suggestion"
    if "Unseen Passage" in t:
        return "SSC English Unseen Passage Suggestion"
    if "Completing Story" in t:
        return "SSC Completing Story Suggestion"
    if "Writing Part" in t:
        return "SSC English 2nd Paper Writing Part"
    if "Matching" in t or "Rearrange" in t:
        return "SSC English Matching & Rearrange"
    if "Model Test" in t:
        return "SSC English Model Test"
    if "English 1st Paper" in t:
        return "SSC English 1st Paper Suggestion"

    # ICT
    if "কম্পিউটার ভাইরাস" in t or "সাইবার নিরাপত্তা" in t:
        return "কম্পিউটার ভাইরাস ও সাইবার নিরাপত্তা"
    if "ক্লাউড কম্পিউটিং" in t:
        return "ক্লাউড কম্পিউটিং প্রকারভেদ ও গুরুত্ব"
    if "কম্পিউটারের প্রজন্ম" in t:
        return "কম্পিউটারের প্রজন্ম বৈশিষ্ট্য ও তুলনা"
    if "কম্পিউটারের প্রকারভেদ" in t:
        return "কম্পিউটারের প্রকারভেদ ও শ্রেণীবিভাগ"
    if "কম্পিউটারের ইতিহাস" in t:
        return "কম্পিউটারের ইতিহাস ও বিবর্তন"
    if "কম্পিউটার কাকে বলে" in t:
        return "কম্পিউটার কাকে বলে ইতিহাস ও বৈশিষ্ট্য"

    # BCS & Job
    if "বিসিএস প্রিলিমিনারি" in t or "BCS Preliminary" in t:
        return "বিসিএস প্রিলিমিনারি নম্বর বণ্টন"
    if "প্রাথমিক শিক্ষক নিয়োগ" in t or "প্রাইমারি শিক্ষক নিয়োগ" in t or "ভাইভা প্রস্তুতি" in t:
        return "প্রাথমিক শিক্ষক নিয়োগ ভাইভা প্রস্তুতি"
    if "সহজ গাইড" in t and "চাকরি" in t:
        return "চাকরি ও বিসিএস প্রস্তুতির সহজ গাইড"
    if "সাসটেইনেবল ডেভেলপমেন্ট গোলস" in t or "SDG" in t:
        return "এসডিজি ও বাংলাদেশ লক্ষ্যমাত্রা"

    # Islamic
    if "মিলাদ শরীফ" in t or "ক্বাসিদা" in t:
        if "ইয়া নবী সালাম আলাইকা" in t:
            return "ইয়া নবী সালাম আলাইকা লিরিক্স ও ব্যাখ্যা"
        if "মারহাবা" in t:
            return "মিলাদ শরীফের ক্বাসিদা মারহাবা লিরিক্স"
        if "সালাতুন" in t:
            return "সালাতুন ইয়া রাসুলুল্লাহ আলাইকুম লিরিক্স"
        return "মিলাদ শরীফ ক্বাসিদা লিরিক্স"
    if "আল্লাহ আল্লাহ আল্লাহু" in t:
        return "আল্লাহ আল্লাহ আল্লাহু লা ইলাহা ইল্লাহু লিরিক্স"
    if "আল্লাহুম্মা সাল্লি আলা" in t:
        return "আল্লাহুম্মা সাল্লি আলা সাইয়্যিদিনা মুহাম্মদ লিরিক্স"
    if "আলা হযরত" in t:
        return "ক্বালা calma আলা হযরত আক্বিদা ও কাব্যদর্শন"
    if "কুরআন সংরক্ষণ" in t:
        return "কুরআন সংরক্ষণ ও মুখস্থকরণের ফজিলত"
    if "সিদ্দিকে আকবর" in t:
        return "রাসূল (স.) প্রেমে সিদ্দিকে আকবরের আত্মত্যাগ"
    if "তালেবে ইলম" in t:
        return "তালেবে ইলমদের প্রতি নসিহত ও ইলমের পথ"
    if "ইমামে আযম" in t:
        return "ইমামে আযম ও ইমাম বুখারী জীবনী পর্যালোচনা"
    if "আহলে বাইত" in t:
        return "আহলে বাইতের ভালোবাসার গুরুত্ব হাদিস"
    if "জামেয়া" in t or "পীরে বাঙ্গাল" in t:
        return "জামেয়া আহমদিয়া সুন্নিয়া ইতিহাস ও ঐতিহ্য"
    if "ওয়াদা রক্ষা" in t:
        return "ইসলামে ওয়াদা রক্ষার গুরুত্ব ও বিধান"

    # Political Science
    if "ভূরাজনীতি" in t:
        return "ভূরাজনীতি কাকে বলে উপাদান ও গুরুত্ব"
    if "যুক্তরাষ্ট্রীয় সরকার" in t:
        return "যুক্তরাষ্ট্রীয় সরকার বৈশিষ্ট্য ও গুণাগুণ"
    if "সার্বভৌমত্ব" in t:
        if "একত্ববাদ" in t or "বহুবাদ" in t:
            return "সার্বভৌমত্বের একত্ববাদ ও বহুত্ববাদ"
        return "সার্বভৌমত্ব কাকে বলে বৈশিষ্ট্য ও শ্রেণীবিভাগ"
    if "সরকার ও রাষ্ট্রের পার্থক্য" in t or "সরকার কি" in t:
        return "সরকার কাকে বলে রাষ্ট্র ও সরকারের পার্থক্য"
    if "কল্যাণ রাষ্ট্র" in t:
        return "কল্যাণ রাষ্ট্র কাকে বলে বৈশিষ্ট্য ও কার্যাবলী"
    if "সংরক্ষিত আসন" in t:
        return "জাতীয় সংসদে নারীদের সংরক্ষিত আসনের গুরুত্ব"
    if "শিল্প জাতীয়করণ" in t:
        return "শিল্প জাতীয়করণ কী সমস্যা ও ফলাফল"
    if "নারী আন্দোলন" in t:
        return "নারী আন্দোলন উৎপত্তি ও অস্তিত্ব রক্ষার লড়াই"
    if "খেলার সাথী" in t:
        return "সামাজিকীকরণে খেলার সাথীর ভূমিকা"
    if "জনসংখ্যা বৃদ্ধির প্রভাব" in t:
        return "পরিবেশের ওপর জনসংখ্যা বৃদ্ধির প্রভাব"
    if "জনসংখ্যা পরিবর্তন" in t:
        return "জনসংখ্যা পরিবর্তনের প্রধান নিয়ামকসমূহ"
    if "পরিবেশ কাকে বলে" in t:
        return "পরিবেশ কাকে বলে উপাদান ও শ্রেণীবিভাগ"
    if "প্রতিবেশ কি" in t:
        return "প্রতিবেশ কি পরিবেশ ও প্রতিবেশের সম্পর্ক"
    if "সংস্কৃতি কি" in t:
        return "সংস্কৃতি কি বৈশিষ্ট্য ও বাঙালির সংস্কৃতি"
    if "গ্রামীণ ও শহরের সংস্কৃতি" in t:
        return "গ্রামীণ ও শহরের সংস্কৃতির পার্থক্য"
    if "রাজনৈতিক অর্থনীতি" in t:
        return "রাজনৈতিক অর্থনীতি কাকে বলে"
    if "নারী দশক" in t:
        return "নারী দশকের লক্ষ্য ও উদ্দেশ্য"
    if "পিতৃতন্ত্র" in t:
        return "পিতৃতন্ত্র কাকে বলে বৈশিষ্ট্য ও প্রভাব"
    if "রাজনীতিতে নারীর অংশগ্রহণ" in t:
        return "রাজনীতিতে নারীর অংশগ্রহণ বলতে কী বোঝায়"
    if "নারীর ক্ষমতায়নে এনজিও" in t:
        return "নারীর ক্ষমতায়নে এনজিও-র ভূমিকা"
    if "নারী নির্যাতন" in t:
        return "নারী নির্যাতন কী কারণ ও প্রতিকার"
    if "১৯০৯ সালের ভারত শাসন আইন" in t or "মর্লে-মিন্টো" in t:
        return "১৯০৯ সালের ভারত শাসন আইন বৈশিষ্ট্য"
    if "রাজা রামমোহন রায়" in t:
        return "সমাজ সংস্কারে রাজা রামমোহন রায়ের অবদান"
    if "মহাত্মা গান্ধী" in t:
        return "মহাত্মা গান্ধীর জনপ্রিয়তার কারণ ও রাজনৈতিক আদর্শ"
    if "ইমাম গাজ্জালি" in t:
        return "রাষ্ট্রচিন্তায় ইমাম গাজ্জালির অবদান"
    if "বাজেট কী" in t:
        return "বাজেট কী গুরুত্ব ও অর্থনীতিতে ভূমিকা"
    if "১০০টি অর্থনীতি" in t:
        return "১০০টি অর্থনীতির গুরুত্বপূর্ণ সংক্ষিপ্ত প্রশ্নোত্তর"
    if "রাষ্ট্রের সংজ্ঞা" in t:
        return "রাষ্ট্রের সংজ্ঞা উপাদান ও লক্ষ্য উদ্দেশ্য"
    if "মুদ্রাস্ফীতি" in t:
        return "বাংলাদেশে মুদ্রাস্ফীতি কারণ ও রোধের উপায়"
    if "মৌলিক অর্থনীতির বৈশিষ্ট্য" in t:
        return "বাংলাদেশের মৌলিক অর্থনীতির বৈশিষ্ট্য ও সমস্যা"
    if "রেমিট্যান্স" in t:
        return "রেমিট্যান্স কী বাংলাদেশের অর্থনীতিতে গুরুত্ব"
    if "খেলাফত আন্দোলন" in t:
        return "খেলাফত আন্দোলনের ব্যর্থতার কারণসমূহ"
    if "ঈশ্বরচন্দ্র বিদ্যাসাগর" in t:
        return "সমাজ সংস্কারে ঈশ্বরচন্দ্র বিদ্যাসাগরের অবদান"
    if "শেরে বাংলা ফজলুল হক" in t:
        return "শেরে বাংলা এ কে ফজলুল হকের অবদান"
    if "লেনিন" in t:
        if "দলীয় তত্ত্ব" in t:
            return "লেনিনের দলীয় তত্ত্ব বিশ্লেষণ"
        if "সাম্রাজ্যবাদ" in t:
            return "লেনিনের সাম্রাজ্যবাদ তত্ত্ব ও মার্কসবাদ"
        return "ভ্লাদিমির লেনিনের রাজনৈতিক দর্শন"
    if "বাংলাদেশের জনসংখ্যা" in t:
        return "বাংলাদেশের জনসংখ্যা পরিস্থিতি ও বৈশিষ্ট্য"
    if "কৃষি খাতে উন্নয়ন" in t or "কৃষি খাতে সরকার" in t:
        return "বাংলাদেশে কৃষি খাতে উন্নয়নে সরকারের পদক্ষেপ"
    if "প্রাণিসম্পদ গবেষণা" in t or "BLRI" in t:
        return "বাংলাদেশ প্রাণিসম্পদ গবেষণা ইনস্টিটিউট"
    if "বনজ সম্পদ" in t:
        return "বাংলাদেশের বনজ সম্পদ ও প্রতিষ্ঠান"
    if "কৃষি প্রযুক্তি" in t or "কৃষি গবেষণা" in t:
        return "বাংলাদেশের কৃষি গবেষণা প্রতিষ্ঠান ও শস্যের জাত"
    if "রাজনৈতিক দল" in t:
        return "সরকার ও রাজনৈতিক দল গণতান্ত্রিক চর্চা"
    if "উন্নয়নশীল অর্থনীতি" in t:
        return "উন্নয়নশীল দেশের অর্থনীতিতে রাজনীতির ভূমিকা"
    if "বাংলাদেশের অর্থনীতি" in t:
        return "বাংলাদেশের অর্থনীতির ইতিহাস ও বর্তমান রূপরেখা"
    if "এসডিজি" in t:
        return "টেকসই উন্নয়ন লক্ষ্যমাত্রা এসডিজি বাংলাদেশ"
    if "বাগধারা" in t:
        return "বাংলা বাগধারা সংকলন অর্থসহ তালিকা"
    if "বাংলাদেশের ইতিহাস" in t:
        return "বাংলাদেশের পূর্ণাঙ্গ ইতিহাস ও রাজনৈতিক পটভূমি"
    if "জাতীয়তাবাদ" in t:
        return "সাম্প্রতিক জাতীয়তাবাদ বলতে কী বোঝায়"
    if "রাষ্ট্রনায়কত্ব" in t:
        return "রাষ্ট্রনায়কত্ব কী সফল রাষ্ট্রনায়কের গুণাবলী"
    if "রাজনৈতিক অর্থনীতি" in t:
        return "রাজনৈতিক অর্থনীতি কাকে বলে"
    if "রাষ্ট্রচিন্তা কাকে বলে" in t:
        return "রাষ্ট্রচিন্তা কাকে বলে ও পরিধি"
    if "সাম্প্রতিক কালের রাষ্ট্রচিন্তা" in t:
        return "সাম্প্রতিক কালের রাষ্ট্রচিন্তা"
    if "প্রাচ্যের রাষ্ট্রচিন্তা" in t:
        return "প্রাচ্যের রাষ্ট্রচিন্তা পাঠের গুরুত্ব"
    if "বইয়ের তালিকা" in t:
        return "রাষ্ট্রবিজ্ঞান অনার্স পাঠ্য বইয়ের তালিকা"
    if "মাস্টার্স সাজেশন্স" in t or "মাস্টার্স পরীক্ষা" in t:
        return "রাষ্ট্রবিজ্ঞান মাস্টার্স চূড়ান্ত সাজেশন"
    if "আলিম পরীক্ষার রুটিন" in t or "Alim Exam" in t:
        return "আলিম পরীক্ষার রুটিন"
    if "সার্টিফিকেট নাম ও বয়স সংশোধন" in t:
        return "সার্টিফিকেট নাম ও বয়স সংশোধনের নিয়ম"
    if "নামতা ১ থেকে ২০" in t:
        return "নামতা ১ থেকে ২০"

    # Fallback
    core = re.split(r'[:|–—\-]', t)[0].strip()
    core = re.sub(r'[?,;:!]', '', core).strip()
    words = core.split()
    if len(words) > 5:
        return " ".join(words[:4])
    return core

def determine_categories_and_tags(title, orig_cats, content):
    t = title.lower()
    raw_title = title
    cats = [c.lower() for c in orig_cats]
    
    categories = []
    tags = set()
    primary_slug = ""
    
    # 1. Political Science
    if any("political science" in c for c in cats):
        categories.append({"name": "Political Science", "slug": "political-science", "parent": None})
        primary_slug = "political-science"
        tags.add("রাষ্ট্রবিজ্ঞান")
        tags.add("Political Science")
        tags.add("অনার্স রাষ্ট্রবিজ্ঞান")
        if "মাস্টার্স" in raw_title:
            tags.add("মাস্টার্স রাষ্ট্রবিজ্ঞান")
        if "সাজেশন" in raw_title:
            tags.add("রাষ্ট্রবিজ্ঞান সাজেশন")
            
    # 2. Job Preparation
    if any("job study" in c for c in cats):
        categories.append({"name": "Job Preparation", "slug": "job-preparation", "parent": None})
        if not primary_slug:
            primary_slug = "job-preparation"
        tags.add("চাকরি প্রস্তুতি")
        tags.add("Job Preparation")
        if "বিসিএস" in raw_title:
            tags.add("বিসিএস প্রস্তুতি")
            tags.add("BCS Preliminary")
        if "শিক্ষক নিয়োগ" in raw_title:
            tags.add("প্রাথমিক শিক্ষক নিয়োগ")
            tags.add("Primary Teacher Exam")
            
    # 3. ICT & Technology
    if any("ict guide" in c for c in cats):
        categories.append({"name": "ICT & Technology", "slug": "ict-technology", "parent": None})
        if not primary_slug:
            primary_slug = "ict-technology"
        tags.add("আইসিটি")
        tags.add("ICT Guide")
        tags.add("কম্পিউটার শিক্ষা")
        if "সাইবার" in raw_title:
            tags.add("সাইবার নিরাপত্তা")
        if "ক্লাউড" in raw_title:
            tags.add("ক্লাউড কম্পিউটিং")
            
    # 4. Islamic Article
    if any("islamic article" in c for c in cats):
        categories.append({"name": "Islamic Article", "slug": "islamic-article", "parent": None})
        if not primary_slug:
            primary_slug = "islamic-article"
        tags.add("ইসলামিক প্রবন্ধ")
        tags.add("ইসলামিক জীবনবিধান")
        if "ক্বাসিদা" in raw_title or "মিলাদ" in raw_title:
            tags.add("মিলাদ শরীফ")
            tags.add("ক্বাসিদা লিরিক্স")
        if "কুরআন" in raw_title:
            tags.add("কুরআন ও হাদিস")
            
    # 5. SSC & Dakhil
    if any("ssc" in c or "dakhil" in c or "bangla 1st" in c for c in cats) or "ssc" in t or "দাখিল" in raw_title:
        categories.append({"name": "SSC & Dakhil", "slug": "ssc-dakhil", "parent": None})
        if not primary_slug:
            primary_slug = "ssc-dakhil"
        tags.add("এসএসসি পরীক্ষা")
        tags.add("SSC Suggestion")
        if "দাখিল" in raw_title or any("dakhil" in c for c in cats):
            tags.add("দাখিল পরীক্ষা")
            tags.add("Dakhil Suggestion")
        if "বাংলা ১ম পত্র" in raw_title or "bangla 1st" in t:
            categories.append({"name": "Bangla 1st Paper", "slug": "bangla-1st-paper", "parent": "ssc-dakhil"})
            tags.add("বাংলা ১ম পত্র")
            tags.add("Bangla 1st Paper")
        if "ইংরেজি" in raw_title or "english" in t:
            categories.append({"name": "English 2nd Paper", "slug": "english-2nd-paper", "parent": "ssc-dakhil"})
            tags.add("ইংরেজি ২য় পত্র")
            tags.add("SSC English 2nd Paper")
        if "সৃজনশীল" in raw_title or "cq" in t:
            tags.add("সৃজনশীল প্রশ্নব্যাংক")
        if "বহুনির্বাচনি" in raw_title or "mcq" in t:
            tags.add("MCQ প্রশ্নব্যাংক")
            
    # 6. Education Guide
    if any("education" in c for c in cats) or "অনার্স" in raw_title or "ডিগ্রি" in raw_title or not categories:
        categories.append({"name": "Education Guide", "slug": "education-guide", "parent": None})
        if not primary_slug:
            primary_slug = "education-guide"
        tags.add("শিক্ষা নির্দেশিকা")
        tags.add("Education Guide")
        if "জাতীয় বিশ্ববিদ্যালয়" in raw_title or "জাতীয় বিশ্ববিদ্যালয়" in raw_title or "nu" in t:
            categories.append({"name": "National University", "slug": "national-university", "parent": "education-guide"})
            tags.add("জাতীয় বিশ্ববিদ্যালয়")
            tags.add("National University")
            if "অনার্স ২য় বর্ষ" in raw_title or "অনার্স ২য় বর্ষ" in raw_title:
                tags.add("অনার্স ২য় বর্ষ")
                tags.add("NU Honours 2nd Year")
            elif "ডিগ্রি ২য় বর্ষ" in raw_title or "ডিগ্রি ২য় বর্ষ" in raw_title:
                tags.add("ডিগ্রি ২য় বর্ষ")
                tags.add("NU Degree 2nd Year")
            if "রুটিন" in raw_title:
                tags.add("পরীক্ষার রুটিন")
        elif "ভর্তি" in raw_title:
            categories.append({"name": "University Admission", "slug": "university-admission", "parent": "education-guide"})
            tags.add("বিশ্ববিদ্যালয় ভর্তি")
        elif "সার্টিফিকেট" in raw_title or "বোর্ড" in raw_title:
            tags.add("ঢাকা শিক্ষাবোর্ড")
            tags.add("সার্টিফিকেট সংশোধন")

    # Add year & generic tags
    if "২০২৬" in raw_title or "2026" in raw_title:
        tags.add("২০২৬")
    if "২০২৭" in raw_title or "2027" in raw_title:
        tags.add("২০২৭")
    if "হ্যান্ডনোট" in raw_title:
        tags.add("হ্যান্ডনোট")

    unique_cats = []
    seen_cats = set()
    for c in categories:
        if c["slug"] not in seen_cats:
            seen_cats.add(c["slug"])
            unique_cats.append(c)

    def slugify(text):
        s = text.lower().strip()
        s = re.sub(r'[\s_]+', '-', s)
        s = re.sub(r'[^\w\-]', '', s)
        if not s:
            s = f"tag-{abs(hash(text)) % 10000}"
        return s

    tag_objects = []
    for t_text in sorted(list(tags)):
        tag_objects.append({
            "name": t_text,
            "slug": slugify(t_text)
        })

    return unique_cats, tag_objects, primary_slug

def clean_and_optimize_post_body(raw_html, post_title):
    soup = BeautifulSoup(raw_html, 'html.parser')
    
    # 1. Remove script tags
    for s in soup.find_all('script'):
        s.decompose()
        
    # 2. Remove Blogger theme widgets (navigation, pager, share, labels)
    for cls in ['next-post-link', 'prev-post-link', 'label-head', 'post-share', 'blog-pager', 'post-nav', 'post-next', 'post-prev']:
        for el in soup.find_all(class_=re.compile(cls, re.I)):
            el.decompose()
            
    cleaned = str(soup)
    
    # 3. Replace Blogger jump breaks with WordPress <!--more-->
    cleaned = re.sub(r'<a\s+name=[\'"]more[\'"]\s*>(?:</a>)?', '\n<!--more-->\n', cleaned, flags=re.I)
    
    # 4. Rewrite internal links from arafatitbd.blogspot.com to helptrickbd.com
    def link_repl(match):
        full_url = match.group(1)
        clean_url = full_url.split('#')[0]
        m = re.search(r'/([^/]+)\.html', clean_url)
        if m:
            s = m.group(1)
            return f'href="https://www.helptrickbd.com/{s}/"'
        return 'href="https://www.helptrickbd.com/"'
        
    cleaned = re.sub(r'href=[\'"]https?://arafatitbd\.blogspot\.com([^\'"]*)[\'"]', link_repl, cleaned)
    # Also clean any plain text or unquoted occurrences
    cleaned = re.sub(r'https?://arafatitbd\.blogspot\.com/[0-9]{4}/[0-9]{2}/([^/]+)\.html(?:#more)?', r'https://www.helptrickbd.com/\1/', cleaned)
    cleaned = re.sub(r'https?://arafatitbd\.blogspot\.com', 'https://www.helptrickbd.com', cleaned)

    # 5. Clean images: lazy loading, async decoding, descriptive alt
    def img_repl(m):
        tag = m.group(0)
        if 'loading=' not in tag:
            tag = tag[:-1] + ' loading="lazy">' if tag.endswith('>') else tag + ' loading="lazy"'
        if 'decoding=' not in tag:
            tag = tag[:-1] + ' decoding="async">' if tag.endswith('>') else tag + ' decoding="async"'
        if 'alt=' not in tag or 'alt=""' in tag or "alt=''" in tag:
            safe_title = html.escape(post_title, quote=True)
            if 'alt=""' in tag:
                tag = tag.replace('alt=""', f'alt="{safe_title}"')
            elif "alt=''" in tag:
                tag = tag.replace("alt=''", f'alt="{safe_title}"')
            else:
                tag = tag[:-1] + f' alt="{safe_title}">' if tag.endswith('>') else tag + f' alt="{safe_title}"'
        return tag
        
    cleaned = re.sub(r'<img[^>]+>', img_repl, cleaned)
    cleaned = re.sub(r'<div class="separator"[^>]*>', '<div>', cleaned)
    
    return cleaned.strip()

# Process all 134 items
all_defined_categories = {}
all_defined_tags = {}
processed_items = []

for idx, p in enumerate(posts):
    post_id = idx + 1
    raw_title = p.get("title", {}).get("$t", "No Title")
    clean_title = html.unescape(raw_title).strip()
    
    orig_url = ""
    for l in p.get("link", []):
        if l.get("rel") == "alternate":
            orig_url = l.get("href", "")
            break
            
    slug = ""
    if orig_url:
        m = re.search(r'/([^/]+)\.html$', orig_url)
        if m:
            slug = m.group(1)
            
    if not slug:
        slug = f"post-{post_id}"
        
    published_iso = p.get("published", {}).get("$t", "")
    updated_iso = p.get("updated", {}).get("$t", "")
    
    post_date, post_date_gmt, pubDate_rfc = parse_iso_date(published_iso)
    post_modified, post_modified_gmt, _ = parse_iso_date(updated_iso)
    
    author_name = "ayesha"
    orig_cats = [c.get("term", "") for c in p.get("category", []) if "term" in c]
    
    raw_content = p.get("content", {}).get("$t", "")
    opt_content = clean_and_optimize_post_body(raw_content, clean_title)
    
    # Extract first image for featured / social preview
    imgs = re.findall(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]', opt_content)
    featured_img = imgs[0] if imgs else ""
    
    meta_desc = extract_meta_description(clean_title, opt_content)
    focus_kw = extract_focus_keyword(clean_title)
    seo_title = f"{clean_title} | Help Trick BD"
    
    post_categories, post_tags, primary_cat_slug = determine_categories_and_tags(clean_title, orig_cats, opt_content)
    
    for c in post_categories:
        all_defined_categories[c["slug"]] = c
    for t in post_tags:
        all_defined_tags[t["slug"]] = t
        
    word_count = len(re.findall(r'\b\w+\b', clean_text_for_seo(opt_content)))
    
    processed_items.append({
        "post_id": post_id,
        "title": clean_title,
        "slug": slug,
        "orig_url": orig_url,
        "post_date": post_date,
        "post_date_gmt": post_date_gmt,
        "pubDate_rfc": pubDate_rfc,
        "post_modified": post_modified,
        "post_modified_gmt": post_modified_gmt,
        "author": author_name,
        "categories": post_categories,
        "tags": post_tags,
        "primary_cat_slug": primary_cat_slug,
        "focus_keyword": focus_kw,
        "meta_desc": meta_desc,
        "seo_title": seo_title,
        "featured_image": featured_img,
        "content": opt_content,
        "word_count": word_count
    })

print(f"Successfully processed {len(processed_items)} posts.")
print(f"Total Unique Categories: {len(all_defined_categories)}")
print(f"Total Unique Tags: {len(all_defined_tags)}")

# Helper to build WXR string for a given subset of items
def build_wxr_xml(items_subset, batch_title_suffix=""):
    # Collect categories and tags used by this subset
    sub_cats = {}
    sub_tags = {}
    for it in items_subset:
        for c in it["categories"]:
            sub_cats[c["slug"]] = c
        for t in it["tags"]:
            sub_tags[t["slug"]] = t
            
    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8" ?>',
        f'<!-- WordPress eXtended RSS (WXR 1.2) - Help Trick BD Migration {batch_title_suffix} -->',
        '<rss version="2.0"',
        '    xmlns:excerpt="http://wordpress.org/export/1.2/excerpt/"',
        '    xmlns:content="http://purl.org/rss/1.0/modules/content/"',
        '    xmlns:wfw="http://wellformedweb.org/CommentAPI/"',
        '    xmlns:dc="http://purl.org/dc/elements/1.1/"',
        '    xmlns:wp="http://wordpress.org/export/1.2/"',
        '>',
        '<channel>',
        f'    <title><![CDATA[{SITE_TITLE}]]></title>',
        f'    <link>{SITE_URL}</link>',
        '    <description><![CDATA[শিক্ষা, তথ্যপ্রযুক্তি ও ক্যারিয়ার বিষয়ক নির্ভরযোগ্য গাইডলাইন]]></description>',
        f'    <pubDate>{datetime.datetime.now(datetime.timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")}</pubDate>',
        '    <language>bn-BD</language>',
        '    <wp:wxr_version>1.2</wp:wxr_version>',
        f'    <wp:base_site_url>{SITE_URL}</wp:base_site_url>',
        f'    <wp:base_blog_url>{SITE_URL}</wp:base_blog_url>',
        '',
        '    <!-- Author Definition -->',
        '    <wp:author>',
        '        <wp:author_id>1</wp:author_id>',
        '        <wp:author_login><![CDATA[ayesha]]></wp:author_login>',
        '        <wp:author_email><![CDATA[admin@helptrickbd.com]]></wp:author_email>',
        '        <wp:author_display_name><![CDATA[ayesha]]></wp:author_display_name>',
        '        <wp:author_first_name><![CDATA[Ayesha]]></wp:author_first_name>',
        '        <wp:author_last_name><![CDATA[]]></wp:author_last_name>',
        '    </wp:author>',
        ''
    ]

    # Category definitions
    term_id_counter = 1
    cat_term_ids = {}
    for slug, c in sorted(sub_cats.items()):
        cat_term_ids[slug] = term_id_counter
        parent_str = f'<wp:category_parent><![CDATA[{c["parent"]}]]></wp:category_parent>' if c["parent"] else '<wp:category_parent></wp:category_parent>'
        xml_lines.append('    <wp:category>')
        xml_lines.append(f'        <wp:term_id>{term_id_counter}</wp:term_id>')
        xml_lines.append(f'        <wp:category_nicename><![CDATA[{c["slug"]}]]></wp:category_nicename>')
        xml_lines.append(f'        {parent_str}')
        xml_lines.append(f'        <wp:cat_name><![CDATA[{c["name"]}]]></wp:cat_name>')
        xml_lines.append('    </wp:category>')
        term_id_counter += 1

    xml_lines.append('')

    # Tag definitions
    for slug, t in sorted(sub_tags.items()):
        xml_lines.append('    <wp:tag>')
        xml_lines.append(f'        <wp:term_id>{term_id_counter}</wp:term_id>')
        xml_lines.append(f'        <wp:tag_slug><![CDATA[{t["slug"]}]]></wp:tag_slug>')
        xml_lines.append(f'        <wp:tag_name><![CDATA[{t["name"]}]]></wp:tag_name>')
        xml_lines.append('    </wp:tag>')
        term_id_counter += 1

    xml_lines.append('')

    # Items
    def safe_cdata(text):
        # Escape any accidental CDATA closure in text
        return text.replace("]]>", "]]]]><![CDATA[>")

    for it in items_subset:
        xml_lines.append('    <item>')
        xml_lines.append(f'        <title><![CDATA[{safe_cdata(it["title"])}]]></title>')
        xml_lines.append(f'        <link>{SITE_URL}/{it["slug"]}/</link>')
        xml_lines.append(f'        <pubDate>{it["pubDate_rfc"]}</pubDate>')
        xml_lines.append('        <dc:creator><![CDATA[ayesha]]></dc:creator>')
        xml_lines.append(f'        <guid isPermaLink="false">{SITE_URL}/?p={it["post_id"]}</guid>')
        xml_lines.append('        <description></description>')
        xml_lines.append(f'        <content:encoded><![CDATA[{safe_cdata(it["content"])}]]></content:encoded>')
        xml_lines.append(f'        <excerpt:encoded><![CDATA[{safe_cdata(it["meta_desc"])}]]></excerpt:encoded>')
        xml_lines.append(f'        <wp:post_id>{it["post_id"]}</wp:post_id>')
        xml_lines.append(f'        <wp:post_date><![CDATA[{it["post_date"]}]]></wp:post_date>')
        xml_lines.append(f'        <wp:post_date_gmt><![CDATA[{it["post_date_gmt"]}]]></wp:post_date_gmt>')
        xml_lines.append('        <wp:comment_status><![CDATA[open]]></wp:comment_status>')
        xml_lines.append('        <wp:ping_status><![CDATA[closed]]></wp:ping_status>')
        xml_lines.append(f'        <wp:post_name><![CDATA[{it["slug"]}]]></wp:post_name>')
        xml_lines.append('        <wp:status><![CDATA[publish]]></wp:status>')
        xml_lines.append('        <wp:post_parent>0</wp:post_parent>')
        xml_lines.append('        <wp:menu_order>0</wp:menu_order>')
        xml_lines.append('        <wp:post_type><![CDATA[post]]></wp:post_type>')
        xml_lines.append('        <wp:post_password><![CDATA[]]></wp:post_password>')
        xml_lines.append('        <wp:is_sticky>0</wp:is_sticky>')
        
        # Categories
        for c in it["categories"]:
            xml_lines.append(f'        <category domain="category" nicename="{c["slug"]}"><![CDATA[{safe_cdata(c["name"])}]]></category>')
            
        # Tags
        for t in it["tags"]:
            xml_lines.append(f'        <category domain="post_tag" nicename="{t["slug"]}"><![CDATA[{safe_cdata(t["name"])}]]></category>')
            
        # Rank Math SEO Postmeta
        meta_pairs = [
            ("rank_math_title", it["seo_title"]),
            ("rank_math_description", it["meta_desc"]),
            ("rank_math_focus_keyword", it["focus_keyword"]),
            ("rank_math_robots", 'a:1:{i:0;s:5:"index";}'),
            ("rank_math_facebook_title", it["title"]),
            ("rank_math_facebook_description", it["meta_desc"]),
            ("rank_math_facebook_image", it["featured_image"]),
            ("rank_math_twitter_title", it["title"]),
            ("rank_math_twitter_description", it["meta_desc"]),
            ("rank_math_twitter_image", it["featured_image"]),
            ("rank_math_twitter_card_type", "summary_large_image"),
            ("rank_math_primary_category", str(cat_term_ids.get(it["primary_cat_slug"], 1)))
        ]
        
        if it["word_count"] > 1200:
            meta_pairs.append(("rank_math_pillar_content", "on"))
            
        for m_key, m_val in meta_pairs:
            xml_lines.append('        <wp:postmeta>')
            xml_lines.append(f'            <wp:meta_key><![CDATA[{safe_cdata(m_key)}]]></wp:meta_key>')
            xml_lines.append(f'            <wp:meta_value><![CDATA[{safe_cdata(m_val)}]]></wp:meta_value>')
            xml_lines.append('        </wp:postmeta>')
            
        xml_lines.append('    </item>')

    xml_lines.append('</channel>')
    xml_lines.append('</rss>')
    return "\n".join(xml_lines)

# Generate the 3 Files
# Part 1: Posts 1 to 45 (45 posts)
part1_items = processed_items[:45]
part1_file = os.path.join(WORKSPACE_DIR, "helptrickbd_part1_posts_01_to_45.xml")
part1_xml = build_wxr_xml(part1_items, "Part 1 (Posts 01 to 45)")
with open(part1_file, "w", encoding="utf-8") as f:
    f.write(part1_xml)
print(f"Generated Part 1: {part1_file} ({len(part1_items)} posts, {os.path.getsize(part1_file):,} bytes)")

# Part 2: Posts 46 to 90 (45 posts)
part2_items = processed_items[45:90]
part2_file = os.path.join(WORKSPACE_DIR, "helptrickbd_part2_posts_46_to_90.xml")
part2_xml = build_wxr_xml(part2_items, "Part 2 (Posts 46 to 90)")
with open(part2_file, "w", encoding="utf-8") as f:
    f.write(part2_xml)
print(f"Generated Part 2: {part2_file} ({len(part2_items)} posts, {os.path.getsize(part2_file):,} bytes)")

# Part 3: Posts 91 to 134 (44 posts)
part3_items = processed_items[90:134]
part3_file = os.path.join(WORKSPACE_DIR, "helptrickbd_part3_posts_91_to_134.xml")
part3_xml = build_wxr_xml(part3_items, "Part 3 (Posts 91 to 134)")
with open(part3_file, "w", encoding="utf-8") as f:
    f.write(part3_xml)
print(f"Generated Part 3: {part3_file} ({len(part3_items)} posts, {os.path.getsize(part3_file):,} bytes)")

# Master File: All 134 Posts
master_file = os.path.join(WORKSPACE_DIR, "helptrickbd_wp_import_all_134.xml")
master_xml = build_wxr_xml(processed_items, "Full Master (All 134 Posts)")
with open(master_file, "w", encoding="utf-8") as f:
    f.write(master_xml)
print(f"Generated Master: {master_file} ({len(processed_items)} posts, {os.path.getsize(master_file):,} bytes)")

# Overwrite helptrickbd_wp_import.xml with full master for safety
with open(os.path.join(WORKSPACE_DIR, "helptrickbd_wp_import.xml"), "w", encoding="utf-8") as f:
    f.write(master_xml)

# Save migration log JSON
log_file = os.path.join(WORKSPACE_DIR, "migration_log.json")
with open(log_file, "w", encoding="utf-8") as f:
    json.dump({
        "generated_at": datetime.datetime.now().isoformat(),
        "total_posts": len(processed_items),
        "source_blog": "arafatitbd.blogspot.com",
        "target_site": SITE_URL,
        "author": "ayesha",
        "batches": [
            {
                "file": "helptrickbd_part1_posts_01_to_45.xml",
                "post_range": "01 - 45",
                "count": len(part1_items),
                "size_bytes": os.path.getsize(part1_file)
            },
            {
                "file": "helptrickbd_part2_posts_46_to_90.xml",
                "post_range": "46 - 90",
                "count": len(part2_items),
                "size_bytes": os.path.getsize(part2_file)
            },
            {
                "file": "helptrickbd_part3_posts_91_to_134.xml",
                "post_range": "91 - 134",
                "count": len(part3_items),
                "size_bytes": os.path.getsize(part3_file)
            }
        ],
        "posts": [
            {
                "id": p["post_id"],
                "batch": "Part 1" if p["post_id"] <= 45 else ("Part 2" if p["post_id"] <= 90 else "Part 3"),
                "title": p["title"],
                "slug": p["slug"],
                "date": p["post_date"],
                "categories": [c["name"] for c in p["categories"]],
                "tags_count": len(p["tags"]),
                "focus_keyword": p["focus_keyword"],
                "word_count": p["word_count"],
                "has_jump_break": "<!--more-->" in p["content"]
            }
            for p in processed_items
        ]
    }, f, ensure_ascii=False, indent=2)

print(f"Generated Migration Log: {log_file}")
