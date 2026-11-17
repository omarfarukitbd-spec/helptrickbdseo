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
    // 1. Heading Typography
    $heading_family_key = get_theme_mod('ht_font_heading_family', 'shurjo');
    $heading_weight     = get_theme_mod('ht_font_heading_weight', '700');
    $heading_lh         = get_theme_mod('ht_font_heading_lh', '1.35');

    $font_map = [
        'shurjo'        => "'Shurjo', 'SolaimanLipi', Georgia, 'Times New Roman', serif",
        'solaimanlipi'  => "'SolaimanLipi', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
        'hindsiliguri'  => "'Hind Siliguri', 'SolaimanLipi', sans-serif",
        'system_serif'  => "Georgia, 'Times New Roman', Times, serif",
        'system_sans'   => "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
    ];

    $heading_font = isset($font_map[$heading_family_key]) ? $font_map[$heading_family_key] : $font_map['shurjo'];

    // 2. Body Typography
    $body_family_key = get_theme_mod('ht_font_body_family', 'solaimanlipi');
    $body_size       = get_theme_mod('ht_font_body_size', '16px');
    $body_lh         = get_theme_mod('ht_font_body_lh', '1.8');

    $body_font = isset($font_map[$body_family_key]) ? $font_map[$body_family_key] : $font_map['solaimanlipi'];

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

    // Attach inline style to ht-main-style if enqueued, else fallback to print in head
    if (wp_style_is('ht-main-style', 'enqueued')) {
        wp_add_inline_style('ht-main-style', $css);
    } else {
        echo "<style id=\"ht-dynamic-typography-css\">\n" . $css . "</style>\n";
    }
}
add_action('wp_enqueue_scripts', 'ht_customizer_dynamic_css', 100);
