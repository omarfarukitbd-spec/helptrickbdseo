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
        <section class="ht-hero-section" aria-label="<?php esc_attr_e('Featured and Latest Guides', 'helptrickbd'); ?>">
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
                                <?php ht_the_thumbnail(get_the_ID(), 'ht-hero-large', 'ht-hero-lead-img', true); ?>
                            </a>
                            <div class="ht-hero-lead-body">
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
                                    <span class="ht-hero-author">
                                        <span class="ht-hero-author-avatar-badge" aria-hidden="true"><?php ht_m3_icon('person', 15); ?></span>
                                        <span class="ht-hero-author-name"><?php the_author(); ?></span>
                                    </span>
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
        <!-- 2. 4-COLUMN MULTI-CATEGORY GRID (Newspaper Style)        -->
        <!-- ========================================================= -->
        <?php if (get_theme_mod('ht_multi_cat_enable', true)) : 
            $cat_col_1 = get_theme_mod('ht_multi_cat_1', 'national-university');
            $cat_col_2 = get_theme_mod('ht_multi_cat_2', 'political-science');
            $cat_col_3 = get_theme_mod('ht_multi_cat_3', 'education-guide');
            $cat_col_4 = get_theme_mod('ht_multi_cat_4', 'ssc-dakhil');

            $multi_cats = array_filter([$cat_col_1, $cat_col_2, $cat_col_3, $cat_col_4]);
            if (!empty($multi_cats)) :
                $section_title = get_theme_mod('ht_multi_cat_title', 'বিভাগ ও বিষয়ভিত্তিক বিশেষ হ্যান্ডনোট');
                $section_sub   = get_theme_mod('ht_multi_cat_subtitle', 'জাতীয় বিশ্ববিদ্যালয়, বোর্ড পরীক্ষা ও সাম্প্রতিক একাডেমিক স্টাডিজ');
        ?>
        <section class="ht-multi-cat-section" aria-label="<?php echo esc_attr($section_title); ?>">
            <div class="ht-section-header">
                <div class="ht-section-header-left">
                    <h2 class="ht-section-title">
                        <?php ht_m3_icon('grid_view', 22, 'ht-icon-primary'); ?>
                        <span><?php echo esc_html($section_title); ?></span>
                    </h2>
                    <?php if ($section_sub) : ?>
                        <span class="ht-section-subtitle"><?php echo esc_html($section_sub); ?></span>
                    <?php endif; ?>
                </div>
            </div>

            <div class="ht-multi-cat-grid">
                <?php
                foreach ($multi_cats as $cat_slug) :
                    $cat_obj = get_category_by_slug($cat_slug);
                    if (!$cat_obj) continue;

                    $cat_id    = $cat_obj->term_id;
                    $cat_name  = $cat_obj->name;
                    $cat_link  = get_category_link($cat_id);
                    $cat_icon  = function_exists('ht_get_category_icon') ? ht_get_category_icon($cat_slug, $cat_name) : 'folder';
                    $cat_pal   = function_exists('ht_get_category_palette') ? ht_get_category_palette($cat_slug, $cat_name) : ['color' => '#2563eb', 'bg' => 'rgba(37,99,235,0.08)', 'border' => 'rgba(37,99,235,0.2)'];

                    $col_query = new WP_Query([
                        'cat'                 => $cat_id,
                        'posts_per_page'      => 4,
                        'post_status'         => 'publish',
                        'ignore_sticky_posts' => 1,
                        'no_found_rows'       => true,
                    ]);

                    if ($col_query->have_posts()) :
                        $col_count = 0;
                ?>
                    <div class="ht-multi-cat-col" style="--col-accent: <?php echo esc_attr($cat_pal['color']); ?>; --col-bg: <?php echo esc_attr($cat_pal['bg']); ?>; --col-border: <?php echo esc_attr($cat_pal['border']); ?>;">
                        <!-- Column Header -->
                        <div class="ht-col-header">
                            <div class="ht-col-title-wrap">
                                <span class="ht-col-icon"><?php ht_m3_icon($cat_icon, 18); ?></span>
                                <h3 class="ht-col-title">
                                    <a href="<?php echo esc_url($cat_link); ?>"><?php echo esc_html($cat_name); ?></a>
                                </h3>
                            </div>
                            <a href="<?php echo esc_url($cat_link); ?>" class="ht-col-more-link" aria-label="<?php echo esc_attr($cat_name); ?> - সকল পোস্ট">
                                <span>আরও</span>
                                <?php ht_m3_icon('arrow_forward', 14); ?>
                            </a>
                        </div>

                        <!-- Posts List in this Column -->
                        <div class="ht-col-posts">
                            <?php
                            while ($col_query->have_posts()) :
                                $col_query->the_post();
                                $col_count++;

                                if ($col_count === 1) :
                                    // 1st Post: Big Lead Post Card with Image
                            ?>
                                    <article class="ht-col-lead-card">
                                        <a href="<?php the_permalink(); ?>" class="ht-col-lead-thumb-wrap">
                                            <?php ht_the_thumbnail(get_the_ID(), 'ht-card-thumb', 'ht-col-lead-img'); ?>
                                        </a>
                                        <div class="ht-col-lead-body">
                                            <h4 class="ht-col-lead-title">
                                                <a href="<?php the_permalink(); ?>"><?php the_title(); ?></a>
                                            </h4>
                                            <div class="ht-col-lead-meta">
                                                <?php ht_post_date(); ?>
                                                <?php ht_reading_time(); ?>
                                            </div>
                                        </div>
                                    </article>
                                    <div class="ht-col-sub-list">
                                <?php
                                else :
                                    // Posts 2, 3, 4: Compact list items
                                ?>
                                    <article class="ht-col-sub-item">
                                        <span class="ht-col-sub-num"><?php echo esc_html($col_count); ?></span>
                                        <div class="ht-col-sub-body">
                                            <h5 class="ht-col-sub-title">
                                                <a href="<?php the_permalink(); ?>"><?php the_title(); ?></a>
                                            </h5>
                                            <div class="ht-col-sub-meta">
                                                <time datetime="<?php echo esc_attr(get_the_date('c')); ?>">
                                                    <?php echo esc_html(get_the_date('j F, Y')); ?>
                                                </time>
                                            </div>
                                        </div>
                                    </article>
                                <?php
                                endif;
                            endwhile;
                            if ($col_count > 1) :
                                echo '</div><!-- .ht-col-sub-list -->';
                            endif;
                            ?>
                        </div><!-- .ht-col-posts -->

                        <!-- Column Footer Link -->
                        <div class="ht-col-footer">
                            <a href="<?php echo esc_url($cat_link); ?>" class="ht-col-footer-btn">
                                <span><?php esc_html_e('এই বিভাগের সকল পোস্ট', 'helptrickbd'); ?></span>
                                <?php ht_m3_icon('arrow_forward', 14); ?>
                            </a>
                        </div>
                    </div><!-- .ht-multi-cat-col -->
                <?php
                        wp_reset_postdata();
                    endif;
                endforeach;
                ?>
            </div><!-- .ht-multi-cat-grid -->
        </section>
        <?php
            endif;
        endif;
        ?>

        <!-- ========================================================= -->
        <!-- 3. MAIN FEED & SIDEBAR SECTION                           -->
        <!-- ========================================================= -->
        <div class="ht-layout-row">

            <!-- Primary 70% Content Area -->
            <div class="ht-content-area">


                <!-- Section Heading -->
                <div class="ht-section-header">
                    <h2 class="ht-section-title">
                        <?php ht_m3_icon('auto_stories', 22, 'ht-icon-primary'); ?>
                        <span><?php esc_html_e('Recent Publications & Full Handnotes', 'helptrickbd'); ?></span>
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
                        echo paginate_links([
                            'total'     => $feed_query->max_num_pages,
                            'current'   => $paged,
                            'prev_text' => ht_m3_icon('arrow_back', 16, '', false) . ' ' . esc_html__('Previous', 'helptrickbd'),
                            'next_text' => esc_html__('Next', 'helptrickbd') . ' ' . ht_m3_icon('arrow_forward', 16, '', false),
                        ]);
                        ?>
                    </div>

                <?php
                    wp_reset_postdata();
                else :
                    echo '<p class="ht-no-posts">' . esc_html__('No publications found.', 'helptrickbd') . '</p>';
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
