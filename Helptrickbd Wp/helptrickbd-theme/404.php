<?php
/**
 * The Template for displaying 404 pages (Not Found)
 * High-conversion search box & popular recommendations.
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

get_header();
?>

<main id="primary" class="ht-main-site ht-404-site">
    <div class="ht-container">

        <!-- Breadcrumbs Navigation -->
        <?php ht_breadcrumbs(); ?>

        <div class="ht-404-wrapper">
            <div class="ht-404-icon-wrap">
                <?php ht_m3_icon('help_outline', 64, 'ht-icon-404'); ?>
            </div>
            <h1 class="ht-404-title"><?php esc_html_e('404: Page Not Found', 'helptrickbd'); ?></h1>
            <p class="ht-404-desc">
                <?php esc_html_e('The page you are looking for might have been removed, had its name changed, or is temporarily unavailable. Please try searching below or explore our popular categories.', 'helptrickbd'); ?>
            </p>

            <!-- Search Form -->
            <div class="ht-404-search-box">
                <?php get_search_form(); ?>
            </div>

            <!-- Popular Quick Links -->
            <div class="ht-404-suggestions">
                <span class="ht-404-sug-title"><?php esc_html_e('Popular Topics:', 'helptrickbd'); ?></span>
                <div class="ht-404-tags">
                    <a href="<?php echo esc_url(home_url('/category/national-university/')); ?>" class="ht-tab-btn"><?php esc_html_e('National University', 'helptrickbd'); ?></a>
                    <a href="<?php echo esc_url(home_url('/category/education-guide/')); ?>" class="ht-tab-btn"><?php esc_html_e('Education Guide', 'helptrickbd'); ?></a>
                    <a href="<?php echo esc_url(home_url('/category/ssc-dakhil/')); ?>" class="ht-tab-btn"><?php esc_html_e('SSC & Dakhil', 'helptrickbd'); ?></a>
                    <a href="<?php echo esc_url(home_url('/category/political-science/')); ?>" class="ht-tab-btn"><?php esc_html_e('Political Science', 'helptrickbd'); ?></a>
                    <a href="<?php echo esc_url(home_url('/category/ict-technology/')); ?>" class="ht-tab-btn"><?php esc_html_e('ICT & Tech', 'helptrickbd'); ?></a>
                </div>
            </div>

            <div class="ht-404-back-home">
                <a href="<?php echo esc_url(home_url('/')); ?>" class="ht-btn ht-btn-primary">
                    <?php ht_m3_icon('home', 18); ?>
                    <span><?php esc_html_e('Back to Home', 'helptrickbd'); ?></span>
                </a>
            </div>

        </div>

    </div><!-- .ht-container -->
</main><!-- #primary -->

<?php
get_footer();
