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

## 🎭 6. Anti-AI Template Protocol & Human Editorial Diversity (স্বাভাবিক মানবিক কনটেন্ট আর্কিটেকচার)

গুগল হেল্পফুল কনটেন্ট সিস্টেম (Helpful Content System) এবং মানব পাঠকদের সবচেয়ে বড় বিরক্তির কারণ হলো **"রোবটিক বা কুকি-কাটার টেমপ্লেট"** (একই ছাঁচে সব পোস্ট তৈরি করা)। একজন বাস্তব লেখক বা শিক্ষক কখনোই সব বিষয়ে একই ডিজাইন, একই রকম বক্স বা একই পয়েন্ট ব্যবহার করেন না।

ব্লগকে ১০০% ন্যাচারাল এবং মানবিক দেখাতে নিচের **৫টি আলাদা কনটেন্ট আর্কিটাইপ (Content Archetypes)** অনুযায়ী ডিজাইন ও ভাষা পরিবর্তন করতে হবে:

---

### A. The 5 Human Content Archetypes (৫টি ভিন্নধর্মী পোস্ট স্ট্রাকচার)

#### ১. লিটারারি ও হিস্টরিক্যাল স্টোরিটেলিং (সাহিত্য, ইতিহাস ও জীবনী)
- **কোথায় প্রযোজ্য:** হাসন রাজা, বিদ্যাসাগর, মুক্তিযুদ্ধ, সাহিত্যিক প্রবন্ধ, ইসলামিক ক্বাসিদা ইত্যাদি।
- **ডিজাইন ও লেআউট:** কোনো কৃত্রিম রোবটিক সূচিপত্র (TOC) বা জোর করে চাপিয়ে দেওয়া তুলনা ছক থাকবে না। এটি হবে একটি সুন্দর ম্যাগাজিন/নিউজপেপার স্টাইল বড় প্রবন্ধ।
- **উপাদান:** আকর্ষণীয় উদ্ধৃতি (Blockquote), প্রাসঙ্গিক ঐতিহাসিক পটভূমি, সাহিত্যিক বিশ্লেষণ এবং সাবলীল গল্পকথন।
- **টোন:** আবেগঘন, চিন্তাশীল, নান্দনিক ও প্রমিত।

#### ২. বিশ্ববিদ্যালয় অ্যাকাডেমিক হ্যান্ডনোট (অনার্স ও মাস্টার্স রাষ্ট্রবিজ্ঞান)
- **কোথায় প্রযোজ্য:** রাষ্ট্রচিন্তা, সংবিধান, রাজনৈতিক দল, সমাজবিজ্ঞান, জাতীয় বিশ্ববিদ্যালয় সাজেশন।
- **ডিজাইন ও লেআউট:** প্রখ্যাত বিশ্ববিদ্যালয় শিক্ষকদের লেকচার শিট বা সিনিয়রদের স্পেশাল হ্যান্ডনোট স্টাইল।
- **উপাদান:** "বিগত সালের পরীক্ষার প্রশ্ন বিশ্লেষণ", রাষ্ট্রবিজ্ঞানীদের প্রামাণ্য কোটেশন কার্ড, তাত্ত্বিক বৈশিষ্ট্যের বুলেট পয়েন্ট, ক-বিভাগ/খ-বিভাগ ভিত্তিক প্রশ্নের কাঠামো।
- **টোন:** অ্যাকাডেমিক, বস্তুনিষ্ঠ ও তথ্যবহুল।

#### ৩. স্টেপ-বাই-স্টেপ প্র্যাকটিক্যাল গাইড ও নোটিশ (পরীক্ষা, রুটিন, ফরম পূরণ)
- **কোথায় প্রযোজ্য:** আলিম/এসএসসি পরীক্ষার রুটিন, সার্টিফিকেট সংশোধন, ভর্তি বিজ্ঞপ্তি।
- **ডিজাইন ও লেআউট:** সরাসরি কাজের কথা (Zero Fluff)। স্টেপ ইন্ডিকেটর (Step 1 ➡️ Step 2 ➡️ Step 3), জরুরি সতর্কবার্তা বক্স (Alert Box), সময়সূচির পরিষ্কার তালিকা এবং অফিশিয়াল লিংক।
- **টোন:** সংক্ষিপ্ত, স্পষ্ট, সহমর্মিতাপূর্ণ ও দিকনির্দেশনামূলক।

#### ৪. স্কুল শিক্ষার্থী বান্ধব গাইড (Class 6–10 ও ইংরেজি প্যাসেজ)
- **কোথায় প্রযোজ্য:** ক্লাস ৬ এর ইংরেজি প্যাসেজ, ব্যাকরণ, স্কুলের সাধারণ গণিত।
- **ডিজাইন ও লেআউট:** শিক্ষকের সাথে ছাত্রের বন্ধুত্বপূর্ণ ক্লাসরুম স্টাইল।
- **উপাদান:** রঙিন প্যাসেজ হাইলাইট, শব্দার্থ ও বিপরীত শব্দের কার্ড, মডেল প্রশ্ন (MCQ & Short Questions), বাংলায় অর্থ ও প্র্যাকটিস কুইজ।
- **টোন:** সহজ-সরল, শিক্ষণীয় ও অনুপ্রেরণাদায়ী।

#### ৫. বিসিএস ও চাকরি রিভিশন শিট (Job Prep & Competitive Exams)
- **কোথায় প্রযোজ্য:** জব স্টাডি, বিসিএস প্রস্তুতি, সাধারণ জ্ঞান, শর্টকাট গণিত।
- **ডিজাইন ও লেআউট:** বুলেট শিট ও হাই-ইল্ড ফ্যাক্টস (High-yield summary)।
- **উপাদান:** "এক নজরে মনে রাখার টেকনিক", বিগত বছরের পিএসসি প্রশ্ন সমাধান, দ্রুত রিভিশন ছক।
- **টোন:** দ্রুত পাঠযোগ্য, তথ্যঘন ও কৌশলভিত্তিক।

---

### B. Anti-AI Writing Nuances (রোবটিক ভাষা দূর করার কৌশল)

1. **Sentence Burstiness (বাক্যের দৈর্ঘ্যের বৈচিত্র্য):** এআই সবসময় একই মাপের লম্বা বাক্য লেখে। কিন্তু মানুষ কখনো খুব ছোট বাক্য লেখে ("কথাটি শুনতে অদ্ভুত লাগতে পারে।"), আবার পরক্ষণেই একটি বিশ্লেষণধর্মী বড় বাক্য লেখে, তারপর আবার একটি প্রশ্ন ছুঁড়ে দেয় ("তাহলে মূল সমস্যা কোথায়?")। এই ছন্দ বজায় রাখতে হবে।
2. **ক্লিশে ও বাঁধাধরা শব্দের বর্জন:** নিচের কৃত্রিম রোবটিক শব্দগুলো পরিহার করতে হবে:
   - ❌ "পরিশেষে বলা যায়...", "উপর্যুক্ত আলোচনার প্রেক্ষিতে...", "তদুপরি...", "সারসংক্ষেপ (Quick Overview):" (সব পোস্টে একই শব্দ ব্যবহার নিষিদ্ধ)।
   - ✅ স্বাভাবিক মানবিক রূপান্তর: "সহজ কথায় বলতে গেলে...", "পরীক্ষায় ভালো নম্বরের জন্য যা মনে রাখা জরুরি...", "আসুন জেনে নেওয়া যাক...", "বাস্তব অভিজ্ঞতা থেকে দেখা যায়..."।
3. **CSS ও ভিজ্যুয়াল স্টাইলের বৈচিত্র্য:** 
   - সব পোস্টে একই নীল বর্ডার (`border-left: 5px solid #1a73e8`) বা একই ধূসর বক্স চাপিয়ে দেওয়া যাবে না।
   - পোস্টের বিষয় অনুযায়ী কখনো বর্ডারলেস মিনিমালিস্ট ডিজাইন, কখনো হালকা স্লেট/অ্যাম্বার কার্ড, কখনো সিম্পল প্যারাগ্রাফ স্পেসিং ব্যবহার করতে হবে।
4. **প্রয়োজন অনুযায়ী উপাদান নির্ধারণ:** যে পোস্টে সূচিপত্র বা টেবিলের প্রয়োজন নেই (যেমন: নোটিশ, কবিতা বা ছোট গাইড), সেখানে জোর করে সূচিপত্র বা টেবিল ঢুকানো সম্পূর্ণ নিষিদ্ধ।

---

## 🔍 7. Search Console & Indexing Health (গুগল সার্চ কনসোল ও ইনডেক্সিং)

- Submit sitemaps: `/sitemap.xml` and `/atom.xml?redirect=false&start-index=1&max-results=500`.
- Monitor **Page Indexing** report:
  - Fix "Discovered - currently not indexed" by improving internal linking and content depth.
  - Fix "Crawled - currently not indexed" by eliminating duplicate/thin content and updating freshness.
- Test Core Web Vitals: Ensure LCP $< 2.5\text{s}$, FID/INP $< 200\text{ms}$, CLS $< 0.1$.

