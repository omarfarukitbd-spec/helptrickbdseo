<?php
/**
 * Header Masthead Component (Single Refined Brand Wordmark & Institutional Tagline)
 *
 * @package HelpTrickBD_EduPortal
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
      <?php if (is_front_page() || is_home()) : ?>
        <h1 class="n-brand-wordmark">
          <a href="<?php echo $site_url; ?>"><?php echo $brand_html; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?></a>
        </h1>
      <?php else : ?>
        <div class="n-brand-wordmark">
          <a href="<?php echo $site_url; ?>"><?php echo $brand_html; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?></a>
        </div>
      <?php endif; ?>

      <p class="n-brand-tagline"><?php echo esc_html($site_desc); ?></p>
    </div>
  </div>
</header>
