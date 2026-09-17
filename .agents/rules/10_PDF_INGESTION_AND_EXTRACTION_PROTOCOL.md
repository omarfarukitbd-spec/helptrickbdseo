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

## 3. Editorial Proofreading & Quality Gatekeeper Protocol
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

## 4. Automation Command Reference
* **Standard Ingestion:**
  ```powershell
  python tools/pdf_to_md/convert.py "input_pdfs/example.pdf"
  ```
* **High-Precision Cloud Vision (for complex scanned Bengali):**
  ```powershell
  python tools/pdf_to_md/convert.py "input_pdfs/example.pdf" --api-key "<KEY>"
  ```
