---
name: seo-blogger-adsense
description: End-to-end SEO, Google AdSense approval, and ranking mastery for Blogger (Blogspot) and content websites. Use whenever working on website SEO, Google ranking, AdSense approval, XML theme optimization, content writing, or Search Console indexing.
---

# 🚀 Blogger SEO & Google AdSense Approval Mastery Skill

This skill equips the AI agent to act as a world-class SEO Director, Webmaster, and AdSense Approval Strategist specifically tuned for **Blogger (Blogspot)** and content-driven websites.

---

## 📋 1. AdSense Approval 100% Blueprint (গুগল এডসেন্স অনুমোদনের নিয়মাবলি)

Google AdSense rejects 90% of blogs due to "Low Value Content", "Scraped Content", or "Navigation Issues". Follow this strict checklist to guarantee approval:

### A. The 5 Mandatory Legal & Trust Pages (আবশ্যিক পেজসমূহ)
Never apply for AdSense without these 5 standalone static pages in Blogger:
1. **About Us (আমাদের সম্পর্কে):** Who runs the site, mission, editorial guidelines, expertise (E-E-A-T signals).
2. **Contact Us (যোগাযোগ):** Working contact form, email address, physical address/city, social profiles.
3. **Privacy Policy (গোপনীয়তা নীতি):** Explicit mention of Google AdSense, cookies, DoubleClick DART cookie, third-party advertising partners, GDPR/CCPA compliance.
4. **Terms and Conditions (ব্যবহারের শর্তাবলি):** Content usage, intellectual property, disclaimer of warranties.
5. **Disclaimer (দাবিত্যাগ):** Educational/informational disclaimer, affiliate disclosure (if applicable).

### B. Content Inventory Requirements (কন্টেন্ট রিকোয়ারমেন্ট)
- **Minimum Post Count:** 20 to 30 high-quality, fully unique published articles.
- **Article Word Count:** 800 to 1,500+ words per article. Zero thin content (posts under 400 words must be deleted or expanded).
- **Value Addition:** Must solve real user queries. Do not generate generic regurgitated AI text. Use practical examples, step-by-step guides, tables, and unique perspectives.
- **Images:** Every post must have at least 1-2 original or properly attributed featured images with descriptive alt text and WebP/compressed formats. Zero copyright infringement.

### C. Site Structure & Navigation (সাইট স্ট্রাকচার)
- **Category Balance:** Minimum 3-4 distinct categories/labels in Blogger. Every category MUST have at least 4-5 published posts (no empty or single-post categories).
- **Navigation Menus:** 
  - **Header Menu:** Home, Categories (Dropdown), Contact.
  - **Footer Menu:** About Us, Privacy Policy, Terms & Conditions, Disclaimer, Contact Us.
- **Clean Theme:** Clean, mobile-responsive theme with readable typography (16px+ body font), dark/light contrast, no broken links, zero intrusive popups.

---

## ⚙️ 2. Blogger Technical SEO & Theme Optimization (ব্লগার টেকনিক্যাল এসইও)

### A. Custom robots.txt for Blogger
Configure in **Settings > Crawlers and indexing > Custom robots.txt**:
```text
User-agent: *
Disallow: /search
Disallow: /*?m=1
Disallow: /*?m=0
Allow: /

Sitemap: https://YOUR_DOMAIN.com/sitemap.xml
Sitemap: https://YOUR_DOMAIN.com/atom.xml?redirect=false&start-index=1&max-results=500
```

### B. Custom Robot Header Tags (ব্লগার রোবট হেডার ট্যাগ)
Configure in **Settings > Crawlers and indexing > Custom robot header tags**:
- **Home page tags:** `all`, `noodp`
- **Archive and search page tags:** `noindex`, `nofollow`, `noodp`
- **Post and page tags:** `all`, `noodp`

### C. XML Theme Head Optimization (মেটা ট্যাগ ও স্কিমা)
Inject into Blogger Theme XML (`<head>` section):
1. **Dynamic Meta Description:**
```xml
<b:if cond='data:view.isPost'>
  <meta expr:content='data:blog.metaDescription' name='description'/>
  <meta expr:content='data:blog.pageName' property='og:title'/>
  <meta expr:content='data:blog.canonicalUrl' property='og:url'/>
  <meta content='article' property='og:type'/>
</b:if>
```
2. **JSON-LD Schema Markup (BlogPosting / Article Schema):**
Generate structured `application/ld+json` including `headline`, `image`, `datePublished`, `dateModified`, `author` (Person), and `publisher` (Organization).

---

## 🎯 3. Keyword Research & Google Ranking Strategy (র‍্যাংকিং স্ট্র্যাটেজি)

### A. KGR (Keyword Golden Ratio) Method for Fast Ranking
Target low-competition keywords that rank in days without backlinks:
$$\text{KGR} = \frac{\text{Allintitle results (allintitle: "keyword")}}{\text{Monthly Search Volume}} < 0.25$$
- If KGR $< 0.25$: High probability of ranking in top 50 as soon as indexed.
- Target search volume: 50 to 250 monthly searches.

### B. Search Intent Mapping
Ensure article format matches user intent:
- **Informational ("কিভাবে", "কী", "কখন"):** How-to guides, numbered steps, summary callouts.
- **Commercial/Review ("সেরা", "বনাম"):** Comparison tables, pros/cons, rating badges.
- **Navigational/Direct:** Direct answer in the first 100 words (Featured Snippet optimization).

---

## ✍️ 4. On-Page SEO & Content Preservation Standards (কনটেন্ট ও অডিয়েন্স আর্কিটেকচার)

### A. Audience & Persona Profiling (টার্গেট অডিয়েন্স নির্ণয়)
পোস্ট রিক্রিয়েট বা রিভাইভ করার আগে অবশ্যই মূল কনটেন্ট পড়ে টার্গেট পাঠক নিশ্চিত করতে হবে:
1. **স্কুল ও বোর্ড শিক্ষার্থী (Class 6–10, SSC, HSC, Alim):** সহজ-সরল ভাষা, বোর্ড পরীক্ষার স্ট্যান্ডার্ড, ব্যাকরণ ও প্যাসেজ সংক্রান্ত প্রশ্নোত্তর।
2. **বিশ্ববিদ্যালয় অনার্স/মাস্টার্স শিক্ষার্থী (Political Science, Sociology):** অ্যাকাডেমিক পরিভাষা, রাষ্ট্রবিজ্ঞানীদের প্রামাণ্য উক্তি, তাত্ত্বিক কাঠামো ও বিগত সালের প্রশ্ন সমাধান।
3. **চাকরি ও বিসিএস প্রার্থী (Job Prep):** সংক্ষিপ্ত নোটস, বিগত সালের প্রশ্ন বিশ্লেষণ, দ্রুত মুখস্থ করার টেকনিক ও তথ্য ছক।
4. **ইসলামিক ও ভক্তিমূলক পাঠক (Islamic Article):** ভাবগাম্ভীর্যপূর্ণ ভাষা, বিশুদ্ধ লিরিক্স/ক্বাসিদা, অনুবাদ ও আধ্যাত্মিক তাৎপর্য।
5. **আইসিটি ও সাধারণ প্রযুক্তি (ICT Guide):** হ্যান্ডস-অন গাইড, ধাপে ধাপে নির্দেশিকা ও বাস্তব উদাহরণ।

### B. Strict Language & Content Preservation Rules (ভাষা ও মূল কনটেন্ট সংরক্ষণ নীতি)
- **Language Preservation (ভাষা অপরিবর্তনীয়):** পোস্টটি যদি ইংরেজিতে থাকে, তবে তা **১০০% প্রমিত ইংরেজিতেই** রাখতে হবে। কখনো ইংরেজি পোস্টকে বাংলায় অনুবাদ করা যাবে না।
- **Non-destructive Augmentation (মূল টেক্সট অক্ষুণ্ণ রাখা):** ইউজারের মূল কনটেন্ট কোনোভাবেই ডিলিট বা প্রতিস্থাপন (replace) করা যাবে না। কেবল এডসেন্স পলিসিগত সমস্যা থাকলে শব্দ ঠিক করা যাবে।
- **Before & After Information Addition:** পোস্ট বড় করতে হলে ইউজারের মূল লেখার **আগে** (Introduction/Summary) এবং **পরে** (Detailed Analysis, Table, Model Questions, FAQ) তথ্য যোগ করতে হবে; মূল বডিতে নয়।
- **Original Thumbnail Preservation:** যদি পোস্টে লেখকের নিজস্ব থাম্বনেইল থাকে, তবে তা অবশ্যই মূল ব্যানার হিসেবে অক্ষুণ্ণ রাখতে হবে।

### C. The Blogger `<!--more-->` Jump Break Standard (হোমপেজ স্নsnippet রুল)
- ব্লগারে হোমপেজ ও ক্যাটাগরি পেজে সুন্দর ও পরিচ্ছন্ন স্নsnippet প্রদর্শনের জন্য পোস্টের প্রথম ৩–৪ লাইন বা ভূমিকার ঠিক পরেই **`<!--more-->`** ট্যাগটি বাধ্যতামূলকভাবে বসাতে হবে।
```html
<p>প্রথম প্যারাগ্রাফ বা মূল ভূমিকা এখানে থাকবে (২-৩ বাক্য)...</p>
<!--more-->
<!-- এর নিচে বাকি মূল পোস্ট, সূচিপত্র ও বিস্তারিত অংশ থাকবে -->
```

### D. Label Governance & User Consent (লেবেল নির্ধারণে ইউজারের অনুমতি)
- কখনো নিজের ইচ্ছামতো ব্লগারে নতুন লেবেল তৈরি বা যুক্ত করা যাবে না।
- প্রতিটি পোস্ট পাবলিশ বা আপডেটের আগে ইউজারকে স্পষ্টভাবে জিজ্ঞেস করতে হবে:
  > *"এই পোস্টটি কি '[বিদ্যমান ক্যাটাগরি]'-এ যাবে, নাকি এর জন্য নতুন কোনো লেবেল তৈরি করতে চান?"*
- ইউজার সম্মতি দিলে কেবল সেই নির্ধারিত লেবেলেই পোস্টটি যাবে।

### E. Standard Structural Elements
1. **URL Slug (Permalink):** মূল ফোকাস কি-ওয়ার্ড সম্বলিত ছোট পারমালিংক।
2. **Title (H1):** আকর্ষণীয় ও প্রাসঙ্গিক টাইটেল।
3. **Intro (First 100 Words):** মূল প্রশ্নের সরাসরি সারসংক্ষেপ উত্তর।
4. **Jump Break:** প্রথম প্যারার পর `<!--more-->`।
5. **Internal Linking:** প্রাসঙ্গিক ২-৩টি পোস্টের লিঙ্ক।
6. **FAQ Schema:** ৩-৫টি বাস্তবসম্মত প্রশ্নোত্তর সহ Schema.org microdata।

---

## 🔍 5. Search Console & Indexing Health (গুগল সার্চ কনসোল ও ইনডেক্সিং)

- Submit sitemaps: `/sitemap.xml` and `/atom.xml?redirect=false&start-index=1&max-results=500`.
- Monitor **Page Indexing** report:
  - Fix "Discovered - currently not indexed" by improving internal linking and content depth.
  - Fix "Crawled - currently not indexed" by eliminating duplicate/thin content and updating freshness.
- Test Core Web Vitals: Ensure LCP $< 2.5\text{s}$, FID/INP $< 200\text{ms}$, CLS $< 0.1$.
