<?php
/**
 * Single Post Component: Student Reading Toolbelt (Font Resizer, Focus Mode, Save, Print)
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}
$is_en = function_exists('ht_is_bangla_locale') && !ht_is_bangla_locale();
?>
<div class="ht-reading-toolbelt">
    <?php if (get_theme_mod('ht_font_resizer_enable', true)) : ?>
        <!-- Font Size Resizer -->
        <div class="ht-toolbelt-group ht-font-resizer" title="<?php echo $is_en ? esc_attr__('Change font size', 'helptrickbd') : esc_attr__('ফন্টের আকার পরিবর্তন করুন', 'helptrickbd'); ?>">
            <span class="ht-tool-label"><?php ht_m3_icon('format_size', 16); ?> <?php echo $is_en ? esc_html__('Font:', 'helptrickbd') : esc_html__('ফন্ট:', 'helptrickbd'); ?></span>
            <button class="ht-resizer-btn" id="ht-font-dec" aria-label="<?php echo $is_en ? esc_attr__('Decrease font size', 'helptrickbd') : esc_attr__('ফন্ট ছোট করুন', 'helptrickbd'); ?>">A-</button>
            <button class="ht-resizer-btn ht-active" id="ht-font-reset" aria-label="<?php echo $is_en ? esc_attr__('Reset font size', 'helptrickbd') : esc_attr__('স্বাভাবিক আকার', 'helptrickbd'); ?>">A</button>
            <button class="ht-resizer-btn" id="ht-font-inc" aria-label="<?php echo $is_en ? esc_attr__('Increase font size', 'helptrickbd') : esc_attr__('ফন্ট বড় করুন', 'helptrickbd'); ?>">A+</button>
        </div>
    <?php endif; ?>

    <?php if (get_theme_mod('ht_focus_mode_enable', true)) : ?>
        <!-- Focus Mode Toggle -->
        <button class="ht-toolbelt-btn" id="ht-focus-toggle" aria-label="<?php echo $is_en ? esc_attr__('Focus reading mode', 'helptrickbd') : esc_attr__('ফোকাস রিডিং মোড', 'helptrickbd'); ?>" title="<?php echo $is_en ? esc_attr__('Focus Mode', 'helptrickbd') : esc_attr__('ফোকাস রিডিং মোড', 'helptrickbd'); ?>">
            <?php ht_m3_icon('auto_stories', 16); ?>
            <span class="ht-btn-label"><?php echo $is_en ? esc_html__('Focus Mode', 'helptrickbd') : esc_html__('ফোকাস মোড', 'helptrickbd'); ?></span>
        </button>
    <?php endif; ?>

    <?php if (get_theme_mod('ht_bookmark_btn_enable', true)) : ?>
        <!-- Bookmark / Save for Later -->
        <button class="ht-toolbelt-btn ht-bookmark-toggle" data-id="<?php the_ID(); ?>" data-title="<?php echo esc_attr(get_the_title()); ?>" data-url="<?php the_permalink(); ?>" aria-label="<?php echo $is_en ? esc_attr__('Save to reading list', 'helptrickbd') : esc_attr__('পড়ার তালিকায় সেভ করুন', 'helptrickbd'); ?>" title="<?php echo $is_en ? esc_attr__('Save Post', 'helptrickbd') : esc_attr__('পড়ার তালিকায় সেভ করুন', 'helptrickbd'); ?>">
            <?php ht_m3_icon('bookmark', 16); ?>
            <span class="ht-bm-text ht-btn-label"><?php echo $is_en ? esc_html__('Save Post', 'helptrickbd') : esc_html__('পোস্ট সেভ', 'helptrickbd'); ?></span>
        </button>
    <?php endif; ?>

    <?php if (get_theme_mod('ht_print_btn_enable', true)) : ?>
        <!-- 1-Click Print & PDF -->
        <button class="ht-toolbelt-btn" id="ht-print-btn" aria-label="<?php echo $is_en ? esc_attr__('Print or save PDF', 'helptrickbd') : esc_attr__('প্রিন্ট বা পিডিএফ সেভ করুন', 'helptrickbd'); ?>" title="<?php echo $is_en ? esc_attr__('Print / PDF', 'helptrickbd') : esc_attr__('প্রিন্ট বা পিডিএফ সেভ করুন', 'helptrickbd'); ?>">
            <?php ht_m3_icon('print', 16); ?>
            <span class="ht-btn-label"><?php echo $is_en ? esc_html__('Print / PDF', 'helptrickbd') : esc_html__('প্রিন্ট / PDF', 'helptrickbd'); ?></span>
        </button>
    <?php endif; ?>
</div>
