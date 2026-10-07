<?php
/**
 * The Front Page Magazine Layout for HelpTrickBD Pro
 * Hero Grid (1+3), Category Filter Tabs, Native In-Feed Ads & Sidebar.
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

get_header();
?>

<main id="primary" class="ht-main-site">
    <div class="ht-container">

        <!-- ========================================================= -->
        <!-- 1. FEATURED HERO MAGAZINE GRID (1 LARGE + 3 SUB)          -->
        <!-- ========================================================= -->
        <?php
        $hero_query = new WP_Query([
            'posts_per_page'      => 4,
            'post_status'         => 'publish',
            'ignore_sticky_posts' => 1,
        ]);

        if ($hero_query->have_posts()) :
            $post_count = 0;
        ?>
        <section class="ht-hero-section" aria-label="প্রধান আকর্ষণ ও সর্বশেষ নির্দেশিকা">
            <div class="ht-hero-grid">
                <?php
                while ($hero_query->have_posts()) :
                    $hero_query->the_post();
                    $post_count++;

                    if ($post_count === 1) :
                        // Lead Hero Article Card
                    ?>
                        <article class="ht-hero-lead-card">
                            <a href="<?php the_permalink(); ?>" class="ht-hero-lead-thumb-wrap">
                                <?php ht_the_thumbnail(get_the_ID(), 'ht-hero-large', 'ht-hero-lead-img'); ?>
                                <span class="ht-hero-gradient"></span>
                            </a>
                            <div class="ht-hero-lead-overlay">
                                <div class="ht-hero-badge-wrap">
                                    <?php ht_category_badge(); ?>
                                    <?php ht_eeat_badge(); ?>
                                </div>
                                <h2 class="ht-hero-lead-title">
                                    <a href="<?php the_permalink(); ?>"><?php the_title(); ?></a>
                                </h2>
                                <p class="ht-hero-lead-excerpt">
                                    <?php echo esc_html(wp_trim_words(get_the_excerpt(), 22)); ?>
                                </p>
                                <div class="ht-card-meta">
                                    <?php ht_post_date(); ?>
                                    <?php ht_reading_time(); ?>
                                </div>
                            </div>
                        </article>
                        
                        <div class="ht-hero-sub-grid">
                    <?php
                    else :
                        // 3 Secondary Cards
                    ?>
                        <article class="ht-hero-sub-card">
                            <a href="<?php the_permalink(); ?>" class="ht-hero-sub-thumb-wrap">
                                <?php ht_the_thumbnail(get_the_ID(), 'ht-card-thumb', 'ht-hero-sub-img'); ?>
                            </a>
                            <div class="ht-hero-sub-info">
                                <div class="ht-sub-badge"><?php ht_category_badge(); ?></div>
                                <h3 class="ht-hero-sub-title">
                                    <a href="<?php the_permalink(); ?>"><?php the_title(); ?></a>
                                </h3>
                                <div class="ht-card-meta">
                                    <?php ht_post_date(); ?>
                                </div>
                            </div>
                        </article>
                    <?php
                    endif;
                endwhile;
                ?>
                </div><!-- .ht-hero-sub-grid -->
            </div><!-- .ht-hero-grid -->
        </section>
        <?php
            wp_reset_postdata();
        endif;
        ?>

        <!-- ========================================================= -->
        <!-- 2. MAIN FEED & SIDEBAR SECTION                           -->
        <!-- ========================================================= -->
        <div class="ht-layout-row">

            <!-- Primary 70% Content Area -->
            <div class="ht-content-area">

                <!-- Category Filter Tabs -->
                <nav class="ht-category-tabs" aria-label="বিষয়ভিত্তিক ফিল্টার">
                    <span class="ht-tabs-heading">
                        <?php ht_m3_icon('category', 18); ?>
                        <span>বিষয়সমূহ:</span>
                    </span>
                    <div class="ht-tabs-scroll">
                        <a href="<?php echo esc_url(home_url('/')); ?>" class="ht-tab-btn ht-tab-active">সকল পোস্ট</a>
                        <a href="<?php echo esc_url(home_url('/category/national-university/')); ?>" class="ht-tab-btn">জাতীয় বিশ্ববিদ্যালয়</a>
                        <a href="<?php echo esc_url(home_url('/category/education-guide/')); ?>" class="ht-tab-btn">শিক্ষা গাইড</a>
                        <a href="<?php echo esc_url(home_url('/category/ssc-dakhil/')); ?>" class="ht-tab-btn">এসএসসি ও দাখিল</a>
                        <a href="<?php echo esc_url(home_url('/category/political-science/')); ?>" class="ht-tab-btn">রাষ্ট্রবিজ্ঞান</a>
                        <a href="<?php echo esc_url(home_url('/category/ict-technology/')); ?>" class="ht-tab-btn">আইসিটি</a>
                        <a href="<?php echo esc_url(home_url('/category/job-preparation/')); ?>" class="ht-tab-btn">চাকরি প্রস্তুতি</a>
                    </div>
                </nav>

                <!-- Section Heading -->
                <div class="ht-section-header">
                    <h2 class="ht-section-title">
                        <?php ht_m3_icon('auto_stories', 22, 'ht-icon-primary'); ?>
                        <span>সাম্প্রতিক প্রকাশনা ও পূর্ণাঙ্গ হ্যান্ডনোট</span>
                    </h2>
                </div>

                <!-- Articles Grid Feed -->
                <?php
                $paged = (get_query_var('paged')) ? get_query_var('paged') : 1;
                $feed_query = new WP_Query([
                    'post_type'           => 'post',
                    'post_status'         => 'publish',
                    'paged'               => $paged,
                    'posts_per_page'      => 10,
                    'offset'              => ($paged === 1) ? 4 : 0, // Offset first 4 hero posts on page 1
                    'ignore_sticky_posts' => 1,
                ]);

                if ($feed_query->have_posts()) :
                    $card_counter = 0;
                ?>
                    <div class="ht-cards-grid">
                        <?php
                        while ($feed_query->have_posts()) :
                            $feed_query->the_post();
                            $card_counter++;
                        ?>
                            <article id="post-<?php the_ID(); ?>" <?php post_class('ht-card'); ?>>
                                <div class="ht-card-thumb-wrap">
                                    <a href="<?php the_permalink(); ?>">
                                        <?php ht_the_thumbnail(get_the_ID(), 'ht-card-thumb'); ?>
                                    </a>
                                    <!-- Bookmark Action Button -->
                                    <button class="ht-card-bm-btn ht-bookmark-toggle" data-id="<?php the_ID(); ?>" data-title="<?php echo esc_attr(get_the_title()); ?>" data-url="<?php the_permalink(); ?>" aria-label="পড়ার তালিকায় সংরক্ষণ করুন">
                                        <?php ht_m3_icon('bookmark', 18); ?>
                                    </button>
                                    <div class="ht-card-cat-float">
                                        <?php ht_category_badge(); ?>
                                    </div>
                                </div>

                                <div class="ht-card-body">
                                    <h3 class="ht-card-title">
                                        <a href="<?php the_permalink(); ?>"><?php the_title(); ?></a>
                                    </h3>
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
                        echo paginate_links([
                            'total'     => $feed_query->max_num_pages,
                            'current'   => $paged,
                            'prev_text' => ht_m3_icon('arrow_back', 16, '', false) . ' পূর্ববর্তী',
                            'next_text' => 'পরবর্তী ' . ht_m3_icon('arrow_forward', 16, '', false),
                        ]);
                        ?>
                    </div>

                <?php
                    wp_reset_postdata();
                else :
                    echo '<p class="ht-no-posts">কোনো প্রকাশনা পাওয়া যায়নি।</p>';
                endif;
                ?>

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
