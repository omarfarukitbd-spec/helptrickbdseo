<?php
/**
 * HelpTrickBD Pro - Migrated Content Sanitizer & Dark Mode Optimizer
 * Automatically neutralizes hardcoded inline dark colors, blinding light backgrounds,
 * legacy font declarations, and optimizes HTML payload for 100% Core Web Vitals speed.
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Filter post content to remove legacy inline style conflicts from Blogger migration.
 *
 * @param string $content The post content.
 * @return string Sanitized content.
 */
function ht_sanitize_migrated_post_content($content) {
    if (empty($content) || (function_exists('is_singular') && !is_singular())) {
        return $content;
    }

    // Fast bail-out if no inline styles exist
    if (stripos($content, 'style=') === false) {
        return $content;
    }

    // Helper for attribute escaping
    $esc = function ($str) {
        return function_exists('esc_attr') ? esc_attr($str) : htmlspecialchars($str, ENT_QUOTES, 'UTF-8');
    };

    // 1. Strip hardcoded inline colors from headings (h1 - h6) so they inherit theme typography
    $content = preg_replace_callback('/<(h[1-6])([^>]*)>(.*?)(<\/\1>)/is', function ($matches) use ($esc) {
        $tag   = $matches[1];
        $attrs = $matches[2];
        $inner = $matches[3];
        $close = $matches[4];

        if (stripos($attrs, 'style=') !== false) {
            $attrs = preg_replace_callback('/style=(["\'])(.*?)\1/is', function ($sm) use ($esc) {
                $cleaned_style = preg_replace('/color\s*:[^;]+;?/i', '', $sm[2]);
                $cleaned_style = trim(preg_replace('/;{2,}/', ';', $cleaned_style), "; \t\n\r\0\x0B");
                return $cleaned_style ? 'style="' . $esc($cleaned_style) . '"' : '';
            }, $attrs);
        }

        return "<{$tag}{$attrs}>{$inner}{$close}";
    }, $content);

    // 2. Universal inline style cleanup for text & container elements
    $content = preg_replace_callback('/style=(["\'])(.*?)\1/is', function ($matches) use ($esc) {
        $style = $matches[2];

        // Neutralize hardcoded dark text colors
        $style = preg_replace(
            '/color\s*:\s*(?:#[0-6][0-9a-f]{5}|#[0-6][0-9a-f]{2}|rgb\(\s*(?:[0-9]|[1-9][0-9]|1[0-1][0-9])\s*,\s*(?:[0-9]|[1-9][0-9]|1[0-1][0-9])\s*,\s*(?:[0-9]|[1-9][0-9]|1[0-1][0-9])\s*\)|black|#1a73e8|#0c2340|#14532d|#15803d|#0369a1|#047857|#202124|#1e293b|#334155|#64748b|#b45309|#b91c1c)\s*(?:!important)?\s*;?/i',
            '',
            $style
        );

        // Neutralize blinding white/light backgrounds
        $style = preg_replace(
            '/background(?:-color)?\s*:\s*(?:#(?:f[0-9a-f]{5}|e[0-9a-f]{5}|d[0-9a-f]{5}|fff(?:fff)?)|white|rgb\(\s*(?:2[0-5][0-9])\s*,\s*(?:2[0-5][0-9])\s*,\s*(?:2[0-5][0-9])\s*\)|linear-gradient\([^)]*(?:240|250|253|255|fff|e8f)[^)]*\))\s*(?:!important)?\s*;?/i',
            '',
            $style
        );

        // Neutralize legacy inline font-family declarations
        $style = preg_replace('/font-family\s*:\s*[^;]+;?/i', '', $style);

        // Clean up redundant semicolons and trim
        $style = trim(preg_replace('/;{2,}/', ';', $style), "; \t\n\r\0\x0B");

        if (empty($style)) {
            return '';
        }

        return 'style="' . $esc($style) . '"';
    }, $content);

    // 3. Remove leftover empty style="" attributes
    $content = preg_replace('/\s+style=(["\'])\s*\1/i', '', $content);

    return $content;
}
add_filter('the_content', 'ht_sanitize_migrated_post_content', 20);
