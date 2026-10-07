<?php
/**
 * Custom Template Tags and Utilities for HelpTrickBD Pro
 * Pure Bengali numbers, E-E-A-T badges, reading times, zero emojis, Material 3 vector icons.
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Convert English numbers to Bengali numerals.
 *
 * @param int|string $number The number to convert.
 * @return string Bengali numeral string.
 */
function ht_bn_number($number) {
    $en = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
    $bn = ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯'];
    return str_replace($en, $bn, strval($number));
}

/**
 * Format date into Bengali format (e.g. "৩ অক্টোবর ২০২৬").
 *
 * @param string|int $timestamp Date string or Unix timestamp.
 * @return string Formatted Bengali date.
 */
function ht_bn_date($timestamp = null) {
    if (!$timestamp) {
        $timestamp = get_the_time('U');
    } elseif (!is_numeric($timestamp)) {
        $timestamp = strtotime($timestamp);
    }

    $day = date('j', $timestamp);
    $month = date('n', $timestamp);
    $year = date('Y', $timestamp);

    $months_bn = [
        1 => 'জানুয়ারি', 2 => 'ফেব্রুয়ারি', 3 => 'মার্চ', 4 => 'এপ্রিল',
        5 => 'মে', 6 => 'জুন', 7 => 'জুলাই', 8 => 'আগস্ট',
        9 => 'সেপ্টেম্বর', 10 => 'অক্টোবর', 11 => 'নভেম্বর', 12 => 'ডিসেম্বর'
    ];

    return sprintf(
        '%s %s %s',
        ht_bn_number($day),
        isset($months_bn[$month]) ? $months_bn[$month] : '',
        ht_bn_number($year)
    );
}

/**
 * Calculate estimated reading time and word count.
 *
 * @param int $post_id Post ID.
 * @return array Array with ['words' => int, 'minutes' => int, 'html' => string].
 */
function ht_get_reading_time($post_id = null) {
    if (!$post_id) {
        $post_id = get_the_ID();
    }

    $content = get_post_field('post_content', $post_id);
    $clean_content = wp_strip_all_tags(strip_shortcodes($content));
    $word_count = count(preg_split('/\s+/u', $clean_content, -1, PREG_SPLIT_NO_EMPTY));

    // Average reading speed: 180 words per minute for Bengali/academic content
    $minutes = max(1, ceil($word_count / 180));

    $html = sprintf(
        '<span class="ht-meta-item ht-reading-time" title="%s শব্দ">%s %s মিনিট পড়ার সময়</span>',
        esc_attr(ht_bn_number($word_count)),
        ht_m3_icon('schedule', 16, '', false),
        esc_html(ht_bn_number($minutes))
    );

    return [
        'words' => $word_count,
        'minutes' => $minutes,
        'html' => $html
    ];
}

/**
 * Render Reading Time badge.
 *
 * @param int $post_id Post ID.
 */
function ht_reading_time($post_id = null) {
    $info = ht_get_reading_time($post_id);
    echo $info['html']; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped
}

/**
 * Render Formatted Post Date.
 *
 * @param int $post_id Post ID.
 */
function ht_post_date($post_id = null) {
    if (!$post_id) {
        $post_id = get_the_ID();
    }
    printf(
        '<time class="ht-meta-item ht-date" datetime="%s">%s %s</time>',
        esc_attr(get_the_date('c', $post_id)),
        ht_m3_icon('event', 16, '', false),
        esc_html(ht_bn_date(get_post_time('U', false, $post_id)))
    );
}

/**
 * Render Dynamic Last-Updated Date if modified.
 *
 * @param int $post_id Post ID.
 */
function ht_last_updated($post_id = null) {
    if (!$post_id) {
        $post_id = get_the_ID();
    }

    $published_time = get_post_time('U', false, $post_id);
    $modified_time = get_post_modified_time('U', false, $post_id);

    // Only display if updated more than 24 hours after publishing
    if (($modified_time - $published_time) > 86400) {
        printf(
            '<div class="ht-updated-badge" title="সর্বশেষ পরিমার্জন">%s <span>সর্বশেষ পরিমার্জিত: %s</span></div>',
            ht_m3_icon('history', 16, '', false),
            esc_html(ht_bn_date($modified_time))
        );
    }
}

/**
 * Render Google E-E-A-T Fact-Checked Verified Badge.
 */
function ht_eeat_badge() {
    printf(
        '<div class="ht-eeat-badge" title="শিক্ষক ও বিষয় বিশেষজ্ঞদের দ্বারা তথ্য যাচাইকৃত">%s <span>তথ্য যাচাইকৃত</span></div>',
        ht_m3_icon('verified', 18, 'ht-icon-verified', false)
    );
}

/**
 * Render Primary Category Badge.
 *
 * @param int $post_id Post ID.
 */
function ht_category_badge($post_id = null) {
    if (!$post_id) {
        $post_id = get_the_ID();
    }

    $categories = get_the_category($post_id);
    if (!empty($categories)) {
        $primary_cat = $categories[0];
        printf(
            '<a href="%s" class="ht-cat-badge ht-cat-%s">%s</a>',
            esc_url(get_category_link($primary_cat->term_id)),
            esc_attr($primary_cat->slug),
            esc_html($primary_cat->name)
        );
    }
}

/**
 * Post Views Counter & Display.
 *
 * @param int $post_id Post ID.
 */
function ht_post_views($post_id = null) {
    if (!$post_id) {
        $post_id = get_the_ID();
    }

    $count = (int) get_post_meta($post_id, 'ht_post_views_count', true);
    if (!$count) {
        $count = 1;
    }

    printf(
        '<span class="ht-meta-item ht-views">%s %s বার পঠিত</span>',
        ht_m3_icon('visibility', 16, '', false),
        esc_html(ht_bn_number($count))
    );
}

/**
 * Increment Post Views Count.
 *
 * @param int $post_id Post ID.
 */
function ht_set_post_views($post_id) {
    if (!is_single() || empty($post_id)) {
        return;
    }

    $count_key = 'ht_post_views_count';
    $count = (int) get_post_meta($post_id, $count_key, true);

    if ($count == 0) {
        delete_post_meta($post_id, $count_key);
        add_post_meta($post_id, $count_key, 1);
    } else {
        $count++;
        update_post_meta($post_id, $count_key, $count);
    }
}
