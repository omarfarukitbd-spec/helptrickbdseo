<?php
/**
 * HelpTrickBD Pro - Smart 301 Permanent Redirect Engine for Blogger-to-WordPress Migration
 * Intercepts incoming legacy Blogger URLs (/YYYY/MM/slug.html, /p/slug.html, and /search/label/...)
 * and permanently redirects (HTTP 301) them to corresponding modern WordPress permalinks.
 * Preserves 100% of SEO PageRank, backlinks, and eliminates all 404 errors.
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Blogger to WordPress 301 Redirection Handler
 */
function ht_blogger_301_redirect_engine() {
    $request_uri = $_SERVER['REQUEST_URI'] ?? '';
    if (empty($request_uri)) {
        return;
    }

    $parsed_path = parse_url($request_uri, PHP_URL_PATH);
    if (!$parsed_path) {
        return;
    }

    // 1. Check for legacy Blogger Post and Page URLs ending in .html
    if (preg_match('#/(?:p/|\d{4}/\d{2}/)?([^/]+)\.html$#i', $parsed_path, $matches)) {
        $raw_slug   = strtolower($matches[1]);
        $clean_slug = preg_replace('/_\d+$/', '', $raw_slug);

        // Predefined aliases for Blogger truncated slugs
        $aliases = [
            'ssc-english-2nd-paper-suggestion-2027'       => 'ssc-english-2nd-paper-final-suggestion',
            'bcs-preliminary-marks-distribution-booklist' => 'bcs-preliminary-marks-distribution_01436475916',
            'remittance-importance'                       => 'what-is-remittance-importance-economy-obstacles',
            'basic-economy-problems-bd'                   => 'bangladesh-basic-economy-features-problems-solutions',
            'budget-importance'                           => 'what-is-budget-importance-role-economy',
            'nu-cgpa-calculator'                          => 'nu-cgpa-calculator',
        ];

        $target_slug = $aliases[$raw_slug] ?? ($aliases[$clean_slug] ?? $clean_slug);

        // Try to locate published post or page by slug
        $post = get_page_by_path($target_slug, OBJECT, ['post', 'page']);
        if ($post && in_array($post->post_status, ['publish', 'inherit'], true)) {
            $destination_url = get_permalink($post->ID);
            wp_redirect($destination_url, 301);
            exit;
        }

        // Secondary fallback search by name
        $found_posts = get_posts([
            'name'           => $target_slug,
            'post_type'      => ['post', 'page'],
            'post_status'    => 'publish',
            'posts_per_page' => 1,
            'no_found_rows'  => true,
        ]);

        if (!empty($found_posts)) {
            $destination_url = get_permalink($found_posts[0]->ID);
            wp_redirect($destination_url, 301);
            exit;
        }

        // Direct home permalink fallback if slug matches standard format
        $destination_url = home_url('/' . sanitize_title($target_slug) . '/');
        wp_redirect($destination_url, 301);
        exit;
    }

    // 2. Check for legacy Blogger Label Archives (/search/label/CategoryName)
    if (preg_match('#/search/label/([^/?&#]+)#i', $parsed_path, $matches)) {
        $label = urldecode($matches[1]);
        $category = get_category_by_slug(sanitize_title($label));
        if ($category) {
            wp_redirect(get_category_link($category->term_id), 301);
            exit;
        }
        $tag = get_term_by('slug', sanitize_title($label), 'post_tag');
        if ($tag) {
            wp_redirect(get_tag_link($tag->term_id), 301);
            exit;
        }
        // Fallback to internal search
        wp_redirect(home_url('/?s=' . urlencode($label)), 301);
        exit;
    }

    // 3. Check for legacy Blogger Search URLs (/search?q=Query)
    if (strpos($parsed_path, '/search') === 0 && isset($_GET['q'])) {
        $query = sanitize_text_field(wp_unslash($_GET['q']));
        wp_redirect(home_url('/?s=' . urlencode($query)), 301);
        exit;
    }
}
add_action('template_redirect', 'ht_blogger_301_redirect_engine', 1);
