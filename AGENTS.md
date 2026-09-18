# 🧠 Project Knowledge & Antigravity Handover Context (AGENTS.md)

This file is automatically loaded by Antigravity IDE into the AI agent's memory whenever this repository is opened on any computer (Home PC, Office Laptop, etc.).

---

## 📌 1. Project Profile & Core Objective
- **Website:** [Helptrickbd.com](https://www.helptrickbd.com/)
- **CMS:** Blogger (Blogspot)
- **Primary Goal:** 100% Google AdSense Approval, Core Web Vitals excellence, and fast Google Search Console ranking.
- **Repository:** `https://github.com/omarfarukitbd-spec/helptrickbdseo.git`
- **Main Branch:** `main`
- **Full Chat & Pair-Programming History:** See [`docs/CHAT_HISTORY.md`](file:///docs/CHAT_HISTORY.md) for the complete 97-turn conversational transcript between user and Antigravity.

---

## 🏛️ Autonomous Agent Governance & Multi-PC Rules System (MANDATORY)
This project enforces a fail-safe, multi-machine agent governance system. Antigravity IDE automatically loads all modular rulebooks from `.agents/rules/` into every agent's core memory across all devices (Home PC, Office Laptop, etc.):

1. **[00_AGENT_CONSTITUTION.md](file:///.agents/rules/00_AGENT_CONSTITUTION.md)**: Supreme authority, Stop-Gates & User Permission Matrix.
2. **[01_CONTENT_STANDARDS.md](file:///.agents/rules/01_CONTENT_STANDARDS.md)**: Word counts (1,200–1,600+), Language strictness (English stays English, Bengali stays Bengali), SolaimanLipi, `<!--more-->` tag, 5 Human Archetypes.
3. **[02_IMAGE_AND_ASSET_RULES.md](file:///.agents/rules/02_IMAGE_AND_ASSET_RULES.md)**: 16:9 banners, 10–20 KB WebP compression, jsDelivr CDN hosting, authentic author thumbnail preservation, UI annotations (Red Box, Arrow, Pin).
4. **[03_PUBLISHING_PERMALINK_RULES.md](file:///.agents/rules/03_PUBLISHING_PERMALINK_RULES.md)**: Mandatory 2-Step Custom English Permalink Minting (Zero generic `blog-post_xx.html`), Blogger API v3, Google Indexing API pinging.
5. **[04_LABEL_TAXONOMY_GOVERNANCE.md](file:///.agents/rules/04_LABEL_TAXONOMY_GOVERNANCE.md)**: Strict Label Permission Gate & AdSense category balance.
6. **[05_MULTI_PC_SYNC_PROTOCOL.md](file:///.agents/rules/05_MULTI_PC_SYNC_PROTOCOL.md)**: Git Pull Strictly Manual (User Instruction Only), Post-Task Auto-Push (`git push origin main`), Secrets safety.
7. **[06_COMMUNICATION_AND_REPORTING_PROTOCOL.md](file:///.agents/rules/06_COMMUNICATION_AND_REPORTING_PROTOCOL.md)**: Mandatory Live Bengali Reporting & 100% Bengali Artifacts (Plans, Walkthroughs & Audits).
8. **[07_POST_BACKUP_AND_RESTORE_PROTOCOL.md](file:///.agents/rules/07_POST_BACKUP_AND_RESTORE_PROTOCOL.md)**: Mandatory Pre-Edit Full Post Backup & Rollback Protocol (Original HTML, Image Manifest, Labels & Metadata).
9. **[08_INQUISITIVE_DISCOVERY_AND_TRUTH_PROTOCOL.md](file:///.agents/rules/08_INQUISITIVE_DISCOVERY_AND_TRUTH_PROTOCOL.md)**: Mandatory Inquisitive Clarification Gate (Zero guesswork on short prompts), Lightning-Fast Execution Once Clear, and Zero Sycophancy (Challenge mistakes with facts, policy & reality; Never blindly agree).
10. **[09_SINGLE_THEME_SOURCE_OF_TRUTH_PROTOCOL.md](file:///.agents/rules/09_SINGLE_THEME_SOURCE_OF_TRUTH_PROTOCOL.md)**: Mandatory Single Theme Source of Truth (Zero separate snippet files; all edits directly inside `Helptrickbd theme code.xml`; zero code duplication; dark mode post contrast & callout inversion engine).
11. **[10_PDF_INGESTION_AND_EXTRACTION_PROTOCOL.md](file:///.agents/rules/10_PDF_INGESTION_AND_EXTRACTION_PROTOCOL.md)**: Mandatory PDF Ingestion, Rapid Extraction & Editorial Correction Protocol (Zero manual page slicing/disk loops; auto-detect Born-Digital vs Scanned; PyMuPDF4LLM & In-Memory Vision Pipeline; mandatory Bengali conjunct/table editorial proofreading).

### 🛡️ Automated Quality Gatekeeper Tools:
- **Pre-Flight Post Validator (Quality Gatekeeper):**
  ```bash
  python tools/governance/pre_flight_checker.py <PATH_TO_HTML> [--metadata <PATH_TO_JSON>]
  ```
  *Every agent MUST run this before publishing. If any check fails, publishing is strictly BLOCKED.*
- **User Permission Gatekeeper:**
  ```bash
  python tools/governance/agent_permission_gate.py <ACTION_NAME> --details "<DETAILS>" [--confirmed]
  ```

---

## 💎 2. Established Architectural Decisions & Standards

### A. Typography & Fonts:
- **Default Font:** `SolaimanLipi` (applied cleanly via CSS `@font-face` from Ekushey CDN / jsDelivr).
- **Reason:** Hind Siliguri had broken conjunct/glyph rendering issues (e.g., numeral ১ and specific Bengali ligatures had distorted spacing). SolaimanLipi renders standard Bengali newspaper-grade typography across all modern browsers and mobile viewports.
- **Master Theme File:** [`Helptrickbd theme code.xml`](file:///Helptrickbd%20theme%20code.xml) (Single source of truth).

### B. Content & Article Architecture Standard:
Every revived or new article MUST strictly adhere to:
1. **Length:** Minimum 1,150–1,500+ words (Zero thin content).
2. **Hero Banner:** 16:9 aspect ratio (`1200x675` px) with high-contrast Bengali title, clean category badge, author attribution, and descriptive `alt` and `title` tags.
3. **Position 0 Optimization:** Quick summary answer box in the first 100 words.
4. **Visual Richness:** Clean comparison table (`table` with SolaimanLipi styling) and highlight callout boxes.
5. **Schema.org Microdata:** Valid `FAQPage` and `BlogPosting` JSON-LD microdata embedded in every post.
6. **Internal & Authority Links:** 2–3 contextual internal links to related live posts on Helptrickbd + authoritative external links.

### C. AdSense Policy & Safety:
- Full live audit completed across all 78 posts.
- **Result:** **0 Critical AdSense Policy Violations** (no copyright issues, no adult content, no deceptive downloads).

### D. Critical Content Preservation & Publishing Rules (কঠোর সম্পাদকীয় নীতিমালা):
1. **Audience & Intent Profiling:** প্রতিটি পোস্টের মূল বিষয়বস্তু দেখে তার টার্গেট পাঠক নিশ্চিত করতে হবে (স্কুল ছাত্র, অনার্স/মাস্টার্স রাষ্ট্রবিজ্ঞান শিক্ষার্থী, চাকরি প্রার্থী, না ইসলামিক পাঠক)।
2. **Strict Language Preservation:** ইংরেজি পোস্ট **১০০% ইংরেজিতেই** রাখতে হবে। কোনো ইংরেজি পোস্ট বাংলায় রূপান্তর করা সম্পূর্ণ নিষিদ্ধ।
3. **Non-destructive Augmentation:** ইউজারের মূল টেক্সট সবসময় অক্ষুণ্ণ রাখতে হবে। পোস্ট বড় করতে হলে ইউজারের লেখার **আগে ভূমিকা** এবং **পরে মডেল প্রশ্ন/বিশ্লেষণ/নোটস** যোগ করতে হবে।
4. **Original Thumbnail Preservation & Custom Template Standard:** লেখকের নিজস্ব থাম্বনেইল থাকলে তা কোনোভাবেই প্রতিস্থাপন করা যাবে না। নতুন থাম্বনেইল তৈরি করতে হলে অবশ্যই `Thumbnail BG/` ফোল্ডারের নির্দিষ্ট ব্যাকগ্রাউন্ড (১ ক্যাটাগরি = ১ ফিক্সড ব্যাকগ্রাউন্ড), অফিসিয়াল হেল্পট্রিকবিডি লোগো এবং `Hind Siliguri Bold` ফন্ট ব্যবহার করতে হবে।
5. **Mandatory `<!--more-->` Jump Break & Byte-0 Top Hero Placement (হিরো ইমেজের বাইট-০ অবস্থান ও পরে বাধ্যতামূলক মোর ট্যাগ):** ব্লগারে পোস্টের মূল ব্যানার বা হিরো ইমেজ (`<figure><img ...></figure>`) এইচটিএমএল ফাইলের একদম শুরুতে (Byte 0 / প্রথম ১০০ ক্যারেক্টারের মধ্যে) অবস্থান করবে। কোনো অবস্থাতেই বড় `<style>` বা সিএসএস ব্লক হিরো ইমেজের পূর্বে বসানো যাবে না, যাতে গুগল ব্লগারের ৮ কেবি (8 KB) থাম্বনেইল স্ক্যানার প্রথম ১০০ ক্যারেক্টারেই ইমেজ পেয়ে যায় এবং এডমিন প্যানেলে ধূসর অক্ষরের ফলব্যাক আইকন তৈরি না হয়। এবং তার নিচে ভূমিকা প্যারাগ্রাফের ঠিক পরেই `<!--more-->` ট্যাগ বসাতে হবে। কোনো অবস্থাতেই হিরো ইমেজের পূর্বে `<!--more-->` বসানো যাবে না। ইমেজের পূর্বে মোর ট্যাগ দিলে ব্লগারে আরএসএস ফিড থেকে ছবি বাদ পড়ে যায় এবং হোমপেজ/রিলেটেড পোস্ট উইজেটে ব্রোকেন ধূসর ক্যামেরা আইকন তৈরি হয়।
6. **Label Governance (ইউজারের পূর্বানুমতি):** পোস্ট পাবলিশ বা আপডেটের আগে অবশ্যই ইউজারকে জিজ্ঞেস করতে হবে কোন লেবেলে যুক্ত হবে এবং কোনো নতুন লেবেল যোগ করা হবে কি না।
7. **Anti-AI Editorial Diversity & Archetypes (স্বাভাবিক মানবিক কনটেন্ট আর্কিটেকচার):** কোনো রোবটিক কুকি-কাটার টেমপ্লেট ব্যবহার করা সম্পূর্ণ নিষিদ্ধ। প্রতিটি আর্টিকেলে একই রকম নীল বর্ডার, একই বাঁধা-ধরা 'সারসংক্ষেপ (Quick Overview)' বা জোর করে সূচিপত্র/তুলনামূলক টেবিল ঢুকানো যাবে না। বিষয়বস্তু ও উদ্দেশ্য অনুযায়ী ৫টি মানবিক আর্কিটাইপ (সাহিত্যিক প্রবন্ধ, বিশ্ববিদ্যালয় লেকচার হ্যান্ডনোট, স্টেপ-বাই-স্টেপ রুটিন/নোটিশ, স্কুল স্টাডি গাইড, এবং বিসিএস বুলেট শিট) অনুযায়ী ভিন্ন ভিন্ন ডিজাইন ও বাক্যের মানবিক ছন্দ (Sentence Burstiness) ব্যবহার করতে হবে।
8. **English Content Bilingual Thumbnail & High-Rank Keyword Rule (দ্বিভাষিক থাম্বনেইল, গুগল হাই-র‌্যাংক কি-ওয়ার্ড ও মানবিক ইন্টিগ্রেশন নীতি):**
   - **থাম্বনেইল দ্বিভাষিক স্ট্যান্ডার্ড:** পোস্ট যদি ইংরেজিতে হয় (যেমন: English 1st/2nd Paper, Grammar বা Suggestion), তবে থাম্বনেইলে **বাংলা ও ইংরেজি উভয় ভাষাই উপস্থিত থাকতে হবে** (প্রধান ইংরেজি কি-ওয়ার্ড/টাইটেল বড় হরফে এবং সাথে সাবটাইটেল/হুকে সুস্পষ্ট বাংলা টেক্সট যাতে শিক্ষার্থীদের ক্লিক-থ্রু রেট বৃদ্ধি পায়)। বাংলা পোস্ট হলে থাম্বনেইল মূলত মার্জিত বাংলায় থাকবে। **Universal English Footer Tagline:** সব থাম্বনেইলে ডানপাশের ফ্রস্টেড পিল সর্বদা ১০০% ইংরেজিতে থাকবে: `Learn Smart • Lead Future • Latest Edition 2026`।
   - **ইংরেজি কনটেন্টের কি-ওয়ার্ড ও জিরো-ট্রান্সলিটারেশন নীতি:** ইংরেজি ব্যাকরণ ও বিষয়ের টেকনিক্যাল টার্মগুলোকে বাংলায় বিকৃত বা উচ্চারণ করে লেখা (যেমন: 'চেঞ্জিং সেন্টেন্সেস', 'ট্যাগ কোশ্চেন', 'সাফিক্স-প্রিফিক্স', 'ভয়েস চেঞ্জ', 'প্রিপজিশন', 'কানেক্টরস') সম্পূর্ণ নিষিদ্ধ। এগুলো সর্বদা প্রমিত **ইংরেজি বর্ণমালায়** লিখতে হবে (`Changing Sentences`, `Tag Questions`, `Suffix and Prefix`, `Appropriate Prepositions`, `Sentence Connectors`) এবং বাংলা বাক্যের সাথে স্বাভাবিক সংযোগে (`Changing Sentences-এর গোল্ডেন রুলস`, `Tag Questions-এ ভালো করার ট্রিকস`) ব্যবহার করতে হবে।
   - **টাইটেল ও প্যারাগ্রাফের অটো-ম্যাচিং (Semantic Matching):** গুগলে শীর্ষে থাকা হাই-ভলিউম সার্চ কোয়েরিগুলো টাইটেল, পারমালিঙ্ক, প্রথম ১০০ শব্দের ওভারভিউ বক্স, H2 হেডিং ও প্যারাগ্রাফে প্রাকৃতিকভাবে সন্নিবেশিত করতে হবে যাতে টাইটেল ও কনটেন্টের মধ্যে স্বয়ংক্রিয় সেমান্টিক সাদৃশ্য তৈরি হয়।
   - **বাংলা কনটেন্টের ক্ষেত্রে মানবিক সুর (Natural Human Tone):** বাংলা পোস্টের ক্ষেত্রে গুগল সার্চে শীর্ষে থাকা কি-ওয়ার্ডগুলোকে বাক্যের স্বাভাবিক মানবিক সুর (Human Tone & Sentence Burstiness)-এর সাথে মেলাতে হবে; কোনো জোরপূর্বক বা রোবটিক কি-ওয়ার্ড স্টাফিং সম্পূর্ণ নিষিদ্ধ।
9. **In-Body Visuals & Anti-AI Image Policy (বড় পোস্টের বডি ইমেজ ও কপিরাইট-মুক্ত ভিজ্যুয়াল স্ট্যান্ডার্ড):**
   - **কখন ইমেজ যোগ করতে হবে:** পোস্ট যদি দীর্ঘ বা বড় হয় (১,০০০–১,৫০০+ শব্দ), তবে বিষয়বস্তুকে প্রাঞ্জল করতে ও পাঠকের মনোযোগ ধরে রাখতে আর্টিকেলের ভেতরে প্রাসঙ্গিক ১–২টি সহযোগী ইমেজ/ইনফোগ্রাফিক যুক্ত করতে হবে।
   - **১০০% কপিরাইট মুক্ত (Zero Copyright Risk):** কোনো কপিরাইটযুক্ত সাইট বা অন্য কারও কনটেন্ট থেকে সরাসরি ছবি নেওয়া সম্পূর্ণ নিষিদ্ধ। পাবলিক ডোমেইন (উইকিমিডিয়া কমন্স), রয়্যালটি-ফ্রি লাইসেন্স বা নিজস্ব জেনারেটেড ভিজ্যুয়াল ব্যবহার করতে হবে।
   - **Anti-AI Aesthetic (এআই বোঝার উপায় থাকবে না):** এআই-এর চেনা ত্রুটি (মোমের মতো প্লাস্টিক ত্বক, অতিরিক্ত চকচকে গ্লো, বিকৃত অঙ্গপ্রত্যঙ্গ, বা ব্যাকগ্রাউন্ডে দুর্বোধ্য হিজিবিজি হরফ) সম্পূর্ণ বর্জন করতে হবে। ব্যবহার করতে হবে:
     * *রিয়েলিস্টিক ডকুমেন্টারি ফটোগ্রাফি:* ন্যাচারাল লাইটিং, বাস্তবসম্মত টেক্সচার ও ফটোসাংবাদিকতা স্টাইল।
     * *ক্লিন মিনিমালিস্ট ডায়াগ্রাম/ইনফোগ্রাফিক:* পাঠ্যপুস্তক-মানের পরিষ্কার কনসেপ্ট ডায়াগ্রাম বা ফ্ল্যাট ভেক্টর চার্ট (কোনো দুর্বোধ্য লেখা ছাড়া)।
     * *ঐতিহাসিক প্রামাণ্য ছবি:* পাবলিক ডোমেইনের আসল ঐতিহাসিক আলোকচিত্র (যেমন: হাসন রাজা, বিদ্যাসাগর, মুক্তিযুদ্ধ)।
   - **পারফেক্ট এসইও ও এইচটিএমএল স্ট্রাকচার (Semantic Markup):**
     * প্রতিটি ইন-বডি ইমেজ `<figure>` এবং `<figcaption>` দিয়ে এনক্যাপসুলেট করা হবে।
     * বাধ্যতামূলকভাবে বিষয়ভিত্তিক কি-ওয়ার্ড সমৃদ্ধ `alt` এবং `title` ট্যাগ থাকবে (গুগল ইমেজ এসইও-এর জন্য)।
     * পেজ স্পিড ও কোর ওয়েব ভাইটালস (Core Web Vitals) অক্ষুণ্ণ রাখতে `loading="lazy"`, রেসপনসিভ `max-width: 100%`, সুন্দর বর্ডার রেডিয়াস ও শ্যাডো প্রয়োগ করতে হবে।
10. **Tutorial & Practical How-To Architecture (টিউটোরিয়াল আর্কিটেকচার ও স্টেপ-বাই-স্টেপ ইন্টারফেস মার্কিং স্ট্যান্ডার্ড):**
    - **উদ্দেশ্য ও দর্শন:** টিউটোরিয়াল বা নির্দেশনামূলক পোস্টের (যেমন: সার্টিফিকেট সংশোধন, অনলাইন আবেদন, সফটওয়্যার বা মোবাইল সেটিংস) মূল লক্ষ্য হলো পাঠক যেন কোনো বিভ্রান্তি ছাড়াই কাজ সম্পন্ন করতে পারে। শুধু মুখের কথা বা টেক্সট লিখে ছেড়ে দেওয়া যাবে না।
    - **স্টেপ-বাই-স্টেপ স্ট্রাকচার (Step Cards):** প্রতিটি ধাপ আলাদা কার্ড আকারে থাকবে (`ধাপ ০১: পোর্টালে প্রবেশ`, `ধাপ ০২: ফরম পূরণ`, `ধাপ ০৩: ফি পরিশোধ` ইত্যাদি)।
    - **অরিজিনাল ইন্টারফেস ও ভিজ্যুয়াল মার্কিং (Annotated UI Screenshots):**
      * সংশ্লিষ্ট ওয়েবসাইট বা সফটওয়্যারের আসল ইন্টারফেসের পরিষ্কার স্ক্রিনশট দিতে হবে।
      * ব্যবহারকারীকে **ঠিক কোন বাটনে বা অপশনে ক্লিক করতে হবে**, তা লাল রঙের হাইলাইট বক্স (`Red Highlight Box`), উজ্জ্বল নির্দেশক তীর (`Arrow`) অথবা নম্বরযুক্ত সার্কেল পিন (`❶`, `❷`) দিয়ে সুস্পষ্টভাবে মার্ক করে দিতে হবে।
      * কোনো বিভ্রান্তিকর বা অস্পষ্ট ছবি ব্যবহার করা যাবে না।
    - **সতর্কবার্তা ও প্রো-টিপস (Callouts):** প্রতিটি স্টেপের নিচে সাধারণ ভুল এড়াতে `⚠️ সতর্কতা` বা `💡 টিপস` বক্স যুক্ত থাকবে।
11. **Strict Google-Standard Custom Permalink Governance (ডিফল্ট বা জেনেরিক পারমালিঙ্ক সম্পূর্ণ নিষিদ্ধ):**
    - ব্লগারে কোনো নতুন পোস্ট সরাসরি বাংলা টাইটেল দিয়ে ইনিশিয়াল পাবলিশ করা সম্পূর্ণ নিষিদ্ধ। বাংলা টাইটেল দিলে ব্লগার স্বয়ংক্রিয়ভাবে `2026/09/blog-post.html` বা `blog-post_15.html` এর মতো অর্থহীন জেনেরিক পারমালিঙ্ক তৈরি করে, যা এসইও ও গুগল এডসেন্সের ক্ষেত্রে মারাত্মক নেতিবাচক প্রভাব ফেলে।
    - **২-ধাপ পারমালিঙ্ক পদ্ধতি (The 2-Step Minting Protocol):**
      * *ধাপ ০১ (পারমালিঙ্ক মিন্ট):* পোস্ট তৈরির সময় টাইটেলে ইংরেজি বা বাংলিশ কি-ওয়ার্ড সমৃদ্ধ স্লাগ (যেমন: `computer-virus-cyber-security-guide-2026` অথবা `bcs-preliminary-marks-distribution`) বসিয়ে ড্রাফট থেকে পাবলিশ করতে হবে, যাতে ব্লগার স্থায়ীভাবে গুগল-স্ট্যান্ডার্ড ইংরেজি পারমালিঙ্ক তৈরি করে।
      * *ধাপ ০২ (বাংলা টাইটেল প্রতিস্থাপন):* পারমালিঙ্ক তৈরি হওয়ামাত্র পোস্টের টাইটেলটি আপডেট করে পূর্ণাঙ্গ মূল বাংলা টাইটেল বসিয়ে দিতে হবে। এর ফলে পারমালিঙ্ক ইংরেজি এসইও-বান্ধব থাকবে এবং পোস্টের শিরোনাম সুন্দর বাংলায় প্রদর্শিত হবে।
12. **Zero-Emoji Policy (১০০% ইমোজি বর্জন):** পোস্টের টাইটেল, সাবটাইটেল, হেডিং (H2, H3), সূচিপত্র (TOC), কলআউট বক্স বা বডির কোথাও কোনো ধরণের ইমোজি (`📌`, `👉`, `📢`, `⏱️`, `✅`, `🎓`, `📘`, `💬`, `💡`, `⚠️` ইত্যাদি) ব্যবহার সম্পূর্ণ নিষিদ্ধ। টাইপোগ্রাফি হবে শতভাগ মার্জিত, পাঠ্যপুস্তক ও জাতীয় দৈনিকের মতো মানসম্মত।
13. **Theme Native Share Exclusivity (কাস্টম শেয়ার বক্স সম্পূর্ণ নিষিদ্ধ):** ব্লগারে প্রতিটি পোস্টের নিচে থিমের নিজস্ব সোশ্যাল শেয়ার বাটন (Facebook, Twitter, WhatsApp) বিল্ট-ইনভাবে প্রদর্শিত হয়। পোস্টের কনটেন্টের ভেতর অতিরিক্ত কাস্টম শেয়ার বক্স (`📢 আপনার সহপাঠী ও বন্ধুদের সাথে শেয়ার করুন:`) ঢোকানো সম্পূর্ণ নিষিদ্ধ।
14. **Live Bengali Reporting & 100% Bengali Artifacts (লাইভ বাংলা রিপোর্টিং ও শতভাগ বাংলা প্ল্যান/ওয়াকথ্রু):** কাজ চলাকালীন এজেন্ট কখন কী করছে, কোন ফাইল বা স্ক্রিপ্ট নিয়ে কাজ করছে—তা চ্যাটে লাইভ বাংলায় লিখে ইউজারকে জানাবে। টুলস কলের নাম ও বিবরণ (`toolAction` ও `toolSummary`) বাংলায় নির্ধারণ করতে হবে। এছাড়া সমস্ত `implementation_plan.md` ও `walkthrough.md` সহ যাবতীয় অডিট রিপোর্ট ও প্ল্যান শতভাগ প্রাঞ্জল বাংলায় প্রণয়ন করা বাধ্যতামূলক (কোনো ইংরেজি প্ল্যান বা ওয়াকথ্রু লেখা যাবে না)।
15. **Mandatory Pre-Edit Full Post Backup & Label Protection (সম্পাদনার পূর্বে বাধ্যতামূলক পূর্ণাঙ্গ ব্যাকআপ ও লেবেল সংরক্ষণ):** ব্লগারে বিদ্যমান বা পুরনো কোনো পোস্ট সম্পাদনা (Edit) বা আপডেট (Update) করার পূর্বে বাধ্যতামূলকভাবে সেই পোস্টের আসল এইচটিএমএল কোড, ইমেজ লিঙ্ক, ক্যাটাগরি লেবেল এবং মেটাডাটা `backups/posts/<slug>/<timestamp>/` ফোল্ডারে ব্যাকআপ রাখতে হবে। পোস্টের পূর্বের লেবেল কোনো অবস্থাতেই হারিয়ে যাওয়া বা মুছে ফেলা যাবে না।
16. **Zero Over-Engineered Styling & Simplicity Mandate (অতিরঞ্জিত কোড বর্জন — সিম্পলিসিটি ও মার্জিত ভেক্টর আইকন):** পোস্ট বা থিমের জন্য কোনো ধরণের অতিরঞ্জিত (Over-the-top / Garish), অতিরিক্ত রঙিন, ভারী শ্যাডো বা জটিল সিএসএস কোড লেখা সম্পূর্ণ নিষিদ্ধ যা থিমের নিজস্ব রেসপনসিভ লেআউটকে নষ্ট করে। শিশুদের মতো চটুল ইমোজির বদলে প্রয়োজনে অত্যন্ত পরিমিতভাবে প্রফেশনাল ভেক্টর আইকন (SVG/FontAwesome) ব্যবহার করতে হবে এবং পোস্টের উপস্থাপন সবসময় সহজ, পরিষ্কার ও পাঠযোগ্য (Simple & Minimalist) রাখতে হবে।
17. **Topic Silo Internal Linking Governance (টপিকাল সাইলো ইন্টারনাল লিঙ্কিং ও অমিল পোস্ট বর্জন নীতিমালা):** কোনো বিষয়ের বা সিলেবাসের খুব কাছাকাছি প্রাসঙ্গিক লাইভ পোস্ট থাকলেই কেবল সেখানে ইন-টেক্সট কনটেক্সচুয়াল ও সিলেবাস সিরিজ সাইলো ইন্টারনাল লিঙ্কিং কার্যকর হবে। কিন্তু যদি কাছাকাছি বা প্রাসঙ্গিক কোনো পোস্ট না থাকে, তবে কোনো অবস্থাতেই অমিল, ভিন্ন ক্যাটাগরি বা অপ্রাসঙ্গিক পোস্টের লিংক জোর করে ঢুকানো সম্পূর্ণ নিষিদ্ধ; সেক্ষেত্রে সিস্টেম স্বয়ংক্রিয়ভাবে লিঙ্কিং **সম্পূর্ণ স্কিপ (Skip)** করবে।
18. **Anti-Cannibalization & Duplicate Content Guard (ডুপ্লিকেট টপিক ও ক্যানিব্যালাইজেশন প্রতিরোধ নীতিমালা):** ইউজার কোনো পিডিএফ (PDF) বা প্রশ্নের তালিকা দিলে, নতুন পোস্ট তৈরির পূর্বে সাইটের সমস্ত লাইভ পোস্টের (`all_live_posts_catalog.json`) সাথে প্রস্তাবিত বিষয়ের মিল স্ক্যান করতে হবে (`python tools/governance/topic_cannibalization_guard.py`)। কোনো বিষয়ের ওপর ইতিমধ্যে সাইটে বিস্তারিত পোস্ট থাকলে ইউজারকে লাইভ পোস্টের টাইটেল ও ইউআরএল সহ সাথে সাথে জানাতে হবে এবং সেই টপিকটি নতুন করে পোস্ট করা থেকে **সম্পূর্ণ বিরত (Skip)** থাকতে হবে। শুধুমাত্র সাইটে অনুপস্থিত নতুন ও অনুত্তরিত বিষয়গুলো নিয়েই নতুন পোস্ট রচনা করা যাবে।
19. **Mandatory CDN Cache-Busting & Purge Protocol (ক্যাশ ইনভ্যালিডেশন ও গ্লোবাল পার্জ প্রটোকল):** ব্লগারে বা গিটহাবে কোনো ইমেজ আপডেট বা প্রতিস্থাপন করলে কোনো অবস্থাতেই পুরনো একই অপরিবর্তিত ইউআরএল রাখা যাবে না। ইউআরএলে অবশ্যই ভার্সনিং প্যারামিটার বা নতুন ফাইলনেম দিতে হবে (যেমন: `banner.webp?v=20260916` বা `banner-v2.webp`)। একইসাথে ইমেজ আপডেট সম্পন্ন হওয়ামাত্র যেকোনো এজেন্টকে বাধ্যতামূলকভাবে সিডিএন পার্জ টুল এক্সিকিউট করতে হবে: `python tools/governance/cache_manager.py <ছবির_নাম.webp>` যাতে ক্লাউডফ্লেয়ার ও ফাস্টলি এজ ক্যাশ থেকে তৎক্ষণাৎ পুরনো ক্যাশ ফ্ল্যাশ হয়ে নতুন ইমেজ লাইভ হয়ে যায়।
20. **Mandatory Post-Publish/Edit Search Description Delivery (১৫০ অক্ষরের মধ্যে পারফেক্ট এসইও সার্চ ডেসক্রিপশন ডেলিভারি):** প্রতিটি নতুন পোস্ট পাবলিশ বা বিদ্যমান পোস্ট সম্পাদনা/আপডেট করার পর যেকোনো এজেন্টকে অবশ্যই চ্যাট রেসপন্স এবং ওয়াকথ্রুতে পোস্টের চূড়ান্ত বাংলা টাইটেল এবং ব্লগারের 'Search Description' বক্সের জন্য নিখুঁত কি-ওয়ার্ড সমৃদ্ধ ১৩০–১৪৮ অক্ষরের (বাধ্যতামূলকভাবে ১০০% ১৫০ অক্ষরের মধ্যে) কপি-রেডি সার্চ ডেসক্রিপশন প্রদান করতে হবে। যেহেতু ব্লগার এপিআই v3 দিয়ে এই ফিল্ডটি স্বয়ংক্রিয়ভাবে আপডেট করা যায় না, তাই ইউজার যেন এক ক্লিকে কপি করে ব্লগারের ড্যাশবোর্ডের ডানপাশের 'Search Description' বক্সে পেস্ট করে পোস্ট আপডেট করতে পারেন, তার জন্য এটি প্রতিটি এজেন্টের জন্য কঠোর ও অলঙ্ঘনীয় বাধ্যবাধকতা।
21. **Mandatory Real-Time Google WebSub (PubSubHubbub) Hub Pinger (রিয়েল-টাইম গুগল ফিড পুশ প্রটোকল):** যেকোনো নতুন পোস্ট পাবলিশ কিংবা বিদ্যমান পোস্ট সম্পাদনা/আপডেট করার পর যেকোনো এজেন্টকে বাধ্যতামূলকভাবে গুগলের সেন্ট্রাল হাবে রিয়েল-টাইম ফিড নোটিফিকেশন পাঠাতে হবে: `python tools/indexer/pubsub_hub_pinger.py`। এটি গুগলের অফিশিয়াল হাবে (`pubsubhubbub.appspot.com`) এবং Superfeedr হাবে তাৎক্ষণিক `HTTP 204` সিগন্যাল পাঠিয়ে গুগলবটের রিয়েল-টাইম ফিড রিডারকে সেকেন্ডের মধ্যে সাইটে এনে তাৎক্ষণিক ক্রল ও ইনডেক্সিং শুরু করায়। কোনো এজেন্ট এই ধাপ বাদ দিতে পারবে না।
22. **Post-Level Responsive Styling Standard (পোস্টের নিজস্ব মার্জিত ও রেসপনসিভ সিএসএস আর্কিটেকচার):**
    - **স্বয়ংসম্পূর্ণ ইন-পোস্ট সিএসএস স্টাইল বৈধ:** ব্যবহারকারীর স্পষ্ট নির্দেশনায় প্রতিটি আর্টিকেলে নিজস্ব মার্জিত, নিখুঁত ও রেসপনসিভ `<style>` ব্লক ব্যবহার করা যাবে (রেফারেন্স: `secularism-vs-islamic-values-in.html`)।
    - **স্ট্যান্ডার্ড উপাদানসমূহ:**
      * *হেডিং (`.htbd-academic-heading`):* গাড় নেভি কালার (`#0c2340`), বামে ৫ পিক্সেল অ্যাকসেন্ট বর্ডার (`#d4af37` বা `#1e3a8a`), প্যাডিং-লেফট ১৪px, মার্জিন ও বোল্ড ফন্ট।
      * *সাব-হেডিং (`.htbd-academic-subheading`):* রয়াল ব্লু (`#1e3a8a`), ২০px ফন্ট, ফন্ট-ওয়েট ৬০০।
      * *সারসংক্ষেপ বক্স (`.htbd-overview-box`):* সফট ব্যাকগ্রাউন্ড (`#f8fafd`), সূক্ষ্ম বর্ডার (`#dbeafe`), বামে ৫px নেভি বর্ডার (`#0c2340`), রাউন্ডেড কর্নার ও শ্যাডো।
      * *সূচিপত্র বক্স (`.htbd-toc-card`):* পরিচ্ছন্ন ব্যাকগ্রাউন্ড (`#f8fafc`), বর্ডার ও সুবিন্যস্ত লিংক।
      * *তুলনামূলক ও তথ্য সারণী (`.htbd-academic-table`):* নেভি হেডার (`#0c2340`), সাদা টেক্সট, অল্টারনেটিং রো (`#f8fafc`), সূক্ষ্ম বর্ডার (`#e2e8f0`) এবং মোবাইল স্ক্রোল র‍্যাপার।
      * *পরামর্শ/সতর্কতা বক্স (`.htbd-exam-card` / `.htbd-tip-card`):* শান্ত ব্যাকগ্রাউন্ড (যেমন হালকা সবুজ `#f0fdf4` বা হালকা অ্যাম্বার `#fefce8`), সূক্ষ্ম বর্ডার এবং ১০০% স্পষ্ট পঠনযোগ্য ডার্ক টেক্সট (কোনো ডার্ক-অন-ডার্ক রঙের ত্রুটি ছাড়া)।
      * *ডাউনলোড কার্ড ও সিরিজ বক্স:* মার্জিত বাটন ও সাইলো লিংক বক্স।
23. **Inquisitive Discovery Gate & Rapid Execution (অস্পষ্টতায় অনুমান সম্পূর্ণ নিষিদ্ধ — প্রশ্ন করে স্পষ্টতা অর্জন ও বিদ্যুৎগতির ডেলিভারি):**
    - ইউজার ব্যস্ততার কারণে অনেক সময় সংক্ষিপ্ত বা অসম্পূর্ণ প্রম্পট দেবেন।
    - কোনো এজেন্ট কখনোই নিজের থেকে মনগড়া ধারণা বা শর্টকাট অনুমান নিয়ে কাজ শুরু করবে না।
    - ডিজাইন, ব্যাকগ্রাউন্ড টেমপ্লেট, লেবেল, কিংবা টার্গেট অডিয়েন্স নিয়ে ১% সন্দেহ থাকলেও ইউজারকে সুনির্দিষ্ট প্রশ্ন (Clarifying Questions) করে শতভাগ পরিষ্কার হতে হবে।
    - রিকোয়ারমেন্ট স্পষ্ট হওয়ামাত্র আর কোনো ট্রায়াল-অ্যান্ড-এরর বা সময় অপচয় না করে সরাসরি বিদ্যুৎগতিতে নির্ভুল রেজাল্ট ডেলিভারি দিতে হবে।
24. **Zero Sycophancy & Fact-Grounded Defense (ইউজারের ভুল থাকলে হাঁ-তে হাঁ মেলানো সম্পূর্ণ নিষিদ্ধ — বাস্তব তথ্য ও ফ্যাক্ট দিয়ে পথ দেখানো):**
    - চাটুকার চ্যাটবটের মতো ইউজারের যেকোনো কথায় অন্ধের মতো "হাঁ তে হাঁ" মেলানো সম্পূর্ণ নিষিদ্ধ।
    - ইউজার মানুষ, তাই অনিচ্ছাকৃতভাবে এমন নির্দেশ দিতে পারেন যা এসইও, কোর ওয়েব ভাইটালস বা গুগল অ্যাডসেন্স পলিসির ক্ষতি করতে পারে।
    - এজেন্টের অলঙ্ঘনীয় দায়িত্ব হলো অন্ধের মতো সম্মতি না দিয়ে বাস্তব তথ্য (Facts), অ্যালগরিদম পলিসি ও টেকনিক্যাল বাস্তবতা তুলে ধরে ইউজারকে বিনয়ের সাথে চ্যালেঞ্জ করা, সঠিক বিকল্প পথ দেখানো এবং প্রশ্ন করে সঠিক সিদ্ধান্ত নেওয়া।
25. **Mandatory Bi-Modal (Light & Dark Mode) Styling Protocol (পোস্টের সিএসএস বাধ্যতামূলকভাবে লাইট ও ডার্ক উভয় মোডে শতভাগ নিখুঁত ও পাঠযোগ্য হওয়ার নিয়ম):**
    - ভবিষ্যতে ব্লগারে নতুন যে কোনো পোস্ট তৈরি বা পুরনো পোস্ট সম্পাদনার সময় পোস্টের ভেতরে যত সিএসএস (CSS) লেখা হবে, তা লাইট মোড (Light Mode) এবং ডার্ক মোড (Dark Mode) উভয় মোডেই যেন শতভাগ নিখুঁত, দৃষ্টিনন্দন ও পাঠযোগ্য থাকে। কোনো পোস্ট শুধুমাত্র লাইট মোডের কথা ভেবে ডিজাইন করা সম্পূর্ণ নিষিদ্ধ।
    - **হার্ডকোডেড ইনলাইন স্টাইল বর্জন:** ট্যাগে সরাসরি `style="background: #ffffff; color: #000;"` জাতীয় ইনলাইন স্টাইল হার্ডকোড করা নিষিদ্ধ, কারণ ডার্ক মোডে এটি অপরিবর্তিত থেকে কনট্রাস্ট নষ্ট করে।
    - **পোস্ট-লেভেল `<style>` ব্লকে ডার্ক মোড বাধ্যতামূলক:** আর্টিকেলের ভেতরে কোনো কাস্টম `<style>` ব্লক লিখলে একই সাথে লাইট মোডের ডিফল্ট স্টাইল এবং `.dark .custom-class` / `#mainContent.dark .custom-class` দিয়ে ডার্ক মোড অভিযোজন (ডার্ক স্লেট `#1e293b` ব্যাকগ্রাউন্ড, সাদা হেডিং `#ffffff`, হালকা পাঠযোগ্য বডি টেক্সট `#cbd5e1`, এবং স্কাই ব্লু লিংক `#38bdf8`) অন্তর্ভুক্ত করা বাধ্যতামূলক।
    - **প্রি-ফ্লাইট কোয়ালিটি গেটওয়ে:** প্রতিটি পোস্ট প্রকাশের পূর্বে `python tools/governance/pre_flight_checker.py` দ্বারা ডার্ক মোড ও লাইট মোড বাই-মোডাল সিএসএস কমপ্লায়েন্স যাচাই করা হবে। কোনো পোস্টে ডার্ক মোড রুল অনুপস্থিত থাকলে পাবলিকেশন স্বয়ংক্রিয়ভাবে ব্লক হয়ে যাবে।
26. **Exam & Model Test Question Architecture: Mandatory Section-Level Deep Linking & Solution Card Governance (মডেল টেস্ট ও প্রশ্নোত্তরের সেকশন ডিপ লিঙ্কিং প্রটোকল):**
    - পরীক্ষা, মডেল টেস্ট বা প্রশ্নপত্র ভিত্তিক পোস্ট তৈরির সময় প্রতিটি প্রশ্নের পাশে যদি সাইটের ইতিপূর্বে প্রকাশিত আর্টিকেলে কোনো উত্তর বিদ্যমান থাকে, তবে কেবল মূল পোস্টের সাধারণ লিঙ্ক নয়—বরং বাধ্যতামূলকভাবে সেই নির্দিষ্ট উত্তরের সেকশন অ্যাঙ্কর ডিপ লিঙ্ক (`https://www.helptrickbd.com/...post.html#specific-section-id`) প্রশ্নের পাশে যুক্ত করতে হবে, যাতে শিক্ষার্থী সরাসরি উত্তরে স্ক্রোল করে জাম্প করতে পারে।
    - সাইটে পূর্বে প্রকাশিত না থাকা প্রশ্নগুলোর পূর্ণাঙ্গ সমাধান ইন-পেজ সলিউশন কার্ডে (`.htbd-solution-card`) দিতে হবে।
    - যেকোনো এজেন্ট মডেল টেস্ট পোস্টের প্ল্যান (`implementation_plan.md`) সাজানোর সময় বাধ্যতামূলকভাবে প্রতিটি প্রশ্নের বিপরীতে সেকশন ডিপ লিঙ্ক ও ইন-পেজ উত্তরের ম্যাপিং ছক সংযুক্ত করবে। এই প্রটোকল অলঙ্ঘনীয়।

---

## 🚀 3. Milestones Completed So Far
1. **Batch 1 (10 Posts Revived):** Expanded from 100–300 words to 1,200–1,600 words each.
2. **Batch 2 (10 Posts Revived):** Expanded with Position 0 answers, comparison tables, and FAQ microdata.
3. **Batch 3 (10 Posts Revived + 1 Flagship Post):** Completed all 30 thin posts + 1 flagship post (`পুরুষতন্ত্র কাকে বলে?`).
4. **Blogger API v3 Direct Publishing:** All 31 posts updated directly live on Blogger without needing manual copy-pasting.
5. **Google Indexing API:** All 31 revived URLs submitted to Google Indexing API with `URL_UPDATED` status via [`tools/indexer/ping_all_revived.py`](file:///tools/indexer/ping_all_revived.py).

---

## 🛠️ 4. Project Tools & Execution Guide

### Dependency Installation:
```bash
pip install -r requirements.txt
```

### Key Python Automation Scripts:
- **Real-Time Google WebSub (PubSubHubbub) Hub Pinger:**
  ```bash
  python tools/indexer/pubsub_hub_pinger.py
  ```
- **Revive & Expand Post Content:**
  ```bash
  python tools/content_optimizer/post_reviver.py
  ```
- **Generate 16:9 Banners:**
  ```bash
  python tools/image_generator/banner_generator.py
  ```
- **Update Live Post on Blogger:**
  ```bash
  python tools/blogger_publisher/update_post.py --post_id <POST_ID> --html_file <PATH_TO_HTML>
  ```
- **Audit Live Site for AdSense Policy Violations:**
  ```bash
  python tools/policy_guard/scan_live_site.py
  ```
- **All-in-One Credentials & API Health Checker:**
  ```bash
  python tools/check_all_credentials.py
  ```
- **10-20 KB Ultra WebP Image Compressor (Core Web Vitals):**
  ```bash
  python tools/image_optimizer/webp_compressor.py -i <IMAGE_PATH>
  ```
- **Google People Also Ask (PAA) Long-Tail Query Scraper:**
  ```bash
  python tools/paa_miner/paa_scraper.py -k "<KEYWORD>" --lang bn
  ```
- **Google Search Console Striking Distance (Page 2 Keywords) Miner:**
  ```bash
  python tools/gsc_miner/striking_distance_miner.py
  ```
- **Outbound & Inbound Link-Rot / Dead Link Guardian:**
  ```bash
  python tools/link_guardian/link_checker.py
  ```
- **Competitor SERP Content Gap Analyzer:**
  ```bash
  python tools/serp_analyzer/content_gap_analyzer.py -k "<KEYWORD>"
  ```
- **AdSense High-RPM Keyword Matcher & Ad Placement Advisor:**
  ```bash
  python tools/adsense_suite/rpm_booster.py -f <HTML_FILE>
  ```
- **Generate Authentic Tutorial Screenshots:**
  ```bash
  python tools/image_generator/build_real_annotated_tutorials.py
  ```
- **Master Unified Publishing & SEO Pipeline (The Central Engine):**
  ```bash
  python tools/pipeline/master_publisher_pipeline.py --html <FILE> --post-id <ID> --url <LIVE_URL> --auto-compress --check-links --publish --index
  ```
- **Topic Cannibalization & Duplicate Guard (PDF/Topic Pre-Scan):**
  ```bash
  python tools/governance/topic_cannibalization_guard.py --topics "<TOPIC_1>" "<TOPIC_2>"
  # অথবা ফাইল/পিডিএফ মোড:
  python tools/governance/topic_cannibalization_guard.py --pdf <PATH_TO_PDF>
  ```
- **Keyword Cannibalization Auditor & Resolver:**
  ```bash
  python tools/cannibalization_detector/cannibalization_finder.py
  ```
- **Seasonal Trend & Traffic Forecaster:**
  ```bash
  python tools/trend_forecaster/trend_predictor.py
  ```
- **Silo Architecture & Internal Link Visualizer:**
  ```bash
  python tools/silo_architect/cluster_visualizer.py
  ```
- **10-20 KB Social Share Card & OpenGraph Generator:**
  ```bash
  python tools/social_card_generator/social_card_builder.py -t "<TITLE>" -c "<CATEGORY>"
  ```
- **Dwell Time & User Engagement Booster:**
  ```bash
  python tools/engagement_booster/dwell_optimizer.py -f <HTML_FILE>
  ```
- **Visual Asset & Core Web Vitals Image Safety Auditor:**
  ```bash
  python tools/vision_auditor/image_safety_auditor.py [--auto_fix]
  ```

---

## 🔒 5. Credentials Required (Not in Git)
The following 3 files must be placed locally in the project:
1. `service_account.json` ➡️ Root folder (Google Indexing API)
2. `tools/blogger_publisher/client_secrets.json` ➡️ OAuth Client ID
3. `tools/blogger_publisher/blogger_token.json` ➡️ Authenticated Blogger session

---

## 🧭 6. Agent Directives for Any New Session
1. Treat [`docs/CHAT_HISTORY.md`](file:///docs/CHAT_HISTORY.md) as the primary conversation history log.
2. Follow all guidelines in [`.agents/skills/seo-blogger-adsense/SKILL.md`](file:///.agents/skills/seo-blogger-adsense/SKILL.md).
3. Always verify changes with live site inspections or tests before claiming completion.
4. Auto-commit and push significant milestones to `origin main`.
5. **Strict Multi-PC Sync Protocol (বাসা ও অফিস পিসি নিরবচ্ছিন্ন সিঙ্ক নিয়ম):**
   - **প্রতিটি কাজের শুরুতে (Pre-task Check):** যেকোনো নতুন টাস্ক বা প্রম্পটের শুরুতে `git fetch origin` করে দেখতে হবে অন্য পিসি (বাসার পিসি বা অফিস ল্যাপটপ) থেকে কোনো নতুন কমিট এসেছে কিনা। নতুন আপডেট থাকলে তা `git pull --rebase origin main` দিয়ে সাথে সাথে লোকাল প্রজেক্টে যুক্ত করে নিতে হবে।
   - **প্রতিটি কাজের শেষে (Post-task Auto-Push):** যেকোনো কাজ সম্পন্ন হওয়ামাত্র সমস্ত নতুন কোড, রিপোর্ট, আর্টিকেল বা অ্যাসেট স্বয়ংক্রিয়ভাবে `git add`, `git commit` এবং `git push origin main` করে দিতে হবে, যাতে অন্য পিসিতে বসার সাথে সাথেই সব কাজ সম্পূর্ণ আপ-টু-ডেট পাওয়া যায়।
6. **Search Console Daily Improvement Trigger Protocol (সার্চ কনসোল দৈনিক ট্র্যাকিং নিয়ম):**
   - ইউজার চ্যাটে `"search console er ajker update ki"`, `"আজকের সার্চ কনসোল আপডেট কী"`, বা `"update ber koro"` বলা মাত্র কোনো কালক্ষেপণ না করে সাথে সাথে `python tools/analytics/track_gsc_improvements.py` স্ক্রিপ্ট রান করবে এবং ১৭ সেপ্টেম্বর ২০২৬ তারিখের বেসলাইনের সাথে তুলনা করে অগ্রগতি রিপোর্ট বাংলায় উপস্থাপন করবে।


