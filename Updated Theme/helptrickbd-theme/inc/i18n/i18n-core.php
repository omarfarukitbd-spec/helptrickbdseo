<?php
/**
 * Internationalization (i18n) Core Handler
 * HelpTrickBD Pro Theme
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Load Theme Textdomain.
 */
function ht_load_theme_textdomain() {
    load_theme_textdomain('helptrickbd', get_template_directory() . '/languages');
}
add_action('after_setup_theme', 'ht_load_theme_textdomain');

/**
 * Get the current active language code ('bn' or 'en').
 *
 * @return string Language slug ('bn' or 'en').
 */
function ht_get_current_lang() {
    // 1. Polylang Integration
    if (function_exists('pll_current_language')) {
        $pll_lang = pll_current_language('slug');
        if (!empty($pll_lang)) {
            return ($pll_lang === 'en') ? 'en' : 'bn';
        }
    }

    // 2. WPML Integration
    if (defined('ICL_LANGUAGE_CODE')) {
        return (ICL_LANGUAGE_CODE === 'en') ? 'en' : 'bn';
    }

    // 3. User session / Query Param Override (?lang=en or ?lang=bn)
    if (isset($_GET['lang']) && in_array(sanitize_key($_GET['lang']), ['en', 'bn'], true)) {
        return sanitize_key($_GET['lang']);
    }

    // 4. Native WordPress Locale Check
    $locale = get_locale();
    if (stripos($locale, 'en') === 0) {
        return 'en';
    }

    // Default to Bengali
    return 'bn';
}

/**
 * Check if the current locale/language is Bengali.
 *
 * @return bool True if Bengali, false otherwise.
 */
function ht_is_bangla_locale() {
    return ht_get_current_lang() === 'bn';
}

/**
 * Generate language switch URL for given target language.
 *
 * @param string $target_lang Target language code ('bn' or 'en').
 * @return string Target language URL.
 */
function ht_get_language_url($target_lang = 'bn') {
    // 1. Polylang handler
    if (function_exists('pll_the_languages')) {
        $translations = pll_the_languages(['raw' => 1]);
        if (!empty($translations) && is_array($translations)) {
            foreach ($translations as $item) {
                if (isset($item['slug']) && $item['slug'] === $target_lang && !empty($item['url'])) {
                    return $item['url'];
                }
            }
        }
    }

    // 2. Default Query Param Fallback
    return add_query_arg('lang', $target_lang);
}
