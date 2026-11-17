<?php
/**
 * Homepage Section 6: Photo Guides & Gallery (Configurable from Admin Panel)
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

if (!get_theme_mod('htbd_show_sec_gallery', get_theme_mod('ht_show_sec_gallery', true))) {
    return;
}

$sec_title = get_theme_mod('htbd_sec_gallery_title', get_theme_mod('ht_sec_gallery_title', 'পরীক্ষা প্রস্তুতি ও সচিত্র গাইড'));
if (empty($sec_title) || $sec_title === 'Visual Study Guides & Infographics') {
    $sec_title = 'পরীক্ষা প্রস্তুতি ও সচিত্র গাইড';
}

$cat_id     = (int) get_theme_mod('htbd_sec_gallery_category', get_theme_mod('ht_sec_gallery_category', 0));
$post_count = (int) get_theme_mod('htbd_sec_gallery_count', get_theme_mod('ht_sec_gallery_count', 4));
$link_text  = get_theme_mod('htbd_sec_gallery_link_text', get_theme_mod('ht_sec_gallery_link_text', 'সকল গ্যালারি →'));
if (empty($link_text) || $link_text === 'View Gallery →') {
    $link_text = 'সকল গ্যালারি →';
}

$photo_cache_key = 'ht_home_photo_post_ids_' . $cat_id . '_' . $post_count;
$photo_post_ids = get_transient($photo_cache_key);

if (false === $photo_post_ids) {
    $query_args = array(
        'posts_per_page'      => $post_count > 0 ? $post_count : 4,
        'post_status'         => 'publish',
        'ignore_sticky_posts' => 1,
        'fields'              => 'ids',
        'no_found_rows'       => true,
    );

    if ($cat_id > 0) {
        $query_args['cat'] = $cat_id;
    }

    $photo_q = new WP_Query($query_args);
    $photo_post_ids = !empty($photo_q->posts) ? $photo_q->posts : array();
    set_transient($photo_cache_key, $photo_post_ids, 2 * HOUR_IN_SECONDS);
}

if ($cat_id > 0) {
    $target_link = get_category_link($cat_id);
} else {
    $target_link = home_url('/blog/');
}

if (empty($photo_post_ids)) {
    return;
}

$photo_query = new WP_Query(array(
    'post__in'            => $photo_post_ids,
    'orderby'             => 'post__in',
    'posts_per_page'      => count($photo_post_ids),
    'ignore_sticky_posts' => 1,
    'no_found_rows'       => true,
));

if (!$photo_query->have_posts()) {
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

  <div class="n-photogrid">
    <?php
    while ($photo_query->have_posts()) :
        $photo_query->the_post();
        ?>
        <a href="<?php the_permalink(); ?>" class="n-pcard">
          <div class="pim">
            <?php if (has_post_thumbnail()) : ?>
              <?php
              the_post_thumbnail('ht-card-thumb', array(
                  'loading'  => 'lazy',
                  'decoding' => 'async',
                  'width'    => 300,
                  'height'   => 200,
                  'alt'      => esc_attr(get_the_title()),
              ));
              ?>
            <?php else : ?>
              <img src="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/Thumbnail%20BG/ict.webp" loading="lazy" decoding="async" width="300" height="200" alt="<?php the_title_attribute(); ?>">
            <?php endif; ?>
          </div>
          <h4><?php the_title(); ?></h4>
        </a>
        <?php
    endwhile;
    wp_reset_postdata();
    ?>
  </div>
</section>