<?php
/**
 * Homepage Section 4: 3-Column Specialized Subject Grid
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}

$grid_query = new WP_Query(array(
    'posts_per_page'      => 3,
    'offset'              => 4,
    'post_status'         => 'publish',
    'ignore_sticky_posts' => 1,
    'no_found_rows'       => true,
));

if (!$grid_query->have_posts()) {
    return;
}
?>
<section class="n-sec" aria-label="<?php esc_attr_e('বিভাগ ও বিষয়ভিত্তিক বিশেষায়িত হ্যান্ডনোট', 'helptrickbd-edu'); ?>">
  <div class="n-sec-head">
    <h3><?php esc_html_e('বিভাগ ও বিষয়ভিত্তিক বিশেষায়িত হ্যান্ডনোট', 'helptrickbd-edu'); ?></h3>
    <span class="rule" aria-hidden="true"></span>
    <a href="<?php echo esc_url(home_url('/blog/')); ?>">
      <?php esc_html_e('সব লেখা →', 'helptrickbd-edu'); ?>
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
