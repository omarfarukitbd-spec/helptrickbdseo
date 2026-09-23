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

## 5. Automation Command Reference
* **Standard Ingestion:**
  ```powershell
  python tools/pdf_to_md/convert.py "input_pdfs/example.pdf"
  ```
* **High-Precision Cloud Vision (for complex scanned Bengali):**
  ```powershell
  python tools/pdf_to_md/convert.py "input_pdfs/example.pdf" --api-key "<KEY>"
  ```

