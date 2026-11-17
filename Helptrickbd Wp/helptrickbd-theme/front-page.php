<?php
/**
 * Master Homepage Controller (Slim Modular Architecture)
 * HelpTrickBD Pro - Newspaper & Educational Portal Hybrid
 * Strictly follows the final version of helptrickbd-edu layout:
 * 1. Breaking Notice Marquee Ticker
 * 2. Magazine Lead Hero Story & Spotlight Cards
 * 3. 3-Column Specialized Subject Cards Grid (Strict SSC & Dakhil)
 * 4. Main 2-Column Home Layout Grid:
 *    - Left: Subject-Based Filterable Posts (2 columns)
 *    - Right: Academic Sidebar (Trending 1-6, Stay Connected, Categories Grid)
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

get_header();
?>

<div class="ht-container">
  <?php
  // 1. Breaking Notice Marquee Ticker
  get_template_part('template-parts/home/section-ticker');

  // 2. Magazine Lead Hero Story & Spotlight Cards
  get_template_part('template-parts/home/section-lead-hero');

  // 3. 3-Column Specialized Subject Cards Grid (Strict SSC & Dakhil)
  get_template_part('template-parts/home/section-subject-grid');
  ?>

  <!-- 4. Subject-Based Filterable Posts & Academic Sidebar -->
  <div class="n-home-layout-grid">
    <div class="n-home-layout-main">
      <?php get_template_part('template-parts/home/section-filter-rows'); ?>
    </div>
    <aside class="n-home-layout-sidebar">
      <?php get_template_part('template-parts/home/sidebar-popular-cats'); ?>
    </aside>
  </div>
</div>

<?php
get_footer();
