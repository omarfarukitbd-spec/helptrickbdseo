<?php
/**
 * Header Component: Bilingual Language Switcher [ BN | EN ]
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

$current_lang = function_exists('ht_get_current_lang') ? ht_get_current_lang() : 'bn';
$bn_url       = function_exists('ht_get_language_url') ? ht_get_language_url('bn') : '?lang=bn';
$en_url       = function_exists('ht_get_language_url') ? ht_get_language_url('en') : '?lang=en';
?>
<!-- Bilingual Language Switcher -->
<div class="ht-lang-switcher" aria-label="<?php esc_attr_e('Language Selector', 'helptrickbd'); ?>">
    <a href="<?php echo esc_url($bn_url); ?>" 
       class="ht-lang-btn ht-lang-bn <?php echo ($current_lang === 'bn') ? 'is-active' : ''; ?>" 
       hreflang="bn" 
       title="<?php esc_attr_e('বাংলা সংস্করণ', 'helptrickbd'); ?>">
       বাংলা
    </a>
    <span class="ht-lang-divider" aria-hidden="true">|</span>
    <a href="<?php echo esc_url($en_url); ?>" 
       class="ht-lang-btn ht-lang-en <?php echo ($current_lang === 'en') ? 'is-active' : ''; ?>" 
       hreflang="en" 
       title="<?php esc_attr_e('English Edition', 'helptrickbd'); ?>">
       EN
    </a>
</div>
