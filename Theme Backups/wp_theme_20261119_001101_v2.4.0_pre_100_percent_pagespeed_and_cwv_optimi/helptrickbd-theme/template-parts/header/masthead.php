<?php
/**
 * Header Masthead Component (Single Refined Brand Wordmark & Institutional Tagline)
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

$site_url  = esc_url(home_url('/'));
$site_name = get_bloginfo('name', 'display');
if (empty($site_name) || $site_name === 'WordPress') {
    $site_name = 'HelpTrickBD';
}
$site_desc = get_bloginfo('description', 'display');
if (empty($site_desc)) {
    $site_desc = 'The Future of Online Education';
}

// Brand display: clean unified "HelpTrickBD.com" wordmark
$display_brand = $site_name;
if (stripos($display_brand, '.com') === false) {
    $brand_html = esc_html($display_brand) . '<span class="n-brand-tld">.com</span>';
} else {
    $brand_html = esc_html($display_brand);
}
?>
<header class="n-masthead">
  <div class="ht-container">
    <div class="n-masthead-inner">
      <div class="n-brand-left">
        <?php if (is_front_page() || is_home()) : ?>
          <h1 class="n-brand-wordmark">
            <a href="<?php echo $site_url; ?>"><?php echo $brand_html; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?></a>
          </h1>
        <?php else : ?>
          <div class="n-brand-wordmark">
            <a href="<?php echo $site_url; ?>"><?php echo $brand_html; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?></a>
          </div>
        <?php endif; ?>
      </div>

      <div class="n-brand-right">
        <?php get_template_part('template-parts/header/language-switcher'); ?>
        <?php if (get_theme_mod('ht_header_theme_toggle_enable', true)) : ?>
          <button type="button" class="n-masthead-theme-btn ht-theme-toggle" id="ht-theme-toggle" aria-label="<?php echo (function_exists('ht_is_bangla_locale') && !ht_is_bangla_locale()) ? esc_attr__('Toggle Dark/Light Mode', 'helptrickbd') : esc_attr__('ডার্ক ও লাইট মোড পরিবর্তন করুন', 'helptrickbd'); ?>" title="<?php echo (function_exists('ht_is_bangla_locale') && !ht_is_bangla_locale()) ? esc_attr__('Toggle Dark/Light Mode', 'helptrickbd') : esc_attr__('ডার্ক ও লাইট মোড পরিবর্তন করুন', 'helptrickbd'); ?>">
            <span class="ht-theme-icon-sun" aria-hidden="true"><?php htbd_icon('sun', array('width' => 19, 'height' => 19)); ?></span>
            <span class="ht-theme-icon-moon" aria-hidden="true"><?php htbd_icon('moon', array('width' => 19, 'height' => 19)); ?></span>
          </button>
        <?php endif; ?>
        <button type="button" class="n-masthead-search-btn ht-search-trigger" id="ht-search-trigger" aria-label="<?php echo (function_exists('ht_is_bangla_locale') && !ht_is_bangla_locale()) ? esc_attr__('Search', 'helptrickbd') : esc_attr__('অনুসন্ধান', 'helptrickbd'); ?>">
          <?php htbd_icon('search', array('width' => 20, 'height' => 20)); ?>
        </button>
      </div>
    </div>
  </div>
</header>
