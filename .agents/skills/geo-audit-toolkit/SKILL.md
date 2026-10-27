---
name: geo-audit-toolkit
description: Official open-source Generative Engine Optimization (GEO) & Answer Engine Optimization (AEO) audit toolkit. Evaluates websites across ChatGPT/SearchGPT, Google AI Overviews, Perplexity, Claude, and Mistral Le Chat for AI crawler policies (robots.txt), Schema.org JSON-LD structured data, BLUF answer compliance, and authority signals.
---

# 🤖 GEO Audit Toolkit — HelpTrickBD Autonomous Skill

An evidence-based, open-source **Generative Engine Optimization (GEO)** and **Answer Engine Optimization (AEO)** diagnostic toolkit. It measures how effectively generative AI search engines (ChatGPT, Google AI Overviews, Perplexity, Claude, and Le Chat) crawl, extract, and cite HelpTrickBD content.

---

## 🎯 What it Audits

1. **AI Crawler Taxonomy & Access:**
   - Evaluates `robots.txt` compliance across 27+ AI crawlers categorized into Training, Search/RAG, and User-Fetch tiers.
   - Validates `/llms.txt` presence and structure according to `llmstxt.org` specification.

2. **Schema.org & Entity Health (EEP):**
   - Deep JSON-LD schema parsing (EducationalOrganization, Article, FAQPage, BreadcrumbList, WebSite).
   - Validates visible facts coverage against schema declarations to avoid hallucination penalties.

3. **BLUF (Bottom Line Up Front) Compliance:**
   - Inspects whether pages answer core user search intents in the first 100–150 words (essential for Google AI Overviews and ChatGPT snippet selection).

4. **Multi-LLM Retrieval Mapping:**
   - **ChatGPT / SearchGPT:** Backed by Google search proxy.
   - **Google AI Overviews / Gemini:** Direct Google index.
   - **Perplexity:** Multi-index (Google + Brave).
   - **Claude:** Brave search index.
   - **Le Chat (Mistral):** Brave search index.

---

## 🚀 How to Run an Audit

### 1. From Terminal / Command Line:
```bash
# Run full audit on HelpTrickBD homepage
py tools/geo_auditor.py https://www.helptrickbd.com/

# Audit specific article or section with up to 5 sampled pages
py tools/geo_auditor.py https://www.helptrickbd.com/category/education/ --max-pages 5
```

### 2. Output & Reports:
All audit reports are automatically compiled and saved in:
`reports/geo_audits/<slug>/<YYYY-MM-DD>-audit.md`

Each report includes:
- **Strengths (Keep these):** Validated technical assets.
- **Action Plan:** Prioritized fixes categorized by LLM impact (`+++`, `++`, `+`).
- **Quick Wins:** Concrete changes taking ≤ 30 minutes.
- **Technical Appendices:** Detailed crawler findings and JSON-LD diagnostics.
