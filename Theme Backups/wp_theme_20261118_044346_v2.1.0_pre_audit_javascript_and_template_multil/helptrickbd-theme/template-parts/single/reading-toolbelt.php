<?php
/**
 * Single Post Component: Student Reading Toolbelt (Font Resizer, Focus Mode, Save, Print)
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}
?>
<div class="ht-reading-toolbelt">
    <?php if (get_theme_mod('ht_font_resizer_enable', true)) : ?>
        <!-- Font Size Resizer -->
        <div class="ht-toolbelt-group ht-font-resizer" title="<?php esc_attr_e('ফন্টের আকার পরিবর্তন করুন', 'helptrickbd'); ?>">
            <span class="ht-tool-label"><?php ht_m3_icon('format_size', 16); ?> <?php esc_html_e('ফন্ট:', 'helptrickbd'); ?></span>
            <button class="ht-resizer-btn" id="ht-font-dec" aria-label="<?php esc_attr_e('ফন্ট ছোট করুন', 'helptrickbd'); ?>">A-</button>
            <button class="ht-resizer-btn ht-active" id="ht-font-reset" aria-label="<?php esc_attr_e('স্বাভাবিক আকার', 'helptrickbd'); ?>">A</button>
            <button class="ht-resizer-btn" id="ht-font-inc" aria-label="<?php esc_attr_e('ফন্ট বড় করুন', 'helptrickbd'); ?>">A+</button>
        </div>
    <?php endif; ?>

    <?php if (get_theme_mod('ht_focus_mode_enable', true)) : ?>
        <!-- Focus Mode Toggle -->
        <button class="ht-toolbelt-btn" id="ht-focus-toggle" aria-label="<?php esc_attr_e('ফোকাস রিডিং মোড', 'helptrickbd'); ?>">
            <?php ht_m3_icon('auto_stories', 16); ?>
            <span><?php esc_html_e('ফোকাস মোড', 'helptrickbd'); ?></span>
        </button>
    <?php endif; ?>

    <?php if (get_theme_mod('ht_bookmark_btn_enable', true)) : ?>
        <!-- Bookmark / Save for Later -->
        <button class="ht-toolbelt-btn ht-bookmark-toggle" data-id="<?php the_ID(); ?>" data-title="<?php echo esc_attr(get_the_title()); ?>" data-url="<?php the_permalink(); ?>" aria-label="<?php esc_attr_e('পড়ার তালিকায় সেভ করুন', 'helptrickbd'); ?>">
            <?php ht_m3_icon('bookmark', 16); ?>
            <span class="ht-bm-text"><?php esc_html_e('পোস্ট সেভ করুন', 'helptrickbd'); ?></span>
        </button>
    <?php endif; ?>

    <?php if (get_theme_mod('ht_print_btn_enable', true)) : ?>
        <!-- 1-Click Print & PDF -->
        <button class="ht-toolbelt-btn" id="ht-print-btn" aria-label="<?php esc_attr_e('প্রিন্ট বা পিডিএফ সেভ করুন', 'helptrickbd'); ?>">
            <?php ht_m3_icon('print', 16); ?>
            <span><?php esc_html_e('প্রিন্ট বা পিডিএফ', 'helptrickbd'); ?></span>
        </button>
    <?php endif; ?>
</div>
