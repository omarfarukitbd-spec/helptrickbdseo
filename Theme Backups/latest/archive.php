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
                <span><?php esc_html_e('Category Archive', 'helptrickbd'); ?></span>
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
                            get_template_part('template-parts/content', 'card');

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
                            'prev_text' => ht_m3_icon('arrow_back', 16, '', false) . ' ' . esc_html__('Previous', 'helptrickbd'),
                            'next_text' => esc_html__('Next', 'helptrickbd') . ' ' . ht_m3_icon('arrow_forward', 16, '', false),
                        ]);
                        ?>
                    </div>

                <?php else : ?>
                    <?php get_template_part('template-parts/content', 'none'); ?>
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
