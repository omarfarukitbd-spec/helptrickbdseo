<?php
/**
 * Homepage Section 3: Specialized Subject Grid (Configurable from Admin Panel)
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}

if (!get_theme_mod('htbd_show_sec_ssc', true)) {
    return;
}

$sec_title     = get_theme_mod('htbd_sec_ssc_title', 'এসএসসি / দাখিল');
$cat_id        = (int) get_theme_mod('htbd_sec_ssc_category', 0);
$post_count    = (int) get_theme_mod('htbd_sec_ssc_count', 5);
$link_text     = get_theme_mod('htbd_sec_ssc_link_text', 'সব লেখা →');

$query_args = array(
    'posts_per_page'      => $post_count > 0 ? $post_count : 5,
    'post_status'         => 'publish',
    'ignore_sticky_posts' => 1,
    'no_found_rows'       => true,
);

if ($cat_id > 0) {
    $query_args['cat'] = $cat_id;
    $target_link = get_category_link($cat_id);
} else {
    // Default to 'ssc-dakhil' category
    $ssc_term = get_category_by_slug('ssc-dakhil');
    if ($ssc_term) {
        $query_args['cat'] = $ssc_term->term_id;
        $target_link = get_category_link($ssc_term->term_id);
    } else {
        $target_link = home_url('/category/ssc-dakhil/');
    }
}

$grid_query = new WP_Query($query_args);

if (!$grid_query->have_posts()) {
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

  <div class="n-grid3">
    <?php
    while ($grid_query->have_posts()) :
        $grid_query->the_post();
        $cats = get_the_category();
        ?>
        <div class="n-item">
          <span class="sk">
            <?php echo !empty($cats) ? esc_html($cats[0]->name) : esc_html__('হ্যান্ডনোট', 'helptrickbd-edu'); ?>
          </span>
          <h4>
            <a href="<?php the_permalink(); ?>">
              <?php the_title(); ?>
            </a>
          </h4>
          <p><?php echo esc_html(wp_trim_words(get_the_excerpt(), 18, '...')); ?></p>
          <div class="meta">
            <span><?php echo esc_html(get_the_date('j F, Y')); ?></span> &bull; 
            <span><?php echo esc_html(htbd_reading_time()); ?></span>
          </div>
        </div>
        <?php
    endwhile;
    wp_reset_postdata();
    ?>
  </div>
</section>
