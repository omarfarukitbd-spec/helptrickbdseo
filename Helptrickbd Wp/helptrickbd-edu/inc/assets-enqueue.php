<?php
/**
 * Script & Style Enqueueing with Dynamic Cache Busting (filemtime)
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}

if (!function_exists('htbd_edu_enqueue_scripts')) {
    /**
     * Enqueue all theme scripts and stylesheets with filemtime versioning.
     */
    function htbd_edu_enqueue_scripts() {
        $theme_dir = get_template_directory();
        $theme_uri = get_template_directory_uri();

        // 1. Google Web Fonts: Noto Serif Bengali & Hind Siliguri with font-display: swap
        wp_enqueue_style(
            'htbd-google-fonts',
            'https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@400;500;600;700&family=Noto+Serif+Bengali:wght@600;700;800;900&display=swap',
            array(),
            null
        );

        // 2. Base Theme Style.css
        $style_ver = file_exists($theme_dir . '/style.css') ? filemtime($theme_dir . '/style.css') : '1.0.0';
        wp_enqueue_style('htbd-theme-style', get_stylesheet_uri(), array(), $style_ver);

        // 3. Main Global CSS
        if (file_exists($theme_dir . '/assets/css/main.css')) {
            $main_css_ver = filemtime($theme_dir . '/assets/css/main.css');
            wp_enqueue_style('htbd-main-css', $theme_uri . '/assets/css/main.css', array('htbd-theme-style'), $main_css_ver);
        }

        // 4. Homepage Sections Specialized CSS (Only on Home / Front Page)
        if ((is_front_page() || is_home()) && file_exists($theme_dir . '/assets/css/home-sections.css')) {
            $home_css_ver = filemtime($theme_dir . '/assets/css/home-sections.css');
            wp_enqueue_style('htbd-home-css', $theme_uri . '/assets/css/home-sections.css', array('htbd-main-css'), $home_css_ver);
        }

        // 5. Single Post & Page Specific CSS
        if ((is_singular()) && file_exists($theme_dir . '/assets/css/single-post.css')) {
            $single_css_ver = filemtime($theme_dir . '/assets/css/single-post.css');
            wp_enqueue_style('htbd-single-css', $theme_uri . '/assets/css/single-post.css', array('htbd-main-css'), $single_css_ver);
        }

        // 6. Dark Mode CSS Tokens
        if (file_exists($theme_dir . '/assets/css/dark-mode.css')) {
            $dark_css_ver = filemtime($theme_dir . '/assets/css/dark-mode.css');
            wp_enqueue_style('htbd-dark-css', $theme_uri . '/assets/css/dark-mode.css', array('htbd-main-css'), $dark_css_ver);
        }

        // 7. Global Main JS (Theme switcher, search modal, drawer)
        if (file_exists($theme_dir . '/assets/js/main.js')) {
            $main_js_ver = filemtime($theme_dir . '/assets/js/main.js');
            wp_enqueue_script('htbd-main-js', $theme_uri . '/assets/js/main.js', array(), $main_js_ver, true);
        }

        // 8. Newspaper Font Resizer JS
        if (file_exists($theme_dir . '/assets/js/font-resizer.js')) {
            $font_js_ver = filemtime($theme_dir . '/assets/js/font-resizer.js');
            wp_enqueue_script('htbd-font-resizer-js', $theme_uri . '/assets/js/font-resizer.js', array(), $font_js_ver, true);
        }

        // 9. Client-side Interactive Filter JS (Home only)
        if ((is_front_page() || is_home()) && file_exists($theme_dir . '/assets/js/home-filter.js')) {
            $filter_js_ver = filemtime($theme_dir . '/assets/js/home-filter.js');
            wp_enqueue_script('htbd-home-filter-js', $theme_uri . '/assets/js/home-filter.js', array(), $filter_js_ver, true);
        }

        // 10. Live AJAX Instant Search JS
        if (file_exists($theme_dir . '/assets/js/ajax-search.js')) {
            $ajax_js_ver = filemtime($theme_dir . '/assets/js/ajax-search.js');
            wp_enqueue_script('htbd-ajax-search-js', $theme_uri . '/assets/js/ajax-search.js', array(), $ajax_js_ver, true);
            wp_localize_script('htbd-ajax-search-js', 'htbdEduSettings', array(
                'restUrl' => esc_url_raw(rest_url('wp/v2/')),
                'nonce'   => wp_create_nonce('wp_rest'),
            ));
        }

        // 11. Offline Bookmarks Engine JS
        if (file_exists($theme_dir . '/assets/js/bookmarks.js')) {
            $bm_js_ver = filemtime($theme_dir . '/assets/js/bookmarks.js');
            wp_enqueue_script('htbd-bookmarks-js', $theme_uri . '/assets/js/bookmarks.js', array(), $bm_js_ver, true);
        }

        // 12. Real-Time Exam Countdown JS (Home only)
        if ((is_front_page() || is_home()) && file_exists($theme_dir . '/assets/js/exam-countdown.js')) {
            $exam_js_ver = filemtime($theme_dir . '/assets/js/exam-countdown.js');
            wp_enqueue_script('htbd-exam-countdown-js', $theme_uri . '/assets/js/exam-countdown.js', array(), $exam_js_ver, true);
        }

        // 13. Reading Progress Indicator JS (Single posts)
        if (is_singular() && file_exists($theme_dir . '/assets/js/reading-progress.js')) {
            $read_js_ver = filemtime($theme_dir . '/assets/js/reading-progress.js');
            wp_enqueue_script('htbd-reading-progress-js', $theme_uri . '/assets/js/reading-progress.js', array(), $read_js_ver, true);
        }

        // 14. 1-Click Code & Question Copy Engine JS (Single posts)
        if (is_singular() && file_exists($theme_dir . '/assets/js/copy-question.js')) {
            $copy_js_ver = filemtime($theme_dir . '/assets/js/copy-question.js');
            wp_enqueue_script('htbd-copy-question-js', $theme_uri . '/assets/js/copy-question.js', array(), $copy_js_ver, true);
        }
    }
}
add_action('wp_enqueue_scripts', 'htbd_edu_enqueue_scripts');

/**
 * Add defer attribute to enqueued scripts for performance.
 */
function htbd_edu_defer_scripts($tag, $handle) {
    $defer_handles = array(
        'htbd-main-js',
        'htbd-font-resizer-js',
        'htbd-home-filter-js',
        'htbd-ajax-search-js',
        'htbd-bookmarks-js',
        'htbd-exam-countdown-js',
        'htbd-reading-progress-js',
        'htbd-copy-question-js',
    );
    if (in_array($handle, $defer_handles, true)) {
        return str_replace(' src', ' defer="defer" src', $tag);
    }
    return $tag;
}
add_filter('script_loader_tag', 'htbd_edu_defer_scripts', 10, 2);
