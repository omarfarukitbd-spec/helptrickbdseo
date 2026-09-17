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
7. **Post-Level Responsive Styling Architecture (পোস্টের নিজস্ব মার্জিত ও রেসপনসিভ সিএসএস আর্কিটেকচার)**:
   - **ইন-পোস্ট সিএসএস স্টাইল সম্পূর্ণ অনুমোদিত ও স্ট্যান্ডার্ড:** ব্যবহারকারীর স্পষ্ট নির্দেশনায় প্রতিটি আর্টিকেলে নিখুঁত পাঠযোগ্যতা ও রেসপনসিভনেস নিশ্চিত করতে পোস্টের নিজস্ব `<style>` ব্লক ব্যবহার করা হবে (রেফারেন্স: `secularism-vs-islamic-values-in.html`)।
   - **স্ট্যান্ডার্ড উপাদান ও ক্লাসসমূহ:**
     * *হেডিং (`.htbd-academic-heading`):* গাড় নেভি কালার (`#0c2340`), বামে ৫px অ্যাকসেন্ট বর্ডার (`#d4af37` বা `#1e3a8a`), প্যাডিং-লেফট ১৪px, মার্জিন ও বোল্ড ফন্ট।
     * *সাব-হেডিং (`.htbd-academic-subheading`):* রয়াল ব্লু (`#1e3a8a`), ২০px ফন্ট, ফন্ট-ওয়েট ৬০০।
     * *সারসংক্ষেপ অ্যান্সার বক্স (`.htbd-overview-box`):* সফট ব্যাকগ্রাউন্ড (`#f8fafd`), সূক্ষ্ম বর্ডার (`#dbeafe`), বামে ৫px নেভি বর্ডার (`#0c2340`), রাউন্ডেড কর্নার ও সূক্ষ্ম শ্যাডো।
     * *সূচিপত্র বক্স (`.htbd-toc-card`):* পরিচ্ছন্ন ব্যাকগ্রাউন্ড (`#f8fafc`), সূক্ষ্ম স্লেট বর্ডার ও সুবিন্যস্ত লিঙ্ক।
     * *তুলনামূলক ও তথ্য সারণী (`.htbd-academic-table`):* নেভি হেডার (`#0c2340`), সাদা টেক্সট, অল্টারনেটিং রো (`#f8fafc`), সূক্ষ্ম বর্ডার (`#e2e8f0`) এবং মোবাইল স্ক্রোল র‍্যাপার।
     * *পরামর্শ/সতর্কতা বক্স (`.htbd-exam-card` / `.htbd-tip-card`):* শান্ত ব্যাকগ্রাউন্ড (হালকা সবুজ `#f0fdf4` বা হালকা অ্যাম্বার `#fefce8`), সূক্ষ্ম বর্ডার এবং ১০০% স্পষ্ট পঠনযোগ্য ডার্ক টেক্সট (কোনো ডার্ক-অন-ডার্ক রঙের ত্রুটি ছাড়া)।
     * *ডাউনলোড বক্স ও সিরিজ বক্স:* মার্জিত ডাউনলোড বাটন ও সাইলো নেভিগেশন কার্ড।

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

---

## ১০. পোস্ট-লেভেল সিএসএস ও ডার্ক-লাইট বাই-মোডাল স্টাইলিং নীতিমালা (Mandatory Bi-Modal Light & Dark Mode Styling Protocol)

ভবিষ্যতে ব্লগারে যে কোনো নতুন পোস্ট তৈরি বা পুরনো পোস্ট সম্পাদনার সময় পোস্টের ভেতরে যত সিএসএস (CSS) লেখা হবে, তা লাইট মোড (Light Mode) এবং ডার্ক মোড (Dark Mode) উভয় মোডেই যেন শতভাগ দৃষ্টিনন্দন, নিখুঁত কনট্রাস্ট ও পাঠযোগ্য থাকে। কোনো পোস্ট শুধুমাত্র লাইট মোডের কথা চিন্তা করে ডিজাইন করা কঠোরভাবে নিষিদ্ধ।

### ১. মূল দর্শন ও নীতি (Core Mandate):
- হেল্পট্রিকবিডি সাইটে বহু পাঠক ডার্ক মোড ব্যবহার করেন। তাই আর্টিকেলের ভেতর ব্যবহৃত যে কোনো বক্স, কার্ড, টেবিল, সূচিপত্র, হাইলাইট বা টেক্সট এলিমেন্ট লাইট ও ডার্ক উভয় অবস্থায় স্বয়ংক্রিয়ভাবে খাপ খাইয়ে নিতে হবে।
- এমন কোনো রঙ বা স্টাইল নির্বাচন করা যাবে না যা ডার্ক মোডে গেলে কালো ব্যাকগ্রাউন্ডের সাথে মিশে যায় বা সাদা ব্যাকগ্রাউন্ডে সাদা হয়ে অস্পষ্ট হয়ে পড়ে।

### ২. ইনলাইন হার্ডকোডেড স্টাইল বর্জন (Ban on Inflexible Inline Styles):
- আর্টিকেলের ভেতরে এইচটিএমএল ট্যাগে সরাসরি হালকা ব্যাকগ্রাউন্ড ও গাঢ় লেখার রঙ হার্ডকোড করা নিষিদ্ধ:
  ```html
  <!-- নিষিদ্ধ ইনলাইন স্টাইল (ডার্ক মোডে এটি অপরিবর্তিত থেকে কনট্রাস্ট নষ্ট করে) -->
  <div style="background: #ffffff; color: #1e293b; border: 1px solid #e2e8f0;">...</div>
  ```
- **সঠিক পদ্ধতি:** সবসময় অর্থপূর্ণ সিএসএস ক্লাস (CSS Class) অথবা থিমের প্রি-ডিফাইনড স্ট্যান্ডার্ড সিলেক্টর ব্যবহার করতে হবে।

### ৩. পোস্ট-লেভেল কাস্টম `<style>` ব্লকের ক্ষেত্রে দ্বিমুখী বাই-মোডাল আর্কিটেকচার:
যদি কোনো বিশেষ আর্টিকেলের জন্য পোস্টের ভেতরে কাস্টম `<style>` ব্লক লিখতে হয়, তবে বাধ্যতামূলকভাবে একই সাথে লাইট মোড এবং ডার্ক মোডের রুল লিখতে হবে:
```html
<style>
  /* ১. লাইট মোড ডিফল্ট (Light Mode Default) */
  .htbd-custom-card {
    background: #f8fafc;
    color: #1e293b;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 16px;
    margin: 16px 0;
  }
  .htbd-custom-card h3 {
    color: #0f172a;
  }
  .htbd-custom-card a {
    color: #2563eb;
    text-decoration: underline;
  }

  /* ২. ডার্ক মোড বাধ্যতামূলক অভিযোজন (Dark Mode Mandatory Adaptation) */
  .dark .htbd-custom-card,
  #mainContent.dark .htbd-custom-card {
    background: #1e293b !important;
    color: #f1f5f9 !important;
    border-color: #334155 !important;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3) !important;
  }
  .dark .htbd-custom-card *,
  #mainContent.dark .htbd-custom-card * {
    color: inherit !important;
  }
  .dark .htbd-custom-card h3,
  #mainContent.dark .htbd-custom-card h3 {
    color: #ffffff !important;
  }
  .dark .htbd-custom-card a,
  #mainContent.dark .htbd-custom-card a {
    color: #38bdf8 !important;
  }
</style>
```

### ৪. অফিসিয়াল ডার্ক মোড কালার প্যালেট স্পেসিফিকেশন:
পোস্টের সিএসএস লেখার সময় নিচের স্ট্যান্ডার্ড প্যালেট অনুসরণ করতে হবে:
- **কার্ড/বক্স ব্যাকগ্রাউন্ড:** `#1e293b` (ডার্ক স্লেট) অথবা `#0f172a` (ডিপ ব্যাকগ্রাউন্ড)।
- **হেডিংস (H1–H4) ও বোল্ড টেক্সট:** `#ffffff` (১০০% ক্রিস্টাল ক্লিয়ার সাদা)।
- **প্যারাগ্রাফ ও বডি টেক্সট:** `#cbd5e1` বা `#f1f5f9` (উজ্জ্বল আরামদায়ক ধূসর-সাদা)।
- **বর্ডার ও ডিভাইডার:** `#334155` বা `#475569`।
- **হাইপারলিংক:** `#38bdf8` (উজ্জ্বল স্কাই ব্লু) এবং হোভারে `#7dd3fc`।
- **সহযোগী টেক্সট ও ক্যাপশন:** `#94a3b8` (মিউটেড স্লেট)।

### ৫. টেবিল ও ডেটা গ্রিডের বাই-মোডাল নিয়ম:
পোস্টে টেবিল যুক্ত করলে তা লাইট মোডে যেমন পরিচ্ছন্ন থাকবে, ডার্ক মোডেও যেন পড়ার উপযোগী থাকে:
- হেডার (`th`): ডার্ক মোডে ব্যাকগ্রাউন্ড `#0f172a`, টেক্সট `#38bdf8`।
- সেল (`td`): ডার্ক মোডে ব্যাকগ্রাউন্ড `#1e293b`, টেক্সট `#cbd5e1`।
- বর্ডার: ডার্ক মোডে `#334155`।

### ৬. অটোমেটেড প্রি-ফ্লাইট কোয়ালিটি গেটওয়ে এনফোর্সমেন্ট:
কোনো পোস্ট পাবলিশ করার পূর্বে বাধ্যতামূলকভাবে কোয়ালিটি গেটওয়ে চালাতে হবে:
```bash
python tools/governance/pre_flight_checker.py <PATH_TO_POST_HTML>
```
যদি কোনো পোস্টে এমন সিএসএস পাওয়া যায় যার ডার্ক মোড রুল অনুপস্থিত, তবে প্রি-ফ্লাইট গেটওয়ে স্বয়ংক্রিয়ভাবে পোস্ট পাবলিকেশন আটকে দেবে (`BLOCKED`)।

