<?php
/**
 * HelpTrickBD Pro - Complete Schema.org JSON-LD Structured Data Engine
 * Outputs Google Rich Results compliant JSON-LD for Article, BreadcrumbList, FAQPage,
 * WebSite (Sitelinks Searchbox), and Organization.
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Output Rich JSON-LD Structured Data in head.
 */
function ht_render_schema_jsonld() {
    $schemas = [];

    // 1. WebSite & Organization Schema (Site-wide)
    if (is_front_page() || is_home()) {
        $schemas[] = [
            '@context'        => 'https://schema.org',
            '@type'           => 'WebSite',
            '@id'             => home_url('/#website'),
            'url'             => home_url('/'),
            'name'            => get_bloginfo('name'),
            'description'     => get_bloginfo('description'),
            'inLanguage'      => 'bn-BD',
            'potentialAction' => [
                '@type'       => 'SearchAction',
                'target'      => [
                    '@type'       => 'EntryPoint',
                    'urlTemplate' => home_url('/?s={search_term_string}'),
                ],
                'query-input' => 'required name=search_term_string',
            ],
        ];

        $logo_url = '';
        $custom_logo_id = get_theme_mod('custom_logo');
        if ($custom_logo_id) {
            $logo_url = wp_get_attachment_image_url($custom_logo_id, 'full');
        }

        $same_as = array_filter([
            get_theme_mod('ht_facebook_url', ''),
            get_theme_mod('ht_telegram_url', ''),
            get_theme_mod('ht_whatsapp_url', ''),
            get_theme_mod('ht_youtube_url', ''),
        ]);

        $schemas[] = [
            '@context'    => 'https://schema.org',
            '@type'       => 'EducationalOrganization',
            '@id'         => home_url('/#organization'),
            'name'        => get_bloginfo('name'),
            'url'         => home_url('/'),
            'logo'        => !empty($logo_url) ? [
                '@type'  => 'ImageObject',
                'url'    => esc_url($logo_url),
            ] : null,
            'sameAs'      => array_values($same_as),
            'description' => get_bloginfo('description'),
        ];
    }

    // 2. Article / EducationalArticle Schema for Single Posts
    if (is_singular('post')) {
        $post_id   = get_the_ID();
        $post      = get_post($post_id);
        $permalink = get_permalink($post_id);

        // Featured image
        $image_url = '';
        if (has_post_thumbnail($post_id)) {
            $image_url = get_the_post_thumbnail_url($post_id, 'full');
        } else {
            // Check first image in content
            if (preg_match('/<img[^>]+src=[\'"]([^\'"]+)[\'"]/', $post->post_content, $m)) {
                $image_url = $m[1];
            }
        }

        // Author info
        $author_id   = $post->post_author;
        $author_name = get_the_author_meta('display_name', $author_id);
        $author_url  = get_author_posts_url($author_id);

        // Description
        $description = get_post_meta($post_id, 'rank_math_description', true);
        if (empty($description)) {
            $description = wp_strip_all_tags(get_the_excerpt($post_id));
        }

        // Word Count
        $clean_content = wp_strip_all_tags(strip_shortcodes($post->post_content));
        $word_count    = count(preg_split('/\s+/u', $clean_content, -1, PREG_SPLIT_NO_EMPTY));

        $article_type = 'Article';
        $categories   = get_the_category($post_id);
        if (!empty($categories)) {
            $cat_slug = $categories[0]->slug;
            if (strpos($cat_slug, 'tech') !== false || strpos($cat_slug, 'ict') !== false) {
                $article_type = 'TechArticle';
            } elseif (strpos($cat_slug, 'education') !== false || strpos($cat_slug, 'nu') !== false || strpos($cat_slug, 'honours') !== false) {
                $article_type = 'EducationalArticle';
            }
        }

        $logo_url = '';
        $custom_logo_id = get_theme_mod('custom_logo');
        if ($custom_logo_id) {
            $logo_url = wp_get_attachment_image_url($custom_logo_id, 'full');
        }

        $schemas[] = [
            '@context'         => 'https://schema.org',
            '@type'            => $article_type,
            '@id'              => $permalink . '#article',
            'isPartOf'         => [
                '@type' => 'WebPage',
                '@id'   => $permalink,
                'url'   => $permalink,
                'name'  => get_the_title($post_id),
            ],
            'headline'         => get_the_title($post_id),
            'description'      => $description,
            'mainEntityOfPage' => [
                '@type' => 'WebPage',
                '@id'   => $permalink,
            ],
            'url'              => $permalink,
            'datePublished'    => get_the_date('c', $post_id),
            'dateModified'     => get_the_modified_date('c', $post_id),
            'author'           => [
                '@type' => 'Person',
                'name'  => $author_name,
                'url'   => esc_url($author_url),
            ],
            'publisher'        => [
                '@type' => 'Organization',
                'name'  => get_bloginfo('name'),
                'url'   => home_url('/'),
                'logo'  => !empty($logo_url) ? [
                    '@type' => 'ImageObject',
                    'url'   => esc_url($logo_url),
                ] : null,
            ],
            'image'            => !empty($image_url) ? [
                '@type' => 'ImageObject',
                'url'   => esc_url($image_url),
            ] : null,
            'wordCount'        => (int) $word_count,
            'inLanguage'       => 'bn-BD',
        ];

        // 3. Auto-detect FAQ Q&A patterns in post content
        $faq_items = ht_extract_faqs_from_content($post->post_content);
        if (!empty($faq_items)) {
            $schemas[] = [
                '@context'   => 'https://schema.org',
                '@type'      => 'FAQPage',
                'mainEntity' => $faq_items,
            ];
        }
    }

    // 4. Output Schemas as JSON-LD
    foreach ($schemas as $schema) {
        if (!empty($schema)) {
            echo '<script type="application/ld+json">' . wp_json_encode($schema, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_PRETTY_PRINT) . '</script>' . "\n";
        }
    }
}
add_action('wp_head', 'ht_render_schema_jsonld', 2);

/**
 * Helper to auto-extract FAQs from content.
 * Matches headings containing 'প্রশ্ন', 'FAQ', '?' followed by paragraphs.
 *
 * @param string $content Post content HTML.
 * @return array Schema.org Question array.
 */
function ht_extract_faqs_from_content($content) {
    if (empty($content)) {
        return [];
    }

    $faqs = [];
    // Match h2/h3/h4 followed by paragraph
    $pattern = '/<(h[2-4])[^>]*>(.*?(?:\?|প্রশ্ন|FAQ).*?)<\/\1>\s*<p[^>]*>(.*?)<\/p>/ius';
    if (preg_match_all($pattern, $content, $matches, PREG_SET_ORDER)) {
        $count = 0;
        foreach ($matches as $match) {
            if ($count >= 6) {
                break; // Max 6 FAQs for rich snippet
            }
            $question = wp_strip_all_tags($match[2]);
            $answer   = wp_strip_all_tags($match[3]);

            if (mb_strlen($question) > 5 && mb_strlen($answer) > 10) {
                $faqs[] = [
                    '@type'          => 'Question',
                    'name'           => $question,
                    'acceptedAnswer' => [
                        '@type' => 'Answer',
                        'text'  => $answer,
                    ],
                ];
                $count++;
            }
        }
    }

    return $faqs;
}
