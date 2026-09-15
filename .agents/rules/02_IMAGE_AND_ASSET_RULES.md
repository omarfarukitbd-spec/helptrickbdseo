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
3. **Category Background Rule**:
   - Use fixed template backgrounds from `Thumbnail BG/` according to category mapping:
     * Education / Board Guides ➡️ Specified Education BG
     * Technology / Cloud ➡️ Tech BG
     * Politics / Academic ➡️ Academic BG
     * Islamic / Devotional ➡️ Islamic BG
     * Job Preparation / BCS ➡️ Job Prep BG
4. **Original Author Thumbnail Preservation (মৌলিক থাম্বনেইল অপরিবর্তনীয়)**:
   - If a post already possesses an authentic thumbnail designed by the site owner, the agent **MUST NOT replace or overwrite it**.
   - Only create new thumbnails for posts that completely lack a featured image or when explicitly requested by the user.

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

---

## ⚙️ 3. WebP Compression & Core Web Vitals (১০–২০ KB কম্প্রেশন)
1. **Compression Pipeline**:
   - Every PNG/JPG asset must be compressed using `tools/image_optimizer/webp_compressor.py`.
   - WebP quality setting: 75–82% with sharp YUV and smart subsampling to maintain crisp Bengali text while keeping file size under 20 KB.
2. **Lazy Loading & Responsive Attributes**:
   - All in-body images must include `loading="lazy"` and `decoding="async"`.
   - Include explicit `width="1200"` and `height="675"` (or proportional aspect ratios) to prevent Cumulative Layout Shift (CLS).

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
