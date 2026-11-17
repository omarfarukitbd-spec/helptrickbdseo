<?php
/**
 * Homepage Section 6: Photo Guides & Gallery (Configurable from Admin Panel)
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}

if (!get_theme_mod('htbd_show_sec_gallery', true)) {
    return;
}

$sec_title  = get_theme_mod('htbd_sec_gallery_title', 'Visual Study Guides & Infographics');
if ($sec_title === 'পরীক্ষা প্রস্তুতি ও সচিত্র গাইড') {
    $sec_title = 'Visual Study Guides & Infographics';
}
$cat_id     = (int) get_theme_mod('htbd_sec_gallery_category', 0);
$post_count = (int) get_theme_mod('htbd_sec_gallery_count', 4);
$link_text  = get_theme_mod('htbd_sec_gallery_link_text', 'View Gallery →');
if ($link_text === 'সকল গ্যালারি →') {
    $link_text = 'View Gallery →';
}

$query_args = array(
    'posts_per_page'      => $post_count > 0 ? $post_count : 4,
    'post_status'         => 'publish',
    'ignore_sticky_posts' => 1,
    'no_found_rows'       => true,
);

if ($cat_id > 0) {
    $query_args['cat'] = $cat_id;
    $target_link = get_category_link($cat_id);
} else {
    $target_link = home_url('/blog/');
}

$photo_query = new WP_Query($query_args);

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
              the_post_thumbnail('ht-photo-grid', array(
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
