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

                    <!-- Student Reading Toolbelt -->
                    <div class="ht-reading-toolbelt">
                        <?php if (get_theme_mod('ht_font_resizer_enable', true)) : ?>
                            <!-- Font Size Resizer -->
                            <div class="ht-toolbelt-group ht-font-resizer" title="ফন্ট সাইজ পরিবর্তন করুন">
                                <span class="ht-tool-label"><?php ht_m3_icon('format_size', 16); ?> সাইজ:</span>
                                <button class="ht-resizer-btn" id="ht-font-dec" aria-label="ফন্ট ছোট করুন">A-</button>
                                <button class="ht-resizer-btn ht-active" id="ht-font-reset" aria-label="স্বাভাবিক ফন্ট">A</button>
                                <button class="ht-resizer-btn" id="ht-font-inc" aria-label="ফন্ট বড় করুন">A+</button>
                            </div>
                        <?php endif; ?>

                        <?php if (get_theme_mod('ht_focus_mode_enable', true)) : ?>
                            <!-- Focus Mode Toggle -->
                            <button class="ht-toolbelt-btn" id="ht-focus-toggle" aria-label="ফোকাস রিডিং মোড">
                                <?php ht_m3_icon('auto_stories', 16); ?>
                                <span>ফোকাস মোড</span>
                            </button>
                        <?php endif; ?>

                        <?php if (get_theme_mod('ht_bookmark_btn_enable', true)) : ?>
                            <!-- Bookmark / Save for Later -->
                            <button class="ht-toolbelt-btn ht-bookmark-toggle" data-id="<?php the_ID(); ?>" data-title="<?php echo esc_attr(get_the_title()); ?>" data-url="<?php the_permalink(); ?>" aria-label="পড়ার তালিকায় রাখুন">
                                <?php ht_m3_icon('bookmark', 16); ?>
                                <span class="ht-bm-text">পড়ার তালিকায় রাখুন</span>
                            </button>
                        <?php endif; ?>

                        <?php if (get_theme_mod('ht_print_btn_enable', true)) : ?>
                            <!-- 1-Click Print & PDF -->
                            <button class="ht-toolbelt-btn" id="ht-print-btn" aria-label="প্রিন্ট বা পিডিএফ সেভ করুন">
                                <?php ht_m3_icon('print', 16); ?>
                                <span>প্রিন্ট / পিডিএফ</span>
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
                                    <span class="ht-toc-title">সূচিপত্র (বিষয়বস্তু রূপরেখা)</span>
                                </div>
                                <button class="ht-toc-toggle" id="ht-toc-toggle-btn" aria-label="টগল করুন">
                                    <?php ht_m3_icon('keyboard_arrow_down', 18); ?>
                                </button>
                            </div>
                            <nav class="ht-toc-nav" id="ht-toc-nav" aria-label="সূচিপত্র"></nav>
                        </div>
                    <?php endif; ?>

                </header>

                <!-- Article Main Content -->
                <div class="ht-article-content ht-entry-content" id="ht-article-body">
                    <?php
                    the_content();

                    wp_link_pages([
                        'before'      => '<div class="ht-page-links"><span class="ht-page-links-title">পৃষ্ঠাসমূহ:</span>',
                        'after'       => '</div>',
                        'link_before' => '<span class="ht-page-number">',
                        'link_after'  => '</span>',
                    ]);
                    ?>
                </div>

                <?php if (get_theme_mod('ht_citation_enable', true)) : ?>
                    <!-- Academic Source & Official Gazette Citation Box -->
                    <div class="ht-citation-card">
                        <div class="ht-citation-header">
                            <?php ht_m3_icon('menu_book', 18); ?>
                            <span class="ht-citation-title">তথ্যসূত্র ও অ্যাকাডেমিক সাইটেশন</span>
                        </div>
                        <div class="ht-citation-body">
                            <p class="ht-citation-text">
                                <strong>প্রামাণ্য উৎস:</strong> জাতীয় শিক্ষাক্রম ও পাঠ্যপুস্তক বোর্ড (NCTB), জাতীয় বিশ্ববিদ্যালয় অফিশিয়াল গেজেট ও অ্যাকাডেমিক রেগুলেশন।
                            </p>
                            <div class="ht-citation-apa-box">
                                <span class="ht-apa-label">APA 7th Edition Citation:</span>
                                <code class="ht-apa-code" id="ht-apa-text">HelpTrickBD. (<?php echo esc_html(date('Y', get_post_time('U'))); ?>). <?php the_title(); ?>. Help Trick BD. Retrieved from <?php the_permalink(); ?></code>
                                <button class="ht-btn-copy-citation" id="ht-copy-apa-btn" aria-label="সাইটেশন কপি করুন">
                                    <?php ht_m3_icon('content_copy', 14); ?>
                                    <span>কপি করুন</span>
                                </button>
                            </div>
                        </div>
                    </div>
                <?php endif; ?>

                <?php if (get_theme_mod('ht_post_community_enable', true)) : ?>
                    <!-- Official Community Study Group Join Card -->
                    <div class="ht-single-community-card">
                        <div class="ht-community-icon-box">
                            <?php ht_m3_icon('campaign', 28); ?>
                        </div>
                        <div class="ht-community-info">
                            <h4 class="ht-community-title">পরীক্ষার জরুরি রুটিন ও স্পেশাল হ্যান্ডনোট মিস করতে না চাইলে!</h4>
                            <p class="ht-community-desc">আমাদের ভেরিফাইড হোয়াটসঅ্যাপ ও টেলিগ্রাম স্টাডি গ্রুপে আজই যুক্ত হোন।</p>
                        </div>
                        <div class="ht-community-links">
                            <a href="<?php echo esc_url(get_theme_mod('ht_whatsapp_url', 'https://chat.whatsapp.com/')); ?>" target="_blank" rel="noopener noreferrer" class="ht-btn ht-btn-whatsapp">
                                <?php ht_m3_icon('whatsapp', 18); ?>
                                <span>WhatsApp গ্রুপ</span>
                            </a>
                            <a href="<?php echo esc_url(get_theme_mod('ht_telegram_url', 'https://t.me/helptrickbd')); ?>" target="_blank" rel="noopener noreferrer" class="ht-btn ht-btn-telegram">
                                <?php ht_m3_icon('telegram', 18); ?>
                                <span>Telegram চ্যানেল</span>
                            </a>
                        </div>
                    </div>
                <?php endif; ?>

                <!-- Tags Cloud -->
                <?php
                $tags = get_the_tags();
                if ($tags) :
                ?>
                    <div class="ht-tags-list" aria-label="ট্যাগসমূহ">
                        <span class="ht-tags-label">ট্যাগসমূহ:</span>
                        <?php foreach ($tags as $tag) : ?>
                            <a href="<?php echo esc_url(get_tag_link($tag->term_id)); ?>" class="ht-tag-chip">
                                #<?php echo esc_html($tag->name); ?>
                            </a>
                        <?php endforeach; ?>
                    </div>
                <?php endif; ?>

                <!-- Ad Slot After Content -->
                <?php ht_render_ad('ht_ad_after_content', 'ht-ad-single-bottom', 250); ?>

                <!-- Related Posts Algorithm -->
                <?php
                if (get_theme_mod('ht_related_posts_enable', true)) :
                    $current_cats = wp_get_post_categories(get_the_ID());
                    if (!empty($current_cats)) :
                        $related_query = new WP_Query([
                            'category__in'        => $current_cats,
                            'post__not_in'        => [get_the_ID()],
                            'posts_per_page'      => 3,
                            'ignore_sticky_posts' => 1,
                        ]);

                        if ($related_query->have_posts()) :
                    ?>
                        <section class="ht-related-section" aria-label="সম্পর্কিত আরও আর্টিকেল">
                            <h3 class="ht-related-heading">
                                <?php ht_m3_icon('menu_book', 20); ?>
                                <span>আরও পড়ুন (সম্পর্কিত নির্দেশিকা)</span>
                            </h3>
                            <div class="ht-related-grid">
                                <?php
                                while ($related_query->have_posts()) :
                                    $related_query->the_post();
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
    <button class="ht-dock-btn" id="ht-dock-copy" aria-label="কপি করুন">
        <?php ht_m3_icon('content_copy', 15); ?>
        <span>কপি</span>
    </button>
    <button class="ht-dock-btn" id="ht-dock-share-wa" aria-label="WhatsApp-এ শেয়ার">
        <?php ht_m3_icon('whatsapp', 15); ?>
        <span>শেয়ার</span>
    </button>
</div>

<!-- Print Watermark Container (Visible Only During Print) -->
<div class="ht-print-watermark" aria-hidden="true">
    <div class="ht-print-logo">HelpTrickBD.com</div>
    <div class="ht-print-subtitle">শিক্ষা ও তথ্যপ্রযুক্তি সহায়ক উন্মুক্ত পোর্টাল | সংগ্রহ: <?php the_permalink(); ?></div>
</div>

<?php
get_footer();
