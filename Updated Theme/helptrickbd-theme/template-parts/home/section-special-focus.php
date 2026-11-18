<?php
/**
 * Homepage Section 5: National University & Special Focus (Single Clean Container)
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

if (!get_theme_mod('htbd_show_sec_nu', get_theme_mod('ht_show_sec_nu', true))) {
    return;
}

$is_bn = function_exists('ht_is_bangla_locale') ? ht_is_bangla_locale() : true;
$default_title = $is_bn ? 'জাতীয় বিশ্ববিদ্যালয় ও উচ্চশিক্ষা' : 'National University & Higher Studies';
$sec_title = get_theme_mod('htbd_sec_nu_title', get_theme_mod('ht_sec_nu_title', $default_title));
if (empty($sec_title)) {
    $sec_title = $default_title;
}

$cat_id     = (int) get_theme_mod('htbd_sec_nu_category', get_theme_mod('ht_sec_nu_category', 0));
$post_count = (int) get_theme_mod('htbd_sec_nu_count', get_theme_mod('ht_sec_nu_count', 6));

$default_link = $is_bn ? 'সকল হ্যান্ডনোট →' : 'All NU Handnotes →';
$link_text  = get_theme_mod('htbd_sec_nu_link_text', get_theme_mod('ht_sec_nu_link_text', $default_link));
if (empty($link_text)) {
    $link_text = $default_link;
}

$target_cat_id = 0;
if ($cat_id > 0) {
    $target_cat_id = $cat_id;
    $target_link = get_category_link($cat_id);
} else {
    $nu_term = get_category_by_slug('national-university');
    if ($nu_term) {
        $target_cat_id = $nu_term->term_id;
        $target_link = get_category_link($nu_term->term_id);
    } else {
        $target_link = home_url('/category/national-university/');
    }
}

$nu_cache_key = 'ht_home_nu_post_ids_' . $target_cat_id . '_' . $post_count . '_' . ($is_bn ? 'bn' : 'en');
$nu_post_ids = get_transient($nu_cache_key);

if (false === $nu_post_ids) {
    $query_args = array(
        'posts_per_page'      => $post_count > 0 ? $post_count : 6,
        'post_status'         => 'publish',
        'ignore_sticky_posts' => 1,
        'fields'              => 'ids',
        'no_found_rows'       => true,
    );

    if ($target_cat_id > 0) {
        $query_args['cat'] = $target_cat_id;
    }

    $nu_q = new WP_Query($query_args);
    $nu_post_ids = !empty($nu_q->posts) ? $nu_q->posts : array();
    if (!empty($nu_post_ids)) {
        set_transient($nu_cache_key, $nu_post_ids, 2 * HOUR_IN_SECONDS);
    }
}

if (empty($nu_post_ids)) {
    return;
}

$focus_query = new WP_Query(array(
    'post__in'            => $nu_post_ids,
    'orderby'             => 'post__in',
    'posts_per_page'      => count($nu_post_ids),
    'ignore_sticky_posts' => 1,
    'no_found_rows'       => true,
));

if (!$focus_query->have_posts()) {
    return;
}
?>
<section class="n-sec" aria-label="<?php echo esc_attr($sec_title); ?>">
  <div class="n-sec-head">
    <h3><?php echo esc_html($sec_title); ?></h3>
    <span class="rule" aria-hidden="true"></span>
    <a href="<?php echo esc_url($target_link); ?>">
      <?php echo esc_html($link_text); ?>
    </a>
  </div>

  <div class="n-label-grid">
    <?php
    while ($focus_query->have_posts()) :
        $focus_query->the_post();
        ?>
        <a href="<?php the_permalink(); ?>" class="n-lrow">
          <?php if (has_post_thumbnail()) : ?>
            <?php
            the_post_thumbnail('medium', array(
                'loading'     => 'lazy',
                'decoding'    => 'async',
                'class'       => 'n-lrow-img',
                'width'       => 96,
                'height'      => 68,
                'alt'         => '',
                'aria-hidden' => 'true',
            ));
            ?>
          <?php else : ?>
            <img src="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/Thumbnail%20BG/nu.webp" loading="lazy" decoding="async" class="n-lrow-img" width="96" height="68" alt="" aria-hidden="true">
          <?php endif; ?>

          <div class="n-lrow-text">
            <span class="lt-t"><?php the_title(); ?></span>
          </div>
        </a>
        <?php
    endwhile;
    wp_reset_postdata();
    ?>
  </div>
</section>