<?php
/**
 * Inlined Critical CSS Engine for Zero FOUC & 100/100 Core Web Vitals
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}

if (!function_exists('htbd_inline_critical_css')) {
    /**
     * Outputs inlined critical CSS directly in <head>.
     * Guarantees zero layout shift and bulletproof styling against render-blocking delays.
     */
    function htbd_inline_critical_css() {
        ?>
<style id="htbd-critical-css">
@font-face {
  font-family: 'Shurjo';
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url('<?php echo esc_url(get_template_directory_uri() . '/assets/fonts/ShurjoWeb_400.woff2'); ?>') format('woff2');
}
@font-face {
  font-family: 'Shurjo';
  font-style: normal;
  font-weight: 700;
  font-display: swap;
  src: url('<?php echo esc_url(get_template_directory_uri() . '/assets/fonts/ShurjoWeb_700.woff2'); ?>') format('woff2');
}
@font-face {
  font-family: 'SolaimanLipi';
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url('<?php echo esc_url(get_template_directory_uri() . '/assets/fonts/SolaimanLipi_400.woff2'); ?>') format('woff2');
}
@font-face {
  font-family: 'SolaimanLipi';
  font-style: normal;
  font-weight: 700;
  font-display: swap;
  src: url('<?php echo esc_url(get_template_directory_uri() . '/assets/fonts/SolaimanLipi_700.woff2'); ?>') format('woff2');
}
/* ==========================================================================
   1. CSS Custom Properties (Tokens)
   ========================================================================== */
:root {
  --ht-font-sans: 'SolaimanLipi', 'Siyam Rupali', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --ht-font-serif: 'Shurjo', Georgia, 'Times New Roman', serif;
  --ht-font-heading: 'Shurjo', Georgia, serif;
  --ht-bg: #f8fafc;
  --ht-surface: #ffffff;
  --ht-surface-alt: #f1f5f9;
  --ht-border: #e2e8f0;
  --ht-rule: #0f172a;
  --ht-text-primary: #0f172a;
  --ht-text-secondary: #475569;
  --ht-text-muted: #64748b;
  --ht-primary: #1a56db;
  --ht-primary-dark: #1e40af;
  --ht-accent: #d97706;
  --ht-danger: #dc2626;
  --ht-max-width: 1240px;
  --ht-radius: 8px;
  --ht-radius-sm: 4px;
  --ht-radius-lg: 12px;
  --ht-shadow-sm: 0 1px 3px rgba(0,0,0,0.06);
  --ht-shadow-md: 0 4px 6px -1px rgba(0,0,0,0.08);

  /* Semantic Aliases */
  --htbd-primary: var(--ht-primary);
  --htbd-accent: var(--ht-accent);
  --htbd-bg: var(--ht-bg);
  --htbd-surface: var(--ht-surface);
  --htbd-border: var(--ht-border);
  --htbd-text: var(--ht-text-primary);
  --htbd-text-muted: var(--ht-text-muted);
}

[data-theme="dark"] {
  --ht-bg: #090d16;
  --ht-surface: #111827;
  --ht-surface-alt: #1f2937;
  --ht-border: #1f2937;
  --ht-rule: #374151;
  --ht-text-primary: #f8fafc;
  --ht-text-secondary: #cbd5e1;
  --ht-text-muted: #94a3b8;
  --ht-primary: #3b82f6;
  --ht-primary-dark: #60a5fa;
  --ht-accent: #f59e0b;
}

/* ==========================================================================
   2. Reset & Base Layout
   ========================================================================== */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
html {
  font-size: 16px;
  -webkit-text-size-adjust: 100%;
  scroll-behavior: smooth;
}
body {
  font-family: var(--ht-font-sans);
  background-color: var(--ht-bg);
  color: var(--ht-text-primary);
  line-height: var(--ht-body-line-height, 1.75);
  font-size: calc(1rem * var(--ht-font-scale, 1));
  overflow-x: hidden;
  transition: background-color 0.2s ease, color 0.2s ease;
  letter-spacing: normal;
}
html[lang="bn-BD"] body, body.ht-lang-bn {
  font-family: 'SolaimanLipi', 'Noto Sans Bengali', var(--ht-font-sans);
  line-height: 1.8;
  letter-spacing: normal !important;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
html[lang="bn-BD"] h1, html[lang="bn-BD"] h2, html[lang="bn-BD"] h3,
html[lang="bn-BD"] h4, html[lang="bn-BD"] h5, html[lang="bn-BD"] h6,
body.ht-lang-bn h1, body.ht-lang-bn h2, body.ht-lang-bn h3,
body.ht-lang-bn h4, body.ht-lang-bn h5, body.ht-lang-bn h6,
body.ht-lang-bn .n-lead-title, body.ht-lang-bn .ht-card-title,
body.ht-lang-bn .ht-article-title, body.ht-lang-bn .n-sec-head h3 {
  font-family: 'Shurjo', 'SolaimanLipi', var(--ht-font-serif);
  line-height: 1.45;
  letter-spacing: normal !important;
}
ul, ol, menu {
  list-style: none !important;
  margin: 0 !important;
  padding: 0 !important;
}
a {
  color: inherit;
  text-decoration: none;
  transition: color 0.15s ease;
}
img {
  max-width: 100%;
  height: auto;
  display: block;
  content-visibility: auto;
}
button {
  font-family: inherit;
  border: none;
  background: none;
  cursor: pointer;
}
.ht-container {
  width: 100%;
  max-width: var(--ht-max-width);
  margin-left: auto;
  margin-right: auto;
  padding: 0 10px;
}
@media (min-width: 600px) {
  .ht-container {
    padding: 0 16px;
  }
}
@media (min-width: 768px) {
  .ht-container {
    padding: 0 24px;
  }
}
.skip-link {
  position: absolute;
  top: -100px;
  left: 16px;
  background: var(--ht-primary);
  color: #ffffff;
  padding: 8px 16px;
  z-index: 9999;
  border-radius: var(--ht-radius-sm);
  font-weight: 600;
  transition: top 0.2s ease;
}
.skip-link:focus {
  top: 16px;
}
.ht-icon {
  display: inline-block;
  vertical-align: middle;
  flex-shrink: 0;
}

/* ==========================================================================
   3. Header Above-the-Fold (Dateline, Masthead, Sticky Navbar)
   ========================================================================== */
.n-dateline {
  background: var(--ht-surface);
  border-bottom: 1px solid var(--ht-border);
  font-size: 0.8125rem;
  color: var(--ht-text-muted);
  padding: 6px 0;
}
.n-dateline-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
}
.n-dateline-right {
  display: flex;
  align-items: center;
  gap: 8px;
}
.n-fsbar {
  display: flex;
  align-items: center;
  gap: 4px;
  background: var(--ht-surface-alt);
  padding: 2px 6px;
  border-radius: 999px;
  font-size: 0.75rem;
}
.n-fsbtn {
  padding: 2px 6px;
  border-radius: 4px;
  color: var(--ht-text-muted);
  font-weight: 500;
}
.n-fsbtn.active {
  background: var(--ht-surface);
  color: var(--ht-text-primary);
  font-weight: 700;
  box-shadow: var(--ht-shadow-sm);
}
.ht-icon-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  color: var(--ht-text-secondary);
  background: var(--ht-surface-alt);
  transition: background 0.15s ease, color 0.15s ease;
}
.ht-icon-btn:hover {
  background: var(--ht-border);
  color: var(--ht-text-primary);
}
@media (max-width: 639px) {
  .n-fsbar { display: none !important; }
  .n-dateline-inner { flex-wrap: nowrap; gap: 10px; }
  .n-dateline-left { min-width: 0; flex: 1; }
  .n-date-text { font-size: 0.75rem; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .n-dateline-right { gap: 6px; flex-shrink: 0; }
}
.n-masthead {
  background: var(--ht-surface);
  padding: 12px 0 10px;
  border-bottom: 2px solid var(--ht-border);
}
@media (min-width: 768px) {
  .n-masthead {
    padding: 18px 0 16px;
    border-bottom: 3.5px double var(--ht-rule);
  }
}
.n-masthead-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}
.n-brand-left {
  display: flex;
  align-items: center;
}
.n-brand-wordmark {
  font-family: var(--ht-font-serif);
  font-size: clamp(1.6rem, 4vw, 2.75rem);
  font-weight: 900;
  letter-spacing: -0.02em;
  color: var(--ht-text-primary);
  line-height: 1.15;
  margin: 0;
  text-align: left;
}
.n-brand-wordmark a {
  color: inherit;
  text-decoration: none;
}
.n-brand-tld {
  color: var(--ht-accent, #b3271e);
  font-weight: 700;
  font-size: 0.85em;
  letter-spacing: -0.01em;
}
.n-brand-subdomain {
  display: none !important;
}
.n-brand-right {
  display: flex;
  align-items: center;
  gap: 12px;
}
.n-masthead-search-btn,
.n-masthead-theme-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: var(--ht-radius-full);
  border: 1.5px solid var(--ht-border);
  background: var(--ht-surface-alt);
  color: var(--ht-text-primary);
  cursor: pointer;
}
.n-masthead-theme-btn .ht-theme-icon-sun { display: none; }
.n-masthead-theme-btn .ht-theme-icon-moon { display: inline-flex; }
[data-theme="dark"] .n-masthead-theme-btn .ht-theme-icon-sun { display: inline-flex; }
[data-theme="dark"] .n-masthead-theme-btn .ht-theme-icon-moon { display: none; }
.n-navwrap {
  position: sticky;
  top: 0;
  z-index: 100;
  background: var(--ht-surface);
  border-bottom: 1px solid var(--ht-border);
  box-shadow: 0 2px 4px rgba(0,0,0,0.02);
}
.n-nav-inner {
  display: flex;
  align-items: center;
  gap: 12px;
  height: 48px;
}
.n-mobile-toggle {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 6px;
  color: var(--ht-text-primary);
}
@media (min-width: 992px) {
  .n-mobile-toggle {
    display: none;
  }
}
.n-nav-track {
  display: flex;
  align-items: center;
  gap: 4px;
  overflow-x: auto;
  white-space: nowrap;
  scrollbar-width: none;
  -webkit-overflow-scrolling: touch;
  flex: 1;
}
.n-nav-track::-webkit-scrollbar {
  display: none;
}
.n-nav-item {
  padding: 6px 12px;
  border-radius: 999px;
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--ht-text-secondary);
  transition: all 0.15s ease;
}
.n-nav-item:hover, .n-nav-item.active {
  background: var(--ht-primary);
  color: #ffffff;
}
@media (max-width: 767px) {
  .n-kbd-shortcut {
    display: none !important;
  }
}

/* ==========================================================================
   4. Homepage Above-the-Fold (Ticker & Lead Hero)
   ========================================================================== */
.n-ticker {
  display: flex;
  align-items: center;
  background: var(--ht-surface);
  border: 1px solid var(--ht-border);
  border-radius: var(--ht-radius);
  margin: 16px 0;
  overflow: hidden;
  height: 42px;
}
.n-ticker-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: var(--ht-danger);
  color: #ffffff;
  font-size: 0.8125rem;
  font-weight: 700;
  padding: 0 14px;
  height: 100%;
  white-space: nowrap;
  flex-shrink: 0;
}
.n-ticker-dot {
  width: 7px;
  height: 7px;
  background: #ffffff;
  border-radius: 50%;
  animation: htbd-pulse 1.5s infinite;
}
@keyframes htbd-pulse {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.4; transform: scale(0.85); }
}
.n-ticker-track {
  flex: 1;
  overflow: hidden;
  white-space: nowrap;
  position: relative;
  padding: 0 12px;
}
.n-ticker-move {
  display: inline-flex;
  align-items: center;
  gap: 16px;
  font-size: 0.875rem;
  color: var(--ht-text-primary);
}
.n-ticker-sep {
  color: var(--ht-text-muted);
}
.n-lead {
  display: grid;
  grid-template-columns: 1fr;
  gap: 24px;
  margin-bottom: 24px;
}
@media (min-width: 992px) {
  .n-lead {
    grid-template-columns: 65% calc(35% - 24px);
  }
}
.n-kicker {
  display: inline-block;
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--ht-primary);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 6px;
}
.n-lead-title {
  font-family: var(--ht-font-heading);
  font-size: clamp(1.35rem, 3vw, 1.875rem);
  font-weight: 700;
  line-height: 1.3;
  margin-bottom: 12px;
  color: var(--ht-text-primary);
}
.htbd-ad-slot {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 90px;
  background: var(--ht-surface-alt);
  border: 1px dashed var(--ht-border);
  border-radius: var(--ht-radius);
  margin: 20px 0;
  text-align: center;
}
.ht-sidebar-area .widget_search,
.ht-sidebar-area .wp-block-search,
.ht-sidebar-wrapper .widget_search,
.ht-sidebar-wrapper .wp-block-search,
.n-home-layout-sidebar .widget_search,
.n-home-layout-sidebar .wp-block-search,
.ht-sidebar-area .widget_archive,
.ht-sidebar-area .wp-block-archives,
.ht-sidebar-wrapper .widget_archive,
.ht-sidebar-wrapper .wp-block-archives,
.n-home-layout-sidebar .widget_archive,
.n-home-layout-sidebar .wp-block-archives,
.ht-sidebar-area .widget_categories,
.ht-sidebar-area .wp-block-categories,
.ht-sidebar-wrapper .widget_categories,
.ht-sidebar-wrapper .wp-block-categories,
.n-home-layout-sidebar .widget_categories,
.n-home-layout-sidebar .wp-block-categories,
.ht-widget:has(.wp-block-archives),
.ht-widget:has(.wp-block-categories),
.ht-widget:has(.wp-block-search),
.ht-widget:has(.widget_search),
.ht-widget:has(.widget_archive),
.ht-widget:has(.widget_categories),
.ht-widget.widget_search,
.ht-widget.widget_archive,
.ht-widget.widget_categories,
.n-sidebar-cats-widget {
  display: none !important;
}
</style>
        <?php
    }
}
add_action('wp_head', 'htbd_inline_critical_css', 1);
