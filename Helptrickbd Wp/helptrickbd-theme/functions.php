<?php
/**
 * HelpTrickBD Pro Theme Functions and Definitions
 * Zero external bloat, pure PHP 8.1+, pure Material 3 SVG vector icons.
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

// Define Theme Version
define('HT_THEME_VERSION', '1.2.5');

// Include Inc Modules
require_once get_template_directory() . '/inc/material-icons.php';
require_once get_template_directory() . '/inc/template-tags.php';
require_once get_template_directory() . '/inc/breadcrumbs.php';
require_once get_template_directory() . '/inc/customizer.php';
require_once get_template_directory() . '/inc/ad-inserter.php';
require_once get_template_directory() . '/inc/ajax-search.php';
require_once get_template_directory() . '/inc/widgets.php';
require_once get_template_directory() . '/inc/content-cleaner.php';
require_once get_template_directory() . '/inc/redirect-engine.php';
require_once get_template_directory() . '/inc/link-rewriter.php';

/**
 * Sets up theme defaults and registers support for various WordPress features.
 */
function ht_theme_setup() {
    // Make theme available for translation
    load_theme_textdomain('helptrickbd', get_template_directory() . '/languages');

    // Add default posts and comments RSS feed links to head
    add_theme_support('automatic-feed-links');

    // Let WordPress manage the document title
    add_theme_support('title-tag');

    // Enable support for Post Thumbnails on posts and pages
    add_theme_support('post-thumbnails');
    set_post_thumbnail_size(800, 450, true);
    add_image_size('ht-hero-large', 1200, 675, true);
    add_image_size('ht-card-thumb', 600, 338, true);

    // Register Navigation Menus
    register_nav_menus([
        'primary-menu' => 'প্রধান মেনু (Primary Header Menu)',
        'footer-menu'  => 'ফুটার মেনু (Footer Menu)',
        'mobile-menu'  => 'মোবাইল ড্রয়ার মেনু (Mobile Menu)',
    ]);

    // Switch default core markup to output valid HTML5
    add_theme_support('html5', [
        'search-form',
        'comment-form',
        'comment-list',
        'gallery',
        'caption',
        'style',
        'script',
    ]);

    // Gutenberg wide alignment and responsive embeds
    add_theme_support('align-wide');
    add_theme_support('responsive-embeds');

    // Custom Logo
    add_theme_support('custom-logo', [
        'height'      => 60,
        'width'       => 240,
        'flex-height' => true,
        'flex-width'  => true,
    ]);
}
add_action('after_setup_theme', 'ht_theme_setup');

/**
 * Set the content width in pixels, based on the theme's design and stylesheet.
 */
function ht_content_width() {
    $GLOBALS['content_width'] = apply_filters('ht_content_width', 880);
}
add_action('after_setup_theme', 'ht_content_width', 0);

/**
 * Register widget area (Sidebars and Footer).
 */
function ht_widgets_init() {
    register_sidebar([
        'name'          => 'মূল সাইডবার (Primary Sidebar)',
        'id'            => 'ht-primary-sidebar',
        'description'   => 'আর্টিকেল এবং আর্কাইভ পেজের ডান পাশের সাইডবার',
        'before_widget' => '<div id="%1$s" class="ht-widget %2$s">',
        'after_widget'  => '</div>',
        'before_title'  => '<h3 class="ht-widget-title">',
        'after_title'   => '</h3>',
    ]);

    for ($i = 1; $i <= 4; $i++) {
        register_sidebar([
            'name'          => sprintf('ফুটার কলাম %d (Footer Column %d)', $i, $i),
            'id'            => 'ht-footer-' . $i,
            'description'   => sprintf('ফুটার সেকশনের কলাম %d উইজেট', $i),
            'before_widget' => '<div id="%1$s" class="ht-footer-widget %2$s">',
            'after_widget'  => '</div>',
            'before_title'  => '<h4 class="ht-footer-widget-title">',
            'after_title'   => '</h4>',
        ]);
    }
}
add_action('widgets_init', 'ht_widgets_init');

/**
 * Enqueue scripts and styles.
 */
function ht_enqueue_scripts() {
    // SolaimanLipi High-Precision Bengali Web Font + Inter (Latin Numerals)
    wp_enqueue_style(
        'ht-solaiman-lipi',
        'https://fonts.maateen.me/solaiman-lipi/font.css',
        [],
        null
    );
    wp_enqueue_style(
        'ht-google-fonts',
        'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap',
        [],
        null
    );

    // Main Theme Stylesheet
    wp_enqueue_style('ht-style', get_stylesheet_uri(), [], HT_THEME_VERSION);
    wp_enqueue_style('ht-main', get_template_directory_uri() . '/assets/css/main.css', ['ht-style'], HT_THEME_VERSION);
    wp_enqueue_style('ht-spotlight', get_template_directory_uri() . '/assets/css/spotlight.css', ['ht-main'], HT_THEME_VERSION);

    if (is_singular()) {
        wp_enqueue_style('ht-single', get_template_directory_uri() . '/assets/css/single.css', ['ht-main'], HT_THEME_VERSION);
        wp_enqueue_script('ht-single-tools', get_template_directory_uri() . '/assets/js/single-tools.js', [], HT_THEME_VERSION, true);
    }

    // National University CGPA Calculator Web App Assets
    if (is_page('nu-cgpa-calculator') || is_page_template('page-nu-cgpa-calculator.php')) {
        wp_enqueue_style(
            'ht-nu-cgpa-calculator-css',
            get_template_directory_uri() . '/assets/css/nu-cgpa-calculator.css',
            ['ht-main'],
            HT_THEME_VERSION
        );
        wp_enqueue_script(
            'ht-nu-cgpa-calculator-js',
            get_template_directory_uri() . '/assets/js/nu-cgpa-calculator.js',
            [],
            HT_THEME_VERSION,
            true
        );
    }

    // Main JavaScript
    wp_enqueue_script('ht-main-js', get_template_directory_uri() . '/assets/js/main.js', [], HT_THEME_VERSION, true);
    wp_enqueue_script('ht-spotlight-js', get_template_directory_uri() . '/assets/js/spotlight.js', ['ht-main-js'], HT_THEME_VERSION, true);
    wp_enqueue_script('ht-prefetch-js', get_template_directory_uri() . '/assets/js/prefetch.js', ['ht-main-js'], HT_THEME_VERSION, true);

    // Localize data for AJAX and features
    wp_localize_script('ht-main-js', 'htConfig', [
        'ajaxUrl'        => admin_url('admin-ajax.php'),
        'searchNonce'    => wp_create_nonce('ht_live_search_nonce'),
        'siteUrl'        => home_url(),
        'countdownDate'  => get_theme_mod('ht_countdown_date', '2026-11-20'),
        'countdownTitle' => get_theme_mod('ht_countdown_title', 'অনার্স ২য় বর্ষ পরীক্ষা ২০২৬'),
        'downloadTimer'  => get_theme_mod('ht_download_timer', 5),
    ]);
}
add_action('wp_enqueue_scripts', 'ht_enqueue_scripts');

/**
 * Output Head Meta (Fonts Preconnect, PWA manifest, Theme Color, Google Auto Ads).
 */
function ht_head_meta() {
    echo '<link rel="preconnect" href="https://fonts.googleapis.com">' . "\n";
    echo '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>' . "\n";
    echo '<meta name="theme-color" content="#2563eb">' . "\n";
    echo '<link rel="manifest" href="' . esc_url(get_template_directory_uri() . '/manifest.json') . '">' . "\n";
    echo '<link rel="apple-touch-icon" href="' . esc_url(get_template_directory_uri() . '/assets/images/icon-192.png') . '">' . "\n";

    // Auto Ads code if provided
    $auto_ads = get_theme_mod('ht_ad_auto_ads', '');
    if (!empty(trim($auto_ads))) {
        echo $auto_ads . "\n"; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped
    }
}
add_action('wp_head', 'ht_head_meta', 1);

// Disable comments globally site-wide
add_filter('comments_open', '__return_false', 20, 2);
add_filter('pings_open', '__return_false', 20, 2);
add_filter('comments_array', '__return_empty_array', 10, 2);

function ht_disable_comments_post_types_support() {
    remove_post_type_support('post', 'comments');
    remove_post_type_support('page', 'comments');
}
add_action('init', 'ht_disable_comments_post_types_support');

/**
 * Clean & normalize post content migrated from Blogger.
 * Strips legacy embedded <style> blocks that hardcode black text / white backgrounds,
 * strips conflicting inline dark colors & light backgrounds so text cleanly adapts to Dark Mode.
 */
function ht_clean_migrated_post_content($content) {
    if (empty($content) || !is_singular() || is_admin()) {
        return $content;
    }

    // 1. Remove legacy embedded <style> tags injected by old Blogger templates
    $content = preg_replace('/<style[^>]*>[\s\S]*?<\/style>/i', '', $content);

    // 2. Strip hardcoded dark text colors from inline styles (causes black-on-black in dark mode)
    $dark_patterns = [
        '#000000', '#000', 'black',
        '#0f172a', '#1e293b', '#202124', '#334155', '#475569',
        '#555555', '#555', '#3c4043', '#5f6368', '#111827', '#1f2937'
    ];
    foreach ($dark_patterns as $dp) {
        $content = preg_replace('/color\s*:\s*' . preg_quote($dp, '/') . '\s*(!important)?\s*;?/i', '', $content);
    }
    // Also remove rgb dark colors
    $content = preg_replace('/color\s*:\s*rgb\s*\(\s*(?:0|30|32|33|34|50|51|52|60)\s*,\s*(?:0|30|32|33|34|50|51|52|60)\s*,\s*(?:0|30|32|33|34|36|50|51|52|60)\s*\)\s*(!important)?\s*;?/i', '', $content);

    // 3. Strip hardcoded light background colors from inline styles (causes blinding white boxes in dark mode)
    $light_bg_patterns = [
        '#ffffff', '#fff', 'white',
        '#f8fafc', '#f1f5f9', '#f8fafd', '#f9f9f9', '#fcfcfc', '#eff6ff', '#e8f5e9', '#ecfdf5'
    ];
    foreach ($light_bg_patterns as $lbp) {
        $content = preg_replace('/background(-color)?\s*:\s*' . preg_quote($lbp, '/') . '\s*(!important)?\s*;?/i', '', $content);
    }

    // 4. Clean up any empty style attributes
    $content = preg_replace('/\s*style\s*=\s*["\']\s*["\']/i', '', $content);

    return $content;
}
add_filter('the_content', 'ht_clean_migrated_post_content', 15);

/**
 * Automatically wrap tables in responsive scroll wrapper
 */
function ht_wrap_responsive_tables($content) {
    if (is_singular() && !is_admin()) {
        $pattern = '/<table(?![^>]*class=[\'"][^\'"]*ht-table-responsive)([^>]*)>(.*?)<\/table>/is';
        $replacement = '<div class="ht-table-responsive"><div class="ht-table-scroll-hint">' . ht_m3_icon('swap_horiz', 16, '', false) . ' <span>সম্পূর্ণ তথ্য দেখতে ডানে-বামে স্ক্রোল করুন</span></div><table$1>$2</table></div>';
        $content = preg_replace($pattern, $replacement, $content);
    }
    return $content;
}
add_filter('the_content', 'ht_wrap_responsive_tables', 20);

/**
 * Render featured image or branded fallback SVG card.
 *
 * @param int $post_id Post ID.
 * @param string $size Image size.
 * @param string $extra_class Additional CSS class.
 */
function ht_the_thumbnail($post_id = null, $size = 'ht-card-thumb', $extra_class = '') {
    if (!$post_id) {
        $post_id = get_the_ID();
    }

    $class_attr = $extra_class ? ' ' . esc_attr($extra_class) : '';

    if (has_post_thumbnail($post_id)) {
        the_post_thumbnail($size, [
            'class'   => 'ht-thumbnail-img' . $class_attr,
            'loading' => 'lazy',
            'decoding'=> 'async',
            'alt'     => esc_attr(get_the_title($post_id)),
        ]);
        return;
    }

    // Check first image in content
    $content = get_post_field('post_content', $post_id);
    if (preg_match('/<img[^>]+src=[\'"]([^\'"]+)[\'"]/', $content, $m)) {
        printf(
            '<img src="%s" class="ht-thumbnail-img%s" alt="%s" loading="lazy" decoding="async">',
            esc_url($m[1]),
            $class_attr,
            esc_attr(get_the_title($post_id))
        );
        return;
    }

    // Fallback Branded SVG Card
    $title = get_the_title($post_id);
    printf(
        '<div class="ht-fallback-thumb%s"><div class="ht-fallback-content">%s<span>%s</span></div></div>',
        $class_attr,
        ht_m3_icon('menu_book', 40, 'ht-fallback-icon', false),
        esc_html(wp_trim_words($title, 6))
    );
}

/**
 * Track Post Views on Single Post Load.
 */
function ht_track_post_views() {
    if (is_single()) {
        ht_set_post_views(get_the_ID());
    }
}
add_action('wp_head', 'ht_track_post_views');

/**
 * Completely unregister legacy default WordPress widgets (Recent Posts, Comments, Archives, Categories).
 */
function ht_unregister_default_widgets() {
    unregister_widget('WP_Widget_Recent_Posts');
    unregister_widget('WP_Widget_Recent_Comments');
    unregister_widget('WP_Widget_Archives');
    unregister_widget('WP_Widget_Categories');
}
add_action('widgets_init', 'ht_unregister_default_widgets', 15);

/**
 * Return contextual Material 3 icon name for a category based on slug and Bengali name.
 *
 * @param string $slug Category slug.
 * @param string $name Category name.
 * @return string Material 3 icon key.
 */
function ht_get_category_icon($slug = '', $name = '') {
    $slug = strtolower($slug);
    $name = mb_strtolower($name);

    if (strpos($slug, 'honours') !== false || strpos($slug, 'nu') !== false || strpos($name, 'অনার্স') !== false || strpos($name, 'বিশ্ববিদ্যালয়') !== false) {
        return 'account_balance';
    }
    if (strpos($slug, 'degree') !== false || strpos($slug, 'hsc') !== false || strpos($slug, 'ssc') !== false || strpos($slug, 'dakhil') !== false || strpos($name, 'ডিগ্রি') !== false || strpos($name, 'এইচএসসি') !== false || strpos($name, 'দাখিল') !== false) {
        return 'school';
    }
    if (strpos($slug, 'english') !== false || strpos($slug, 'bangla') !== false || strpos($slug, 'grammar') !== false || strpos($name, 'ইংরেজি') !== false || strpos($name, 'বাংলা') !== false || strpos($name, 'ভাষা') !== false) {
        return 'translate';
    }
    if (strpos($slug, 'job') !== false || strpos($slug, 'bcs') !== false || strpos($slug, 'career') !== false || strpos($name, 'চাকরি') !== false || strpos($name, 'বিসিএস') !== false) {
        return 'work';
    }
    if (strpos($slug, 'political') !== false || strpos($slug, 'law') !== false || strpos($name, 'রাষ্ট্রবিজ্ঞান') !== false || strpos($name, 'আইন') !== false) {
        return 'policy';
    }
    if (strpos($slug, 'islamic') !== false || strpos($slug, 'quran') !== false || strpos($name, 'ইসলামিক') !== false || strpos($name, 'ধর্ম') !== false) {
        return 'brightness_7';
    }
    if (strpos($slug, 'tech') !== false || strpos($slug, 'code') !== false || strpos($slug, 'computer') !== false || strpos($slug, 'ict') !== false || strpos($name, 'প্রযুক্তি') !== false || strpos($name, 'কম্পিউটার') !== false || strpos($name, 'আইসিটি') !== false) {
        return 'devices';
    }
    if (strpos($slug, 'note') !== false || strpos($slug, 'handnote') !== false || strpos($slug, 'routine') !== false || strpos($name, 'নোট') !== false || strpos($name, 'সাজেশন') !== false || strpos($name, 'রুটিন') !== false) {
        return 'description';
    }
    return 'folder_open';
}

/**
 * Register Rank Math SEO postmeta fields for REST API access.
 * Enables automated tools to read and update Rank Math metadata.
 */
function ht_register_rank_math_rest_meta() {
    $meta_keys = [
        'rank_math_title',
        'rank_math_description',
        'rank_math_focus_keyword',
        'rank_math_canonical_url',
        'rank_math_robots',
    ];

    foreach ($meta_keys as $key) {
        register_post_meta('post', $key, [
            'show_in_rest' => true,
            'single'       => true,
            'type'         => 'string',
            'auth_callback' => function() {
                return current_user_can('edit_posts');
            }
        ]);
    }
}
add_action('init', 'ht_register_rank_math_rest_meta');

