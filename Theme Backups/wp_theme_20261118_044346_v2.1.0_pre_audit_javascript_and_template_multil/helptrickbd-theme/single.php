<?php
/**
 * The Master Controller for displaying single posts
 * Clean Micro-Modular Architecture (Enterprise Grade)
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

get_header();

// 1. Live Reading Progress Bar
get_template_part('template-parts/single/reading-bar');
?>

<main id="primary" class="ht-main-site ht-single-site">
    <div class="ht-container">

        <!-- Breadcrumbs Navigation -->
        <?php ht_breadcrumbs(); ?>

        <div class="ht-layout-row">

            <!-- Primary Article Column (70%) -->
            <article id="post-<?php the_ID(); ?>" <?php post_class('ht-article-col'); ?>>
                
                <?php
                while (have_posts()) :
                    the_post();

                    // 2. Article Header (Badges, Title, Meta, Freshness, Share, Toolbelt, Ad & TOC)
                    get_template_part('template-parts/single/article-header');

                    // 3. Article Main Content
                    get_template_part('template-parts/single/article-content');

                    // 4. Multi-Platform Social Share Bar (Bottom)
                    ht_social_share_bar('bottom');

                    // 5. Interactive Post Helpful / Like Reaction Box
                    ht_post_reaction_box();

                    // 6. Tags Cloud
                    get_template_part('template-parts/single/tags-list');

                    // 7. Google E-E-A-T Compliant Author Bio Box
                    get_template_part('template-parts/single/author-bio');

                    // 8. Previous / Next Article Navigation Cards
                    get_template_part('template-parts/single/post-navigation');

                    // Ad Slot After Content
                    ht_render_ad('ht_ad_after_content', 'ht-ad-single-bottom', 250);

                    // 9. Related Posts (12-Hour Transient Cached Grid)
                    get_template_part('template-parts/single/related-posts');

                    // Comments Template
                    if (comments_open() || get_comments_number()) :
                        comments_template();
                    endif;

                endwhile;
                ?>

            </article><!-- .ht-article-col -->

            <!-- Sidebar (30%) -->
            <aside class="ht-sidebar-area">
                <?php get_sidebar(); ?>
            </aside>

        </div><!-- .ht-layout-row -->

    </div><!-- .ht-container -->
</main><!-- #primary -->

<?php
// 10. Floating Highlight Dock & Print Watermark
get_template_part('template-parts/single/highlight-dock');

get_footer();
