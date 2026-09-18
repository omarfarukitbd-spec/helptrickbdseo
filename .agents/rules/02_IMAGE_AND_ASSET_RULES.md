# 🖼️ 02_IMAGE_AND_ASSET_RULES.md — Visual Asset & CDN Standards
### Helptrickbd.com Image Quality, Core Web Vitals & CDN Governance

> [!IMPORTANT]
> **Core Web Vitals & Image SEO Rule**: Poorly formatted, uncompressed, or missing images destroy mobile page speed (LCP) and fail Google AdSense mobile compliance. Every image in this repository must be featherweight, high-resolution, and served via global CDN.

---

## 📐 1. Hero Banner Standards (হিরো থাম্বনেইল মানদণ্ড)
1. **Dimensions & Aspect Ratio**:
   - **Resolution**: Exactly `1200 x 675` pixels (Standard 16:9 widescreen ratio).
   - **File Size**: Target **10–20 KB** (Maximum 25 KB) in WebP format.
2. **Design Typography**:
   - High-contrast typography readable on mobile devices.
   - Bengali Font: `Hind Siliguri Bold` or `SolaimanLipi`.
   - English Font: `Inter Bold` or `Poppins Bold`.
   - Never mix languages on the banner (Bengali post = 100% Bengali text; English post = 100% English text).
3. **Mandatory 'Thumbnail BG/' Template Rule (নিজস্ব টেমপ্লেট ব্যাকগ্রাউন্ড বাধ্যতামূলক)**:
   - কোনো কৃত্রিম, প্লেইন বা জেনেরিক গ্র্যাডিয়েন্ট ব্যাকগ্রাউন্ড তৈরি করা সম্পূর্ণ নিষিদ্ধ।
   - প্রতিটি থাম্বনেইল অবশ্যই `Thumbnail BG/` ফোল্ডারের নির্দিষ্ট হাই-রেজোলিউশন টেমপ্লেট ব্যাকগ্রাউন্ডের ওপর ফ্রস্টেড গ্লাস কার্ড ও টাইপোগ্রাফি কম্পোজিট করে তৈরি করতে হবে:
     * `Thumbnail BG/bg.png` ➔ ইসলামিক আর্টিকেল (Islamic Article)
     * `Thumbnail BG/bg_1.png` ➔ স্কুল / ক্লাস ৬ / ফলব্যাক (Class 6 & General School Guides)
     * `Thumbnail BG/bg_2.png` ➔ রাষ্ট্রবিজ্ঞান ও অ্যাকাডেমিক (Political Science)
     * `Thumbnail BG/bg_3.png` ➔ শিক্ষা গাইড ও নোটিশ (Education Guide)
     * `Thumbnail BG/bg_4.png` ➔ চাকরির প্রস্তুতি ও পরীক্ষা (Job Study Article — Primary Viva, BCS)
     * `Thumbnail BG/bg_5.png` ➔ তথ্যপ্রযুক্তি ও কম্পিউটার (ICT Guide — Cloud Computing, Computer Virus)
4. **HarfBuzz Engine for Flawless Bengali Conjuncts (যুক্তাক্ষর বিকৃতি রোধ)**:
   - উইন্ডোজে বেসিক PIL/FreeType বাংলা যুক্তাক্ষর সঠিকভাবে শেপ করতে পারে না (যেমন: `ক্লাউড` হয়ে যায় `ক্-লাউড`)।
   - তাই ব্যানার তৈরির জন্য সবসময় `tools/image_generator/build_official_bg_thumbnails.py` (Chromium HarfBuzz ইঞ্জিন) ব্যবহার করতে হবে, যা ১০০% নির্ভুল বাংলা যুক্তাক্ষর ও প্রফেশনাল টাইপোগ্রাফি নিশ্চিত করে।
5. **English Content Bilingual Thumbnail & Keyword Rule (ইংরেজি কনটেন্টে বাংলা ও ইংরেজি দ্বিভাষিক থাম্বনেইল ও কি-ওয়ার্ড নীতি)**:
   - **থাম্বনেইল দ্বিভাষিক নীতি:** পোস্ট যদি ইংরেজিতে হয় (যেমন: English 1st Paper, English 2nd Paper, Grammar বা Suggestion), তবে থাম্বনেইলে **বাংলা ও ইংরেজি উভয় ভাষাই উপস্থিত থাকতে হবে**।
     * প্রধান ইংরেজি কি-ওয়ার্ড/টাইটেল (যেমন: "SSC 2027 English 1st Paper Suggestion") থাকবে বড় হরফে।
     * সাথে সাবটাইটেল বা হুকে সুস্পষ্ট বাংলা টেক্সট (যেমন: "সিন ও আনসিন প্যাসেজের চূড়ান্ত সমাধান") থাকবে, যাতে বাংলাদেশি শিক্ষার্থীরা এক নজরেই বুঝতে পারে এবং ক্লিক-থ্রু রেট (CTR) বৃদ্ধি পায়।
   - **পোস্টে ইংরেজি কি-ওয়ার্ডের বাধ্যতামূলক উপস্থিতি:** ইংরেজি পোস্টের বডিতে, মূল হেডিং (H1, H2), পারমালিঙ্ক স্লাগ, স্কিমা মাইক্রোডাটা এবং ইমেজ alt ট্যাগে অবশ্যই লক্ষ্যযুক্ত **ইংরেজি কি-ওয়ার্ড (English Keywords)** যথাযথভাবে বজায় রাখতে হবে যাতে গুগল সার্চ কনসোলে ইংরেজি কি-ওয়ার্ডে পোস্টটি শীর্ষ র‍্যাংক পায়।
   - পোস্ট যদি বাংলায় হয়, তবে থাম্বনেইল ও বডি মূলত মার্জিত বাংলায় থাকবে।
6. **Original Author Thumbnail Preservation (মৌলিক থাম্বনেইল অপরিবর্তনীয়)**:
   - If a post already possesses an authentic thumbnail designed by the site owner, the agent **MUST NOT replace or overwrite it**.
   - Only create new thumbnails for posts that completely lack a featured image or when explicitly requested by the user.
7. **Mandatory HTML Placement — Strictly BEFORE `<!--more-->` (ফিচার্ড ইমেজ অবস্থান ও জাম্প ব্রেক)**:
   - প্রতিটি আর্টিকেলের শুরুতে হিরো ব্যানার বা মূল ফিচার্ড ইমেজটি (`<img>`) অবশ্যই সবার উপরে বা ইন্ট্রোর প্রারম্ভে অবস্থান করবে।
   - ব্লগারে স্নsnippet ও ফেজ কাটার জন্য ব্যবহৃত `<!--more-->` ট্যাগটি **বাধ্যতামূলকভাবে হিরো ইমেজের পরে** বসাতে হবে।
   - কোনো অবস্থাতেই হিরো ইমেজের পূর্বে `<!--more-->` বসানো যাবে না। কারণ `<!--more-->` ইমেজের আগে বসলে ব্লগার আরএসএস/জেসন ফিডে (`c[l].content.$t`) ইমেজ অন্তর্ভুক্ত হয় না, যার ফলে হোমপেজ বা আর্টিকেলের নিচের রিলেটেড পোস্ট উইজেটে ("YOU MAY LIKE") ধূসর ক্যামেরা আইকন (`noThumb`) প্রদর্শন করে।
8. **Universal English Footer Tagline Mandate (থাম্বনেইলের নিচের ট্যাগলাইন সর্বদা ১০০% ইংরেজিতে রাখার অলঙ্ঘনীয় নিয়ম)**:
   - বাংলা পোস্ট হোক বা ইংরেজি পোস্ট হোক, সকল ক্যাটাগরি ও সকল ব্যাকগ্রাউন্ড টেমপ্লেটের (`bg.png`, `bg_1.png`, `bg_2.png`, `bg_3.png`, `bg_4.png`, `bg_5.png`) জন্য থাম্বনেইলের নিচের ডানপাশের ক্যাপসুল/পিলটিতে সর্বদা ১০০% ইংরেজিতে থাকবে:
     `Learn Smart • Lead Future • Latest Edition 2026`
   - কোনো অবস্থাতেই এটি বাংলায় ("সঠিক জ্ঞান • উজ্জ্বল ভবিষ্যৎ • সর্বশেষ সংস্করণ ২০২৬") রূপান্তর করা সম্পূর্ণ নিষিদ্ধ। এটি হেল্পট্রিকবিডির অফিশিয়াল গ্লোবাল ব্র্যান্ড সিগনেচার।

---

## 🌐 2. CDN Hosting & URL Protocol (jsDelivr সিডিএন বাধ্যতামূলক)
1. **Zero Local Path Leaks**:
   - Never reference local filesystem paths (`file:///...`, `D:/...`, or relative `assets/...`) inside post HTML meant for Blogger.
2. **jsDelivr CDN Standard**:
   - All newly generated images MUST be committed to Git under `assets/images/posts/` or `assets/images/tutorials/`.
   - Inside post HTML, reference them strictly through the official jsDelivr GitHub CDN pattern:
     ```html
     https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/<filename>.webp
     ```
   - Test that the CDN URL resolves to HTTP 200 after git push.

3. **Mandatory Cache Invalidation & Versioning Protocol (ক্যাশ ইনভ্যালিডেশন ও পার্জ প্রটোকল — STRICT MANDATE)**:
   - **সমস্যা প্রতিরোধ**: যখন কোনো বিদ্যমান পোস্টের থাম্বনেইল বা ইমেজ আপডেট/রিপ্লেস করা হয়, গুগল প্রক্সি (`blogger_img_proxy`), jsDelivr সিডিএন এবং ক্লায়েন্ট ব্রাউজার পুরনো ক্যাশ ইমেজ দেখাতে পারে।
   - **বাধ্যতামূলক ২টি নিয়ম (Any Agent MUST follow 100%)**:
     * **ক. ইউআরএল ভার্সনিং বা ক্যাশ-বাস্টিং**: বিদ্যমান কোনো পোস্টের ইমেজ আপডেট করলে পোস্টের এইচটিএমএলে অবশ্যই ইমেজের ইউআরএলে ভার্সন ট্যাগ যোগ করতে হবে (যেমন: `.../banner.webp?v=20260916` অথবা নতুন ফাইলনেম `.../banner-v2.webp`)। এর ফলে গুগল প্রক্সি ও ব্রাউজার তৎক্ষণাৎ নতুন ছবিটি ফেচ করতে বাধ্য হয়।
     * **খ. অটোমেটিক সিডিএন পার্জিং**: ইমেজ আপডেট বা জেনারেট করার পর এজেন্টকে অবশ্যই নিচের কমান্ডটি রান করতে হবে:
       ```bash
       python tools/governance/cache_manager.py <RELATIVE_PATH_OR_FILENAME>
       ```
       এটি jsDelivr-এর গ্লোবাল ক্লাউডফ্লেয়ার (CF) ও ফাস্টলি (FY) এজ ক্যাশ নিমেষেই বিশ্বব্যাপী পার্জ ও রিফ্রেশ করে দেয়।

---

## ⚙️ 3. WebP Compression & Core Web Vitals (মোবাইল LCP ও কম্প্রেশন স্ট্যান্ডার্ড)
1. **Compression Pipeline**:
   - Every PNG/JPG asset must be compressed using `tools/image_optimizer/webp_compressor.py`.
   - WebP quality setting: 75–82% with sharp YUV and smart subsampling to maintain crisp Bengali text while keeping file size under 20–25 KB.
2. **Hero Image vs In-Body Image Loading Architecture (Google web.dev LCP Standard)**:
   > [!IMPORTANT]
   > **Mobile LCP Golden Rule**: পেজের প্রথম ছবি বা হিরো থাম্বনেইলটিই হলো ব্রাউজারের Largest Contentful Paint (LCP) এলিমেন্ট। গুগলের অফিশিয়াল ডেভেলপার ডকুমেন্টেশন ([web.dev/optimize-lcp](https://web.dev/optimize-lcp/)) অনুযায়ী, হিরো ইমেজে ভুলেও `loading="lazy"` দেওয়া যাবে না।
   - **Hero Image (পোস্টের প্রথম ব্যানার/থাম্বনেইল):**
     * **বাধ্যতামূলক অ্যাট্রিবিউট:** `loading="eager" fetchpriority="high" decoding="async"`
     * **কঠোর নিষেধাজ্ঞা:** হিরো ইমেজে `loading="lazy"` সম্পূর্ণরূপে নিষিদ্ধ। এটি দিলে মোবাইলে ২.৫ সেকেন্ডের বেশি LCP বিলম্ব ঘটে এবং সার্চ কনসোলে এরর আসে।
     * **CLS প্রতিরোধ:** লেআউট শিফট রোধ করতে অবশ্যই সুনির্দিষ্ট ডাইমেনশন `width="1200" height="675"` এবং রেসপনসিভ সিএসএস ব্যবহার করতে হবে।
   - **In-Body Images (পোস্ট বডির ভেতরের বাকি সব ছবি):**
     * বডির সব ছবিতে বাধ্যতামূলকভাবে `loading="lazy" decoding="async"` থাকতে হবে যাতে ব্যান্ডউইথ সাশ্রয় হয় এবং ইনিশিয়াল পেজ স্পিড সুপারফাস্ট থাকে।
     * প্রতিটি ছবিতে প্রাসঙ্গিক বাংলা কি-ওয়ার্ড সমৃদ্ধ `alt` এবং `title` ট্যাগ বাধ্যতামূলক।

---

## 📸 4. In-Body Visuals & Anti-AI Aesthetic Policy
1. **When to Add In-Body Visuals**:
   - For long-form guides (1,200–1,600+ words), include 1–2 relevant illustrative figures or concept diagrams to enhance dwell time.
2. **Anti-AI Visual Standard (এআই বোঝার উপায় থাকবে না)**:
   - Strictly prohibit typical AI artifacts: waxy plastic skin, unnatural radiant glows, deformed hands/fingers, or nonsensical alien text in the background.
   - Prefer:
     * High-clarity real screenshot documentation.
     * Clean vector-style concept diagrams or flowcharts.
     * Authentic historical public domain photographs (e.g., Wikimedia Commons).
3. **Semantic HTML Figure Markup**:
   - Always encapsulate in-body images with `<figure>` and `<figcaption>`:
     ```html
     <figure style="margin: 28px 0; text-align: center;">
       <img src="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/tutorials/example.webp" 
            alt="বিষয়ভিত্তিক কি-ওয়ার্ড সমৃদ্ধ পূর্ণাঙ্গ বর্ণনা" 
            title="বিষয়ভিত্তিক কি-ওয়ার্ড সমৃদ্ধ টাইটেল" 
            loading="lazy" 
            style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 14px rgba(0,0,0,0.08);" />
       <figcaption style="font-size: 13px; color: #64748b; margin-top: 8px;">চিত্র: বিষয়বস্তুর সংক্ষিপ্ত ব্যাখ্যা</figcaption>
     </figure>
     ```

---

## 🎯 5. Tutorial & Practical How-To Screenshots (ইউআই অ্যানোটেশন স্ট্যান্ডার্ড)
1. **Real Interface Capture**:
   - Use real browser captures of government portals, educational boards, or software settings.
2. **Annotated Guidance Elements**:
   - **Red Highlight Box**: Use `#E53E3E` 3px border around the specific input field, dropdown, or submit button the user must click.
   - **Directional Arrow**: Bright pointer indicating the exact action point.
   - **Step Pin**: Numbered circle (`❶`, `❷`, `❸`) indicating the exact sequence.
3. **Python PIL Font Standard on Windows**:
   - When annotating images using Python Pillow on Windows, NEVER use default bitmap fonts (causes `???` broken glyphs for Bengali).
   - Use `C:/Windows/Fonts/NirmalaUI.ttf` or `NirmalaB.ttf` to guarantee clean, native Bengali rendering.
