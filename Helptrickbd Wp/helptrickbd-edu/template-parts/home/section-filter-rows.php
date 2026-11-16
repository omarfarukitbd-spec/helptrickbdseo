<?php
/**
 * Homepage Section 5: Filterable Live Thumb-Rows & Quick Revision Digest
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}

if (!get_theme_mod('htbd_show_sec_filter', true)) {
    return;
}

$sec_title  = get_theme_mod('htbd_sec_filter_title', 'দ্রুত রিভিশন ও বিষয়ভিত্তিক ডাইজেস্ট');
$post_count = (int) get_theme_mod('htbd_sec_filter_count', 12);
$link_text  = get_theme_mod('htbd_sec_filter_link_text', 'সব লেখা →');

$rows_query = new WP_Query(array(
    'posts_per_page'      => $post_count > 0 ? $post_count : 12,
    'post_status'         => 'publish',
    'ignore_sticky_posts' => 1,
    'no_found_rows'       => true,
));

if (!$rows_query->have_posts()) {
    return;
}
?>
<section class="n-sec" aria-label="<?php echo esc_attr($sec_title); ?>">
  <div class="n-sec-head">
    <h3><?php echo esc_html($sec_title); ?></h3>
    <span class="rule" aria-hidden="true"></span>
    <a href="<?php echo esc_url(home_url('/blog/')); ?>">
      <?php echo esc_html($link_text); ?>
    </a>
  </div>

  <!-- Interactive Filter Tabs (Top Ranked Helptrickbd Categories) -->
  <div class="n-thumb-tabs" role="group" aria-label="<?php esc_attr_e('বিষয় অনুযায়ী ফিল্টার', 'helptrickbd-edu'); ?>">
    <button type="button" class="n-thumb-tab-btn active" data-cat="all"><?php esc_html_e('সব বিষয়', 'helptrickbd-edu'); ?></button>
    <button type="button" class="n-thumb-tab-btn" data-cat="ssc-dakhil"><?php esc_html_e('এসএসসি ও দাখিল', 'helptrickbd-edu'); ?></button>
    <button type="button" class="n-thumb-tab-btn" data-cat="political-science"><?php esc_html_e('রাষ্ট্রবিজ্ঞান', 'helptrickbd-edu'); ?></button>
    <button type="button" class="n-thumb-tab-btn" data-cat="bangla-1st-paper"><?php esc_html_e('বাংলা ১ম পত্র', 'helptrickbd-edu'); ?></button>
    <button type="button" class="n-thumb-tab-btn" data-cat="islamic-article"><?php esc_html_e('ইসলামিক আর্টিকেল', 'helptrickbd-edu'); ?></button>
    <button type="button" class="n-thumb-tab-btn" data-cat="national-university"><?php esc_html_e('জাতীয় বিশ্ববিদ্যালয়', 'helptrickbd-edu'); ?></button>
    <button type="button" class="n-thumb-tab-btn" data-cat="ict-technology"><?php esc_html_e('আইসিটি ও প্রযুক্তি', 'helptrickbd-edu'); ?></button>
  </div>

  <!-- Rows List with 132x92 Thumbnails -->
  <div class="n-thumb-list">
    <?php
    while ($rows_query->have_posts()) :
        $rows_query->the_post();
        $cats = get_the_category();
        $cat_slugs = array();
        if (!empty($cats)) {
            foreach ($cats as $c) {
                $cat_slugs[] = $c->slug;
            }
        }
        $cat_classes = implode(' ', $cat_slugs);
        ?>
        <a href="<?php the_permalink(); ?>" class="n-trow" data-cats="<?php echo esc_attr($cat_classes); ?>">
          <div class="th">
            <?php if (has_post_thumbnail()) : ?>
              <?php
              the_post_thumbnail('ht-thumb-row', array(
                  'loading'  => 'lazy',
                  'decoding' => 'async',
                  'width'    => 132,
                  'height'   => 92,
                  'alt'      => esc_attr(get_the_title()),
              ));
              ?>
            <?php else : ?>
              <img src="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/Thumbnail%20BG/ssc.webp" loading="lazy" decoding="async" width="132" height="92" alt="<?php the_title_attribute(); ?>">
            <?php endif; ?>
          </div>

          <div class="info">
            <?php if (!empty($cats)) : ?>
              <span class="tag"><?php echo esc_html($cats[0]->name); ?></span>
            <?php endif; ?>
            <h4><?php the_title(); ?></h4>
            <div class="meta">
              <span><?php echo esc_html(get_the_date('j F, Y')); ?></span> &bull; 
              <span><?php echo esc_html(htbd_reading_time()); ?></span>
            </div>
          </div>

          <div class="arr" aria-hidden="true">&rarr;</div>
        </a>
        <?php
    endwhile;
    wp_reset_postdata();
    ?>
  </div>
</section>
