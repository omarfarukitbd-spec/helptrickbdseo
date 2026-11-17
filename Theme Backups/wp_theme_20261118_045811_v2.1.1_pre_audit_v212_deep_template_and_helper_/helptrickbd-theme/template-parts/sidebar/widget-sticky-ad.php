<?php
/**
 * Sidebar Widget 2: Sticky Sidebar Google AdSlot
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

if (!get_theme_mod('ht_sidebar_ad_enable', true)) {
    return;
}
?>
<div class="n-sidebar-ad-widget" style="margin: 14px 0;">
  <?php
  if (function_exists('ht_render_ad')) {
      ht_render_ad('ht_ad_sticky_sidebar', 'ht-sidebar-ad-slot', 280);
  }
  ?>
</div>
