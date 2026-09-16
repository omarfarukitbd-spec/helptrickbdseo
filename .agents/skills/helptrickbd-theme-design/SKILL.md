---
name: helptrickbd-theme-design
description: Complete design system, CSS architecture, native shortcodes, typography tokens, and responsive layout guidelines for the official Helptrickbd Blogger theme (FlexSpot Premium). Use whenever writing posts, creating UI components, designing tables, adding callout boxes, or modifying theme code.
---

# 🎨 Helptrickbd Theme Design & CSS Architecture Mastery (FlexSpot Engine)

This skill provides an authoritative, end-to-end technical reference for the official **Helptrickbd.com** theme (based on *FlexSpot Blogger Premium Template v2.7.0.V*). Every agent, designer, and content engineer must follow these design tokens, native CSS classes, shortcode conventions, and layout rules.

---

## 🏛️ 1. Theme Foundations & Container Dimensions

| Property | Value | Notes |
| :--- | :--- | :--- |
| **Theme Engine** | FlexSpot Blogger Premium v2.7.0.V | Templateiki customized engine |
| **Max Page Width** | `1145px` (`outerContainer.width`) | Centered via `#center-container`, `#outer-wrapper` |
| **Sidebar Width** | `320px` (`sidebar.width`) | Sticky via Theia Sticky Sidebar v1.7.0 |
| **Main Content Width** | Dynamic (~`780px` desktop) | `#main`, `.main-wrapper` |
| **Base Font Size** | `18px` for body text (`.post-body p`) | SolaimanLipi global override |
| **Primary Brand Color** | `#4E65FF` (`--main-button-color`) | High-contrast modern electric blue |
| **Secondary Brand Color** | `#2B64FF` (`--all-link-color`) | Hyperlink text color |
| **Text Main Color** | `#101010` / `#202124` | Primary high-contrast dark text |
| **Dark Mode Background** | `#111827` (`body.dark`) | Deep slate dark mode surface |

---

## 📱 2. Responsive Breakpoints & Mobile Adaptability

The theme uses 8 distinct responsive breakpoints. All custom post content must harmonize with these boundaries:

1. **`@media (max-width: 1178px)`**: Container padding collapses; body adjusts from fixed width to fluid width.
2. **`@media (max-width: 1080px)`**: Featured hero grids transition into 2-column mode.
3. **`@media (max-width: 880px)` (Critical Tablet Breakpoint)**:
   - Sidebar (`#sidebar-container`) un-sticks and drops below the main content area.
   - Header navigation collapses into the slide-out mobile drawer (`#menu-space`).
   - Content expands to full width with side padding.
4. **`@media (max-width: 768px)` (Standard Tablet/Mobile)**:
   - Footer widgets switch from 3 columns to 1 column.
   - Author profile boxes and meta headers stack vertically.
5. **`@media (max-width: 680px)`**:
   - Post list entries convert to single column compact cards.
   - Entry titles reduce font size to `16px`.
6. **`@media (max-width: 640px)` (Standard Smartphone)**:
   - Multi-column home widgets (`.mega-mode`, `.grid-posts`) become 100% full width stacked blocks.
   - `.post-body` margins tighten to prevent horizontal scrolling.
7. **`@media (max-width: 480px)` (Small Smartphone)**:
   - Action buttons (`.sp-bt`) stack text and icons cleanly.
   - Post title font size scales down for headline readability.
8. **`@media (max-width: 380px)` (Compact Mobile Viewports)**:
   - Social share icons shrink to 32px touch targets.

> [!IMPORTANT]
> **Mobile Padding Rule**: Never declare fixed pixel widths (`width: 1280px !important;` or inline `width: 800px;`) on post elements. Always use `width: 100%; max-width: 100%; box-sizing: border-box;`.

---

## 🔤 3. Typography & Bengali Font Rendering

The theme integrates **SolaimanLipi** as the supreme sitewide font:

```css
/* Sitewide typography rule enforced in theme <head> */
html, body, 
.post-body, 
.post-title, 
.post-title a,
h1, h2, h3, h4, h5, h6, 
p, span, a, li, td, th, 
input, button, select, textarea,
.widget, .sidebar, .header-menu, .footer,
.entry-title, .entry-content {
  font-family: 'SolaimanLipi', 'Noto Sans Bengali', Arial, sans-serif !important;
}
```

### Content Hierarchy Inside `.post-body`:
- **Title (H1)**: Handled by theme template (`<h1 class='post-title entry-title'>`). **NEVER** insert an `<h1>` inside post content!
- **H2 (Major Section)**: `24px`, `font-weight: 600`, `color: var(--theme-text-color)`, `margin: 25px 0 12px 0`.
- **H3 (Sub-section)**: `21px`, `font-weight: 600`, `margin: 20px 0 10px 0`.
- **H4 (Topic Group)**: `18px`, `font-weight: 600`, `margin: 15px 0 8px 0`.
- **Body Paragraph (`p`)**: `18px !important`, `line-height: 1.85 !important`, `color: #202124 !important`.
- **Lists (`ul`, `ol`)**: `margin: 10px 0`, `padding-left: 20px`, `line-height: 1.6`.

---

## 🧩 4. Built-in Native Shortcodes & UI Components

The FlexSpot theme features an integrated JavaScript shortcode processor inside the post body. You can use native shortcodes or clean semantic HTML classes:

### A. Alert / Callout Notification Boxes
The theme intercepts `<blockquote>` with trigger keywords and transforms them into FontAwesome-badged alert cards:

| Shortcode in `<blockquote>` | Rendered Class | Icon | Theme Purpose |
| :--- | :--- | :--- | :--- |
| `(alert-success)` | `.alert-message.success` | `\f058` (Check Circle) | Positive confirmations, success tips |
| `(alert-passed)` | `.alert-message.passed` | `\f1e3` (Info Badge) | Verified steps, information notes |
| `(alert-warning)` | `.alert-message.warning` | `\f071` (Exclamation Triangle) | Cautions, deadlines, essential warnings |
| `(alert-error)` | `.alert-message.error` | `\f06a` (Circle Exclamation) | Critical hazards, banned actions |

#### Example Usage (Semantic HTML):
```html
<div class="alert-message success">
  <strong>সফলতা:</strong> আপনার আবেদনটি সফলভাবে বোর্ডে জমা হয়েছে।
</div>

<div class="alert-message warning">
  <strong>সতর্কতা:</strong> ভুল তথ্য প্রদান করলে আবেদন স্বয়ংক্রিয়ভাবে বাতিল হয়ে যাবে।
</div>
```

---

### B. Action Buttons & Download Pills
The theme converts link shortcodes with `#text=(...)`, `#icon=(...)`, `#color=(...)` and `#size=(...)`:

#### Direct Semantic HTML Button (Recommended):
```html
<a class="main-button button sp-bt download" href="https://example.com/file.pdf" target="_blank" rel="noopener noreferrer">
  <span class="bt-info">ডাউনলোড করুন</span>
</a>
```

Available button modifier classes:
- `.download`: Download cloud icon (`\f381`)
- `.demo`: Eye preview icon (`\f06e`)
- `.link`: External link icon (`\f35d`)
- `.contact`: Address book icon (`\f2b9`)
- `.info`: Information circle icon (`\f05a`)

---

### C. Code Blocks with One-Click Copy (`.code-box`)
For ICT tutorials, software commands, or coding snippets:

```html
<pre class="code-box">git push origin main<button class="tune">Copy Now</button><input id="showlink" readonly="readonly" type="text" value="git push origin main"/></pre>
```

---

### D. Table of Contents (`.tociki-pro`)
The theme includes the `ndabas/toc` jQuery plugin. To activate:
- Add `<strike>(toc)</strike>` or `#title=(সূচিপত্র)` in the post, or
- Standard semantic container:
```html
<div class="tociki-pro">
  <div class="tociki-inner">
    <a href="javascript:;" class="tociki-title" role="button">
      <span class="tociki-title-text">সূচিপত্র</span>
    </a>
    <ol id="tociki"></ol>
  </div>
</div>
```
*(The script scans all `h2, h3, h4` in `.post-body` and builds a smooth-scrolling nested index).*

---

### E. Responsive Comparison Tables
Theme CSS establishes:
```css
.post-body table {
  width: 100%;
  border-collapse: collapse;
  border: 1px solid rgba(154, 154, 154, 0.15);
}
.post-body table th {
  font-weight: 700;
  padding: 8px 12px;
  background: #f8fafd;
}
.post-body table td {
  padding: 8px 12px;
  border: 1px solid rgba(154, 154, 154, 0.15);
}
```

#### Safe Mobile Responsive Pattern:
Always wrap multi-column tables with an overflow wrapper:
```html
<div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 15px 0;">
  <table style="width: 100%; min-width: 550px;">
    <thead>
      <tr>
        <th>বিষয় / কোর্স</th>
        <th>বিষয় কোড</th>
        <th>পূর্ণমান</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>রাজনৈতিক তত্ত্ব</td>
        <td>২১১৯০১</td>
        <td>১০০</td>
      </tr>
    </tbody>
  </table>
</div>
```

---

## 🚨 5. Feed Mechanics & The `<!--more-->` Rule

The FlexSpot theme uses client-side feed readers for:
- Related Posts ("YOU MAY LIKE" widget)
- Category Grids
- Mega Menus & Recent Tickers

### The Critical Engine Logic:
```javascript
h = c[l].content.$t;
h.indexOf("<img") > -1 ? $src = s(h) : $src = noThumb;
```

If `<!--more-->` is placed **before** the hero `<img>` tag:
1. Blogger's feed engine truncates `content.$t` at `<!--more-->`.
2. `h` has no `<img>` tag.
3. `$src` falls back to `noThumb`.
4. The related post widget displays a broken gray camera SVG!

**Enforced Law**: The hero banner (`<img>`) must ALWAYS appear before `<!--more-->`.

---

## 🌓 6. Dark Mode Variables Reference (`body.dark`)

When the user activates dark mode, the theme toggles `body.dark`:

| CSS Custom Property | Light Mode | Dark Mode (`body.dark`) |
| :--- | :--- | :--- |
| `--body-color-main` | `#f3f8ff` | `#111827` |
| `--main-text-color` | `#101010` | `#E4E4E4` |
| `--all-link-color` | `#2b64ff` | `rgba(255, 255, 255, 0.7)` |
| `--bg-cards` | `#ffffff` | `#1f2937` |
| `--theme-text-color` | `#3e3e3e` | `#dadada` |
| `--comment-content` | `#f6f6f6` | `#26313e` |

Agents writing custom inline CSS must use these variables or transparent alpha colors rather than hardcoded white/black.

---

## 🎯 7. Zero-Emoji & Vector Icon Standard

In accordance with Helptrickbd Governance Rule 12 & Rule 16:
- **Zero Emojis**: Never use emoji symbols (`📌`, `👉`, `📢`, `✅`, `💡`, `⚠️`) in content or widgets.
- **FontAwesome 6**: The theme includes FontAwesome 6 Free (`font-family: 'Font Awesome 6 Free'; font-weight: 900`).
- Use clean semantic HTML or CSS pseudo-elements:
  ```html
  <span class="fa-solid fa-circle-check" aria-hidden="true"></span>
  <span class="fa-solid fa-triangle-exclamation" aria-hidden="true"></span>
  <span class="fa-solid fa-book-open" aria-hidden="true"></span>
  ```

---

## 📋 8. Authoring Checklist for Helptrickbd Posts

Before publishing any post, verify against this theme checklist:
1. Hero banner is at top, followed by 100-word intro, followed by `<!--more-->`.
2. No `<h1>` tag inside post body (H2 for main sections, H3 for subsections).
3. Tables wrapped with `overflow-x: auto;` container.
4. Alerts use `.alert-message.success / .warning / .passed / .error`.
5. In-body images have `loading="lazy"`, `decoding="async"`, and `max-width: 100%`.
6. Zero emojis; vector icons used where necessary.
7. **Zero Embedded `<style>` Bloat**: Rely 100% on the theme's native CSS inheritance. Never inject `@font-face`, `.htbd-post-wrapper`, or redundant table/heading CSS.
8. **Zero Colorful Glitz**: No neon colors, loud rainbow borders, or heavy shadows. Keep all design clean, calm, high-contrast, and comfortable for extended reading.
9. Table of contents uses native `<strike>#title=(সূচিপত্র) (toc)</strike>` or `.tociki-pro`.

---

## 🚫 9. Zero-Bloat Policy & Theme Native Markup Reference

| Component | DO NOT Use (Banned Bloat) | USE INSTEAD (Theme Native) |
| :--- | :--- | :--- |
| **Typography** | In-post `@font-face`, `.htbd-post-wrapper` | Plain `<p>`, `<span>`, `<strong>` (Theme inherits SolaimanLipi globally) |
| **Headings** | `.htbd-heading` with custom thick blue border | Standard `<h2>`, `<h3>`, `<h4>` (Theme formats with 600-weight & slate accents) |
| **Table of Contents** | Custom 30-line CSS `.htbd-toc-box` | Native `<strike>#title=(সূচিপত্র) (toc)</strike>` or `<div class="tociki-pro">...</div>` |
| **Tables** | Custom `.htbd-table` with heavy styling | Standard semantic `<table>`, `<thead>`, `<tbody>`, `<th>`, `<td>` (Theme auto-wraps & styles) |
| **Alert / Notes** | Injected custom styled cards | Native `.alert-message.passed` / `.warning` / `.success` |
| **Code Blocks** | Custom code wrappers | Native `<pre class="code-box">code<button class="tune">Copy Now</button><input id="showlink" readonly type="text" value="code"/></pre>` |
| **Exceptions** | Loud gradients, neon colors, heavy shadows | If a custom widget (e.g. series navigation) is needed, use minimal inline CSS with `#e2e8f0` borders and `#ffffff` card surface. |
