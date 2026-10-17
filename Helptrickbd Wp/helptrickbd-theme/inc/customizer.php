<?php
/**
 * WordPress Customizer Settings for HelpTrickBD Pro
 * Complete theme customizer suite: Header & Menu, Sidebar, Footer, Social, Study Tools & AdSense.
 * Global Standard English configuration.
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
    // Enable selective refresh postMessage for Core settings
    if ($wp_customize->get_setting('blogname')) {
        $wp_customize->get_setting('blogname')->transport = 'postMessage';
    }
    if ($wp_customize->get_setting('blogdescription')) {
        $wp_customize->get_setting('blogdescription')->transport = 'postMessage';
    }

    // -------------------------------------------------------------
    // Main Panel: HelpTrickBD Pro Settings
    // -------------------------------------------------------------
    $wp_customize->add_panel('ht_main_panel', [
        'title'       => esc_html__('HelpTrickBD Theme Settings', 'helptrickbd'),
        'description' => esc_html__('Configure header navigation, sidebar modules, footer columns, study tools, social links, and Google AdSense slots.', 'helptrickbd'),
        'priority'    => 25,
    ]);

    // =============================================================
    // Section 1: Header & Navigation
    // =============================================================
    $wp_customize->add_section('ht_header_section', [
        'title'    => esc_html__('Header & Navigation', 'helptrickbd'),
        'panel'    => 'ht_main_panel',
        'priority' => 10,
    ]);

    // Ticker Toggle
    $wp_customize->add_setting('ht_ticker_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_ticker_enable', [
        'label'   => esc_html__('Enable Topbar Breaking Notice Ticker', 'helptrickbd'),
        'section' => 'ht_header_section',
        'type'    => 'checkbox',
    ]);

    // Ticker Badge Label
    $wp_customize->add_setting('ht_ticker_badge_label', [
        'default'           => 'নোটিশ ও আপডেট',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('ht_ticker_badge_label', [
        'label'   => esc_html__('Notice Ticker Badge Label', 'helptrickbd'),
        'section' => 'ht_header_section',
        'type'    => 'text',
    ]);

    // Ticker Text
    $wp_customize->add_setting('ht_ticker_text', [
        'default'           => esc_html__('National University Honours 2nd Year Exam Routine & Guidelines 2026 Published', 'helptrickbd'),
        'sanitize_callback' => 'sanitize_text_field',
        'transport'         => 'postMessage',
    ]);
    $wp_customize->add_control('ht_ticker_text', [
        'label'   => esc_html__('Notice Ticker Text', 'helptrickbd'),
        'section' => 'ht_header_section',
        'type'    => 'text',
    ]);

    // Ticker Link
    $wp_customize->add_setting('ht_ticker_link', [
        'default'           => '',
        'sanitize_callback' => 'esc_url_raw',
    ]);
    $wp_customize->add_control('ht_ticker_link', [
        'label'   => esc_html__('Notice Target URL (Optional)', 'helptrickbd'),
        'section' => 'ht_header_section',
        'type'    => 'url',
    ]);

    // Header Countdown Toggle
    $wp_customize->add_setting('ht_countdown_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_countdown_enable', [
        'label'   => esc_html__('Display Exam Countdown in Header', 'helptrickbd'),
        'section' => 'ht_header_section',
        'type'    => 'checkbox',
    ]);

    // Exam countdown title
    $wp_customize->add_setting('ht_countdown_title', [
        'default'           => esc_html__('Honours 2nd Year Exam 2026', 'helptrickbd'),
        'sanitize_callback' => 'sanitize_text_field',
        'transport'         => 'postMessage',
    ]);
    $wp_customize->add_control('ht_countdown_title', [
        'label'   => esc_html__('Exam Countdown Label / Title', 'helptrickbd'),
        'section' => 'ht_header_section',
        'type'    => 'text',
    ]);

    // Exam countdown date
    $wp_customize->add_setting('ht_countdown_date', [
        'default'           => '2026-11-20',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('ht_countdown_date', [
        'label'       => esc_html__('Target Exam Date (YYYY-MM-DD)', 'helptrickbd'),
        'description' => esc_html__('Format: 2026-11-20', 'helptrickbd'),
        'section'     => 'ht_header_section',
        'type'        => 'date',
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

    // =============================================================
    // Section 1.5: Homepage 4-Column Multi-Category Grid
    // =============================================================
    $wp_customize->add_section('ht_multi_cat_section', [
        'title'    => esc_html__('Homepage Multi-Category Grid', 'helptrickbd'),
        'panel'    => 'ht_main_panel',
        'priority' => 12,
    ]);

    // Multi-Cat Toggle
    $wp_customize->add_setting('ht_multi_cat_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_multi_cat_enable', [
        'label'   => esc_html__('Enable 4-Column Departmental Grid', 'helptrickbd'),
        'section' => 'ht_multi_cat_section',
        'type'    => 'checkbox',
    ]);

    // Section Title
    $wp_customize->add_setting('ht_multi_cat_title', [
        'default'           => 'বিভাগ ও বিষয়ভিত্তিক বিশেষ হ্যান্ডনোট',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('ht_multi_cat_title', [
        'label'   => esc_html__('Section Main Heading', 'helptrickbd'),
        'section' => 'ht_multi_cat_section',
        'type'    => 'text',
    ]);

    // Section Subtitle
    $wp_customize->add_setting('ht_multi_cat_subtitle', [
        'default'           => 'জাতীয় বিশ্ববিদ্যালয়, বোর্ড পরীক্ষা ও সাম্প্রতিক একাডেমিক স্টাডিজ',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('ht_multi_cat_subtitle', [
        'label'   => esc_html__('Section Subtitle', 'helptrickbd'),
        'section' => 'ht_multi_cat_section',
        'type'    => 'text',
    ]);

    // Column 1 Category Slug
    $wp_customize->add_setting('ht_multi_cat_1', [
        'default'           => 'national-university',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('ht_multi_cat_1', [
        'label'   => esc_html__('Column 1 Category Slug', 'helptrickbd'),
        'section' => 'ht_multi_cat_section',
        'type'    => 'text',
    ]);

    // Column 2 Category Slug
    $wp_customize->add_setting('ht_multi_cat_2', [
        'default'           => 'political-science',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('ht_multi_cat_2', [
        'label'   => esc_html__('Column 2 Category Slug', 'helptrickbd'),
        'section' => 'ht_multi_cat_section',
        'type'    => 'text',
    ]);

    // Column 3 Category Slug
    $wp_customize->add_setting('ht_multi_cat_3', [
        'default'           => 'education-guide',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('ht_multi_cat_3', [
        'label'   => esc_html__('Column 3 Category Slug', 'helptrickbd'),
        'section' => 'ht_multi_cat_section',
        'type'    => 'text',
    ]);

    // Column 4 Category Slug
    $wp_customize->add_setting('ht_multi_cat_4', [
        'default'           => 'ssc-dakhil',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('ht_multi_cat_4', [
        'label'   => esc_html__('Column 4 Category Slug', 'helptrickbd'),
        'section' => 'ht_multi_cat_section',
        'type'    => 'text',
    ]);

    // =============================================================
    // Section 2: Sidebar Modules
    // =============================================================
    $wp_customize->add_section('ht_sidebar_section', [
        'title'    => esc_html__('Sidebar Modules', 'helptrickbd'),
        'panel'    => 'ht_main_panel',
        'priority' => 15,
    ]);

    // Sidebar Top Live Search
    $wp_customize->add_setting('ht_sidebar_search_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_sidebar_search_enable', [
        'label'       => esc_html__('Enable Top Live Search Box in Sidebar', 'helptrickbd'),
        'description' => esc_html__('Provides instant AJAX search suggestions in the sidebar.', 'helptrickbd'),
        'section'     => 'ht_sidebar_section',
        'type'        => 'checkbox',
    ]);

    $wp_customize->add_setting('ht_sidebar_search_title', [
        'default'           => esc_html__('Instant Search', 'helptrickbd'),
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('ht_sidebar_search_title', [
        'label'   => esc_html__('Search Box Title', 'helptrickbd'),
        'section' => 'ht_sidebar_section',
        'type'    => 'text',
    ]);

    $wp_customize->add_setting('ht_sidebar_search_placeholder', [
        'default'           => esc_html__('Search handnotes, suggestions, or guides...', 'helptrickbd'),
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('ht_sidebar_search_placeholder', [
        'label'   => esc_html__('Search Field Placeholder', 'helptrickbd'),
        'section' => 'ht_sidebar_section',
        'type'    => 'text',
    ]);

    // Sidebar Countdown Widget
    $wp_customize->add_setting('ht_sidebar_countdown_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_sidebar_countdown_enable', [
        'label'   => esc_html__('Display Exam Countdown Card in Sidebar', 'helptrickbd'),
        'section' => 'ht_sidebar_section',
        'type'    => 'checkbox',
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

    // Sidebar Categories
    $wp_customize->add_setting('ht_sidebar_categories_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_sidebar_categories_enable', [
        'label'       => esc_html__('Enable Category Cards Widget', 'helptrickbd'),
        'description' => esc_html__('Displays categories with vector icons and post count badges.', 'helptrickbd'),
        'section'     => 'ht_sidebar_section',
        'type'        => 'checkbox',
    ]);

    $wp_customize->add_setting('ht_sidebar_categories_title', [
        'default'           => esc_html__('Explore Categories', 'helptrickbd'),
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('ht_sidebar_categories_title', [
        'label'   => esc_html__('Categories Section Title', 'helptrickbd'),
        'section' => 'ht_sidebar_section',
        'type'    => 'text',
    ]);

    $wp_customize->add_setting('ht_sidebar_categories_count', [
        'default'           => 10,
        'sanitize_callback' => 'absint',
    ]);
    $wp_customize->add_control('ht_sidebar_categories_count', [
        'label'       => esc_html__('Max Categories to Display (4 to 20)', 'helptrickbd'),
        'section'     => 'ht_sidebar_section',
        'type'        => 'number',
        'input_attrs' => ['min' => 4, 'max' => 20, 'step' => 1],
    ]);

    // =============================================================
    // Section 3: Social & Community Links
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

    // =============================================================
    // Section 4: Footer & Copyright
    // =============================================================
    $wp_customize->add_section('ht_footer_section', [
        'title'    => esc_html__('Footer & Copyright', 'helptrickbd'),
        'panel'    => 'ht_main_panel',
        'priority' => 25,
    ]);

    // Pre-Footer Community Bar
    $wp_customize->add_setting('ht_pre_footer_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_pre_footer_enable', [
        'label'   => esc_html__('Enable Pre-Footer Community Bar (WhatsApp/Telegram)', 'helptrickbd'),
        'section' => 'ht_footer_section',
        'type'    => 'checkbox',
    ]);

    $wp_customize->add_setting('ht_pre_footer_title', [
        'default'           => esc_html__('Want exam routines & special suggestions first?', 'helptrickbd'),
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('ht_pre_footer_title', [
        'label'   => esc_html__('Community Bar Main Title', 'helptrickbd'),
        'section' => 'ht_footer_section',
        'type'    => 'text',
    ]);

    $wp_customize->add_setting('ht_pre_footer_sub', [
        'default'           => esc_html__('Join our official WhatsApp and Telegram study groups.', 'helptrickbd'),
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('ht_pre_footer_sub', [
        'label'   => esc_html__('Community Bar Subtitle', 'helptrickbd'),
        'section' => 'ht_footer_section',
        'type'    => 'text',
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

    // =============================================================
    // Section 5: Single Post & Student Study Tools
    // =============================================================
    $wp_customize->add_section('ht_study_tools_section', [
        'title'    => esc_html__('Single Post & Study Tools', 'helptrickbd'),
        'panel'    => 'ht_main_panel',
        'priority' => 30,
    ]);

    // Reading Progress Bar
    $wp_customize->add_setting('ht_reading_progress_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_reading_progress_enable', [
        'label'   => esc_html__('Enable Top Live Reading Progress Bar', 'helptrickbd'),
        'section' => 'ht_study_tools_section',
        'type'    => 'checkbox',
    ]);

    // Font Resizer
    $wp_customize->add_setting('ht_font_resizer_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_font_resizer_enable', [
        'label'   => esc_html__('Enable Font Resizer Tool (A- / A / A+)', 'helptrickbd'),
        'section' => 'ht_study_tools_section',
        'type'    => 'checkbox',
    ]);

    // Focus Mode
    $wp_customize->add_setting('ht_focus_mode_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_focus_mode_enable', [
        'label'   => esc_html__('Enable Focus Reading Mode Button', 'helptrickbd'),
        'section' => 'ht_study_tools_section',
        'type'    => 'checkbox',
    ]);

    // Bookmark Button
    $wp_customize->add_setting('ht_bookmark_btn_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_bookmark_btn_enable', [
        'label'   => esc_html__('Enable Reading List Bookmark Button', 'helptrickbd'),
        'section' => 'ht_study_tools_section',
        'type'    => 'checkbox',
    ]);

    // 1-Click Print & PDF
    $wp_customize->add_setting('ht_print_btn_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_print_btn_enable', [
        'label'   => esc_html__('Enable 1-Click Print & PDF Button', 'helptrickbd'),
        'section' => 'ht_study_tools_section',
        'type'    => 'checkbox',
    ]);

    // Auto TOC
    $wp_customize->add_setting('ht_toc_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_toc_enable', [
        'label'   => esc_html__('Enable Automatic Table of Contents (TOC)', 'helptrickbd'),
        'section' => 'ht_study_tools_section',
        'type'    => 'checkbox',
    ]);

    // Post Community Box
    $wp_customize->add_setting('ht_post_community_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_post_community_enable', [
        'label'   => esc_html__('Display Telegram & WhatsApp Community Card Below Post', 'helptrickbd'),
        'section' => 'ht_study_tools_section',
        'type'    => 'checkbox',
    ]);

    // Academic Citation
    $wp_customize->add_setting('ht_citation_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_citation_enable', [
        'label'   => esc_html__('Enable Academic Source Citation Box (APA 7th)', 'helptrickbd'),
        'section' => 'ht_study_tools_section',
        'type'    => 'checkbox',
    ]);

    // Related Posts
    $wp_customize->add_setting('ht_related_posts_enable', [
        'default'           => true,
        'sanitize_callback' => 'wp_validate_boolean',
    ]);
    $wp_customize->add_control('ht_related_posts_enable', [
        'label'   => esc_html__('Display Related Articles Grid Below Content', 'helptrickbd'),
        'section' => 'ht_study_tools_section',
        'type'    => 'checkbox',
    ]);

    // Reviewer Name
    $wp_customize->add_setting('ht_reviewer_name', [
        'default'           => esc_html__('Senior Faculty Panel', 'helptrickbd'),
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('ht_reviewer_name', [
        'label'       => esc_html__('Fact-Check Reviewer / Educator Name', 'helptrickbd'),
        'description' => esc_html__('Displayed in the top E-E-A-T verified badge.', 'helptrickbd'),
        'section'     => 'ht_study_tools_section',
        'type'        => 'text',
    ]);

    // Download Timer
    $wp_customize->add_setting('ht_download_timer', [
        'default'           => 5,
        'sanitize_callback' => 'absint',
    ]);
    $wp_customize->add_control('ht_download_timer', [
        'label'       => esc_html__('PDF Download Countdown Seconds', 'helptrickbd'),
        'description' => esc_html__('Between 1 and 30 seconds (Default: 5).', 'helptrickbd'),
        'section'     => 'ht_study_tools_section',
        'type'        => 'number',
        'input_attrs' => ['min' => 1, 'max' => 30, 'step' => 1],
    ]);

    // Author & Researcher Custom Avatar Upload
    $wp_customize->add_setting('ht_author_custom_avatar', [
        'default'           => '',
        'sanitize_callback' => 'esc_url_raw',
    ]);
    $wp_customize->add_control(new WP_Customize_Image_Control($wp_customize, 'ht_author_custom_avatar', [
        'label'       => esc_html__('Author Profile Photo (Optional Override)', 'helptrickbd'),
        'description' => esc_html__('Upload your author profile photo. If empty, automatically uses your WordPress User Profile photo/avatar.', 'helptrickbd'),
        'section'     => 'ht_study_tools_section',
    ]));

    // Author & Researcher Custom Name Override
    $wp_customize->add_setting('ht_author_custom_name', [
        'default'           => '',
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('ht_author_custom_name', [
        'label'       => esc_html__('Author Public Display Name (Optional Override)', 'helptrickbd'),
        'description' => esc_html__('Leave empty to automatically pull Display Name from WordPress Users -> Profile.', 'helptrickbd'),
        'section'     => 'ht_study_tools_section',
        'type'        => 'text',
    ]);

    // Author & Researcher Professional Title
    $wp_customize->add_setting('ht_author_custom_title', [
        'default'           => esc_html__('Author & Researcher', 'helptrickbd'),
        'sanitize_callback' => 'sanitize_text_field',
    ]);
    $wp_customize->add_control('ht_author_custom_title', [
        'label'       => esc_html__('Author Academic Credential / Title', 'helptrickbd'),
        'description' => esc_html__('E.g., "Author & Senior Researcher" or "Education Specialist".', 'helptrickbd'),
        'section'     => 'ht_study_tools_section',
        'type'        => 'text',
    ]);

    // Author & Researcher Custom Biography
    $wp_customize->add_setting('ht_author_custom_bio', [
        'default'           => '',
        'sanitize_callback' => 'sanitize_textarea_field',
    ]);
    $wp_customize->add_control('ht_author_custom_bio', [
        'label'       => esc_html__('Author Biography (Optional Override)', 'helptrickbd'),
        'description' => esc_html__('Leave empty to automatically pull from WordPress Users -> Profile -> Biographical Info.', 'helptrickbd'),
        'section'     => 'ht_study_tools_section',
        'type'        => 'textarea',
    ]);

    // =============================================================
    // Section 6: Google AdSense & Monetization
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

/**
 * Enqueue scripts for Customizer Live Preview (postMessage).
 */
function ht_customize_preview_js() {
    wp_enqueue_script(
        'ht-customizer-preview',
        get_template_directory_uri() . '/assets/js/customizer-preview.js',
        ['customize-preview', 'jquery'],
        HT_THEME_VERSION,
        true
    );
}
add_action('customize_preview_init', 'ht_customize_preview_js');
