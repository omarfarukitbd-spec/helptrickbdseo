<?php
/**
 * WordPress Customizer Settings for HelpTrickBD Pro
 * Complete theme customizer suite: Header & Menu, Sidebar, Footer, Social, Study Tools & AdSense.
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Register Customizer settings and controls.
 *
 * @param WP_Customize_Manager $wp_customize Customizer manager.
 */
function ht_customize_register($wp_customize) {
    // -------------------------------------------------------------
    // Main Panel: HelpTrickBD Pro Settings
    // -------------------------------------------------------------
    $wp_customize->add_panel('ht_main_panel', [
        'title'       => 'HelpTrickBD Pro সেটিংস',
        'description' => 'থিমের মেনুবার, সাইডবার, ফুটার, সোশ্যাল লিংক, স্টুডেন্ট টুলস ও এডসেন্স কাস্টমাইজেশন',
        'priority'    => 25,
    ]);

    // =============================================================
    // Section 1: হেডার ও মেনুবার সেটিংস
    // =============================================================
    $wp_customize->add_section('ht_header_section', [
        'title'    => 'হেডার ও মেনুবার সেটিংস',
        'panel'    => 'ht_main_panel',
        'priority' => 10,
    ]);

    // Ticker Toggle
    $wp_customize->add_setting('ht_ticker_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_ticker_enable', [
        'label'   => 'টপবার জরুরি বিজ্ঞপ্তি (Ticker) চালু রাখুন',
        'section' => 'ht_header_section',
        'type'    => 'checkbox',
    ]);

    // Ticker Text
    $wp_customize->add_setting('ht_ticker_text', [
        'default'           => 'জাতীয় বিশ্ববিদ্যালয় অনার্স ২য় বর্ষ পরীক্ষার রুটিন ও পরীক্ষার গাইড ২০২৬ প্রকাশিত',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('ht_ticker_text', [
        'label'   => 'জরুরি বিজ্ঞপ্তির টেক্সট',
        'section' => 'ht_header_section',
        'type'    => 'text',
    ]);

    // Ticker Link
    $wp_customize->add_setting('ht_ticker_link', [
        'default'           => '',
        'sanitize_callback' => 'esc_url_raw',
    ]);
    $wp_customize->add_control('ht_ticker_link', [
        'label'   => 'বিজ্ঞপ্তির লিংক (ঐচ্ছিক)',
        'section' => 'ht_header_section',
        'type'    => 'url',
    ]);

    // Header Countdown Toggle
    $wp_customize->add_setting('ht_countdown_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_countdown_enable', [
        'label'   => 'হেডারে পরীক্ষার দিন গণনা (Countdown) প্রদর্শন করুন',
        'section' => 'ht_header_section',
        'type'    => 'checkbox',
    ]);

    // Exam countdown title
    $wp_customize->add_setting('ht_countdown_title', [
        'default'           => 'অনার্স ২য় বর্ষ পরীক্ষা ২০২৬',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('ht_countdown_title', [
        'label'   => 'আসন্ন পরীক্ষার নাম / শিরোনাম',
        'section' => 'ht_header_section',
        'type'    => 'text',
    ]);

    // Exam countdown date
    $wp_customize->add_setting('ht_countdown_date', [
        'default'           => '2026-11-20',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('ht_countdown_date', [
        'label'       => 'পরীক্ষার তারিখ (YYYY-MM-DD)',
        'description' => 'ফরম্যাট: 2026-11-20',
        'section'     => 'ht_header_section',
        'type'        => 'date',
    ]);

    // Search Trigger in Header
    $wp_customize->add_setting('ht_header_search_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_header_search_enable', [
        'label'   => 'হেডারে লাইভ সার্চ বাটন (Ctrl+K) প্রদর্শন করুন',
        'section' => 'ht_header_section',
        'type'    => 'checkbox',
    ]);

    // Bookmarks Trigger in Header
    $wp_customize->add_setting('ht_header_bookmarks_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_header_bookmarks_enable', [
        'label'   => 'হেডারে বুকমার্ক (পড়ার তালিকা) বাটন প্রদর্শন করুন',
        'section' => 'ht_header_section',
        'type'    => 'checkbox',
    ]);

    // Theme Switcher in Header
    $wp_customize->add_setting('ht_header_theme_toggle_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_header_theme_toggle_enable', [
        'label'   => 'হেডারে ডার্ক/লাইট মোড সুইচ প্রদর্শন করুন',
        'section' => 'ht_header_section',
        'type'    => 'checkbox',
    ]);

    // =============================================================
    // Section 2: সাইডবার সেটিংস
    // =============================================================
    $wp_customize->add_section('ht_sidebar_section', [
        'title'    => 'সাইডবার মডিউল সেটিংস',
        'panel'    => 'ht_main_panel',
        'priority' => 15,
    ]);

    // Sidebar Top Live Search
    $wp_customize->add_setting('ht_sidebar_search_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_sidebar_search_enable', [
        'label'       => 'সাইডবারের সর্ব উপরে লাইভ সার্চ বক্স চালু রাখুন',
        'description' => 'ইনস্ট্যান্ট AJAX সাজেশন সহ প্রিমিয়াম সার্চ বক্স',
        'section'     => 'ht_sidebar_section',
        'type'        => 'checkbox',
    ]);

    $wp_customize->add_setting('ht_sidebar_search_title', [
        'default'           => 'অনুসন্ধান করুন',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('ht_sidebar_search_title', [
        'label'   => 'সার্চ বক্সের শিরোনাম',
        'section' => 'ht_sidebar_section',
        'type'    => 'text',
    ]);

    $wp_customize->add_setting('ht_sidebar_search_placeholder', [
        'default'           => 'হ্যান্ডনোট, সাজেশন বা বিষয় খুঁজুন...',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('ht_sidebar_search_placeholder', [
        'label'   => 'সার্চ ফিল্ডের প্লেসহোল্ডার টেক্সট',
        'section' => 'ht_sidebar_section',
        'type'    => 'text',
    ]);

    // Sidebar Countdown Widget
    $wp_customize->add_setting('ht_sidebar_countdown_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_sidebar_countdown_enable', [
        'label'   => 'সাইডবারে পরীক্ষার দিন গণনা কার্ড প্রদর্শন করুন',
        'section' => 'ht_sidebar_section',
        'type'    => 'checkbox',
    ]);

    // Sidebar Popular Posts
    $wp_customize->add_setting('ht_sidebar_popular_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_sidebar_popular_enable', [
        'label'       => 'জনপ্রিয় পোস্ট ও হ্যান্ডনোট সেকশন চালু রাখুন',
        'description' => 'র‍্যাঙ্ক নম্বর ব্যাজ ও সার্কুলার থাম্বনেইল সহ কম্প্যাক্ট ডিজাইন',
        'section'     => 'ht_sidebar_section',
        'type'        => 'checkbox',
    ]);

    $wp_customize->add_setting('ht_sidebar_popular_title', [
        'default'           => 'জনপ্রিয় পোস্ট ও হ্যান্ডনোট',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('ht_sidebar_popular_title', [
        'label'   => 'জনপ্রিয় পোস্ট সেকশনের শিরোনাম',
        'section' => 'ht_sidebar_section',
        'type'    => 'text',
    ]);

    $wp_customize->add_setting('ht_sidebar_popular_count', [
        'default'           => 5,
        'sanitize_callback' => 'absint',
    ]);
    $wp_customize->add_control('ht_sidebar_popular_count', [
        'label'       => 'জনপ্রিয় পোস্টের সংখ্যা (৩ থেকে ১০)',
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
        'label'   => 'সাইডবারে স্টিকি এডসেন্স স্লট প্রদর্শন করুন',
        'section' => 'ht_sidebar_section',
        'type'    => 'checkbox',
    ]);

    // Sidebar Categories
    $wp_customize->add_setting('ht_sidebar_categories_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_sidebar_categories_enable', [
        'label'       => 'সকল বিষয়শ্রেণী (ক্যাটাগরি) কার্ড সেকশন চালু রাখুন',
        'description' => 'প্রাসঙ্গিক ভেক্টর আইকন ও সর্ব ডানে পরিসংখ্যান ব্যাজ সহ',
        'section'     => 'ht_sidebar_section',
        'type'        => 'checkbox',
    ]);

    $wp_customize->add_setting('ht_sidebar_categories_title', [
        'default'           => 'সকল বিষয়শ্রেণী (ক্যাটাগরি)',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('ht_sidebar_categories_title', [
        'label'   => 'বিষয়শ্রেণী সেকশনের শিরোনাম',
        'section' => 'ht_sidebar_section',
        'type'    => 'text',
    ]);

    $wp_customize->add_setting('ht_sidebar_categories_count', [
        'default'           => 10,
        'sanitize_callback' => 'absint',
    ]);
    $wp_customize->add_control('ht_sidebar_categories_count', [
        'label'       => 'সর্বোচ্চ প্রদর্শিত ক্যাটাগরির সংখ্যা (৪ থেকে ২০)',
        'section'     => 'ht_sidebar_section',
        'type'        => 'number',
        'input_attrs' => ['min' => 4, 'max' => 20, 'step' => 1],
    ]);

    // =============================================================
    // Section 3: সোশ্যাল ও কমিউনিটি লিংক
    // =============================================================
    $wp_customize->add_section('ht_community_section', [
        'title'    => 'সোশ্যাল ও কমিউনিটি লিংক',
        'panel'    => 'ht_main_panel',
        'priority' => 20,
    ]);

    $wp_customize->add_setting('ht_whatsapp_url', [
        'default'           => 'https://chat.whatsapp.com/',
        'sanitize_callback' => 'esc_url_raw',
    ]);
    $wp_customize->add_control('ht_whatsapp_url', [
        'label'       => 'হোয়াটসঅ্যাপ গ্রুপ লিংক',
        'description' => 'শিক্ষার্থীরা এই লিংকে ক্লিক করে সরাসরি স্টাডি গ্রুপে যুক্ত হবে',
        'section'     => 'ht_community_section',
        'type'        => 'url',
    ]);

    $wp_customize->add_setting('ht_telegram_url', [
        'default'           => 'https://t.me/helptrickbd',
        'sanitize_callback' => 'esc_url_raw',
    ]);
    $wp_customize->add_control('ht_telegram_url', [
        'label'       => 'টেলিগ্রাম চ্যানেল / গ্রুপ লিংক',
        'section'     => 'ht_community_section',
        'type'        => 'url',
    ]);

    $wp_customize->add_setting('ht_facebook_url', [
        'default'           => 'https://facebook.com/helptrickbd',
        'sanitize_callback' => 'esc_url_raw',
    ]);
    $wp_customize->add_control('ht_facebook_url', [
        'label'   => 'ফেসবুক পেজ / গ্রুপ লিংক',
        'section' => 'ht_community_section',
        'type'    => 'url',
    ]);

    $wp_customize->add_setting('ht_youtube_url', [
        'default'           => 'https://youtube.com/@helptrickbd',
        'sanitize_callback' => 'esc_url_raw',
    ]);
    $wp_customize->add_control('ht_youtube_url', [
        'label'   => 'ইউটিউব চ্যানেল লিংক (ঐচ্ছিক)',
        'section' => 'ht_community_section',
        'type'    => 'url',
    ]);

    $wp_customize->add_setting('ht_twitter_url', [
        'default'           => '',
        'sanitize_callback' => 'esc_url_raw',
    ]);
    $wp_customize->add_control('ht_twitter_url', [
        'label'   => 'টুইটার / এক্স (X) প্রোফাইল লিংক',
        'section' => 'ht_community_section',
        'type'    => 'url',
    ]);

    $wp_customize->add_setting('ht_contact_email', [
        'default'           => 'contact@helptrickbd.com',
        'sanitize_callback' => 'sanitize_email',
    ]);
    $wp_customize->add_control('ht_contact_email', [
        'label'   => 'সাপোর্ট ও যোগাযোগ ইমেইল',
        'section' => 'ht_community_section',
        'type'    => 'text',
    ]);

    // =============================================================
    // Section 4: ফুটার ও কপিরাইট সেটিংস
    // =============================================================
    $wp_customize->add_section('ht_footer_section', [
        'title'    => 'ফুটার ও কপিরাইট সেটিংস',
        'panel'    => 'ht_main_panel',
        'priority' => 25,
    ]);

    // Pre-Footer Community Bar
    $wp_customize->add_setting('ht_pre_footer_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_pre_footer_enable', [
        'label'   => 'ফুটারের উপরের কমিউনিটি বার (WhatsApp/Telegram) চালু রাখুন',
        'section' => 'ht_footer_section',
        'type'    => 'checkbox',
    ]);

    $wp_customize->add_setting('ht_pre_footer_title', [
        'default'           => 'পরীক্ষার রুটিন ও স্পেশাল সাজেশন সবার আগে পেতে চান?',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('ht_pre_footer_title', [
        'label'   => 'কমিউনিটি বারের প্রধান শিরোনাম',
        'section' => 'ht_footer_section',
        'type'    => 'text',
    ]);

    $wp_customize->add_setting('ht_pre_footer_sub', [
        'default'           => 'আমাদের অফিসিয়াল হোয়াটসঅ্যাপ ও টেলিগ্রাম গ্রুপে যুক্ত হোন।',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('ht_pre_footer_sub', [
        'label'   => 'কমিউনিটি বারের সাব-টাইটেল',
        'section' => 'ht_footer_section',
        'type'    => 'text',
    ]);

    // Footer Description
    $wp_customize->add_setting('ht_footer_desc', [
        'default'           => 'Help Trick BD বাংলাদেশের শিক্ষার্থীদের জন্য জাতীয় বিশ্ববিদ্যালয়, এসএসসি/দাখিল, বিসিএস প্রস্তুতি, রাষ্ট্রবিজ্ঞান অ্যাকাডেমিক হ্যান্ডনোট এবং আধুনিক তথ্যপ্রযুক্তি নির্দেশিকার একটি নির্ভরযোগ্য শিক্ষা পোর্টাল।',
        'sanitize_callback' => 'sanitize_textarea_field',
    ]);
    $wp_customize->add_control('ht_footer_desc', [
        'label'   => 'ফুটার ব্র্যান্ড পরিচিতি বিবরণ',
        'section' => 'ht_footer_section',
        'type'    => 'textarea',
    ]);

    // Footer Trust Text
    $wp_customize->add_setting('ht_footer_trust_text', [
        'default'           => '১০০% প্রামাণ্য তথ্য ও শিক্ষক-পর্যালোচিত কন্টেন্ট',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('ht_footer_trust_text', [
        'label'   => 'ফুটার ট্রাস্ট ব্যাজ টেক্সট',
        'section' => 'ht_footer_section',
        'type'    => 'text',
    ]);

    // Footer Copyright
    $wp_customize->add_setting('ht_footer_copyright', [
        'default'           => '',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('ht_footer_copyright', [
        'label'       => 'কাস্টম কপিরাইট টেক্সট (ফাঁকা রাখলে স্বয়ংক্রিয় সাল সহ দেখাবে)',
        'section'     => 'ht_footer_section',
        'type'        => 'text',
    ]);

    // Footer Credit
    $wp_customize->add_setting('ht_footer_credit', [
        'default'           => 'নির্মিত হয়েছে শিক্ষা ও উন্মুক্ত জ্ঞানের প্রসারে',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('ht_footer_credit', [
        'label'   => 'ফুটার ক্রেডিট লাইন',
        'section' => 'ht_footer_section',
        'type'    => 'text',
    ]);

    // Back to top button
    $wp_customize->add_setting('ht_back_to_top_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_back_to_top_enable', [
        'label'   => 'সার্কুলার স্ক্রোল-টু-টপ বাটন চালু রাখুন',
        'section' => 'ht_footer_section',
        'type'    => 'checkbox',
    ]);

    // Mobile dock
    $wp_customize->add_setting('ht_mobile_dock_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_mobile_dock_enable', [
        'label'   => 'মোবাইল নিচের ফ্লোটিং নেভিগেশন ডক (Mobile Dock) চালু রাখুন',
        'section' => 'ht_footer_section',
        'type'    => 'checkbox',
    ]);

    // =============================================================
    // Section 5: সিঙ্গেল পোস্ট ও স্টাডি টুলস
    // =============================================================
    $wp_customize->add_section('ht_study_tools_section', [
        'title'    => 'সিঙ্গেল পোস্ট ও স্টাডি টুলস',
        'panel'    => 'ht_main_panel',
        'priority' => 30,
    ]);

    // Reading Progress Bar
    $wp_customize->add_setting('ht_reading_progress_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_reading_progress_enable', [
        'label'   => 'লাইভ রিডিং প্রগ্রেস বার (শীর্ষে নীল দাগ) চালু রাখুন',
        'section' => 'ht_study_tools_section',
        'type'    => 'checkbox',
    ]);

    // Font Resizer
    $wp_customize->add_setting('ht_font_resizer_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_font_resizer_enable', [
        'label'   => 'ফন্ট সাইজ পরিবর্তন টুল (A- / A / A+) চালু রাখুন',
        'section' => 'ht_study_tools_section',
        'type'    => 'checkbox',
    ]);

    // Focus Mode
    $wp_customize->add_setting('ht_focus_mode_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_focus_mode_enable', [
        'label'   => 'ফোকাস রিডিং মোড বাটন চালু রাখুন',
        'section' => 'ht_study_tools_section',
        'type'    => 'checkbox',
    ]);

    // Bookmark Button
    $wp_customize->add_setting('ht_bookmark_btn_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_bookmark_btn_enable', [
        'label'   => 'পড়ার তালিকায় রাখুন (বুকমার্ক) বাটন চালু রাখুন',
        'section' => 'ht_study_tools_section',
        'type'    => 'checkbox',
    ]);

    // 1-Click Print & PDF
    $wp_customize->add_setting('ht_print_btn_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_print_btn_enable', [
        'label'   => '১-ক্লিক প্রিন্ট / পিডিএফ সেভ বাটন চালু রাখুন',
        'section' => 'ht_study_tools_section',
        'type'    => 'checkbox',
    ]);

    // Auto TOC
    $wp_customize->add_setting('ht_toc_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_toc_enable', [
        'label'   => 'স্বয়ংক্রিয় সূচিপত্র (Table of Contents) চালু রাখুন',
        'section' => 'ht_study_tools_section',
        'type'    => 'checkbox',
    ]);

    // Post Community Box
    $wp_customize->add_setting('ht_post_community_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_post_community_enable', [
        'label'   => 'পোস্টের নিচে টেলিগ্রাম ও হোয়াটসঅ্যাপ কার্ড প্রদর্শন করুন',
        'section' => 'ht_study_tools_section',
        'type'    => 'checkbox',
    ]);

    // Academic Citation
    $wp_customize->add_setting('ht_citation_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_citation_enable', [
        'label'   => 'অ্যাকাডেমিক সাইটেশন কপি বক্স (APA 7th) চালু রাখুন',
        'section' => 'ht_study_tools_section',
        'type'    => 'checkbox',
    ]);

    // Related Posts
    $wp_customize->add_setting('ht_related_posts_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_related_posts_enable', [
        'label'   => 'পোস্টের নিচে সম্পর্কিত আর্টিকেল গ্রিড প্রদর্শন করুন',
        'section' => 'ht_study_tools_section',
        'type'    => 'checkbox',
    ]);

    // Reviewer Name
    $wp_customize->add_setting('ht_reviewer_name', [
        'default'           => 'ফারুক স্যার',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('ht_reviewer_name', [
        'label'       => 'ফ্যাক্ট-চেক পর্যালোচক শিক্ষকের নাম',
        'description' => 'পোস্টের শীর্ষ E-E-A-T ভেরিফাইড ব্যাজে প্রদর্শিত হবে',
        'section'     => 'ht_study_tools_section',
        'type'        => 'text',
    ]);

    // Download Timer
    $wp_customize->add_setting('ht_download_timer', [
        'default'           => 5,
        'sanitize_callback' => 'absint',
    ]);
    $wp_customize->add_control('ht_download_timer', [
        'label'       => 'পিডিএফ ডাউনলোড বাটনের কাউন্টডাউন সেকেন্ড',
        'description' => '৫ থেকে ১০ সেকেন্ডের মধ্যে রাখুন (ডিফল্ট: ৫)',
        'section'     => 'ht_study_tools_section',
        'type'        => 'number',
        'input_attrs' => ['min' => 1, 'max' => 30, 'step' => 1],
    ]);

    // =============================================================
    // Section 6: গুগল এডসেন্স বিজ্ঞাপন স্লট
    // =============================================================
    $wp_customize->add_section('ht_ads_section', [
        'title'    => 'গুগল এডসেন্স বিজ্ঞাপন স্লট',
        'panel'    => 'ht_main_panel',
        'priority' => 35,
    ]);

    $ad_slots = [
        'ht_ad_header'        => ['হেডার বিজ্ঞাপন (৭২৮×৯০ বা রেসপন্সিভ)', 'হেডারের নিচে প্রদর্শিত হবে'],
        'ht_ad_below_title'   => ['আর্টিকেল টাইটেলের নিচে বিজ্ঞাপন', 'পোস্ট টাইটেলের ঠিক নিচে প্রদর্শিত হবে'],
        'ht_ad_in_content'    => ['আর্টিকেলের মাঝখানে ইন-কন্টেন্ট বিজ্ঞাপন', 'প্যারাগ্রাফ ৩ বা ৪ এর পর স্বয়ংক্রিয়ভাবে প্রবেশ করবে'],
        'ht_ad_after_content' => ['আর্টিকেলের শেষে বিজ্ঞাপন', 'কনটেন্ট শেষ হওয়ার পর প্রদর্শিত হবে'],
        'ht_ad_sticky_sidebar'=> ['স্টিকি সাইডবার বিজ্ঞাপন (৩০০×৬০০ / ৩০০×২৫০)', 'ডেস্কটপ সাইডবারে ফিক্সড স্ক্রল হিসেবে থাকবে'],
        'ht_ad_auto_ads'      => ['গুগল অটো এডস (Auto Ads Script)', '<head> ট্যাগে যোগ করার জন্য'],
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
        'label'       => 'মার্জিত এডব্লকার রিকোয়েস্ট নোটিশ চালু রাখুন',
        'description' => 'এডব্লকার অন থাকা ভিজিটরদের হোয়াইটলিস্ট করার ভদ্র অনুরোধ প্রদর্শন করবে',
        'section'     => 'ht_ads_section',
        'type'        => 'checkbox',
    ]);
}
add_action('customize_register', 'ht_customize_register');

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
