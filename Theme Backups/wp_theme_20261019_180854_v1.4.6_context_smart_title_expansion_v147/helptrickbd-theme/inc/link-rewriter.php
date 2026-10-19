<?php
/**
 * HelpTrickBD Pro - Dynamic Internal Link Rewriter for Migrated Articles
 * Automatically rewrites legacy Blogger internal links (/YYYY/MM/slug.html, blogspot.com)
 * into modern, clean WordPress permalinks (/slug/) directly during page render.
 * Works immediately for all existing posts without requiring database re-imports.
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Filter post content to rewrite legacy Blogger internal links to WordPress permalinks.
 *
 * @param string $content The post content.
 * @return string Content with modern WordPress permalinks.
 */
function ht_rewrite_migrated_internal_links($content) {
    if (empty($content) || (function_exists('is_singular') && !is_singular())) {
        return $content;
    }

    // Quick bail-out if no anchor tags or .html links exist
    if (stripos($content, '<a ') === false || stripos($content, '.html') === false) {
        return $content;
    }

    // Predefined aliases for Blogger truncated slugs
    static $aliases = [
        'ssc-english-2nd-paper-suggestion-2027'       => 'ssc-english-2nd-paper-final-suggestion',
        'bcs-preliminary-marks-distribution-booklist' => 'bcs-preliminary-marks-distribution_01436475916',
        'remittance-importance'                       => 'what-is-remittance-importance-economy-obstacles',
        'basic-economy-problems-bd'                   => 'bangladesh-basic-economy-features-problems-solutions',
        'budget-importance'                           => 'what-is-budget-importance-role-economy',
        'nu-cgpa-calculator'                          => 'nu-cgpa-calculator',
    ];

    $base_url = function_exists('home_url') ? home_url() : 'https://www.helptrickbd.com';

    return preg_replace_callback('/<a\s+([^>]*?)href=(["\'])(.*?)\2([^>]*?)>/is', function ($matches) use ($aliases, $base_url) {
        $before_href = $matches[1];
        $quote       = $matches[2];
        $href        = trim($matches[3]);
        $after_href  = $matches[4];

        // Only process internal links matching helptrickbd, blogspot, or relative /YYYY/MM/
        $is_internal = (
            stripos($href, 'helptrickbd.com') !== false ||
            stripos($href, 'blogspot.com') !== false ||
            preg_match('#^/(?:p/|\d{4}/\d{2}/)#i', $href)
        );

        if (!$is_internal || stripos($href, '.html') === false) {
            return $matches[0];
        }

        // Separate URL path and fragment (#hash)
        $fragment = '';
        if (strpos($href, '#') !== false) {
            list($href, $fragment) = explode('#', $href, 2);
            $fragment = '#' . $fragment;
        }

        // Extract slug from /YYYY/MM/slug.html or /p/slug.html
        if (preg_match('#/(?:p/|\d{4}/\d{2}/)?([^/]+)\.html$#i', $href, $slug_matches)) {
            $raw_slug   = strtolower($slug_matches[1]);
            $clean_slug = preg_replace('/_\d+$/', '', $raw_slug);

            $target_slug = $aliases[$raw_slug] ?? ($aliases[$clean_slug] ?? $clean_slug);

            // Construct modern WordPress permalink
            $new_url = rtrim($base_url, '/') . '/' . sanitize_title($target_slug) . '/' . $fragment;

            return '<a ' . $before_href . 'href=' . $quote . esc_url($new_url) . $quote . $after_href . '>';
        }

        return $matches[0];
    }, $content);
}
add_filter('the_content', 'ht_rewrite_migrated_internal_links', 25);
