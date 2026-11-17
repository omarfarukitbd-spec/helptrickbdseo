<?php
/**
 * The Header for HelpTrickBD Pro
 * Semantic HTML5, Material 3 Vector Icons, Masthead & Navigation.
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
    <meta name="color-scheme" content="light dark">
    <meta name="theme-color" content="#1e40af">
    <link rel="profile" href="https://gmpg.org/xfn/11">
    <link rel="manifest" href="<?php echo esc_url(get_template_directory_uri() . '/manifest.json'); ?>">
    <link rel="apple-touch-icon" href="<?php echo esc_url(get_template_directory_uri() . '/assets/images/icon-192.png'); ?>">
    <?php wp_head(); ?>
</head>

<body <?php body_class(); ?>>
<?php wp_body_open(); ?>

<!-- Skip to content for accessibility -->
<a class="skip-link screen-reader-text" href="#primary"><?php esc_html_e('সরাসরি মূল কনটেন্টে যান', 'helptrickbd'); ?></a>

<div id="page" class="ht-site-wrapper site-wrapper">

    <?php
    // 1. Topbar / Dateline (Optional or sitewide)
    if (get_theme_mod('ht_topbar_enable', true)) {
        get_template_part('template-parts/header/topbar');
    }

    // 2. Newspaper Masthead (Left Logo, Right Search, No Tagline)
    get_template_part('template-parts/header/masthead');

    // 3. Sticky Newspaper Navigation & Category Track
    get_template_part('template-parts/header/navbar');
    ?>

    <!-- Mobile Drawer Navigation -->
    <div class="ht-mobile-drawer" id="ht-mobile-drawer" aria-hidden="true">
        <div class="ht-mobile-drawer-header">
            <div class="ht-drawer-brand">
                <span class="ht-logo-text">HelpTrick<span class="ht-logo-accent">BD</span></span>
            </div>
            <button class="ht-drawer-close" id="ht-drawer-close" aria-label="<?php esc_attr_e('মেনু বন্ধ করুন', 'helptrickbd'); ?>">
                <?php ht_m3_icon('close', 20); ?>
            </button>
        </div>
        
        <div class="ht-mobile-drawer-body">
            <!-- Dynamic All Categories Engine -->
            <div class="ht-drawer-categories-wrap">
                <div class="ht-drawer-section-header">
                    <span class="ht-drawer-section-title"><?php esc_html_e('সকল ক্যাটাগরি ও বিষয়', 'helptrickbd'); ?></span>
                    <?php 
                    $cat_count_total = wp_count_terms(['taxonomy' => 'category', 'hide_empty' => true]);
                    if (!is_wp_error($cat_count_total) && $cat_count_total > 0) :
                    ?>
                        <span class="ht-drawer-cat-total"><?php echo esc_html(function_exists('ht_bn_number') ? ht_bn_number($cat_count_total) : $cat_count_total); ?></span>
                    <?php endif; ?>
                </div>
                <div class="ht-drawer-cat-list">
                    <?php
                    $drawer_cats = get_categories([
                        'orderby'    => 'count',
                        'order'      => 'DESC',
                        'hide_empty' => true,
                        'exclude'    => [1],
                        'number'     => 0,
                    ]);
                    if (!empty($drawer_cats)) :
                        foreach ($drawer_cats as $d_cat) :
                            if ($d_cat->slug === 'uncategorized' || $d_cat->count <= 0 || $d_cat->term_id == 1) continue;
                            $cat_icon = function_exists('ht_get_category_icon') ? ht_get_category_icon($d_cat->slug, $d_cat->name) : 'folder';
                            $cat_pal  = function_exists('ht_get_category_palette') ? ht_get_category_palette($d_cat->slug, $d_cat->name) : ['color' => '#2563eb', 'bg' => 'rgba(37,99,235,0.08)', 'border' => 'rgba(37,99,235,0.2)'];
                    ?>
                            <a href="<?php echo esc_url(get_category_link($d_cat->term_id)); ?>" 
                               class="ht-drawer-cat-item"
                               style="--cat-color: <?php echo esc_attr($cat_pal['color']); ?>; --cat-bg: <?php echo esc_attr($cat_pal['bg']); ?>; --cat-border: <?php echo esc_attr($cat_pal['border']); ?>;">
                                <span class="ht-drawer-cat-icon"><?php ht_m3_icon($cat_icon, 18); ?></span>
                                <span class="ht-drawer-cat-name"><?php echo esc_html($d_cat->name); ?></span>
                                <span class="ht-drawer-cat-badge"><?php echo esc_html(function_exists('ht_bn_number') ? ht_bn_number($d_cat->count) : $d_cat->count); ?></span>
                            </a>
                    <?php
                        endforeach;
                    endif;
                    ?>
                </div>
            </div>
        </div>
    </div>
    <div class="ht-drawer-overlay" id="ht-drawer-overlay"></div>

    <!-- Header Ad Slot (if configured in Customizer) -->
    <?php if (function_exists('ht_render_ad')) { ht_render_ad('ht_ad_header', 'ht-container ht-ad-header-slot', 90); } ?>

    <!-- Main Content Container Wrapper -->
    <div id="content" class="ht-site-content">
