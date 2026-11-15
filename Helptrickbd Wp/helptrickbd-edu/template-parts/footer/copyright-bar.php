<?php
/**
 * Footer Copyright & Disclaimer Bar Component
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}
?>
<div class="ht-copyright-bar">
  <div class="ht-copyright-text">
    &copy; <?php echo esc_html(htbd_bengali_number(date('Y'))); ?> <?php esc_html_e('হেল্পট্রিকবিডি। সর্বস্বত্ব সংরক্ষিত।', 'helptrickbd-edu'); ?>
    <span class="ht-copyright-tagline"><?php esc_html_e('• শিক্ষা ও তথ্যপ্রযুক্তি রিসোর্স পোর্টাল', 'helptrickbd-edu'); ?></span>
  </div>

  <div class="ht-copyright-actions">
    <button type="button" id="ht-back-to-top" class="ht-back-btn" aria-label="<?php esc_attr_e('উপরে ফিরে যান', 'helptrickbd-edu'); ?>">
      <span><?php esc_html_e('উপরে যান', 'helptrickbd-edu'); ?></span>
      <?php htbd_icon('chevron-right', array('class' => 'ht-arrow-up', 'width' => 14, 'height' => 14)); ?>
    </button>
  </div>
</div>
