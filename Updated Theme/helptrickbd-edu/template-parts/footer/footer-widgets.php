<?php
/**
 * Footer 4-Column Academic Widgets Component
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}
?>
<div class="ht-footer-widgets">
  <!-- Col 1: About Helptrickbd -->
  <div class="ht-footer-col">
    <h3 class="ht-footer-title"><?php esc_html_e('About HelpTrickBD', 'helptrickbd-edu'); ?></h3>
    <p>
      <?php esc_html_e('HelpTrickBD is an academic resource and educational portal in Bangladesh dedicated to university guidelines, board exam handnotes, and syllabus solutions.', 'helptrickbd-edu'); ?>
    </p>
    <p class="ht-footer-contact">
      <strong><?php esc_html_e('Email:', 'helptrickbd-edu'); ?></strong> 
      <a href="mailto:contact@helptrickbd.com">contact@helptrickbd.com</a>
    </p>
  </div>

  <!-- Col 2: Academic Shortcuts -->
  <div class="ht-footer-col">
    <h3 class="ht-footer-title"><?php esc_html_e('Academic Handnotes', 'helptrickbd-edu'); ?></h3>
    <ul class="ht-footer-links">
      <li><a href="<?php echo esc_url(home_url('/category/national-university/')); ?>"><?php esc_html_e('National University', 'helptrickbd-edu'); ?></a></li>
      <li><a href="<?php echo esc_url(home_url('/category/ssc-dakhil/')); ?>"><?php esc_html_e('SSC & Dakhil Examination', 'helptrickbd-edu'); ?></a></li>
      <li><a href="<?php echo esc_url(home_url('/category/political-science/')); ?>"><?php esc_html_e('Political Science Handnotes', 'helptrickbd-edu'); ?></a></li>
      <li><a href="<?php echo esc_url(home_url('/category/english-2nd-paper/')); ?>"><?php esc_html_e('English 2nd Paper & Grammar', 'helptrickbd-edu'); ?></a></li>
      <li><a href="<?php echo esc_url(home_url('/nu-cgpa-calculator/')); ?>"><?php esc_html_e('NU CGPA Calculator', 'helptrickbd-edu'); ?></a></li>
    </ul>
  </div>

  <!-- Col 3: Institutional Links -->
  <div class="ht-footer-col">
    <h3 class="ht-footer-title"><?php esc_html_e('Institutional Policies', 'helptrickbd-edu'); ?></h3>
    <ul class="ht-footer-links">
      <li><a href="<?php echo esc_url(home_url('/about-us/')); ?>"><?php esc_html_e('About Us', 'helptrickbd-edu'); ?></a></li>
      <li><a href="<?php echo esc_url(home_url('/contact-us/')); ?>"><?php esc_html_e('Contact Us', 'helptrickbd-edu'); ?></a></li>
      <li><a href="<?php echo esc_url(home_url('/privacy-policy/')); ?>"><?php esc_html_e('Privacy Policy', 'helptrickbd-edu'); ?></a></li>
      <li><a href="<?php echo esc_url(home_url('/terms-conditions/')); ?>"><?php esc_html_e('Terms & Conditions', 'helptrickbd-edu'); ?></a></li>
      <li><a href="<?php echo esc_url(home_url('/disclaimer/')); ?>"><?php esc_html_e('Disclaimer', 'helptrickbd-edu'); ?></a></li>
      <li><a href="<?php echo esc_url(home_url('/cookie-policy/')); ?>"><?php esc_html_e('Cookie Policy', 'helptrickbd-edu'); ?></a></li>
      <li><a href="<?php echo esc_url(home_url('/sitemap/')); ?>"><?php esc_html_e('Sitemap', 'helptrickbd-edu'); ?></a></li>
    </ul>
  </div>

  <!-- Col 4: Community & Official Channels -->
  <div class="ht-footer-col">
    <h3 class="ht-footer-title"><?php esc_html_e('Join Our Study Channels', 'helptrickbd-edu'); ?></h3>
    <p><?php esc_html_e('Stay updated with exam routines, urgent board notices, and curated academic suggestions:', 'helptrickbd-edu'); ?></p>
    <div class="ht-footer-social-btns">
      <a href="https://t.me/helptrickbd_official" target="_blank" rel="noopener noreferrer" class="ht-btn ht-btn-telegram">
        <?php htbd_icon('telegram', array('width' => 16, 'height' => 16)); ?>
        <span><?php esc_html_e('Telegram Channel', 'helptrickbd-edu'); ?></span>
      </a>
      <a href="https://whatsapp.com/channel/0029Vb956jgCHDyrx1wkUh2a" target="_blank" rel="noopener noreferrer" class="ht-btn ht-btn-whatsapp">
        <?php htbd_icon('whatsapp', array('width' => 16, 'height' => 16)); ?>
        <span><?php esc_html_e('WhatsApp Channel', 'helptrickbd-edu'); ?></span>
      </a>
    </div>
  </div>
</div>
