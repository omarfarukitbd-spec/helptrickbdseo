<?php
/**
 * The Sidebar containing the primary widget area
 * Sidebar Top AJAX Live Search, Exam Countdown, Ranked Popular Posts with Circular Thumbs,
 * Sticky Ad Slot, Contextual Category Cards with Far-Right Stats.
 * Completely purged of legacy core widgets (Recent Posts, Archives, Comments, raw bullet Categories).
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}
?>

<div class="ht-sidebar-wrapper">

    <!-- Widget 1: Sidebar Top Instant AJAX Live Search (Position #1) -->
    <?php if (get_theme_mod('ht_sidebar_search_enable', true)) : ?>
        <div class="ht-widget ht-widget-side-search">
            <div class="ht-widget-header">
                <?php ht_m3_icon('search', 20, 'ht-widget-icon'); ?>
                <h3 class="ht-widget-title"><?php echo esc_html(get_theme_mod('ht_sidebar_search_title', 'অনুসন্ধান করুন')); ?></h3>
            </div>
            <div class="ht-widget-body">
                <div class="ht-side-search-box">
                    <form role="search" method="get" class="ht-side-search-form" action="<?php echo esc_url(home_url('/')); ?>">
                        <div class="ht-side-search-input-wrap">
                            <span class="ht-side-search-icon" aria-hidden="true">
                                <?php ht_m3_icon('search', 18); ?>
                            </span>
                            <input 
                                type="search" 
                                id="ht-side-search-input" 
                                class="ht-side-search-field" 
                                placeholder="<?php echo esc_attr(get_theme_mod('ht_sidebar_search_placeholder', 'হ্যান্ডনোট, সাজেশন বা বিষয় খুঁজুন...')); ?>" 
                                value="<?php echo get_search_query(); ?>" 
                                name="s" 
                                autocomplete="off"
                                spellcheck="false"
                                aria-label="সাইডবার অনুসন্ধান"
                            >
                            <button type="button" class="ht-side-search-clear" id="ht-side-search-clear" aria-label="মুছে ফেলুন" style="display:none;">
                                <?php ht_m3_icon('clear', 16); ?>
                            </button>
                            <span class="ht-side-search-spinner" id="ht-side-search-spinner" aria-hidden="true" style="display:none;"></span>
                        </div>
                    </form>
                    <!-- Instant Live AJAX Search Dropdown Results -->
                    <div class="ht-side-search-results" id="ht-side-search-results" aria-live="polite" style="display:none;"></div>
                </div>
            </div>
        </div>
    <?php endif; ?>

    <!-- Widget 2: Exam Countdown Card (If Enabled) -->
    <?php if (get_theme_mod('ht_sidebar_countdown_enable', true) && get_theme_mod('ht_countdown_enable', true)) : ?>
        <div class="ht-widget ht-widget-countdown">
            <div class="ht-widget-header">
                <?php ht_m3_icon('timer', 20, 'ht-widget-icon'); ?>
                <h3 class="ht-widget-title">পরীক্ষার দিন গণনা</h3>
            </div>
            <div class="ht-widget-body">
                <span class="ht-side-countdown-label"><?php echo esc_html(get_theme_mod('ht_countdown_title', 'অনার্স ২য় বর্ষ পরীক্ষা')); ?></span>
                <div class="ht-side-countdown-display" id="ht-sidebar-countdown-box">
                    <span class="ht-side-days" id="ht-sidebar-days-val">--</span>
                    <span class="ht-side-unit">দিন বাকি</span>
                </div>
            </div>
        </div>
    <?php endif; ?>

    <!-- Widget 3: Ranked Compact Popular Posts with Circular Round Thumbs (Position #3) -->
    <?php if (get_theme_mod('ht_sidebar_popular_enable', true)) : ?>
        <div class="ht-widget ht-widget-popular">
            <div class="ht-widget-header">
                <?php ht_m3_icon('trending_up', 20, 'ht-widget-icon'); ?>
                <h3 class="ht-widget-title"><?php echo esc_html(get_theme_mod('ht_sidebar_popular_title', 'জনপ্রিয় পোস্ট ও হ্যান্ডনোট')); ?></h3>
            </div>
            <div class="ht-widget-body">
                <?php
                $pop_count = absint(get_theme_mod('ht_sidebar_popular_count', 5));
                if ($pop_count < 3 || $pop_count > 10) {
                    $pop_count = 5;
                }

                // Query top popular posts by views
                $popular_query = new WP_Query([
                    'posts_per_page'      => $pop_count,
                    'post_status'         => 'publish',
                    'ignore_sticky_posts' => 1,
                    'meta_key'            => 'ht_post_views_count',
                    'orderby'             => 'meta_value_num date',
                    'order'               => 'DESC',
                ]);

                // Fallback to recent posts if views are not yet accumulated
                if (!$popular_query->have_posts()) {
                    $popular_query = new WP_Query([
                        'posts_per_page'      => $pop_count,
                        'post_status'         => 'publish',
                        'ignore_sticky_posts' => 1,
                        'orderby'             => 'date',
                        'order'               => 'DESC',
                    ]);
                }

                if ($popular_query->have_posts()) :
                ?>
                    <div class="ht-popular-list">
                        <?php
                        $rank = 0;
                        while ($popular_query->have_posts()) :
                            $popular_query->the_post();
                            $rank++;
                        ?>
                            <article class="ht-popular-item">
                                <!-- Compact Round Circular Post Thumbnail with Floating Rank Badge -->
                                <a href="<?php the_permalink(); ?>" class="ht-popular-thumb-wrap" aria-label="<?php the_title_attribute(); ?>">
                                    <div class="ht-popular-thumb-circle">
                                        <?php ht_the_thumbnail(get_the_ID(), 'thumbnail', 'ht-popular-thumb-round'); ?>
                                    </div>
                                    <span class="ht-popular-badge ht-rank-<?php echo esc_attr($rank); ?>" title="র‍্যাঙ্ক #<?php echo esc_attr($rank); ?>"><?php echo esc_html(ht_bn_number($rank)); ?></span>
                                </a>

                                <!-- Post Details -->
                                <div class="ht-popular-details">
                                    <?php
                                    $cats = get_the_category();
                                    if (!empty($cats)) : ?>
                                        <div class="ht-popular-cat-wrap">
                                            <span class="ht-popular-cat-chip"><?php echo esc_html($cats[0]->name); ?></span>
                                        </div>
                                    <?php endif; ?>
                                    <h4 class="ht-popular-title">
                                        <a href="<?php the_permalink(); ?>"><?php the_title(); ?></a>
                                    </h4>
                                    <div class="ht-popular-meta">
                                        <span class="ht-popular-date">
                                            <?php ht_m3_icon('event', 13, 'ht-meta-icon'); ?>
                                            <?php ht_post_date(); ?>
                                        </span>
                                    </div>
                                </div>
                            </article>
                        <?php
                        endwhile;
                        wp_reset_postdata();
                        ?>
                    </div>
                <?php endif; ?>
            </div>
        </div>
    <?php endif; ?>

    <!-- Widget 4: Sticky Sidebar Google AdSlot (Position #4) -->
    <?php if (get_theme_mod('ht_sidebar_ad_enable', true)) : ?>
        <?php ht_render_ad('ht_ad_sticky_sidebar', 'ht-widget ht-sidebar-ad-slot', 280); ?>
    <?php endif; ?>

    <!-- Widget 5: Contextual Categories with Web Icons & Far-Right Stats Badges (Position #5) -->
    <?php if (get_theme_mod('ht_sidebar_categories_enable', true)) : ?>
        <div class="ht-widget ht-widget-categories">
            <div class="ht-widget-header">
                <?php ht_m3_icon('folder_open', 20, 'ht-widget-icon'); ?>
                <h3 class="ht-widget-title"><?php echo esc_html(get_theme_mod('ht_sidebar_categories_title', 'সকল বিষয়শ্রেণী (ক্যাটাগরি)')); ?></h3>
            </div>
            <div class="ht-widget-body">
                <div class="ht-cat-cards-grid">
                    <?php
                    $cat_limit = absint(get_theme_mod('ht_sidebar_categories_count', 10));
                    if ($cat_limit < 4 || $cat_limit > 20) {
                        $cat_limit = 10;
                    }

                    $categories = get_categories([
                        'orderby'    => 'count',
                        'order'      => 'DESC',
                        'number'     => $cat_limit,
                        'hide_empty' => true,
                    ]);

                    foreach ($categories as $category) :
                        $cat_icon = ht_get_category_icon($category->slug, $category->name);
                    ?>
                        <a href="<?php echo esc_url(get_category_link($category->term_id)); ?>" class="ht-cat-card-box" title="<?php echo esc_attr($category->name); ?>">
                            <div class="ht-cat-card-left">
                                <span class="ht-cat-card-icon">
                                    <?php ht_m3_icon($cat_icon, 18); ?>
                                </span>
                                <span class="ht-cat-card-name"><?php echo esc_html($category->name); ?></span>
                            </div>
                            <!-- Statistics Badge Pinned Far Right -->
                            <span class="ht-cat-stat-badge">
                                <?php echo esc_html(ht_bn_number($category->count)); ?>টি
                            </span>
                        </a>
                    <?php endforeach; ?>
                </div>
            </div>
        </div>
    <?php endif; ?>

</div><!-- .ht-sidebar-wrapper -->
