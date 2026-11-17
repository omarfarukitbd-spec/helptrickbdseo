<?php
/**
 * WordPress Customizer: Footer & Copyright Section
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Register Footer settings.
 *
 * @param WP_Customize_Manager $wp_customize Customizer manager.
 */
function ht_customize_register_footer($wp_customize) {
    // =============================================================
    // Section: Footer & Copyright
    // =============================================================
    $wp_customize->add_section('ht_footer_section', [
        'title'    => esc_html__('Footer & Copyright', 'helptrickbd'),
        'panel'    => 'ht_main_panel',
        'priority' => 25,
    ]);

    // Footer Description
    $wp_customize->add_setting('ht_footer_desc', [
        'default'           => esc_html__('HelpTrickBD is a trusted educational portal providing National University routines, SSC/Dakhil suggestions, BCS preparation, Political Science handnotes, and modern ICT guides for students.', 'helptrickbd'),
        'sanitize_callback' => 'sanitize_textarea_field',
    ]);
    $wp_customize->add_control('ht_footer_desc', [
        'label'   => esc_html__('Footer Brand About Description', 'helptrickbd'),
        'section' => 'ht_footer_section',
        'type'    => 'textarea',
    ]);

    // Footer Trust Text
    $wp_customize->add_setting('ht_footer_trust_text', [
        'default'           => esc_html__('100% Authentic Information & Expert-Reviewed Content', 'helptrickbd'),
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('ht_footer_trust_text', [
        'label'   => esc_html__('Footer Trust Badge Text', 'helptrickbd'),
        'section' => 'ht_footer_section',
        'type'    => 'text',
    ]);

    // Footer Copyright
    $wp_customize->add_setting('ht_footer_copyright', [
        'default'           => '',
        'sanitize_callback' => 'sanitize_text_field',
        'transport'         => 'postMessage',
    ]);
    $wp_customize->add_control('ht_footer_copyright', [
        'label'       => esc_html__('Custom Copyright Notice (Leave blank for automatic current year)', 'helptrickbd'),
        'section'     => 'ht_footer_section',
        'type'        => 'text',
    ]);

    // Footer Credit
    $wp_customize->add_setting('ht_footer_credit', [
        'default'           => esc_html__('Built for educational excellence and open knowledge', 'helptrickbd'),
        'sanitize_callback' => 'sanitize_text_field',
        'transport'         => 'postMessage',
    ]);
    $wp_customize->add_control('ht_footer_credit', [
        'label'   => esc_html__('Footer Credit Line', 'helptrickbd'),
        'section' => 'ht_footer_section',
        'type'    => 'text',
    ]);

    // Back to top button
    $wp_customize->add_setting('ht_back_to_top_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_back_to_top_enable', [
        'label'   => esc_html__('Enable Circular Scroll-to-Top Button', 'helptrickbd'),
        'section' => 'ht_footer_section',
        'type'    => 'checkbox',
    ]);

    // Mobile dock
    $wp_customize->add_setting('ht_mobile_dock_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_mobile_dock_enable', [
        'label'   => esc_html__('Enable Mobile Bottom Navigation Dock', 'helptrickbd'),
        'section' => 'ht_footer_section',
        'type'    => 'checkbox',
    ]);
}
add_action('customize_register', 'ht_customize_register_footer', 25);
