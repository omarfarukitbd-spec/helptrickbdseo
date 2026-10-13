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
                <span><?php esc_html_e('Search Results', 'helptrickbd'); ?></span>
            </div>
            <h1 class="ht-archive-title">
                "<?php echo esc_html(get_search_query()); ?>"
            </h1>
            <p class="ht-search-count">
                <?php
                printf(
                    /* translators: %s: number of found posts */
                    esc_html__('Found %s results', 'helptrickbd'),
                    esc_html($wp_query->found_posts)
                );
                ?>
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
                            get_template_part('template-parts/content', 'card');
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
