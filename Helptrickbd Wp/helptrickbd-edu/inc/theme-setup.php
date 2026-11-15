<?php
/**
 * Theme Setup & Registration
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}

if (!function_exists('htbd_edu_setup')) {
    /**
     * Sets up theme defaults and registers support for various WordPress features.
     */
    function htbd_edu_setup() {
        // Make theme available for translation.
        load_theme_textdomain('helptrickbd-edu', get_template_directory() . '/languages');

        // Add default posts and comments RSS feed links to head.
        add_theme_support('automatic-feed-links');

        // Let WordPress manage the document title.
        add_theme_support('title-tag');

        // Enable support for Post Thumbnails on posts and pages.
        add_theme_support('post-thumbnails');

        // Custom Logo support.
        add_theme_support('custom-logo', array(
            'height'      => 80,
            'width'       => 300,
            'flex-height' => true,
            'flex-width'  => true,
            'header-text' => array('site-title', 'site-description'),
        ));

        // Custom Header support.
        add_theme_support('custom-header', array(
            'default-image'      => '',
            'width'              => 1200,
            'height'             => 300,
            'flex-height'        => true,
            'flex-width'         => true,
            'default-text-color' => '222222',
            'header-text'        => true,
        ));

        // Responsive Embeds.
        add_theme_support('responsive-embeds');

        // WordPress Block Styles (block gap, duotone, etc.).
        add_theme_support('wp-block-styles');

        // Add support for full and wide align images.
        add_theme_support('align-wide');

        // Switch default core markup to HTML5.
        add_theme_support('html5', array(
            'search-form',
            'comment-form',
            'comment-list',
            'gallery',
            'caption',
            'style',
            'script',
        ));

        // Add theme support for selective refresh for widgets.
        add_theme_support('customize-selective-refresh-widgets');

        // ── Image Sizes ──────────────────────────────────────────────────────
        // Required standard sizes per brief.
        add_image_size('htbd-thumbnail', 400, 267, true);    // 3:2 Card Thumbnail
        add_image_size('htbd-medium',    800, 534, true);    // 3:2 Medium
        add_image_size('htbd-hero',     1200, 675, true);    // 16:9 Hero Banner

        // Additional high-performance crops used by templates.
        add_image_size('ht-lead-banner', 800,  450, true);   // 16:9 Lead Banner
        add_image_size('ht-card-banner', 400,  225, true);   // 16:9 Card Thumbnail
        add_image_size('ht-thumb-row',   132,   92, true);   // Compact Newspaper Thumb
        add_image_size('ht-photo-grid',  300,  200, true);   // 3:2 Photo Gallery Card

        // ── Navigation Menus ─────────────────────────────────────────────────
        register_nav_menus(array(
            'primary-nav' => esc_html__('প্রধান মেনু (Newspaper Bar)', 'helptrickbd-edu'),
            'mobile-nav'  => esc_html__('মোবাইল ড্রয়ার মেনু', 'helptrickbd-edu'),
            'footer-nav'  => esc_html__('ফুটার মেনু', 'helptrickbd-edu'),
        ));
    }
}
add_action('after_setup_theme', 'htbd_edu_setup');

/**
 * Register widget areas / sidebars.
 */
function htbd_edu_widgets_init() {
    // Primary content sidebar.
    register_sidebar(array(
        'name'          => esc_html__('প্রধান সাইডবার', 'helptrickbd-edu'),
        'id'            => 'htbd-sidebar',
        'description'   => esc_html__('আর্টিকেল পেজের ডানদিকের উইজেট এরিয়া।', 'helptrickbd-edu'),
        'before_widget' => '<section id="%1$s" class="widget %2$s">',
        'after_widget'  => '</section>',
        'before_title'  => '<h3 class="widget-title">',
        'after_title'   => '</h3>',
    ));

    // Footer widget area – Column 1.
    register_sidebar(array(
        'name'          => esc_html__('ফুটার কলাম ১', 'helptrickbd-edu'),
        'id'            => 'htbd-footer-1',
        'description'   => esc_html__('ফুটারের প্রথম কলামের উইজেট এরিয়া।', 'helptrickbd-edu'),
        'before_widget' => '<section id="%1$s" class="widget %2$s">',
        'after_widget'  => '</section>',
        'before_title'  => '<h3 class="widget-title footer-widget-title">',
        'after_title'   => '</h3>',
    ));

    // Footer widget area – Column 2.
    register_sidebar(array(
        'name'          => esc_html__('ফুটার কলাম ২', 'helptrickbd-edu'),
        'id'            => 'htbd-footer-2',
        'description'   => esc_html__('ফুটারের দ্বিতীয় কলামের উইজেট এরিয়া।', 'helptrickbd-edu'),
        'before_widget' => '<section id="%1$s" class="widget %2$s">',
        'after_widget'  => '</section>',
        'before_title'  => '<h3 class="widget-title footer-widget-title">',
        'after_title'   => '</h3>',
    ));

    // Footer widget area – Column 3.
    register_sidebar(array(
        'name'          => esc_html__('ফুটার কলাম ৩', 'helptrickbd-edu'),
        'id'            => 'htbd-footer-3',
        'description'   => esc_html__('ফুটারের তৃতীয় কলামের উইজেট এরিয়া।', 'helptrickbd-edu'),
        'before_widget' => '<section id="%1$s" class="widget %2$s">',
        'after_widget'  => '</section>',
        'before_title'  => '<h3 class="widget-title footer-widget-title">',
        'after_title'   => '</h3>',
    ));

    // Legacy sidebar-main alias for backward compatibility.
    register_sidebar(array(
        'name'          => esc_html__('সাইডবার উইজেট (Legacy)', 'helptrickbd-edu'),
        'id'            => 'sidebar-main',
        'description'   => esc_html__('পুরনো সাইডবার উইজেট এরিয়া (পিছিয়ে সামঞ্জস্যতার জন্য)।', 'helptrickbd-edu'),
        'before_widget' => '<section id="%1$s" class="widget %2$s">',
        'after_widget'  => '</section>',
        'before_title'  => '<h3 class="widget-title">',
        'after_title'   => '</h3>',
    ));
}
add_action('widgets_init', 'htbd_edu_widgets_init');
