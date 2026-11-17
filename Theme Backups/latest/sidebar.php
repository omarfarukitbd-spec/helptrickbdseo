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

<aside id="secondary" class="ht-sidebar-area ht-sidebar-wrapper" aria-label="<?php esc_attr_e('সাইডবার', 'helptrickbd'); ?>">
  <?php get_template_part('template-parts/home/sidebar-popular-cats'); ?>
</aside>
