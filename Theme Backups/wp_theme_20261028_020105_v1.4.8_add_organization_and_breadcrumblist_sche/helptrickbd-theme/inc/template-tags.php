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
        '<span class="ht-meta-item ht-reading-time" title="%s শব্দ">%s %s মিনিট পড়া</span>',
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
        esc_html(get_the_date('', $post_id))
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
            '<div class="ht-updated-badge" title="%s">%s <span>%s: %s</span></div>',
            esc_attr__('সর্বশেষ হালনাগাদ', 'helptrickbd'),
            ht_m3_icon('history', 16, '', false),
            esc_html__('হালনাগাদ', 'helptrickbd'),
            esc_html(get_the_modified_date('', $post_id))
        );
    }
}

/**
 * Render Google E-E-A-T Fact-Checked Verified Badge.
 */
function ht_eeat_badge() {
    printf(
        '<div class="ht-eeat-badge" title="%s">%s <span>%s</span></div>',
        esc_attr__('শিক্ষক ও গবেষক দ্বারা তথ্য যাচাইকৃত', 'helptrickbd'),
        ht_m3_icon('verified', 18, 'ht-icon-verified', false),
        esc_html__('তথ্য যাচাইকৃত', 'helptrickbd')
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
        '<span class="ht-meta-item ht-views">%s %s %s</span>',
        ht_m3_icon('visibility', 16, '', false),
        esc_html(ht_bn_number(number_format_i18n($count))),
        esc_html__('বার পঠিত', 'helptrickbd')
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

/**
 * Render High-Conversion Multi-Platform Social Share Bar.
 *
 * @param string $location 'top' or 'bottom'.
 * @param int $post_id Post ID.
 */
function ht_social_share_bar($location = 'bottom', $post_id = null) {
    if (!$post_id) {
        $post_id = get_the_ID();
    }

    $permalink = esc_url(get_permalink($post_id));
    $title = rawurlencode(html_entity_decode(get_the_title($post_id), ENT_QUOTES, 'UTF-8'));
    $encoded_url = rawurlencode($permalink);

    $fb_url = "https://www.facebook.com/sharer/sharer.php?u={$encoded_url}";
    $wa_url = "https://api.whatsapp.com/send?text={$title}%20{$encoded_url}";
    $tg_url = "https://t.me/share/url?url={$encoded_url}&text={$title}";
    $tw_url = "https://twitter.com/intent/tweet?text={$title}&url={$encoded_url}";
    $li_url = "https://www.linkedin.com/sharing/share-offsite/?url={$encoded_url}";

    if ($location === 'top') :
    ?>
        <div class="ht-share-bar ht-share-top" aria-label="<?php esc_attr_e('গাইডটি শেয়ার করুন', 'helptrickbd'); ?>">
            <span class="ht-share-label"><?php ht_m3_icon('share', 15); ?> <span><?php esc_html_e('শেয়ার:', 'helptrickbd'); ?></span></span>
            <div class="ht-share-pills">
                <a href="<?php echo esc_url($fb_url); ?>" target="_blank" rel="noopener noreferrer" class="ht-share-btn ht-share-fb" aria-label="<?php esc_attr_e('ফেসবুকে শেয়ার করুন', 'helptrickbd'); ?>" title="Facebook">
                    <?php ht_m3_icon('facebook', 16); ?>
                </a>
                <a href="<?php echo esc_url($wa_url); ?>" target="_blank" rel="noopener noreferrer" class="ht-share-btn ht-share-wa" aria-label="<?php esc_attr_e('হোয়াটসঅ্যাপে শেয়ার করুন', 'helptrickbd'); ?>" title="WhatsApp">
                    <?php ht_m3_icon('whatsapp', 16); ?>
                </a>
                <a href="<?php echo esc_url($tg_url); ?>" target="_blank" rel="noopener noreferrer" class="ht-share-btn ht-share-tg" aria-label="<?php esc_attr_e('টেলিগ্রামে শেয়ার করুন', 'helptrickbd'); ?>" title="Telegram">
                    <?php ht_m3_icon('telegram', 16); ?>
                </a>
                <a href="<?php echo esc_url($tw_url); ?>" target="_blank" rel="noopener noreferrer" class="ht-share-btn ht-share-tw" aria-label="<?php esc_attr_e('এক্স-এ শেয়ার করুন', 'helptrickbd'); ?>" title="X">
                    <?php ht_m3_icon('twitter_x', 14); ?>
                </a>
                <button type="button" class="ht-share-btn ht-share-copy ht-btn-copy-link" data-url="<?php echo esc_url($permalink); ?>" aria-label="<?php esc_attr_e('লিংক কপি করুন', 'helptrickbd'); ?>" title="<?php esc_attr_e('লিংক কপি করুন', 'helptrickbd'); ?>">
                    <?php ht_m3_icon('link', 16); ?>
                </button>
            </div>
        </div>
    <?php else : ?>
        <div class="ht-share-card ht-share-bottom" aria-label="<?php esc_attr_e('সহপাঠীদের সাথে শেয়ার করুন', 'helptrickbd'); ?>">
            <div class="ht-share-card-header">
                <div class="ht-share-icon-wrap">
                    <?php ht_m3_icon('share', 20); ?>
                </div>
                <div class="ht-share-card-text">
                    <h4 class="ht-share-card-title"><?php esc_html_e('সহপাঠী ও বন্ধুদের সাথে শেয়ার করুন', 'helptrickbd'); ?></h4>
                    <p class="ht-share-card-sub"><?php esc_html_e('আপনার সহপাঠী ও বন্ধুদের প্রস্তুতিতে সহায়তা করতে সোশ্যাল মিডিয়ায় শেয়ার করুন।', 'helptrickbd'); ?></p>
                </div>
            </div>
            <div class="ht-share-card-btns">
                <a href="<?php echo esc_url($fb_url); ?>" target="_blank" rel="noopener noreferrer" class="ht-share-large-btn ht-share-fb">
                    <?php ht_m3_icon('facebook', 18); ?>
                    <span>Facebook</span>
                </a>
                <a href="<?php echo esc_url($wa_url); ?>" target="_blank" rel="noopener noreferrer" class="ht-share-large-btn ht-share-wa">
                    <?php ht_m3_icon('whatsapp', 18); ?>
                    <span>WhatsApp</span>
                </a>
                <a href="<?php echo esc_url($tg_url); ?>" target="_blank" rel="noopener noreferrer" class="ht-share-large-btn ht-share-tg">
                    <?php ht_m3_icon('telegram', 18); ?>
                    <span>Telegram</span>
                </a>
                <a href="<?php echo esc_url($tw_url); ?>" target="_blank" rel="noopener noreferrer" class="ht-share-large-btn ht-share-tw">
                    <?php ht_m3_icon('twitter_x', 16); ?>
                    <span>X</span>
                </a>
                <a href="<?php echo esc_url($li_url); ?>" target="_blank" rel="noopener noreferrer" class="ht-share-large-btn ht-share-li">
                    <?php ht_m3_icon('linkedin', 18); ?>
                    <span>LinkedIn</span>
                </a>
                <button type="button" class="ht-share-large-btn ht-share-copy ht-btn-copy-link" data-url="<?php echo esc_url($permalink); ?>">
                    <?php ht_m3_icon('link', 18); ?>
                    <span><?php esc_html_e('লিংক কপি', 'helptrickbd'); ?></span>
                </button>
            </div>
        </div>
    <?php
    endif;
}

/**
 * Render Interactive Post Reactions Box.
 *
 * @param int $post_id Post ID.
 */
function ht_post_reaction_box($post_id = null) {
    if (!$post_id) {
        $post_id = get_the_ID();
    }

    $likes = (int) get_post_meta($post_id, 'ht_post_likes_count', true);
    if ($likes <= 0) {
        $likes = 28;
    }
    ?>
    <div class="ht-reaction-card" id="ht-reaction-card" data-id="<?php echo esc_attr($post_id); ?>">
        <div class="ht-reaction-content">
            <span class="ht-reaction-question"><?php esc_html_e('এই গাইডটি কি আপনার প্রস্তুতিতে সহায়ক হয়েছে?', 'helptrickbd'); ?></span>
            <span class="ht-reaction-sub"><?php esc_html_e('শিক্ষার্থীদের মূল্যায়ন আমাদের নির্ভুল ও মানসম্মত হ্যান্ডনোট তৈরি করতে সহায়তা করে।', 'helptrickbd'); ?></span>
        </div>
        <div class="ht-reaction-action">
            <button type="button" class="ht-reaction-btn" id="ht-btn-like" aria-label="<?php esc_attr_e('সহায়ক হয়েছে', 'helptrickbd'); ?>">
                <?php ht_m3_icon('thumb_up', 20, 'ht-icon-reaction'); ?>
                <span class="ht-reaction-label"><?php esc_html_e('সহায়ক হয়েছে', 'helptrickbd'); ?></span>
                <span class="ht-reaction-count" id="ht-reaction-count-val"><?php echo esc_html(ht_bn_number($likes)); ?></span>
            </button>
        </div>
    </div>
    <?php
}

/**
 * Resolve author avatar image URL with multi-fallback support:
 * 1. Theme Customizer Override
 * 2. WordPress User Meta (Local Avatar Plugins / Custom Uploads)
 * 3. Native WordPress Avatar / Gravatar
 *
 * @param int $author_id User ID.
 * @return string Avatar image URL.
 */
function ht_get_author_avatar_url($author_id = null) {
    if (!$author_id) {
        $author_id = get_post_field('post_author', get_the_ID());
        if (!$author_id) {
            $author_id = get_the_author_meta('ID');
        }
    }

    // 1. Theme Customizer Override
    $customizer_img = get_theme_mod('ht_author_custom_avatar', '');
    if (!empty($customizer_img)) {
        return esc_url($customizer_img);
    }

    // 2. Common User Meta fields used by WordPress Avatar plugins
    $meta_keys = ['wp_user_avatar', 'simple_local_avatar', 'profile_photo', 'user_avatar'];
    foreach ($meta_keys as $key) {
        $meta_val = get_user_meta($author_id, $key, true);
        if (!empty($meta_val)) {
            if (is_numeric($meta_val)) {
                $img = wp_get_attachment_image_url($meta_val, 'full');
                if ($img) return esc_url($img);
            } elseif (is_array($meta_val) && !empty($meta_val['full'])) {
                return esc_url($meta_val['full']);
            } elseif (is_string($meta_val) && filter_var($meta_val, FILTER_VALIDATE_URL)) {
                return esc_url($meta_val);
            }
        }
    }

    // 3. Native WordPress get_avatar_url
    $avatar_url = get_avatar_url($author_id, ['size' => 120]);
    if ($avatar_url) {
        return esc_url($avatar_url);
    }

    return '';
}

/**
 * Render Google E-E-A-T Compliant Rich Author Bio Box.
 * Auto-syncs with WordPress User Profile (display_name, description, avatar) and Customizer overrides.
 *
 * @param int $author_id Author User ID.
 */
function ht_author_bio_box($author_id = null) {
    if (!$author_id) {
        $author_id = get_post_field('post_author', get_the_ID());
        if (!$author_id) {
            $author_id = get_the_author_meta('ID');
        }
    }

    // 1. Dynamic Display Name
    $custom_name = get_theme_mod('ht_author_custom_name', '');
    $author_name = !empty($custom_name) ? $custom_name : get_the_author_meta('display_name', $author_id);
    if (empty($author_name)) {
        $author_name = get_the_author();
    }

    // 2. Dynamic Biographical Info from WordPress Profile
    $author_bio = get_the_author_meta('description', $author_id);
    if (empty($author_bio)) {
        $author_bio = get_theme_mod('ht_author_custom_bio', 'শিক্ষা ও প্রযুক্তি বিষয়ক গবেষক, জাতীয় বিশ্ববিদ্যালয় এবং বিসিএস স্টাডি বিশ্লেষক। শিক্ষার্থীদের জন্য নির্ভুল, তথ্যবহুল ও সময়োপযোগী হ্যান্ডনোট প্রস্তুত করাই HelpTrickBD-এর মূল লক্ষ্য।');
    }

    $author_role = get_theme_mod('ht_author_custom_title', esc_html__('লেখক ও গবেষক', 'helptrickbd'));
    $author_posts_url = get_author_posts_url($author_id);
    $total_posts = count_user_posts($author_id, 'post', true);
    $avatar_url = ht_get_author_avatar_url($author_id);
    ?>
    <section class="ht-author-bio-card" aria-label="<?php esc_attr_e('লেখক পরিচিতি', 'helptrickbd'); ?>">
        <div class="ht-author-avatar-col">
            <a href="<?php echo esc_url($author_posts_url); ?>" class="ht-author-avatar-link">
                <?php if (!empty($avatar_url)) : ?>
                    <img src="<?php echo esc_url($avatar_url); ?>" alt="<?php echo esc_attr($author_name); ?>" class="ht-author-bio-avatar" width="86" height="86" loading="lazy">
                <?php else : ?>
                    <?php echo get_avatar($author_id, 86, '', esc_attr($author_name), ['class' => 'ht-author-bio-avatar']); ?>
                <?php endif; ?>
            </a>
        </div>
        <div class="ht-author-details-col">
            <div class="ht-author-header-line">
                <div class="ht-author-title-group">
                    <span class="ht-author-pretitle"><?php echo esc_html($author_role); ?></span>
                    <h3 class="ht-author-name">
                        <a href="<?php echo esc_url($author_posts_url); ?>"><?php echo esc_html($author_name); ?></a>
                    </h3>
                </div>
                <div class="ht-author-eeat-pill" title="<?php esc_attr_e('গুগল E-E-A-T ভেরিফাইড শিক্ষক ও গবেষক', 'helptrickbd'); ?>">
                    <?php ht_m3_icon('verified', 16, 'ht-icon-verified'); ?>
                    <span><?php esc_html_e('ভেরিফাইড লেখক', 'helptrickbd'); ?></span>
                </div>
            </div>
            <p class="ht-author-bio-text">
                <?php echo esc_html($author_bio); ?>
            </p>
            <div class="ht-author-footer-line">
                <div class="ht-author-stats">
                    <?php ht_m3_icon('auto_stories', 15); ?>
                    <span><?php esc_html_e('মোট প্রকাশনা:', 'helptrickbd'); ?> <strong><?php echo esc_html(ht_bn_number($total_posts)); ?></strong> <?php esc_html_e('টি হ্যান্ডনোট', 'helptrickbd'); ?></span>
                </div>
                <a href="<?php echo esc_url($author_posts_url); ?>" class="ht-author-all-posts-link">
                    <span><?php esc_html_e('লেখকের সকল পোস্ট দেখুন', 'helptrickbd'); ?></span>
                    <?php ht_m3_icon('arrow_forward', 15); ?>
                </a>
            </div>
        </div>
    </section>
    <?php
}

/**
 * Render Previous and Next Post Navigation Cards.
 */
function ht_post_navigation_cards() {
    $prev_post = get_previous_post();
    $next_post = get_next_post();

    if (!$prev_post && !$next_post) {
        return;
    }
    ?>
    <nav class="ht-post-nav-cards" aria-label="<?php esc_attr_e('পোস্ট নেভিগেশন', 'helptrickbd'); ?>">
        <?php if ($prev_post) : ?>
            <a href="<?php echo esc_url(get_permalink($prev_post->ID)); ?>" class="ht-nav-card ht-nav-card-prev">
                <div class="ht-nav-card-arrow">
                    <?php ht_m3_icon('arrow_back', 18); ?>
                    <span><?php esc_html_e('পূর্ববর্তী গাইড', 'helptrickbd'); ?></span>
                </div>
                <div class="ht-nav-card-content">
                    <h4 class="ht-nav-card-title"><?php echo esc_html(get_the_title($prev_post->ID)); ?></h4>
                </div>
            </a>
        <?php else : ?>
            <div class="ht-nav-card ht-nav-card-empty"></div>
        <?php endif; ?>

        <?php if ($next_post) : ?>
            <a href="<?php echo esc_url(get_permalink($next_post->ID)); ?>" class="ht-nav-card ht-nav-card-next">
                <div class="ht-nav-card-arrow">
                    <span><?php esc_html_e('পরবর্তী গাইড', 'helptrickbd'); ?></span>
                    <?php ht_m3_icon('arrow_forward', 18); ?>
                </div>
                <div class="ht-nav-card-content">
                    <h4 class="ht-nav-card-title"><?php echo esc_html(get_the_title($next_post->ID)); ?></h4>
                </div>
            </a>
        <?php else : ?>
            <div class="ht-nav-card ht-nav-card-empty"></div>
        <?php endif; ?>
    </nav>
    <?php
}

