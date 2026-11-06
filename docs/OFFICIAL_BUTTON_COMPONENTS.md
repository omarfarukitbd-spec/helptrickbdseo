# HelpTrickBD Official Button Standards (v1.4.9)

Official UI standards for in-article action buttons on HelpTrickBD WordPress Theme.

---

## 1. Official PDF Download Pill Button (`.pdf-download-btn`)

### Features
- **Centered:** Encapsulated in `.pdf-download-wrap` (`margin: 20px auto; display: flex; justify-content: center;`).
- **Typography & Details:** Clean "Download PDF" title without cluttered file-size text.
- **Dual-Mode:** High contrast in Light Mode (`#ffffff`, `#17233d`) and Dark Mode (`#1e293b`, `#f8fafc`).
- **Interactive Modes:**
  1. **Direct 1-Click Download:** `download` attribute on anchor tag.
  2. **30-Second Countdown Timer:** Automatic interactive state via `data-timer="30" data-url="..."`.
- **Mobile Responsive:** Fluid scaling down to 320px viewport without wrapping or overflow.

### HTML Structure
```html
<div class="pdf-download-wrap">
  <a class="pdf-download-btn" href="https://example.com/file.pdf" data-timer="30" data-url="https://example.com/file.pdf" target="_blank" rel="noopener noreferrer">
    <!-- PDF Vector Icon -->
    <svg class="pdf-file-icon" viewBox="0 0 40 44" fill="none">
      <path d="M7 2H25L36 13V41H7V2Z" fill="#fff" stroke="#ef3038" stroke-width="2"/>
      <path d="M25 2V13H36" stroke="#ef3038" stroke-width="2"/>
      <rect x="2" y="20" width="35" height="16" rx="3" fill="#ef3038"/>
      <text x="19.5" y="32" text-anchor="middle" fill="white" font-size="11" font-weight="bold">PDF</text>
    </svg>
    <span class="pdf-divider"></span>
    <span class="pdf-info">
      <span class="pdf-title">Download PDF</span>
    </span>
    <span class="pdf-download-action">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
        <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
        <path d="m7 10 5 5 5-5"/>
        <path d="M12 15V3"/>
      </svg>
      Download
    </span>
  </a>
</div>
```

---

## 2. Official Source Link / Navigation Pill Button (`.source-link-btn`)

### Features
- **Centered:** Encapsulated in `.source-link-wrap`.
- **Layout:**
  - Left: Interlocking Chain Link SVG Icon (`#4935e9` / `#818cf8`).
  - Middle: Vertical divider + 2-line title & description.
  - Right: Curved square button with external link arrow (`↗`).
- **Hover Shield:** `!important` text color declarations preventing WordPress theme link hover collisions.

### HTML Structure
```html
<div class="source-link-wrap">
  <a class="source-link-btn" href="https://example.com/post-url" target="_blank" rel="noopener noreferrer">
    <svg class="source-link-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">
      <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/>
      <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>
    </svg>
    <span class="source-link-divider"></span>
    <span class="source-link-content">
      <span class="source-link-title">২০২১ সালের সম্পূর্ণ সমাধান দেখুন</span>
      <span class="source-link-desc">ক, খ ও গ বিভাগের শতভাগ নির্ভুল সমাধান গাইড</span>
    </span>
    <span class="source-link-arrow">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
        <path d="M14 3h7v7"/>
        <path d="M10 14 21 3"/>
        <path d="M21 14v6a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h6"/>
      </svg>
    </span>
  </a>
</div>
```
