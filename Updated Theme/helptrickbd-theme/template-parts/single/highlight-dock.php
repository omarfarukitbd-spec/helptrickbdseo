<?php
/**
 * Single Post Component: Medium-style Text Highlight Floating Dock & Print Watermark
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}
?>
<!-- Medium-style Text Highlight Floating Dock -->
<div class="ht-highlight-dock" id="ht-highlight-dock" aria-hidden="true">
    <button class="ht-dock-btn" id="ht-dock-copy" aria-label="<?php esc_attr_e('নির্বাচিত অংশ কপি করুন', 'helptrickbd'); ?>">
        <?php ht_m3_icon('content_copy', 15); ?>
        <span><?php esc_html_e('কপি', 'helptrickbd'); ?></span>
    </button>
    <button class="ht-dock-btn" id="ht-dock-share-wa" aria-label="<?php esc_attr_e('হোয়াটসঅ্যাপে শেয়ার করুন', 'helptrickbd'); ?>">
        <?php ht_m3_icon('whatsapp', 15); ?>
        <span><?php esc_html_e('শেয়ার', 'helptrickbd'); ?></span>
    </button>
</div>

<!-- Print Watermark Container (Visible Only During Print) -->
<div class="ht-print-watermark" aria-hidden="true">
    <div class="ht-print-logo">HelpTrickBD.com</div>
    <div class="ht-print-subtitle">শিক্ষা ও তথ্যপ্রযুক্তি রিসোর্স পোর্টাল | <?php the_permalink(); ?></div>
</div>
