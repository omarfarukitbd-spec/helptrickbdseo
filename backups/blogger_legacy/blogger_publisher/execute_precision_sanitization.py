import os
import sys
import json
import re

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID

service = get_authenticated_service()

def clean_post(pid, title_desc, replacer_func):
    print(f"\nProcessing {pid} ({title_desc})...")
    post = service.posts().get(blogId=BLOG_ID, postId=pid, view="ADMIN").execute()
    content = post.get("content", "")
    new_content, count = replacer_func(content)
    if count == 0:
        print(f"  [WARN] 0 replacements made in {pid}!")
        return False
    print(f"  [OK] {count} replacements made. Updating Blogger...")
    post["content"] = new_content
    res = service.posts().update(blogId=BLOG_ID, postId=pid, body=post).execute()
    print(f"  [SUCCESS] {pid} updated successfully!")
    return True

# 1. Post 2080353291294038390 (রাষ্ট্রচিন্তা কাকে বলে)
def repl_statesmanship(c):
    # Find section 5.1
    start_tag = '<h2 class="htbd-heading" id="contemporary-movements">৫.১ সমকালীন বাংলাদেশে নারী অধিকার আন্দোলনের অর্জন ও নতুন চ্যালেঞ্জ</h2>'
    new_section = (
        '<h2 class="htbd-heading" id="contemporary-movements">৫.১ আধুনিক যুগে রাষ্ট্রচিন্তার প্রায়োগিক গুরুত্ব ও গণতান্ত্রিক মূল্যবোধ</h2>\n'
        '<p>একবিংশ শতাব্দীর বিশ্বায়িত প্রেক্ষাপটে রাষ্ট্রচিন্তার ভূমিকা আরও বহুমাত্রিক ও অপরিহার্য হয়ে উঠেছে। '
        'আধুনিক জনকল্যাণমূলক রাষ্ট্রের মূল লক্ষ্য কেবল ভৌগোলিক অখণ্ডতা রক্ষা বা আইন প্রয়োগ নয়, বরং প্রতিটি নাগরিকের মৌলিক অধিকার সুনিশ্চিত করা, '
        'আইনের শাসন প্রতিষ্ঠা এবং প্রাতিষ্ঠানিক জবাবদিহিতা অক্ষুণ্ণ রাখা।</p>\n'
        '<p>সুষ্ঠু ও দায়িত্বশীল রাজনৈতিক দর্শন ছাড়া কোনো রাষ্ট্র টেকসই গণতান্ত্রিক প্রতিষ্ঠান গড়ে তুলতে পারে না। '
        'ক্ষমতা বিকেন্দ্রীকরণ, সাংবিধানিক নীতিমালার সুরক্ষা এবং নাগরিক কল্যাণভিত্তিক নীতি প্রণয়নে প্রাচীন ও আধুনিক রাষ্ট্রচিন্তাবিদদের রাজনৈতিক দর্শন '
        'সর্বদা দিকনির্দেশক হিসেবে ভূমিকা পালন করে।</p>\n'
    )
    if start_tag in c:
        idx1 = c.find(start_tag)
        # find the end of the two paragraphs
        idx2 = c.find('<div class="htbd-callout', idx1)
        if idx2 != -1:
            updated = c[:idx1] + new_section + c[idx2:]
            return updated, 1
    return c, 0

# 2. Post 8316268127112895155 (নারী আন্দোলন)
def repl_nari_andolon(c):
    count = 0
    # Replace 'যৌন হয়রানি' or 'যৌন হয়রানি'
    updated, n1 = re.subn(r'কর্মক্ষেত্রে\s+যৌন\s+[হহ][যয়]়?রানি\s+বন্ধে', 'কর্মক্ষেত্রে শারীরিক ও মানসিক হেনস্তা প্রতিরোধে', c)
    count += n1
    return updated, count

# 3. Post 6485913933681271646 (ইমাম গাজ্জালি)
def repl_ghazali(c):
    count = 0
    # Replace 'মানুষ যৌন সম্পর্ক ও সন্তান লাভের আশায়'
    target = 'মানুষ যৌন সম্পর্ক ও সন্তান লাভের আশায়'
    repl = 'মানুষ পারিবারিক বন্ধন স্থাপন, বংশরক্ষা এবং সন্তান লালন-পালনের উদ্দেশ্যে'
    if target in c:
        c = c.replace(target, repl)
        count += 1
    return c, count

# 4. Post 8548896560937787860 (নারী নির্যাতন)
def repl_violence(c):
    count = 0
    # Replace in law box: 'ধর্ষণ, ধর্ষণজনিত মৃত্যু'
    target1 = 'ধর্ষণ, ধর্ষণজনিত মৃত্যু'
    repl1 = 'চরম সহিংস অপরাধ, নির্যাতনজনিত মৃত্যু'
    if target1 in c:
        c = c.replace(target1, repl1)
        count += 1
        
    # Replace in Q1: 'ধর্ষণের সর্বোচ্চ শাস্তি'
    target2 = 'ধর্ষণের সর্বোচ্চ শাস্তি'
    repl2 = 'গুরুতর সহিংসতার অপরাধে সর্বোচ্চ শাস্তি'
    if target2 in c:
        c = c.replace(target2, repl2)
        count += 1
        
    return c, count

print("=" * 60)
print("EXECUTING PRECISE REPLACEMENTS ON LIVE BLOGGER")
print("=" * 60)
clean_post("2080353291294038390", "রাষ্ট্রচিন্তা কাকে বলে", repl_statesmanship)
clean_post("8316268127112895155", "নারী আন্দোলন", repl_nari_andolon)
clean_post("6485913933681271646", "ইমাম গাজ্জালি", repl_ghazali)
clean_post("8548896560937787860", "নারী নির্যাতন", repl_violence)
