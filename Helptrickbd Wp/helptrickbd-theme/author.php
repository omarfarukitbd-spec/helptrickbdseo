<?php
/**
 * The Template for displaying Author Archive pages
 * Author Profile Card, Total Posts Count, E-E-A-T credentials & posts grid.
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

get_header();

$curauth = (get_query_var('author_name')) ? get_user_by('slug', get_query_var('author_name')) : get_userdata(get_query_var('author'));
$total_author_posts = count_user_posts($curauth->ID, 'post', true);
?>

<main id="primary" class="ht-main-site ht-author-site">
    <div class="ht-container">

        <!-- Breadcrumbs Navigation -->
        <?php ht_breadcrumbs(); ?>

        <!-- Author Profile Banner -->
        <header class="ht-author-profile-card">
            <div class="ht-author-profile-avatar">
                <?php echo get_avatar($curauth->ID, 96, '', '', ['class' => 'ht-avatar-lg']); ?>
            </div>
            <div class="ht-author-profile-info">
                <div class="ht-author-profile-badge-row">
                    <span class="ht-author-role">প্রাবন্ধিক ও শিক্ষক</span>
                    <?php ht_eeat_badge(); ?>
                </div>
                <h1 class="ht-author-profile-name">
                    <?php echo esc_html($curauth->display_name); ?>
                </h1>
                <p class="ht-author-profile-bio">
                    <?php
                    $bio = get_the_author_meta('description', $curauth->ID);
                    echo esc_html($bio ? $bio : 'শিক্ষা ও প্রযুক্তি বিষয়ক গবেষক, লেখক এবং হেল্প ট্রিক বিডি-র নিয়মিত কন্টেন্ট ডিরেক্টর।');
                    ?>
                </p>
                <div class="ht-author-profile-meta">
                    <span class="ht-author-count">
                        <?php ht_m3_icon('auto_stories', 16); ?>
                        <strong><?php echo esc_html(ht_bn_number($total_author_posts)); ?></strong> টি প্রকাশিত আর্টিকেল
                    </span>
                </div>
            </div>
        </header>

        <div class="ht-layout-row">

            <!-- Primary 70% Content Area -->
            <div class="ht-content-area">

                <div class="ht-section-header">
                    <h2 class="ht-section-title">
                        <?php ht_m3_icon('format_list_bulleted', 20, 'ht-icon-primary'); ?>
                        <span>লেখকের প্রকাশিত আর্টিকেলের তালিকা</span>
                    </h2>
                </div>

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
                    <p class="ht-no-posts">এই লেখকের এখনো কোনো পোস্ট প্রকাশিত হয়নি।</p>
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
