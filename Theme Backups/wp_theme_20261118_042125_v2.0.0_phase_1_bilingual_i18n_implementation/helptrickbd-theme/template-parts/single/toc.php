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
?>
<!-- Auto Table of Contents (সূচিপত্র) Container -->
<div class="ht-toc-container" id="ht-toc-container">
    <div class="ht-toc-header" id="ht-toc-header">
        <div class="ht-toc-title-wrap">
            <?php ht_m3_icon('format_list_bulleted', 18); ?>
            <span class="ht-toc-title"><?php esc_html_e('সূচিপত্র', 'helptrickbd'); ?></span>
        </div>
        <button class="ht-toc-toggle" id="ht-toc-toggle-btn" aria-label="<?php esc_attr_e('সূচিপত্র খুলুন বা বন্ধ করুন', 'helptrickbd'); ?>">
            <?php ht_m3_icon('keyboard_arrow_down', 18); ?>
        </button>
    </div>
    <nav class="ht-toc-nav" id="ht-toc-nav" aria-label="<?php esc_attr_e('সূচিপত্র', 'helptrickbd'); ?>"></nav>
</div>
