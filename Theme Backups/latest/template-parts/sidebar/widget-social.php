<?php
/**
 * Sidebar Widget 3: Official Social Media & Community Channels
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

$fb_url = get_theme_mod('ht_facebook_url', 'https://facebook.com/helptrickbd');
$yt_url = get_theme_mod('ht_youtube_url', 'https://www.youtube.com/@helptrickbd');
$tg_url = get_theme_mod('ht_telegram_url', 'https://t.me/helptrickbd_official');
$wa_url = get_theme_mod('ht_whatsapp_url', 'https://whatsapp.com/channel/0029Vb956jgCHDyrx1wkUh2a');

if (empty($fb_url) && empty($yt_url) && empty($tg_url) && empty($wa_url)) {
    return;
}
?>
<div class="n-sidebar-social-widget" aria-label="<?php esc_attr_e('যুক্ত থাকুন', 'helptrickbd'); ?>">
  <div class="n-sec-head" style="margin-top:0;margin-bottom:10px;">
    <h3 style="font-size:1.15rem;"><?php esc_html_e('যুক্ত থাকুন', 'helptrickbd'); ?></h3>
    <span class="rule" aria-hidden="true"></span>
  </div>
  <div class="n-social-grid">
    <?php if (!empty($fb_url)) : ?>
      <a href="<?php echo esc_url($fb_url); ?>" target="_blank" rel="noopener noreferrer" class="n-soc-card n-soc-fb">
        <span class="n-soc-icon"><?php htbd_icon('facebook', array('width' => 18, 'height' => 18)); ?></span>
        <div class="n-soc-info">
          <span class="n-soc-name">Facebook</span>
          <span class="n-soc-sub"><?php esc_html_e('অফিসিয়াল পেজ', 'helptrickbd'); ?></span>
        </div>
        <span class="n-soc-btn"><?php esc_html_e('ফলো করুন', 'helptrickbd'); ?></span>
      </a>
    <?php endif; ?>

    <?php if (!empty($yt_url)) : ?>
      <a href="<?php echo esc_url($yt_url); ?>" target="_blank" rel="noopener noreferrer" class="n-soc-card n-soc-yt">
        <span class="n-soc-icon"><?php htbd_icon('youtube', array('width' => 18, 'height' => 18)); ?></span>
        <div class="n-soc-info">
          <span class="n-soc-name">YouTube</span>
          <span class="n-soc-sub"><?php esc_html_e('ভিডিও টিউটোরিয়াল', 'helptrickbd'); ?></span>
        </div>
        <span class="n-soc-btn"><?php esc_html_e('সাবস্ক্রাইব', 'helptrickbd'); ?></span>
      </a>
    <?php endif; ?>

    <?php if (!empty($tg_url)) : ?>
      <a href="<?php echo esc_url($tg_url); ?>" target="_blank" rel="noopener noreferrer" class="n-soc-card n-soc-tg">
        <span class="n-soc-icon"><?php htbd_icon('telegram', array('width' => 18, 'height' => 18)); ?></span>
        <div class="n-soc-info">
          <span class="n-soc-name">Telegram</span>
          <span class="n-soc-sub"><?php esc_html_e('স্টাডি চ্যানেল', 'helptrickbd'); ?></span>
        </div>
        <span class="n-soc-btn"><?php esc_html_e('যুক্ত হোন', 'helptrickbd'); ?></span>
      </a>
    <?php endif; ?>

    <?php if (!empty($wa_url)) : ?>
      <a href="<?php echo esc_url($wa_url); ?>" target="_blank" rel="noopener noreferrer" class="n-soc-card n-soc-wa">
        <span class="n-soc-icon"><?php htbd_icon('whatsapp', array('width' => 18, 'height' => 18)); ?></span>
        <div class="n-soc-info">
          <span class="n-soc-name">WhatsApp</span>
          <span class="n-soc-sub"><?php esc_html_e('পরীক্ষার আপডেট', 'helptrickbd'); ?></span>
        </div>
        <span class="n-soc-btn"><?php esc_html_e('যুক্ত হোন', 'helptrickbd'); ?></span>
      </a>
    <?php endif; ?>
  </div>
</div>
