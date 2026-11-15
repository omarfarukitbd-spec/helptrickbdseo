<?php
/**
 * Homepage Section 7: Infographic & Visual Study Photo Gallery
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}

$photo_query = new WP_Query(array(
    'posts_per_page'      => 4,
    'offset'              => 21,
    'post_status'         => 'publish',
    'ignore_sticky_posts' => 1,
    'no_found_rows'       => true,
));

if (!$photo_query->have_posts()) {
    $photo_query = new WP_Query(array(
        'posts_per_page'      => 4,
        'post_status'         => 'publish',
        'ignore_sticky_posts' => 1,
        'no_found_rows'       => true,
    ));
}
?>
<section class="n-sec" aria-label="<?php esc_attr_e('ইনফোগ্রাফিক ও ভিজ্যুয়াল স্টাডি গ্যালারি', 'helptrickbd-edu'); ?>">
  <div class="n-sec-head">
    <h3><?php esc_html_e('ইনফোগ্রাফিক ও ভিজ্যুয়াল স্টাডি গ্যালারি', 'helptrickbd-edu'); ?></h3>
    <span class="rule" aria-hidden="true"></span>
    <a href="<?php echo esc_url(home_url('/blog/')); ?>">
      <?php esc_html_e('সকল গ্যালারি →', 'helptrickbd-edu'); ?>
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
