import json
import os
import re
import html
import datetime
import xml.etree.ElementTree as ET

WORKSPACE_DIR = r'd:\android\Project\Helptrickbd Wp'
INPUT_JSON = r'C:\Users\omarf\.gemini\antigravity-ide\brain\24142913-8319-445a-9f47-d2935029fdec\scratch\scraped_blogger_pages.json'
OUTPUT_XML = os.path.join(WORKSPACE_DIR, 'helptrickbd_pages_import.xml')

with open(INPUT_JSON, 'r', encoding='utf-8') as f:
    pages = json.load(f)

print(f"Loaded {len(pages)} pages to convert into WordPress WXR 1.2 XML.")

# Descriptions & Focus keywords for each page
PAGE_METADATA = {
    'nu-cgpa-calculator': {
        'title': 'জাতীয় বিশ্ববিদ্যালয় সিজিপিএ ক্যালকুলেটর (NU CGPA & SGPA Calculator)',
        'focus_keyword': 'NU CGPA Calculator',
        'desc': 'জাতীয় বিশ্ববিদ্যালয় অনার্স ও ডিগ্রি কোর্সের জিপিএ, সিজিপিএ (CGPA) এবং এসজিপিএ সহজে ও নির্ভুলভাবে হিসাব করুন Help Trick BD অফিসিয়াল ক্যালকুলেটরে।'
    },
    'cover-page': {
        'title': 'অ্যাসাইনমেন্ট ও টার্ম পেপার কভার পেজ মেকার (Assignment Cover Page)',
        'focus_keyword': 'Assignment Cover Page',
        'desc': 'জাতীয় বিশ্ববিদ্যালয় ও কলেজের অ্যাসাইনমেন্ট, টার্ম পেপার ও প্রজেক্টের জন্য প্রমিত কভার পেজ তৈরি ও ডাউনলোড করুন।'
    },
    'about-us': {
        'title': 'আমাদের সম্পর্কে (About Us)',
        'focus_keyword': 'About Help Trick BD',
        'desc': 'Help Trick BD-এর লক্ষ্য, উদ্দেশ্য ও অ্যাকাডেমিক কনটেন্ট টিম সম্পর্কে বিস্তারিত জানুন।'
    },
    'contact-us': {
        'title': 'যোগাযোগ (Contact Us)',
        'focus_keyword': 'Contact Help Trick BD',
        'desc': 'আমাদের সাথে যেকোনো শিক্ষা সংক্রান্ত পরামর্শ, মতামত বা সহযোগিতার জন্য সরাসরি যোগাযোগ করুন।'
    },
    'privacy-policy': {
        'title': 'গোপনীয়তা নীতি (Privacy Policy)',
        'focus_keyword': 'Privacy Policy',
        'desc': 'Help Trick BD ওয়েবসাইটের ব্যবহারকারী ডেটা সুরক্ষা, কুকিজ এবং গোপনীয়তা নীতিমালা।'
    },
    'terms-conditions': {
        'title': 'শর্তাবলী (Terms & Conditions)',
        'focus_keyword': 'Terms and Conditions',
        'desc': 'Help Trick BD প্ল্যাটফর্ম ব্যবহারের সাধারণ নিয়মাবলী ও আইনি শর্তাদি।'
    },
    'disclaimer': {
        'title': 'দাবিত্যাগ (Disclaimer)',
        'focus_keyword': 'Disclaimer',
        'desc': 'Help Trick BD-এর শিক্ষামূলক তথ্য, সাজেশন ও স্টাডি মেটেরিয়ালের নীতিগত দাবিত্যাগ।'
    },
    'cookie-policy': {
        'title': 'কুকি নীতিমালা (Cookie Policy)',
        'focus_keyword': 'Cookie Policy',
        'desc': 'Help Trick BD ওয়েবসাইটে ব্যবহৃত কুকি ও বিশ্লেষণ সংক্রান্ত তথ্যাবলী।'
    },
    'sitemap': {
        'title': 'সাইটম্যাপ (HTML Sitemap)',
        'focus_keyword': 'HTML Sitemap',
        'desc': 'Help Trick BD-এর সকল পোস্ট, ক্যাটাগরি ও স্টাডি গাইডের পূর্ণাঙ্গ সূচিপত্র।'
    }
}

xml_header = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"
	xmlns:excerpt="http://wordpress.org/export/1.2/excerpt/"
	xmlns:content="http://purl.org/rss/1.0/modules/content/"
	xmlns:wfw="http://wellformedweb.org/CommentAPI/"
	xmlns:dc="http://purl.org/dc/elements/1.1/"
	xmlns:wp="http://wordpress.org/export/1.2/"
>
<channel>
	<title>Help Trick BD</title>
	<link>https://www.helptrickbd.com</link>
	<description>Help Trick BD Academic Portal</description>
	<pubDate>Wed, 07 Oct 2026 12:00:00 +0000</pubDate>
	<language>bn-BD</language>
	<wp:wxr_version>1.2</wp:wxr_version>
	<wp:base_site_url>https://www.helptrickbd.com</wp:base_site_url>
	<wp:base_blog_url>https://www.helptrickbd.com</wp:base_blog_url>

	<wp:author>
		<wp:author_id>1</wp:author_id>
		<wp:author_login><![CDATA[ayesha]]></wp:author_login>
		<wp:author_email><![CDATA[ayesha@helptrickbd.com]]></wp:author_email>
		<wp:author_display_name><![CDATA[Ayesha]]></wp:author_display_name>
		<wp:author_first_name><![CDATA[Ayesha]]></wp:author_first_name>
		<wp:author_last_name><![CDATA[]]></wp:author_last_name>
	</wp:author>
"""

items_xml = []
start_id = 15001

for idx, p in enumerate(pages, 1):
    slug = p['slug']
    raw_content = p['content']
    meta = PAGE_METADATA.get(slug, {
        'title': p['title'],
        'focus_keyword': slug.replace('-', ' ').title(),
        'desc': f"{p['title']} সম্পর্কে বিস্তারিত তথ্যাবলী জানুন Help Trick BD-তে।"
    })
    
    page_title = meta['title']
    focus_kw = meta['focus_keyword']
    desc = meta['desc']
    post_id = start_id + idx
    
    # Clean any internal blogger links inside page content
    clean_content = raw_content
    clean_content = re.sub(
        r'https?://(?:www\.)?helptrickbd\.com/p/([^/]+)\.html',
        r'https://www.helptrickbd.com/\1/',
        clean_content
    )
    clean_content = re.sub(
        r'https?://(?:www\.)?helptrickbd\.com/\d{4}/\d{2}/([^/]+)\.html',
        r'https://www.helptrickbd.com/\1/',
        clean_content
    )
    
    item = f"""	<item>
		<title><![CDATA[{page_title}]]></title>
		<link>https://www.helptrickbd.com/{slug}/</link>
		<pubDate>Wed, 07 Oct 2026 12:00:00 +0000</pubDate>
		<dc:creator><![CDATA[ayesha]]></dc:creator>
		<guid isPermaLink="false">https://www.helptrickbd.com/?page_id={post_id}</guid>
		<description></description>
		<content:encoded><![CDATA[{clean_content}]]></content:encoded>
		<excerpt:encoded><![CDATA[]]></excerpt:encoded>
		<wp:post_id>{post_id}</wp:post_id>
		<wp:post_date><![CDATA[2026-10-07 12:00:00]]></wp:post_date>
		<wp:post_date_gmt><![CDATA[2026-10-07 06:00:00]]></wp:post_date_gmt>
		<wp:comment_status><![CDATA[closed]]></wp:comment_status>
		<wp:ping_status><![CDATA[closed]]></wp:ping_status>
		<wp:post_name><![CDATA[{slug}]]></wp:post_name>
		<wp:status><![CDATA[publish]]></wp:status>
		<wp:post_parent>0</wp:post_parent>
		<wp:menu_order>0</wp:menu_order>
		<wp:post_type><![CDATA[page]]></wp:post_type>
		<wp:post_password><![CDATA[]]></wp:post_password>
		<wp:is_sticky>0</wp:is_sticky>
		<wp:postmeta>
			<wp:meta_key><![CDATA[rank_math_title]]></wp:meta_key>
			<wp:meta_value><![CDATA[{page_title} - Help Trick BD]]></wp:meta_value>
		</wp:postmeta>
		<wp:postmeta>
			<wp:meta_key><![CDATA[rank_math_description]]></wp:meta_key>
			<wp:meta_value><![CDATA[{desc}]]></wp:meta_value>
		</wp:postmeta>
		<wp:postmeta>
			<wp:meta_key><![CDATA[rank_math_focus_keyword]]></wp:meta_key>
			<wp:meta_value><![CDATA[{focus_kw}]]></wp:meta_value>
		</wp:postmeta>
		<wp:postmeta>
			<wp:meta_key><![CDATA[rank_math_robots]]></wp:meta_key>
			<wp:meta_value><![CDATA[a:1:{{i:0;s:5:"index";}}]]></wp:meta_value>
		</wp:postmeta>
	</item>
"""
    items_xml.append(item)

full_xml = xml_header + "".join(items_xml) + "</channel>\n</rss>\n"

with open(OUTPUT_XML, 'w', encoding='utf-8') as f:
    f.write(full_xml)

print(f"Generated {OUTPUT_XML} successfully ({os.path.getsize(OUTPUT_XML)} bytes).")
