<?php
/**
 * The Template for displaying all single posts
 * TOC, Reading Bar, Font Resizer, Focus Mode, APA Citation, Quiz & Code Runner.
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

get_header();
?>

<?php if (get_theme_mod('ht_reading_progress_enable', true)) : ?>
<!-- Live Reading Progress Bar -->
<div class="ht-reading-progress" id="ht-reading-progress" aria-hidden="true">
    <div class="ht-progress-fill" id="ht-progress-fill"></div>
</div>
<?php endif; ?>

<main id="primary" class="ht-main-site ht-single-site">
    <div class="ht-container">

        <!-- Breadcrumbs Navigation -->
        <?php ht_breadcrumbs(); ?>

        <div class="ht-layout-row">

            <!-- Primary 70% Article Column -->
            <article id="post-<?php the_ID(); ?>" <?php post_class('ht-article-col'); ?>>
                
                <?php
                while (have_posts()) :
                    the_post();
                ?>

                <!-- Article Header -->
                <header class="ht-article-header">
                    <div class="ht-header-top-badges">
                        <?php ht_category_badge(); ?>
                        <?php ht_eeat_badge(); ?>
                    </div>

                    <h1 class="ht-article-title"><?php the_title(); ?></h1>

                    <div class="ht-article-meta-row">
                        <!-- Date, Reading Time, Views -->
                        <div class="ht-meta-stats">
                            <?php ht_post_date(); ?>
                            <?php ht_reading_time(); ?>
                            <?php ht_post_views(); ?>
                        </div>
                    </div>

                    <!-- Dynamic Last Updated Freshness Signal -->
                    <?php ht_last_updated(); ?>

                    <!-- Social Share Pills (Top) -->
                    <?php ht_social_share_bar('top'); ?>

                    <!-- Student Reading Toolbelt -->
                    <div class="ht-reading-toolbelt">
                        <?php if (get_theme_mod('ht_font_resizer_enable', true)) : ?>
                            <!-- Font Size Resizer -->
                            <div class="ht-toolbelt-group ht-font-resizer" title="<?php esc_attr_e('ফন্টের আকার পরিবর্তন করুন', 'helptrickbd'); ?>">
                                <span class="ht-tool-label"><?php ht_m3_icon('format_size', 16); ?> <?php esc_html_e('ফন্ট:', 'helptrickbd'); ?></span>
                                <button class="ht-resizer-btn" id="ht-font-dec" aria-label="<?php esc_attr_e('ফন্ট ছোট করুন', 'helptrickbd'); ?>">A-</button>
                                <button class="ht-resizer-btn ht-active" id="ht-font-reset" aria-label="<?php esc_attr_e('স্বাভাবিক আকার', 'helptrickbd'); ?>">A</button>
                                <button class="ht-resizer-btn" id="ht-font-inc" aria-label="<?php esc_attr_e('ফন্ট বড় করুন', 'helptrickbd'); ?>">A+</button>
                            </div>
                        <?php endif; ?>

                        <?php if (get_theme_mod('ht_focus_mode_enable', true)) : ?>
                            <!-- Focus Mode Toggle -->
                            <button class="ht-toolbelt-btn" id="ht-focus-toggle" aria-label="<?php esc_attr_e('ফোকাস রিডিং মোড', 'helptrickbd'); ?>">
                                <?php ht_m3_icon('auto_stories', 16); ?>
                                <span><?php esc_html_e('ফোকাস মোড', 'helptrickbd'); ?></span>
                            </button>
                        <?php endif; ?>

                        <?php if (get_theme_mod('ht_bookmark_btn_enable', true)) : ?>
                            <!-- Bookmark / Save for Later -->
                            <button class="ht-toolbelt-btn ht-bookmark-toggle" data-id="<?php the_ID(); ?>" data-title="<?php echo esc_attr(get_the_title()); ?>" data-url="<?php the_permalink(); ?>" aria-label="<?php esc_attr_e('পড়ার তালিকায় সেভ করুন', 'helptrickbd'); ?>">
                                <?php ht_m3_icon('bookmark', 16); ?>
                                <span class="ht-bm-text"><?php esc_html_e('পোস্ট সেভ করুন', 'helptrickbd'); ?></span>
                            </button>
                        <?php endif; ?>

                        <?php if (get_theme_mod('ht_print_btn_enable', true)) : ?>
                            <!-- 1-Click Print & PDF -->
                            <button class="ht-toolbelt-btn" id="ht-print-btn" aria-label="<?php esc_attr_e('প্রিন্ট বা পিডিএফ সেভ করুন', 'helptrickbd'); ?>">
                                <?php ht_m3_icon('print', 16); ?>
                                <span><?php esc_html_e('প্রিন্ট বা পিডিএফ', 'helptrickbd'); ?></span>
                            </button>
                        <?php endif; ?>
                    </div>

                    <!-- Ad Slot Below Title -->
                    <?php ht_render_ad('ht_ad_below_title', 'ht-ad-single-top', 250); ?>

                    <?php if (get_theme_mod('ht_toc_enable', true)) : ?>
                        <!-- Auto Table of Contents (সূচিপত্র) Container -->
                        <div class="ht-toc-container" id="ht-toc-container">
                            <div class="ht-toc-header" id="ht-toc-header">
                                <div class="ht-toc-title-wrap">
                                    <?php ht_m3_icon('format_list_bulleted', 18); ?>
                                    <span class="ht-toc-title"><?php esc_html_e('সূচিপত্র', 'helptrickbd'); ?></span>
                                </div>
                                <button class="ht-toc-toggle" id="ht-toc-toggle-btn" aria-label="<?php esc_attr_e('সূচিপত্র খুলুন বা বন্ধ করুন', 'helptrickbd'); ?>">
                                    <?php ht_m3_icon('keyboard_arrow_down', 18); ?>
                                </button>
                            </div>
                            <nav class="ht-toc-nav" id="ht-toc-nav" aria-label="<?php esc_attr_e('সূচিপত্র', 'helptrickbd'); ?>"></nav>
                        </div>
                    <?php endif; ?>

                </header>

                <!-- Article Main Content -->
                <div class="ht-article-content ht-entry-content" id="ht-article-body">
                    <?php
                    the_content();

                    wp_link_pages([
                        'before'      => '<div class="ht-page-links"><span class="ht-page-links-title">' . esc_html__('পৃষ্ঠাসমূহ:', 'helptrickbd') . '</span>',
                        'after'       => '</div>',
                        'link_before' => '<span class="ht-page-number">',
                        'link_after'  => '</span>',
                    ]);
                    ?>
                </div>

                <!-- Multi-Platform Social Share Bar (Bottom) -->
                <?php ht_social_share_bar('bottom'); ?>

                <!-- Interactive Post Helpful / Like Reaction Box -->
                <?php ht_post_reaction_box(); ?>

                <!-- Tags Cloud -->
                <?php
                $tags = get_the_tags();
                if ($tags) :
                ?>
                    <div class="ht-tags-list" aria-label="<?php esc_attr_e('বিষয়ভিত্তিক ট্যাগসমূহ', 'helptrickbd'); ?>">
                        <span class="ht-tags-label"><?php esc_html_e('ট্যাগ:', 'helptrickbd'); ?></span>
                        <?php foreach ($tags as $tag) : ?>
                            <a href="<?php echo esc_url(get_tag_link($tag->term_id)); ?>" class="ht-tag-chip">
                                #<?php echo esc_html($tag->name); ?>
                            </a>
                        <?php endforeach; ?>
                    </div>
                <?php endif; ?>

                <!-- Google E-E-A-T Compliant Author Bio Box -->
                <?php ht_author_bio_box(); ?>

                <!-- Previous / Next Article Navigation Cards -->
                <?php ht_post_navigation_cards(); ?>

                <!-- Ad Slot After Content -->
                <?php ht_render_ad('ht_ad_after_content', 'ht-ad-single-bottom', 250); ?>

                <!-- Related Posts Algorithm with 12-Hour Transient Caching -->
                <?php
                if (get_theme_mod('ht_related_posts_enable', true)) :
                    $current_post_id = get_the_ID();
                    $transient_key   = 'ht_related_' . $current_post_id;
                    $related_ids     = get_transient($transient_key);

                    if (false === $related_ids) {
                        $current_cats = wp_get_post_categories($current_post_id);
                        if (!empty($current_cats)) {
                            $rel_q = new WP_Query([
                                'category__in'        => $current_cats,
                                'post__not_in'        => [$current_post_id],
                                'posts_per_page'      => 3,
                                'ignore_sticky_posts' => 1,
                                'fields'              => 'ids',
                                'no_found_rows'       => true,
                            ]);
                            $related_ids = $rel_q->posts;
                            set_transient($transient_key, $related_ids, 12 * HOUR_IN_SECONDS);
                        } else {
                            $related_ids = [];
                        }
                    }

                    if (!empty($related_ids)) :
                        $cached_query = new WP_Query([
                            'post__in'            => $related_ids,
                            'orderby'             => 'post__in',
                            'posts_per_page'      => count($related_ids),
                            'ignore_sticky_posts' => 1,
                            'no_found_rows'       => true,
                        ]);
                        if ($cached_query->have_posts()) :
                    ?>
                        <section class="ht-related-section" aria-label="<?php esc_attr_e('সম্পর্কিত হ্যান্ডনোট ও গাইড', 'helptrickbd'); ?>">
                            <h3 class="ht-related-heading">
                                <?php ht_m3_icon('menu_book', 20); ?>
                                <span><?php esc_html_e('সম্পর্কিত হ্যান্ডনোট ও গাইড', 'helptrickbd'); ?></span>
                            </h3>
                            <div class="ht-related-grid">
                                <?php
                                while ($cached_query->have_posts()) :
                                    $cached_query->the_post();
                                ?>
                                    <article class="ht-related-card">
                                        <a href="<?php the_permalink(); ?>" class="ht-related-thumb-wrap">
                                            <?php ht_the_thumbnail(get_the_ID(), 'ht-card-thumb'); ?>
                                        </a>
                                        <div class="ht-related-body">
                                            <h4 class="ht-related-title">
                                                <a href="<?php the_permalink(); ?>" title="<?php the_title_attribute(); ?>"><?php the_title(); ?></a>
                                            </h4>
                                            <span class="ht-related-date"><?php ht_post_date(); ?></span>
                                        </div>
                                    </article>
                                <?php
                                endwhile;
                                wp_reset_postdata();
                                ?>
                            </div>
                        </section>
                    <?php
                        endif;
                    endif;
                endif;
                ?>

                <?php
                // If comments are open or there is at least one comment, load up the comment template.
                if (comments_open() || get_comments_number()) :
                    comments_template();
                endif;
                ?>

                <?php endwhile; ?>

            </article><!-- .ht-article-col -->

            <!-- Sidebar (30%) -->
            <aside class="ht-sidebar-area">
                <?php get_sidebar(); ?>
            </aside>

        </div><!-- .ht-layout-row -->

    </div><!-- .ht-container -->
</main><!-- #primary -->

<!-- Medium-style Text Highlight Floating Dock -->
<div class="ht-highlight-dock" id="ht-highlight-dock" aria-hidden="true">
    <button class="ht-dock-btn" id="ht-dock-copy" aria-label="<?php esc_attr_e('নির্বাচিত অংশ কপি করুন', 'helptrickbd'); ?>">
        <?php ht_m3_icon('content_copy', 15); ?>
        <span><?php esc_html_e('কপি', 'helptrickbd'); ?></span>
    </button>
    <button class="ht-dock-btn" id="ht-dock-share-wa" aria-label="<?php esc_attr_e('হোয়াটসঅ্যাপে শেয়ার করুন', 'helptrickbd'); ?>">
        <?php ht_m3_icon('whatsapp', 15); ?>
        <span><?php esc_html_e('শেয়ার', 'helptrickbd'); ?></span>
    </button>
</div>

<!-- Print Watermark Container (Visible Only During Print) -->
<div class="ht-print-watermark" aria-hidden="true">
    <div class="ht-print-logo">HelpTrickBD.com</div>
    <div class="ht-print-subtitle">শিক্ষা ও তথ্যপ্রযুক্তি রিসোর্স পোর্টাল | <?php the_permalink(); ?></div>
</div>

<?php
get_footer();
