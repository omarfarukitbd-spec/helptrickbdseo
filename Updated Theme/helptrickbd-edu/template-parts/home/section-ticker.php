<?php
/**
 * Homepage Section 1: Breaking Notice Marquee Ticker
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}

if (!get_theme_mod('htbd_show_ticker', true)) {
    return;
}

$ticker_query = new WP_Query(array(
    'posts_per_page'      => 6,
    'post_status'         => 'publish',
    'ignore_sticky_posts' => 1,
    'no_found_rows'       => true,
));

if (!$ticker_query->have_posts()) {
    return;
}
?>
<section class="n-ticker" aria-label="<?php esc_attr_e('জরুরি নোটিশ ও সর্বশেষ আপডেট', 'helptrickbd-edu'); ?>">
  <div class="n-ticker-badge">
    <span class="n-ticker-dot" aria-hidden="true"></span>
    <span><?php esc_html_e('জরুরি নোটিশ', 'helptrickbd-edu'); ?></span>
  </div>

  <div class="n-ticker-track">
    <div class="n-ticker-move">
      <?php
      while ($ticker_query->have_posts()) :
          $ticker_query->the_post();
          ?>
          <a href="<?php the_permalink(); ?>" class="n-ticker-item">
            <span><?php the_title(); ?></span>
          </a>
          <span class="n-ticker-sep" aria-hidden="true">&bull;</span>
          <?php
      endwhile;
      wp_reset_postdata();
      ?>
    </div>
  </div>
</section>
