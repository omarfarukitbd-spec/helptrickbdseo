<?php
/**
 * Header Topbar Component (Dateline, Font Resizer, Search Trigger, Theme Toggle)
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}
?>
<div class="n-dateline">
  <div class="ht-container">
    <div class="n-dateline-inner">
      <div class="n-dateline-left">
        <span class="n-date-text">
          <?php echo esc_html(htbd_bengali_today()); ?>
        </span>
      </div>

      <div class="n-dateline-right">
        <!-- Newspaper Font Resizer Bar -->
        <div class="n-fsbar" role="group" aria-label="<?php esc_attr_e('ফন্ট সাইজ পরিবর্তন', 'helptrickbd-edu'); ?>">
          <span><?php esc_html_e('হরফ:', 'helptrickbd-edu'); ?></span>
          <button type="button" class="n-fsbtn" data-scale="sm"><?php esc_html_e('ছোট', 'helptrickbd-edu'); ?></button>
          <button type="button" class="n-fsbtn active" data-scale="md"><?php esc_html_e('মাঝারি', 'helptrickbd-edu'); ?></button>
          <button type="button" class="n-fsbtn" data-scale="lg"><?php esc_html_e('বড়', 'helptrickbd-edu'); ?></button>
        </div>

        <!-- Spotlight Search Trigger -->
        <button type="button" class="ht-icon-btn ht-search-trigger" aria-label="<?php esc_attr_e('অনুসন্ধান করুন', 'helptrickbd-edu'); ?>" title="<?php esc_attr_e('অনুসন্ধান', 'helptrickbd-edu'); ?>">
          <?php htbd_icon('search', array('width' => 16, 'height' => 16)); ?>
        </button>

        <!-- Saved Bookmarks Drawer Trigger -->
        <button type="button" id="ht-bookmark-trigger" class="ht-icon-btn" aria-label="<?php esc_attr_e('সংরক্ষিত হ্যান্ডনোট', 'helptrickbd-edu'); ?>" title="<?php esc_attr_e('সংরক্ষিত হ্যান্ডনোট', 'helptrickbd-edu'); ?>" style="position:relative;">
          <?php htbd_icon('bookmark', array('width' => 16, 'height' => 16)); ?>
          <span id="ht-bookmark-badge" style="display:none;position:absolute;top:-4px;right:-4px;background:var(--ht-accent);color:#ffffff;font-size:0.65rem;font-weight:700;padding:1px 5px;border-radius:999px;line-height:1.2;">0</span>
        </button>

        <!-- Dark / Light Theme Toggle -->
        <button type="button" id="ht-theme-toggle" class="ht-icon-btn" aria-label="<?php esc_attr_e('ডার্ক ও লাইট মোড পরিবর্তন', 'helptrickbd-edu'); ?>">
          <?php htbd_icon('moon', array('width' => 16, 'height' => 16)); ?>
        </button>
      </div>
    </div>
  </div>
</div>
