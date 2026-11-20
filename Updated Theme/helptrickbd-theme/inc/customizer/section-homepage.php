<?php
/**
 * WordPress Customizer: Homepage Sections & Educational Hubs
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Register Homepage Sections settings.
 *
 * @param WP_Customize_Manager $wp_customize Customizer manager.
 */
function ht_customize_register_homepage($wp_customize) {
    $cat_choices = ['0' => esc_html__('— ডিফল্ট / সর্বশেষ পোস্ট —', 'helptrickbd')];
    $all_cats    = get_categories(['hide_empty' => false]);
    if (!empty($all_cats) && !is_wp_error($all_cats)) {
        foreach ($all_cats as $c) {
            $cat_choices[$c->term_id] = esc_html($c->name) . ' (' . $c->count . ')';
        }
    }

    $wp_customize->add_section('ht_homepage_sections', [
        'title'    => esc_html__('Homepage Sections & Educational Hubs', 'helptrickbd'),
        'panel'    => 'ht_main_panel',
        'priority' => 14,
    ]);

    // 1. Ticker Settings
    $wp_customize->add_setting('htbd_show_ticker', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('htbd_show_ticker', [
        'label'   => esc_html__('Enable Notice Marquee Ticker', 'helptrickbd'),
        'section' => 'ht_homepage_sections',
        'type'    => 'checkbox',
    ]);

    $wp_customize->add_setting('htbd_ticker_badge_text', [
        'default'           => 'তাজা আপডেট',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('htbd_ticker_badge_text', [
        'label'   => esc_html__('Notice Ticker Badge Text', 'helptrickbd'),
        'section' => 'ht_homepage_sections',
        'type'    => 'text',
    ]);

    $wp_customize->add_setting('htbd_ticker_count', [
        'default'           => 5,
        'sanitize_callback' => 'absint',
    ]);
    $wp_customize->add_control('htbd_ticker_count', [
        'label'   => esc_html__('Number of Ticker Notices', 'helptrickbd'),
        'section' => 'ht_homepage_sections',
        'type'    => 'number',
    ]);

    // 2. Magazine Lead Hero Story & Spotlights
    $wp_customize->add_setting('htbd_show_lead_hero', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('htbd_show_lead_hero', [
        'label'   => esc_html__('Enable Magazine Lead Hero Story & Spotlights', 'helptrickbd'),
        'section' => 'ht_homepage_sections',
        'type'    => 'checkbox',
    ]);

    $wp_customize->add_setting('htbd_hero_badge_text', [
        'default'           => 'সর্বশেষ প্রকাশনা',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('htbd_hero_badge_text', [
        'label'   => esc_html__('Lead Hero Kicker Badge Text', 'helptrickbd'),
        'section' => 'ht_homepage_sections',
        'type'    => 'text',
    ]);

    // 3. SSC & Dakhil Examination Hub
    $wp_customize->add_setting('htbd_show_sec_ssc', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('htbd_show_sec_ssc', [
        'label'   => esc_html__('Enable SSC & Dakhil Hub Section', 'helptrickbd'),
        'section' => 'ht_homepage_sections',
        'type'    => 'checkbox',
    ]);

    $wp_customize->add_setting('htbd_sec_ssc_title', [
        'default'           => 'এসএসসি ও দাখিল',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('htbd_sec_ssc_title', [
        'label'   => esc_html__('SSC Hub Heading', 'helptrickbd'),
        'section' => 'ht_homepage_sections',
        'type'    => 'text',
    ]);

    $wp_customize->add_setting('htbd_sec_ssc_link_text', [
        'default'           => 'সব দেখুন →',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('htbd_sec_ssc_link_text', [
        'label'   => esc_html__('SSC Hub Link Text', 'helptrickbd'),
        'section' => 'ht_homepage_sections',
        'type'    => 'text',
    ]);

    // 4. Subject Filter Rows Section
    $wp_customize->add_setting('htbd_show_sec_filter', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('htbd_show_sec_filter', [
        'label'   => esc_html__('Enable Subject Filterable Posts Section', 'helptrickbd'),
        'section' => 'ht_homepage_sections',
        'type'    => 'checkbox',
    ]);

    $wp_customize->add_setting('htbd_sec_filter_title', [
        'default'           => 'বিষয়ভিত্তিক গাইড',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('htbd_sec_filter_title', [
        'label'   => esc_html__('Subject Filter Section Title', 'helptrickbd'),
        'section' => 'ht_homepage_sections',
        'type'    => 'text',
    ]);

    $wp_customize->add_setting('htbd_sec_filter_link_text', [
        'default'           => 'সব দেখুন →',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('htbd_sec_filter_link_text', [
        'label'   => esc_html__('Subject Filter Link Text', 'helptrickbd'),
        'section' => 'ht_homepage_sections',
        'type'    => 'text',
    ]);

    // 5. National University & Higher Studies Section
    $wp_customize->add_setting('htbd_show_sec_nu', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('htbd_show_sec_nu', [
        'label'   => esc_html__('Enable National University & Higher Studies Section', 'helptrickbd'),
        'section' => 'ht_homepage_sections',
        'type'    => 'checkbox',
    ]);

    $wp_customize->add_setting('htbd_sec_nu_title', [
        'default'           => 'জাতীয় বিশ্ববিদ্যালয়',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('htbd_sec_nu_title', [
        'label'   => esc_html__('National University Section Title', 'helptrickbd'),
        'section' => 'ht_homepage_sections',
        'type'    => 'text',
    ]);

    $wp_customize->add_setting('htbd_sec_nu_category', [
        'default'           => 0,
        'sanitize_callback' => 'absint',
    ]);
    $wp_customize->add_control('htbd_sec_nu_category', [
        'label'   => esc_html__('Select Category for NU Section', 'helptrickbd'),
        'section' => 'ht_homepage_sections',
        'type'    => 'select',
        'choices' => $cat_choices,
    ]);

    $wp_customize->add_setting('htbd_sec_nu_count', [
        'default'           => 6,
        'sanitize_callback' => 'absint',
    ]);
    $wp_customize->add_control('htbd_sec_nu_count', [
        'label'   => esc_html__('Number of Posts for NU Section', 'helptrickbd'),
        'section' => 'ht_homepage_sections',
        'type'    => 'number',
    ]);

    $wp_customize->add_setting('htbd_sec_nu_link_text', [
        'default'           => 'সব দেখুন →',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('htbd_sec_nu_link_text', [
        'label'   => esc_html__('NU Section Link Text', 'helptrickbd'),
        'section' => 'ht_homepage_sections',
        'type'    => 'text',
    ]);

    // 6. Photo Guides & Gallery Section
    $wp_customize->add_setting('htbd_show_sec_gallery', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('htbd_show_sec_gallery', [
        'label'   => esc_html__('Enable Photo Guides & Gallery Section', 'helptrickbd'),
        'section' => 'ht_homepage_sections',
        'type'    => 'checkbox',
    ]);

    $wp_customize->add_setting('htbd_sec_gallery_title', [
        'default'           => 'সচিত্র স্টাডি গাইড',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('htbd_sec_gallery_title', [
        'label'   => esc_html__('Photo Guides Section Title', 'helptrickbd'),
        'section' => 'ht_homepage_sections',
        'type'    => 'text',
    ]);

    $wp_customize->add_setting('htbd_sec_gallery_category', [
        'default'           => 0,
        'sanitize_callback' => 'absint',
    ]);
    $wp_customize->add_control('htbd_sec_gallery_category', [
        'label'   => esc_html__('Select Category for Photo Guides', 'helptrickbd'),
        'section' => 'ht_homepage_sections',
        'type'    => 'select',
        'choices' => $cat_choices,
    ]);

    $wp_customize->add_setting('htbd_sec_gallery_count', [
        'default'           => 4,
        'sanitize_callback' => 'absint',
    ]);
    $wp_customize->add_control('htbd_sec_gallery_count', [
        'label'   => esc_html__('Number of Posts for Photo Guides', 'helptrickbd'),
        'section' => 'ht_homepage_sections',
        'type'    => 'number',
    ]);

    $wp_customize->add_setting('htbd_sec_gallery_link_text', [
        'default'           => 'সব দেখুন →',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('htbd_sec_gallery_link_text', [
        'label'   => esc_html__('Photo Guides Link Text', 'helptrickbd'),
        'section' => 'ht_homepage_sections',
        'type'    => 'text',
    ]);
}
add_action('customize_register', 'ht_customize_register_homepage', 14);
