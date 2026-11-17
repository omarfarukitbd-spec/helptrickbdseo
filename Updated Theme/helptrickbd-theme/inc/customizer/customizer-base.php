<?php
/**
 * WordPress Customizer Base: Master Panel & Sanitization Engine
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Register Master Panel and Core Settings.
 *
 * @param WP_Customize_Manager $wp_customize Customizer manager.
 */
function ht_customize_register_base($wp_customize) {
    // Enable selective refresh postMessage for Core settings
    if ($wp_customize->get_setting('blogname')) {
        $wp_customize->get_setting('blogname')->transport = 'postMessage';
    }
    if ($wp_customize->get_setting('blogdescription')) {
        $wp_customize->get_setting('blogdescription')->transport = 'postMessage';
    }

    // -------------------------------------------------------------
    // Main Panel: HelpTrickBD Pro Settings
    // -------------------------------------------------------------
    $wp_customize->add_panel('ht_main_panel', [
        'title'       => esc_html__('HelpTrickBD Theme Settings', 'helptrickbd'),
        'description' => esc_html__('Configure typography, header navigation, homepage hubs, sidebar modules, footer columns, study tools, social links, and Google AdSense slots.', 'helptrickbd'),
        'priority'    => 25,
    ]);
}
add_action('customize_register', 'ht_customize_register_base', 5);

/**
 * Custom sanitizer for AdSense code snippets.
 * Allows scripts and tags safely for administrators.
 *
 * @param string $input Input ad code.
 * @return string Sanitized code.
 */
function ht_sanitize_ad_code($input) {
    if (current_user_can('unfiltered_html')) {
        return $input;
    }
    return wp_kses_post($input);
}

/**
 * Enqueue scripts for Customizer Live Preview (postMessage).
 */
function ht_customize_preview_js() {
    wp_enqueue_script(
        'ht-customizer-preview',
        get_template_directory_uri() . '/assets/js/customizer-preview.js',
        ['customize-preview', 'jquery'],
        HT_THEME_VERSION,
        true
    );
}
add_action('customize_preview_init', 'ht_customize_preview_js');
