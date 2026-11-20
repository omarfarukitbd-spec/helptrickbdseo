<?php
/**
 * Homepage Section 3: Specialized Subject Grid (Configurable from Admin Panel)
 * Strictly queries SSC & Dakhil category (6 posts on desktop, 5 on mobile, titles only)
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

if (!get_theme_mod('htbd_show_sec_ssc', get_theme_mod('ht_show_sec_ssc', true))) {
    return;
}

$is_bn = function_exists('ht_is_bangla_locale') ? ht_is_bangla_locale() : true;
$default_title = $is_bn ? 'এসএসসি ও দাখিল' : 'SSC & Dakhil';
$sec_title = get_theme_mod('htbd_sec_ssc_title', get_theme_mod('ht_sec_ssc_title', ''));
if (empty($sec_title) || $sec_title === 'এসএসসি ও দাখিল প্রস্তুতি' || $sec_title === 'SSC & Dakhil Examination Hub') {
    $sec_title = $default_title;
}

$cat_id = (int) get_theme_mod('htbd_sec_ssc_category', get_theme_mod('ht_sec_ssc_category', 0));

$default_link = $is_bn ? 'সব দেখুন →' : 'View All →';
$link_text = get_theme_mod('htbd_sec_ssc_link_text', get_theme_mod('ht_sec_ssc_link_text', ''));
if (empty($link_text) || $link_text === 'সকল হ্যান্ডনোট →' || $link_text === 'View All Handnotes →') {
    $link_text = $default_link;
}

// Strict SSC & Dakhil Category Resolution
$target_term_id = 0;
if ($cat_id > 0) {
    $target_term_id = $cat_id;
} else {
    $ssc_term = get_category_by_slug('ssc-dakhil');
    if (!$ssc_term) {
        $ssc_term = get_term_by('name', 'SSC & Dakhil', 'category');
    }
    if ($ssc_term) {
        $target_term_id = $ssc_term->term_id;
    }
}

$ssc_cache_key = 'ht_home_ssc_post_ids_' . $target_term_id . '_' . ($is_bn ? 'bn' : 'en');
$ssc_post_ids = get_transient($ssc_cache_key);

if (false === $ssc_post_ids) {
    $query_args = array(
        'posts_per_page'      => 6,
        'post_status'         => 'publish',
        'ignore_sticky_posts' => 1,
        'fields'              => 'ids',
        'no_found_rows'       => true,
    );

    if ($target_term_id > 0) {
        $query_args['cat'] = $target_term_id;
    }

    $q = new WP_Query($query_args);
    $ssc_post_ids = !empty($q->posts) ? $q->posts : array();
    set_transient($ssc_cache_key, $ssc_post_ids, 2 * HOUR_IN_SECONDS);
}

if ($target_term_id > 0) {
    $target_link = get_category_link($target_term_id);
} else {
    $target_link = home_url('/category/ssc-dakhil/');
}

if (empty($ssc_post_ids)) {
    return;
}

$grid_query = new WP_Query(array(
    'post__in'            => $ssc_post_ids,
    'orderby'             => 'post__in',
    'posts_per_page'      => count($ssc_post_ids),
    'ignore_sticky_posts' => 1,
    'no_found_rows'       => true,
));

if (!$grid_query->have_posts()) {
    return;
}
?>
<section class="n-sec n-sec-ssc" aria-label="<?php echo esc_attr($sec_title); ?>">
  <div class="n-sec-head">
    <h3><?php echo esc_html($sec_title); ?></h3>
    <span class="rule" aria-hidden="true"></span>
    <a href="<?php echo esc_url($target_link); ?>">
      <?php echo esc_html($link_text); ?>
    </a>
  </div>

  <div class="n-grid3">
    <?php
    while ($grid_query->have_posts()) :
        $grid_query->the_post();
        ?>
        <div class="n-item">
          <span class="sk">
            <?php esc_html_e('এসএসসি ও দাখিল', 'helptrickbd'); ?>
          </span>
          <h4>
            <a href="<?php the_permalink(); ?>">
              <?php the_title(); ?>
            </a>
          </h4>
        </div>
        <?php
    endwhile;
    wp_reset_postdata();
    ?>
  </div>
</section>