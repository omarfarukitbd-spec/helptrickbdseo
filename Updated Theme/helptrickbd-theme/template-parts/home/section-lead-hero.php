<?php
/**
 * Homepage Section 3: Magazine Lead Hero & Spotlight Deck
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

if (!get_theme_mod('htbd_show_lead_hero', get_theme_mod('ht_show_lead_hero', true))) {
    return;
}

$is_bn      = function_exists('ht_is_bangla_locale') ? ht_is_bangla_locale() : true;
$hero_cat   = (int) get_theme_mod('htbd_hero_category', get_theme_mod('ht_hero_category', 0));
$default_badge = $is_bn ? 'সর্বশেষ প্রকাশনা' : 'LATEST POSTS';
$badge_text = get_theme_mod('htbd_hero_badge_text', get_theme_mod('ht_hero_badge_text', $default_badge));
if (empty($badge_text)) {
    $badge_text = $default_badge;
}

$hero_cache_key = 'ht_home_lead_hero_ids_' . $hero_cat . '_' . ($is_bn ? 'bn' : 'en');
$hero_post_ids = get_transient($hero_cache_key);

if (false === $hero_post_ids) {
    $query_args = array(
        'posts_per_page'      => 4,
        'post_status'         => 'publish',
        'ignore_sticky_posts' => 1,
        'orderby'             => 'date',
        'order'               => 'DESC',
        'fields'              => 'ids',
        'no_found_rows'       => true,
    );

    if ($hero_cat > 0) {
        $query_args['cat'] = $hero_cat;
    }

    $hero_q = new WP_Query($query_args);
    $hero_post_ids = !empty($hero_q->posts) ? $hero_q->posts : array();
    set_transient($hero_cache_key, $hero_post_ids, 2 * HOUR_IN_SECONDS);
}

if (empty($hero_post_ids)) {
    return;
}

$hero_query = new WP_Query(array(
    'post__in'            => $hero_post_ids,
    'orderby'             => 'post__in',
    'posts_per_page'      => count($hero_post_ids),
    'ignore_sticky_posts' => 1,
    'no_found_rows'       => true,
));

if (!$hero_query->have_posts()) {
    return;
}

$lead_post = null;
$spotlights = array();

$count = 0;
while ($hero_query->have_posts()) {
    $hero_query->the_post();
    if ($count === 0) {
        $lead_post = get_post();
    } else {
        $spotlights[] = get_post();
    }
    $count++;
}
wp_reset_postdata();

if (!$lead_post) {
    return;
}
?>
<section class="n-lead" aria-label="<?php echo $is_bn ? esc_attr__('নির্বাচিত ও সর্বশেষ প্রবন্ধসমূহ', 'helptrickbd') : esc_attr__('Featured and Latest Articles', 'helptrickbd'); ?>">
  <!-- Main Lead Article (Left 65%) -->
  <article>
    <span class="n-kicker">
      <?php echo esc_html($badge_text); ?>
    </span>

    <h2 class="n-lead-title">
      <a href="<?php echo esc_url(get_permalink($lead_post->ID)); ?>">
        <?php echo esc_html(get_the_title($lead_post->ID)); ?>
      </a>
    </h2>

    <div class="n-byline">
      <span><?php echo esc_html(get_the_author_meta('display_name', $lead_post->post_author)); ?></span>
    </div>

    <?php if (has_post_thumbnail($lead_post->ID)) : ?>
      <figure>
        <?php
        echo get_the_post_thumbnail($lead_post->ID, 'ht-hero-large', array(
            'fetchpriority' => 'high',
            'decoding'      => 'async',
            'width'         => 800,
            'height'        => 450,
            'alt'           => esc_attr(get_the_title($lead_post->ID)),
        ));
        ?>
      </figure>
    <?php endif; ?>

    <div class="n-cols">
      <p><?php echo esc_html(get_the_excerpt($lead_post->ID)); ?></p>
    </div>
  </article>

  <!-- Side Spotlight Cards (Right 35%) -->
  <aside class="n-side">
    <?php foreach ($spotlights as $spot) : ?>
      <div class="n-side-card">
        <span class="sk">
          <?php
          $cats = get_the_category($spot->ID);
          if (!empty($cats)) {
              echo esc_html(function_exists('ht_get_localized_term_name') ? ht_get_localized_term_name($cats[0]) : $cats[0]->name);
          } else {
              echo $is_bn ? esc_html__('একাডেমিক', 'helptrickbd') : esc_html__('Academic', 'helptrickbd');
          }
          ?>
        </span>
        <h3>
          <a href="<?php echo esc_url(get_permalink($spot->ID)); ?>">
            <?php echo esc_html(get_the_title($spot->ID)); ?>
          </a>
        </h3>
        <p><?php echo esc_html(wp_trim_words(get_the_excerpt($spot->ID), 16, '...')); ?></p>
      </div>
    <?php endforeach; ?>
  </aside>
</section>