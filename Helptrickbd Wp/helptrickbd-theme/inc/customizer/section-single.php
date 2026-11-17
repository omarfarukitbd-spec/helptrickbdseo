<?php
/**
 * WordPress Customizer: Single Post & Student Study Tools
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Register Single Post & Study Tools settings.
 *
 * @param WP_Customize_Manager $wp_customize Customizer manager.
 */
function ht_customize_register_single($wp_customize) {
    // =============================================================
    // Section: Single Post & Student Study Tools
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
}
add_action('customize_register', 'ht_customize_register_single', 30);
