<?php
/**
 * Sidebar Widget 1: Trending Most-Viewed Handnotes (Numbered List 1-6)
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

if (!get_theme_mod('ht_sidebar_popular_enable', true)) {
    return;
}

$is_en = function_exists('ht_is_bangla_locale') && !ht_is_bangla_locale();
$popular_title = get_theme_mod('ht_sidebar_popular_title', '');
if (empty($popular_title)) {
    $popular_title = $is_en ? 'Popular & Trending Articles' : 'জনপ্রিয় ও আলোচিত হ্যান্ডনোট';
}
$popular_count = (int) get_theme_mod('ht_sidebar_popular_count', 6);
if ($popular_count < 1) {
    $popular_count = 6;
}

$popular_post_ids = get_transient('ht_sidebar_pop_ids');

if (false === $popular_post_ids) {
    $pop_q = new WP_Query(array(
        'posts_per_page'      => $popular_count,
        'post_status'         => 'publish',
        'meta_key'            => 'ht_post_views_count',
        'orderby'             => 'meta_value_num date',
        'order'               => 'DESC',
        'ignore_sticky_posts' => 1,
        'fields'              => 'ids',
        'no_found_rows'       => true,
    ));

    if (empty($pop_q->posts)) {
        $pop_q = new WP_Query(array(
            'posts_per_page'      => $popular_count,
            'post_status'         => 'publish',
            'meta_key'            => 'htbd_post_views_count',
            'orderby'             => 'meta_value_num date',
            'order'               => 'DESC',
            'ignore_sticky_posts' => 1,
            'fields'              => 'ids',
            'no_found_rows'       => true,
        ));
    }

    if (empty($pop_q->posts)) {
        $pop_q = new WP_Query(array(
            'posts_per_page'      => $popular_count,
            'post_status'         => 'publish',
            'orderby'             => 'comment_count date',
            'order'               => 'DESC',
            'ignore_sticky_posts' => 1,
            'fields'              => 'ids',
            'no_found_rows'       => true,
        ));
    }

    $popular_post_ids = !empty($pop_q->posts) ? $pop_q->posts : array();
    set_transient('ht_sidebar_pop_ids', $popular_post_ids, 6 * HOUR_IN_SECONDS);
}

if (empty($popular_post_ids)) {
    return;
}

$cached_popular_query = new WP_Query(array(
    'post__in'            => $popular_post_ids,
    'orderby'             => 'post__in',
    'posts_per_page'      => count($popular_post_ids),
    'ignore_sticky_posts' => 1,
    'no_found_rows'       => true,
));

if (!$cached_popular_query->have_posts()) {
    return;
}
?>
<div class="n-popular-widget" aria-label="<?php echo $is_en ? esc_attr__('Popular Articles', 'helptrickbd') : esc_attr__('জনপ্রিয় হ্যান্ডনোট', 'helptrickbd'); ?>">
  <div class="n-pop-tab-header">
    <span class="n-pop-tab active"><?php echo esc_html($popular_title); ?></span>
  </div>

  <div class="n-pop-list">
    <?php
    $rank = 1;
    while ($cached_popular_query->have_posts()) :
        $cached_popular_query->the_post();
        ?>
        <a href="<?php the_permalink(); ?>" class="n-pop-item">
          <span class="n-pop-num"><?php echo esc_html(function_exists('ht_number') ? ht_number($rank) : (function_exists('ht_bn_number') ? ht_bn_number($rank) : $rank)); ?></span>
          <span class="n-pop-title"><?php the_title(); ?></span>
        </a>
        <?php
        $rank++;
    endwhile;
    wp_reset_postdata();
    ?>
  </div>
</div>
