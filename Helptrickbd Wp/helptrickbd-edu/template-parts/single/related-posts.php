<?php
/**
 * Single Article Related Posts Component
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}

$current_id = get_the_ID();
$categories = get_the_category($current_id);

if (empty($categories)) {
    return;
}

$related_query = new WP_Query(array(
    'category__in'        => array($categories[0]->term_id),
    'post__not_in'        => array($current_id),
    'posts_per_page'      => 3,
    'ignore_sticky_posts' => 1,
    'no_found_rows'       => true,
));

if (!$related_query->have_posts()) {
    return;
}
?>
<section class="ht-related-section" aria-label="<?php esc_attr_e('Related Handnotes & Suggestions', 'helptrickbd-edu'); ?>">
  <div class="n-sec-head">
    <h3><?php esc_html_e('Related Handnotes & Suggestions', 'helptrickbd-edu'); ?></h3>
    <span class="rule" aria-hidden="true"></span>
  </div>

  <div class="ht-grid-3">
    <?php
    while ($related_query->have_posts()) :
        $related_query->the_post();
        ?>
        <article class="ht-related-card">
          <a href="<?php the_permalink(); ?>" class="ht-related-thumb">
            <?php if (has_post_thumbnail()) : ?>
              <?php
              the_post_thumbnail('ht-card-banner', array(
                  'loading'  => 'lazy',
                  'decoding' => 'async',
                  'width'    => 400,
                  'height'   => 225,
                  'alt'      => esc_attr(get_the_title()),
              ));
              ?>
            <?php else : ?>
              <img src="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/Thumbnail%20BG/nu.webp" loading="lazy" decoding="async" width="400" height="225" alt="<?php the_title_attribute(); ?>">
            <?php endif; ?>
          </a>
          <h4>
            <a href="<?php the_permalink(); ?>">
              <?php the_title(); ?>
            </a>
          </h4>
          <div class="meta">
            <span><?php echo esc_html(get_the_date('j F, Y')); ?></span> &bull; 
            <span><?php echo esc_html(htbd_reading_time()); ?></span>
          </div>
        </article>
        <?php
    endwhile;
    wp_reset_postdata();
    ?>
  </div>
</section>
