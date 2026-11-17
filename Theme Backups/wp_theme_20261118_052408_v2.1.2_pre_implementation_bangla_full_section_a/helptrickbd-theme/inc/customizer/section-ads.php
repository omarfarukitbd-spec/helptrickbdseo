<?php
/**
 * WordPress Customizer: Google AdSense & Monetization Section
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Register AdSense & Monetization settings.
 *
 * @param WP_Customize_Manager $wp_customize Customizer manager.
 */
function ht_customize_register_ads($wp_customize) {
    // =============================================================
    // Section: Google AdSense & Monetization
    // =============================================================
    $wp_customize->add_section('ht_ads_section', [
        'title'    => esc_html__('Google AdSense & Monetization', 'helptrickbd'),
        'panel'    => 'ht_main_panel',
        'priority' => 35,
    ]);

    $ad_slots = [
        'ht_ad_header'        => [esc_html__('Header Ad (728x90 or Responsive)', 'helptrickbd'), esc_html__('Displayed directly below primary header', 'helptrickbd')],
        'ht_ad_below_title'   => [esc_html__('Below Post Title Ad', 'helptrickbd'), esc_html__('Displayed directly beneath article header', 'helptrickbd')],
        'ht_ad_in_content'    => [esc_html__('In-Content Ad', 'helptrickbd'), esc_html__('Automatically inserted after paragraphs 3 or 4', 'helptrickbd')],
        'ht_ad_after_content' => [esc_html__('After Post Content Ad', 'helptrickbd'), esc_html__('Displayed after post text concludes', 'helptrickbd')],
        'ht_ad_infeed_1'      => [esc_html__('Homepage In-Feed Ad Slot 1 (After Hero)', 'helptrickbd'), esc_html__('Responsive in-feed ad banner displayed between Hero and SSC hub', 'helptrickbd')],
        'ht_ad_infeed_2'      => [esc_html__('Homepage In-Feed Ad Slot 2 (After Subject Filter)', 'helptrickbd'), esc_html__('Responsive in-feed ad banner displayed between Subject Filter and Focus block', 'helptrickbd')],
        'ht_ad_sticky_sidebar'=> [esc_html__('Sticky Sidebar Ad (300x600 / 300x250)', 'helptrickbd'), esc_html__('Fixed desktop sidebar ad during scrolling', 'helptrickbd')],
        'ht_ad_auto_ads'      => [esc_html__('Google Auto Ads Script', 'helptrickbd'), esc_html__('Injected inside head element for Auto Ads', 'helptrickbd')],
    ];

    foreach ($ad_slots as $id => $data) {
        $wp_customize->add_setting($id, [
            'default'           => '',
            'sanitize_callback' => 'ht_sanitize_ad_code',
        ]);
        $wp_customize->add_control($id, [
            'label'       => $data[0],
            'description' => $data[1],
            'section'     => 'ht_ads_section',
            'type'        => 'textarea',
        ]);
    }

    // Polite AdBlocker Notice Toggle
    $wp_customize->add_setting('ht_adblock_notice_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_adblock_notice_enable', [
        'label'       => esc_html__('Enable Polite AdBlocker Notice', 'helptrickbd'),
        'description' => esc_html__('Politely asks visitors using ad blockers to whitelist the website.', 'helptrickbd'),
        'section'     => 'ht_ads_section',
        'type'        => 'checkbox',
    ]);
}
add_action('customize_register', 'ht_customize_register_ads', 35);
