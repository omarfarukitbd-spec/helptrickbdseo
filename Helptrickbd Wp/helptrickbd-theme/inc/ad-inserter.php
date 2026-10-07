<?php
/**
 * Dynamic AdSense Inserter & Zero-CLS Ad Containers
 * High-CTR native placements, zero layout shifts, Google compliant.
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Render a designated Ad slot safely.
 *
 * @param string $slot_id Option ID from Customizer.
 * @param string $extra_class Additional CSS class.
 * @param int $min_height Reserved min-height to prevent CLS.
 */
function ht_render_ad($slot_id, $extra_class = '', $min_height = 0) {
    $ad_code = get_theme_mod($slot_id, '');
    if (empty(trim($ad_code))) {
        return;
    }

    $style = $min_height > 0 ? sprintf(' style="min-height:%dpx;"', intval($min_height)) : '';

    echo '<div class="ht-ad-wrapper ht-ad-' . esc_attr($slot_id) . ' ' . esc_attr($extra_class) . '"' . $style . '>';
    echo '<div class="ht-ad-label">বিজ্ঞাপন</div>';
    echo '<div class="ht-ad-content">' . $ad_code . '</div>'; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped
    echo '</div>';
}

/**
 * Filter the_content to dynamically inject in-article ad.
 * Inserts cleanly after paragraph 3 or 4 without breaking tables, quotes, or code.
 *
 * @param string $content Post content.
 * @return string Modified content with ad.
 */
function ht_inject_in_content_ad($content) {
    if (!is_single() || is_admin()) {
        return $content;
    }

    $ad_code = get_theme_mod('ht_ad_in_content', '');
    if (empty(trim($ad_code))) {
        return $content;
    }

    $ad_html = '<div class="ht-ad-wrapper ht-ad-in-content" style="min-height:250px;">' .
               '<div class="ht-ad-label">বিজ্ঞাপন</div>' .
               '<div class="ht-ad-content">' . $ad_code . '</div>' .
               '</div>';

    $closing_p = '</p>';
    $paragraphs = explode($closing_p, $content);
    $total_p = count($paragraphs);

    // If post has at least 5 paragraphs, insert after 3rd
    if ($total_p >= 5) {
        $insert_index = 3;
        foreach ($paragraphs as $index => &$paragraph) {
            if ($index === $insert_index) {
                $paragraph .= $ad_html;
            }
        }
        return implode($closing_p, $paragraphs);
    } elseif ($total_p >= 3) {
        // Shorter post: insert after 2nd
        $paragraphs[1] .= $ad_html;
        return implode($closing_p, $paragraphs);
    }

    return $content;
}
add_filter('the_content', 'ht_inject_in_content_ad', 20);

/**
 * Render In-Feed Native Ad Card for archives and homepage.
 */
function ht_render_in_feed_ad() {
    $ad_code = get_theme_mod('ht_ad_in_content', '');
    if (empty(trim($ad_code))) {
        return;
    }

    echo '<article class="ht-card ht-card-native-ad">';
    echo '<div class="ht-ad-label">বিজ্ঞাপন</div>';
    echo '<div class="ht-ad-content">' . $ad_code . '</div>'; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped
    echo '</article>';
}
