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
define('HT_THEME_VERSION', '1.4.0');

// Include Inc Modules
require_once get_template_directory() . '/inc/material-icons.php';
require_once get_template_directory() . '/inc/template-tags.php';
require_once get_template_directory() . '/inc/breadcrumbs.php';
require_once get_template_directory() . '/inc/schema.php';
require_once get_template_directory() . '/inc/customizer.php';
require_once get_template_directory() . '/inc/ad-inserter.php';
require_once get_template_directory() . '/inc/ajax-search.php';
require_once get_template_directory() . '/inc/widgets.php';
require_once get_template_directory() . '/inc/content-cleaner.php';
require_once get_template_directory() . '/inc/redirect-engine.php';
require_once get_template_directory() . '/inc/link-rewriter.php';
require_once get_template_directory() . '/inc/auto-migrator.php';

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
        'primary-menu' => esc_html__('Primary Menu', 'helptrickbd'),
        'footer-menu'  => esc_html__('Footer Menu', 'helptrickbd'),
        'mobile-menu'  => esc_html__('Mobile Drawer Menu', 'helptrickbd'),
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

    // Gutenberg Block Editor Supports
    add_theme_support('editor-styles');
    add_editor_style('assets/css/editor-style.css');
    add_theme_support('wp-block-styles');
    add_theme_support('align-wide');
    add_theme_support('responsive-embeds');
    add_theme_support('customize-selective-refresh-widgets');

    // Gutenberg Material 3 Theme Color Palette
    add_theme_support('editor-color-palette', [
        [
            'name'  => esc_html__('Primary Blue', 'helptrickbd'),
            'slug'  => 'ht-primary',
            'color' => '#2563eb',
        ],
        [
            'name'  => esc_html__('Primary Dark', 'helptrickbd'),
            'slug'  => 'ht-primary-dark',
            'color' => '#1d4ed8',
        ],
        [
            'name'  => esc_html__('Surface Dark', 'helptrickbd'),
            'slug'  => 'ht-surface-dark',
            'color' => '#0f172a',
        ],
        [
            'name'  => esc_html__('Surface Card', 'helptrickbd'),
            'slug'  => 'ht-card-bg',
            'color' => '#1e293b',
        ],
        [
            'name'  => esc_html__('Text Main', 'helptrickbd'),
            'slug'  => 'ht-text-main',
            'color' => '#0f172a',
        ],
        [
            'name'  => esc_html__('Text Muted', 'helptrickbd'),
            'slug'  => 'ht-text-muted',
            'color' => '#475569',
        ],
        [
            'name'  => esc_html__('Accent Emerald', 'helptrickbd'),
            'slug'  => 'ht-accent-green',
            'color' => '#10b981',
        ],
        [
            'name'  => esc_html__('Accent Amber', 'helptrickbd'),
            'slug'  => 'ht-accent-amber',
            'color' => '#f59e0b',
        ],
    ]);

    // Gutenberg Font Sizes
    add_theme_support('editor-font-sizes', [
        [
            'name' => esc_html__('Small', 'helptrickbd'),
            'size' => 14,
            'slug' => 'small',
        ],
        [
            'name' => esc_html__('Normal', 'helptrickbd'),
            'size' => 16,
            'slug' => 'normal',
        ],
        [
            'name' => esc_html__('Medium', 'helptrickbd'),
            'size' => 18,
            'slug' => 'medium',
        ],
        [
            'name' => esc_html__('Large', 'helptrickbd'),
            'size' => 22,
            'slug' => 'large',
        ],
        [
            'name' => esc_html__('Huge', 'helptrickbd'),
            'size' => 28,
            'slug' => 'huge',
        ],
    ]);

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
        'name'          => esc_html__('Primary Sidebar', 'helptrickbd'),
        'id'            => 'ht-primary-sidebar',
        'description'   => esc_html__('Main sidebar displayed on single posts and archives.', 'helptrickbd'),
        'before_widget' => '<div id="%1$s" class="ht-widget %2$s">',
        'after_widget'  => '</div>',
        'before_title'  => '<h3 class="ht-widget-title">',
        'after_title'   => '</h3>',
    ]);

    for ($i = 1; $i <= 4; $i++) {
        register_sidebar([
            'name'          => sprintf(esc_html__('Footer Column %d', 'helptrickbd'), $i),
            'id'            => 'ht-footer-' . $i,
            'description'   => sprintf(esc_html__('Widget area for footer column %d.', 'helptrickbd'), $i),
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
        wp_enqueue_script('ht-single-tools', get_template_directory_uri() . '/assets/js/single-tools.js', ['ht-main-js'], HT_THEME_VERSION, true);
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
        'viewNonce'      => wp_create_nonce('ht_post_view_nonce'),
        'likeNonce'      => wp_create_nonce('ht_post_like_nonce'),
        'currentPostId'  => is_singular('post') ? get_the_ID() : 0,
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

// Note: Post views are securely tracked via client-side debounced AJAX (ht_ajax_record_view)
// to eliminate crawler/bot inflation and avoid database overhead on wp_head.


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
 * Get curated Material 3 icon for a category based on slug and name.
 *
 * @param string $slug Category slug.
 * @param string $name Category name.
 * @return string Material 3 icon key.
 */
function ht_get_category_icon($slug = '', $name = '') {
    $slug = strtolower($slug);
    $name = mb_strtolower($name);

    // 1. Political Science & Law
    if (strpos($slug, 'political') !== false || strpos($slug, 'law') !== false || strpos($name, 'রাষ্ট্রবিজ্ঞান') !== false || strpos($name, 'আইন') !== false) {
        return 'policy';
    }

    // 2. Education Guide & Academic Advice
    if (strpos($slug, 'education') !== false || strpos($slug, 'guide') !== false || strpos($name, 'শিক্ষা') !== false || strpos($name, 'গাইড') !== false) {
        return 'menu_book';
    }

    // 3. University Admission & Entrance
    if (strpos($slug, 'admission') !== false || strpos($name, 'ভর্তি') !== false) {
        return 'explore';
    }

    // 4. National University & Honours
    if (strpos($slug, 'national') !== false || strpos($slug, 'honours') !== false || strpos($slug, 'nu') !== false || strpos($name, 'জাতীয়') !== false || strpos($name, 'জাতীয়') !== false || strpos($name, 'অনার্স') !== false) {
        return 'account_balance';
    }

    // 5. SSC & Dakhil, HSC, Degree Examinations
    if (strpos($slug, 'ssc') !== false || strpos($slug, 'dakhil') !== false || strpos($slug, 'hsc') !== false || strpos($slug, 'degree') !== false || strpos($name, 'দাখিল') !== false || strpos($name, 'এসএসসি') !== false || strpos($name, 'ডিগ্রি') !== false || strpos($name, 'এইচএসসি') !== false) {
        return 'school';
    }

    // 6. Bangla Literature & 1st Paper
    if (strpos($slug, 'bangla') !== false || strpos($name, 'বাংলা') !== false || strpos($name, 'সাহিত্য') !== false) {
        return 'history_edu';
    }

    // 7. Islamic Studies & Articles
    if (strpos($slug, 'islamic') !== false || strpos($slug, 'quran') !== false || strpos($slug, 'hadith') !== false || strpos($name, 'ইসলামিক') !== false || strpos($name, 'ধর্ম') !== false || strpos($name, 'কুরআন') !== false) {
        return 'mosque';
    }

    // 8. English 1st/2nd Paper & Grammar
    if (strpos($slug, 'english') !== false || strpos($slug, 'grammar') !== false || strpos($name, 'ইংরেজি') !== false || strpos($name, 'গ্রামার') !== false) {
        return 'translate';
    }

    // 9. Job Preparation, BCS & Career
    if (strpos($slug, 'job') !== false || strpos($slug, 'bcs') !== false || strpos($slug, 'career') !== false || strpos($name, 'চাকরি') !== false || strpos($name, 'বিসিএস') !== false) {
        return 'work';
    }

    // 10. ICT, Computer Science & Technology
    if (strpos($slug, 'tech') !== false || strpos($slug, 'code') !== false || strpos($slug, 'computer') !== false || strpos($slug, 'ict') !== false || strpos($name, 'প্রযুক্তি') !== false || strpos($name, 'কম্পিউটার') !== false || strpos($name, 'আইসিটি') !== false) {
        return 'laptop_mac';
    }

    // 11. Routine, Notices & Exam Dates
    if (strpos($slug, 'routine') !== false || strpos($slug, 'notice') !== false || strpos($name, 'রুটিন') !== false || strpos($name, 'নোটিশ') !== false) {
        return 'event';
    }

    // 12. Notes & Suggestions
    if (strpos($slug, 'note') !== false || strpos($slug, 'handnote') !== false || strpos($name, 'নোট') !== false || strpos($name, 'সাজেশন') !== false) {
        return 'description';
    }

    return 'folder';
}

/**
 * Get curated color tokens for category cards and navigation badges.
 *
 * @param string $slug Category slug.
 * @param string $name Category name.
 * @return array Associative array with color, bg, border.
 */
function ht_get_category_palette($slug = '', $name = '') {
    $slug = strtolower($slug);
    $name = mb_strtolower($name);

    if (strpos($slug, 'political') !== false || strpos($slug, 'law') !== false || strpos($name, 'রাষ্ট্রবিজ্ঞান') !== false || strpos($name, 'আইন') !== false) {
        return [
            'color'  => '#e11d48', // Crimson Rose
            'bg'     => 'rgba(225, 29, 72, 0.08)',
            'border' => 'rgba(225, 29, 72, 0.22)',
        ];
    }
    if (strpos($slug, 'education') !== false || strpos($slug, 'guide') !== false || strpos($name, 'শিক্ষা') !== false || strpos($name, 'গাইড') !== false) {
        return [
            'color'  => '#2563eb', // Royal Blue
            'bg'     => 'rgba(37, 99, 235, 0.08)',
            'border' => 'rgba(37, 99, 235, 0.22)',
        ];
    }
    if (strpos($slug, 'admission') !== false || strpos($name, 'ভর্তি') !== false) {
        return [
            'color'  => '#c026d3', // Fuchsia
            'bg'     => 'rgba(192, 38, 211, 0.08)',
            'border' => 'rgba(192, 38, 211, 0.22)',
        ];
    }
    if (strpos($slug, 'national') !== false || strpos($slug, 'honours') !== false || strpos($slug, 'nu') !== false || strpos($name, 'জাতীয়') !== false || strpos($name, 'জাতীয়') !== false || strpos($name, 'অনার্স') !== false) {
        return [
            'color'  => '#1d4ed8', // Sapphire Navy
            'bg'     => 'rgba(29, 78, 216, 0.08)',
            'border' => 'rgba(29, 78, 216, 0.22)',
        ];
    }
    if (strpos($slug, 'ssc') !== false || strpos($slug, 'dakhil') !== false || strpos($slug, 'hsc') !== false || strpos($slug, 'degree') !== false || strpos($name, 'দাখিল') !== false || strpos($name, 'এসএসসি') !== false || strpos($name, 'ডিগ্রি') !== false) {
        return [
            'color'  => '#059669', // Emerald Green
            'bg'     => 'rgba(5, 150, 105, 0.08)',
            'border' => 'rgba(5, 150, 105, 0.22)',
        ];
    }
    if (strpos($slug, 'bangla') !== false || strpos($name, 'বাংলা') !== false || strpos($name, 'সাহিত্য') !== false) {
        return [
            'color'  => '#0d9488', // Teal
            'bg'     => 'rgba(13, 148, 136, 0.08)',
            'border' => 'rgba(13, 148, 136, 0.22)',
        ];
    }
    if (strpos($slug, 'islamic') !== false || strpos($slug, 'quran') !== false || strpos($slug, 'hadith') !== false || strpos($name, 'ইসলামিক') !== false || strpos($name, 'ধর্ম') !== false) {
        return [
            'color'  => '#16a34a', // Islamic Jade Green
            'bg'     => 'rgba(22, 163, 74, 0.08)',
            'border' => 'rgba(22, 163, 74, 0.22)',
        ];
    }
    if (strpos($slug, 'english') !== false || strpos($slug, 'grammar') !== false || strpos($name, 'ইংরেজি') !== false || strpos($name, 'গ্রামার') !== false) {
        return [
            'color'  => '#0284c7', // Sky Blue
            'bg'     => 'rgba(2, 132, 199, 0.08)',
            'border' => 'rgba(2, 132, 199, 0.22)',
        ];
    }
    if (strpos($slug, 'job') !== false || strpos($slug, 'bcs') !== false || strpos($slug, 'career') !== false || strpos($name, 'চাকরি') !== false || strpos($name, 'বিসিএস') !== false) {
        return [
            'color'  => '#d97706', // Amber Gold
            'bg'     => 'rgba(217, 119, 6, 0.08)',
            'border' => 'rgba(217, 119, 6, 0.22)',
        ];
    }
    if (strpos($slug, 'tech') !== false || strpos($slug, 'code') !== false || strpos($slug, 'computer') !== false || strpos($slug, 'ict') !== false || strpos($name, 'প্রযুক্তি') !== false || strpos($name, 'কম্পিউটার') !== false || strpos($name, 'আইসিটি') !== false) {
        return [
            'color'  => '#7c3aed', // Cyber Violet
            'bg'     => 'rgba(124, 58, 237, 0.08)',
            'border' => 'rgba(124, 58, 237, 0.22)',
        ];
    }
    if (strpos($slug, 'routine') !== false || strpos($slug, 'notice') !== false || strpos($name, 'রুটিন') !== false || strpos($name, 'নোটিশ') !== false) {
        return [
            'color'  => '#ea580c', // Warm Orange
            'bg'     => 'rgba(234, 88, 12, 0.08)',
            'border' => 'rgba(234, 88, 12, 0.22)',
        ];
    }
    return [
        'color'  => '#475569', // Slate
        'bg'     => 'rgba(71, 85, 105, 0.08)',
        'border' => 'rgba(71, 85, 105, 0.22)',
    ];
}

/**
 * Clean typography format for Primary Navigation menu items.
 *
 * @param string   $title The menu item's title.
 * @param WP_Post  $item  The current menu item.
 * @param stdClass $args  An object of wp_nav_menu() arguments.
 * @param int      $depth Depth of menu item.
 * @return string
 */
function ht_nav_menu_category_icons($title, $item, $args, $depth) {
    if (isset($args->theme_location) && $args->theme_location === 'primary-menu' && $depth === 0) {
        return '<span class="ht-nav-item-label">' . $title . '</span>';
    }
    return $title;
}
add_filter('nav_menu_item_title', 'ht_nav_menu_category_icons', 10, 4);

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
        'rank_math_seo_score',
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

/**
 * Remove redundant "Category: " or "Tag: " prefix from archive titles
 */
add_filter('get_the_archive_title_prefix', '__return_empty_string');

/**
 * Emit essential security headers
 */
function ht_send_security_headers() {
    if (!is_admin()) {
        header('X-Content-Type-Options: nosniff');
        header('X-Frame-Options: SAMEORIGIN');
        header('Referrer-Policy: strict-origin-when-cross-origin');
    }
}
add_action('send_headers', 'ht_send_security_headers');

/**
 * Ensure comments remain open on all published educational guide posts
 */
add_filter('comments_open', function($open, $post_id) {
    $post = get_post($post_id);
    if ($post && $post->post_type === 'post' && $post->post_status === 'publish') {
        return true;
    }
    return $open;
}, 20, 2);
