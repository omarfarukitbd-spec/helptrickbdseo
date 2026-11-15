<?php
/**
 * Custom Template Tags for HelpTrickBD EduPortal
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}

if (!function_exists('htbd_bengali_number')) {
    /**
     * Converts English numbers to Bengali numerals.
     *
     * @param int|string $number
     * @return string
     */
    function htbd_bengali_number($number) {
        $en = array('0', '1', '2', '3', '4', '5', '6', '7', '8', '9');
        $bn = array('০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯');
        return str_replace($en, $bn, (string)$number);
    }
}

if (!function_exists('htbd_reading_time')) {
    /**
     * Calculates estimated reading time for article.
     *
     * @param int|null $post_id
     * @return string
     */
    function htbd_reading_time($post_id = null) {
        $post = get_post($post_id);
        if (!$post) {
            return '১ মিনিট পাঠ';
        }

        $content = strip_tags(strip_shortcodes($post->post_content));
        // Count words (Bengali words split by spaces)
        $words = preg_split('/\s+/u', trim($content), -1, PREG_SPLIT_NO_EMPTY);
        $word_count = count($words);
        $minutes = max(1, (int)ceil($word_count / 180));

        return htbd_bengali_number($minutes) . ' মিনিট পাঠ';
    }
}

if (!function_exists('htbd_category_badge')) {
    /**
     * Outputs first post category as a styled badge.
     *
     * @param int|null $post_id
     * @param string $class
     * @return void
     */
    function htbd_category_badge($post_id = null, $class = 'ht-badge') {
        $categories = get_the_category($post_id);
        if (!empty($categories)) {
            $cat = $categories[0];
            printf(
                '<a href="%s" class="%s ht-cat-%s">%s</a>',
                esc_url(get_category_link($cat->term_id)),
                esc_attr($class),
                esc_attr($cat->slug),
                esc_html($cat->name)
            );
        }
    }
}

if (!function_exists('htbd_post_meta')) {
    /**
     * Outputs standardized post metadata (date, reading time).
     *
     * @param int|null $post_id
     * @return void
     */
    function htbd_post_meta($post_id = null) {
        $time_string = sprintf(
            '<time class="entry-date published" datetime="%s">%s</time>',
            esc_attr(get_the_date(DATE_W3C, $post_id)),
            esc_html(get_the_date('j F, Y', $post_id))
        );

        echo '<div class="ht-meta-bar">';
        echo '<span class="ht-meta-item">';
        htbd_icon('calendar', array('width' => 14, 'height' => 14));
        echo ' ' . $time_string; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped
        echo '</span>';

        echo '<span class="ht-meta-item">';
        htbd_icon('clock', array('width' => 14, 'height' => 14));
        echo ' ' . esc_html(htbd_reading_time($post_id));
        echo '</span>';
        echo '</div>';
    }
}

if (!function_exists('htbd_author_badge')) {
    /**
     * Outputs author info with verified badge.
     *
     * @param int|null $author_id
     * @return void
     */
    function htbd_author_badge($author_id = null) {
        if (!$author_id) {
            $author_id = get_the_author_meta('ID');
        }

        $author_name = get_the_author_meta('display_name', $author_id);
        $author_url = get_author_posts_url($author_id);
        $avatar = get_avatar($author_id, 32, '', $author_name, array('class' => 'ht-author-img'));

        echo '<div class="ht-author-pill">';
        if ($avatar) {
            echo $avatar; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped
        }
        printf(
            '<a href="%s" class="ht-author-name">%s</a>',
            esc_url($author_url),
            esc_html($author_name)
        );
        htbd_icon('check-circle', array('class' => 'ht-verified-icon', 'width' => 14, 'height' => 14));
        echo '</div>';
    }
}

if (!function_exists('htbd_bengali_today')) {
    /**
     * Returns Bengali formatted today's date.
     *
     * @return string
     */
    function htbd_bengali_today() {
        $days = array('Sunday' => 'রবিবার', 'Monday' => 'সোমবার', 'Tuesday' => 'মঙ্গলবার', 'Wednesday' => 'বুধবার', 'Thursday' => 'বৃহস্পতিবার', 'Friday' => 'শুক্রবার', 'Saturday' => 'শনিবার');
        $months = array('January' => 'জানুয়ারি', 'February' => 'ফেব্রুয়ারি', 'March' => 'মার্চ', 'April' => 'এপ্রিল', 'May' => 'মে', 'June' => 'জুন', 'July' => 'জুলাই', 'August' => 'আগস্ট', 'September' => 'সেপ্টেম্বর', 'October' => 'অক্টোবর', 'November' => 'নভেম্বর', 'December' => 'ডিসেম্বর');
        
        $current_day = $days[date('l')];
        $current_month = $months[date('F')];
        $current_date = htbd_bengali_number(date('j'));
        $current_year = htbd_bengali_number(date('Y'));
        
        return "{$current_day}, {$current_date} {$current_month} {$current_year}";
    }
}
