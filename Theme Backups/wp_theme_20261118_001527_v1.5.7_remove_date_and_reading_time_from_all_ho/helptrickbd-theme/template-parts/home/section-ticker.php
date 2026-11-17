<?php
/**
 * Homepage Section 1: Breaking Notice Marquee Ticker
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

if (!get_theme_mod('htbd_show_ticker', get_theme_mod('ht_ticker_enable', true))) {
    return;
}

$badge_text = get_theme_mod('htbd_ticker_badge_text', get_theme_mod('ht_ticker_badge_label', 'সর্বশেষ আপডেট'));
if (empty($badge_text) || $badge_text === 'LATEST UPDATES') {
    $badge_text = 'সর্বশেষ আপডেট';
}

$ticker_count = (int) get_theme_mod('htbd_ticker_count', 5);
$ticker_cat   = (int) get_theme_mod('htbd_ticker_category', 0);

// Use transient caching for ticker query
$ticker_cache_key = 'ht_home_ticker_ids_' . $ticker_cat . '_' . $ticker_count;
$ticker_ids = get_transient($ticker_cache_key);

if (false === $ticker_ids) {
    $ticker_args = array(
        'posts_per_page'      => $ticker_count > 0 ? $ticker_count : 5,
        'post_status'         => 'publish',
        'ignore_sticky_posts' => 1,
        'fields'              => 'ids',
        'no_found_rows'       => true,
    );

    if ($ticker_cat > 0) {
        $ticker_args['cat'] = $ticker_cat;
    }

    $ticker_q = new WP_Query($ticker_args);
    $ticker_ids = !empty($ticker_q->posts) ? $ticker_q->posts : array();
    set_transient($ticker_cache_key, $ticker_ids, 2 * HOUR_IN_SECONDS);
}

if (empty($ticker_ids)) {
    return;
}

$ticker_query = new WP_Query(array(
    'post__in'            => $ticker_ids,
    'orderby'             => 'post__in',
    'posts_per_page'      => count($ticker_ids),
    'ignore_sticky_posts' => 1,
    'no_found_rows'       => true,
));

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