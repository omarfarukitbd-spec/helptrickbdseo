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

    // 4. Cookie Persistence (30-day sticky language selection)
    if (isset($_COOKIE['ht_lang']) && in_array(sanitize_key($_COOKIE['ht_lang']), ['en', 'bn'], true)) {
        return sanitize_key($_COOKIE['ht_lang']);
    }

    // Default to Bengali
    return 'bn';
}

/**
 * Persist user language choice in cookie on request.
 */
function ht_handle_lang_cookie() {
    if (isset($_GET['lang']) && in_array(sanitize_key($_GET['lang']), ['en', 'bn'], true)) {
        $target_lang = sanitize_key($_GET['lang']);
        if (!headers_sent()) {
            $cookie_path = defined('COOKIEPATH') && COOKIEPATH ? COOKIEPATH : '/';
            $cookie_domain = defined('COOKIE_DOMAIN') ? COOKIE_DOMAIN : '';
            setcookie('ht_lang', $target_lang, time() + (30 * 86400), $cookie_path, $cookie_domain, is_ssl(), false);
            $_COOKIE['ht_lang'] = $target_lang;
        }
    }
}
add_action('init', 'ht_handle_lang_cookie', 1);

/**
 * Filter WordPress Core Locale dynamically.
 *
 * @param string $locale Core locale string.
 * @return string Filtered locale ('bn_BD' or 'en_US').
 */
function ht_dynamic_locale_filter($locale) {
    if (function_exists('pll_current_language') || defined('ICL_LANGUAGE_CODE')) {
        return $locale;
    }
    return ht_is_bangla_locale() ? 'bn_BD' : 'en_US';
}
add_filter('locale', 'ht_dynamic_locale_filter', 99);

/**
 * Dynamically filter HTML language attributes for strict W3C and SEO conformance.
 *
 * @param string $output Language attributes string.
 * @return string Filtered language attributes.
 */
function ht_dynamic_language_attributes($output) {
    $lang_code = ht_is_bangla_locale() ? 'bn-BD' : 'en-US';
    if (preg_match('/lang=[\'"][^\'"]*[\'"]/i', $output)) {
        $output = preg_replace('/lang=[\'"][^\'"]*[\'"]/i', 'lang="' . $lang_code . '"', $output);
    } else {
        $output .= ' lang="' . $lang_code . '"';
    }
    return $output;
}
add_filter('language_attributes', 'ht_dynamic_language_attributes', 99);

/**
 * Add language class to body.
 *
 * @param array $classes Array of body classes.
 * @return array Filtered array of body classes.
 */
function ht_dynamic_body_class($classes) {
    if (ht_is_bangla_locale()) {
        $classes[] = 'ht-lang-bn';
    } else {
        $classes[] = 'ht-lang-en';
    }
    return $classes;
}
add_filter('body_class', 'ht_dynamic_body_class', 20);

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
