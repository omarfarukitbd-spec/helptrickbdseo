---
name: htbd-power-cli
description: Master unified 1-command end-to-end publishing pipeline for Helptrickbd SEO & Content.
license: Apache-2.0
metadata:
  version: v1
  publisher: Helptrickbd
---

# ⚡ htbd-power-cli — Master Unified Publishing Pipeline

Whenever the user provides a PDF, topic, or raw syllabus in chat and asks to publish or create posts, ANY AI agent should invoke this unified high-speed CLI tool instead of writing fragmented 1,000+ line python files.

## 🚀 1-Command Execution

```bash
python tools/cli/htbd.py auto --title "<TOPIC_TITLE>" [--pdf <PATH_TO_PDF>] [--category <CAT>] [--publish] [--live]
```

### Flags:
- `--title`: The main Bengali/English title of the topic or syllabus.
- `--pdf`: (Optional) Absolute or relative path to a syllabus or suggestion PDF.
- `--category`: Category hint (`Education`, `Job Study`, `Islamic`, `Tech`).
- `--publish`: Triggers direct Blogger API publishing.
- `--live`: Publishes directly as Live (omitting this publishes as Draft).

## 🛡️ Internal Automated Pipeline (All in 1 execution):
1. **PDF Parsing**: `pdfplumber` / `pypdf` extracts pages and text.
2. **Silo Architecture**: Automatically maps 1 Pillar + adaptive 3 to 5 Silo parts.
3. **Official Thumbnails**: Uses `Thumbnail BG/` (`bg_1` to `bg_4`) with Hind Siliguri Bold and compresses to 10-20 KB WebP.
4. **Content Synthesis**: Renders from `templates/archetypes/school_study_guide.html` via `template_renderer.py` (> 2,000 words, SolaimanLipi, Position 0 box, FAQ schema).
5. **Quality Gatekeeper**: Audits each post with `PreFlightChecker` (0 errors, 0 warnings).
6. **Live Publishing**: Blogger API v3 insertion + Google Indexing API ping + WebSub hubs ping.
