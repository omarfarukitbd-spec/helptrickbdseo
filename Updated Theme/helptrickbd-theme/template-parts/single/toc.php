<?php
/**
 * Single Post Component: Auto Table of Contents (সূচিপত্র) Container
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

if (!get_theme_mod('ht_toc_enable', true)) {
    return;
}

$is_en = function_exists('ht_is_bangla_locale') && !ht_is_bangla_locale();
$toc_title = $is_en ? esc_html__('Table of Contents', 'helptrickbd') : esc_html__('সূচিপত্র', 'helptrickbd');
$toc_toggle_aria = $is_en ? esc_attr__('Toggle table of contents', 'helptrickbd') : esc_attr__('সূচিপত্র খুলুন বা বন্ধ করুন', 'helptrickbd');
?>
<!-- Auto Table of Contents (সূচিপত্র) Container -->
<div class="ht-toc-container" id="ht-toc-container">
    <div class="ht-toc-header" id="ht-toc-header">
        <div class="ht-toc-title-wrap">
            <?php ht_m3_icon('format_list_bulleted', 18); ?>
            <span class="ht-toc-title"><?php echo esc_html($toc_title); ?></span>
        </div>
        <button class="ht-toc-toggle" id="ht-toc-toggle-btn" aria-label="<?php echo esc_attr($toc_toggle_aria); ?>">
            <?php ht_m3_icon('keyboard_arrow_down', 18); ?>
        </button>
    </div>
    <nav class="ht-toc-nav" id="ht-toc-nav" aria-label="<?php echo esc_attr($toc_title); ?>"></nav>
</div>
