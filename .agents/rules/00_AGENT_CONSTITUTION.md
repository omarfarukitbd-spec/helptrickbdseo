# 🏛️ 00_AGENT_CONSTITUTION.md — The Supreme Project Constitution
### Helptrickbd.com SEO & Multi-PC Autonomous Operations

> [!IMPORTANT]
> **LEGAL & BINDING PRECEDENCE**: This document defines the highest operational authority for any AI agent (Claude, Gemini, GPT, or custom models) working on the `helptrickbdseo` repository. No agent, regardless of its defaults or instructions, may bypass or violate the rules set forth here.

---

## 🧭 1. Hierarchy of Authority
When processing any task or prompt, the agent MUST resolve conflicts in the following strict order:
1. **Explicit User Instruction in Current Turn** (unless requesting actions prohibited by safety/credentials protection).
2. **This Agent Constitution (`.agents/rules/00_AGENT_CONSTITUTION.md`)**.
3. **Domain Rulebooks (`.agents/rules/01_*.md` to `08_*.md`)**.
4. **Project Skill (`.agents/skills/seo-blogger-adsense/SKILL.md`)**.
5. **Project Overview (`AGENTS.md`)**.
6. **Agent's Internal/Pre-trained Default Instincts** (Lowest Priority).

---

## 🛑 2. Strict User Permission Gates (মানবেতর অনুমোদন ব্যতীত যা করা সম্পূর্ণ নিষিদ্ধ)
The agent is strictly FORBIDDEN from performing any of the following actions without obtaining explicit, recorded permission from the user in the chat:

| # | Restricted Action (নিষিদ্ধ কর্ম) | Why It Is Restricted (কেন নিষিদ্ধ) | Required Procedure |
|---|----------------------------------|------------------------------------|---------------------|
| 1 | **Adding, Editing, or Deleting Blogger Labels / Categories** | Uncontrolled labels dilute AdSense category balance, creating thin categories that cause AdSense rejection. | Ask user which existing label to use; never invent a new label without user saying "Yes". |
| 2 | **Deleting Live Posts on Blogger** | Accidental deletion causes instant 404 dead links and destroys existing SEO ranking. | Present post ID and URL; wait for user's explicit confirmation. |
| 3 | **Modifying Live Permalinks (URLs)** | Changing live URLs breaks existing backlinks, Google index entries, and social shares. | Only allowed during the initial 2-step minting process of brand new drafts. |
| 4 | **Replacing Original Author Thumbnails** | The site owner values authentic, author-designed graphics. Overwriting them breaks brand identity. | If an original author thumbnail exists, it must remain untouched unless user explicitly requests replacement. |
| 5 | **Translating Article Content to Another Language** | English posts have international keyword value; Bengali posts target local searchers. Cross-translating destroys intent. | English stays 100% English; Bengali stays 100% Bengali. Zero exceptions. |
| 6 | **Final Live Publishing to Blogger** | Publishing untested, raw AI content directly to live production bypasses quality gatekeeping. | Agent must run `pre_flight_checker.py`, present preview/metadata to user, and confirm before calling live publish. |
| 7 | **Pulling Updates from Git (`git pull` / `git fetch`)** | Unprompted pulls cause unwanted merge conflicts, rebase locks, or unexpected local overwrites. | Only execute `git pull` when the user explicitly instructs in chat (e.g., "গিট থেকে পুল করো" / "pull koro"). |
| 8 | **Editing Existing Posts Without Pre-Backup** | Overwriting content without a snapshot prevents rollback if mistakes occur. | Agent MUST verify that a 100% snapshot (HTML, labels, images, metadata) is created in `backups/posts/` before any update. |

---

## ⚡ 3. Autonomous Permissions (যা এজেন্ট নিজের দায়িত্বে তাৎক্ষণিকভাবে করবে)
The agent is encouraged and expected to perform the following actions autonomously without interrupting the user:
- [x] Researching keywords, SERP gaps, Google PAA queries, and competitors.
- [x] Writing and saving post drafts locally into `output_posts/` with full semantic HTML, schema, and metadata.
- [x] Optimizing and converting images to 10–20 KB WebP format with jsDelivr CDN paths.
- [x] Creating annotated tutorial screenshots with red boxes, directional arrows, and step pins.
- [x] Running automated health audits (`pre_flight_checker.py`, `scan_live_site.py`, `link_checker.py`).
- [x] **Post-Task Auto-Push**: Pushing committed work to GitHub (`git push origin main`) immediately upon completing a task, file update, or milestone.

---

## 🎯 4. Non-Negotiable Core Truths (পরম মূলনীতি)
1. **Zero Thin Content**: Every revived or new post MUST exceed **1,200 to 1,600+ words** with rich depth, practical guidance, and zero fluffy repetition.
2. **Zero Cookie-Cutter Uniformity**: Never output cookie-cutter articles where every post looks identical with the same blue boxes and identical headings. Respect the 5 Human Archetypes (Academic Handnote, Job Bullet Sheet, Tutorial Step Card, Literary Essay, School Study Guide).
3. **Mandatory Jump Break Strictly AFTER Hero Image**: Every post published to Blogger MUST place the featured hero image (`<img>`) at the top, followed by the introductory text, and then `<!--more-->`. Never place `<!--more-->` before the hero image (which breaks RSS feed thumbnails and triggers gray camera placeholders).
4. **Mandatory 2-Step Custom Permalinks**: Every new post MUST be minted with an English slug before applying the Bengali title. Never allow `blog-post_xx.html`.
5. **jsDelivr CDN Hosting**: Never reference local filesystem image paths (`file:///` or relative paths) inside post HTML intended for Blogger. All images MUST reside in GitHub and resolve through jsDelivr CDN.
6. **Anti-Hallucination Grounding**: For Bangladesh board results, certificate corrections, BCS syllabus, and government portals, verify real procedures against official `.gov.bd` sources. Never fabricate fee amounts, gazette dates, or portal links.
7. **Zero-Emoji Policy (১০০% ইমোজি বর্জন)**: Emojis are strictly banned from post titles, headings, TOC, callout boxes, and body text. Content must maintain professional, newspaper-grade typography.
8. **Theme Native Share Exclusivity (কাস্টম শেয়ার বক্স নিষিদ্ধ)**: Injected custom social share boxes (`ht-social-share-box`) or manual WhatsApp/Facebook buttons inside post bodies are strictly prohibited. The Blogger theme provides built-in native share buttons.
9. **Mandatory 'Thumbnail BG/' Template & Bilingual Rule**: All newly created thumbnails MUST be composited ON TOP OF the user's authentic templates from `Thumbnail BG/` using the Chromium HarfBuzz engine (`build_official_bg_thumbnails.py`). Plain artificial gradients are strictly prohibited. **English Content Rule:** For English posts (English 1st/2nd Paper, Grammar, Suggestions), the thumbnail MUST contain BOTH English and Bengali (Primary English Title/Keyword + Clear Bengali Hook/Subtitle), and the post content must strictly preserve and feature the target English keywords for SEO ranking. For Bengali posts, thumbnails remain primarily in Bengali. **Universal English Footer Tagline:** For ALL posts (Bengali or English) and across all background templates, the bottom-right footer tagline pill MUST ALWAYS remain strictly in English: `Learn Smart • Lead Future • Latest Edition 2026`. Never translate this footer tagline into Bengali.
10. **Live Bengali Reporting & Artifact Language (লাইভ বাংলা রিপোর্টিং ও সকল প্ল্যান/ওয়াকথ্রু বাংলায় প্রণয়ন)**: কাজ করার সময় এজেন্ট ঠিক কী নিয়ে কাজ করছে, কেন করছে এবং তার ফলাফল কী—তা চ্যাটে লাইভ বাংলায় লিখে ইউজারকে জানাবে। প্রতিটি টুলস কলের `toolAction` ও `toolSummary` বাংলায় নির্ধারণ করতে হবে। এছাড়া সমস্ত `implementation_plan.md`, `walkthrough.md`, রোডম্যাপ ও অডিট রিপোর্ট **শতভাগ সাবলীল বাংলায়** প্রণয়ন করা বাধ্যতামূলক (কোনো ইংরেজি প্ল্যান বা ওয়াকথ্রু তৈরি সম্পূর্ণ নিষিদ্ধ)।
11. **Mandatory Pre-Edit Post Backup & Label Protection (সম্পাদনার পূর্বে বাধ্যতামূলক ব্যাকআপ ও লেবেল সংরক্ষণ)**: ব্লগারে কোনো পুরনো পোস্ট এডিট করার পূর্বে বাধ্যতামূলকভাবে তার সম্পূর্ণ এইচটিএমএল, মূল লেবেল ও মেটাডাটা ব্যাকআপ ফোল্ডারে সেভ করতে হবে।
12. **Zero Over-Engineered Styling & Simplicity Mandate (অতিরঞ্জিত কোড ও চড়া স্টাইল বর্জন — সিম্পলিসিটি ও মার্জিত ভেক্টর আইকন)**: কোনো অতিরঞ্জিত বা ভারী সিএসএস কোড লেখা যাবে না যা থিমের স্বাভাবিক রেসপনসিভ লেআউটকে ক্ষতিগ্রস্ত করে। ইমোজির বদলে প্রয়োজনে অত্যন্ত পরিমিতভাবে মার্জিত ভেক্টর আইকন (SVG/FontAwesome) ব্যবহার করতে হবে এবং পোস্টের উপস্থাপন সবসময় সহজ, পরিষ্কার ও পাঠযোগ্য (Simple & Minimalist) রাখতে হবে।
13. **Topic Silo Internal Linking Governance (টপিকাল সাইলো ইন্টারনাল লিঙ্কিং ও অমিল পোস্ট বর্জন নীতিমালা)**: কোনো বিষয়ের বা সিলেবাসের খুব কাছাকাছি প্রাসঙ্গিক লাইভ পোস্ট থাকলেই কেবল ইন-টেক্সট কনটেক্সচুয়াল ও সিলেবাস সিরিজ সাইলো লিঙ্কিং কার্যকর হবে। কোনো পোস্টের সাথে সামঞ্জস্যপূর্ণ বা কাছাকাছি বিষয়ের লাইভ পোস্ট না থাকলে কোনো অবস্থাতেই অমিল বা অপ্রাসঙ্গিক পোস্টের লিংক জোর করে ঢুকানো যাবে না; সেক্ষেত্রে সিস্টেম স্বয়ংক্রিয়ভাবে ইন্টারনাল লিঙ্কিং স্কিপ (Skip) করবে।
14. **Anti-Cannibalization & Duplicate Content Guard (ডুপ্লিকেট টপিক ও ক্যানিব্যালাইজেশন প্রতিরোধ গার্ড)**: পিডিএফ বা কোনো সোর্স থেকে নতুন পোস্ট তৈরির পূর্বে বাধ্যতামূলকভাবে সাইটের সমস্ত লাইভ পোস্টের সাথে প্রস্তাবিত বিষয়ের মিল পরীক্ষা করতে হবে (`topic_cannibalization_guard.py`)। কোনো বিষয়ের ওপর ইতিমধ্যে পূর্ণাঙ্গ পোস্ট থাকলে তৎক্ষণাৎ ইউজারকে ইনফর্ম করতে হবে এবং সেই টপিক সম্পূর্ণ স্কিপ (Skip) করে পিডিএফের অন্যান্য নতুন ও অনুত্তরিত টপিক নিয়ে পোস্ট তৈরি করতে হবে।
15. **Mandatory CDN Cache-Busting & Purge Protocol (ক্যাশ বাস্টিং ও সিডিএন পার্জ প্রটোকল)**: যখনই কোনো বিদ্যমান পোস্টের থাম্বনেইল বা ইমেজ আপডেট করা হবে, এজেন্টকে বাধ্যতামূলকভাবে ইউআরএলে ভার্সনিং প্যারামিটার (যেমন: `banner.webp?v=20260916` বা `banner-v2.webp`) প্রয়োগ করতে হবে এবং `python tools/governance/cache_manager.py <filename>` এক্সিকিউট করে jsDelivr-এর গ্লোবাল ক্লাউডফ্লেয়ার ক্যাশ পার্জ করতে হবে। এটি লঙ্ঘন করা সম্পূর্ণ নিষিদ্ধ।
16. **Mandatory Post-Publish/Edit Search Description Delivery (১৫০ অক্ষরের মধ্যে পারফেক্ট এসইও সার্চ ডেসক্রিপশন ডেলিভারি)**: প্রতিটি নতুন পোস্ট পাবলিশ বা বিদ্যমান পোস্ট সম্পাদনা/আপডেট করার পর যেকোনো এজেন্টকে অবশ্যই চ্যাট রেসপন্স এবং ওয়াকথ্রুতে পোস্টের চূড়ান্ত বাংলা টাইটেল এবং ব্লগারের 'Search Description' বক্সের জন্য নিখুঁত কি-ওয়ার্ড সমৃদ্ধ ১৩০–১৪৮ অক্ষরের (বাধ্যতামূলকভাবে ১০০% ১৫০ অক্ষরের মধ্যে) কপি-রেডি সার্চ ডেসক্রিপশন প্রদান করতে হবে। যেহেতু ব্লগার এপিআই v3 দিয়ে এই ফিল্ডটি স্বয়ংক্রিয়ভাবে আপডেট করা যায় না, তাই ইউজার যেন এক ক্লিকে কপি করে ব্লগারের ড্যাশবোর্ডের ডানপাশের 'Search Description' বক্সে পেস্ট করে পোস্ট আপডেট করতে পারেন, তার জন্য এটি প্রতিটি এজেন্টের জন্য কঠোর ও অলঙ্ঘনীয় বাধ্যবাধকতা।
17. **Mandatory Post-Publish Real-Time PubSubHubbub (WebSub) Push (রিয়েল-টাইম গুগল ফিড পুশ প্রটোকল)**: যেকোনো নতুন পোস্ট পাবলিশ কিংবা বিদ্যমান পোস্ট সম্পাদনা/আপডেট করার পর যেকোনো এজেন্টকে বাধ্যতামূলকভাবে গুগলের সেন্ট্রাল হাবে রিয়েল-টাইম ফিড নোটিফিকেশন পাঠাতে হবে (`python tools/indexer/pubsub_hub_pinger.py`)। এটি গুগলের অফিশিয়াল হাবে (`pubsubhubbub.appspot.com`) এবং Superfeedr হাবে তাৎক্ষণিক `HTTP 204` সিগন্যাল পাঠিয়ে গুগলবটের রিয়েল-টাইম ফিড রিডারকে সেকেন্ডের মধ্যে সাইটে এনে তাৎক্ষণিক ক্রল ও ইনডেক্সিং শুরু করায়।
18. **Post-Level Responsive Styling Standard (পোস্টের নিজস্ব মার্জিত ও রেসপনসিভ সিএসএস আর্কিটেকচার)**:
    - **স্বয়ংসম্পূর্ণ ইন-পোস্ট সিএসএস স্টাইল বৈধ ও স্ট্যান্ডার্ড:** ব্যবহারকারীর নির্দেশনায় প্রতিটি আর্টিকেলে নিখুঁত পাঠযোগ্যতা ও রেসপনসিভনেস নিশ্চিত করতে পোস্টের নিজস্ব মার্জিত `<style>` ব্লক ব্যবহার করা যাবে (রেফারেন্স: `secularism-vs-islamic-values-in.html`)।
    - **স্ট্যান্ডার্ড উপাদান ও ক্লাসসমূহ:**
      * *হেডিং (`.htbd-academic-heading`):* গাড় নেভি কালার (`#0c2340`), বামে ৫px অ্যাকসেন্ট বর্ডার (`#d4af37` বা `#1e3a8a`), প্যাডিং-লেফট ১৪px, মার্জিন ও বোল্ড ফন্ট।
      * *সাব-হেডিং (`.htbd-academic-subheading`):* রয়াল ব্লু (`#1e3a8a`), ২০px ফন্ট, ফন্ট-ওয়েট ৬০০।
      * *সারসংক্ষেপ অ্যান্সার বক্স (`.htbd-overview-box`):* সফট ব্যাকগ্রাউন্ড (`#f8fafd`), সূক্ষ্ম বর্ডার (`#dbeafe`), বামে ৫px নেভি বর্ডার (`#0c2340`), রাউন্ডেড কর্নার ও শ্যাডো।
      * *সূচিপত্র বক্স (`.htbd-toc-card`):* পরিচ্ছন্ন ব্যাকগ্রাউন্ড (`#f8fafc`), সূক্ষ্ম স্লেট বর্ডার ও সুবিন্যস্ত লিঙ্ক।
      * *তুলনামূলক ও তথ্য সারণী (`.htbd-academic-table`):* নেভি হেডার (`#0c2340`), সাদা টেক্সট, অল্টারনেটিং রো (`#f8fafc`), সূক্ষ্ম বর্ডার (`#e2e8f0`) এবং মোবাইল স্ক্রোল র‍্যাপার।
      * *পরামর্শ/সতর্কতা বক্স (`.htbd-exam-card` / `.htbd-tip-card`):* শান্ত ব্যাকগ্রাউন্ড (হালকা সবুজ `#f0fdf4` বা হালকা অ্যাম্বার `#fefce8`), সূক্ষ্ম বর্ডার এবং ১০০% স্পষ্ট পঠনযোগ্য ডার্ক টেক্সট (কোনো ডার্ক-অন-ডার্ক রঙের ত্রুটি ছাড়া)।
      * *ডাউনলোড বক্স ও সিরিজ বক্স:* মার্জিত ডাউনলোড বাটন ও সাইলো নেভিগেশন কার্ড।
19. **The Inquisitive Discovery & Rapid Execution Protocol (অস্পষ্টতায় অনুমান সম্পূর্ণ নিষিদ্ধ — প্রশ্ন করে স্পষ্টতা অর্জন ও বিদ্যুৎগতির বাস্তবায়ন)**:
    - ইউজার অনেক সময় ব্যস্ততার কারণে অত্যন্ত সংক্ষিপ্ত প্রম্পট প্রদান করেন।
    - কোনো এজেন্ট কখনোই নিজের থেকে মনগড়া ধারণা, অনুমান বা শর্টকাট নিয়ে কাজ শুরু করতে পারবে না।
    - ডিজাইন স্টাইল, টেমপ্লেট, লেবেল, বা উদ্দেশ্য নিয়ে সামান্যতম অস্পষ্টতা থাকলেও ইউজারকে প্রশ্ন (Clarifying Questions) করে বিষয়টি পুরোপুরি পরিষ্কার করে নিতে হবে।
    - একবার রিকোয়ারমেন্ট শতভাগ স্পষ্ট হয়ে গেলে কোনো দ্বিধা বা ট্রায়াল-অ্যান্ড-এরর ছাড়া সরাসরি বিদ্যুৎগতিতে নির্ভুল রেজাল্ট ডেলিভারি দিতে হবে।
20. **Zero Sycophancy & Fact-Grounded Challenge (ইউজারের ভুল থাকলে হাঁ-তে হাঁ মেলানো সম্পূর্ণ নিষিদ্ধ — বাস্তব তথ্য ও ফ্যাক্ট দিয়ে পথ দেখানো)**:
    - একজন চাটুকার চ্যাটবটের মতো ইউজারের সব কথায় "হাঁ তে হাঁ" মেলানো সম্পূর্ণ নিষিদ্ধ।
    - ইউজার মানুষ, তাই অনিচ্ছাকৃতভাবে এমন নির্দেশ দিতে পারেন যা এসইও, কোর ওয়েব ভাইটালস, বা গুগল অ্যাডসেন্স পলিসির জন্য ক্ষতিকর।
    - এজেন্টের অলঙ্ঘনীয় দায়িত্ব হলো অন্ধের মতো সম্মতি না দিয়ে বাস্তব তথ্য (Facts), অ্যালগরিদম পলিসি ও টেকনিক্যাল বাস্তবতা তুলে ধরে ইউজারকে বিনয়ের সাথে চ্যালেঞ্জ করা, সঠিক বিকল্প পথ দেখানো এবং প্রশ্ন করে সঠিক সিদ্ধান্ত নেওয়া।
21. **Exam & Model Test Question Architecture: Mandatory Section-Level Deep Linking & Solution Card Governance (মডেল টেস্ট ও প্রশ্নোত্তরের সেকশন ডিপ লিঙ্কিং প্রটোকল)**:
    - পরীক্ষা, মডেল টেস্ট বা প্রশ্নপত্র ভিত্তিক পোস্ট তৈরির সময় প্রতিটি প্রশ্নের পাশে যদি সাইটের ইতিপূর্বে প্রকাশিত আর্টিকেলে কোনো উত্তর বিদ্যমান থাকে, তবে কেবল মূল পোস্টের সাধারণ লিঙ্ক নয়—বরং বাধ্যতামূলকভাবে সেই নির্দিষ্ট উত্তরের সেকশন অ্যাঙ্কর ডিপ লিঙ্ক (`https://www.helptrickbd.com/...post.html#specific-section-id`) প্রশ্নের পাশে যুক্ত করতে হবে, যাতে শিক্ষার্থী সরাসরি উত্তরে স্ক্রোল করে জাম্প করতে পারে।
    - সাইটে পূর্বে প্রকাশিত না থাকা প্রশ্নগুলোর পূর্ণাঙ্গ সমাধান ইন-পেজ সলিউশন কার্ডে (`.htbd-solution-card`) দিতে হবে।
    - যেকোনো এজেন্ট মডেল টেস্ট পোস্টের প্ল্যান (`implementation_plan.md`) সাজানোর সময় বাধ্যতামূলকভাবে প্রতিটি প্রশ্নের বিপরীতে সেকশন ডিপ লিঙ্ক ও ইন-পেজ উত্তরের ম্যাপিং ছক সংযুক্ত করবে। এই প্রটোকল অলঙ্ঘনীয়।
22. **Mandatory Post-Completion Indexing, Multi-Engine Push & Proof Verification Gate (পোস্ট শেষের পর বাধ্যতামূলক ইনডেক্সিং, পুশ ও শতভাগ প্রমাণ যাচাই গেট)**:
    - প্রতিটি নতুন পোস্ট পাবলিশ কিংবা বিদ্যমান পোস্ট সম্পাদনা/আপডেট করার পর এজেন্টকে অবশ্যই:
      * (১) Schema.org রিচ স্নsnippet (`BlogPosting`, `FAQPage`, `BreadcrumbList`) মাইক্রোডাটা নিশ্চিত করতে হবে।
      * (২) লাইভ HTTP 200 ও ক্যানোনিকাল ম্যাচ টেস্ট করতে হবে।
      * (৩) Google Indexing API v3-তে সাবমিট করে 200 OK কনফার্ম করতে হবে।
      * (৪) Google WebSub হাবে ফিড পুশ (HTTP 204) সম্পন্ন করতে হবে।
      * (৫) IndexNow-তে সাবমিট (202 Accepted) করতে হবে।
    - এই ৫টি ধাপ লাইভ টেস্ট করে শতভাগ নিশ্চিত হওয়ার পূর্বে কোনো অবস্থাতেই ইউজারকে "কাজ শেষ" জানানো সম্পূর্ণ নিষিদ্ধ।
    - ইউজারের সামনে বাধ্যতামূলকভাবে লাইভ প্রুফ টেবিল ও ১৫০ অক্ষরের সার্চ ডেসক্রিপশন উপস্থাপন করতে হবে (`python tools/indexer/post_publish_verifier.py`)।

---

## 🔍 5. Pre-Task & Post-Task Rituals
Every agent session on any machine MUST adhere to this operational loop:
```mermaid
graph TD
    A[Start Session: Receive User Request] --> B[Perform Task adhering to 00-06 Rules (Pull ONLY when explicitly instructed by user)]
    B --> C[Run Automated Gatekeeper: python tools/governance/pre_flight_checker.py]
    C -->|Fails Checks| D[Self-Correct Issues]
    D --> C
    C -->|Passes 100%| E[If Live Publish: Seek Explicit User Approval]
    E --> F[Post-Task: git add -A, git commit, git push origin main]
    F --> G[Provide Live Bengali Summary & Complete Turn]
```
