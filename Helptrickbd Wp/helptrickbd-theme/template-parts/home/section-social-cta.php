<?php
/**
 * Homepage Section 2: Telegram & WhatsApp Join Community CTA Bar
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

if (!get_theme_mod('htbd_show_social_cta', get_theme_mod('ht_show_social_cta', true))) {
    return;
}

$telegram_url = get_theme_mod('htbd_telegram_url', get_theme_mod('ht_telegram_url', 'https://t.me/helptrickbd_official'));
$whatsapp_url = get_theme_mod('htbd_whatsapp_url', get_theme_mod('ht_whatsapp_url', 'https://whatsapp.com/channel/0029Vb956jgCHDyrx1wkUh2a'));
?>
<section class="n-social-cta" aria-label="<?php esc_attr_e('সোশ্যাল কমিউনিটি চ্যানেল', 'helptrickbd'); ?>">
  <div class="n-social-cta-text">
    <h4><?php esc_html_e('সবার আগে পরীক্ষার রুটিন ও স্পেশাল সাজেশন পেতে চান?', 'helptrickbd'); ?></h4>
    <p><?php esc_html_e('আমাদের অফিসিয়াল হোয়াটসঅ্যাপ ও টেলিগ্রাম স্টাডি চ্যানেলে যুক্ত হোন।', 'helptrickbd'); ?></p>
  </div>

  <div class="n-social-cta-btns">
    <a href="<?php echo esc_url($whatsapp_url); ?>" target="_blank" rel="noopener noreferrer" class="ht-btn ht-btn-whatsapp">
      <?php htbd_icon('whatsapp', array('width' => 18, 'height' => 18)); ?>
      <span><?php esc_html_e('হোয়াটসঅ্যাপ চ্যানেল', 'helptrickbd'); ?></span>
    </a>
    <a href="<?php echo esc_url($telegram_url); ?>" target="_blank" rel="noopener noreferrer" class="ht-btn ht-btn-telegram">
      <?php htbd_icon('telegram', array('width' => 18, 'height' => 18)); ?>
      <span><?php esc_html_e('টেলিগ্রাম চ্যানেল', 'helptrickbd'); ?></span>
    </a>
  </div>
</section>