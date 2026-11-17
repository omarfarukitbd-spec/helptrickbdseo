<?php
/**
 * Academic Sidebar Component (Global Sidebar for Single & Archive Pages)
 * Exclusively renders the 3 Flagship Sections: Popular Posts, Social Channels, and Categories & Departments
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}
?>

<div id="secondary" class="ht-sidebar-area" aria-label="<?php esc_attr_e('Sidebar', 'helptrickbd-edu'); ?>">
  <?php get_template_part('template-parts/home/sidebar-popular-cats'); ?>
</div>
