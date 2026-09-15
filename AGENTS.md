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

## 💎 2. Established Architectural Decisions & Standards

### A. Typography & Fonts:
- **Default Font:** `SolaimanLipi` (applied cleanly via CSS `@font-face` from Ekushey CDN / jsDelivr).
- **Reason:** Hind Siliguri had broken conjunct/glyph rendering issues (e.g., numeral ১ and specific Bengali ligatures had distorted spacing). SolaimanLipi renders standard Bengali newspaper-grade typography across all modern browsers and mobile viewports.
- **Theme Setup File:** [`templates/theme_customizer/solaiman_lipi_theme_setup.xml`](file:///templates/theme_customizer/solaiman_lipi_theme_setup.xml).

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
4. **Original Thumbnail Preservation & Auto-Banner Freeze:** লেখকের নিজস্ব থাম্বনেইল থাকলে তা কোনোভাবেই প্রতিস্থাপন করা যাবে না। অটোগেনারেটেড ব্যানারে হার্ডকোডেড লেখা (যেমন: 'অনার্স ও বিসিএস') থাকায় অটো-ব্যানার জেনারেশন বন্ধ রাখা হয়েছে। ইউজার পরবর্তীতে থাম্বনেইলের জন্য আলাদা গাইডলাইন ও ডিজাইন নির্ধারণ করে দেবেন।
5. **Mandatory `<!--more-->` Jump Break:** ব্লগারে পোস্টের প্রথম ২-৩ লাইন বা প্রথম প্যারাগ্রাফের ঠিক পরেই `<!--more-->` ট্যাগ বসাতে হবে।
6. **Label Governance (ইউজারের পূর্বানুমতি):** পোস্ট পাবলিশ বা আপডেটের আগে অবশ্যই ইউজারকে জিজ্ঞেস করতে হবে কোন লেবেলে যুক্ত হবে এবং কোনো নতুন লেবেল যোগ করা হবে কি না।

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
- **Submit URLs to Google Indexing API:**
  ```bash
  python tools/indexer/ping_all_revived.py
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
