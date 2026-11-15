<?php
/**
 * Homepage Section 6: Special Focus Desk (Dot Header & Grid)
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}

$focus_query = new WP_Query(array(
    'posts_per_page'      => 6,
    'offset'              => 15,
    'post_status'         => 'publish',
    'ignore_sticky_posts' => 1,
    'no_found_rows'       => true,
));

if (!$focus_query->have_posts()) {
    // If not enough posts with offset, fallback without offset
    $focus_query = new WP_Query(array(
        'posts_per_page'      => 6,
        'post_status'         => 'publish',
        'ignore_sticky_posts' => 1,
        'no_found_rows'       => true,
    ));
}
?>
<section class="n-sec" aria-label="<?php esc_attr_e('জাতীয় বিশ্ববিদ্যালয় ও বোর্ড স্পেশাল ফোকাস ডেস্ক', 'helptrickbd-edu'); ?>">
  <div class="n-sec-head">
    <h3><?php esc_html_e('জাতীয় বিশ্ববিদ্যালয় ও বোর্ড স্পেশাল ফোকাস ডেস্ক', 'helptrickbd-edu'); ?></h3>
    <span class="rule" aria-hidden="true"></span>
    <a href="<?php echo esc_url(home_url('/category/national-university/')); ?>">
      <?php esc_html_e('সব হ্যান্ডনোট →', 'helptrickbd-edu'); ?>
    </a>
  </div>

  <div class="n-labelbox">
    <div class="n-label-head">
      <span class="n-label-title">
        <?php esc_html_e('ফোকাস ডেস্ক:', 'helptrickbd-edu'); ?> <b><?php esc_html_e('জাতীয় বিশ্ববিদ্যালয় ও বোর্ড', 'helptrickbd-edu'); ?></b>
      </span>
      <span class="n-label-dots" aria-hidden="true"></span>
      <svg class="n-label-ic" viewBox="0 0 27 21" fill="currentColor" aria-hidden="true">
        <circle cx="3" cy="3" r="2"/><circle cx="10" cy="3" r="2"/><circle cx="17" cy="3" r="2"/><circle cx="24" cy="3" r="2"/>
        <circle cx="3" cy="10.5" r="2"/><circle cx="10" cy="10.5" r="2"/><circle cx="17" cy="10.5" r="2"/><circle cx="24" cy="10.5" r="2"/>
        <circle cx="3" cy="18" r="2"/><circle cx="10" cy="18" r="2"/><circle cx="17" cy="18" r="2"/><circle cx="24" cy="18" r="2"/>
      </svg>
    </div>

    <p class="n-label-sub">
      <?php esc_html_e('নির্বাচিত বিভাগের সর্বশেষ হ্যান্ডনোট, সাজেশন ও পূর্ণাঙ্গ মডেল টেস্ট', 'helptrickbd-edu'); ?>
    </p>

    <div class="n-label-grid">
      <?php
      while ($focus_query->have_posts()) :
          $focus_query->the_post();
          ?>
          <a href="<?php the_permalink(); ?>" class="n-lrow">
            <?php if (has_post_thumbnail()) : ?>
              <?php
              the_post_thumbnail(array(54, 54), array(
                  'loading'  => 'lazy',
                  'decoding' => 'async',
                  'width'    => 54,
                  'height'   => 54,
                  'alt'      => esc_attr(get_the_title()),
              ));
              ?>
            <?php else : ?>
              <img src="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/Thumbnail%20BG/nu.webp" loading="lazy" decoding="async" width="54" height="54" alt="<?php the_title_attribute(); ?>">
            <?php endif; ?>

            <div class="n-lrow-text">
              <span class="lt-t"><?php the_title(); ?></span>
              <span class="lt-m"><?php echo esc_html(get_the_date('j F, Y')); ?></span>
            </div>
          </a>
          <?php
      endwhile;
      wp_reset_postdata();
      ?>
    </div>
  </div>
</section>
