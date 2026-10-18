# 10_PDF_INGESTION_AND_EXTRACTION_PROTOCOL.md
# HelpTrickBD SEO — PDF Ingestion, Rapid Extraction & Editorial Correction Rulebook

> **Scope:** Mandatory protocol for every AI Agent whenever a user provides, uploads, or references a PDF file in `input_pdfs/` or anywhere in the workspace.

---

## 1. The Fundamental Law (Zero Manual Slicing)
1. **STRICTLY FORBIDDEN:** An agent must **NEVER** manually extract PDF pages into dozens of individual image files (`.jpg`, `.png`) on disk, nor write slow sequential loops to OCR pages one-by-one.
2. **MANDATORY TOOL:** All PDF processing MUST be executed via the project's centralized conversion engine:
   ```powershell
   python tools/pdf_to_md/convert.py "<PATH_TO_PDF>"
   ```

---

## 2. Dual-Engine Ingestion Pipeline

```
[Input PDF File] 
       │
       ▼
tools/pdf_to_md/convert.py
       │
       ├─► [Born-Digital Vector PDF] ──► PyMuPDF4LLM Engine (1-2 Seconds) ──► Output: .md
       │
       └─► [Scanned / Photo PDF] ─────► In-Memory Fast Engine / Gemini ────► Output: .md
                                                                                  │
                                                                                  ▼
                                                            [Agent Editorial Proofreading Gate]
                                                            (Spelling, Bengali Conjuncts & Tables)
                                                                                  │
                                                                                  ▼
                                                            [HelpTrickBD Academic Archetype Post]
```

### Engine A: Born-Digital PDFs (Word / Vector / E-book)
* Executed via `pymupdf4llm`.
* Converts multi-page documents in milliseconds.
* Retains exact vector text, headings, bullet lists, and markdown tables (`| Col1 | Col2 |`).

### Engine B: Scanned Photocopy / Image PDFs
* Executed in-memory via `winocr` or `Gemini Flash Vision AI` (if `GEMINI_API_KEY` is present).
* Zero temporary disk files.
* Direct conversion into structured `.md` with page headers and layout preservation.

---

## 3. Mandatory Pre-Post PDF Analysis & Keyword Research Protocol (পিডিএফ বিশ্লেষণ, টপিক রিসার্চ ও কিওয়ার্ড ইন্টিগ্রেশন নীতি)

পিডিএফ থেকে কোনো পোস্ট তৈরির পূর্বে এজেন্টকে বাধ্যতামূলকভাবে নিচের ধারাবাহিক ধাপগুলো শতভাগ অনুসরণ করতে হবে:

### ক. ধাপ ০১: পিডিএফ কনটেন্ট বিশ্লেষণ (Comprehensive PDF Content Analysis)
* ড্রাফট শুরু করার আগে পিডিএফ-এর মূল বিষয়বস্তু, পাঠ্যক্রম, তথ্য, অধ্যায় ও প্রশ্নের ধরণ পুঙ্খানুপুঙ্খভাবে বিশ্লেষণ করতে হবে।

### খ. ধাপ ০২: নির্ধারিত টপিক নিয়ে এজেন্টের গবেষণা (Target Post Topic Research)
* পিডিএফ বিশ্লেষণের পর যে নির্দিষ্ট পোস্টটি তৈরি করা হবে, সেটির টপিক ও পাঠক চাহিদা (Student / User Search Intent) নিয়ে এজেন্টকে বিস্তারিত গবেষণা করতে হবে।

### গ. ধাপ ০৩: গুগলে শীর্ষ র‍্যাঙ্কিং কিওয়ার্ডের তালিকা প্রণয়ন (Top-Ranking Keyword Listing)
* **বাংলা পোস্টের জন্য (Bangla Content):**
  - সংশ্লিষ্ট পোস্ট সম্পর্কিত গুগলে সবচেয়ে বেশি র‍্যাঙ্ক করে এমন **বাংলা কিওয়ার্ড (Bangla Keywords)** এবং **ইংরেজি কিওয়ার্ড (English Keywords)** উভয় তালিকা প্রস্তুত করতে হবে।
* **ইংরেজি পোস্টের জন্য (English Content):**
  - শুধুমাত্র গুগলে শীর্ষ র‍্যাঙ্কিং থাকা **ইংরেজি কিওয়ার্ডসমূহ (English Keywords Only)** গবেষণা করে তালিকা প্রস্তুত করতে হবে (কোনো বাংলা কিওয়ার্ড আসবে না)।

### ঘ. ধাপ ০৪: Title, H2, H3, H4 ও Paragraph-এ ১০০% মানবিক সুরে কিওয়ার্ড সন্নিবেশ (Natural Human Tone & Seamless Placement)
* প্রস্তুতকৃত কিওয়ার্ডগুলোকে পোস্টের **Title (শিরোনাম), H2, H3, H4 হেডিং এবং প্রতিটি Paragraph (প্যারাগ্রাফ)-এর ভেতরে এমনভাবে বিন্যস্ত করতে হবে যেন প্রতিটি বাক্য অত্যন্ত প্রাসঙ্গিক (Contextually Relative) মনে হয়**।
* **শতভাগ মানবিক সুর (100% Natural Human Tone):**
  - কোনো প্রকার কৃত্রিম, রোবটিক বা জোরপূর্বক কিওয়ার্ড স্টাফিং সম্পূর্ণ নিষিদ্ধ।
  - বাক্যের স্বাভাবিক গঠন, শিক্ষক-সুলভ প্রাঞ্জলতা এবং লেখার সাবলীল প্রবাহ (Sentence Burstiness) শতভাগ বজায় রাখতে হবে।
  - বাংলা পোস্টে ইংরেজি টার্মগুলো স্বাভাবিক সংযোগে (যেমন: "কপোতাক্ষ নদ কবিতার CQ সমাধান", "SSC 2027 Bangla 1st Paper Suggestion-এর গুরুত্বপূর্ণ টিপস") ব্যবহৃত হবে।
  - ইংরেজি পোস্টে সম্পূর্ণ ইংরেজি বাক্যের ছন্দে শীর্ষ কিওয়ার্ডগুলো প্রাকৃতিকভাবে যুক্ত থাকবে।

---

## 4. Editorial Proofreading & Quality Gatekeeper Protocol
Raw OCR text from a scanned PDF must **NEVER** be published directly to Blogger. The agent must perform the following validation:

1. **Bengali Conjunct & Spelling Rectification:**
   * Thoroughly check all Bengali words for common OCR artifacts (e.g. `কষ` -> `ক্ষ`, `ঞচ` -> `ঞ্চ`).
   * Verify spelling against standard Bangla Academy academic terminology.
2. **Table Alignment & Data Verification:**
   * Verify that markdown table rows, headers, and marks distribution correspond exactly to syllabus standards.
3. **Cannibalization Check:**
   * Verify against `all_live_posts_catalog.json` using `topic_cannibalization_guard.py` before finalizing drafts.
4. **Theme & Dark Mode Integration:**
   * Wrap content in `<div class="htbd-academic-container">`.
   * Apply `.htbd-overview-box` at Position 0.
   * Format tables as `.htbd-academic-table`.
   * Format exam questions as `.htbd-exam-card` and quotes as `.htbd-quote-box`.
5. **Hero Banner Standard:**
   * Generate official banner from `Thumbnail BG/bg_2.png` with 1200x675 dimensions, `loading="eager" fetchpriority="high" decoding="async"`, and `class="htbd-hero-img"`.

---

## 5. Mandatory Official Source PDF Sourcing, Direct Website Hosting & Reader Download Card Standard (নতুন পোস্টের জন্য অফিসিয়াল পিডিএফ সংগ্রহ, সরাসরি হোস্টিং ও পাঠক ডাউনলোড কার্ড নীতি)

যেসব নোটিশ, সার্কুলার, রুটিন, রেজাল্ট, সিলেবাস বা নির্দেশনার অফিসিয়াল পিডিএফ সংশ্লিষ্ট সরকারি বা প্রাতিষ্ঠানিক ওয়েবসাইটে প্রকাশিত থাকে, সেসব বিষয়ে নতুন কোনো পোস্ট তৈরির ক্ষেত্রে এজেন্টকে নিচের নীতিমালাগুলো অলঙ্ঘনীয়ভাবে বাস্তবায়ন করতে হবে:

### ক. আসল ও প্রামাণ্য অফিসিয়াল পিডিএফ সংগ্রহ (Genuine Source Acquisition)
1. **মূল উৎস থেকে সংগ্রহ:** সংশ্লিষ্ট কর্তৃপক্ষ (যেমন: ঢাকা শিক্ষা বোর্ড, জাতীয় বিশ্ববিদ্যালয় `nu.ac.bd`, এনটিআরসিএ `ntrca.gov.bd`, শিক্ষা মন্ত্রণালয় `moedu.gov.bd`, প্রাথমিক শিক্ষা অধিদপ্তর `dpe.gov.bd`, বা বাংলাদেশ সরকারি কর্ম কমিশন `bpsc.gov.bd`)-এর অফিশিয়াল ওয়েবসাইট থেকে মূল স্বাক্ষরিত ও স্মারক নম্বরযুক্ত আসল পিডিএফ সংগ্রহ করতে হবে।
2. **জিরো ভুয়া বা আংশিক ফাইল:** কোনো অবস্থাতেই সোশ্যাল মিডিয়ার ক্রপ করা ছবি, আংশিক স্ন্যাপশট বা থার্ড-পার্টি ব্লগের বিকৃত পিডিএফ ব্যবহার করা যাবে না।
3. **লোকাল আর্কাইভিং:** সংগৃহীত পিডিএফটি প্রজেক্টের `input_pdfs/` ফোল্ডারে স্পষ্ট ইংরেজি নামে (যেমন: `ssc-2027-test-exam-notice-dhaka-board.pdf`) সংরক্ষণ করতে হবে।

### খ. আমাদের ওয়েবসাইটে সরাসরি হোস্টিং (Direct Hosting on Helptrickbd.com)
1. **কোনো এক্সটার্নাল লিংকের ওপর নির্ভরতা নয়:** সরকারি ওয়েবসাইটগুলোর সার্ভার প্রায়ই ডাউন থাকে বা লিংক পরিবর্তন হয়ে যায়, যার ফলে ভিজিটররা ৪MD/Dead Link-এর সম্মুখীন হন। তাই বাহ্যিক লিংকের পরিবর্তে পিডিএফ ফাইলটি সরাসরি আমাদের ওয়েবসাইটে হোস্ট করতে হবে।
2. **হোস্টিং পদ্ধতি:**
   - **WordPress Media Library:** ওয়ার্ডপ্রেস সাইটে নতুন পোস্ট তৈরির সময় পিডিএফ ফাইলটি ওয়ার্ডপ্রেস মিডিয়া লাইব্রেরিতে (`/wp-json/wp/v2/media`) আপলোড করে তার পারমানেন্ট ইউআরএল (`https://www.helptrickbd.com/wp-content/uploads/YYYY/MM/...pdf`) সংগ্রহ করতে হবে।
   - **GitHub / Fast CDN Fallback:** ওয়ার্ডপ্রেসের পাশাপাশি ফাইলটি গিটহাব রিপোজিটরির মাধ্যমে ব্যাকআপ রাখা হবে, যাতে বিদ্যুৎগতির সিডিএন এক্সেস নিশ্চিত থাকে।

### গ. পোস্টে আকর্ষণীয় ও রেসপনসিভ পিডিএফ কার্ড যুক্ত করা (In-Post Official PDF Card Architecture)
পোস্টের বডিতে (বিশেষ করে সারসংক্ষেপ বা মূল টেবিলের পর) পাঠকদের সরাসরি দেখার ও ডাউনলোড করার জন্য পরিচ্ছন্ন ও রেসপনসিভ অফিশিয়াল পিডিএফ কার্ড যুক্ত করতে হবে। 

**স্ট্যান্ডার্ড এইচটিএমএল স্ট্রাকচার:**
```html
<div class="htbd-pdf-card" style="background:#f8fafc; border:1px solid #e2e8f0; border-left:5px solid #0c2340; border-radius:8px; padding:20px; margin:25px 0; font-family:'SolaimanLipi', sans-serif;">
  <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:15px;">
    <div>
      <span style="background:#0c2340; color:#fff; font-size:12px; font-weight:600; padding:4px 10px; border-radius:4px; text-transform:uppercase;">অফিসিয়াল বিজ্ঞপ্তি ও পিডিএফ</span>
      <h3 style="margin:8px 0 4px 0; color:#0c2340; font-size:18px; font-weight:700;">{বিজ্ঞপ্তির পূর্ণাঙ্গ আনুষ্ঠানিক শিরোনাম}</h3>
      <p style="margin:0; color:#64748b; font-size:13px;">স্মারক নম্বর: {স্মারক নম্বর} | প্রকাশের তারিখ: {তারিখ} | ফাইল সাইজ: {সাইজ}</p>
    </div>
    <div style="display:flex; gap:10px; flex-wrap:wrap;">
      <a href="{PDF_LIVE_URL}" target="_blank" rel="noopener noreferrer" style="background:#1e3a8a; color:#ffffff; padding:10px 18px; border-radius:6px; text-decoration:none; font-size:14px; font-weight:600; display:inline-flex; align-items:center; gap:6px;">
        📄 সরাসরি পিডিএফ দেখুন
      </a>
      <a href="{PDF_LIVE_URL}" download style="background:#059669; color:#ffffff; padding:10px 18px; border-radius:6px; text-decoration:none; font-size:14px; font-weight:600; display:inline-flex; align-items:center; gap:6px;">
        📥 পিডিএফ ডাউনলোড
      </a>
    </div>
  </div>
</div>
```

### ঘ. এসইও ও ইউজার ট্রাস্ট সুবিধা (E-E-A-T & Ranking Benefit)
- **ডুয়েল বেনিফিট:** পাঠকরা হেল্পট্রিকবিডি থেকেই সরাসরি ১-ক্লিকে আসল প্রামাণ্য পিডিএফ পেয়ে যায়, যা বাউন্স রেট হ্রাস করে এবং অন-সাইট এঙ্গেজমেন্ট উল্লেখযোগ্যভাবে বৃদ্ধি করে।
- **E-E-A-T ট্রাস্ট:** অফিসিয়াল স্বাক্ষরিত ডকুমেন্টের সরাসরি উপস্থিতি পোস্টের অথেন্টিসিটি ১০০% বাড়িয়ে দেয়, যা গুগল অ্যাডসেন্স ও গুগল সার্চ কনসোলে টপ র‍্যাংকিং নিশ্চিত করে।

---

## 6. Automation Command Reference
* **Standard Ingestion:**
  ```powershell
  python tools/pdf_to_md/convert.py "input_pdfs/example.pdf"
  ```
* **High-Precision Cloud Vision (for complex scanned Bengali):**
  ```powershell
  python tools/pdf_to_md/convert.py "input_pdfs/example.pdf" --api-key "<KEY>"
  ```


