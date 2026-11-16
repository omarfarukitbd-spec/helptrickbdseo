<?php
/**
 * Homepage Section 3: Magazine Lead Hero & Spotlight Deck
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}

if (!get_theme_mod('htbd_show_lead_hero', true)) {
    return;
}

$hero_cat   = (int) get_theme_mod('htbd_hero_category', 0);
$badge_text = get_theme_mod('htbd_hero_badge_text', 'নির্বাচিত হ্যান্ডনোট ও বিশেষ গাইড');

$query_args = array(
    'posts_per_page'      => 4,
    'post_status'         => 'publish',
    'ignore_sticky_posts' => 1,
    'no_found_rows'       => true,
);

if ($hero_cat > 0) {
    $query_args['cat'] = $hero_cat;
}

$hero_query = new WP_Query($query_args);

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
<section class="n-lead" aria-label="<?php esc_attr_e('প্রধান সংবাদ ও নির্বাচিত হ্যান্ডনোট', 'helptrickbd-edu'); ?>">
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
      <span><?php echo esc_html(get_the_date('j F, Y', $lead_post->ID)); ?></span>
      <span><?php echo esc_html(htbd_reading_time($lead_post->ID)); ?></span>
    </div>

    <?php if (has_post_thumbnail($lead_post->ID)) : ?>
      <figure>
        <?php
        echo get_the_post_thumbnail($lead_post->ID, 'ht-lead-banner', array(
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
          echo !empty($cats) ? esc_html($cats[0]->name) : esc_html__('একাডেমিক', 'helptrickbd-edu');
          ?>
        </span>
        <h4>
          <a href="<?php echo esc_url(get_permalink($spot->ID)); ?>">
            <?php echo esc_html(get_the_title($spot->ID)); ?>
          </a>
        </h4>
        <p><?php echo esc_html(wp_trim_words(get_the_excerpt($spot->ID), 16, '...')); ?></p>
      </div>
    <?php endforeach; ?>
  </aside>
</section>
