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

/**
 * Smart Localized Taxonomy Term Name (Category/Tag).
 * Translates Bengali database term names to standard English when English locale is active.
 *
 * @param int|WP_Term|string $term_or_id Term object, ID, or slug.
 * @param string $taxonomy Taxonomy name (default 'category').
 * @return string Localized term name.
 */
function ht_get_localized_term_name($term_or_id, $taxonomy = 'category') {
    if (empty($term_or_id)) {
        return '';
    }

    $term = null;
    if ($term_or_id instanceof WP_Term) {
        $term = $term_or_id;
    } elseif (is_numeric($term_or_id)) {
        $term = get_term((int) $term_or_id, $taxonomy);
    } elseif (is_string($term_or_id)) {
        $term = get_term_by('slug', $term_or_id, $taxonomy);
    }

    if (!$term || is_wp_error($term)) {
        return is_string($term_or_id) ? esc_html($term_or_id) : '';
    }

    // 1. If Polylang or WPML has a translation
    if (function_exists('pll_get_term')) {
        $target_lang = ht_is_bangla_locale() ? 'bn' : 'en';
        $trans_id    = pll_get_term($term->term_id, $target_lang);
        if ($trans_id && $trans_id !== $term->term_id) {
            $trans_term = get_term($trans_id, $taxonomy);
            if ($trans_term && !is_wp_error($trans_term)) {
                return $trans_term->name;
            }
        }
    }

    // 2. If Bengali locale is active, return native term name
    if (ht_is_bangla_locale()) {
        return $term->name;
    }

    // 3. English Mode: Map known slugs to standardized English names
    $slug_map = array(
        'national-university' => __('National University', 'helptrickbd'),
        'education-guide'     => __('Education & Routines', 'helptrickbd'),
        'ssc-dakhil'          => __('SSC & Dakhil Suggestions', 'helptrickbd'),
        'political-science'   => __('Political Science Handnotes', 'helptrickbd'),
        'ict-technology'      => __('ICT & Technology', 'helptrickbd'),
        'job-preparation'     => __('Career & BCS Preparation', 'helptrickbd'),
        'islamic-article'     => __('Islamic Articles & Duas', 'helptrickbd'),
        'bangla-1st-paper'    => __('Bangla 1st Paper', 'helptrickbd'),
        'english-grammar'     => __('English Grammar & Composition', 'helptrickbd'),
        'hsc'                 => __('HSC Suggestions & Guides', 'helptrickbd'),
        'degree'              => __('Degree Routine & Handnotes', 'helptrickbd'),
        'routine'             => __('Exam Routines & Notices', 'helptrickbd'),
        'admission'           => __('College & University Admission', 'helptrickbd'),
        'bcs'                 => __('BCS & Job Preparation', 'helptrickbd'),
        'academic'            => __('Academic Handnotes', 'helptrickbd'),
        'notice'              => __('Official Notices & Updates', 'helptrickbd'),
    );

    if (isset($slug_map[$term->slug])) {
        return $slug_map[$term->slug];
    }

    // Check partial slug matches
    foreach ($slug_map as $key => $val) {
        if (strpos($term->slug, $key) !== false) {
            return $val;
        }
    }

    // If term name contains Bengali characters, convert slug to Clean English Title Case
    if (preg_match('/[\x{0980}-\x{09FF}]/u', $term->name)) {
        return ucwords(str_replace(array('-', '_'), ' ', $term->slug));
    }

    return $term->name;
}

/**
 * Filter archive titles in English mode so category archive headers appear in English.
 *
 * @param string $title Original archive title.
 * @return string Localized archive title.
 */
function ht_localize_archive_title($title) {
    if (function_exists('ht_is_bangla_locale') && !ht_is_bangla_locale() && is_category()) {
        $term = get_queried_object();
        if ($term instanceof WP_Term) {
            return ht_get_localized_term_name($term);
        }
    }
    return $title;
}
add_filter('get_the_archive_title', 'ht_localize_archive_title');

