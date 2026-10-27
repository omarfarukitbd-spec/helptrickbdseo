<?php
/**
 * HelpTrickBD Pro - 1-Click Database Migrator & SEO Optimizer
 * Automatically optimizes legacy Blogger links, Rank Math SEO metadata,
 * and featured images directly inside WordPress without phpMyAdmin.
 * Zero-Emoji compliance (Rule 12).
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Runs complete database optimization across all published posts.
 *
 * @return array Summary of actions performed.
 */
function ht_run_database_optimization() {
    global $wpdb;

    $summary = [
        'posts_processed' => 0,
        'links_updated'   => 0,
        'seo_meta_set'    => 0,
        'thumbs_bound'    => 0,
        'start_time'      => current_time('mysql'),
    ];

    // Predefined aliases for Blogger truncated slugs
    $aliases = [
        'ssc-english-2nd-paper-suggestion-2027'       => 'ssc-english-2nd-paper-final-suggestion',
        'bcs-preliminary-marks-distribution-booklist' => 'bcs-preliminary-marks-distribution_01436475916',
        'remittance-importance'                       => 'what-is-remittance-importance-economy-obstacles',
        'basic-economy-problems-bd'                   => 'bangladesh-basic-economy-features-problems-solutions',
        'budget-importance'                           => 'what-is-budget-importance-role-economy',
        'nu-cgpa-calculator'                          => 'nu-cgpa-calculator',
        'bangladesh-population-features'              => 'bangladesh-population-features-trends-challenges',
        'computer-types'                              => 'computer-types-classification-analog-digital-hybrid',
        'computer-generations'                        => 'computer-generations-first-to-fifth-technology',
        'computer-history'                            => 'computer-history-abacus-to-modern-processors',
        'computer-definition'                         => 'what-is-computer-definition-functions-components',
        'alim-exam-routine'                           => 'alim-exam-routine-2025-madrasah-board',
    ];

    $base_url = rtrim(home_url(), '/');

    // Fetch all published posts
    $posts = $wpdb->get_results("SELECT ID, post_title, post_name, post_content FROM {$wpdb->posts} WHERE post_type = 'post' AND post_status = 'publish'");

    if (empty($posts)) {
        return $summary;
    }

    foreach ($posts as $post) {
        $summary['posts_processed']++;
        $content = $post->post_content;
        $content_changed = false;

        // 1. Rewrite Legacy Internal Links in post_content
        if (stripos($content, '.html') !== false) {
            $new_content = preg_replace_callback('/<a\s+([^>]*?)href=(["\'])(.*?)\2([^>]*?)>/is', function ($matches) use ($aliases, $base_url, &$summary, &$content_changed) {
                $before_href = $matches[1];
                $quote       = $matches[2];
                $href        = trim($matches[3]);
                $after_href  = $matches[4];

                $is_internal = (
                    stripos($href, 'helptrickbd.com') !== false ||
                    stripos($href, 'blogspot.com') !== false ||
                    preg_match('#^/(?:p/|\d{4}/\d{2}/)#i', $href)
                );

                if (!$is_internal || stripos($href, '.html') === false) {
                    return $matches[0];
                }

                $fragment = '';
                if (strpos($href, '#') !== false) {
                    list($href, $fragment) = explode('#', $href, 2);
                    $fragment = '#' . $fragment;
                }

                if (preg_match('#/(?:p/|\d{4}/\d{2}/)?([^/]+)\.html$#i', $href, $slug_matches)) {
                    $raw_slug   = strtolower($slug_matches[1]);
                    $clean_slug = preg_replace('/_\d+$/', '', $raw_slug);
                    $target_slug = $aliases[$raw_slug] ?? ($aliases[$clean_slug] ?? $clean_slug);
                    $new_url = $base_url . '/' . sanitize_title($target_slug) . '/' . $fragment;

                    if ($href !== $new_url) {
                        $summary['links_updated']++;
                        $content_changed = true;
                        return '<a ' . $before_href . 'href=' . $quote . esc_url($new_url) . $quote . $after_href . '>';
                    }
                }

                return $matches[0];
            }, $content);

            if ($content_changed && $new_content !== $content) {
                $wpdb->update(
                    $wpdb->posts,
                    ['post_content' => $new_content],
                    ['ID' => $post->ID]
                );
                $content = $new_content;
            }
        }

        // 2. Rank Math SEO Postmeta Injection
        $current_kw   = get_post_meta($post->ID, 'rank_math_focus_keyword', true);
        $current_desc = get_post_meta($post->ID, 'rank_math_description', true);

        if (empty($current_kw) || empty($current_desc)) {
            // Determine Focus Keyword
            $title = html_entity_decode($post->post_title, ENT_QUOTES, 'UTF-8');
            $clean_title = preg_replace('/\b202[4-9]\b/', '', $title);
            $parts = preg_split('/[|\-–—:]/u', $clean_title);
            $focus_kw = trim($parts[0]);
            if (mb_strlen($focus_kw, 'UTF-8') < 4) {
                $focus_kw = trim($title);
            }

            // Determine Clean Bengali Meta Description
            $text_corpus = wp_strip_all_tags($content);
            $text_corpus = preg_replace('/\s+/u', ' ', $text_corpus);
            $text_corpus = trim($text_corpus);

            $meta_desc = '';
            if (!empty($text_corpus)) {
                $sentences = explode('।', $text_corpus);
                foreach ($sentences as $s) {
                    $s = trim($s);
                    if (empty($s)) continue;
                    if (empty($meta_desc)) {
                        $meta_desc = $s;
                    } elseif (mb_strlen($meta_desc . '। ' . $s, 'UTF-8') <= 155) {
                        $meta_desc .= '। ' . $s;
                    } else {
                        break;
                    }
                }
                if (!empty($meta_desc) && !str_ends_with($meta_desc, '।')) {
                    $meta_desc .= '।';
                }
            }

            if (empty($meta_desc)) {
                $meta_desc = mb_substr($text_corpus, 0, 150, 'UTF-8') . '...';
            }

            if (empty($current_kw)) {
                update_post_meta($post->ID, 'rank_math_focus_keyword', $focus_kw);
            }
            if (empty($current_desc)) {
                update_post_meta($post->ID, 'rank_math_description', $meta_desc);
            }
            update_post_meta($post->ID, 'rank_math_title', '%title% %sep% %sitename%');

            $summary['seo_meta_set']++;
        }

        // 3. Featured Image Linker
        if (!has_post_thumbnail($post->ID)) {
            if (preg_match('/<img[^>]+src=[\'"]([^\'"]+)[\'"]/i', $content, $img_m)) {
                $img_url = $img_m[1];
                $img_file = basename(parse_url($img_url, PHP_URL_PATH));
                $clean_file_slug = pathinfo($img_file, PATHINFO_FILENAME);

                // Look up existing attachment in database
                $att_id = $wpdb->get_var($wpdb->prepare(
                    "SELECT ID FROM {$wpdb->posts} WHERE post_type = 'attachment' AND (post_name = %s OR guid LIKE %s) LIMIT 1",
                    $clean_file_slug,
                    '%' . $wpdb->esc_like($img_file) . '%'
                ));

                if ($att_id) {
                    set_post_thumbnail($post->ID, $att_id);
                    $summary['thumbs_bound']++;
                }
            }
        }
    }

    // Save execution record
    update_option('ht_last_optimization_summary', $summary);
    update_option('ht_optimization_v1_done', current_time('mysql'));

    return $summary;
}

/**
 * Automatically trigger optimization when theme is activated.
 */
function ht_auto_migrate_on_theme_activation() {
    ht_run_database_optimization();
}
add_action('after_switch_theme', 'ht_auto_migrate_on_theme_activation');

/**
 * Add Admin Menu for HelpTrickBD Optimizer under Tools.
 */
function ht_register_admin_optimizer_menu() {
    add_management_page(
        'HelpTrickBD অপ্টিমাইজার',
        'HelpTrickBD অপ্টিমাইজার',
        'manage_options',
        'ht-optimizer',
        'ht_render_admin_optimizer_page'
    );
}
add_action('admin_menu', 'ht_register_admin_optimizer_menu');

/**
 * Render HelpTrickBD Optimizer Admin Dashboard Page.
 */
function ht_render_admin_optimizer_page() {
    if (!current_user_can('manage_options')) {
        return;
    }

    $message = '';
    if (isset($_POST['ht_run_optimizer']) && check_admin_referer('ht_optimizer_action', 'ht_optimizer_nonce')) {
        $result = ht_run_database_optimization();
        $message = sprintf(
            'সফলভাবে সম্পন্ন হয়েছে! মোট পোস্ট প্রসেস করা হয়েছে: %d, অভ্যন্তরীণ লিঙ্ক রূপান্তর: %d, র‍্যাংক ম্যাথ মেটা যুক্ত: %d, ফিচার্ড ইমেজ বাইন্ড: %d।',
            $result['posts_processed'],
            $result['links_updated'],
            $result['seo_meta_set'],
            $result['thumbs_bound']
        );
    }

    $last_run = get_option('ht_optimization_v1_done', 'এখনো চালানো হয়নি');
    $last_summary = get_option('ht_last_optimization_summary', []);
    ?>
    <div class="wrap" style="max-width: 900px; font-family: 'SolaimanLipi', -apple-system, sans-serif;">
        <h1 style="font-size: 24px; font-weight: 700; color: #1e293b; margin-bottom: 20px;">
            HelpTrickBD Pro - ১-ক্লিক এসইও ও ডাটাবেস অপ্টিমাইজার
        </h1>

        <?php if (!empty($message)) : ?>
            <div class="notice notice-success is-dismissible" style="padding: 12px 16px; font-size: 15px;">
                <p><strong>[সফল]</strong> <?php echo esc_html($message); ?></p>
            </div>
        <?php endif; ?>

        <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 24px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); margin-bottom: 24px;">
            <h2 style="font-size: 18px; margin-top: 0; color: #0f172a;">স্বয়ংক্রিয় অপ্টিমাইজেশন পরিচালনা</h2>
            <p style="color: #475569; font-size: 14px; line-height: 1.6;">
                এই বাটনটিতে ক্লিক করলে থিম স্বয়ংক্রিয়ভাবে ডাটাবেসের সমস্ত পোস্ট স্ক্যান করবে এবং নিচের কাজগুলো সম্পন্ন করবে:
            </p>
            <ul style="list-style: disc; margin-left: 20px; color: #334155; font-size: 14px; line-height: 1.8;">
                <li>ব্লগারে পুরনো সমস্ত <code>.html</code> অভ্যন্তরীণ লিঙ্ক স্থায়ীভাবে ক্লিন পারমালিঙ্কে রূপান্তর।</li>
                <li>র‍্যাংক ম্যাথ (Rank Math) এসইও ফোকাস কি-ওয়ার্ড ও ১৪০-১৫৫ ক্যারেক্টারের প্রমিত মেটা ডেসক্রিপশন ইনজেক্ট।</li>
                <li>পোস্টের ব্যানার ইমেজ স্বয়ংক্রিয়ভাবে নেটিভ <code>featured_media</code> হিসেবে সেট।</li>
            </ul>

            <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin: 20px 0;">
                <p style="margin: 0; font-size: 14px; color: #64748b;">
                    <strong>সর্বশেষ রান করার সময়:</strong> <?php echo esc_html($last_run); ?>
                </p>
                <?php if (!empty($last_summary)) : ?>
                    <p style="margin: 8px 0 0 0; font-size: 13px; color: #64748b;">
                        প্রসেসকৃত পোস্ট: <?php echo intval($last_summary['posts_processed'] ?? 0); ?> | 
                        লিঙ্ক রূপান্তর: <?php echo intval($last_summary['links_updated'] ?? 0); ?> | 
                        মেটা আপডেট: <?php echo intval($last_summary['seo_meta_set'] ?? 0); ?>
                    </p>
                <?php endif; ?>
            </div>

            <form method="post">
                <?php wp_nonce_field('ht_optimizer_action', 'ht_optimizer_nonce'); ?>
                <button type="submit" name="ht_run_optimizer" class="button button-primary button-hero" style="font-size: 15px; font-weight: 600; padding: 10px 24px; height: auto;">
                    ১-ক্লিকে সাইট অপ্টিমাইজ করুন
                </button>
            </form>
        </div>
    </div>
    <?php
}
