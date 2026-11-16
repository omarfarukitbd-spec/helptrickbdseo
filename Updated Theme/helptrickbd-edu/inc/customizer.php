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
     * Registers panels, sections, settings, and controls for the Theme Customizer.
     *
     * @param WP_Customize_Manager $wp_customize Theme Customizer object.
     */
    function htbd_edu_customize_register($wp_customize) {

        // =========================================================================
        // 1. SITE IDENTITY PANEL (Logo & Tagline)
        // =========================================================================
        $wp_customize->add_panel('htbd_panel_site_identity', array(
            'title'       => esc_html__('সাইট পরিচিতি ও ব্র্যান্ডিং', 'helptrickbd-edu'),
            'description' => esc_html__('লোগো ও সাইট ট্যাগলাইন সেটিংস', 'helptrickbd-edu'),
            'priority'    => 20,
        ));

        $wp_customize->add_section('htbd_section_site_identity', array(
            'title'       => esc_html__('লোগো ও ব্র্যান্ডিং অপশন', 'helptrickbd-edu'),
            'panel'       => 'htbd_panel_site_identity',
            'priority'    => 10,
        ));

        // Custom Logo Setting
        $wp_customize->add_setting('htbd_custom_logo', array(
            'default'           => '',
            'sanitize_callback' => 'esc_url_raw',
        ));
        $wp_customize->add_control(new WP_Customize_Image_Control($wp_customize, 'htbd_custom_logo', array(
            'label'       => esc_html__('কাস্টম হেডার লোগো', 'helptrickbd-edu'),
            'section'     => 'htbd_section_site_identity',
            'description' => esc_html__('ওয়েবসাইটের প্রধান হেডারের জন্য লোগো আপলোড করুন।', 'helptrickbd-edu'),
        )));

        // Site Tagline Setting
        $wp_customize->add_setting('htbd_site_tagline', array(
            'default'           => esc_html__('শিক্ষা ও প্রযুক্তির নির্ভরযোগ্য পোর্টাল', 'helptrickbd-edu'),
            'sanitize_callback' => 'sanitize_text_field',
        ));
        $wp_customize->add_control('htbd_site_tagline', array(
            'label'       => esc_html__('সাইট ট্যাগলাইন', 'helptrickbd-edu'),
            'section'     => 'htbd_section_site_identity',
            'type'        => 'text',
        ));

        // =========================================================================
        // 2. COLORS PANEL (Primary, Accent, Text Colors)
        // =========================================================================
        $wp_customize->add_panel('htbd_panel_colors', array(
            'title'       => esc_html__('কালার ও থিম প্যালেট', 'helptrickbd-edu'),
            'description' => esc_html__('থিমের প্রধান রং, অ্যাকসেন্ট রং এবং টেক্সট কালার নির্ধারণ করুন।', 'helptrickbd-edu'),
            'priority'    => 25,
        ));

        $wp_customize->add_section('htbd_section_colors', array(
            'title'       => esc_html__('থিম কালার অপশন', 'helptrickbd-edu'),
            'panel'       => 'htbd_panel_colors',
            'priority'    => 10,
        ));

        // Primary Color
        $wp_customize->add_setting('htbd_primary_color', array(
            'default'           => '#1a56db',
            'sanitize_callback' => 'sanitize_hex_color',
        ));
        $wp_customize->add_control(new WP_Customize_Color_Control($wp_customize, 'htbd_primary_color', array(
            'label'       => esc_html__('প্রধান কালার (Primary Color)', 'helptrickbd-edu'),
            'section'     => 'htbd_section_colors',
        )));

        // Accent Color
        $wp_customize->add_setting('htbd_accent_color', array(
            'default'           => '#d97706',
            'sanitize_callback' => 'sanitize_hex_color',
        ));
        $wp_customize->add_control(new WP_Customize_Color_Control($wp_customize, 'htbd_accent_color', array(
            'label'       => esc_html__('অ্যাকসেন্ট কালার (Accent Color)', 'helptrickbd-edu'),
            'section'     => 'htbd_section_colors',
        )));

        // Text Color
        $wp_customize->add_setting('htbd_text_color', array(
            'default'           => '#1f2937',
            'sanitize_callback' => 'sanitize_hex_color',
        ));
        $wp_customize->add_control(new WP_Customize_Color_Control($wp_customize, 'htbd_text_color', array(
            'label'       => esc_html__('বডি টেক্সট কালার (Text Color)', 'helptrickbd-edu'),
            'section'     => 'htbd_section_colors',
        )));

        // =========================================================================
        // 3. TYPOGRAPHY PANEL (Font Size Base & Font Family)
        // =========================================================================
        $wp_customize->add_panel('htbd_panel_typography', array(
            'title'       => esc_html__('টাইপোগ্রাফি ও ফন্ট সেটিংস', 'helptrickbd-edu'),
            'description' => esc_html__('বেস ফন্ট সাইজ এবং হেডিং ফন্ট নির্বাচন করুন।', 'helptrickbd-edu'),
            'priority'    => 28,
        ));

        $wp_customize->add_section('htbd_section_typography', array(
            'title'       => esc_html__('ফন্ট সাইজ ও টাইপোগ্রাফি', 'helptrickbd-edu'),
            'panel'       => 'htbd_panel_typography',
            'priority'    => 10,
        ));

        // Base Font Size
        $wp_customize->add_setting('htbd_font_size_base', array(
            'default'           => '16px',
            'sanitize_callback' => 'sanitize_text_field',
        ));
        $wp_customize->add_control('htbd_font_size_base', array(
            'label'       => esc_html__('বেস ফন্ট সাইজ (Base Font Size)', 'helptrickbd-edu'),
            'section'     => 'htbd_section_typography',
            'type'        => 'select',
            'choices'     => array(
                '14px' => esc_html__('১৪ পিক্সেল (ছোট)', 'helptrickbd-edu'),
                '15px' => esc_html__('১৫ পিক্সেল', 'helptrickbd-edu'),
                '16px' => esc_html__('১৬ পিক্সেল (আদর্শ)', 'helptrickbd-edu'),
                '17px' => esc_html__('১৭ পিক্সেল', 'helptrickbd-edu'),
                '18px' => esc_html__('১৮ পিক্সেল (বড়)', 'helptrickbd-edu'),
            ),
        ));

        // Heading Font Family
        $wp_customize->add_setting('htbd_font_heading', array(
            'default'           => 'SolaimanLipi',
            'sanitize_callback' => 'sanitize_text_field',
        ));
        $wp_customize->add_control('htbd_font_heading', array(
            'label'       => esc_html__('হেডিং ফন্ট ফ্যামিলি', 'helptrickbd-edu'),
            'section'     => 'htbd_section_typography',
            'type'        => 'select',
            'choices'     => array(
                'SolaimanLipi'       => 'SolaimanLipi (প্রস্তাবিত)',
                'Hind Siliguri'      => 'Hind Siliguri',
                'Noto Serif Bengali' => 'Noto Serif Bengali',
            ),
        ));

        // =========================================================================
        // 4. SOCIAL LINKS PANEL (Facebook, YouTube, Telegram, WhatsApp)
        // =========================================================================
        $wp_customize->add_panel('htbd_panel_social', array(
            'title'       => esc_html__('সোশ্যাল মিডিয়া চ্যানেল', 'helptrickbd-edu'),
            'description' => esc_html__('অফিসিয়াল সোশ্যাল মিডিয়া পেজ ও চ্যানেল লিংকসমূহ।', 'helptrickbd-edu'),
            'priority'    => 35,
        ));

        $wp_customize->add_section('htbd_section_social', array(
            'title'       => esc_html__('অফিসিয়াল সোশ্যাল লিংক', 'helptrickbd-edu'),
            'panel'       => 'htbd_panel_social',
            'priority'    => 10,
        ));

        // Facebook URL
        $wp_customize->add_setting('htbd_facebook_url', array(
            'default'           => 'https://facebook.com/helptrickbd',
            'sanitize_callback' => 'esc_url_raw',
        ));
        $wp_customize->add_control('htbd_facebook_url', array(
            'label'       => esc_html__('ফেসবুক পেজ লিংক', 'helptrickbd-edu'),
            'section'     => 'htbd_section_social',
            'type'        => 'url',
        ));

        // YouTube URL
        $wp_customize->add_setting('htbd_youtube_url', array(
            'default'           => 'https://www.youtube.com/@helptrickbd',
            'sanitize_callback' => 'esc_url_raw',
        ));
        $wp_customize->add_control('htbd_youtube_url', array(
            'label'       => esc_html__('ইউটিউব চ্যানেল লিংক', 'helptrickbd-edu'),
            'section'     => 'htbd_section_social',
            'type'        => 'url',
        ));

        // Telegram Channel URL
        $wp_customize->add_setting('htbd_telegram_url', array(
            'default'           => 'https://t.me/helptrickbd_official',
            'sanitize_callback' => 'esc_url_raw',
        ));
        $wp_customize->add_control('htbd_telegram_url', array(
            'label'       => esc_html__('টেলিগ্রাম চ্যানেল লিংক', 'helptrickbd-edu'),
            'section'     => 'htbd_section_social',
            'type'        => 'url',
        ));

        // WhatsApp Channel URL
        $wp_customize->add_setting('htbd_whatsapp_url', array(
            'default'           => 'https://whatsapp.com/channel/0029Vb956jgCHDyrx1wkUh2a',
            'sanitize_callback' => 'esc_url_raw',
        ));
        $wp_customize->add_control('htbd_whatsapp_url', array(
            'label'       => esc_html__('হোয়াটসঅ্যাপ চ্যানেল লিংক', 'helptrickbd-edu'),
            'section'     => 'htbd_section_social',
            'type'        => 'url',
        ));

        // =========================================================================
        // 5. FOOTER PANEL (Copyright Text & Footer Columns)
        // =========================================================================
        $wp_customize->add_panel('htbd_panel_footer', array(
            'title'       => esc_html__('ফুটার সেটিংস ও কাস্টমাইজেশন', 'helptrickbd-edu'),
            'description' => esc_html__('ফুটার কপিরাইট টেক্সট এবং কলাম সংখ্যা নির্ধারণ করুন।', 'helptrickbd-edu'),
            'priority'    => 40,
        ));

        $wp_customize->add_section('htbd_section_footer', array(
            'title'       => esc_html__('ফুটার লেআউট ও কপিরাইট', 'helptrickbd-edu'),
            'panel'       => 'htbd_panel_footer',
            'priority'    => 10,
        ));

        // Copyright Text
        $wp_customize->add_setting('htbd_footer_copyright', array(
            'default'           => '© ২০২৬ HelpTrickBD. সর্বস্বত্ব সংরক্ষিত।',
            'sanitize_callback' => 'wp_kses_post',
        ));
        $wp_customize->add_control('htbd_footer_copyright', array(
            'label'       => esc_html__('কপিরাইট নোটিশ টেক্সট', 'helptrickbd-edu'),
            'section'     => 'htbd_section_footer',
            'type'        => 'textarea',
        ));

        // Footer Columns
        $wp_customize->add_setting('htbd_footer_columns', array(
            'default'           => '3',
            'sanitize_callback' => 'sanitize_text_field',
        ));
        $wp_customize->add_control('htbd_footer_columns', array(
            'label'       => esc_html__('ফুটার কলাম সংখ্যা', 'helptrickbd-edu'),
            'section'     => 'htbd_section_footer',
            'type'        => 'select',
            'choices'     => array(
                '1' => esc_html__('১ কলাম', 'helptrickbd-edu'),
                '2' => esc_html__('২ কলাম', 'helptrickbd-edu'),
                '3' => esc_html__('৩ কলাম (স্ট্যান্ডার্ড)', 'helptrickbd-edu'),
                '4' => esc_html__('৪ কলাম', 'helptrickbd-edu'),
            ),
        ));

        // =========================================================================
        // 6. AD CODES PANEL (Header Ad, In-feed Ad, Single Post Ad)
        // =========================================================================
        $wp_customize->add_panel('htbd_panel_ad_codes', array(
            'title'       => esc_html__('বিজ্ঞাপন ও অ্যাড স্লট', 'helptrickbd-edu'),
            'description' => esc_html__('হেডার অ্যাড, ইনফীড অ্যাড এবং সিঙ্গেল পোস্ট বিজ্ঞাপনের কোড।', 'helptrickbd-edu'),
            'priority'    => 45,
        ));

        $wp_customize->add_section('htbd_section_ad_codes', array(
            'title'       => esc_html__('বিজ্ঞাপন কোড কনফিগারেশন', 'helptrickbd-edu'),
            'panel'       => 'htbd_panel_ad_codes',
            'priority'    => 10,
        ));

        // Header Ad Code
        $wp_customize->add_setting('htbd_header_ad_code', array(
            'default'           => '',
            'sanitize_callback' => 'htbd_sanitize_ad_code',
        ));
        $wp_customize->add_control('htbd_header_ad_code', array(
            'label'       => esc_html__('হেডার ব্যানার অ্যাড কোড (728x90)', 'helptrickbd-edu'),
            'description' => esc_html__('হেডারের নিচে প্রদর্শিত বিজ্ঞাপনের HTML/JavaScript কোড দিন।', 'helptrickbd-edu'),
            'section'     => 'htbd_section_ad_codes',
            'type'        => 'textarea',
        ));

        // In-feed Ad Code
        $wp_customize->add_setting('htbd_infeed_ad_code', array(
            'default'           => '',
            'sanitize_callback' => 'htbd_sanitize_ad_code',
        ));
        $wp_customize->add_control('htbd_infeed_ad_code', array(
            'label'       => esc_html__('ইন-ফিড অ্যাড কোড (In-Feed Ad)', 'helptrickbd-edu'),
            'description' => esc_html__('হোমপেজ বা আর্কাইভ গ্রিডের মাঝে প্রদর্শিত বিজ্ঞাপনের কোড।', 'helptrickbd-edu'),
            'section'     => 'htbd_section_ad_codes',
            'type'        => 'textarea',
        ));

        // Single Post Ad Code
        $wp_customize->add_setting('htbd_single_post_ad_code', array(
            'default'           => '',
            'sanitize_callback' => 'htbd_sanitize_ad_code',
        ));
        $wp_customize->add_control('htbd_single_post_ad_code', array(
            'label'       => esc_html__('সিঙ্গেল আর্টিকেল অ্যাড কোড', 'helptrickbd-edu'),
            'description' => esc_html__('আর্টিকেল বডির মাঝে বা শেষে প্রদর্শিত বিজ্ঞাপনের কোড।', 'helptrickbd-edu'),
            'section'     => 'htbd_section_ad_codes',
            'type'        => 'textarea',
        ));

        // =========================================================================
        // 7. HOMEPAGE MASTER SECTIONS PANEL (Full Admin Panel Customizability)
        // =========================================================================
        $cat_choices = array('0' => esc_html__('— সকল ক্যাটাগরি (Latest Posts) —', 'helptrickbd-edu'));
        $all_cats    = get_categories(array('hide_empty' => false));
        if (!empty($all_cats) && !is_wp_error($all_cats)) {
            foreach ($all_cats as $c) {
                $cat_choices[$c->term_id] = esc_html($c->name) . ' (' . $c->count . ')';
            }
        }

        $wp_customize->add_panel('htbd_panel_homepage', array(
            'title'       => esc_html__('হোমপেজ ও সেকশন কাস্টমাইজেশন', 'helptrickbd-edu'),
            'description' => esc_html__('হোমপেজের প্রতিটি সেকশনের নাম, ক্যাটাগরি, পোস্ট সংখ্যা ও দৃশ্যমানতা নিয়ন্ত্রণ করুন।', 'helptrickbd-edu'),
            'priority'    => 30,
        ));

        // --- 7.1 Ticker Section ---
        $wp_customize->add_section('htbd_sec_ctrl_ticker', array(
            'title'    => esc_html__('১. ব্রেকিং নোটিশ টিকার', 'helptrickbd-edu'),
            'panel'    => 'htbd_panel_homepage',
            'priority' => 10,
        ));
        $wp_customize->add_setting('htbd_show_ticker', array('default' => true, 'sanitize_callback' => 'wp_validate_boolean'));
        $wp_customize->add_control('htbd_show_ticker', array('label' => esc_html__('টিকার প্রদর্শন করুন', 'helptrickbd-edu'), 'section' => 'htbd_sec_ctrl_ticker', 'type' => 'checkbox'));
        $wp_customize->add_setting('htbd_ticker_badge_text', array('default' => 'সর্বশেষ', 'sanitize_callback' => 'sanitize_text_field'));
        $wp_customize->add_control('htbd_ticker_badge_text', array('label' => esc_html__('টিকার ব্যাজ টেক্সট', 'helptrickbd-edu'), 'section' => 'htbd_sec_ctrl_ticker', 'type' => 'text'));
        $wp_customize->add_setting('htbd_ticker_count', array('default' => 5, 'sanitize_callback' => 'absint'));
        $wp_customize->add_control('htbd_ticker_count', array('label' => esc_html__('প্রদর্শিত পোস্ট সংখ্যা', 'helptrickbd-edu'), 'section' => 'htbd_sec_ctrl_ticker', 'type' => 'number'));
        $wp_customize->add_setting('htbd_ticker_category', array('default' => 0, 'sanitize_callback' => 'absint'));
        $wp_customize->add_control('htbd_ticker_category', array('label' => esc_html__('ক্যাটাগরি ফিল্টার', 'helptrickbd-edu'), 'section' => 'htbd_sec_ctrl_ticker', 'type' => 'select', 'choices' => $cat_choices));

        // --- 7.2 Navbar Section ---
        $wp_customize->add_section('htbd_sec_ctrl_nav', array(
            'title'    => esc_html__('২. প্রধান মেনু ও ন্যাভিগেশন বার', 'helptrickbd-edu'),
            'panel'    => 'htbd_panel_homepage',
            'priority' => 15,
        ));
        $wp_customize->add_setting('htbd_nav_home_text', array('default' => 'All Posts', 'sanitize_callback' => 'sanitize_text_field'));
        $wp_customize->add_control('htbd_nav_home_text', array('label' => esc_html__('প্রথম ট্যাবের নাম (হোম)', 'helptrickbd-edu'), 'section' => 'htbd_sec_ctrl_nav', 'type' => 'text'));

        // --- 7.3 Lead Hero Section ---
        $wp_customize->add_section('htbd_sec_ctrl_hero', array(
            'title'    => esc_html__('৩. ম্যাগাজিন লিড হিরো স্টোরি', 'helptrickbd-edu'),
            'panel'    => 'htbd_panel_homepage',
            'priority' => 20,
        ));
        $wp_customize->add_setting('htbd_show_lead_hero', array('default' => true, 'sanitize_callback' => 'wp_validate_boolean'));
        $wp_customize->add_control('htbd_show_lead_hero', array('label' => esc_html__('লিড হিরো সেকশন প্রদর্শন করুন', 'helptrickbd-edu'), 'section' => 'htbd_sec_ctrl_hero', 'type' => 'checkbox'));
        $wp_customize->add_setting('htbd_hero_badge_text', array('default' => 'সর্বশেষ পোস্ট', 'sanitize_callback' => 'sanitize_text_field'));
        $wp_customize->add_control('htbd_hero_badge_text', array('label' => esc_html__('হিরো স্টোরি ব্যাজ টেক্সট', 'helptrickbd-edu'), 'section' => 'htbd_sec_ctrl_hero', 'type' => 'text'));
        $wp_customize->add_setting('htbd_hero_category', array('default' => 0, 'sanitize_callback' => 'absint'));
        $wp_customize->add_control('htbd_hero_category', array('label' => esc_html__('হিরো সেকশন ক্যাটাগরি', 'helptrickbd-edu'), 'section' => 'htbd_sec_ctrl_hero', 'type' => 'select', 'choices' => $cat_choices));

        // --- 7.4 SSC / Dakhil Section ---
        $wp_customize->add_section('htbd_sec_ctrl_ssc', array(
            'title'    => esc_html__('৪. এসএসসি / দাখিল সেকশন', 'helptrickbd-edu'),
            'panel'    => 'htbd_panel_homepage',
            'priority' => 25,
        ));
        $wp_customize->add_setting('htbd_show_sec_ssc', array('default' => true, 'sanitize_callback' => 'wp_validate_boolean'));
        $wp_customize->add_control('htbd_show_sec_ssc', array('label' => esc_html__('এই সেকশন প্রদর্শন করুন', 'helptrickbd-edu'), 'section' => 'htbd_sec_ctrl_ssc', 'type' => 'checkbox'));
        $wp_customize->add_setting('htbd_sec_ssc_title', array('default' => 'এসএসসি / দাখিল', 'sanitize_callback' => 'sanitize_text_field'));
        $wp_customize->add_control('htbd_sec_ssc_title', array('label' => esc_html__('সেকশন শিরোনাম', 'helptrickbd-edu'), 'section' => 'htbd_sec_ctrl_ssc', 'type' => 'text'));
        $wp_customize->add_setting('htbd_sec_ssc_category', array('default' => 0, 'sanitize_callback' => 'absint'));
        $wp_customize->add_control('htbd_sec_ssc_category', array('label' => esc_html__('ক্যাটাগরি নির্বাচন', 'helptrickbd-edu'), 'section' => 'htbd_sec_ctrl_ssc', 'type' => 'select', 'choices' => $cat_choices));
        $wp_customize->add_setting('htbd_sec_ssc_count', array('default' => 5, 'sanitize_callback' => 'absint'));
        $wp_customize->add_control('htbd_sec_ssc_count', array('label' => esc_html__('পোস্ট সংখ্যা', 'helptrickbd-edu'), 'section' => 'htbd_sec_ctrl_ssc', 'type' => 'number'));
        $wp_customize->add_setting('htbd_sec_ssc_link_text', array('default' => 'সব লেখা →', 'sanitize_callback' => 'sanitize_text_field'));
        $wp_customize->add_control('htbd_sec_ssc_link_text', array('label' => esc_html__('ভিউ অল লিংক টেক্সট', 'helptrickbd-edu'), 'section' => 'htbd_sec_ctrl_ssc', 'type' => 'text'));

        // --- 7.5 Filter Rows Section ---
        $wp_customize->add_section('htbd_sec_ctrl_filter', array(
            'title'    => esc_html__('৫. দ্রুত রিভিশন ও বিষয়ভিত্তিক ডাইজেস্ট', 'helptrickbd-edu'),
            'panel'    => 'htbd_panel_homepage',
            'priority' => 30,
        ));
        $wp_customize->add_setting('htbd_show_sec_filter', array('default' => true, 'sanitize_callback' => 'wp_validate_boolean'));
        $wp_customize->add_control('htbd_show_sec_filter', array('label' => esc_html__('ফিল্টার ডাইজেস্ট সেকশন প্রদর্শন করুন', 'helptrickbd-edu'), 'section' => 'htbd_sec_ctrl_filter', 'type' => 'checkbox'));
        $wp_customize->add_setting('htbd_sec_filter_title', array('default' => 'দ্রুত রিভিশন ও বিষয়ভিত্তিক ডাইজেস্ট', 'sanitize_callback' => 'sanitize_text_field'));
        $wp_customize->add_control('htbd_sec_filter_title', array('label' => esc_html__('সেকশন শিরোনাম', 'helptrickbd-edu'), 'section' => 'htbd_sec_ctrl_filter', 'type' => 'text'));
        $wp_customize->add_setting('htbd_sec_filter_count', array('default' => 12, 'sanitize_callback' => 'absint'));
        $wp_customize->add_control('htbd_sec_filter_count', array('label' => esc_html__('সর্বোচ্চ পোস্ট সংখ্যা', 'helptrickbd-edu'), 'section' => 'htbd_sec_ctrl_filter', 'type' => 'number'));
        $wp_customize->add_setting('htbd_sec_filter_link_text', array('default' => 'সব লেখা →', 'sanitize_callback' => 'sanitize_text_field'));
        $wp_customize->add_control('htbd_sec_filter_link_text', array('label' => esc_html__('লিংক টেক্সট', 'helptrickbd-edu'), 'section' => 'htbd_sec_ctrl_filter', 'type' => 'text'));

        // --- 7.6 National University & Special Focus ---
        $wp_customize->add_section('htbd_sec_ctrl_nu', array(
            'title'    => esc_html__('৬. জাতীয় বিশ্ববিদ্যালয় ও উচ্চশিক্ষা', 'helptrickbd-edu'),
            'panel'    => 'htbd_panel_homepage',
            'priority' => 35,
        ));
        $wp_customize->add_setting('htbd_show_sec_nu', array('default' => true, 'sanitize_callback' => 'wp_validate_boolean'));
        $wp_customize->add_control('htbd_show_sec_nu', array('label' => esc_html__('এই সেকশন প্রদর্শন করুন', 'helptrickbd-edu'), 'section' => 'htbd_sec_ctrl_nu', 'type' => 'checkbox'));
        $wp_customize->add_setting('htbd_sec_nu_title', array('default' => 'জাতীয় বিশ্ববিদ্যালয় ও উচ্চশিক্ষা', 'sanitize_callback' => 'sanitize_text_field'));
        $wp_customize->add_control('htbd_sec_nu_title', array('label' => esc_html__('সেকশন শিরোনাম', 'helptrickbd-edu'), 'section' => 'htbd_sec_ctrl_nu', 'type' => 'text'));
        $wp_customize->add_setting('htbd_sec_nu_category', array('default' => 0, 'sanitize_callback' => 'absint'));
        $wp_customize->add_control('htbd_sec_nu_category', array('label' => esc_html__('ক্যাটাগরি নির্বাচন', 'helptrickbd-edu'), 'section' => 'htbd_sec_ctrl_nu', 'type' => 'select', 'choices' => $cat_choices));
        $wp_customize->add_setting('htbd_sec_nu_count', array('default' => 6, 'sanitize_callback' => 'absint'));
        $wp_customize->add_control('htbd_sec_nu_count', array('label' => esc_html__('পোস্ট সংখ্যা', 'helptrickbd-edu'), 'section' => 'htbd_sec_ctrl_nu', 'type' => 'number'));
        $wp_customize->add_setting('htbd_sec_nu_link_text', array('default' => 'সব হ্যান্ডনোট →', 'sanitize_callback' => 'sanitize_text_field'));
        $wp_customize->add_control('htbd_sec_nu_link_text', array('label' => esc_html__('লিংক টেক্সট', 'helptrickbd-edu'), 'section' => 'htbd_sec_nu', 'type' => 'text'));

        // --- 7.7 Photo Guides & Gallery ---
        $wp_customize->add_section('htbd_sec_ctrl_gallery', array(
            'title'    => esc_html__('৭. পরীক্ষা প্রস্তুতি ও সচিত্র গাইড', 'helptrickbd-edu'),
            'panel'    => 'htbd_panel_homepage',
            'priority' => 40,
        ));
        $wp_customize->add_setting('htbd_show_sec_gallery', array('default' => true, 'sanitize_callback' => 'wp_validate_boolean'));
        $wp_customize->add_control('htbd_show_sec_gallery', array('label' => esc_html__('সচিত্র গাইড সেকশন প্রদর্শন করুন', 'helptrickbd-edu'), 'section' => 'htbd_sec_ctrl_gallery', 'type' => 'checkbox'));
        $wp_customize->add_setting('htbd_sec_gallery_title', array('default' => 'পরীক্ষা প্রস্তুতি ও সচিত্র গাইড', 'sanitize_callback' => 'sanitize_text_field'));
        $wp_customize->add_control('htbd_sec_gallery_title', array('label' => esc_html__('সেকশন শিরোনাম', 'helptrickbd-edu'), 'section' => 'htbd_sec_ctrl_gallery', 'type' => 'text'));
        $wp_customize->add_setting('htbd_sec_gallery_category', array('default' => 0, 'sanitize_callback' => 'absint'));
        $wp_customize->add_control('htbd_sec_gallery_category', array('label' => esc_html__('ক্যাটাগরি নির্বাচন', 'helptrickbd-edu'), 'section' => 'htbd_sec_ctrl_gallery', 'type' => 'select', 'choices' => $cat_choices));
        $wp_customize->add_setting('htbd_sec_gallery_count', array('default' => 4, 'sanitize_callback' => 'absint'));
        $wp_customize->add_control('htbd_sec_gallery_count', array('label' => esc_html__('পোস্ট সংখ্যা', 'helptrickbd-edu'), 'section' => 'htbd_sec_ctrl_gallery', 'type' => 'number'));
        $wp_customize->add_setting('htbd_sec_gallery_link_text', array('default' => 'সকল গ্যালারি →', 'sanitize_callback' => 'sanitize_text_field'));
        $wp_customize->add_control('htbd_sec_gallery_link_text', array('label' => esc_html__('লিংক টেক্সট', 'helptrickbd-edu'), 'section' => 'htbd_sec_ctrl_gallery', 'type' => 'text'));

        // --- 7.8 Trust Deck & Countdown ---
        $wp_customize->add_section('htbd_sec_ctrl_trust', array(
            'title'    => esc_html__('৮. ট্রাস্ট ডেক ও পরীক্ষার কাউন্টডাউন', 'helptrickbd-edu'),
            'panel'    => 'htbd_panel_homepage',
            'priority' => 45,
        ));
        $wp_customize->add_setting('htbd_show_sec_trust', array('default' => true, 'sanitize_callback' => 'wp_validate_boolean'));
        $wp_customize->add_control('htbd_show_sec_trust', array('label' => esc_html__('ট্রাস্ট ডেক প্রদর্শন করুন', 'helptrickbd-edu'), 'section' => 'htbd_sec_ctrl_trust', 'type' => 'checkbox'));
        $wp_customize->add_setting('htbd_exam_date_ssc', array('default' => '2027-02-01T09:00:00', 'sanitize_callback' => 'sanitize_text_field'));
        $wp_customize->add_control('htbd_exam_date_ssc', array('label' => esc_html__('এসএসসি পরীক্ষার তারিখ (ISO ফরম্যাট)', 'helptrickbd-edu'), 'description' => esc_html__('যেমন: 2027-02-01T09:00:00', 'helptrickbd-edu'), 'section' => 'htbd_sec_ctrl_trust', 'type' => 'text'));
    }
}
add_action('customize_register', 'htbd_edu_customize_register');

if (!function_exists('htbd_sanitize_ad_code')) {
    /**
     * Sanitizes raw ad script/html code.
     * Allows scripts and iframes for Google AdSense and ad networks if user has unfiltered_html capability.
     *
     * @param string $content Raw ad HTML/JS code.
     * @return string Sanitized code.
     */
    function htbd_sanitize_ad_code($content) {
        if (current_user_can('unfiltered_html')) {
            return $content;
        }
        return wp_kses_post($content);
    }
}
