<?php
/**
 * Master Homepage Controller (Slim Modular Architecture)
 * HelpTrickBD Pro - Newspaper & Educational Portal Hybrid
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
  ?>

  <?php
  $ad_slot_1 = get_theme_mod('htbd_ad_infeed_1', get_theme_mod('ht_ad_infeed_1', get_theme_mod('htbd_ad_infeed')));
  if (!empty($ad_slot_1)) :
  ?>
    <!-- In-Feed Ad Slot 1 -->
    <div class="htbd-ad-slot htbd-ad-infeed" style="min-height:250px;margin:24px 0;display:flex;justify-content:center;align-items:center;background:var(--ht-surface-alt);border:1px dashed var(--ht-border);border-radius:var(--ht-radius-sm);" aria-label="<?php esc_attr_e('বিজ্ঞাপন', 'helptrickbd'); ?>">
      <?php echo $ad_slot_1; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?>
    </div>
  <?php endif; ?>

  <?php
  // 3. 3-Column Specialized Subject Cards Grid (Strict SSC & Dakhil)
  get_template_part('template-parts/home/section-subject-grid');
  ?>

  <!-- 4. Subject-Based Filterable Posts & Newspaper Sidebar (Popular Posts & Categories) -->
  <div class="n-home-layout-grid">
    <div class="n-home-layout-main">
      <?php get_template_part('template-parts/home/section-filter-rows'); ?>
    </div>
    <aside class="n-home-layout-sidebar">
      <?php get_template_part('template-parts/home/sidebar-popular-cats'); ?>
    </aside>
  </div>

  <?php
  $ad_slot_2 = get_theme_mod('htbd_ad_infeed_2', get_theme_mod('ht_ad_infeed_2', get_theme_mod('htbd_ad_infeed')));
  if (!empty($ad_slot_2)) :
  ?>
    <!-- In-Feed Ad Slot 2 -->
    <div class="htbd-ad-slot htbd-ad-infeed" style="min-height:250px;margin:24px 0;display:flex;justify-content:center;align-items:center;background:var(--ht-surface-alt);border:1px dashed var(--ht-border);border-radius:var(--ht-radius-sm);" aria-label="<?php esc_attr_e('বিজ্ঞাপন', 'helptrickbd'); ?>">
      <?php echo $ad_slot_2; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?>
    </div>
  <?php endif; ?>

  <?php
  // 5. National University & Board Special Focus Desk (Clean Single Container)
  get_template_part('template-parts/home/section-special-focus');

  // 6. Infographic & Visual Study Photo Gallery (Full Titles, No Line Clamp)
  get_template_part('template-parts/home/section-photo-grid');

  // 7. Trust Deck
  get_template_part('template-parts/home/section-trust-deck');
  ?>
</div>

<?php
get_footer();
