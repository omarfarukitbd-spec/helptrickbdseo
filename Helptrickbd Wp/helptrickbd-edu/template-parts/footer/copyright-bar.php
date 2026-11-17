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
    &copy; <?php echo esc_html(date('Y')); ?> <?php esc_html_e('HelpTrickBD.com — All rights reserved.', 'helptrickbd-edu'); ?>
    <span class="ht-copyright-tagline"><?php esc_html_e('• Academic Resources & Educational Portal', 'helptrickbd-edu'); ?></span>
  </div>

  <div class="ht-copyright-actions">
    <button type="button" id="ht-back-to-top" class="ht-back-btn" aria-label="<?php esc_attr_e('Back to Top', 'helptrickbd-edu'); ?>">
      <span><?php esc_html_e('Back to Top', 'helptrickbd-edu'); ?></span>
      <?php htbd_icon('chevron-right', array('class' => 'ht-arrow-up', 'width' => 14, 'height' => 14)); ?>
    </button>
  </div>
</div>
