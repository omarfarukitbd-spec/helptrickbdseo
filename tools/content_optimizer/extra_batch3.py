#!/usr/bin/env python3
with open('tools/content_optimizer/batch3_reviver.py', 'r', encoding='utf-8') as f:
    text = f.read()

salatun_extra = """
    <p><strong>প্রশ্ন ২: মিলাদ ও কিয়ামে দাঁড়িয়ে সালাম দেওয়ার বিধান কী?</strong><br>
    উত্তর: অধিকাংশ আলেম ও ফুকাহায়ে কেরামের মতে, রাসূলুল্লাহ (সা.)-এর প্রতি তাজিম ও সম্মান প্রদর্শনার্থে দাঁড়িয়ে সালাম পেশ করা মুস্তাহাব ও ভালোবাসার বহিঃপ্রকাশ, তবে এটিকে ফরজ বা ওয়াজিব মনে করা যাবে না।</p>
    <p><strong>প্রশ্ন ৩: ক্বাসিদায়ে বুরদার মূল রচয়িতা কে?</strong><br>
    উত্তর: মিশরের প্রখ্যাত সুফি কবি ইমাম শরফুদ্দিন আল-বুসিরী (র.)।</p>
"""

comp_history_extra = """
  <p><strong>প্রশ্ন: আধুনিক কম্পিউটারের মস্তিষ্ক (CPU) প্রথম কে উদ্ভাবন করেন?</strong><br>
  <strong>উত্তর:</strong> ১৯৭১ সালে টেড হফ, ফেডেরিকো ফ্যাগিন ও স্ট্যান মজরের নেতৃত্বে ইনটেল দল প্রথম একক চিপ মাইক্রোপ্রসেসর Intel 4004 তৈরি করে।</p>
  <p><strong>প্রশ্ন: বাইনারি কোডের প্রবক্তা কে ছিলেন?</strong><br>
  <strong>উত্তর:</strong> জার্মান দার্শনিক ও গণিতবিদ গটফ্রিড ভন লাইবনিজ ১৬৭৯ সালে দ্বিমিক বা বাইনারি পদ্ধতির পূর্ণাঙ্গ রূপরেখা উপস্থাপন করেন।</p>
"""

comp_gen_extra = """
    <p><strong>প্রশ্ন ৩: ভিএলএসআই (VLSI) এবং ইউএলএসআই (ULSI)-এর পূর্ণরূপ কী?</strong><br>
    উত্তর: VLSI হলো Very Large Scale Integration (চতুর্থ প্রজন্ম) এবং ULSI হলো Ultra Large Scale Integration (পঞ্চম প্রজন্ম)।</p>
    <p><strong>প্রশ্ন ৪: কৃত্রিম বুদ্ধিমত্তার (AI) জনক কাকে বলা হয়?</strong><br>
    উত্তর: ব্রিটিশ গণিতবিদ অ্যালান ট্যুরিং এবং মার্কিন কম্পিউটার বিজ্ঞানী জন ম্যাকার্থিকে এআই-এর অন্যতম জনক বিবেচনা করা হয়।</p>
"""

comp_types_extra = """
    <p><strong>প্রশ্ন ৩: মাইক্রোকম্পিউটার ও সুপার কম্পিউটারের প্রধান পার্থক্য কী?</strong><br>
    উত্তর: মাইক্রোকম্পিউটার একজন ব্যবহারকারীর দৈনন্দিন কাজের জন্য একক সিপিইউ ব্যবহার করে, আর সুপার কম্পিউটার হাজার হাজার প্রসেসরের সমন্বয়ে জটিল গাণিতিক ও বৈজ্ঞানিক গণনা পরিচালনা করে।</p>
    <p><strong>প্রশ্ন ৪: বিশ্বের দ্রুততম সুপার কম্পিউটার কোনটি?</strong><br>
    উত্তর: বর্তমানে যুক্তরাষ্ট্রের ওক রিজ ন্যাশনাল ল্যাবরেটরির 'ফ্রন্টিয়ার' (Frontier) বিশ্বের দ্রুততম এক্সাস্কেল সুপার কম্পিউটার।</p>
"""

pol_econ_extra = """
    <p><strong>প্রশ্ন ৩: রিকার্ডোর তুলনামূলক সুবিধা তত্ত্বের (Comparative Advantage) মূল কথা কী?</strong><br>
    উত্তর: প্রতিটি দেশের উচিত সেই পণ্য উৎপাদনে মনোযোগ দেওয়া যাতে তার সুযোগ ব্যয় (Opportunity Cost) সবচেয়ে কম, এবং অন্যান্য পণ্য আন্তর্জাতিক বাণিজ্যের মাধ্যমে আমদানি করা।</p>
    <p><strong>প্রশ্ন ৪: কেইনসীয় অর্থনীতি কত সালের মন্দার পর জনপ্রিয় হয়?</strong><br>
    উত্তর: ১৯২৯ সালের বৈশ্বিক মহামন্দার পর ১৯৩০-এর দশকে জন মেনার্ড কেইনসের হাত ধরে এই মতবাদ বিশ্বজুড়ে গৃহীত হয়।</p>
"""

nationalization_extra = """
    <p><strong>প্রশ্ন ৩: বিরাষ্ট্রীয়করণ বোর্ড বা বেসরকারীকরণ কমিশন কত সালে গঠিত হয়?</strong><br>
    উত্তর: ১৯৯৩ সালে বাংলাদেশে বেসরকারীকরণ বোর্ড গঠিত হয় যা পরবর্তীতে ২০০০ সালে বেসরকারীকরণ কমিশনে রূপ নেয়।</p>
    <p><strong>প্রশ্ন ৪: পাট শিল্পকে পূর্বে কী বলা হতো?</strong><br>
    উত্তর: বাংলাদেশের সোনালী আঁশ (Golden Fiber) এবং জাতীয় অর্থনীতির মূল চালিকাশক্তি বলা হতো।</p>
"""

govt_parties_extra = """
    <p><strong>প্রশ্ন ৩: রাজনৈতিক দলের প্রধান লক্ষ্য কী?</strong><br>
    উত্তর: সাংবিধানিক ও শান্তিপূর্ণ নির্বাচনের মাধ্যমে রাষ্ট্রক্ষমতা অর্জন করে জনকল্যাণমূলক নীতি ও কর্মসূচি বাস্তবায়ন করা।</p>
    <p><strong>প্রশ্ন ৪: বাংলাদেশের সংবিধানের কোন অনুচ্ছেদে বাক ও সংগঠনের স্বাধীনতার কথা বলা হয়েছে?</strong><br>
    উত্তর: সংবিধানের ৩৯ অনুচ্ছেদে চিন্তা ও বিবেকের স্বাধীনতা এবং ৩৮ অনুচ্ছেদে সমিতি ও সংগঠন গঠনের মৌলিক অধিকার দেওয়া হয়েছে।</p>
"""

extras = [
    ('build_post_salatun', '</div>\n</div>\n\n<script type="application/ld+json">', salatun_extra + '  </div>\n</div>\n\n<script type="application/ld+json">'),
    ('build_post_computer_history_part2', '<h2 id="faqs"', comp_history_extra + '\n  <h2 id="faqs"'),
    ('build_post_computer_generations_part3', '</div>\n</div>\n\n<script type="application/ld+json">', comp_gen_extra + '  </div>\n</div>\n\n<script type="application/ld+json">'),
    ('build_post_computer_types_part4', '</div>\n</div>\n\n<script type="application/ld+json">', comp_types_extra + '  </div>\n</div>\n\n<script type="application/ld+json">'),
    ('build_post_political_economy', '</div>\n</div>\n\n<script type="application/ld+json">', pol_econ_extra + '  </div>\n</div>\n\n<script type="application/ld+json">'),
    ('build_post_industrial_nationalization', '</div>\n</div>\n\n<script type="application/ld+json">', nationalization_extra + '  </div>\n</div>\n\n<script type="application/ld+json">'),
    ('build_post_government_political_parties', '</div>\n</div>\n\n<script type="application/ld+json">', govt_parties_extra + '  </div>\n</div>\n\n<script type="application/ld+json">'),
]

for fn, target, repl in extras:
    fn_idx = text.find(f"def {fn}()")
    if fn_idx != -1:
        target_idx = text.find(target, fn_idx)
        if target_idx != -1:
            text = text[:target_idx] + repl + text[target_idx + len(target):]
            print(f"Added extra to {fn}")
        else:
            print(f"Target not found in {fn}")
    else:
        print(f"Function not found: {fn}")

with open('tools/content_optimizer/batch3_reviver.py', 'w', encoding='utf-8') as f:
    f.write(text)
print("Batch 3 extra additions complete!")
