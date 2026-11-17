<?php
/**
 * Custom Template Tags for HelpTrickBD EduPortal
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}

if (!function_exists('htbd_get_default_thumbnail')) {
    /**
     * Returns the URL of the default fallback thumbnail.
     *
     * @return string Absolute URL to the default placeholder image.
     */
    function htbd_get_default_thumbnail() {
        return get_template_directory_uri() . '/assets/images/default-thumbnail.webp';
    }
}

if (!function_exists('htbd_primary_category')) {
    /**
     * Returns the primary category of a post as an associative array.
     * Respects Rank Math and Yoast SEO primary category meta if set.
     *
     * @param int|null $post_id Post ID; defaults to current post.
     * @return array{name: string, url: string, slug: string}|null Array with keys 'name', 'url', 'slug', or null if no category found.
     */
    function htbd_primary_category($post_id = null) {
        $post_id = $post_id ? (int) $post_id : get_the_ID();

        // Rank Math primary category.
        $rank_math_primary = get_post_meta($post_id, 'rank_math_primary_category', true);
        if ($rank_math_primary) {
            $term = get_term((int) $rank_math_primary, 'category');
            if ($term && !is_wp_error($term)) {
                return array(
                    'name' => $term->name,
                    'url'  => get_category_link($term->term_id),
                    'slug' => $term->slug,
                );
            }
        }

        // Yoast SEO primary category.
        $yoast_primary = get_post_meta($post_id, '_yoast_wpseo_primary_category', true);
        if ($yoast_primary) {
            $term = get_term((int) $yoast_primary, 'category');
            if ($term && !is_wp_error($term)) {
                return array(
                    'name' => $term->name,
                    'url'  => get_category_link($term->term_id),
                    'slug' => $term->slug,
                );
            }
        }

        // Fall back to the first assigned category.
        $categories = get_the_category($post_id);
        if (!empty($categories)) {
            $cat = $categories[0];
            return array(
                'name' => $cat->name,
                'url'  => get_category_link($cat->term_id),
                'slug' => $cat->slug,
            );
        }

        return null;
    }
}

if (!function_exists('htbd_bengali_number')) {
    /**
     * Converts English/Arabic numerals to Bengali numerals (০–৯).
     *
     * @param int|string $number The number to convert.
     * @return string Bengali numeral string.
     */
    function htbd_bengali_number($number) {
        $en = array('0', '1', '2', '3', '4', '5', '6', '7', '8', '9');
        $bn = array('০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯');
        return str_replace($en, $bn, (string) $number);
    }
}

if (!function_exists('htbd_bengali_date')) {
    /**
     * Converts a Unix timestamp to a Bengali-formatted date string.
     *
     * @param int $timestamp Unix timestamp.
     * @return string Date formatted as "রবিবার, ১৫ নভেম্বর ২০২৬".
     */
    function htbd_bengali_date($timestamp) {
        $days = array(
            'Sunday'    => 'রবিবার',
            'Monday'    => 'সোমবার',
            'Tuesday'   => 'মঙ্গলবার',
            'Wednesday' => 'বুধবার',
            'Thursday'  => 'বৃহস্পতিবার',
            'Friday'    => 'শুক্রবার',
            'Saturday'  => 'শনিবার',
        );
        $months = array(
            'January'   => 'জানুয়ারি',
            'February'  => 'ফেব্রুয়ারি',
            'March'     => 'মার্চ',
            'April'     => 'এপ্রিল',
            'May'       => 'মে',
            'June'      => 'জুন',
            'July'      => 'জুলাই',
            'August'    => 'আগস্ট',
            'September' => 'সেপ্টেম্বর',
            'October'   => 'অক্টোবর',
            'November'  => 'নভেম্বর',
            'December'  => 'ডিসেম্বর',
        );

        $day_name   = isset($days[ date('l', $timestamp) ]) ? $days[ date('l', $timestamp) ] : date('l', $timestamp);
        $month_name = isset($months[ date('F', $timestamp) ]) ? $months[ date('F', $timestamp) ] : date('F', $timestamp);
        $date_num   = htbd_bengali_number(date('j', $timestamp));
        $year_num   = htbd_bengali_number(date('Y', $timestamp));

        return "{$day_name}, {$date_num} {$month_name} {$year_num}";
    }
}

if (!function_exists('htbd_bengali_today')) {
    /**
     * Returns today's date as a Bengali-formatted string.
     *
     * @return string Today's date in Bengali.
     */
    function htbd_bengali_today() {
        return htbd_bengali_date(current_time('timestamp')); // phpcs:ignore WordPress.DateTime.CurrentTimeTimestamp.Requested
    }
}

if (!function_exists('htbd_reading_time')) {
    /**
     * Calculates and returns the estimated reading time for a post.
     * Assumes an average reading speed of 200 words per minute.
     *
     * @param int|null $post_id Post ID; defaults to current post.
     * @return string Bengali reading time string, e.g. "৩ মিনিট পাঠ".
     */
    function htbd_reading_time($post_id = null) {
        $post = get_post($post_id);
        if (!$post) {
            return '1 min read';
        }

        $content    = strip_tags(strip_shortcodes($post->post_content));
        $words      = preg_split('/\s+/u', trim($content), -1, PREG_SPLIT_NO_EMPTY);
        $word_count = count($words);
        $minutes    = max(1, (int) ceil($word_count / 200));

        return $minutes . ' min read';
    }
}

if (!function_exists('htbd_author_badge')) {
    /**
     * Returns verified author badge HTML string.
     * Includes avatar, author name link, and a verified checkmark icon.
     *
     * @param int|null $author_id Author user ID; defaults to current post author.
     * @return string Author badge HTML.
     */
    function htbd_author_badge($author_id = null) {
        if (!$author_id) {
            $author_id = (int) get_the_author_meta('ID');
        }

        $author_name = esc_html(get_the_author_meta('display_name', $author_id));
        $author_url  = esc_url(get_author_posts_url($author_id));
        $avatar      = get_avatar($author_id, 32, '', $author_name, array('class' => 'ht-author-img'));

        $html  = '<div class="ht-author-pill" itemprop="author" itemscope itemtype="https://schema.org/Person">';
        if ($avatar) {
            $html .= $avatar;
        }
        $html .= '<a href="' . $author_url . '" class="ht-author-name" itemprop="url"><span itemprop="name">' . $author_name . '</span></a>';
        $html .= '<svg class="ht-verified-icon" width="14" height="14" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false">';
        $html .= '<path d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" stroke="#2563eb" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>';
        $html .= '</svg>';
        $html .= '</div>';

        return $html;
    }
}

if (!function_exists('htbd_category_badge')) {
    /**
     * Returns the primary category as a styled badge anchor HTML string.
     *
     * @param int|null $post_id  Post ID; defaults to current post.
     * @param string   $classes  Additional CSS classes to append.
     * @return string  Category badge anchor HTML, or empty string if no category.
     */
    function htbd_category_badge($post_id = null, $classes = '') {
        $primary = htbd_primary_category($post_id);
        if (!$primary) {
            return '';
        }

        $base_class  = 'ht-badge ht-cat-' . esc_attr($primary['slug']);
        $extra       = $classes ? ' ' . esc_attr($classes) : '';
        $final_class = $base_class . $extra;

        return sprintf(
            '<a href="%s" class="%s">%s</a>',
            esc_url($primary['url']),
            $final_class,
            esc_html($primary['name'])
        );
    }
}

if (!function_exists('htbd_get_breadcrumbs')) {
    /**
     * Returns breadcrumb HTML for the current page.
     * Uses Rank Math breadcrumbs if available, falls back to Yoast SEO,
     * then falls back to a custom built breadcrumb trail.
     *
     * @return string Breadcrumb HTML string.
     */
    function htbd_get_breadcrumbs() {
        // Rank Math breadcrumbs.
        if (function_exists('rank_math_the_breadcrumbs')) {
            ob_start();
            rank_math_the_breadcrumbs();
            return ob_get_clean();
        }

        // Yoast SEO breadcrumbs.
        if (function_exists('yoast_breadcrumb')) {
            ob_start();
            yoast_breadcrumb('<nav class="ht-breadcrumbs" aria-label="breadcrumb">', '</nav>');
            return ob_get_clean();
        }

        // Custom fallback breadcrumb trail.
        $html  = '<nav class="ht-breadcrumbs" aria-label="breadcrumb">';
        $html .= '<ol class="ht-breadcrumb-list" itemscope itemtype="https://schema.org/BreadcrumbList">';

        $position = 1;

        // Home.
        $html .= sprintf(
            '<li class="ht-breadcrumb-item" itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem"><a href="%s" itemprop="item"><span itemprop="name">হোম</span></a><meta itemprop="position" content="%d" /></li>',
            esc_url(home_url('/')),
            $position
        );
        $position++;

        if (is_category()) {
            $cat = get_queried_object();
            if ($cat->parent) {
                $parent = get_category($cat->parent);
                $html  .= sprintf(
                    '<li class="ht-breadcrumb-item" itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem"><a href="%s" itemprop="item"><span itemprop="name">%s</span></a><meta itemprop="position" content="%d" /></li>',
                    esc_url(get_category_link($parent->term_id)),
                    esc_html($parent->name),
                    $position
                );
                $position++;
            }
            $html .= '<li class="ht-breadcrumb-item current" aria-current="page">' . esc_html($cat->name) . '</li>';

        } elseif (is_tag()) {
            $html .= '<li class="ht-breadcrumb-item current" aria-current="page">ট্যাগ: ' . esc_html(single_tag_title('', false)) . '</li>';

        } elseif (is_single()) {
            $primary = htbd_primary_category(get_the_ID());
            if ($primary) {
                $html .= sprintf(
                    '<li class="ht-breadcrumb-item" itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem"><a href="%s" itemprop="item"><span itemprop="name">%s</span></a><meta itemprop="position" content="%d" /></li>',
                    esc_url($primary['url']),
                    esc_html($primary['name']),
                    $position
                );
                $position++;
            }
            $html .= '<li class="ht-breadcrumb-item current" aria-current="page">' . esc_html(get_the_title()) . '</li>';

        } elseif (is_page()) {
            $html .= '<li class="ht-breadcrumb-item current" aria-current="page">' . esc_html(get_the_title()) . '</li>';

        } elseif (is_search()) {
            $html .= '<li class="ht-breadcrumb-item current" aria-current="page">অনুসন্ধান: ' . esc_html(get_search_query()) . '</li>';

        } elseif (is_404()) {
            $html .= '<li class="ht-breadcrumb-item current" aria-current="page">পাতা পাওয়া যায়নি</li>';
        }

        $html .= '</ol></nav>';
        return $html;
    }
}

if (!function_exists('ht_breadcrumbs')) {
    /**
     * Backward-compatible echo wrapper for breadcrumbs.
     */
    function ht_breadcrumbs() {
        echo htbd_get_breadcrumbs();
    }
}

if (!function_exists('htbd_post_views')) {
    /**
     * Returns the total view count for a post.
     * Uses the WP options API with a post-specific meta key.
     *
     * @param int $post_id Post ID.
     * @return int Total view count.
     */
    function htbd_post_views($post_id) {
        $post_id = (int) $post_id;
        $count   = (int) get_post_meta($post_id, 'ht_post_views_count', true);
        if (!$count) {
            $count = (int) get_post_meta($post_id, 'htbd_post_views_count', true);
        }
        return $count;
    }
}

if (!function_exists('htbd_increment_post_views')) {
    /**
     * Increments the view counter for a single post.
     * Should be called on `wp` action for singular post pages.
     * Skips bots and logged-in administrators/editors to prevent inflation.
     *
     * @param int $post_id Post ID.
     * @return void
     */
    function htbd_increment_post_views($post_id) {
        $post_id = (int) $post_id;
        if (!$post_id) {
            return;
        }

        // Skip editors and admins from inflating counts.
        if (current_user_can('edit_posts')) {
            return;
        }

        $current = htbd_post_views($post_id);
        update_post_meta($post_id, 'ht_post_views_count', $current + 1);
        update_post_meta($post_id, 'htbd_post_views_count', $current + 1);
    }
}

if (!function_exists('htbd_post_meta')) {
    /**
     * Outputs standardized post metadata (date and reading time).
     *
     * @param int|null $post_id Post ID; defaults to current post.
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
        echo '<svg class="ht-icon" width="14" height="14" viewBox="0 0 24 24" fill="none" aria-hidden="true"><rect x="3" y="4" width="18" height="18" rx="2" stroke="currentColor" stroke-width="2"/><line x1="16" y1="2" x2="16" y2="6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><line x1="8" y1="2" x2="8" y2="6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><line x1="3" y1="10" x2="21" y2="10" stroke="currentColor" stroke-width="2"/></svg>';
        echo ' ' . $time_string; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped
        echo '</span>';

        echo '<span class="ht-meta-item">';
        echo '<svg class="ht-icon" width="14" height="14" viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2"/><polyline points="12 6 12 12 16 14" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
        echo ' ' . esc_html(htbd_reading_time($post_id));
        echo '</span>';
        echo '</div>';
    }
}


if (!function_exists('htbd_output_faq_schema')) {
    /**
     * Parses post content for FAQ pairs and outputs FAQPage Schema.org JSON-LD.
     * Supports <details>/<summary> pairs as well as <h3> question + <p> answer patterns.
     * Outputs FAQPage JSON-LD if 2 or more FAQ pairs are found.
     *
     * @param int|null $post_id Post ID; defaults to current post.
     * @return void
     */
    function htbd_output_faq_schema($post_id = null) {
        $post_id = $post_id ? (int) $post_id : get_the_ID();
        $post    = get_post($post_id);
        if (!$post || empty($post->post_content)) {
            return;
        }

        $content = $post->post_content;
        $faqs    = array();

        // 1. Check for <details><summary>Question</summary>Answer</details> pattern
        if (preg_match_all('/<details\b[^>]*>[\s\r\n]*<summary\b[^>]*>(.*?)<\/summary>([\s\S]*?)<\/details>/iu', $content, $details_matches, PREG_SET_ORDER)) {
            foreach ($details_matches as $dm) {
                $q = trim(wp_strip_all_tags($dm[1]));
                $a = trim(wp_strip_all_tags($dm[2]));
                if (!empty($q) && !empty($a)) {
                    $faqs[] = array(
                        'question' => $q,
                        'answer'   => $a,
                    );
                }
            }
        }

        // 2. Fall back to <h3>Question</h3> followed by <p>Answer</p> pattern if < 2 FAQs found
        if (count($faqs) < 2) {
            if (preg_match_all('/<h3\b[^>]*>(.*?)<\/h3>\s*<p\b[^>]*>(.*?)<\/p>/isu', $content, $h3_matches, PREG_SET_ORDER)) {
                $candidate_faqs = array();
                foreach ($h3_matches as $hm) {
                    $q = trim(wp_strip_all_tags($hm[1]));
                    $a = trim(wp_strip_all_tags($hm[2]));
                    if (mb_strlen($q) >= 4 && mb_strlen($a) >= 10) {
                        $candidate_faqs[] = array(
                            'question' => $q,
                            'answer'   => $a,
                        );
                    }
                }
                if (count($candidate_faqs) >= 2) {
                    $faqs = $candidate_faqs;
                }
            }
        }

        // Require at least 2 FAQ pairs
        if (count($faqs) < 2) {
            return;
        }

        $main_entity = array();
        foreach ($faqs as $faq) {
            $main_entity[] = array(
                '@type'          => 'Question',
                'name'           => esc_html($faq['question']),
                'acceptedAnswer' => array(
                    '@type' => 'Answer',
                    'text'  => esc_html($faq['answer']),
                ),
            );
        }

        $schema_faq = array(
            '@context'   => 'https://schema.org',
            '@type'      => 'FAQPage',
            'mainEntity' => $main_entity,
        );

        echo '<script type="application/ld+json">' . "\n";
        echo wp_json_encode($schema_faq, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT) . "\n";
        echo '</script>' . "\n";
    }
}

if (!function_exists('htbd_output_breadcrumb_schema')) {
    /**
     * Outputs BreadcrumbList Schema.org JSON-LD for rich snippets.
     * Skipped if Rank Math or Yoast SEO handles breadcrumbs/schema.
     * Works for: homepage, category, single post, page, search, author, tag, date.
     *
     * @return void
     */
    function htbd_output_breadcrumb_schema() {
        if (function_exists('rank_math_the_seo_title') || defined('WPSEO_VERSION')) {
            return;
        }

        $items    = array();
        $position = 1;

        // 1. Home item (always first)
        $items[] = array(
            '@type'    => 'ListItem',
            'position' => $position,
            'name'     => 'হোম',
            'item'     => esc_url(home_url('/')),
        );
        $position++;

        if (is_front_page() || is_home()) {
            // Homepage only has Home item
        } elseif (is_category()) {
            $cat = get_queried_object();
            if ($cat && !is_wp_error($cat)) {
                if ($cat->parent) {
                    $ancestors = array_reverse(get_ancestors($cat->term_id, 'category'));
                    foreach ($ancestors as $ancestor_id) {
                        $ancestor = get_category($ancestor_id);
                        if ($ancestor && !is_wp_error($ancestor)) {
                            $items[] = array(
                                '@type'    => 'ListItem',
                                'position' => $position,
                                'name'     => esc_html($ancestor->name),
                                'item'     => esc_url(get_category_link($ancestor->term_id)),
                            );
                            $position++;
                        }
                    }
                }
                $items[] = array(
                    '@type'    => 'ListItem',
                    'position' => $position,
                    'name'     => esc_html($cat->name),
                    'item'     => esc_url(get_category_link($cat->term_id)),
                );
            }
        } elseif (is_singular('post')) {
            $post_id = get_the_ID();
            $primary = function_exists('htbd_primary_category') ? htbd_primary_category($post_id) : null;
            if ($primary) {
                $cat_obj = get_category_by_slug($primary['slug']);
                if ($cat_obj && $cat_obj->parent) {
                    $ancestors = array_reverse(get_ancestors($cat_obj->term_id, 'category'));
                    foreach ($ancestors as $ancestor_id) {
                        $ancestor = get_category($ancestor_id);
                        if ($ancestor && !is_wp_error($ancestor)) {
                            $items[] = array(
                                '@type'    => 'ListItem',
                                'position' => $position,
                                'name'     => esc_html($ancestor->name),
                                'item'     => esc_url(get_category_link($ancestor->term_id)),
                            );
                            $position++;
                        }
                    }
                }
                $items[] = array(
                    '@type'    => 'ListItem',
                    'position' => $position,
                    'name'     => esc_html($primary['name']),
                    'item'     => esc_url($primary['url']),
                );
                $position++;
            }
            $items[] = array(
                '@type'    => 'ListItem',
                'position' => $position,
                'name'     => esc_html(wp_strip_all_tags(get_the_title($post_id))),
                'item'     => esc_url(get_permalink($post_id)),
            );
        } elseif (is_page()) {
            $page_id   = get_the_ID();
            $ancestors = get_post_ancestors($page_id);
            if (!empty($ancestors)) {
                $ancestors = array_reverse($ancestors);
                foreach ($ancestors as $ancestor_id) {
                    $items[] = array(
                        '@type'    => 'ListItem',
                        'position' => $position,
                        'name'     => esc_html(wp_strip_all_tags(get_the_title($ancestor_id))),
                        'item'     => esc_url(get_permalink($ancestor_id)),
                    );
                    $position++;
                }
            }
            $items[] = array(
                '@type'    => 'ListItem',
                'position' => $position,
                'name'     => esc_html(wp_strip_all_tags(get_the_title($page_id))),
                'item'     => esc_url(get_permalink($page_id)),
            );
        } elseif (is_tag()) {
            $tag = get_queried_object();
            if ($tag && !is_wp_error($tag)) {
                $items[] = array(
                    '@type'    => 'ListItem',
                    'position' => $position,
                    'name'     => esc_html('ট্যাগ: ' . $tag->name),
                    'item'     => esc_url(get_tag_link($tag->term_id)),
                );
            }
        } elseif (is_author()) {
            $author_id = (int) get_queried_object_id();
            $items[]   = array(
                '@type'    => 'ListItem',
                'position' => $position,
                'name'     => esc_html(get_the_author_meta('display_name', $author_id)),
                'item'     => esc_url(get_author_posts_url($author_id)),
            );
        } elseif (is_search()) {
            $items[] = array(
                '@type'    => 'ListItem',
                'position' => $position,
                'name'     => esc_html('অনুসন্ধান: ' . get_search_query()),
                'item'     => esc_url(get_search_link()),
            );
        } elseif (is_404()) {
            $items[] = array(
                '@type'    => 'ListItem',
                'position' => $position,
                'name'     => 'পাতা পাওয়া যায়নি',
                'item'     => esc_url(home_url(add_query_arg(null, null))),
            );
        }

        if (empty($items)) {
            return;
        }

        $schema = array(
            '@context'        => 'https://schema.org',
            '@type'           => 'BreadcrumbList',
            'itemListElement' => $items,
        );

        echo '<script type="application/ld+json">' . "\n";
        echo wp_json_encode($schema, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT) . "\n";
        echo '</script>' . "\n";
    }
}

if (!function_exists('htbd_output_blogposting_schema')) {
    /**
     * Outputs BlogPosting Schema.org JSON-LD for single post articles.
     * Skipped if Rank Math or Yoast SEO is active.
     *
     * @param int|null $post_id Post ID; defaults to current post.
     * @return void
     */
    function htbd_output_blogposting_schema($post_id = null) {
        if (function_exists('rank_math_the_seo_title') || defined('WPSEO_VERSION')) {
            return;
        }

        $post_id = $post_id ? (int) $post_id : get_the_ID();
        $post    = get_post($post_id);
        if (!$post) {
            return;
        }

        $post_url       = get_permalink($post_id);
        $author_id      = (int) $post->post_author;
        $headline       = wp_strip_all_tags(get_the_title($post_id));
        $excerpt        = has_excerpt($post_id) ? get_the_excerpt($post_id) : wp_trim_words(strip_shortcodes($post->post_content), 35, '...');
        $description    = wp_strip_all_tags($excerpt);
        $content_clean  = strip_tags(strip_shortcodes($post->post_content));
        $words          = preg_split('/\s+/u', trim($content_clean), -1, PREG_SPLIT_NO_EMPTY);
        $word_count     = is_array($words) ? count($words) : 0;
        $date_published = get_the_date('c', $post_id);
        $date_modified  = get_the_modified_date('c', $post_id);

        if (has_post_thumbnail($post_id)) {
            $image_url = get_the_post_thumbnail_url($post_id, 'full');
        } else {
            $image_url = function_exists('htbd_get_default_thumbnail') ? htbd_get_default_thumbnail() : get_template_directory_uri() . '/assets/images/default-thumbnail.webp';
        }

        $publisher_logo = get_template_directory_uri() . '/assets/images/logo.png';
        $custom_logo_id = get_theme_mod('custom_logo');
        if ($custom_logo_id) {
            $logo_src = wp_get_attachment_image_src($custom_logo_id, 'full');
            if (!empty($logo_src[0])) {
                $publisher_logo = $logo_src[0];
            }
        }

        $schema = array(
            '@context'         => 'https://schema.org',
            '@type'            => 'BlogPosting',
            'headline'         => esc_html($headline),
            'description'      => esc_html($description),
            'image'            => esc_url($image_url),
            'author'           => array(
                '@type' => 'Person',
                'name'  => esc_html(get_the_author_meta('display_name', $author_id)),
                'url'   => esc_url(get_author_posts_url($author_id)),
            ),
            'publisher'        => array(
                '@type' => 'Organization',
                'name'  => 'HelpTrickBD',
                'logo'  => array(
                    '@type' => 'ImageObject',
                    'url'   => esc_url($publisher_logo),
                ),
            ),
            'datePublished'    => $date_published,
            'dateModified'     => $date_modified,
            'mainEntityOfPage' => array(
                '@type' => 'WebPage',
                '@id'   => esc_url($post_url),
            ),
            'wordCount'        => (int) $word_count,
            'inLanguage'       => 'bn-BD',
        );

        echo '<script type="application/ld+json">' . "\n";
        echo wp_json_encode($schema, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT) . "\n";
        echo '</script>' . "\n";
    }
}

if (!function_exists('htbd_advanced_pagination')) {
    /**
     * Renders modern advanced pagination with status info and numbered buttons.
     *
     * @param WP_Query|null $query Custom query or defaults to global $wp_query.
     */
    function htbd_advanced_pagination($query = null) {
        if (!$query) {
            global $wp_query;
            $query = $wp_query;
        }

        $total_pages = (int) $query->max_num_pages;
        if ($total_pages <= 1) {
            return;
        }

        $current_page = max(1, get_query_var('paged'), get_query_var('page'));
        $total_posts  = (int) $query->found_posts;
        $posts_per_page = (int) $query->get('posts_per_page');
        if ($posts_per_page <= 0) {
            $posts_per_page = (int) get_option('posts_per_page', 10);
        }

        $start_post = (($current_page - 1) * $posts_per_page) + 1;
        $end_post   = min($current_page * $posts_per_page, $total_posts);

        echo '<nav class="ht-adv-pagination" aria-label="' . esc_attr__('Pagination Navigation', 'helptrickbd-edu') . '">';
        
        // Page status info bar
        echo '<div class="ht-adv-page-info">';
        printf(
            /* translators: 1: current page, 2: total pages, 3: start post, 4: end post, 5: total posts */
            esc_html__('Page %1$d of %2$d • Showing %3$d–%4$d of %5$d Articles', 'helptrickbd-edu'),
            $current_page,
            $total_pages,
            $start_post,
            $end_post,
            $total_posts
        );
        echo '</div>';

        // Page buttons list
        echo '<ul class="ht-adv-page-list">';

        // « First button
        if ($current_page > 1) {
            echo '<li class="ht-adv-item"><a href="' . esc_url(get_pagenum_link(1)) . '" class="ht-adv-btn ht-adv-first" aria-label="' . esc_attr__('First Page', 'helptrickbd-edu') . '">&laquo; First</a></li>';
            echo '<li class="ht-adv-item"><a href="' . esc_url(get_pagenum_link($current_page - 1)) . '" class="ht-adv-btn ht-adv-prev" aria-label="' . esc_attr__('Previous Page', 'helptrickbd-edu') . '">&lsaquo; Prev</a></li>';
        } else {
            echo '<li class="ht-adv-item disabled"><span class="ht-adv-btn ht-adv-first" aria-disabled="true">&laquo; First</span></li>';
            echo '<li class="ht-adv-item disabled"><span class="ht-adv-btn ht-adv-prev" aria-disabled="true">&lsaquo; Prev</span></li>';
        }

        // Numbered buttons with ellipsis
        $mid_size = 2;
        $start_loop = max(1, $current_page - $mid_size);
        $end_loop   = min($total_pages, $current_page + $mid_size);

        if ($start_loop > 1) {
            echo '<li class="ht-adv-item"><a href="' . esc_url(get_pagenum_link(1)) . '" class="ht-adv-btn ht-adv-num">1</a></li>';
            if ($start_loop > 2) {
                echo '<li class="ht-adv-item ht-adv-dots"><span>&hellip;</span></li>';
            }
        }

        for ($i = $start_loop; $i <= $end_loop; $i++) {
            if ($i === $current_page) {
                echo '<li class="ht-adv-item active"><span class="ht-adv-btn ht-adv-num active" aria-current="page">' . esc_html($i) . '</span></li>';
            } else {
                echo '<li class="ht-adv-item"><a href="' . esc_url(get_pagenum_link($i)) . '" class="ht-adv-btn ht-adv-num">' . esc_html($i) . '</a></li>';
            }
        }

        if ($end_loop < $total_pages) {
            if ($end_loop < $total_pages - 1) {
                echo '<li class="ht-adv-item ht-adv-dots"><span>&hellip;</span></li>';
            }
            echo '<li class="ht-adv-item"><a href="' . esc_url(get_pagenum_link($total_pages)) . '" class="ht-adv-btn ht-adv-num">' . esc_html($total_pages) . '</a></li>';
        }

        // Next › and Last » buttons
        if ($current_page < $total_pages) {
            echo '<li class="ht-adv-item"><a href="' . esc_url(get_pagenum_link($current_page + 1)) . '" class="ht-adv-btn ht-adv-next" aria-label="' . esc_attr__('Next Page', 'helptrickbd-edu') . '">Next &rsaquo;</a></li>';
            echo '<li class="ht-adv-item"><a href="' . esc_url(get_pagenum_link($total_pages)) . '" class="ht-adv-btn ht-adv-last" aria-label="' . esc_attr__('Last Page', 'helptrickbd-edu') . '">Last &raquo;</a></li>';
        } else {
            echo '<li class="ht-adv-item disabled"><span class="ht-adv-btn ht-adv-next" aria-disabled="true">Next &rsaquo;</span></li>';
            echo '<li class="ht-adv-item disabled"><span class="ht-adv-btn ht-adv-last" aria-disabled="true">Last &raquo;</span></li>';
        }

        echo '</ul>';
        echo '</nav>';
    }
}
