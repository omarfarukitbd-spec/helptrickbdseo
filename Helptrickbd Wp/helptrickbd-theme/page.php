<?php
/**
 * The Template for displaying all standalone pages
 * (About Us, Contact Us, Privacy Policy, Terms, Disclaimer)
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

get_header();
?>

<main id="primary" class="ht-main-site ht-page-site">
    <div class="ht-container">

        <!-- Breadcrumbs Navigation -->
        <?php ht_breadcrumbs(); ?>

        <div class="ht-layout-row ht-page-layout">

            <!-- Primary Content Area -->
            <article id="post-<?php the_ID(); ?>" <?php post_class('ht-page-col'); ?>>
                <?php
                while (have_posts()) :
                    the_post();
                ?>
                    <header class="ht-page-header">
                        <h1 class="ht-page-title"><?php the_title(); ?></h1>
                    </header>

                    <div class="ht-page-content ht-entry-content">
                        <?php the_content(); ?>
                    </div>
                <?php endwhile; ?>
            </article>

            <!-- Sidebar (Optional on pages) -->
            <aside class="ht-sidebar-area">
                <?php get_sidebar(); ?>
            </aside>

        </div><!-- .ht-layout-row -->

    </div><!-- .ht-container -->
</main><!-- #primary -->

<?php
get_footer();
