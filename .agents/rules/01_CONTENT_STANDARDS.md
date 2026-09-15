# ✍️ 01_CONTENT_STANDARDS.md — Editorial & Writing Standards
### Helptrickbd.com High-Value Content & Human Architecture

> [!IMPORTANT]
> **AdSense Core Rule**: Google AdSense rejects websites with "Low Value Content" or regurgitated robotic AI text. Every article published under this domain must read as if authored by a senior Bangladeshi academic, educator, or certified industry specialist.

---

## 🌐 1. Language Preservation Policy (ভাষার বিশুদ্ধতা রক্ষা)
1. **English Articles Stay 100% English**:
   - If an existing post or topic is in English, its text, headings, tables, FAQs, and metadata MUST remain **100% in English**.
   - Converting an English post to Bengali (or vice-versa) is **STRICTLY PROHIBITED**.
2. **Bengali Articles Stay 100% Bengali**:
   - Bengali articles must use natural, grammatically sound standard Sadhu-Cholit (standard contemporary Bengali) with zero broken phrasing or robotic literal translations.
   - Avoid unneeded English script inside Bengali text except for technical acronyms (e.g., RAM, ROM, CPU, URL, API).
3. **Zero Mixed Script Thumbnails**:
   - Bengali post ➡️ 100% Bengali thumbnail title and badges.
   - English post ➡️ 100% English thumbnail title and badges.

---

## 📏 2. Length, Depth & Non-Destructive Augmentation
1. **Word Count Standard**:
   - **Minimum Length**: 1,200 words.
   - **Target Standard**: 1,400–1,800+ words for competitive search queries.
   - **Zero Thin Content**: Never leave a post under 1,000 words.
2. **Non-Destructive Augmentation (লেখকের মূল লেখা অক্ষুণ্ণ রাখা)**:
   - When expanding an existing or thin post written by the site owner, the **original user text must remain preserved verbatim**.
   - The agent augments the article by adding:
     * A rich, engaging introduction and context setup **before** the original text.
     * In-depth analysis, case studies, comparison tables, model Q&A, and reference frameworks **after** the original text.

---

## 🔤 3. Typography & Cleanliness
1. **Bengali Font Standard**:
   - Default font for Bengali content: `SolaimanLipi` (applied cleanly via `@font-face` from jsDelivr / Ekushey CDN).
   - Never use fonts that distort Bengali conjuncts (যেমন: ১, ঙ্গ, ঙ্ক, ত্র, ক্ষ, ষ্ণ).
2. **Zero-Emoji Policy (১০০% ইমোজি বর্জন — Absolute Ban)**:
   - পোস্টের টাইটেল, সাবটাইটেল, হেডিং (H2, H3), সূচিপত্র (TOC), পড়ার সময় মেটা ব্যাজ, কলআউট বক্স কিংবা পোস্ট বডির কোথাও কোনো ধরণের ইমোজি (`📌`, `👉`, `📢`, `⏱️`, `✅`, `🎓`, `📘`, `💬`, `💡`, `⚠️`, `🔍`, `🚀`, `⭐`, `❶`, `❷` ইত্যাদি) ব্যবহার সম্পূর্ণ নিষিদ্ধ।
   - সূচিপত্রে কোনো হাত নির্দেশক (`👉`) বা পিন (`📌`) থাকবে না। সূচিপত্র হবে পরিপাটি টাইপোগ্রাফিক ("সূচিপত্র (গুরুত্বপূর্ণ বিষয়বস্তু)") এবং আইটেমগুলো ক্লিন বুলেট (`• ` বা `— `) বা নম্বরযুক্ত হবে।
   - কলআউট বক্সে ইমোজির বদলে মার্জিত টেক্সট ("পরামর্শ:", "সতর্কতা:", "নোট:") ব্যবহার করতে হবে।
   - মেটা ব্যাজে ইমোজিহীন টেক্সট ("পড়ার সময়:", "সর্বশেষ সংস্করণ: ২০২৬") ব্যবহার করতে হবে।
3. **Native Theme Share Governance (কাস্টম শেয়ার বক্স সম্পূর্ণ নিষিদ্ধ)**:
   - ব্লগারে প্রতিটি পোস্টের নিচে থিমের নিজস্ব সোশ্যাল শেয়ার প্লাগইন (Facebook, Twitter, WhatsApp, ইত্যাদি) বিল্ট-ইনভাবে প্রদর্শিত হয়।
   - কোনো পোস্টের বডির ভেতর কৃত্রিম কাস্টম শেয়ার বক্স (`<div class="ht-social-share-box">` বা "আপনার সহপাঠী ও বন্ধুদের সাথে শেয়ার করুন") যুক্ত করা সম্পূর্ণ নিষিদ্ধ।
   - পোস্টের কনটেন্ট কনক্লুশন বা এফএকিউ-এর সাথে সাথে পরিচ্ছন্নভাবে শেষ হবে, যাতে থিমের নিজস্ব শেয়ার বাটনগুলো প্রাকৃতিক সৌন্দর্যে প্রকাশিত হয়।
4. **Mandatory Jump Break (`<!--more-->`) Strictly AFTER Hero Image (হিরো ইমেজের পরে বাধ্যতামূলক মোর ট্যাগ)**:
   - পোস্টের মূল ব্যানার বা হিরো ইমেজ (`<img>`) সবার উপরে থাকবে এবং তার নিচে ভূমিকা প্যারাগ্রাফের ঠিক পরে `<!--more-->` ট্যাগ বসাতে হবে।
   - **কঠোর নিষেধাজ্ঞা:** কোনো অবস্থাতেই মূল হিরো ইমেজের আগে `<!--more-->` ট্যাগ বসানো সম্পূর্ণ নিষিদ্ধ। ইমেজের পূর্বে `<!--more-->` বসালে ব্লগার স্বয়ংক্রিয়ভাবে ফিড থেকে ছবি বাদ দিয়ে দেয়, যার ফলে হোমপেজ, ক্যাটাগরি গ্রিড এবং রিলেটেড পোস্ট উইজেটে ("YOU MAY LIKE") ব্রোকেন বা ধূসর ক্যামেরা আইকন (`noThumb`) প্রদর্শিত হয়।
   - প্রি-ফ্লাইট কোয়ালিটি চেকার স্বয়ংক্রিয়ভাবে নিশ্চিত করে যে প্রথম `<img>` ট্যাগটি যেন অবশ্যই `<!--more-->`-এর পূর্বে অবস্থান করে।
5. **Zero Over-Engineered / Garish Styling & Simplicity First (অতিরঞ্জিত কোড ও চড়া স্টাইল বর্জন — সিম্পলিসিটি ফার্স্ট)**:
   - কোনো পোস্টে বা থিমে চোখে পড়ার মতো অতিরঞ্জিত (Over-the-top / Garish), অতিরিক্ত রঙিন, ভারী শ্যাডো, জটিল বক্সিং বা অপ্রয়োজনীয় ভারী সিএসএস কোড লেখা সম্পূর্ণ নিষিদ্ধ।
   - কন্টেন্টের ভিজ্যুয়াল লুক হবে অত্যন্ত সহজ-সরল, মার্জিত, পাঠ্যপুস্তক ও জাতীয় দৈনিকের মতো পরিচ্ছন্ন (Clean, Minimalist & Highly Readable)।
   - থিমের মূল লেআউট, উইডথ, মার্জিন বা কন্টেইনারে প্রভাব ফেলে এমন কোনো বিধ্বংসী সিএসএস বা জাভাস্ক্রিপ্ট কখনো জেনারেট করা যাবে না। থিমের নিজস্ব রেসপনসিভনেস অক্ষুণ্ণ রাখতে হবে।
6. **Vector Icons Over Emojis (ইমোজির বদলে মার্জিত ভেক্টর আইকন ও পরিমিত ব্যবহার)**:
   - শিশুদের মতো চটুল ইমোজি সম্পূর্ণ বর্জন করতে হবে।
   - নির্দেশক বা চিহ্নিতকরণের ক্ষেত্রে একান্ত প্রয়োজন হলে মার্জিত ও পরিমিতভাবে ক্লিন ভেক্টর আইকন (SVG বা থিমের বিল্ট-ইন FontAwesome আইকন যেমন `<i class="fa-solid fa-check"></i>`) ব্যবহার করতে হবে।
   - অহেতুক আইকনের ভিড় জমিয়ে লেখার স্বাভাবিক পাঠযোগ্যতা নষ্ট করা যাবে না; পোস্ট যতটা সম্ভব সিম্পল ও পরিচ্ছন্ন রাখতে হবে।

---

## 🎨 4. The 5 Human Content Archetypes (মানবিক আর্কিটাইপ বৈচিত্র্য)
Never apply a single cookie-cutter format to all posts. Match the structure to the target audience:

### Archetype A: বিশ্ববিদ্যালয় লেকচার হ্যান্ডনোট (University Lecture Handnote)
- **Target Audience**: অনার্স ও মাস্টার্স শিক্ষার্থী (রাষ্ট্রবিজ্ঞান, সমাজবিজ্ঞান, অর্থনীতি)।
- **Tone**: অ্যাকাডেমিক, বিশ্লেষণধর্মী, প্রামাণ্য রেফারেন্স সমৃদ্ধ।
- **Key Elements**: তাত্ত্বিক সংজ্ঞা, প্রখ্যাত পণ্ডিতদের উক্তি (Blockquotes), বৈশিষ্ট্য ছক, বিগত জাতীয় বিশ্ববিদ্যালয়ের প্রশ্ন বিশ্লেষণ।

### Archetype B: বিসিএস ও সরকারি চাকরি বুলেট শিট (Job Prep Bullet Sheet)
- **Target Audience**: বিসিএস ও ব্যাংক/প্রাইমারি শিক্ষক নিয়োগ প্রার্থী।
- **Tone**: সরাসরি, তথ্যঘন, দ্রুত রিভিশন উপযোগী।
- **Key Elements**: একনজরে তথ্য ছক, বিগত সালের প্রিলিমিনারি প্রশ্ন সমাধান, ভাইভা টিপস, স্মৃতিসহায়ক শর্ট টেকনিক।

### Archetype C: প্র্যাকটিক্যাল টিউটোরিয়াল স্টেপ কার্ড (Step-by-Step How-To Guide)
- **Target Audience**: সাধারণ নাগরিক, শিক্ষার্থী, প্রযুক্তি ব্যবহারকারী।
- **Tone**: নির্দেশনামূলক, সহজবোধ্য, আশ্বস্তকারী।
- **Key Elements**: ধাপে ধাপে নম্বরযুক্ত কার্ড (`ধাপ ০১`, `ধাপ ০২`), আসল পোর্টালের স্ক্রিনশট ও অ্যানোটেশন, প্রয়োজনীয় ডকুমেন্টের চেকলিস্ট, সম্ভাব্য সমস্যা ও সমাধান।

### Archetype D: সাহিত্যিক ও জীবনভিত্তিক প্রবন্ধ (Literary & Historical Essay)
- **Target Audience**: সাহিত্যপ্রেমী ও সাধারণ পাঠক।
- **Tone**: প্রাঞ্জল, ভাবগাম্ভীর্যপূর্ণ, ঐতিহাসিক বর্ণনা।
- **Key Elements**: জীবনবৃত্তান্ত ছক, মূল সৃষ্টির তাৎপর্য, সমকালীন প্রাসঙ্গিকতা।

### Archetype E: স্কুল ও বোর্ড স্টাডি গাইড (School & Board Exam Study Guide)
- **Target Audience**: ষষ্ঠ থেকে দশম শ্রেণি, এসএসসি ও এইচএসসি শিক্ষার্থী।
- **Tone**: শিক্ষার্থীবান্ধব, সহজ ব্যাখ্যা, বোর্ড পরীক্ষা কেন্দ্রিক।
- **Key Elements**: পাঠ্যবইয়ের সহজ সারাংশ, নমুনা জ্ঞানমূলক ও অনুধাবনমূলক প্রশ্ন-উত্তর, বোর্ড পরীক্ষার কমন টিপস।

---

## 🏷️ 5. Position 0 & Structured Data (SEO Microdata)
1. **Position 0 Quick Answer**:
   - Provide a concise 40–60 word direct definition or answer within the first 100 words to target Google Featured Snippets.
2. **Schema.org Microdata**:
   - Embed valid `application/ld+json` schema at the end of the post HTML:
     * `BlogPosting` schema with `headline`, `author`, `publisher`, `image`, and `datePublished`.
     * `FAQPage` schema containing at least 3–5 high-intent FAQ questions and comprehensive answers.

---

## 🏛️ 6. বাংলাদেশ সরকারি তথ্য ও অ্যান্টি-হ্যালুসিনেশন নীতিমালা (BD Grounding)
1. **সরকারি সাইট ও গেজেট ভেরিফিকেশন**:
   - শিক্ষাবোর্ড আবেদন (যেমন: ঢাকা শিক্ষা বোর্ড `dhakaeducationboard.gov.bd`), বিসিএস (`bpsc.gov.bd`), জাতীয় বিশ্ববিদ্যালয় (`nu.ac.bd`), এনআইডি (`nidw.gov.bd`), এবং সরকারি চাকরির আবেদন সম্পর্কিত যেকোনো পোস্ট লেখার সময় তথ্য সবসময় আসল সরকারি গেজেট ও পোর্টাল অনুযায়ী ভেরিফাই করতে হবে।
2. **জিরো ফ্যাব্রিকেশন (No Invented Numbers/Dates)**:
   - কোনো কাল্পনিক সোনালী সেবা ফি, ভুয়া বিজ্ঞপ্তির তারিখ, ভুল আবেদন লিঙ্ক বা অস্পষ্ট নিয়ম বানিয়ে লেখা সম্পূর্ণ নিষিদ্ধ।
   - ফি বা নিয়ম পরিবর্তনশীল হলে সরকারি ওয়েবসাইটের সর্বশেষ নোটিশ উল্লেখ করে লিঙ্ক বা নির্দেশিকা দিতে হবে।

---

## 🔗 7. লাইভ ইন্টারনাল লিঙ্কিং ইন্টিগ্রিটি (Zero Dead Links)
1. **শুধুমাত্র লাইভ ইউআরএল ব্যবহার**:
   - আর্টিকেলে ইন্টারনাল লিঙ্ক দেওয়ার সময় কেবল `helptrickbd.com`-এর ইতিমধ্যে লাইভ ও গুগল ইনডেক্সড থাকা পোস্টগুলোর লিংক ব্যবহার করতে হবে।
   - ড্রাফট অবস্থায় থাকা পোস্টের অনুমিত লিংক বা ভাঙা অ্যাঙ্কর (`href="#"` বা `href=""`) ব্যবহার করা সম্পূর্ণ নিষিদ্ধ।
2. **লিংক ট্র্যাকার ভেরিফিকেশন**:
   - লিঙ্ক যুক্ত করার পূর্বে `tools/indexer/all_fixed_urls.txt` অথবা `audit_adsense_policy_live.json` ফাইল দেখে লাইভ ইউআরএল নিশ্চিত করতে হবে।
