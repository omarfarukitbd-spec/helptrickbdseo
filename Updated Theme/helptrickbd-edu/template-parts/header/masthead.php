<?php
/**
 * Header Masthead Component (Grand Serif Wordmark & Institutional Tagline)
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}

$site_url  = esc_url(home_url('/'));
$site_name = get_bloginfo('name', 'display');
if (empty($site_name) || $site_name === 'WordPress') {
    $site_name = 'হেল্পট্রিকবিডি';
}
$site_desc = get_bloginfo('description', 'display');
if (empty($site_desc)) {
    $site_desc = 'সহজ ভাষায় লেখা শিক্ষামূলক কনটেন্ট ও একাডেমিক হ্যান্ডনোট';
}
?>
<header class="n-masthead">
  <div class="ht-container">
    <div class="n-masthead-inner">
      <?php if (is_front_page() || is_home()) : ?>
        <h1 class="n-brand-wordmark">
          <a href="<?php echo $site_url; ?>"><?php echo esc_html($site_name); ?></a>
        </h1>
      <?php else : ?>
        <div class="n-brand-wordmark">
          <a href="<?php echo $site_url; ?>"><?php echo esc_html($site_name); ?></a>
        </div>
      <?php endif; ?>

      <div class="n-brand-subdomain">HELPTRICKBD.COM</div>
      <p class="n-brand-tagline"><?php echo esc_html($site_desc); ?></p>
    </div>
  </div>
</header>
