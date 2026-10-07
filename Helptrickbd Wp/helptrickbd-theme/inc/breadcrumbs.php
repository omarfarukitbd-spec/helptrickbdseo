<?php
/**
 * SEO Breadcrumbs with Rank Math Fallback
 * Pure semantic HTML5 and Schema.org BreadcrumbList support.
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Render Breadcrumbs navigation.
 */
function ht_breadcrumbs() {
    // 1. If Rank Math SEO breadcrumbs function is available and enabled
    if (function_exists('rank_math_the_breadcrumbs')) {
        echo '<div class="ht-breadcrumbs-wrapper">';
        rank_math_the_breadcrumbs();
        echo '</div>';
        return;
    }

    // 2. Native Schema-compliant Breadcrumbs Fallback
    if (is_front_page()) {
        return;
    }

    $sep = ht_m3_icon('arrow_forward', 14, 'ht-crumb-sep', false);
    $home_title = 'হোম';

    echo '<nav class="ht-breadcrumbs" aria-label="ব্রেডক্রাম্ব">';
    echo '<ol itemscope itemtype="https://schema.org/BreadcrumbList">';

    // Home item
    echo '<li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">';
    echo '<a itemprop="item" href="' . esc_url(home_url('/')) . '">';
    echo ht_m3_icon('home', 14, 'ht-home-icon', false);
    echo '<span itemprop="name">' . esc_html($home_title) . '</span>';
    echo '</a>';
    echo '<meta itemprop="position" content="1" />';
    echo '</li>';

    $position = 2;

    if (is_single()) {
        $cats = get_the_category();
        if (!empty($cats)) {
            $cat = $cats[0];
            echo '<li class="ht-crumb-sep-item">' . $sep . '</li>';
            echo '<li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">';
            echo '<a itemprop="item" href="' . esc_url(get_category_link($cat->term_id)) . '">';
            echo '<span itemprop="name">' . esc_html($cat->name) . '</span>';
            echo '</a>';
            echo '<meta itemprop="position" content="' . $position . '" />';
            echo '</li>';
            $position++;
        }

        echo '<li class="ht-crumb-sep-item">' . $sep . '</li>';
        echo '<li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem" class="ht-crumb-current" aria-current="page">';
        echo '<span itemprop="name">' . esc_html(wp_trim_words(get_the_title(), 8)) . '</span>';
        echo '<meta itemprop="position" content="' . $position . '" />';
        echo '</li>';

    } elseif (is_category()) {
        echo '<li class="ht-crumb-sep-item">' . $sep . '</li>';
        echo '<li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem" class="ht-crumb-current" aria-current="page">';
        echo '<span itemprop="name">' . esc_html(single_cat_title('', false)) . '</span>';
        echo '<meta itemprop="position" content="' . $position . '" />';
        echo '</li>';

    } elseif (is_tag()) {
        echo '<li class="ht-crumb-sep-item">' . $sep . '</li>';
        echo '<li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem" class="ht-crumb-current" aria-current="page">';
        echo '<span itemprop="name">' . esc_html(single_tag_title('', false)) . '</span>';
        echo '<meta itemprop="position" content="' . $position . '" />';
        echo '</li>';

    } elseif (is_page()) {
        echo '<li class="ht-crumb-sep-item">' . $sep . '</li>';
        echo '<li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem" class="ht-crumb-current" aria-current="page">';
        echo '<span itemprop="name">' . esc_html(get_the_title()) . '</span>';
        echo '<meta itemprop="position" content="' . $position . '" />';
        echo '</li>';

    } elseif (is_search()) {
        echo '<li class="ht-crumb-sep-item">' . $sep . '</li>';
        echo '<li class="ht-crumb-current" aria-current="page">অনুসন্ধান ফলাফল: "' . esc_html(get_search_query()) . '"</li>';

    } elseif (is_404()) {
        echo '<li class="ht-crumb-sep-item">' . $sep . '</li>';
        echo '<li class="ht-crumb-current" aria-current="page">পেজটি পাওয়া যায়নি</li>';
    }

    echo '</ol>';
    echo '</nav>';
}
