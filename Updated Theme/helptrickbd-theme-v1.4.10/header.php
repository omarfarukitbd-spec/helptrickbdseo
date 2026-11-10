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
<a class="skip-link screen-reader-text" href="#primary"><?php esc_html_e('সরাসরি মূল কনটেন্টে যান', 'helptrickbd'); ?></a>

<div id="page" class="ht-site-wrapper">

    <!-- Top Bar: Breaking Notice, Countdown & Date -->
    <aside class="ht-topbar" aria-label="<?php esc_attr_e('জরুরি নোটিশ ও সময়সূচি', 'helptrickbd'); ?>">
        <div class="ht-container ht-topbar-inner">
            
            <!-- Breaking Notice & Routine Ticker (Dynamic Rotator) -->
            <?php if (get_theme_mod('ht_ticker_enable', true)) : ?>
                <div class="ht-ticker-wrap" id="ht-ticker-wrap">
                    <div class="ht-ticker-badge">
                        <span class="ht-ticker-pulse" aria-hidden="true"></span>
                        <span class="ht-ticker-label"><?php echo esc_html(get_theme_mod('ht_ticker_badge_label', 'নোটিশ ও আপডেট')); ?></span>
                    </div>
                    <div class="ht-ticker-slider" id="ht-ticker-slider">
                        <ul class="ht-ticker-items" id="ht-ticker-items">
                            <?php
                            $ticker_query = new WP_Query([
                                'posts_per_page'      => 6,
                                'post_status'         => 'publish',
                                'ignore_sticky_posts' => 1,
                                'no_found_rows'       => true,
                            ]);
                            if ($ticker_query->have_posts()) :
                                $t_idx = 0;
                                while ($ticker_query->have_posts()) :
                                    $ticker_query->the_post();
                                    $t_idx++;
                                    $active_cls = ($t_idx === 1) ? ' ht-ticker-item-active' : '';
                            ?>
                                    <li class="ht-ticker-item<?php echo esc_attr($active_cls); ?>" data-index="<?php echo esc_attr($t_idx - 1); ?>">
                                        <a href="<?php the_permalink(); ?>" class="ht-ticker-link">
                                            <span class="ht-ticker-title"><?php echo esc_html(wp_trim_words(get_the_title(), 12)); ?></span>
                                        </a>
                                    </li>
                            <?php
                                endwhile;
                                wp_reset_postdata();
                            else :
                                $ticker_fallback = get_theme_mod('ht_ticker_text', 'জাতীয় বিশ্ববিদ্যালয় অনার্স ২য় বর্ষ পরীক্ষার গাইড ও প্রমোশনের নিয়মাবলী ২০২৬');
                            ?>
                                <li class="ht-ticker-item ht-ticker-item-active">
                                    <span class="ht-ticker-text"><?php echo esc_html($ticker_fallback); ?></span>
                                </li>
                            <?php endif; ?>
                        </ul>
                    </div>
                    <div class="ht-ticker-controls">
                        <button type="button" class="ht-ticker-ctrl-btn" id="ht-ticker-prev" aria-label="<?php esc_attr_e('পূর্ববর্তী নোটিশ', 'helptrickbd'); ?>" title="<?php esc_attr_e('পূর্ববর্তী নোটিশ', 'helptrickbd'); ?>">
                            <?php ht_m3_icon('keyboard_arrow_left', 16); ?>
                        </button>
                        <button type="button" class="ht-ticker-ctrl-btn" id="ht-ticker-next" aria-label="<?php esc_attr_e('পরবর্তী নোটিশ', 'helptrickbd'); ?>" title="<?php esc_attr_e('পরবর্তী নোটিশ', 'helptrickbd'); ?>">
                            <?php ht_m3_icon('keyboard_arrow_right', 16); ?>
                        </button>
                    </div>
                </div>
            <?php endif; ?>

            <!-- Topbar Right: Date -->
            <div class="ht-topbar-right">
                <div class="ht-topbar-date">
                    <?php ht_m3_icon('event', 14); ?>
                    <span><?php echo esc_html(date_i18n(get_option('date_format'))); ?></span>
                </div>
            </div>

        </div>
    </aside>

    <!-- Main Navigation Header -->
    <header id="masthead" class="ht-header">
        <div class="ht-container ht-header-inner">

            <!-- Off-Canvas Drawer Hamburger Button (Desktop & Mobile) -->
            <button class="ht-menu-toggle" id="ht-menu-toggle" aria-label="<?php esc_attr_e('সকল ক্যাটাগরি ও মেনু ব্রাউজ করুন', 'helptrickbd'); ?>" title="<?php esc_attr_e('সকল ক্যাটাগরি ও মেনু', 'helptrickbd'); ?>" aria-expanded="false">
                <?php ht_m3_icon('menu', 24, 'ht-icon-menu'); ?>
                <?php ht_m3_icon('close', 24, 'ht-icon-close'); ?>
            </button>

            <!-- Brand Logo / Site Title (Semantic H1 on Homepage) -->
            <div class="ht-brand">
                <?php if (is_front_page() || is_home()) : ?>
                    <h1 class="ht-brand-heading">
                <?php else : ?>
                    <div class="ht-brand-heading">
                <?php endif; ?>

                <?php if (has_custom_logo()) : ?>
                    <?php the_custom_logo(); ?>
                <?php else : ?>
                    <a href="<?php echo esc_url(home_url('/')); ?>" class="ht-logo-link" rel="home">
                        <span class="ht-logo-text">HelpTrick<span class="ht-logo-accent">BD</span></span>
                        <span class="ht-logo-tagline"><?php esc_html_e('শিক্ষা ও তথ্যপ্রযুক্তি রিসোর্স পোর্টাল', 'helptrickbd'); ?></span>
                    </a>
                <?php endif; ?>

                <?php if (is_front_page() || is_home()) : ?>
                    </h1>
                <?php else : ?>
                    </div>
                <?php endif; ?>
            </div>

            <!-- Primary Navigation Menu with Interactive Left & Right Scroll Controls -->
            <div class="ht-nav-wrapper">
                <button type="button" class="ht-nav-scroll-btn ht-nav-scroll-prev" id="ht-nav-prev" aria-label="<?php esc_attr_e('মেনু বামে স্ক্রোল করুন', 'helptrickbd'); ?>" style="display: none;">
                    <?php ht_m3_icon('keyboard_arrow_left', 18); ?>
                </button>
                <nav id="site-navigation" class="ht-nav" aria-label="<?php esc_attr_e('মূল নেভিগেশন মেনু', 'helptrickbd'); ?>">
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
                        // Default fallback menu based on HelpTrickBD categories with rich icons & palette styling
                        $default_nav_items = [
                            ['url' => home_url('/'), 'label' => 'প্রচ্ছদ', 'slug' => 'home', 'name' => 'Home', 'color' => '#2563eb', 'bg' => 'rgba(37,99,235,0.08)', 'border' => 'rgba(37,99,235,0.2)'],
                            ['url' => home_url('/category/education-guide/'), 'label' => 'এডুকেশন গাইড', 'slug' => 'education-guide', 'name' => 'Education Guide'],
                            ['url' => home_url('/category/national-university/'), 'label' => 'জাতীয় বিশ্ববিদ্যালয়', 'slug' => 'national-university', 'name' => 'National University'],
                            ['url' => home_url('/category/ssc-dakhil/'), 'label' => 'এসএসসি ও দাখিল', 'slug' => 'ssc-dakhil', 'name' => 'SSC & Dakhil'],
                            ['url' => home_url('/category/political-science/'), 'label' => 'রাষ্ট্রবিজ্ঞান', 'slug' => 'political-science', 'name' => 'Political Science'],
                            ['url' => home_url('/category/bangla-1st-paper/'), 'label' => 'বাংলা ১ম পত্র', 'slug' => 'bangla-1st-paper', 'name' => 'Bangla'],
                            ['url' => home_url('/category/islamic-article/'), 'label' => 'ইসলামিক প্রবন্ধ', 'slug' => 'islamic-article', 'name' => 'Islamic Article'],
                            ['url' => home_url('/category/english-2nd-paper/'), 'label' => 'ইংরেজি', 'slug' => 'english-2nd-paper', 'name' => 'English'],
                            ['url' => home_url('/category/ict-technology/'), 'label' => 'আইসিটি', 'slug' => 'ict-technology', 'name' => 'ICT & Tech'],
                            ['url' => home_url('/category/job-preparation/'), 'label' => 'চাকরি প্রস্তুতি', 'slug' => 'job-preparation', 'name' => 'Job Preparation'],
                            ['url' => home_url('/category/university-admission/'), 'label' => 'বিশ্ববিদ্যালয় ভর্তি', 'slug' => 'university-admission', 'name' => 'Admission'],
                        ];
                        ?>
                        <ul class="ht-menu-list">
                            <?php foreach ($default_nav_items as $d_item) :
                                $cat_pal    = function_exists('ht_get_category_palette') ? ht_get_category_palette($d_item['slug'], $d_item['name']) : ['color' => '#2563eb', 'bg' => 'rgba(37,99,235,0.08)', 'border' => 'rgba(37,99,235,0.2)'];
                                $icon_color = isset($d_item['color']) ? $d_item['color'] : $cat_pal['color'];
                                $pill_bg    = isset($d_item['bg']) ? $d_item['bg'] : $cat_pal['bg'];
                                $pill_border= isset($d_item['border']) ? $d_item['border'] : $cat_pal['border'];
                            ?>
                                <li>
                                    <a href="<?php echo esc_url($d_item['url']); ?>" class="ht-nav-pill" style="--cat-color: <?php echo esc_attr($icon_color); ?>; --cat-bg: <?php echo esc_attr($pill_bg); ?>; --cat-border: <?php echo esc_attr($pill_border); ?>;">
                                        <span class="ht-nav-item-label"><?php echo esc_html($d_item['label']); ?></span>
                                    </a>
                                </li>
                            <?php endforeach; ?>
                        </ul>
                        <?php
                    }
                    ?>
                </nav>
                <button type="button" class="ht-nav-scroll-btn ht-nav-scroll-next" id="ht-nav-next" aria-label="<?php esc_attr_e('মেনু ডানে স্ক্রোল করুন', 'helptrickbd'); ?>">
                    <?php ht_m3_icon('keyboard_arrow_right', 18); ?>
                </button>
            </div>

            <!-- Action Controls (Search, Bookmarks, Theme Switcher) -->
            <div class="ht-header-actions">
                
                <?php if (get_theme_mod('ht_header_search_enable', true)) : ?>
                    <!-- Instant Search Trigger (Ctrl+K) -->
                    <button class="ht-search-btn" id="ht-search-trigger" aria-label="<?php esc_attr_e('অনুসন্ধান করুন (Ctrl+K)', 'helptrickbd'); ?>">
                        <?php ht_m3_icon('search', 20); ?>
                        <span class="ht-search-text"><?php esc_html_e('অনুসন্ধান...', 'helptrickbd'); ?></span>
                        <kbd class="ht-search-kbd">Ctrl+K</kbd>
                    </button>
                <?php endif; ?>

                <?php if (get_theme_mod('ht_header_bookmarks_enable', true)) : ?>
                    <!-- Saved Bookmarks Drawer Trigger -->
                    <button class="ht-action-btn ht-bookmarks-trigger" id="ht-bookmarks-trigger" aria-label="<?php esc_attr_e('পড়ার তালিকা (বুকমার্ক)', 'helptrickbd'); ?>" title="<?php esc_attr_e('পড়ার তালিকা', 'helptrickbd'); ?>">
                        <?php ht_m3_icon('bookmark', 20); ?>
                        <span class="ht-badge-count" id="ht-bookmark-badge">০</span>
                    </button>
                <?php endif; ?>

                <?php if (get_theme_mod('ht_header_theme_toggle_enable', true)) : ?>
                    <!-- Dark / Light Mode Switcher -->
                    <button class="ht-action-btn ht-theme-toggle" id="ht-theme-toggle" aria-label="<?php esc_attr_e('ডার্ক / লাইট মোড পরিবর্তন করুন', 'helptrickbd'); ?>" title="<?php esc_attr_e('থিম মোড পরিবর্তন', 'helptrickbd'); ?>">
                        <span class="ht-theme-icon-light"><?php ht_m3_icon('dark_mode', 20); ?></span>
                        <span class="ht-theme-icon-dark"><?php ht_m3_icon('light_mode', 20); ?></span>
                    </button>
                <?php endif; ?>

            </div>

        </div>
    </header>

    <!-- Mobile Drawer Navigation (Outside header so backdrop-filter does not trap overlay) -->
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
                <!-- Dynamic All Categories Engine (Entire Drawer dedicated to categories) -->
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
                            'exclude'    => [1], // Hide Uncategorized
                            'number'     => 0,   // Show all active categories
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
    <?php ht_render_ad('ht_ad_header', 'ht-container ht-ad-header-slot', 90); ?>

    <!-- Main Content Container Wrapper -->
    <div id="content" class="ht-site-content">
