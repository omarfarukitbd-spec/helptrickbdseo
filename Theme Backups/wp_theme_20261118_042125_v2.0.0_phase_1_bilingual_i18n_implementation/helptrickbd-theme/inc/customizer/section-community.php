<?php
/**
 * WordPress Customizer: Social & Community Links
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Register Social & Community settings.
 *
 * @param WP_Customize_Manager $wp_customize Customizer manager.
 */
function ht_customize_register_community($wp_customize) {
    // =============================================================
    // Section: Social & Community Links
    // =============================================================
    $wp_customize->add_section('ht_community_section', [
        'title'    => esc_html__('Social & Community Links', 'helptrickbd'),
        'panel'    => 'ht_main_panel',
        'priority' => 20,
    ]);

    $wp_customize->add_setting('ht_whatsapp_url', [
        'default'           => 'https://whatsapp.com/channel/0029Vb956jgCHDyrx1wkUh2a',
        'sanitize_callback' => 'esc_url_raw',
    ]);
    $wp_customize->add_control('ht_whatsapp_url', [
        'label'       => esc_html__('WhatsApp Channel URL', 'helptrickbd'),
        'description' => esc_html__('Official WhatsApp channel link for students.', 'helptrickbd'),
        'section'     => 'ht_community_section',
        'type'        => 'url',
    ]);

    $wp_customize->add_setting('ht_telegram_url', [
        'default'           => 'https://t.me/helptrickbd_official',
        'sanitize_callback' => 'esc_url_raw',
    ]);
    $wp_customize->add_control('ht_telegram_url', [
        'label'       => esc_html__('Telegram Channel URL', 'helptrickbd'),
        'section'     => 'ht_community_section',
        'type'        => 'url',
    ]);

    $wp_customize->add_setting('ht_facebook_url', [
        'default'           => 'https://facebook.com/helptrickbd',
        'sanitize_callback' => 'esc_url_raw',
    ]);
    $wp_customize->add_control('ht_facebook_url', [
        'label'   => esc_html__('Facebook Page URL', 'helptrickbd'),
        'section' => 'ht_community_section',
        'type'    => 'url',
    ]);

    $wp_customize->add_setting('ht_youtube_url', [
        'default'           => 'https://www.youtube.com/@helptrickbd',
        'sanitize_callback' => 'esc_url_raw',
    ]);
    $wp_customize->add_control('ht_youtube_url', [
        'label'   => esc_html__('YouTube Channel URL', 'helptrickbd'),
        'section' => 'ht_community_section',
        'type'    => 'url',
    ]);

    $wp_customize->add_setting('ht_twitter_url', [
        'default'           => '',
        'sanitize_callback' => 'esc_url_raw',
    ]);
    $wp_customize->add_control('ht_twitter_url', [
        'label'   => esc_html__('X (Twitter) Profile URL', 'helptrickbd'),
        'section' => 'ht_community_section',
        'type'    => 'url',
    ]);

    $wp_customize->add_setting('ht_contact_email', [
        'default'           => 'contact@helptrickbd.com',
        'sanitize_callback' => 'sanitize_email',
    ]);
    $wp_customize->add_control('ht_contact_email', [
        'label'   => esc_html__('Support & Contact Email', 'helptrickbd'),
        'section' => 'ht_community_section',
        'type'    => 'text',
    ]);
}
add_action('customize_register', 'ht_customize_register_community', 20);
