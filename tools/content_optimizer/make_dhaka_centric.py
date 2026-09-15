# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

path = r'd:\android\Project\Helptrickbd SEO full site\output_posts\revived_posts\how-to-correction-certificate-name-2025.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

c = 0

def rep(old, new, label=''):
    global html, c
    if old in html:
        html = html.replace(old, new)
        c += 1
        print(f'[OK] {label or new[:50]}')
    else:
        print(f'[MISS] {label or old[:50]}')

# TOC section 5 link
rep('৫. বিভিন্ন শিক্ষাবোর্ডের ফি ও সম্ভাব্য সময়সীমার তথ্য ছক</a>',
    '৫. ঢাকা শিক্ষাবোর্ডে ফি ও সম্ভাব্য সময়সীমার তথ্য ছক (২০২৬)</a>', 'TOC S5')

# TOC section 6 link
rep('৬. বোর্ড মিটিংয়ের শুনানি, সাক্ষাৎকার ও নতুন মূল সনদ উত্তোলন</a>',
    '৬. ঢাকা বোর্ড মিটিংয়ের শুনানি, সাক্ষাৎকার ও নতুন সনদ উত্তোলন</a>', 'TOC S6')

# H2 section 5
rep('৫. বিভিন্ন শিক্ষাবোর্ডের ফি ও সম্ভাব্য সময়সীমার তথ্য ছক (২০২৬)</h2>',
    '৫. ঢাকা শিক্ষাবোর্ডে ফি ও সম্ভাব্য সময়সীমার তথ্য ছক (২০২৬)</h2>', 'H2 S5')

# H2 section 6
rep('৬. বোর্ড মিটিংয়ের শুনানি, সাক্ষাৎকার ও নতুন মূল সনদ উত্তোলন</h2>',
    '৬. ঢাকা বোর্ড মিটিংয়ের শুনানি, সাক্ষাৎকার ও নতুন সনদ উত্তোলন</h2>', 'H2 S6')

# Step 1 tip box — split into two parts to avoid quote issues
rep('রাজশাহী, কুমিল্লা, চট্টগ্রাম, যশোর, দিনাজপুর, বরিশাল, সিলেট ও মাদ্রাসা বোর্ডের পোর্টালেও একইভাবে',
    'এই গাইড শুধুমাত্র ঢাকা বোর্ড (efile.dhakaeducationboard.gov.bd)-এর জন্য। রাজশাহী, কুমিল্লা বা অন্য বোর্ডের শিক্ষার্থীরা',
    'Step 1 tip part 1')

rep("'e-Service' মেনুর অধীনে নাম ও বয়স সংশোধন ফরম পাওয়া যায়।",
    'নিজ বোর্ডের পোর্টালে আবেদন করুন।',
    'Step 1 tip part 2')

# Board hearing - add Dhaka specifics
rep('অনলাইনে সফল আবেদনের পর বোর্ডের সংশ্লিষ্ট শাখা',
    'অনলাইনে সফল আবেদনের পর ঢাকা শিক্ষাবোর্ডের সংশ্লিষ্ট শাখা',
    'Board hearing - Dhaka Board')

# Committee name - add Dhaka Board office
rep("'নাম ও বয়স সংশোধন কমিটি'র",
    "'নাম ও বয়স সংশোধন কমিটি'র (ঢাকা বোর্ড: বাক্শীবাজার, মতিঝিল, ঢাকা-এ অবস্থিত)",
    'Committee mention - Dhaka office')

# Status check URL
rep('ওয়েবসাইটে স্ট্যাটাস পরিবর্তন হয়।',
    'efile.dhakaeducationboard.gov.bd-এ স্ট্যাটাস পরিবর্তন হয়।',
    'Status URL')

# Section 5 intro
rep('শিক্ষা বোর্ড অনুযায়ী ফি-এর পরিমাণে সামান্য তারতম্য হতে পারে। সাধারণ শিক্ষাবোর্ডসমূহের স্ট্যান্ডার্ড ফি তালিকা নিচে তুলে ধরা হলো:',
    'ঢাকা শিক্ষাবোর্ডে সোনালী সেবার মাধ্যমে নির্ধারিত ফি পরিশোধ করতে হয়। সংশোধনের ধরন ও জরুরি ভিত্তিতে ফি-এর পরিমাণ পরিবর্তন হতে পারে। ২০২৬ সালের প্রযোজ্য ফি তালিকা:',
    'Section 5 intro')

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f'\nTotal changes: {c}')
print(f'File size: {len(html):,} chars')
