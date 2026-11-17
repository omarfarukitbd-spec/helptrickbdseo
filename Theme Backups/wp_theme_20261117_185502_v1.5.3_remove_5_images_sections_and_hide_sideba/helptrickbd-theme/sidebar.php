<?php
/**
 * Academic Sidebar Component (Global Sidebar for Single, Archive & Page)
 * Exclusively renders the 3 Flagship Sections: Popular Posts (1-6), Social Channels, and Categories & Departments
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}
?>

<div id="secondary" class="ht-sidebar-wrapper">
  <?php get_template_part('template-parts/home/sidebar-popular-cats'); ?>

  <?php if (is_active_sidebar('ht-primary-sidebar')) : ?>
    <div class="ht-dynamic-sidebar-widgets" style="margin-top:20px;">
      <?php dynamic_sidebar('ht-primary-sidebar'); ?>
    </div>
  <?php endif; ?>
</div>
