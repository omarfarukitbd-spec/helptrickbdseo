<?php
/**
 * Locale-Aware Helpers: Numbers, Dates, and Reading Times
 * HelpTrickBD Pro Theme
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Smart Localized Number Converter.
 *
 * @param int|string $number The number to format.
 * @return string Localized number string.
 */
function ht_number($number) {
    if (ht_is_bangla_locale()) {
        $en = ['0','1','2','3','4','5','6','7','8','9'];
        $bn = ['০','১','২','৩','৪','৫','৬','৭','৮','৯'];
        return str_replace($en, $bn, strval($number));
    }
    return strval($number);
}

/**
 * Smart Localized Post Date (Published or Modified).
 *
 * @param int|WP_Post|null $post_id Post ID or object.
 * @param bool $modified Whether to return modified date instead of published date.
 * @return string Localized date string.
 */
function ht_get_localized_post_date($post_id = null, $modified = false) {
    $post = get_post($post_id);
    if (!$post) {
        return '';
    }

    if (ht_is_bangla_locale()) {
        // Bengali calendar formatting
        $en_months = ['January','February','March','April','May','June','July','August','September','October','November','December'];
        $bn_months = ['জানুয়ারি','ফেব্রুয়ারি','মার্চ','এপ্রিল','মে','জুন','জুলাই','আগস্ট','সেপ্টেম্বর','অক্টোবর','নভেম্বর','ডিসেম্বর'];

        $day   = $modified ? get_the_modified_date('j', $post) : get_the_date('j', $post);
        $month = $modified ? get_the_modified_date('F', $post) : get_the_date('F', $post);
        $year  = $modified ? get_the_modified_date('Y', $post) : get_the_date('Y', $post);

        $month_bn = str_replace($en_months, $bn_months, $month);

        return sprintf(
            '%s %s, %s',
            ht_number($day),
            $month_bn,
            ht_number($year)
        );
    }

    // English calendar formatting
    return $modified ? get_the_modified_date('F j, Y', $post) : get_the_date('F j, Y', $post);
}

/**
 * Smart Localized Reading Time.
 *
 * @param int|WP_Post|null $post_id Post ID or object.
 * @return string Localized reading time string.
 */
function ht_get_localized_reading_time($post_id = null) {
    $post = get_post($post_id);
    if (!$post) {
        return '';
    }

    $content    = strip_tags($post->post_content);
    $word_count = mb_strlen(preg_replace('/\s+/', '', $content));
    $words      = !empty($word_count) ? $word_count / 5 : str_word_count($content);
    $minutes    = max(1, ceil($words / 180));

    if (ht_is_bangla_locale()) {
        return ht_number($minutes) . ' ' . esc_html__('মিনিট পড়া', 'helptrickbd');
    }

    return $minutes . ' ' . esc_html__('min read', 'helptrickbd');
}

/**
 * Smart Localized Post Views Count.
 *
 * @param int $count Number of views.
 * @return string Localized views string.
 */
function ht_get_localized_post_views($count) {
    $formatted_count = number_format_i18n($count);
    if (ht_is_bangla_locale()) {
        return ht_number($formatted_count) . ' ' . esc_html__('বার পঠিত', 'helptrickbd');
    }
    return $formatted_count . ' ' . esc_html__('Views', 'helptrickbd');
}
