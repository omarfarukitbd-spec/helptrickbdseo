<?php
/**
 * The Header for HelpTrickBD Pro
 * Semantic HTML5, Zero Emojis, Material 3 Vector Icons, Top Bar & Navigation.
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}
?><!DOCTYPE html>
<html <?php language_attributes(); ?> data-theme="light">
<head>
    <meta charset="<?php bloginfo('charset'); ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <link rel="profile" href="https://gmpg.org/xfn/11">
    <?php wp_head(); ?>
</head>

<body <?php body_class(); ?>>
<?php wp_body_open(); ?>

<!-- Skip to content for accessibility -->
<a class="skip-link screen-reader-text" href="#primary">মূল বিষয়বস্তুতে যান</a>

<div id="page" class="ht-site-wrapper">

    <!-- Top Bar: Breaking Notice, Countdown & Date -->
    <aside class="ht-topbar" aria-label="জরুরি বিজ্ঞপ্তি ও সময়">
        <div class="ht-container ht-topbar-inner">
            
            <!-- Breaking Notice Ticker -->
            <?php if (get_theme_mod('ht_ticker_enable', true)) : ?>
                <div class="ht-ticker-wrap">
                    <span class="ht-ticker-badge">
                        <?php ht_m3_icon('campaign', 16, 'ht-ticker-icon'); ?>
                        <span>বিজ্ঞপ্তি</span>
                    </span>
                    <div class="ht-ticker-content">
                        <?php
                        $ticker_text = get_theme_mod('ht_ticker_text', 'জাতীয় বিশ্ববিদ্যালয় অনার্স ২য় বর্ষ পরীক্ষার গাইড ও প্রমোশনের নিয়মাবলী ২০২৬');
                        $ticker_link = get_theme_mod('ht_ticker_link', '');
                        if ($ticker_link) : ?>
                            <a href="<?php echo esc_url($ticker_link); ?>" class="ht-ticker-link"><?php echo esc_html($ticker_text); ?></a>
                        <?php else : ?>
                            <span class="ht-ticker-text"><?php echo esc_html($ticker_text); ?></span>
                        <?php endif; ?>
                    </div>
                </div>
            <?php endif; ?>

            <!-- Topbar Right: Exam Countdown & Date -->
            <div class="ht-topbar-right">
                <?php if (get_theme_mod('ht_countdown_enable', true)) : ?>
                    <div class="ht-top-countdown" id="ht-top-countdown" title="আসন্ন পরীক্ষার দিন গণনা">
                        <?php ht_m3_icon('timer', 15); ?>
                        <span class="ht-countdown-title"><?php echo esc_html(get_theme_mod('ht_countdown_title', 'অনার্স ২য় বর্ষ')); ?>:</span>
                        <span class="ht-countdown-days" id="ht-countdown-val">গণনা হচ্ছে...</span>
                    </div>
                <?php endif; ?>

                <div class="ht-topbar-date">
                    <?php ht_m3_icon('event', 14); ?>
                    <span><?php echo esc_html(ht_bn_date()); ?></span>
                </div>
            </div>

        </div>
    </aside>

    <!-- Main Navigation Header -->
    <header id="masthead" class="ht-header">
        <div class="ht-container ht-header-inner">

            <!-- Mobile Hamburger Button -->
            <button class="ht-menu-toggle" id="ht-menu-toggle" aria-label="মেনু খুলুন" aria-expanded="false">
                <?php ht_m3_icon('menu', 24, 'ht-icon-menu'); ?>
                <?php ht_m3_icon('close', 24, 'ht-icon-close'); ?>
            </button>

            <!-- Brand Logo / Site Title -->
            <div class="ht-brand">
                <?php if (has_custom_logo()) : ?>
                    <?php the_custom_logo(); ?>
                <?php else : ?>
                    <a href="<?php echo esc_url(home_url('/')); ?>" class="ht-logo-link" rel="home">
                        <span class="ht-logo-text">HelpTrick<span class="ht-logo-accent">BD</span></span>
                        <span class="ht-logo-tagline">শিক্ষা ও প্রযুক্তি সহায়ক পোর্টাল</span>
                    </a>
                <?php endif; ?>
            </div>

            <!-- Primary Navigation Menu -->
            <nav id="site-navigation" class="ht-nav" aria-label="প্রধান নেভিগেশন">
                <?php
                if (has_nav_menu('primary-menu')) {
                    wp_nav_menu([
                        'theme_location' => 'primary-menu',
                        'menu_class'     => 'ht-menu-list',
                        'container'      => false,
                        'depth'          => 2,
                        'fallback_cb'    => false,
                    ]);
                } else {
                    // Default fallback menu based on HelpTrickBD categories
                    ?>
                    <ul class="ht-menu-list">
                        <li><a href="<?php echo esc_url(home_url('/')); ?>">হোম</a></li>
                        <li><a href="<?php echo esc_url(home_url('/category/education-guide/')); ?>">শিক্ষা গাইড</a></li>
                        <li><a href="<?php echo esc_url(home_url('/category/national-university/')); ?>">জাতীয় বিশ্ববিদ্যালয়</a></li>
                        <li><a href="<?php echo esc_url(home_url('/category/ssc-dakhil/')); ?>">এসএসসি ও দাখিল</a></li>
                        <li><a href="<?php echo esc_url(home_url('/category/political-science/')); ?>">রাষ্ট্রবিজ্ঞান</a></li>
                        <li><a href="<?php echo esc_url(home_url('/category/ict-technology/')); ?>">আইসিটি</a></li>
                        <li><a href="<?php echo esc_url(home_url('/category/job-preparation/')); ?>">চাকরি প্রস্তুতি</a></li>
                    </ul>
                    <?php
                }
                ?>
            </nav>

            <!-- Action Controls (Search, Bookmarks, Theme Switcher) -->
            <div class="ht-header-actions">
                
                <?php if (get_theme_mod('ht_header_search_enable', true)) : ?>
                    <!-- Instant Search Trigger (Ctrl+K) -->
                    <button class="ht-search-btn" id="ht-search-trigger" aria-label="অনুসন্ধান করুন (Ctrl+K)">
                        <?php ht_m3_icon('search', 20); ?>
                        <span class="ht-search-text">খুঁজুন...</span>
                        <kbd class="ht-search-kbd">Ctrl+K</kbd>
                    </button>
                <?php endif; ?>

                <?php if (get_theme_mod('ht_header_bookmarks_enable', true)) : ?>
                    <!-- Saved Bookmarks Drawer Trigger -->
                    <button class="ht-action-btn ht-bookmarks-trigger" id="ht-bookmarks-trigger" aria-label="পড়ার তালিকা (বুকমার্ক)" title="পড়ার তালিকা">
                        <?php ht_m3_icon('bookmark', 20); ?>
                        <span class="ht-badge-count" id="ht-bookmark-badge">০</span>
                    </button>
                <?php endif; ?>

                <?php if (get_theme_mod('ht_header_theme_toggle_enable', true)) : ?>
                    <!-- Dark / Light Mode Switcher -->
                    <button class="ht-action-btn ht-theme-toggle" id="ht-theme-toggle" aria-label="ডার্ক/লাইট মোড পরিবর্তন করুন" title="থিম পরিবর্তন">
                        <span class="ht-theme-icon-light"><?php ht_m3_icon('dark_mode', 20); ?></span>
                        <span class="ht-theme-icon-dark"><?php ht_m3_icon('light_mode', 20); ?></span>
                    </button>
                <?php endif; ?>

            </div>

        </div>

        <!-- Mobile Drawer Navigation -->
        <div class="ht-mobile-drawer" id="ht-mobile-drawer" aria-hidden="true">
            <div class="ht-mobile-drawer-header">
                <div class="ht-drawer-brand">
                    <span class="ht-logo-text">HelpTrick<span class="ht-logo-accent">BD</span></span>
                </div>
                <button class="ht-drawer-close" id="ht-drawer-close" aria-label="মেনু বন্ধ করুন">
                    <?php ht_m3_icon('close', 20); ?>
                </button>
            </div>
            
            <?php if (get_theme_mod('ht_countdown_enable', true)) : ?>
                <div class="ht-drawer-countdown">
                    <?php ht_m3_icon('timer', 16); ?>
                    <span><?php echo esc_html(get_theme_mod('ht_countdown_title', 'অনার্স ২য় বর্ষ')); ?>:</span>
                    <strong id="ht-drawer-countdown-val">গণনা হচ্ছে...</strong>
                </div>
            <?php endif; ?>

            <div class="ht-mobile-drawer-body">
                <span class="ht-drawer-section-title">মূল নেভিগেশন ও বিষয়সমূহ</span>
                <?php
                if (has_nav_menu('mobile-menu')) {
                    wp_nav_menu(['theme_location' => 'mobile-menu', 'menu_class' => 'ht-mobile-menu-list', 'container' => false]);
                } else {
                    wp_nav_menu(['theme_location' => 'primary-menu', 'menu_class' => 'ht-mobile-menu-list', 'container' => false, 'fallback_cb' => false]);
                }
                ?>
            </div>

            <div class="ht-drawer-footer">
                <div class="ht-drawer-social">
                    <a href="<?php echo esc_url(get_theme_mod('ht_whatsapp_url', 'https://chat.whatsapp.com/')); ?>" target="_blank" rel="noopener noreferrer" class="ht-btn ht-btn-sm ht-btn-whatsapp">
                        <?php ht_m3_icon('whatsapp', 16); ?>
                        <span>WhatsApp গ্রুপ</span>
                    </a>
                    <a href="<?php echo esc_url(get_theme_mod('ht_telegram_url', 'https://t.me/helptrickbd')); ?>" target="_blank" rel="noopener noreferrer" class="ht-btn ht-btn-sm ht-btn-telegram">
                        <?php ht_m3_icon('telegram', 16); ?>
                        <span>Telegram চ্যানেল</span>
                    </a>
                </div>
            </div>
        </div>
        <div class="ht-drawer-overlay" id="ht-drawer-overlay"></div>
    </header>

    <!-- Header Ad Slot (if configured in Customizer) -->
    <?php ht_render_ad('ht_ad_header', 'ht-container ht-ad-header-slot', 90); ?>

    <!-- Main Content Container Wrapper -->
    <div id="content" class="ht-site-content">
