<?php
/**
 * WordPress Customizer: Professional Typography Suite
 * Segregated into 2 Distinct Sections:
 * 1. Heading Typography (H1-H6, Section Titles & Article Headlines)
 * 2. Body Typography (Paragraphs, Content Body & Base Reading Font)
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Register Typography Sections and Controls.
 *
 * @param WP_Customize_Manager $wp_customize Customizer manager.
 */
function ht_customize_register_typography($wp_customize) {

    // =============================================================
    // Typography Section 1: Heading Fonts (H1-H6 & Section Titles)
    // =============================================================
    $wp_customize->add_section('ht_typography_heading_section', [
        'title'       => esc_html__('Typography: Heading Fonts (H1-H6)', 'helptrickbd'),
        'description' => esc_html__('Configure font family, font weight, and line height for all headings (H1-H6), article titles, and section headers across the entire website.', 'helptrickbd'),
        'panel'       => 'ht_main_panel',
        'priority'    => 8,
    ]);

    // Heading Font Family
    $wp_customize->add_setting('ht_font_heading_family', [
        'default'           => 'shurjo',
        'sanitize_callback' => 'sanitize_key',
    ]);
    $wp_customize->add_control('ht_font_heading_family', [
        'label'       => esc_html__('Heading Font Family', 'helptrickbd'),
        'description' => esc_html__('Select the font family for all headings and section titles.', 'helptrickbd'),
        'section'     => 'ht_typography_heading_section',
        'type'        => 'select',
        'choices'     => [
            'shurjo'        => esc_html__('Shurjo Serif (Newspaper Editorial - Default)', 'helptrickbd'),
            'solaimanlipi'  => esc_html__('SolaimanLipi (Standard Bengali Newspaper)', 'helptrickbd'),
            'hindsiliguri'  => esc_html__('Hind Siliguri (Modern Clean Sans)', 'helptrickbd'),
            'system_serif'  => esc_html__('System Serif (Georgia, Times)', 'helptrickbd'),
            'system_sans'   => esc_html__('System Sans-Serif (Modern Clean)', 'helptrickbd'),
        ],
    ]);

    // Heading Font Weight
    $wp_customize->add_setting('ht_font_heading_weight', [
        'default'           => '700',
        'sanitize_callback' => 'sanitize_key',
    ]);
    $wp_customize->add_control('ht_font_heading_weight', [
        'label'   => esc_html__('Heading Font Weight', 'helptrickbd'),
        'section' => 'ht_typography_heading_section',
        'type'    => 'select',
        'choices' => [
            '600' => esc_html__('Semi-Bold (600)', 'helptrickbd'),
            '700' => esc_html__('Bold (700) - Default', 'helptrickbd'),
            '800' => esc_html__('Extra Bold (800)', 'helptrickbd'),
        ],
    ]);

    // Heading Line Height
    $wp_customize->add_setting('ht_font_heading_lh', [
        'default'           => '1.35',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('ht_font_heading_lh', [
        'label'   => esc_html__('Heading Line Height Scale', 'helptrickbd'),
        'section' => 'ht_typography_heading_section',
        'type'    => 'select',
        'choices' => [
            '1.25' => esc_html__('Tight (1.25)', 'helptrickbd'),
            '1.35' => esc_html__('Balanced (1.35) - Default', 'helptrickbd'),
            '1.45' => esc_html__('Spacious (1.45)', 'helptrickbd'),
        ],
    ]);

    // =============================================================
    // Typography Section 2: Body & Reading Content Fonts
    // =============================================================
    $wp_customize->add_section('ht_typography_body_section', [
        'title'       => esc_html__('Typography: Body & Reading Content', 'helptrickbd'),
        'description' => esc_html__('Configure font family, font size, and line height for all paragraphs, long-form content, and general body text.', 'helptrickbd'),
        'panel'       => 'ht_main_panel',
        'priority'    => 9,
    ]);

    // Body Font Family
    $wp_customize->add_setting('ht_font_body_family', [
        'default'           => 'solaimanlipi',
        'sanitize_callback' => 'sanitize_key',
    ]);
    $wp_customize->add_control('ht_font_body_family', [
        'label'       => esc_html__('Body Font Family', 'helptrickbd'),
        'description' => esc_html__('Select the font family for all body copy, notes, and paragraphs.', 'helptrickbd'),
        'section'     => 'ht_typography_body_section',
        'type'        => 'select',
        'choices'     => [
            'solaimanlipi'  => esc_html__('SolaimanLipi (Newspaper Standard - Default)', 'helptrickbd'),
            'shurjo'        => esc_html__('Shurjo Serif (Literary Reading)', 'helptrickbd'),
            'hindsiliguri'  => esc_html__('Hind Siliguri (Clean Sans)', 'helptrickbd'),
            'system_sans'   => esc_html__('System Sans-Serif (-apple-system, BlinkMacSystemFont)', 'helptrickbd'),
        ],
    ]);

    // Base Body Font Size
    $wp_customize->add_setting('ht_font_body_size', [
        'default'           => '16px',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('ht_font_body_size', [
        'label'   => esc_html__('Base Body Font Size', 'helptrickbd'),
        'section' => 'ht_typography_body_section',
        'type'    => 'select',
        'choices' => [
            '15px' => esc_html__('Compact (15px)', 'helptrickbd'),
            '16px' => esc_html__('Standard (16px) - Default', 'helptrickbd'),
            '17px' => esc_html__('Enhanced (17px)', 'helptrickbd'),
            '18px' => esc_html__('Large & Accessible (18px)', 'helptrickbd'),
        ],
    ]);

    // Body Line Height
    $wp_customize->add_setting('ht_font_body_lh', [
        'default'           => '1.8',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('ht_font_body_lh', [
        'label'   => esc_html__('Body Line Height (Line Spacing)', 'helptrickbd'),
        'section' => 'ht_typography_body_section',
        'type'    => 'select',
        'choices' => [
            '1.7' => esc_html__('Standard (1.7)', 'helptrickbd'),
            '1.8' => esc_html__('Comfortable Reading (1.8) - Default', 'helptrickbd'),
            '1.9' => esc_html__('Spacious / Academic (1.9)', 'helptrickbd'),
        ],
    ]);
}
add_action('customize_register', 'ht_customize_register_typography', 10);
