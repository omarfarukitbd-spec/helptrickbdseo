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

        // Custom high-performance image crops
        add_image_size('ht-lead-banner', 800, 450, true);   // 16:9 Lead Banner
        add_image_size('ht-card-banner', 400, 225, true);   // 16:9 Card Thumbnail
        add_image_size('ht-thumb-row', 132, 92, true);      // Compact Newspaper Thumb
        add_image_size('ht-photo-grid', 300, 200, true);    // 3:2 Photo Gallery Card

        // Register Primary and Secondary navigation menus
        register_nav_menus(array(
            'primary-nav' => esc_html__('প্রধান মেনু (Newspaper Bar)', 'helptrickbd-edu'),
            'mobile-nav'  => esc_html__('মোবাইল ড্রয়ার মেনু', 'helptrickbd-edu'),
            'footer-nav'  => esc_html__('ফুটার মেনু', 'helptrickbd-edu'),
        ));

        // Switch default core markup for search form, comment form, etc. to HTML5
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

        // Add support for full and wide align images.
        add_theme_support('align-wide');
    }
}
add_action('after_setup_theme', 'htbd_edu_setup');

/**
 * Register widget area.
 */
function htbd_edu_widgets_init() {
    register_sidebar(array(
        'name'          => esc_html__('সাইডবার উইজেট', 'helptrickbd-edu'),
        'id'            => 'sidebar-main',
        'description'   => esc_html__('আর্টিকেল পেজের ডানদিকের উইজেট এরিয়া।', 'helptrickbd-edu'),
        'before_widget' => '<section id="%1$s" class="widget %2$s">',
        'after_widget'  => '</section>',
        'before_title'  => '<h3 class="widget-title">',
        'after_title'   => '</h3>',
    ));
}
add_action('widgets_init', 'htbd_edu_widgets_init');
