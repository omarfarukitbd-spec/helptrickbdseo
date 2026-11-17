<?php
/**
 * Master Sidebar Component (Micro-Modular Component Orchestrator)
 * Loads Widgets 1-4: Trending (1-6), Sticky Ad, Social Channels, and 2-Column Categories Grid.
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}
?>
<div class="n-home-sidebar-wrap">
  <?php
  // 1. Trending Most-Viewed Handnotes (Numbered List 1-6)
  get_template_part('template-parts/sidebar/widget-popular');

  // 2. Sticky Sidebar Google AdSlot
  get_template_part('template-parts/sidebar/widget-sticky-ad');

  // 3. Social Media & Community Channels
  get_template_part('template-parts/sidebar/widget-social');

  // 4. Categories & Departments (2-Column Grid)
  get_template_part('template-parts/sidebar/widget-categories');
  ?>
</div>
