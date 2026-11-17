<?php
/**
 * Single Post Component: Related Posts with 12-Hour Transient Caching
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

if (!get_theme_mod('ht_related_posts_enable', true)) {
    return;
}

$current_post_id = get_the_ID();
$transient_key   = 'ht_related_' . $current_post_id;
$related_ids     = get_transient($transient_key);

if (false === $related_ids) {
    $current_cats = wp_get_post_categories($current_post_id);
    if (!empty($current_cats)) {
        $rel_q = new WP_Query([
            'category__in'        => $current_cats,
            'post__not_in'        => [$current_post_id],
            'posts_per_page'      => 3,
            'ignore_sticky_posts' => 1,
            'fields'              => 'ids',
            'no_found_rows'       => true,
        ]);
        $related_ids = $rel_q->posts;
        set_transient($transient_key, $related_ids, 12 * HOUR_IN_SECONDS);
    } else {
        $related_ids = [];
    }
}

if (!empty($related_ids)) :
    $cached_query = new WP_Query([
        'post__in'            => $related_ids,
        'orderby'             => 'post__in',
        'posts_per_page'      => count($related_ids),
        'ignore_sticky_posts' => 1,
        'no_found_rows'       => true,
    ]);
    if ($cached_query->have_posts()) :
?>
    <section class="ht-related-section" aria-label="<?php esc_attr_e('সম্পর্কিত হ্যান্ডনোট ও গাইড', 'helptrickbd'); ?>">
        <h3 class="ht-related-heading">
            <?php ht_m3_icon('menu_book', 20); ?>
            <span><?php esc_html_e('সম্পর্কিত হ্যান্ডনোট ও গাইড', 'helptrickbd'); ?></span>
        </h3>
        <div class="ht-related-grid">
            <?php
            while ($cached_query->have_posts()) :
                $cached_query->the_post();
            ?>
                <article class="ht-related-card">
                    <a href="<?php the_permalink(); ?>" class="ht-related-thumb-wrap">
                        <?php ht_the_thumbnail(get_the_ID(), 'ht-card-thumb'); ?>
                    </a>
                    <div class="ht-related-body">
                        <h4 class="ht-related-title">
                            <a href="<?php the_permalink(); ?>" title="<?php the_title_attribute(); ?>"><?php the_title(); ?></a>
                        </h4>
                        <span class="ht-related-date"><?php ht_post_date(); ?></span>
                    </div>
                </article>
            <?php
            endwhile;
            wp_reset_postdata();
            ?>
        </div>
    </section>
<?php
    endif;
endif;
