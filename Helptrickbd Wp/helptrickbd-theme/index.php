<?php
/**
 * The main template file (Fallback Blog & Archive)
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

get_header();
?>

<main id="primary" class="ht-main-site ht-index-site">
    <div class="ht-container">

        <?php ht_breadcrumbs(); ?>

        <div class="ht-layout-row">

            <div class="ht-content-area">

                <div class="ht-section-header">
                    <h1 class="ht-section-title">
                        <?php ht_m3_icon('auto_stories', 22, 'ht-icon-primary'); ?>
                        <span>সর্বশেষ প্রকাশনাসমূহ</span>
                    </h1>
                </div>

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
                            if ($card_counter === 4) {
                                ht_render_in_feed_ad();
                            }
                        endwhile;
                        ?>
                    </div><!-- .ht-cards-grid -->

                    <div class="ht-pagination-wrap">
                        <?php
                        the_posts_pagination([
                            'prev_text' => ht_m3_icon('arrow_back', 16, '', false) . ' পূর্ববর্তী',
                            'next_text' => 'পরবর্তী ' . ht_m3_icon('arrow_forward', 16, '', false),
                        ]);
                        ?>
                    </div>

                <?php else : ?>
                    <p class="ht-no-posts">কোনো প্রকাশনা পাওয়া যায়নি।</p>
                <?php endif; ?>

            </div><!-- .ht-content-area -->

            <aside class="ht-sidebar-area">
                <?php get_sidebar(); ?>
            </aside>

        </div><!-- .ht-layout-row -->

    </div><!-- .ht-container -->
</main><!-- #primary -->

<?php
get_footer();
