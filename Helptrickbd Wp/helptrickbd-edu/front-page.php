<?php
/**
 * Master Homepage Controller (Slim Modular Architecture)
 * HelpTrickBD EduPortal - Newspaper & Educational Portal Hybrid
 *
 * @package HelpTrickBD_EduPortal
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

  <!-- In-Feed Ad Slot 1 -->
  <div class="htbd-ad-slot htbd-ad-infeed" aria-label="<?php esc_attr_e('বিজ্ঞাপন', 'helptrickbd-edu'); ?>">
    <?php
    $ad_slot_1 = get_theme_mod('htbd_ad_infeed_1', get_theme_mod('htbd_ad_infeed'));
    if ($ad_slot_1) {
        echo $ad_slot_1; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped
    }
    ?>
  </div>

  <?php
  // 3. 3-Column Specialized Subject Cards Grid
  get_template_part('template-parts/home/section-subject-grid');

  // 4. Interactive Filterable Thumb-Rows & Quick Revision Digest
  get_template_part('template-parts/home/section-filter-rows');
  ?>

  <!-- In-Feed Ad Slot 2 -->
  <div class="htbd-ad-slot htbd-ad-infeed" aria-label="<?php esc_attr_e('বিজ্ঞাপন', 'helptrickbd-edu'); ?>">
    <?php
    $ad_slot_2 = get_theme_mod('htbd_ad_infeed_2', get_theme_mod('htbd_ad_infeed'));
    if ($ad_slot_2) {
        echo $ad_slot_2; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped
    }
    ?>
  </div>

  <?php
  // 5. National University & Board Special Focus Desk (Dot Header)
  get_template_part('template-parts/home/section-special-focus');

  // 6. Infographic & Visual Study Photo Gallery (4-Column)
  get_template_part('template-parts/home/section-photo-grid');

  // 7. Institutional Trust Deck, Popular Posts & Exam Schedule
  get_template_part('template-parts/home/section-trust-deck');
  ?>
</div>

<?php
get_footer();
