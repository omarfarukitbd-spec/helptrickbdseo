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
    <h3 class="ht-footer-title"><?php esc_html_e('হেল্পট্রিকবিডি সম্পর্কে', 'helptrickbd-edu'); ?></h3>
    <p>
      <?php esc_html_e('হেল্পট্রিকবিডি বাংলাদেশের শিক্ষার্থীদের জন্য নির্ভরযোগ্য শিক্ষা ও তথ্যপ্রযুক্তি রিসোর্স পোর্টাল। জাতীয় বিশ্ববিদ্যালয়, বোর্ড পরীক্ষা ও ক্যারিয়ার সংক্রান্ত তথ্যনির্ভর হ্যান্ডনোট সরবরাহ করাই আমাদের মূল অঙ্গীকার।', 'helptrickbd-edu'); ?>
    </p>
    <p class="ht-footer-contact">
      <strong><?php esc_html_e('ইমেইল:', 'helptrickbd-edu'); ?></strong> 
      <a href="mailto:contact@helptrickbd.com">contact@helptrickbd.com</a>
    </p>
  </div>

  <!-- Col 2: Academic Shortcuts -->
  <div class="ht-footer-col">
    <h3 class="ht-footer-title"><?php esc_html_e('একাডেমিক হ্যান্ডনোট', 'helptrickbd-edu'); ?></h3>
    <ul class="ht-footer-links">
      <li><a href="<?php echo esc_url(home_url('/category/national-university/')); ?>"><?php esc_html_e('জাতীয় বিশ্ববিদ্যালয়', 'helptrickbd-edu'); ?></a></li>
      <li><a href="<?php echo esc_url(home_url('/category/ssc-dakhil/')); ?>"><?php esc_html_e('এসএসসি ও দাখিল প্রস্তুতি', 'helptrickbd-edu'); ?></a></li>
      <li><a href="<?php echo esc_url(home_url('/category/political-science/')); ?>"><?php esc_html_e('রাষ্ট্রবিজ্ঞান হ্যান্ডনোট', 'helptrickbd-edu'); ?></a></li>
      <li><a href="<?php echo esc_url(home_url('/category/english/')); ?>"><?php esc_html_e('ইংরেজি গ্রামার ও রুলস', 'helptrickbd-edu'); ?></a></li>
      <li><a href="<?php echo esc_url(home_url('/nu-cgpa-calculator/')); ?>"><?php esc_html_e('NU সিজিপিএ ক্যালকুলেটর', 'helptrickbd-edu'); ?></a></li>
    </ul>
  </div>

  <!-- Col 3: Institutional Links -->
  <div class="ht-footer-col">
    <h3 class="ht-footer-title"><?php esc_html_e('প্রাতিষ্ঠানিক নীতি', 'helptrickbd-edu'); ?></h3>
    <ul class="ht-footer-links">
      <li><a href="<?php echo esc_url(home_url('/about-us/')); ?>"><?php esc_html_e('আমাদের সম্পর্কে', 'helptrickbd-edu'); ?></a></li>
      <li><a href="<?php echo esc_url(home_url('/contact-us/')); ?>"><?php esc_html_e('যোগাযোগ', 'helptrickbd-edu'); ?></a></li>
      <li><a href="<?php echo esc_url(home_url('/privacy-policy/')); ?>"><?php esc_html_e('গোপনীয়তা নীতি', 'helptrickbd-edu'); ?></a></li>
      <li><a href="<?php echo esc_url(home_url('/terms-conditions/')); ?>"><?php esc_html_e('ব্যবহারের শর্তাবলী', 'helptrickbd-edu'); ?></a></li>
      <li><a href="<?php echo esc_url(home_url('/disclaimer/')); ?>"><?php esc_html_e('দাবিত্যাগ (Disclaimer)', 'helptrickbd-edu'); ?></a></li>
      <li><a href="<?php echo esc_url(home_url('/cookie-policy/')); ?>"><?php esc_html_e('কুকি নীতিমালা', 'helptrickbd-edu'); ?></a></li>
      <li><a href="<?php echo esc_url(home_url('/sitemap/')); ?>"><?php esc_html_e('সাইটম্যাপ', 'helptrickbd-edu'); ?></a></li>
    </ul>
  </div>

  <!-- Col 4: Community & Official Channels -->
  <div class="ht-footer-col">
    <h3 class="ht-footer-title"><?php esc_html_e('স্টাডি চ্যানেলে যুক্ত থাকুন', 'helptrickbd-edu'); ?></h3>
    <p><?php esc_html_e('সবার আগে পরীক্ষার রুটিন, নোটিশ ও স্পেশাল সাজেশন পেতে আমাদের অফিসিয়াল চ্যানেলগুলোতে যুক্ত হন:', 'helptrickbd-edu'); ?></p>
    <div class="ht-footer-social-btns">
      <a href="https://t.me/helptrickbd_official" target="_blank" rel="noopener noreferrer" class="ht-btn ht-btn-telegram">
        <?php htbd_icon('telegram', array('width' => 16, 'height' => 16)); ?>
        <span><?php esc_html_e('টেলিগ্রাম চ্যানেল', 'helptrickbd-edu'); ?></span>
      </a>
      <a href="https://whatsapp.com/channel/0029Vb956jgCHDyrx1wkUh2a" target="_blank" rel="noopener noreferrer" class="ht-btn ht-btn-whatsapp">
        <?php htbd_icon('whatsapp', array('width' => 16, 'height' => 16)); ?>
        <span><?php esc_html_e('হোয়াটসঅ্যাপ চ্যানেল', 'helptrickbd-edu'); ?></span>
      </a>
    </div>
  </div>
</div>
