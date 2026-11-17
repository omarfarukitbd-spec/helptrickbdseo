<?php
/**
 * WordPress Customizer: Sidebar Modules
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Register Sidebar settings.
 *
 * @param WP_Customize_Manager $wp_customize Customizer manager.
 */
function ht_customize_register_sidebar($wp_customize) {
    // =============================================================
    // Section: Sidebar Modules
    // =============================================================
    $wp_customize->add_section('ht_sidebar_section', [
        'title'    => esc_html__('Sidebar Modules', 'helptrickbd'),
        'panel'    => 'ht_main_panel',
        'priority' => 16,
    ]);

    // Sidebar Popular Posts
    $wp_customize->add_setting('ht_sidebar_popular_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_sidebar_popular_enable', [
        'label'       => esc_html__('Enable Popular Posts & Handnotes Widget', 'helptrickbd'),
        'description' => esc_html__('Displays top viewed posts with numbered ranking badges and circular thumbnails.', 'helptrickbd'),
        'section'     => 'ht_sidebar_section',
        'type'        => 'checkbox',
    ]);

    $wp_customize->add_setting('ht_sidebar_popular_title', [
        'default'           => esc_html__('Trending Handnotes', 'helptrickbd'),
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('ht_sidebar_popular_title', [
        'label'   => esc_html__('Popular Posts Section Title', 'helptrickbd'),
        'section' => 'ht_sidebar_section',
        'type'    => 'text',
    ]);

    $wp_customize->add_setting('ht_sidebar_popular_count', [
        'default'           => 5,
        'sanitize_callback' => 'absint',
    ]);
    $wp_customize->add_control('ht_sidebar_popular_count', [
        'label'       => esc_html__('Number of Popular Posts (3 to 10)', 'helptrickbd'),
        'section'     => 'ht_sidebar_section',
        'type'        => 'number',
        'input_attrs' => ['min' => 3, 'max' => 10, 'step' => 1],
    ]);

    // Sidebar Sticky Ad Toggle
    $wp_customize->add_setting('ht_sidebar_ad_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_sidebar_ad_enable', [
        'label'   => esc_html__('Display Sticky AdSlot in Sidebar', 'helptrickbd'),
        'section' => 'ht_sidebar_section',
        'type'    => 'checkbox',
    ]);

    // Dynamic WordPress Widgets Area Toggle (Appearance > Widgets)
    $wp_customize->add_setting('ht_sidebar_widgets_enable', [
        'default'           => false,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_sidebar_widgets_enable', [
        'label'       => esc_html__('Enable Additional Custom Widgets in Sidebar', 'helptrickbd'),
        'description' => esc_html__('Display widgets configured under Appearance > Widgets. (Default: Hidden)', 'helptrickbd'),
        'section'     => 'ht_sidebar_section',
        'type'        => 'checkbox',
    ]);
}
add_action('customize_register', 'ht_customize_register_sidebar', 16);
