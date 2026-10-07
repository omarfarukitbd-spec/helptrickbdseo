<?php
/**
 * The Template for displaying Search Results
 * Keyword highlight, result counts, empty state & sidebar.
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

get_header();
?>

<main id="primary" class="ht-main-site ht-search-site">
    <div class="ht-container">

        <!-- Breadcrumbs Navigation -->
        <?php ht_breadcrumbs(); ?>

        <!-- Search Header -->
        <header class="ht-archive-header ht-search-header">
            <div class="ht-archive-header-badge">
                <?php ht_m3_icon('search', 20); ?>
                <span>অনুসন্ধান ফলাফল</span>
            </div>
            <h1 class="ht-archive-title">
                "<?php echo esc_html(get_search_query()); ?>"
            </h1>
            <p class="ht-search-count">
                মোট <?php echo esc_html(ht_bn_number($wp_query->found_posts)); ?> টি ফলাফল পাওয়া গেছে
            </p>
        </header>

        <div class="ht-layout-row">

            <!-- Primary 70% Content Area -->
            <div class="ht-content-area">

                <?php if (have_posts()) : ?>
                    <div class="ht-cards-grid">
                        <?php
                        while (have_posts()) :
                            the_post();
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
                        <?php endwhile; ?>
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
                        <h3>কোনো ফলাফল পাওয়া যায়নি</h3>
                        <p>আপনার অনুসন্ধান করা শব্দের সাথে মিল রেখে কোনো আর্টিকেল পাওয়া যায়নি। বানান সঠিক রয়েছে কিনা পরীক্ষা করুন বা নিচের বক্স থেকে পুনরায় অনুসন্ধান করুন।</p>
                        <div class="ht-empty-search-box">
                            <?php get_search_form(); ?>
                        </div>
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
