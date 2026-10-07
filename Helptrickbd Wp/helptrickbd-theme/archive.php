<?php
/**
 * The Template for displaying archive pages (Category, Tag, Date)
 * Native in-feed ads, numbered pagination & sidebar.
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

get_header();
?>

<main id="primary" class="ht-main-site ht-archive-site">
    <div class="ht-container">

        <!-- Breadcrumbs Navigation -->
        <?php ht_breadcrumbs(); ?>

        <!-- Archive Header Banner -->
        <header class="ht-archive-header">
            <div class="ht-archive-header-badge">
                <?php ht_m3_icon('category', 20); ?>
                <span>বিষয়শ্রেণী আর্কাইভ</span>
            </div>
            <h1 class="ht-archive-title"><?php the_archive_title(); ?></h1>
            <?php
            $archive_desc = get_the_archive_description();
            if ($archive_desc) :
            ?>
                <div class="ht-archive-desc"><?php echo wp_kses_post($archive_desc); ?></div>
            <?php endif; ?>
        </header>

        <div class="ht-layout-row">

            <!-- Primary 70% Content Area -->
            <div class="ht-content-area">

                <?php if (have_posts()) : ?>
                    <div class="ht-cards-grid">
                        <?php
                        $card_counter = 0;
                        while (have_posts()) :
                            the_post();
                            $card_counter++;
                        ?>
                            <article id="post-<?php the_ID(); ?>" <?php post_class('ht-card'); ?>>
                                <div class="ht-card-thumb-wrap">
                                    <a href="<?php the_permalink(); ?>">
                                        <?php ht_the_thumbnail(get_the_ID(), 'ht-card-thumb'); ?>
                                    </a>
                                    <button class="ht-card-bm-btn ht-bookmark-toggle" data-id="<?php the_ID(); ?>" data-title="<?php echo esc_attr(get_the_title()); ?>" data-url="<?php the_permalink(); ?>" aria-label="পড়ার তালিকায় সংরক্ষণ করুন">
                                        <?php ht_m3_icon('bookmark', 18); ?>
                                    </button>
                                    <div class="ht-card-cat-float">
                                        <?php ht_category_badge(); ?>
                                    </div>
                                </div>

                                <div class="ht-card-body">
                                    <h2 class="ht-card-title">
                                        <a href="<?php the_permalink(); ?>"><?php the_title(); ?></a>
                                    </h2>
                                    <p class="ht-card-excerpt">
                                        <?php echo esc_html(wp_trim_words(get_the_excerpt(), 18)); ?>
                                    </p>
                                    <div class="ht-card-footer">
                                        <?php ht_post_date(); ?>
                                        <?php ht_reading_time(); ?>
                                    </div>
                                </div>
                            </article>
                        <?php
                            // Insert Native In-Feed Ad every 4 cards
                            if ($card_counter === 4) {
                                ht_render_in_feed_ad();
                            }
                        endwhile;
                        ?>
                    </div><!-- .ht-cards-grid -->

                    <!-- Numbered Pagination -->
                    <div class="ht-pagination-wrap">
                        <?php
                        the_posts_pagination([
                            'prev_text' => ht_m3_icon('arrow_back', 16, '', false) . ' পূর্ববর্তী',
                            'next_text' => 'পরবর্তী ' . ht_m3_icon('arrow_forward', 16, '', false),
                        ]);
                        ?>
                    </div>

                <?php else : ?>
                    <div class="ht-empty-state">
                        <?php ht_m3_icon('search', 48, 'ht-empty-icon'); ?>
                        <h3>এই বিভাগে কোনো পোস্ট পাওয়া যায়নি</h3>
                        <p>অনুগ্রহ করে অন্য কোনো বিষয় দেখুন বা সার্চ বারে অনুসন্ধান করুন।</p>
                    </div>
                <?php endif; ?>

            </div><!-- .ht-content-area -->

            <!-- Sidebar (30%) -->
            <aside class="ht-sidebar-area">
                <?php get_sidebar(); ?>
            </aside>

        </div><!-- .ht-layout-row -->

    </div><!-- .ht-container -->
</main><!-- #primary -->

<?php
get_footer();
