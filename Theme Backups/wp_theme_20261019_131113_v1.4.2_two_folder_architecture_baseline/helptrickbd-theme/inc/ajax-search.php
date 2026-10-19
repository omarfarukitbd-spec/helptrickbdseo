<?php
/**
 * Instant Live AJAX Search Endpoint (Spotlight / Ctrl+K)
 * Fast, debounced, with thumbnails and Bengali dates.
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Handle AJAX live search requests.
 */
function ht_ajax_live_search_handler() {
    check_ajax_referer('ht_live_search_nonce', 'nonce');

    $query = isset($_POST['query']) ? sanitize_text_field(wp_unslash($_POST['query'])) : '';

    if (empty($query) || mb_strlen($query) < 2) {
        wp_send_json_success(['results' => [], 'empty' => true]);
    }

    $args = [
        's'                   => $query,
        'post_type'           => 'post',
        'post_status'         => 'publish',
        'posts_per_page'      => 6,
        'ignore_sticky_posts' => 1,
        'no_found_rows'       => true,
    ];

    $search_query = new WP_Query($args);
    $results = [];

    if ($search_query->have_posts()) {
        while ($search_query->have_posts()) {
            $search_query->the_post();
            $post_id = get_the_ID();

            // Thumbnail
            $thumb = '';
            if (has_post_thumbnail($post_id)) {
                $thumb = get_the_post_thumbnail_url($post_id, 'thumbnail');
            } else {
                // Check first image in content
                $content = get_post_field('post_content', $post_id);
                if (preg_match('/<img[^>]+src=[\'"]([^\'"]+)[\'"]/', $content, $m)) {
                    $thumb = $m[1];
                }
            }

            // Categories
            $cats = get_the_category($post_id);
            $cat_name = !empty($cats) ? $cats[0]->name : 'সাধারণ';

            // Decode HTML entities to pure Unicode characters (e.g. &#8211; -> –, &#038; -> &)
            $clean_title = html_entity_decode(wp_specialchars_decode(get_the_title($post_id), ENT_QUOTES), ENT_QUOTES | ENT_HTML5, 'UTF-8');
            $clean_category = html_entity_decode(wp_specialchars_decode($cat_name, ENT_QUOTES), ENT_QUOTES | ENT_HTML5, 'UTF-8');

            $results[] = [
                'id'        => $post_id,
                'title'     => $clean_title,
                'url'       => get_permalink(),
                'date'      => ht_bn_date(get_post_time('U', false, $post_id)),
                'thumbnail' => $thumb,
                'category'  => $clean_category,
            ];
        }
        wp_reset_postdata();
    }

    wp_send_json_success([
        'results' => $results,
        'count'   => count($results),
        'query'   => $query,
    ]);
}
add_action('wp_ajax_ht_live_search', 'ht_ajax_live_search_handler');
add_action('wp_ajax_nopriv_ht_live_search', 'ht_ajax_live_search_handler');

/**
 * Handle Secure AJAX Post View Counting with Bot Filtering & Deduplication.
 */
function ht_ajax_record_view_handler() {
    check_ajax_referer('ht_post_view_nonce', 'nonce');

    $post_id = isset($_POST['post_id']) ? absint($_POST['post_id']) : 0;
    if (!$post_id || get_post_status($post_id) !== 'publish') {
        wp_send_json_error(['message' => 'Invalid post ID']);
    }

    // 1. Crawler / Bot Detection Filter
    $user_agent = isset($_SERVER['HTTP_USER_AGENT']) ? strtolower($_SERVER['HTTP_USER_AGENT']) : '';
    $bot_patterns = [
        'bot', 'crawl', 'spider', 'slurp', 'mediapartners', 'google', 'bing', 'yandex',
        'baidu', 'duckduckgo', 'yahoo', 'ahrefs', 'semrush', 'mj12bot', 'facebookexternalhit',
        'curl', 'python', 'wget', 'headless', 'lighthouse'
    ];
    foreach ($bot_patterns as $bot) {
        if (strpos($user_agent, $bot) !== false) {
            wp_send_json_success(['status' => 'bot_ignored']);
        }
    }

    // 2. Cookie Deduplication Check (Prevent multiple increments from same visitor within 12 hours)
    $cookie_name = 'ht_viewed_' . $post_id;
    if (isset($_COOKIE[$cookie_name])) {
        $count = (int) get_post_meta($post_id, 'ht_post_views_count', true);
        wp_send_json_success(['status' => 'already_counted', 'count' => $count]);
    }

    // 3. Increment Post Views
    $count_key = 'ht_post_views_count';
    $count = (int) get_post_meta($post_id, $count_key, true);
    if ($count == 0) {
        delete_post_meta($post_id, $count_key);
        add_post_meta($post_id, $count_key, 1);
        $count = 1;
    } else {
        $count++;
        update_post_meta($post_id, $count_key, $count);
    }

    // Set 12-hour deduplication cookie
    if (!headers_sent()) {
        setcookie($cookie_name, '1', time() + 43200, COOKIEPATH ? COOKIEPATH : '/', COOKIE_DOMAIN);
    }

    wp_send_json_success([
        'status'  => 'incremented',
        'count'   => $count,
        'countBn' => ht_bn_number($count)
    ]);
}
add_action('wp_ajax_ht_record_view', 'ht_ajax_record_view_handler');
add_action('wp_ajax_nopriv_ht_record_view', 'ht_ajax_record_view_handler');

/**
 * AJAX Handler for Interactive Post Likes / Reactions.
 */
function ht_ajax_like_post_handler() {
    check_ajax_referer('ht_post_like_nonce', 'nonce');

    $post_id = isset($_POST['post_id']) ? absint($_POST['post_id']) : 0;
    if (!$post_id || get_post_status($post_id) !== 'publish') {
        wp_send_json_error(['message' => 'Invalid post ID']);
    }

    $count_key = 'ht_post_likes_count';
    $count = (int) get_post_meta($post_id, $count_key, true);

    // Initial base seed if 0 so early posts look established
    if ($count <= 0) {
        $count = rand(15, 35);
    } else {
        $count++;
    }

    update_post_meta($post_id, $count_key, $count);

    wp_send_json_success([
        'count'   => $count,
        'countBn' => ht_bn_number($count),
        'message' => esc_html__('Thank you! Your feedback has been recorded.', 'helptrickbd'),
    ]);
}
add_action('wp_ajax_ht_like_post', 'ht_ajax_like_post_handler');
add_action('wp_ajax_nopriv_ht_like_post', 'ht_ajax_like_post_handler');


