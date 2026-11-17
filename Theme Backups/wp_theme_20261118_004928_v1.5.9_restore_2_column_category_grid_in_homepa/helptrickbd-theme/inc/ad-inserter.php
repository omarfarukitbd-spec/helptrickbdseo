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
    // Strict Google AdSense Policy: NEVER display ads on 404 error pages
    if (is_404()) {
        return;
    }

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
 * Check if the text before a position has unclosed block tags (DOM Safety).
 *
 * @param string $html_chunk Text before candidate insertion point.
 * @return bool True if inside an open block tag.
 */
function ht_is_inside_block_tag($html_chunk) {
    $tags = array('table', 'blockquote', 'figure', 'ul', 'ol', 'pre', 'code');
    foreach ($tags as $tag) {
        $open_count  = preg_match_all('/<' . $tag . '\b[^>]*>/i', $html_chunk);
        $close_count = preg_match_all('/<\/' . $tag . '>/i', $html_chunk);
        if ($open_count > $close_count) {
            return true;
        }
    }
    return false;
}

/**
 * Filter the_content to dynamically inject in-article ads.
 * Inserts cleanly after paragraph 3 (and paragraph 8 for long-form 1500+ word posts)
 * without breaking tables, blockquotes, code blocks, or callouts.
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

    $ad_html_template = '<div class="ht-ad-wrapper ht-ad-in-content" style="min-height:250px;margin:28px 0;">' .
                        '<div class="ht-ad-label">বিজ্ঞাপন</div>' .
                        '<div class="ht-ad-content">%s</div>' .
                        '</div>';
    $ad_html = sprintf($ad_html_template, $ad_code);

    $closing_p = '</p>';
    $paragraphs = explode($closing_p, $content);
    $total_p = count($paragraphs);

    if ($total_p < 3) {
        return $content;
    }

    // Determine target insertion points: after 3rd paragraph
    $target_indices = array(2); // 0-indexed: index 2 = paragraph 3

    // For long-form posts (8+ paragraphs), insert a second ad after paragraph 7
    if ($total_p >= 9) {
        $target_indices[] = 7;
    }

    $running_content = '';
    foreach ($paragraphs as $index => &$paragraph) {
        $running_content .= $paragraph . $closing_p;
        if (in_array($index, $target_indices, true)) {
            // Verify DOM safety: not inside unclosed table, blockquote, or code
            if (!ht_is_inside_block_tag($running_content)) {
                $paragraph .= $ad_html;
            }
        }
    }

    return implode($closing_p, $paragraphs);
}
add_filter('the_content', 'ht_inject_in_content_ad', 20);

/**
 * Render In-Feed Native Ad Card for archives and homepage.
 */
function ht_render_in_feed_ad() {
    $ad_code = get_theme_mod('ht_ad_in_content', get_theme_mod('htbd_ad_infeed_1', ''));
    if (empty(trim($ad_code))) {
        return;
    }

    echo '<article class="ht-card ht-card-native-ad" style="min-height:250px;">';
    echo '<div class="ht-ad-label">বিজ্ঞাপন</div>';
    echo '<div class="ht-ad-content">' . $ad_code . '</div>'; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped
    echo '</article>';
}