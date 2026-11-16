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
/* ==========================================================================
   1. CSS Custom Properties (Tokens)
   ========================================================================== */
:root {
  --ht-font-sans: 'Hind Siliguri', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --ht-font-serif: 'SolaimanLipi', 'Noto Serif Bengali', Georgia, serif;
  --ht-font-heading: 'SolaimanLipi', 'Hind Siliguri', sans-serif;
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
  line-height: 1.6;
  font-size: calc(1rem * var(--ht-font-scale, 1));
  overflow-x: hidden;
  transition: background-color 0.2s ease, color 0.2s ease;
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
  padding: 0 16px;
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
  text-align: center;
  padding: 14px 0 12px;
  border-bottom: 2px solid var(--ht-border);
}
@media (min-width: 768px) {
  .n-masthead {
    padding: 24px 0 18px;
    border-bottom: 3.5px double var(--ht-rule);
  }
}
.n-brand-wordmark {
  font-family: var(--ht-font-serif);
  font-size: clamp(1.65rem, 5vw, 3.25rem);
  font-weight: 800;
  letter-spacing: -0.02em;
  color: var(--ht-text-primary);
  line-height: 1.15;
  margin-bottom: 4px;
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
.n-brand-tagline {
  font-size: clamp(0.75rem, 2vw, 0.875rem);
  color: var(--ht-text-secondary);
  margin: 0;
  line-height: 1.4;
}
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
</style>
        <?php
    }
}
add_action('wp_head', 'htbd_inline_critical_css', 1);
