<?php
/**
 * Single Article Author & Metadata Component
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}
?>
<div class="ht-single-meta">
  <div class="ht-author-box">
    <?php htbd_author_badge(); ?>
  </div>

  <div class="ht-date-read">
    <span class="ht-meta-item">
      <?php htbd_icon('calendar', array('width' => 14, 'height' => 14)); ?>
      <time datetime="<?php echo esc_attr(get_the_date(DATE_W3C)); ?>"><?php echo esc_html(get_the_date('j F, Y')); ?></time>
    </span>

    <span class="ht-meta-item">
      <?php htbd_icon('clock', array('width' => 14, 'height' => 14)); ?>
      <span><?php echo esc_html(htbd_reading_time()); ?></span>
    </span>
  </div>
</div>
