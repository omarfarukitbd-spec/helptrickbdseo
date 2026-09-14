#!/usr/bin/env python3
with open('tools/content_optimizer/batch_reviver.py', 'r', encoding='utf-8') as f:
    text = f.read()

extra = """
  <h2 id="locke-property-theory" class="htbd-heading">৫.৩ জন লকের 'সম্পত্তির শ্রম তত্ত্ব' (Labor Theory of Property)</h2>
  <p><strong>প্রশ্ন: জন লকের সম্পত্তির শ্রম তত্ত্বটি সংক্ষেপে ব্যাখ্যা কর।</strong></p>
  <p><strong>উত্তর সংক্ষেপ:</strong> উদারনৈতিক দর্শনের জনক জন লক তাঁর <em>'Second Treatise of Government'</em> গ্রন্থে ব্যক্তিগত সম্পত্তির অধিকারকে মানুষের অন্যতম মৌলিক প্রাকৃতিক অধিকার হিসেবে গণ্য করেছেন। লকের মতে, ঈশ্বর এই পৃথিবীর সমস্ত প্রাকৃতিক সম্পদ মানবজাতির সাধারণ ভোগের জন্য দান করেছেন। কিন্তু একজন ব্যক্তির নিজ দেহের ওপর এবং তার শারীরিক শ্রমের ওপর রয়েছে নিরঙ্কুশ ও অবিভাজ্য মালিকানা। যখন কোনো ব্যক্তি প্রকৃতির সাধারণ কোনো উপাদানের সাথে তার নিজস্ব কায়িক শ্রম বা উদ্ভাবনী শক্তি মিশ্রিত করে, তখন সেই বস্তুটি থেকে অন্যদের সাধারণ অধিকার রহিত হয় এবং তা ব্যক্তির একান্ত নিজস্ব সম্পট্টিতে পরিণত হয়।</p>
  <p>লক স্পষ্ট করে বলেছেন যে, রাষ্ট্রের প্রধান দায়িত্বই হলো মানুষের এই জীবন, স্বাধীনতা ও সম্পত্তির (Life, Liberty, and Estate) প্রাকৃতিক অধিকারকে নিরাপত্তা প্রদান করা। সরকার যদি জনগণের এই মৌলিক অধিকার সুরক্ষায় ব্যর্থ হয়, তবে জনগণের সেই সরকারকে পরিবর্তন বা প্রতিস্থাপন করার নৈতিক অধিকার রয়েছে।</p>
"""

idx = text.find('def build_post_modern_political_thought_answer_sheet()')
if idx != -1:
    schema_idx = text.find('<script type="application/ld+json">', idx)
    if schema_idx != -1:
        text = text[:schema_idx] + extra + text[schema_idx:]
        with open('tools/content_optimizer/batch_reviver.py', 'w', encoding='utf-8') as f:
            f.write(text)
        print('Extra added to modern political thought successfully!')
    else:
        print('Schema tag not found after builder')
else:
    print('Builder function not found')
