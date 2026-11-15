<?php
/**
 * HelpTrickBD EduPortal Master Functions & Orchestrator
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}

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

/**
 * Custom excerpt length and read more suffix
 */
function htbd_edu_excerpt_length($length) {
    return 28;
}
add_filter('excerpt_length', 'htbd_edu_excerpt_length', 999);

function htbd_edu_excerpt_more($more) {
    return '...';
}
add_filter('excerpt_more', 'htbd_edu_excerpt_more');

/**
 * Add responsive body classes
 */
function htbd_edu_body_classes($classes) {
    $classes[] = 'htbd-edu-portal';
    if (is_front_page() || is_home()) {
        $classes[] = 'htbd-home-newspaper';
    }
    return $classes;
}
add_filter('body_class', 'htbd_edu_body_classes');
