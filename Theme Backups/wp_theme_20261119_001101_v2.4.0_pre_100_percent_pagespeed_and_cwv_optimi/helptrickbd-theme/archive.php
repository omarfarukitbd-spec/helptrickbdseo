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
                <span><?php echo (function_exists('ht_is_bangla_locale') && !ht_is_bangla_locale()) ? esc_html__('Topic & Category Archive', 'helptrickbd') : esc_html__('বিভাগ ও বিষয়ভিত্তিক আর্কাইভ', 'helptrickbd'); ?></span>
            </div>
            <h1 class="ht-archive-title"><?php the_archive_title(); ?></h1>
            <?php
            $archive_desc = get_the_archive_description();
            if ($archive_desc) :
            ?>
                <div class="ht-archive-desc"><?php echo wp_kses_post($archive_desc); ?></div>
            <?php endif; ?>
            <?php
            // v1.4.10 (F7): post count + sub-category chips under the H1.
            global $wp_query;
            $ht_archive_count = (int) $wp_query->found_posts;
            $count_str = function_exists('ht_number') ? ht_number($ht_archive_count) : (function_exists('ht_bn_number') ? ht_bn_number($ht_archive_count) : $ht_archive_count);
            $posts_label = (function_exists('ht_is_bangla_locale') && !ht_is_bangla_locale()) ? esc_html__('Articles', 'helptrickbd') : esc_html__('টি পোস্ট', 'helptrickbd');
            ?>
            <div class="ht-archive-meta">
                <span class="ht-archive-count"><?php echo esc_html($count_str); ?> <?php echo esc_html($posts_label); ?></span>
            </div>
            <?php
            if (is_category()) :
                $ht_queried_cat = get_queried_object();
                $ht_sub_cats = get_categories([
                    'parent'     => $ht_queried_cat->term_id,
                    'hide_empty' => true,
                    'orderby'    => 'count',
                    'order'      => 'DESC',
                ]);
                if (!empty($ht_sub_cats)) :
                    $subcat_aria = (function_exists('ht_is_bangla_locale') && !ht_is_bangla_locale()) ? esc_attr__('Subcategories', 'helptrickbd') : esc_attr__('সাব-ক্যাটাগরি', 'helptrickbd');
            ?>
                <div class="ht-archive-subcats" role="navigation" aria-label="<?php echo esc_attr($subcat_aria); ?>">
                    <?php foreach ($ht_sub_cats as $ht_sub_cat) : 
                        $sub_count = function_exists('ht_number') ? ht_number($ht_sub_cat->count) : $ht_sub_cat->count;
                        $sub_name  = function_exists('ht_get_localized_term_name') ? ht_get_localized_term_name($ht_sub_cat) : $ht_sub_cat->name;
                    ?>
                        <a href="<?php echo esc_url(get_category_link($ht_sub_cat->term_id)); ?>" class="ht-archive-subcat-chip"><?php echo esc_html($sub_name); ?> (<?php echo esc_html($sub_count); ?>)</a>
                    <?php endforeach; ?>
                </div>
            <?php
                endif;
            endif;
            ?>
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
                        $prev_label = (function_exists('ht_is_bangla_locale') && !ht_is_bangla_locale()) ? esc_html__('Previous', 'helptrickbd') : esc_html__('পূর্ববর্তী', 'helptrickbd');
                        $next_label = (function_exists('ht_is_bangla_locale') && !ht_is_bangla_locale()) ? esc_html__('Next', 'helptrickbd') : esc_html__('পরবর্তী', 'helptrickbd');
                        the_posts_pagination([
                            'prev_text' => ht_m3_icon('arrow_back', 16, '', false) . ' ' . $prev_label,
                            'next_text' => $next_label . ' ' . ht_m3_icon('arrow_forward', 16, '', false),
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
