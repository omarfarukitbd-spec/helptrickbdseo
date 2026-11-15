<?php
/**
 * Fullscreen Search Modal Component
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}
?>
<div id="ht-search-modal" class="ht-search-modal" role="dialog" aria-modal="true" aria-label="<?php esc_attr_e('অনুসন্ধান', 'helptrickbd-edu'); ?>">
  <div class="ht-search-backdrop ht-search-trigger"></div>
  <div class="ht-search-dialog">
    <div class="ht-search-header">
      <h3 class="ht-search-title"><?php esc_html_e('হ্যান্ডনোট ও সাজেশন অনুসন্ধান', 'helptrickbd-edu'); ?></h3>
      <button type="button" id="ht-search-close" class="ht-icon-btn" aria-label="<?php esc_attr_e('বন্ধ করুন', 'helptrickbd-edu'); ?>">
        <?php htbd_icon('close', array('width' => 20, 'height' => 20)); ?>
      </button>
    </div>

    <form role="search" method="get" class="ht-search-form" action="<?php echo esc_url(home_url('/')); ?>">
      <div class="ht-search-input-wrap">
        <?php htbd_icon('search', array('class' => 'ht-search-field-icon', 'width' => 20, 'height' => 20)); ?>
        <input type="search" id="ht-search-input" class="ht-search-field" placeholder="<?php esc_attr_e('টপিক, বিষয় বা প্রশ্ন খুঁজুন... (যেমন: রাষ্ট্রবিজ্ঞান, এসএসসি)', 'helptrickbd-edu'); ?>" value="<?php echo get_search_query(); ?>" name="s" autocomplete="off">
        <button type="submit" class="ht-btn ht-btn-primary"><?php esc_html_e('খুঁজুন', 'helptrickbd-edu'); ?></button>
      </div>
    </form>

    <div class="ht-search-hints">
      <span><?php esc_html_e('জনপ্রিয় অনুসন্ধান:', 'helptrickbd-edu'); ?></span>
      <a href="<?php echo esc_url(home_url('/?s=রাষ্ট্রবিজ্ঞান')); ?>">রাষ্ট্রবিজ্ঞান</a>
      <a href="<?php echo esc_url(home_url('/?s=এসএসসি+সাজেশন')); ?>">এসএসসি সাজেশন</a>
      <a href="<?php echo esc_url(home_url('/?s=ডিগ্রি+রুটিন')); ?>">ডিগ্রি রুটিন</a>
      <a href="<?php echo esc_url(home_url('/?s=ইংলিশ+গ্রামার')); ?>">ইংলিশ গ্রামার</a>
    </div>
  </div>
</div>
