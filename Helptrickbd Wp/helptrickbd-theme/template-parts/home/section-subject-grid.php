<?php
/**
 * Homepage Section 3: Specialized Subject Grid (Configurable from Admin Panel)
 * Strictly queries SSC & Dakhil category (6 posts on desktop, 5 on mobile, titles only)
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}

if (!get_theme_mod('htbd_show_sec_ssc', true)) {
    return;
}

$sec_title     = get_theme_mod('htbd_sec_ssc_title', 'SSC & Dakhil Examination Hub');
if ($sec_title === 'এসএসসি / দাখিল') {
    $sec_title = 'SSC & Dakhil Examination Hub';
}
$cat_id        = (int) get_theme_mod('htbd_sec_ssc_category', 0);
$link_text     = get_theme_mod('htbd_sec_ssc_link_text', 'View All Handnotes →');
if ($link_text === 'সব লেখা →' || $link_text === 'সব পোস্ট দেখুন →') {
    $link_text = 'View All Handnotes →';
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

$query_args = array(
    'posts_per_page'      => 6, // 6 on desktop, 5 on mobile via CSS
    'post_status'         => 'publish',
    'ignore_sticky_posts' => 1,
    'no_found_rows'       => true,
);

if ($target_term_id > 0) {
    $query_args['cat'] = $target_term_id;
    $target_link = get_category_link($target_term_id);
} else {
    $target_link = home_url('/category/ssc-dakhil/');
}

$grid_query = new WP_Query($query_args);

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
            <?php esc_html_e('SSC & Dakhil', 'helptrickbd-edu'); ?>
          </span>
          <h4>
            <a href="<?php the_permalink(); ?>">
              <?php the_title(); ?>
            </a>
          </h4>
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
