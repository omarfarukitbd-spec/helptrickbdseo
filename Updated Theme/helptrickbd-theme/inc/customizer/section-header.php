<?php
/**
 * WordPress Customizer: Header & Navigation Section
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Register Header & Navigation settings.
 *
 * @param WP_Customize_Manager $wp_customize Customizer manager.
 */
function ht_customize_register_header($wp_customize) {
    // =============================================================
    // Section 1: Header & Navigation
    // =============================================================
    $wp_customize->add_section('ht_header_section', [
        'title'    => esc_html__('Header & Navigation', 'helptrickbd'),
        'panel'    => 'ht_main_panel',
        'priority' => 10,
    ]);

    // Search Trigger in Header
    $wp_customize->add_setting('ht_header_search_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_header_search_enable', [
        'label'   => esc_html__('Show Instant Search Button (Ctrl+K) in Header', 'helptrickbd'),
        'section' => 'ht_header_section',
        'type'    => 'checkbox',
    ]);

    // Bookmarks Trigger in Header
    $wp_customize->add_setting('ht_header_bookmarks_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_header_bookmarks_enable', [
        'label'   => esc_html__('Show Reading List (Bookmarks) Button in Header', 'helptrickbd'),
        'section' => 'ht_header_section',
        'type'    => 'checkbox',
    ]);

    // Theme Switcher in Header
    $wp_customize->add_setting('ht_header_theme_toggle_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_header_theme_toggle_enable', [
        'label'   => esc_html__('Show Dark/Light Mode Switcher in Header', 'helptrickbd'),
        'section' => 'ht_header_section',
        'type'    => 'checkbox',
    ]);
}
add_action('customize_register', 'ht_customize_register_header', 12);
