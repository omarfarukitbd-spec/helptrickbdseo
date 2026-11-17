<?php
/**
 * HelpTrickBD EduPortal Master Functions & Orchestrator
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Set the content width in pixels, based on the theme's design and stylesheet.
 * Priority 0 to make it available to lower priority callbacks.
 */
function htbd_edu_content_width() {
    $GLOBALS['content_width'] = apply_filters('htbd_edu_content_width', 800);
}
add_action('after_setup_theme', 'htbd_edu_content_width', 0);

// =============================================================================
// REQUIRED SUBSYSTEMS & MODULES
// =============================================================================

// 1. Theme Setup, Image Sizes & Menus
require_once get_template_directory() . '/inc/theme-setup.php';

// 2. Material 3 Vector SVG Icon Engine
require_once get_template_directory() . '/inc/material-icons.php';

// 3. Custom Template Tags & Date Helpers
require_once get_template_directory() . '/inc/template-tags.php';

// 4. Inlined Critical CSS for 100/100 CWV & FOUC Prevention
require_once get_template_directory() . '/inc/critical-css.php';

// 5. Assets Enqueueing with Dynamic filemtime Versioning
require_once get_template_directory() . '/inc/assets-enqueue.php';

// 6. Theme Customizer Options
require_once get_template_directory() . '/inc/customizer.php';

// 7. Smart 301 Permanent Redirect Engine (Blogger to WordPress Migration & 404 Prevention)
if (file_exists(get_template_directory() . '/inc/redirect-engine.php')) {
    require_once get_template_directory() . '/inc/redirect-engine.php';
}

// 8. Dynamic Internal Link Rewriter (Legacy .html Link Auto-Healer)
if (file_exists(get_template_directory() . '/inc/link-rewriter.php')) {
    require_once get_template_directory() . '/inc/link-rewriter.php';
}

// 9. Schema.org JSON-LD Structured Data Engine (Rich Results & Google E-E-A-T)
if (file_exists(get_template_directory() . '/inc/schema.php')) {
    require_once get_template_directory() . '/inc/schema.php';
}

// 10. Generative Engine Optimization (GEO & AI Search Crawler Directives)
if (file_exists(get_template_directory() . '/inc/geo-engine.php')) {
    require_once get_template_directory() . '/inc/geo-engine.php';
}

// 11. Zero-CLS AdSense Inserter Engine (High-CTR Native Placements)
if (file_exists(get_template_directory() . '/inc/ad-inserter.php')) {
    require_once get_template_directory() . '/inc/ad-inserter.php';
}

// =============================================================================
// CORE HOOKS & FILTERS
// =============================================================================

/**
 * Track and increment post views on single post view.
 */
function htbd_edu_track_post_views() {
    if (is_singular('post')) {
        htbd_increment_post_views(get_queried_object_id());
    }
}
add_action('wp', 'htbd_edu_track_post_views');

/**
 * Custom excerpt length (28 Bengali words).
 *
 * @param int $length Excerpt length.
 * @return int Modified length.
 */
function htbd_edu_excerpt_length($length) {
    return 28;
}
add_filter('excerpt_length', 'htbd_edu_excerpt_length', 999);

/**
 * Custom excerpt ellipsis suffix.
 *
 * @param string $more Current more string.
 * @return string Modified more string.
 */
function htbd_edu_excerpt_more($more) {
    return '...';
}
add_filter('excerpt_more', 'htbd_edu_excerpt_more');

/**
 * Sets exactly 10 posts per page on category archive pages with pagination.
 *
 * @param WP_Query $query Main query.
 */
function htbd_edu_category_posts_per_page($query) {
    if (!is_admin() && $query->is_main_query() && $query->is_category()) {
        $query->set('posts_per_page', 10);
    }
}
add_action('pre_get_posts', 'htbd_edu_category_posts_per_page');

/**
 * Add responsive body classes for styling and newspaper layout.
 *
 * @param array $classes Existing body classes.
 * @return array Modified classes.
 */
function htbd_edu_body_classes($classes) {
    $classes[] = 'htbd-edu-portal';
    if (is_front_page() || is_home()) {
        $classes[] = 'htbd-home-newspaper';
    }
    if (is_singular()) {
        $classes[] = 'htbd-singular-view';
    }
    return $classes;
}
add_filter('body_class', 'htbd_edu_body_classes');

/**
 * Add a pingback url auto-discovery header for single posts, pages, or attachments.
 */
function htbd_edu_pingback_header() {
    if (is_singular() && pings_open()) {
        printf('<link rel="pingback" href="%s">' . "\n", esc_url(get_bloginfo('pingback_url')));
    }
}
add_action('wp_head', 'htbd_edu_pingback_header');

/**
 * Custom document title separator.
 *
 * @param string $sep Current separator.
 * @return string Modified separator.
 */
function htbd_edu_document_title_separator($sep) {
    return '—';
}
add_filter('document_title_separator', 'htbd_edu_document_title_separator');
