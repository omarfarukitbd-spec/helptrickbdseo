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
7. **Theme Native HTML & CSS Architecture (থিমের নিজস্ব ক্লাস ও জিরো-ব্লট পোস্ট স্ট্রাকচার — কঠোর নীতিমালা)**:
   - **ইন-পোস্ট `<style>` ব্লক সম্পূর্ণ নিষিদ্ধ:** পোস্টের ভেতর ৫০-১০০ লাইনের অপ্রয়োজনীয় `<style>` ব্লক বানিয়ে `@font-face`, `.htbd-post-wrapper`, বডি রিসেট, প্যারাগ্রাফ ফন্ট সাইজ বা ডুপ্লিকেট টেবিল সিএসএস লেখা সম্পূর্ণ নিষিদ্ধ। ব্লগারের মূল থিম (FlexSpot Premium) ইতিমধ্যে সোলায়মানলিপি ফন্ট, লাইন-হাইট, হেডিং ও রেসপনসিভনেস সাইটজুড়ে গ্লোবালি নিয়ন্ত্রণ করে।
   - **থিমের নিজস্ব সেমান্টিক ট্যাগ ও ক্লাসের বাধ্যতামূলক ব্যবহার:**
     * *হেডিং:* সাধারণ `<h2>`, `<h3>`, `<h4>` (কোনো অতিরিক্ত ক্লাস ছাড়াই থিম সুন্দর ফ্রন্ট-কালার ও মার্জিন প্রদর্শন করে)।
     * *প্যারাগ্রাফ ও তালিকা:* সাধারণ `<p>`, `<ul>`, `<ol>`, `<li>`।
     * *টেবিল:* সাধারণ `<table>`, `<thead>`, `<tbody>`, `<tr>`, `<th>`, `<td>`। থিম স্বয়ংক্রিয়ভাবে টেবিলকে রেসপনসিভ স্ক্রোল র‍্যাপার দেয় এবং সুন্দর সূক্ষ্ম বর্ডার যুক্ত করে।
     * *সূচিপত্র (Table of Contents):* থিমের নিজস্ব শর্টকোড `<strike>#title=(সূচিপত্র) (toc)</strike>` অথবা সেমান্টিক কন্টেইনার ব্যবহার করতে হবে:
       ```html
       <div class="tociki-pro">
         <div class="tociki-inner">
           <a href="javascript:;" class="tociki-title" role="button" title="সূচিপত্র">
             <span class="tociki-title-text">সূচিপত্র</span>
           </a>
           <ol id="tociki"></ol>
         </div>
       </div>
       ```
     * *অ্যালার্ট ও কলআউট বক্স:* থিমের নিজস্ব শর্টকোড বা ক্লাস ব্যবহার করতে হবে:
       ```html
       <div class="alert-message passed"><strong>পরামর্শ:</strong> গুরুত্বপূর্ণ তথ্য...</div>
       <div class="alert-message warning"><strong>সতর্কতা:</strong> ভুলের ঝুঁকি এড়াতে...</div>
       <div class="alert-message success"><strong>টিপস:</strong> দ্রুত প্রস্তুতির উপায়...</div>
       ```
     * *কোড বক্স:* `<pre class="code-box">কোড বা কমান্ড<button class="tune">Copy Now</button><input id="showlink" readonly="readonly" type="text" value="কোড"/></pre>`
     * *অ্যাকশন বাটন:* `<a class="main-button button sp-bt download" href="...">...</a>`
   - **কাস্টম সিএসএস ব্যবহারের একমাত্র ব্যতিক্রম:** যদি এমন কোনো উপাদান তৈরি করতে হয় যা মূল থিমে নেই (যেমন: ইন্টারনাল ধারাবাহিক পোস্টের সিরিজ নেভিগেশন বক্স বা বিশেষ ধাপ নির্দেশক কার্ড), তবেই কেবল সেই উপাদানের জন্য অত্যন্ত সংক্ষিপ্ত ও ক্লিন ইনলাইন সিএসএস ব্যবহার করা যাবে।
   - **চড়া রঙ বর্জন ও পাঠের পরম আরাম (Zero Colorful Glitz & High Legibility):** ইউজারের নির্দেশনা অনুযায়ী অতিরিক্ত রঙিন কোনো কিছু সম্পূর্ণ বর্জন করতে হবে। স্টাইল হবে মার্জিত, নিখুঁত পাঠ্যপুস্তকের মতো শান্ত ও পরিচ্ছন্ন। অফ-হোয়াইট বা সাদা ব্যাকগ্রাউন্ড, সূক্ষ্ম স্লেট বর্ডার (`#e2e8f0`), গাড় কালো টেক্সট (`#0f172a`, `#202124`) ও পরিমিত হালকা অ্যাকসেন্ট—যাতে ভিজিটর দীর্ঘক্ষণ পড়তে আরাম পান।

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

---

## 🕸️ 8. টপিকাল সাইলো ইন্টারনাল লিঙ্কিং ও অমিল পোস্ট বর্জন নীতিমালা (Topic Silo Architecture & Relevancy-Only Protocol)
1. **শর্তসাপেক্ষ টপিকাল সাইলো (Contextual & Highly Relevant Silo Only)**:
   - কোনো পোস্টের সাথে যদি একই বিষয়ের বা সিলেবাসের (যেমন: মাস্টার্স শেষ পর্ব রাষ্ট্রবিজ্ঞান, বিসিএস প্রস্তুতি, ইত্যাদি) একাধিক লাইভ পোস্ট বিদ্যমান থাকে, তবেই সেখানে টপিকাল সাইলো আর্কিটেকচার কার্যকর হবে:
     * **ইন-টেক্সট কনটেক্সচুয়াল লিংক**: লেখার ভেতর প্রাসঙ্গিক কি-ওয়ার্ডের ওপর স্বাভাবিকভাবে লিংক দেওয়া হবে।
     * **সিলেবাস সিরিজ নেভিগেটর বক্স**: পোস্টের শেষে এবং রেফারেন্সের পূর্বে একটি পরিচ্ছন্ন হ্যান্ডনোট সিরিজ সূচি যুক্ত থাকবে (যেমন: অধ্যায় ১, অধ্যায় ২, অধ্যায় ৩ ইত্যাদি)।
2. **কাছাকাছি পোস্ট না থাকলে শতভাগ স্কিপ (Strict Skip When No Relevant Match — অমিল পোস্ট সম্পূর্ণ নিষিদ্ধ)**:
   - যদি পোস্টটির সাথে সামঞ্জস্যপূর্ণ বা কাছাকাছি বিষয়ের কোনো লাইভ পোস্ট বিদ্যমান না থাকে, তবে কোনো অবস্থাতেই অমিল, ভিন্ন ক্যাটাগরি বা অপ্রাসঙ্গিক বিষয়ের লিংক (যেমন: রাষ্ট্রবিজ্ঞানের ভেতর সার্টিফিকেট সংশোধন বা আইসিটির লিংক) জোর করে ঢোকানো **সম্পূর্ণ নিষিদ্ধ**।
   - কাছাকাছি বিষয়ের কোনো পোস্ট না থাকলে ইন্টারনাল লিঙ্কিং স্বয়ংক্রিয়ভাবে **সম্পূর্ণ স্কিপ (Skip)** করতে হবে। কোনো অবস্থাতেই অপ্রাসঙ্গিক লিংক দিয়ে পোস্টের পাঠযোগ্যতা ও এসইও মান নষ্ট করা যাবে না।
3. **অ্যাঙ্কর টেক্সটের বিশুদ্ধতা (Descriptive Anchor Text)**:
   - কখনোই *"এখানে ক্লিক করুন"* বা *"এই লিংকে যান"* লিখবেন না। সবসময় বিষয়ের সুনির্দিষ্ট কি-ওয়ার্ড দিয়ে হাইপারলিংক তৈরি করতে হবে।
4. **দ্বিমুখী ভারসাম্য (Bi-Directional Mesh)**:
   - একটি সাইলোর প্রতিটি পোস্ট যেন একে অপরের সাথে সংযুক্ত থাকে, কোনো পোস্ট যাতে একা বা বিচ্ছিন্ন (Orphan Post) হয়ে না পড়ে।

---

## 🛡️ 9. ডুপ্লিকেট টপিক ও ক্যানিব্যালাইজেশন প্রতিরোধ নীতিমালা (Anti-Cannibalization & Duplicate Guard Protocol)
1. **পিডিএফ/টপিক প্রি-স্ক্যান বাধ্যবাধকতা**:
   - ইউজার কর্তৃক প্রেরিত কোনো পিডিএফ (PDF), সিলেবাস বা প্রশ্নের তালিকা থেকে কনটেন্ট তৈরি করার পূর্বে অবশ্যই সাইটের বিদ্যমান সমস্ত লাইভ পোস্টের ডেটাবেজ (`all_live_posts_catalog.json`) স্ক্যান করতে হবে।
   - অটোমেটেড গার্ড কমান্ড:
     ```bash
     python tools/governance/topic_cannibalization_guard.py --topics "<TOPIC_1>" "<TOPIC_2>"
     # অথবা ফাইল/পিডিএফ মোড:
     python tools/governance/topic_cannibalization_guard.py --pdf <PATH_TO_PDF>
     python tools/governance/topic_cannibalization_guard.py --file <PATH_TO_TXT_OR_JSON>
     ```
2. **ডুপ্লিকেট শনাক্ত হলে তাৎক্ষণিক স্কিপ ও ইউজারকে অবহিতকরণ**:
   - যদি পিডিএফ-এর কোনো প্রশ্ন বা টপিকের বিস্তারিত বিশ্লেষণ ইতিমধ্যে ওয়েবসাইটে কোনো পোস্টে প্রকাশিত হয়ে থাকে (যেমন: ৫০% বা তার বেশি প্রাসঙ্গিকতা/সাদৃশ্য):
     * সেই টপিকটি নিয়ে নতুন পোস্ট তৈরি করা সম্পূর্ণ নিষিদ্ধ (Keyword Cannibalization রোধ করতে)।
     * বিদ্যমান লাইভ পোস্টের শিরোনাম ও ইউআরএল সহ ইউজারকে স্পষ্টভাবে চ্যাটে জানাতে হবে।
     * সেই টপিকটি বাদ দিয়ে (Skip) পিডিএফ-এর অন্যান্য আনকভার্ড বা নতুন টপিক নির্বাচন করতে হবে।
3. **ক্যানিব্যালাইজেশনের ঝুঁকি ও এসইও ক্ষতি বর্জন**:
   - একই কি-ওয়ার্ড বা টপিকে একাধিক পোস্ট থাকলে গুগল কনফিউজড হয়ে পেজর‍্যাঙ্ক ভাগ করে দেয় (Keyword Cannibalization)। তাই একটি বিষয়ের ওপর একটিই স্বয়ংসম্পূর্ণ, সমৃদ্ধ পোস্ট বজায় রাখতে হবে।
