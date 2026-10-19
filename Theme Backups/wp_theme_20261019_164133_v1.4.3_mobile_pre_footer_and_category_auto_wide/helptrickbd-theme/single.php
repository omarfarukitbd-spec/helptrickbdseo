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

                <?php if (get_theme_mod('ht_citation_enable', true)) : ?>
                    <!-- Advanced Academic Source & Verified Citation Module -->
                    <?php
                    $post_year = get_the_date('Y');
                    $post_date_formatted = get_the_date('F j, Y');
                    $post_modified_formatted = get_the_modified_date('F j, Y');
                    $cite_author_id = get_post_field('post_author', get_the_ID());
                    $cite_custom_name = get_theme_mod('ht_author_custom_name', '');
                    $cite_author_name = !empty($cite_custom_name) ? $cite_custom_name : get_the_author_meta('display_name', $cite_author_id);
                    if (empty($cite_author_name)) {
                        $cite_author_name = get_the_author();
                    }
                    if (empty($cite_author_name)) {
                        $cite_author_name = 'HelpTrickBD Editorial Panel';
                    }
                    $cite_title = get_the_title();
                    $cite_url = get_permalink();
                    ?>
                    <section class="ht-citation-card" id="ht-citation-module" aria-label="<?php esc_attr_e('একাডেমিক সূত্র ও অফিসিয়াল রেফারেন্স নির্দেশিকা', 'helptrickbd'); ?>">
                        <div class="ht-citation-header">
                            <div class="ht-citation-title-wrap">
                                <span class="ht-citation-icon-badge">
                                    <?php ht_m3_icon('school', 20); ?>
                                </span>
                                <div>
                                    <h3 class="ht-citation-title"><?php esc_html_e('একাডেমিক সূত্র ও উদ্ধৃতি (Citation)', 'helptrickbd'); ?></h3>
                                    <span class="ht-citation-subtitle"><?php esc_html_e('অফিসিয়াল পাঠ্যক্রম ও রেফারেন্স নির্দেশিকা', 'helptrickbd'); ?></span>
                                </div>
                            </div>
                            <div class="ht-citation-verified-badge" title="<?php esc_attr_e('পাঠ্যক্রম ও একাডেমিক মানদণ্ড যাচাইকৃত', 'helptrickbd'); ?>">
                                <?php ht_m3_icon('verified', 15); ?>
                                <span><?php esc_html_e('পাঠ্যক্রম অনুমোদিত', 'helptrickbd'); ?></span>
                            </div>
                        </div>

                        <!-- Source Authority Details -->
                        <div class="ht-citation-meta-grid">
                            <div class="ht-cite-meta-item">
                                <span class="ht-cite-meta-label"><?php esc_html_e('মানদণ্ড ও কর্তৃপক্ষ:', 'helptrickbd'); ?></span>
                                <span class="ht-cite-meta-val"><?php esc_html_e('জাতীয় শিক্ষাক্রম (NCTB) ও জাতীয় বিশ্ববিদ্যালয় (NU) সিলেবাস কাঠামো', 'helptrickbd'); ?></span>
                            </div>
                            <div class="ht-cite-meta-item">
                                <span class="ht-cite-meta-label"><?php esc_html_e('প্রকাশের তারিখ:', 'helptrickbd'); ?></span>
                                <span class="ht-cite-meta-val"><?php echo esc_html($post_date_formatted); ?></span>
                            </div>
                            <div class="ht-cite-meta-item">
                                <span class="ht-cite-meta-label"><?php esc_html_e('সর্বশেষ হালনাগাদ:', 'helptrickbd'); ?></span>
                                <span class="ht-cite-meta-val"><?php echo esc_html($post_modified_formatted); ?></span>
                            </div>
                            <div class="ht-cite-meta-item">
                                <span class="ht-cite-meta-label"><?php esc_html_e('রিসোর্স আইডি:', 'helptrickbd'); ?></span>
                                <span class="ht-cite-meta-val"><code>HTBD-<?php the_ID(); ?></code></span>
                            </div>
                        </div>

                        <!-- Citation Format Selection Tabs -->
                        <div class="ht-citation-tabs-nav" role="tablist" aria-label="<?php esc_attr_e('সাইটেশন ফরম্যাট মানদণ্ড', 'helptrickbd'); ?>">
                            <button type="button" class="ht-cite-tab-btn ht-cite-tab-active" data-cite-format="apa" role="tab" aria-selected="true">APA (7th Ed.)</button>
                            <button type="button" class="ht-cite-tab-btn" data-cite-format="mla" role="tab" aria-selected="false">MLA (9th Ed.)</button>
                            <button type="button" class="ht-cite-tab-btn" data-cite-format="harvard" role="tab" aria-selected="false">Harvard</button>
                            <button type="button" class="ht-cite-tab-btn" data-cite-format="bibtex" role="tab" aria-selected="false">BibTeX</button>
                        </div>

                        <!-- Citation Code Content Box -->
                        <div class="ht-citation-code-wrap">
                            <div class="ht-citation-code-content" id="ht-active-citation-text" tabindex="0">
                                <?php echo esc_html($cite_author_name . '. (' . $post_year . '). ' . $cite_title . '. HelpTrickBD Academic Portal. Retrieved from ' . $cite_url); ?>
                            </div>
                            <div class="ht-citation-actions">
                                <button type="button" class="ht-btn-copy-citation" id="ht-copy-citation-btn" aria-label="<?php esc_attr_e('উদ্ধৃতি কপি করুন', 'helptrickbd'); ?>">
                                    <span class="ht-copy-icon-ready"><?php ht_m3_icon('content_copy', 15); ?></span>
                                    <span class="ht-copy-icon-done" style="display:none;"><?php ht_m3_icon('check', 15); ?></span>
                                    <span id="ht-copy-citation-label"><?php esc_html_e('উদ্ধৃতি কপি করুন', 'helptrickbd'); ?></span>
                                </button>
                            </div>
                        </div>

                        <!-- Embedded Citation Data for Instant Tab Switching -->
                        <script type="application/json" id="ht-citation-data">
                        {
                            "apa": <?php echo json_encode($cite_author_name . '. (' . $post_year . '). ' . $cite_title . '. HelpTrickBD Academic Portal. Retrieved from ' . $cite_url); ?>,
                            "mla": <?php echo json_encode('"' . $cite_title . '." HelpTrickBD, ' . $post_date_formatted . ', ' . $cite_url . '.'); ?>,
                            "harvard": <?php echo json_encode($cite_author_name . ', ' . $post_year . '. \'' . $cite_title . '\', HelpTrickBD Academic Portal. Available at: <' . $cite_url . '> [Accessed ' . date('j F Y') . '].'); ?>,
                            "bibtex": <?php echo json_encode("@article{helptrickbd_" . get_the_ID() . ",\n  author    = {" . $cite_author_name . "},\n  title     = {" . $cite_title . "},\n  journal   = {HelpTrickBD Academic Portal},\n  year      = {" . $post_year . "},\n  url       = {" . $cite_url . "}\n}"); ?>
                        }
                        </script>
                    </section>
                <?php endif; ?>

                <!-- Multi-Platform Social Share Bar (Bottom) -->
                <?php ht_social_share_bar('bottom'); ?>

                <!-- Interactive Post Helpful / Like Reaction Box -->
                <?php ht_post_reaction_box(); ?>

                <?php if (get_theme_mod('ht_post_community_enable', true)) : ?>
                    <!-- Official Community Study Group Join Card -->
                    <div class="ht-single-community-card">
                        <div class="ht-community-icon-box">
                            <?php ht_m3_icon('campaign', 28); ?>
                        </div>
                        <div class="ht-community-info">
                            <h4 class="ht-community-title"><?php esc_html_e('সবার আগে পরীক্ষার রুটিন ও স্পেশাল সাজেশন পেতে চান?', 'helptrickbd'); ?></h4>
                            <p class="ht-community-desc"><?php esc_html_e('যুক্ত হোন আমাদের অফিসিয়াল হোয়াটসঅ্যাপ ও টেলিগ্রাম স্টাডি চ্যানেলে।', 'helptrickbd'); ?></p>
                        </div>
                        <div class="ht-community-links">
                            <a href="<?php echo esc_url(get_theme_mod('ht_whatsapp_url', 'https://whatsapp.com/channel/0029Vb956jgCHDyrx1wkUh2a')); ?>" target="_blank" rel="noopener noreferrer" class="ht-btn ht-btn-whatsapp">
                                <?php ht_m3_icon('whatsapp', 18); ?>
                                <span>WhatsApp Channel</span>
                            </a>
                            <a href="<?php echo esc_url(get_theme_mod('ht_telegram_url', 'https://t.me/helptrickbd_official')); ?>" target="_blank" rel="noopener noreferrer" class="ht-btn ht-btn-telegram">
                                <?php ht_m3_icon('telegram', 18); ?>
                                <span>Telegram Channel</span>
                            </a>
                        </div>
                    </div>
                <?php endif; ?>

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
                                                <a href="<?php the_permalink(); ?>"><?php the_title(); ?></a>
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
