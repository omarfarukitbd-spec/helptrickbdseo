---
name: seo-blogger-adsense
description: End-to-end SEO, Google AdSense approval, and ranking mastery for Blogger (Blogspot) and content websites. Use whenever working on website SEO, Google ranking, AdSense approval, XML theme optimization, content writing, or Search Console indexing.
---

# 🚀 Blogger SEO & Google AdSense Approval Mastery Skill

This skill equips the AI agent to act as a world-class SEO Director, Webmaster, and AdSense Approval Strategist specifically tuned for **Blogger (Blogspot)** and content-driven websites.

---

## 📋 1. AdSense Approval 100% Blueprint (গুগল এডসেন্স অনুমোদনের নিয়মাবলি)

Google AdSense rejects 90% of blogs due to "Low Value Content", "Scraped Content", or "Navigation Issues". Follow this strict checklist to guarantee approval:

### A. The 5 Mandatory Legal & Trust Pages (আবশ্যিক পেজসমূহ)
Never apply for AdSense without these 5 standalone static pages in Blogger:
1. **About Us (আমাদের সম্পর্কে):** Who runs the site, mission, editorial guidelines, expertise (E-E-A-T signals).
2. **Contact Us (যোগাযোগ):** Working contact form, email address, physical address/city, social profiles.
3. **Privacy Policy (গোপনীয়তা নীতি):** Explicit mention of Google AdSense, cookies, DoubleClick DART cookie, third-party advertising partners, GDPR/CCPA compliance.
4. **Terms and Conditions (ব্যবহারের শর্তাবলি):** Content usage, intellectual property, disclaimer of warranties.
5. **Disclaimer (দাবিত্যাগ):** Educational/informational disclaimer, affiliate disclosure (if applicable).

### B. Content Inventory Requirements (কন্টেন্ট রিকোয়ারমেন্ট)
- **Minimum Post Count:** 20 to 30 high-quality, fully unique published articles.
- **Article Word Count:** 800 to 1,500+ words per article. Zero thin content (posts under 400 words must be deleted or expanded).
- **Value Addition:** Must solve real user queries. Do not generate generic regurgitated AI text. Use practical examples, step-by-step guides, tables, and unique perspectives.
- **Images:** Every post must have at least 1-2 original or properly attributed featured images with descriptive alt text and WebP/compressed formats. Zero copyright infringement.

### C. Site Structure & Navigation (সাইট স্ট্রাকচার)
- **Category Balance:** Minimum 3-4 distinct categories/labels in Blogger. Every category MUST have at least 4-5 published posts (no empty or single-post categories).
- **Navigation Menus:** 
  - **Header Menu:** Home, Categories (Dropdown), Contact.
  - **Footer Menu:** About Us, Privacy Policy, Terms & Conditions, Disclaimer, Contact Us.
- **Clean Theme:** Clean, mobile-responsive theme with readable typography (16px+ body font), dark/light contrast, no broken links, zero intrusive popups.

---

## ⚙️ 2. Blogger Technical SEO & Theme Optimization (ব্লগার টেকনিক্যাল এসইও)

### A. Custom robots.txt for Blogger
Configure in **Settings > Crawlers and indexing > Custom robots.txt**:
```text
User-agent: *
Disallow: /search
Disallow: /*?m=1
Disallow: /*?m=0
Allow: /

Sitemap: https://YOUR_DOMAIN.com/sitemap.xml
Sitemap: https://YOUR_DOMAIN.com/atom.xml?redirect=false&start-index=1&max-results=500
```

### B. Custom Robot Header Tags (ব্লগার রোবট হেডার ট্যাগ)
Configure in **Settings > Crawlers and indexing > Custom robot header tags**:
- **Home page tags:** `all`, `noodp`
- **Archive and search page tags:** `noindex`, `nofollow`, `noodp`
- **Post and page tags:** `all`, `noodp`

### C. XML Theme Head Optimization (মেটা ট্যাগ ও স্কিমা)
Inject into Blogger Theme XML (`<head>` section):
1. **Dynamic Meta Description:**
```xml
<b:if cond='data:view.isPost'>
  <meta expr:content='data:blog.metaDescription' name='description'/>
  <meta expr:content='data:blog.pageName' property='og:title'/>
  <meta expr:content='data:blog.canonicalUrl' property='og:url'/>
  <meta content='article' property='og:type'/>
</b:if>
```
2. **JSON-LD Schema Markup (BlogPosting / Article Schema):**
Generate structured `application/ld+json` including `headline`, `image`, `datePublished`, `dateModified`, `author` (Person), and `publisher` (Organization).

---

## 🎯 3. Keyword Research & Google Ranking Strategy (র‍্যাংকিং স্ট্র্যাটেজি)

### A. KGR (Keyword Golden Ratio) Method for Fast Ranking
Target low-competition keywords that rank in days without backlinks:
$$\text{KGR} = \frac{\text{Allintitle results (allintitle: "keyword")}}{\text{Monthly Search Volume}} < 0.25$$
- If KGR $< 0.25$: High probability of ranking in top 50 as soon as indexed.
- Target search volume: 50 to 250 monthly searches.

### B. Search Intent Mapping
Ensure article format matches user intent:
- **Informational ("কিভাবে", "কী", "কখন"):** How-to guides, numbered steps, summary callouts.
- **Commercial/Review ("সেরা", "বনাম"):** Comparison tables, pros/cons, rating badges.
- **Navigational/Direct:** Direct answer in the first 100 words (Featured Snippet optimization).

---

## ✍️ 4. On-Page SEO Article Architecture (আর্টিকেল লেখার স্ট্যান্ডার্ড)

When authoring or optimizing any article:
1. **URL Slug (Permalink):** Custom permalink containing exact focus keyword, hyphen-separated, under 50 characters (e.g., `best-class-1-math-guide`).
2. **Title (H1):** Primary keyword near the front, emotional hook/year (e.g., `সহজ নিয়মে সমাধান (২০২৬)`).
3. **Intro (First 100 Words):** Direct answer to search query + Primary keyword in the first sentence + Table of Contents.
4. **Subheadings (H2, H3):** Natural LSI keywords in subheadings. Never skip heading levels.
5. **Internal Linking:** Every article must link to 2-3 relevant existing posts on the blog with descriptive anchor texts (never "ক্লিক করুন" or "click here").
6. **External Authority Links:** 1-2 outbound links to trusted, non-competing authoritative sources (Wikipedia, Govt. portals, official documentation).
7. **Image SEO:** WebP format, descriptive filename (`bengali-vowels-guide.webp`), descriptive `alt` attribute, and visible captions.
8. **FAQ Schema:** 3-5 frequently asked questions at the end of the post with schema markup.

---

## 🔍 5. Search Console & Indexing Health (গুগল সার্চ কনসোল ও ইনডেক্সিং)

- Submit sitemaps: `/sitemap.xml` and `/atom.xml?redirect=false&start-index=1&max-results=500`.
- Monitor **Page Indexing** report:
  - Fix "Discovered - currently not indexed" by improving internal linking and content depth.
  - Fix "Crawled - currently not indexed" by eliminating duplicate/thin content and updating freshness.
- Test Core Web Vitals: Ensure LCP $< 2.5\text{s}$, FID/INP $< 200\text{ms}$, CLS $< 0.1$.
