<?php
/**
 * WordPress Theme Customizer Configuration
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}

if (!function_exists('htbd_edu_customize_register')) {
    /**
     * Add postMessage support for site title and description for the Theme Customizer.
     *
     * @param WP_Customize_Manager $wp_customize Theme Customizer object.
     */
    function htbd_edu_customize_register($wp_customize) {
        // Add Section for Homepage Modules
        $wp_customize->add_section('htbd_homepage_sections', array(
            'title'    => esc_html__('হোমপেজ মডিউল ও সেটিংস', 'helptrickbd-edu'),
            'priority' => 30,
        ));

        // Ticker Enable Toggle
        $wp_customize->add_setting('htbd_show_ticker', array(
            'default'           => true,
            'sanitize_callback' => 'wp_validate_boolean',
        ));
        $wp_customize->add_control('htbd_show_ticker', array(
            'label'    => esc_html__('ব্রেকিং নোটিশ টিকার প্রদর্শন করুন', 'helptrickbd-edu'),
            'section'  => 'htbd_homepage_sections',
            'type'     => 'checkbox',
        ));

        // Social CTA Bar Enable Toggle
        $wp_customize->add_setting('htbd_show_social_cta', array(
            'default'           => true,
            'sanitize_callback' => 'wp_validate_boolean',
        ));
        $wp_customize->add_control('htbd_show_social_cta', array(
            'label'    => esc_html__('টেলিগ্রাম/হোয়াটসঅ্যাপ সিএমটিএ বার প্রদর্শন করুন', 'helptrickbd-edu'),
            'section'  => 'htbd_homepage_sections',
            'type'     => 'checkbox',
        ));

        // Official Social Links Section
        $wp_customize->add_section('htbd_social_links', array(
            'title'    => esc_html__('অফিসিয়াল সোশ্যাল লিংক', 'helptrickbd-edu'),
            'priority' => 35,
        ));

        // Telegram Channel URL
        $wp_customize->add_setting('htbd_telegram_url', array(
            'default'           => 'https://t.me/helptrickbd_official',
            'sanitize_callback' => 'esc_url_raw',
        ));
        $wp_customize->add_control('htbd_telegram_url', array(
            'label'    => esc_html__('টেলিগ্রাম চ্যানেল লিংক', 'helptrickbd-edu'),
            'section'  => 'htbd_social_links',
            'type'     => 'url',
        ));

        // WhatsApp Channel URL
        $wp_customize->add_setting('htbd_whatsapp_url', array(
            'default'           => 'https://whatsapp.com/channel/0029Vb956jgCHDyrx1wkUh2a',
            'sanitize_callback' => 'esc_url_raw',
        ));
        $wp_customize->add_control('htbd_whatsapp_url', array(
            'label'    => esc_html__('হোয়াটসঅ্যাপ চ্যানেল লিংক', 'helptrickbd-edu'),
            'section'  => 'htbd_social_links',
            'type'     => 'url',
        ));
    }
}
add_action('customize_register', 'htbd_edu_customize_register');
