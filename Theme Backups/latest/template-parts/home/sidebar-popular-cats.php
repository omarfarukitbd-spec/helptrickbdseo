<?php
/**
 * Homepage & Global Sidebar Component: Most Popular Posts, Sticky Ad, Social & All Categories
 * Matches Flagship Style Numbered List (1-6), Sticky Sidebar Google AdSense Unit & 2-Column Categories Grid
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

$popular_enabled = get_theme_mod('ht_sidebar_popular_enable', true);
$popular_title   = get_theme_mod('ht_sidebar_popular_title', 'জনপ্রিয় ও আলোচিত হ্যান্ডনোট');
$popular_count   = (int) get_theme_mod('ht_sidebar_popular_count', 6);
if ($popular_count < 1) {
    $popular_count = 6;
}

// 1. Query Top Most-Viewed Posts with 6-Hour Transient Caching
$popular_post_ids = get_transient('ht_sidebar_pop_ids');

if (false === $popular_post_ids) {
    $pop_q = new WP_Query(array(
        'posts_per_page'      => $popular_count,
        'post_status'         => 'publish',
        'meta_key'            => 'ht_post_views_count',
        'orderby'             => 'meta_value_num date',
        'order'               => 'DESC',
        'ignore_sticky_posts' => 1,
        'fields'              => 'ids',
        'no_found_rows'       => true,
    ));

    // Fallback 1: htbd_post_views_count
    if (empty($pop_q->posts)) {
        $pop_q = new WP_Query(array(
            'posts_per_page'      => $popular_count,
            'post_status'         => 'publish',
            'meta_key'            => 'htbd_post_views_count',
            'orderby'             => 'meta_value_num date',
            'order'               => 'DESC',
            'ignore_sticky_posts' => 1,
            'fields'              => 'ids',
            'no_found_rows'       => true,
        ));
    }

    // Fallback 2: Comment count + date
    if (empty($pop_q->posts)) {
        $pop_q = new WP_Query(array(
            'posts_per_page'      => $popular_count,
            'post_status'         => 'publish',
            'orderby'             => 'comment_count date',
            'order'               => 'DESC',
            'ignore_sticky_posts' => 1,
            'fields'              => 'ids',
            'no_found_rows'       => true,
        ));
    }

    $popular_post_ids = !empty($pop_q->posts) ? $pop_q->posts : array();
    set_transient('ht_sidebar_pop_ids', $popular_post_ids, 6 * HOUR_IN_SECONDS);
}

$fb_url = get_theme_mod('ht_facebook_url', 'https://facebook.com/helptrickbd');
$yt_url = get_theme_mod('ht_youtube_url', 'https://www.youtube.com/@helptrickbd');
$tg_url = get_theme_mod('ht_telegram_url', 'https://t.me/helptrickbd_official');
$wa_url = get_theme_mod('ht_whatsapp_url', 'https://whatsapp.com/channel/0029Vb956jgCHDyrx1wkUh2a');
?>
<div class="n-home-sidebar-wrap">
  <?php if ($popular_enabled) : ?>
  <!-- Widget 1: Trending Handnotes (Numbered List 1-6) -->
  <div class="n-popular-widget" aria-label="<?php esc_attr_e('জনপ্রিয় হ্যান্ডনোট', 'helptrickbd'); ?>">
    <div class="n-pop-tab-header">
      <span class="n-pop-tab active"><?php echo esc_html($popular_title); ?></span>
    </div>

    <div class="n-pop-list">
      <?php
      if (!empty($popular_post_ids)) :
          $cached_popular_query = new WP_Query(array(
              'post__in'            => $popular_post_ids,
              'orderby'             => 'post__in',
              'posts_per_page'      => count($popular_post_ids),
              'ignore_sticky_posts' => 1,
              'no_found_rows'       => true,
          ));

          if ($cached_popular_query->have_posts()) :
              $rank = 1;
              while ($cached_popular_query->have_posts()) :
                  $cached_popular_query->the_post();
                  ?>
                  <a href="<?php the_permalink(); ?>" class="n-pop-item">
                    <span class="n-pop-num"><?php echo esc_html(function_exists('ht_bn_number') ? ht_bn_number($rank) : $rank); ?></span>
                    <span class="n-pop-title"><?php the_title(); ?></span>
                  </a>
                  <?php
                  $rank++;
              endwhile;
              wp_reset_postdata();
          endif;
      endif;
      ?>
    </div>
  </div>
  <?php endif; ?>

  <!-- Widget 2: Sticky Sidebar Google AdSlot (Restored for 100% Monetization Safety) -->
  <?php if (get_theme_mod('ht_sidebar_ad_enable', true)) : ?>
    <div class="n-sidebar-ad-widget" style="margin: 14px 0;">
      <?php
      if (function_exists('ht_render_ad')) {
          ht_render_ad('ht_ad_sticky_sidebar', 'ht-sidebar-ad-slot', 280);
      }
      ?>
    </div>
  <?php endif; ?>

  <!-- Widget 3: Social Media & Community Channels -->
  <div class="n-sidebar-social-widget" aria-label="<?php esc_attr_e('যুক্ত থাকুন', 'helptrickbd'); ?>">
    <div class="n-sec-head" style="margin-top:0;margin-bottom:10px;">
      <h3 style="font-size:1.15rem;"><?php esc_html_e('যুক্ত থাকুন', 'helptrickbd'); ?></h3>
      <span class="rule" aria-hidden="true"></span>
    </div>
    <div class="n-social-grid">
      <?php if (!empty($fb_url)) : ?>
        <a href="<?php echo esc_url($fb_url); ?>" target="_blank" rel="noopener noreferrer" class="n-soc-card n-soc-fb">
          <span class="n-soc-icon"><?php htbd_icon('facebook', array('width' => 18, 'height' => 18)); ?></span>
          <div class="n-soc-info">
            <span class="n-soc-name">Facebook</span>
            <span class="n-soc-sub"><?php esc_html_e('অফিসিয়াল পেজ', 'helptrickbd'); ?></span>
          </div>
          <span class="n-soc-btn"><?php esc_html_e('ফলো করুন', 'helptrickbd'); ?></span>
        </a>
      <?php endif; ?>

      <?php if (!empty($yt_url)) : ?>
        <a href="<?php echo esc_url($yt_url); ?>" target="_blank" rel="noopener noreferrer" class="n-soc-card n-soc-yt">
          <span class="n-soc-icon"><?php htbd_icon('youtube', array('width' => 18, 'height' => 18)); ?></span>
          <div class="n-soc-info">
            <span class="n-soc-name">YouTube</span>
            <span class="n-soc-sub"><?php esc_html_e('ভিডিও টিউটোরিয়াল', 'helptrickbd'); ?></span>
          </div>
          <span class="n-soc-btn"><?php esc_html_e('সাবস্ক্রাইব', 'helptrickbd'); ?></span>
        </a>
      <?php endif; ?>

      <?php if (!empty($tg_url)) : ?>
        <a href="<?php echo esc_url($tg_url); ?>" target="_blank" rel="noopener noreferrer" class="n-soc-card n-soc-tg">
          <span class="n-soc-icon"><?php htbd_icon('telegram', array('width' => 18, 'height' => 18)); ?></span>
          <div class="n-soc-info">
            <span class="n-soc-name">Telegram</span>
            <span class="n-soc-sub"><?php esc_html_e('স্টাডি চ্যানেল', 'helptrickbd'); ?></span>
          </div>
          <span class="n-soc-btn"><?php esc_html_e('যুক্ত হোন', 'helptrickbd'); ?></span>
        </a>
      <?php endif; ?>

      <?php if (!empty($wa_url)) : ?>
        <a href="<?php echo esc_url($wa_url); ?>" target="_blank" rel="noopener noreferrer" class="n-soc-card n-soc-wa">
          <span class="n-soc-icon"><?php htbd_icon('whatsapp', array('width' => 18, 'height' => 18)); ?></span>
          <div class="n-soc-info">
            <span class="n-soc-name">WhatsApp</span>
            <span class="n-soc-sub"><?php esc_html_e('পরীক্ষার আপডেট', 'helptrickbd'); ?></span>
          </div>
          <span class="n-soc-btn"><?php esc_html_e('যুক্ত হোন', 'helptrickbd'); ?></span>
        </a>
      <?php endif; ?>
    </div>
  </div>

  <!-- Widget 4: Categories & Departments (2-Column Category Cards Grid) -->
  <?php if (get_theme_mod('ht_sidebar_cats_enable', true)) : ?>
  <div class="n-sidebar-cats-widget" aria-label="<?php esc_attr_e('সকল বিষয় ও বিভাগ', 'helptrickbd'); ?>" style="margin-top:16px;">
    <div class="n-sec-head" style="margin-top:0;margin-bottom:10px;">
      <h3 style="font-size:1.15rem;"><?php esc_html_e('সকল বিষয় ও বিভাগ', 'helptrickbd'); ?></h3>
      <span class="rule" aria-hidden="true"></span>
    </div>

    <div class="n-cats-grid-2col">
      <?php
      $sidebar_cats = get_categories(array(
          'orderby'    => 'count',
          'order'      => 'DESC',
          'hide_empty' => true,
      ));
      if (!empty($sidebar_cats)) :
          foreach ($sidebar_cats as $cat) :
              if ($cat->slug === 'uncategorized' || (int) $cat->count === 0) {
                  continue;
              }
              ?>
              <a href="<?php echo esc_url(get_category_link($cat->term_id)); ?>" class="n-cat-card">
                <span class="n-cat-name"><?php echo esc_html($cat->name); ?></span>
                <span class="n-cat-count"><?php echo esc_html(function_exists('ht_bn_number') ? ht_bn_number($cat->count) : $cat->count); ?></span>
              </a>
              <?php
          endforeach;
      endif;
      ?>
    </div>
  </div>
  <?php endif; ?>
</div>