<?php
/**
 * Dynamic CSS Generator for Customizer Settings
 * Injects CSS variables for Typography, Fonts & Layout into wp_head.
 * Single Source of Truth architecture.
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Output dynamic CSS styles based on Customizer choices.
 */
function ht_customizer_dynamic_css() {
    $is_bn = function_exists('ht_is_bangla_locale') ? ht_is_bangla_locale() : true;

    // 1. Heading Typography
    $default_heading_key = $is_bn ? 'shurjo' : 'system_sans';
    $heading_family_key  = get_theme_mod('ht_font_heading_family', $default_heading_key);
    $heading_weight      = get_theme_mod('ht_font_heading_weight', '700');
    $heading_lh          = get_theme_mod('ht_font_heading_lh', $is_bn ? '1.45' : '1.35');

    $font_map = [
        'shurjo'        => "'Shurjo', 'SolaimanLipi', Georgia, 'Times New Roman', serif",
        'solaimanlipi'  => "'SolaimanLipi', 'Noto Sans Bengali', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
        'hindsiliguri'  => "'Hind Siliguri', 'SolaimanLipi', sans-serif",
        'system_serif'  => "Georgia, 'Times New Roman', Times, serif",
        'system_sans'   => "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
    ];

    $heading_font = isset($font_map[$heading_family_key]) ? $font_map[$heading_family_key] : ($is_bn ? $font_map['shurjo'] : $font_map['system_sans']);

    // 2. Body Typography
    $default_body_key = $is_bn ? 'solaimanlipi' : 'system_sans';
    $body_family_key  = get_theme_mod('ht_font_body_family', $default_body_key);
    $body_size        = get_theme_mod('ht_font_body_size', '16px');
    $body_lh          = get_theme_mod('ht_font_body_lh', $is_bn ? '1.8' : '1.6');

    $body_font = isset($font_map[$body_family_key]) ? $font_map[$body_family_key] : ($is_bn ? $font_map['solaimanlipi'] : $font_map['system_sans']);

    // Generate clean inline CSS
    $css  = ":root {\n";
    $css .= "  --ht-font-heading: " . $heading_font . ";\n";
    $css .= "  --ht-font-serif: var(--ht-font-heading);\n";
    $css .= "  --ht-heading-weight: " . esc_attr($heading_weight) . ";\n";
    $css .= "  --ht-heading-line-height: " . esc_attr($heading_lh) . ";\n";
    $css .= "  --ht-font-body: " . $body_font . ";\n";
    $css .= "  --ht-font-bn: var(--ht-font-body);\n";
    $css .= "  --ht-font-sans: var(--ht-font-body);\n";
    $css .= "  --ht-body-font-size: " . esc_attr($body_size) . ";\n";
    $css .= "  --ht-body-line-height: " . esc_attr($body_lh) . ";\n";
    $css .= "}\n";

    // Locale-specific typography rules
    $css .= "html[lang=\"bn-BD\"], body.ht-lang-bn {\n";
    $css .= "  font-family: var(--ht-font-body);\n";
    $css .= "  line-height: var(--ht-body-line-height);\n";
    $css .= "  letter-spacing: normal !important;\n";
    $css .= "  text-rendering: optimizeLegibility;\n";
    $css .= "  -webkit-font-smoothing: antialiased;\n";
    $css .= "  -moz-osx-font-smoothing: grayscale;\n";
    $css .= "}\n";

    $css .= "html[lang=\"bn-BD\"] h1, html[lang=\"bn-BD\"] h2, html[lang=\"bn-BD\"] h3,\n";
    $css .= "html[lang=\"bn-BD\"] h4, html[lang=\"bn-BD\"] h5, html[lang=\"bn-BD\"] h6,\n";
    $css .= "body.ht-lang-bn h1, body.ht-lang-bn h2, body.ht-lang-bn h3,\n";
    $css .= "body.ht-lang-bn h4, body.ht-lang-bn h5, body.ht-lang-bn h6,\n";
    $css .= "body.ht-lang-bn .n-lead-title, body.ht-lang-bn .ht-card-title,\n";
    $css .= "body.ht-lang-bn .n-sec-head h3, body.ht-lang-bn .ht-article-title {\n";
    $css .= "  font-family: var(--ht-font-heading);\n";
    $css .= "  line-height: var(--ht-heading-line-height);\n";
    $css .= "  letter-spacing: normal !important;\n";
    $css .= "}\n";

    // Attach inline style to enqueued stylesheets
    if (wp_style_is('ht-main', 'enqueued')) {
        wp_add_inline_style('ht-main', $css);
    } elseif (wp_style_is('ht-main-style', 'enqueued')) {
        wp_add_inline_style('ht-main-style', $css);
    } else {
        echo "<style id=\"ht-dynamic-typography-css\">\n" . $css . "</style>\n";
    }
}
add_action('wp_enqueue_scripts', 'ht_customizer_dynamic_css', 100);
