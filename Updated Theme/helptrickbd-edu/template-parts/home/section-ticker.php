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

$badge_text = get_theme_mod('htbd_ticker_badge_text', 'সর্বশেষ');
$ticker_count = (int) get_theme_mod('htbd_ticker_count', 5);
$ticker_cat   = (int) get_theme_mod('htbd_ticker_category', 0);

$ticker_args = array(
    'posts_per_page'      => $ticker_count > 0 ? $ticker_count : 5,
    'post_status'         => 'publish',
    'ignore_sticky_posts' => 1,
    'no_found_rows'       => true,
);

if ($ticker_cat > 0) {
    $ticker_args['cat'] = $ticker_cat;
}

$ticker_query = new WP_Query($ticker_args);

if (!$ticker_query->have_posts()) {
    return;
}
?>
<section class="n-ticker" aria-label="<?php echo esc_attr($badge_text); ?>">
  <div class="n-ticker-badge">
    <span class="n-ticker-dot" aria-hidden="true"></span>
    <span><?php echo esc_html($badge_text); ?></span>
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
