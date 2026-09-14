#!/usr/bin/env python3
import re

with open('tools/content_optimizer/batch_reviver.py', 'r', encoding='utf-8') as f:
    code = f.read()

banners = [
    ('build_post_what_is_statesmanship', 'what-is-statesmanship-banner.jpg', 'রাষ্ট্রচিন্তা কাকে বলে? রাষ্ট্রচিন্তার সংজ্ঞা, পরিধি ও বিবর্তন', 'রাষ্ট্রচিন্তা ও রাষ্ট্রনায়কত্ব: পূর্ণাঙ্গ স্টাডি গাইড', 'চিত্র: প্লেটো ও অ্যারিস্টটলের রাষ্ট্রদর্শন থেকে আধুনিক রাষ্ট্রচিন্তা ও রাষ্ট্রনায়কত্ব'),
    ('build_post_what_is_patriarchy', 'patriarchy-definition-impact-banner.png', 'পিতৃতন্ত্র কাকে বলে? সংজ্ঞা, বৈশিষ্ট্য, প্রভাব ও নারীবাদী তত্ত্ব', 'পিতৃতন্ত্র ও লিঙ্গভিত্তিক ক্ষমতার সম্পর্ক', 'চিত্র: পিতৃতান্ত্রিক সামাজিক কাঠামো, ক্ষমতার অসম বণ্টন ও জেন্ডার সমতার আন্দোলন'),
    ('build_post_role_of_ngos', 'ngos-womens-empowerment-banner.png', 'নারী ক্ষমতায়নে এনজিও (NGO)-এর ভূমিকা ও অবদান', 'নারী ক্ষমতায়ন ও এনজিওর ভূমিকা', 'চিত্র: ক্ষুদ্রঋণ, শিক্ষা ও স্বাবলম্বী প্রকল্প বাস্তবায়নে এনজিওর ভূমিকা'),
    ('build_post_nari_andolon', 'womens-rights-movement-banner.png', 'নারী আন্দোলন: অস্তিত্ব রক্ষার লড়াই ও অধিকার প্রতিষ্ঠার ইতিহাস', 'বাঙালির নারী আন্দোলনের ঐতিহাসিক বিবর্তন', 'চিত্র: বেগম রোকেয়া থেকে আধুনিক নারী অধিকার আন্দোলন ও আইনি স্বীকৃতির সংগ্রাম'),
    ('build_post_recent_nationalism', 'recent-nationalism-banner.png', 'সাম্প্রতিক জাতীয়তাবাদ বলতে কী বোঝায়? সংজ্ঞা, বিবর্তন ও রূপ', 'সাম্প্রতিক জাতীয়তাবাদ ও বৈশ্বিক ভূরাজনীতি', 'চিত্র: বিশ্বায়ন বনাম আধুনিক জাতীয়তাবাদ ও ভূরাজনীতির সমকালীন রূপরেখা'),
    ('build_post_recent_political_thought_suggestion', 'recent-political-thought-banner.png', 'সাম্প্রতিক রাষ্ট্রচিন্তা ফাইনাল সুপার সাজেশন (২০২৬)', 'মাস্টার্স সাম্প্রতিক রাষ্ট্রচিন্তা সুপার সাজেশন', 'চিত্র: জাতীয় বিশ্ববিদ্যালয় মাস্টার্স ফাইনাল পরীক্ষার ১০০% কমন সুপার সাজেশন'),
    ('build_post_masters_social_change', 'social-change-political-dev-banner.png', 'সামাজিক পরিবর্তন ও রাজনৈতিক উন্নয়ন: সুপার সাজেশন ও হ্যান্ডনোট', 'সামাজিক পরিবর্তন ও রাজনৈতিক উন্নয়ন গাইড', 'চিত্র: উন্নয়ন তত্ত্ব, আধুনিকায়ন এবং রাজনৈতিক পরিবর্তনের তাত্ত্বিক রূপরেখা'),
    ('build_post_simple_guide_to_job', 'bcs-job-preparation-guide-banner.png', 'চাকরি ও বিসিএস প্রিলিমিনারি প্রস্তুতির সহজ ও পূর্ণাঙ্গ গাইডলাইন', 'বিসিএস প্রিলি ও সরকারি চাকরি পরীক্ষার প্রস্তুতি রোডম্যাপ', 'চিত্র: প্রথমবারেই বিসিএস প্রিলি পাসের বিষয়ভিত্তিক প্রস্তুতি ও বইয়ের তালিকা'),
    ('build_post_honours_book_list', 'political-science-book-list-banner.png', 'অনার্স রাষ্ট্রবিজ্ঞান ১ম থেকে ৪র্থ বর্ষের রেফারেন্স বইয়ের পূর্ণাঙ্গ তালিকা', 'অনার্স রাষ্ট্রবিজ্ঞান রেফারেন্স বুক লিস্ট', 'চিত্র: জাতীয় বিশ্ববিদ্যালয় অনার্স রাষ্ট্রবিজ্ঞান ১ম থেকে ৪র্থ বর্ষের সেরা রেফারেন্স বইয়ের তালিকা'),
    ('build_post_modern_political_thought_answer_sheet', 'modern-political-thought-sheet-banner.png', 'আধুনিক রাষ্ট্রচিন্তা বিগত সালের প্রশ্ন সমাধান ও উত্তরপত্র হ্যান্ডনোট', 'আধুনিক রাষ্ট্রচিন্তা প্রশ্নব্যাংক ও সাজানো সমাধান', 'চিত্র: জাতীয় বিশ্ববিদ্যালয় অনার্স ও মাস্টার্স পরীক্ষার বিগত সালের প্রশ্নের বিশদ সমাধান'),
]

modified_code = code
for fn_name, banner, alt, title, caption in banners:
    # Pattern matching badge div within the specific function
    pattern = rf'(def {fn_name}\(\):[\s\S]*?<div style=\"margin-bottom: 18px;\">[\s\S]*?</div>)'
    match = re.search(pattern, modified_code)
    if not match:
        print(f'Match NOT found for {fn_name}')
        continue
    
    img_tag = f'''
  <!-- Hero Thumbnail Banner (Blogger Featured Image & Social OpenGraph) -->
  <div style="text-align: center; margin: 18px 0 25px 0;">
    <img src="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/{banner}" 
         alt="{alt}" 
         title="{title}"
         width="1200" height="675"
         loading="eager"
         style="width: 100%; max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 4px 14px rgba(0,0,0,0.12); display: block; margin: 0 auto;"/>
    <span style="display: block; font-size: 14px; color: #5f6368; margin-top: 8px; font-style: italic;">
      {caption}
    </span>
  </div>'''

    target = match.group(1)
    replacement = target + img_tag
    modified_code = modified_code.replace(target, replacement, 1)
    print(f'Successfully injected banner for {fn_name}')

with open('tools/content_optimizer/batch_reviver.py', 'w', encoding='utf-8') as f:
    f.write(modified_code)
print('batch_reviver.py updated successfully!')
