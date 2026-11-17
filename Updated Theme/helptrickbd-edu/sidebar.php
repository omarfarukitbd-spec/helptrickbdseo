<?php
/**
 * Academic Sidebar Component (Global Sidebar for Single & Archive Pages)
 * Matches Home Sidebar with Trending, Social rows, and 2-column Categories
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}
?>

<div id="secondary" class="ht-sidebar-area" aria-label="<?php esc_attr_e('Sidebar', 'helptrickbd-edu'); ?>">
  <?php if (is_active_sidebar('sidebar-main')) : ?>
    <?php dynamic_sidebar('sidebar-main'); ?>
  <?php else : ?>
    <?php get_template_part('template-parts/home/sidebar-popular-cats'); ?>
  <?php endif; ?>
</div>
