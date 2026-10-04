import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID

service = get_authenticated_service()

pid = "2080353291294038390"
print(f"Fetching post {pid}...")
post = service.posts().get(blogId=BLOG_ID, postId=pid, view="ADMIN").execute()
content = post.get("content", "")

target_leak_start = '<h2 class="htbd-heading" id="contemporary-movements">৫.১ সমকালীন বাংলাদেশে নারী অধিকার আন্দোলনের অর্জন ও নতুন চ্যালেঞ্জ</h2>'
target_leak_end = '<h2 class="htbd-heading" id="digital-nationalism">'

idx_start = content.find(target_leak_start)
idx_end = content.find(target_leak_end)

print(f"idx_start: {idx_start}, idx_end: {idx_end}")

if idx_start != -1 and idx_end != -1:
    clean_replacement = (
        '<h2 class="htbd-heading" id="contemporary-movements">৫.১ আধুনিক যুগে রাষ্ট্রচিন্তার প্রায়োগিক গুরুত্ব ও গণতান্ত্রিক মূল্যবোধ</h2>\n'
        '<p>একবিংশ শতাব্দীর বিশ্বায়িত প্রেক্ষাপটে রাষ্ট্রচিন্তার ভূমিকা আরও বহুমাত্রিক ও অপরিহার্য হয়ে উঠেছে। '
        'আধুনিক জনকল্যাণমূলক রাষ্ট্রের মূল লক্ষ্য কেবল ভৌগোলিক অখণ্ডতা রক্ষা বা আইন প্রয়োগ নয়, বরং প্রতিটি নাগরিকের মৌলিক অধিকার সুনিশ্চিত করা, '
        'আইনের শাসন প্রতিষ্ঠা এবং প্রাতিষ্ঠানিক জবাবদিহিতা অক্ষুণ্ণ রাখা।</p>\n'
        '<p>সুষ্ঠু ও দায়িত্বশীল রাজনৈতিক দর্শন ছাড়া কোনো রাষ্ট্র টেকসই গণতান্ত্রিক প্রতিষ্ঠান গড়ে তুলতে পারে না। '
        'ক্ষমতা বিকেন্দ্রীকরণ, সাংবিধানিক নীতিমালার সুরক্ষা এবং নাগরিক কল্যাণভিত্তিক নীতি প্রণয়নে প্রাচীন ও আধুনিক রাষ্ট্রচিন্তাবিদদের রাজনৈতিক দর্শন '
        'সর্বদা দিকনির্দেশক হিসেবে ভূমিকা পালন করে।</p>\n'
    )
    new_content = content[:idx_start] + clean_replacement + content[idx_end:]
    post["content"] = new_content
    res = service.posts().update(blogId=BLOG_ID, postId=pid, body=post).execute()
    print(f"[SUCCESS] Post {pid} successfully sanitized on Blogger!")
else:
    print("[ERROR] Indices not found!")
