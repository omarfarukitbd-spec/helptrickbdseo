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

            $results[] = [
                'id'        => $post_id,
                'title'     => get_the_title(),
                'url'       => get_permalink(),
                'date'      => ht_bn_date(get_post_time('U', false, $post_id)),
                'thumbnail' => $thumb,
                'category'  => $cat_name,
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
