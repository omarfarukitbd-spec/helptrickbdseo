<?php
/**
 * Multilingual Bridge: Polylang & WPML Compatibility Engine & SEO hreflang Output
 * HelpTrickBD Pro Theme
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Output Bidirectional hreflang Link Tags in Head (Google Search Central Standard).
 * Strictly outputs Self-Referencing tag, Alternate language tag, and x-default tag.
 */
function ht_output_bilingual_hreflang_tags() {
    // If Polylang or WPML handles hreflang, defer to them to avoid duplicates
    if (function_exists('pll_the_languages') || defined('ICL_SITEPRESS_VERSION')) {
        return;
    }

    // Only on singular posts, pages, or front-page
    if (!is_singular() && !is_front_page()) {
        return;
    }

    $current_url = home_url(add_query_arg([], $GLOBALS['wp']->request));
    if (is_front_page()) {
        $current_url = home_url('/');
    }

    $bn_url = add_query_arg('lang', 'bn', $current_url);
    $en_url = add_query_arg('lang', 'en', $current_url);
    $default_url = $bn_url;

    echo "\n<!-- HelpTrickBD Bilingual SEO hreflang Engine (Google Search Central Standard) -->\n";
    echo '<link rel="alternate" hreflang="bn-BD" href="' . esc_url($bn_url) . '" />' . "\n";
    echo '<link rel="alternate" hreflang="en-US" href="' . esc_url($en_url) . '" />' . "\n";
    echo '<link rel="alternate" hreflang="x-default" href="' . esc_url($default_url) . '" />' . "\n";
}
add_action('wp_head', 'ht_output_bilingual_hreflang_tags', 1);

/**
 * Filter Schema.org inLanguage tag dynamically.
 *
 * @param array $schema Schema array or string.
 * @return string Current inLanguage string.
 */
function ht_get_schema_in_language() {
    return (ht_get_current_lang() === 'en') ? 'en-US' : 'bn-BD';
}
