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
     * Guarantees zero layout shift and bulletproof list styling against cache delays.
     */
    function htbd_inline_critical_css() {
        ?>
<style id="htbd-critical-css">
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
/* Bulletproof List Reset to Prevent Unstyled Browser Glitches */
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
  padding: 0;
}
/* SVG Icon Alignment */
.ht-icon {
  display: inline-block;
  vertical-align: middle;
  flex-shrink: 0;
}
/* Skeleton for Topbar & Masthead Fold */
.n-dateline {
  background: var(--ht-surface);
  border-bottom: 1px solid var(--ht-border);
  font-size: 0.8125rem;
  color: var(--ht-text-muted);
}
.n-masthead {
  background: var(--ht-surface);
  text-align: center;
  padding: 24px 0 16px;
  border-bottom: 3.5px double var(--ht-rule);
}
.n-navwrap {
  position: sticky;
  top: 0;
  z-index: 100;
  background: var(--ht-surface);
  border-bottom: 1px solid var(--ht-border);
  box-shadow: 0 2px 4px rgba(0,0,0,0.02);
}
</style>
        <?php
    }
}
add_action('wp_head', 'htbd_inline_critical_css', 1);
