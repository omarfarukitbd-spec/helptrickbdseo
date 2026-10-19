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
                        <span><?php esc_html_e('Latest Publications', 'helptrickbd'); ?></span>
                    </h1>
                </div>

                <?php if (have_posts()) : ?>
                    <div class="ht-cards-grid">
                        <?php
                        $card_counter = 0;
                        while (have_posts()) :
                            the_post();
                            $card_counter++;
                            get_template_part('template-parts/content', 'card');

                            if ($card_counter === 4) {
                                ht_render_in_feed_ad();
                            }
                        endwhile;
                        ?>
                    </div><!-- .ht-cards-grid -->

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

            <aside class="ht-sidebar-area">
                <?php get_sidebar(); ?>
            </aside>

        </div><!-- .ht-layout-row -->

    </div><!-- .ht-container -->
</main><!-- #primary -->

<?php
get_footer();
