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
    <button class="ht-dock-btn" id="ht-dock-copy" aria-label="<?php echo (function_exists('ht_is_bangla_locale') && !ht_is_bangla_locale()) ? esc_attr__('Copy Selected Text', 'helptrickbd') : esc_attr__('নির্বাচিত অংশ কপি করুন', 'helptrickbd'); ?>">
        <?php ht_m3_icon('content_copy', 15); ?>
        <span><?php echo (function_exists('ht_is_bangla_locale') && !ht_is_bangla_locale()) ? esc_html__('Copy', 'helptrickbd') : esc_html__('কপি', 'helptrickbd'); ?></span>
    </button>
    <button class="ht-dock-btn" id="ht-dock-share-wa" aria-label="<?php echo (function_exists('ht_is_bangla_locale') && !ht_is_bangla_locale()) ? esc_attr__('Share via WhatsApp', 'helptrickbd') : esc_attr__('হোয়াটসঅ্যাপে শেয়ার করুন', 'helptrickbd'); ?>">
        <?php ht_m3_icon('whatsapp', 15); ?>
        <span><?php echo (function_exists('ht_is_bangla_locale') && !ht_is_bangla_locale()) ? esc_html__('Share', 'helptrickbd') : esc_html__('শেয়ার', 'helptrickbd'); ?></span>
    </button>
</div>

<!-- Print Watermark Container (Visible Only During Print) -->
<div class="ht-print-watermark" aria-hidden="true">
    <div class="ht-print-logo">HelpTrickBD.com</div>
    <?php
    $print_sub = (function_exists('ht_is_bangla_locale') && !ht_is_bangla_locale()) ? esc_html__('Education & Technology Resource Portal', 'helptrickbd') : esc_html__('শিক্ষা ও তথ্যপ্রযুক্তি রিসোর্স পোর্টাল', 'helptrickbd');
    ?>
    <div class="ht-print-subtitle"><?php echo esc_html($print_sub); ?> | <?php the_permalink(); ?></div>
</div>
