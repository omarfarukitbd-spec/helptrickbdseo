<?php
/**
 * Homepage Sidebar Component: Most Popular Posts & All Categories 2-Column Grid
 * Matches Prothom-alo style numbered list (১-৬) and 2-column categories grid
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}

// 1. Query Top 6 Most-Viewed / Ranked Posts (Google Analytics & Traffic Leaderboard)
$popular_query = new WP_Query(array(
    'posts_per_page'      => 6,
    'post_status'         => 'publish',
    'meta_key'            => 'ht_post_views_count',
    'orderby'             => 'meta_value_num date',
    'order'               => 'DESC',
    'ignore_sticky_posts' => 1,
    'no_found_rows'       => true,
));

// Fallback to htbd_post_views_count or comment count if legacy views not yet populated
if (!$popular_query->have_posts()) {
    $popular_query = new WP_Query(array(
        'posts_per_page'      => 6,
        'post_status'         => 'publish',
        'meta_key'            => 'htbd_post_views_count',
        'orderby'             => 'meta_value_num date',
        'order'               => 'DESC',
        'ignore_sticky_posts' => 1,
        'no_found_rows'       => true,
    ));
}

if (!$popular_query->have_posts()) {
    $popular_query = new WP_Query(array(
        'posts_per_page'      => 6,
        'post_status'         => 'publish',
        'orderby'             => 'comment_count date',
        'order'               => 'DESC',
        'ignore_sticky_posts' => 1,
        'no_found_rows'       => true,
    ));
}

// 2. Fetch All Valid Categories
$all_cats = get_categories(array(
    'orderby'    => 'count',
    'order'      => 'DESC',
    'hide_empty' => false,
));
?>
<div class="n-home-sidebar-wrap">
  <!-- Widget 1: সর্বাধিক পঠিত (Prothom-alo Style Underline Tab & Numbers ১-৬) -->
  <div class="n-popular-widget" aria-label="<?php esc_attr_e('সর্বাধিক পঠিত', 'helptrickbd-edu'); ?>">
    <div class="n-pop-tab-header">
      <span class="n-pop-tab active"><?php esc_html_e('সর্বাধিক পঠিত', 'helptrickbd-edu'); ?></span>
    </div>

    <div class="n-pop-list">
      <?php
      if ($popular_query->have_posts()) :
          $rank = 1;
          while ($popular_query->have_posts()) :
              $popular_query->the_post();
              ?>
              <a href="<?php the_permalink(); ?>" class="n-pop-item">
                <span class="n-pop-num"><?php echo esc_html(htbd_bengali_number($rank)); ?></span>
                <span class="n-pop-title"><?php the_title(); ?></span>
              </a>
              <?php
              $rank++;
          endwhile;
          wp_reset_postdata();
      endif;
      ?>
    </div>
  </div>

  <!-- Widget 2: সোশ্যাল মিডিয়া ও কমিউনিটি (Facebook, YouTube, Telegram, WhatsApp) -->
  <div class="n-sidebar-social-widget" aria-label="<?php esc_attr_e('যুক্ত থাকুন', 'helptrickbd-edu'); ?>">
    <div class="n-sec-head" style="margin-top:0;margin-bottom:10px;">
      <h3 style="font-size:1.15rem;"><?php esc_html_e('যুক্ত থাকুন', 'helptrickbd-edu'); ?></h3>
      <span class="rule" aria-hidden="true"></span>
    </div>
    <div class="n-social-grid">
      <a href="https://facebook.com/helptrickbd" target="_blank" rel="noopener noreferrer" class="n-soc-card n-soc-fb">
        <span class="n-soc-icon"><?php htbd_icon('facebook', array('width' => 18, 'height' => 18)); ?></span>
        <div class="n-soc-info">
          <span class="n-soc-name">Facebook</span>
          <span class="n-soc-sub">অফিসিয়াল পেজ</span>
        </div>
        <span class="n-soc-btn">ফলো</span>
      </a>
      <a href="https://www.youtube.com/@helptrickbd" target="_blank" rel="noopener noreferrer" class="n-soc-card n-soc-yt">
        <span class="n-soc-icon"><?php htbd_icon('youtube', array('width' => 18, 'height' => 18)); ?></span>
        <div class="n-soc-info">
          <span class="n-soc-name">YouTube</span>
          <span class="n-soc-sub">ভিডিও লেকচার</span>
        </div>
        <span class="n-soc-btn">সাবস্ক্রাইব</span>
      </a>
      <a href="https://t.me/helptrickbd_official" target="_blank" rel="noopener noreferrer" class="n-soc-card n-soc-tg">
        <span class="n-soc-icon"><?php htbd_icon('telegram', array('width' => 18, 'height' => 18)); ?></span>
        <div class="n-soc-info">
          <span class="n-soc-name">Telegram</span>
          <span class="n-soc-sub">নোটিশ ও সাজেশন</span>
        </div>
        <span class="n-soc-btn">যুক্ত হন</span>
      </a>
      <a href="https://whatsapp.com/channel/0029Vb956jgCHDyrx1wkUh2a" target="_blank" rel="noopener noreferrer" class="n-soc-card n-soc-wa">
        <span class="n-soc-icon"><?php htbd_icon('whatsapp', array('width' => 18, 'height' => 18)); ?></span>
        <div class="n-soc-info">
          <span class="n-soc-name">WhatsApp</span>
          <span class="n-soc-sub">স্টাডি চ্যানেল</span>
        </div>
        <span class="n-soc-btn">যুক্ত হন</span>
      </a>
    </div>
  </div>

  <!-- Widget 3: সকল বিষয় ও বিভাগ (2-Column Category Cards Grid) -->
  <div class="n-sidebar-cats-widget" aria-label="<?php esc_attr_e('সকল বিষয় ও বিভাগ', 'helptrickbd-edu'); ?>">
    <div class="n-sec-head" style="margin-top:0;margin-bottom:10px;">
      <h3 style="font-size:1.15rem;"><?php esc_html_e('সকল বিষয় ও বিভাগ', 'helptrickbd-edu'); ?></h3>
      <span class="rule" aria-hidden="true"></span>
    </div>

    <div class="n-cats-grid-2col">
      <?php
      if (!empty($all_cats)) :
          foreach ($all_cats as $cat) :
              if ($cat->slug === 'uncategorized' || (int) $cat->count === 0) {
                  continue;
              }
              ?>
              <a href="<?php echo esc_url(get_category_link($cat->term_id)); ?>" class="n-cat-card">
                <span class="n-cat-name"><?php echo esc_html($cat->name); ?></span>
                <span class="n-cat-count"><?php echo esc_html(htbd_bengali_number($cat->count)); ?></span>
              </a>
              <?php
          endforeach;
      endif;
      ?>
    </div>
  </div>
</div>
