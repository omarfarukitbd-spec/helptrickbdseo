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
    <style id="ht-critical-theme-overrides">
        /* HelpTrickBD Pro Critical Styles & Responsive Layout Overrides */
        @media (min-width: 992px) {
            .ht-menu-toggle,
            #ht-menu-toggle {
                display: none !important;
                visibility: hidden !important;
                pointer-events: none !important;
            }
        }
        @media (max-width: 991px) {
            .ht-menu-toggle,
            #ht-menu-toggle {
                display: inline-flex !important;
                visibility: visible !important;
                pointer-events: auto !important;
            }
        }
        /* Mobile Drawer Section Header */
        .ht-drawer-section-header {
            display: flex !important;
            flex-direction: row !important;
            align-items: center !important;
            justify-content: space-between !important;
            width: 100% !important;
            margin-bottom: 12px !important;
            padding-bottom: 8px !important;
            border-bottom: 1px solid var(--ht-surface-border) !important;
            box-sizing: border-box !important;
        }
        .ht-drawer-section-title {
            font-size: 0.76rem !important;
            font-weight: 700 !important;
            text-transform: uppercase !important;
            letter-spacing: 0.8px !important;
            color: var(--ht-text-muted) !important;
            margin: 0 !important;
            line-height: 1 !important;
            display: inline-block !important;
        }
        .ht-drawer-cat-total {
            display: inline-flex !important;
            align-items: center !important;
            justify-content: center !important;
            font-size: 0.72rem !important;
            font-weight: 700 !important;
            background: var(--ht-surface-hover) !important;
            border: 1px solid var(--ht-surface-border) !important;
            padding: 2px 8px !important;
            border-radius: 9999px !important;
            line-height: 1.2 !important;
            color: var(--ht-text-muted) !important;
            margin: 0 !important;
        }
        /* Hero Lead Card (Magazine / Newspaper Stacked Layout - No Overlay Clash) */
        .ht-hero-lead-card {
            display: flex !important;
            flex-direction: column !important;
            height: auto !important;
            position: relative !important;
            background: var(--ht-surface-card) !important;
            border: 1px solid var(--ht-surface-border) !important;
            border-radius: var(--ht-radius-lg) !important;
            overflow: hidden !important;
            box-shadow: var(--ht-shadow-sm) !important;
            box-sizing: border-box !important;
            transition: var(--ht-transition) !important;
        }
        .ht-hero-lead-card:hover {
            transform: translateY(-2px) !important;
            box-shadow: var(--ht-shadow-md) !important;
            border-color: var(--ht-primary-light, rgba(37, 99, 235, 0.3)) !important;
        }
        .ht-hero-lead-thumb-wrap {
            display: block !important;
            width: 100% !important;
            height: auto !important;
            position: relative !important;
            overflow: hidden !important;
            aspect-ratio: 16 / 9 !important;
            background: var(--ht-surface-hover) !important;
            flex-shrink: 0 !important;
        }
        .ht-hero-lead-img {
            width: 100% !important;
            height: 100% !important;
            object-fit: cover !important;
            display: block !important;
            transition: transform 0.4s ease !important;
        }
        .ht-hero-lead-card:hover .ht-hero-lead-img {
            transform: scale(1.03) !important;
        }
        .ht-hero-gradient {
            display: none !important;
        }
        .ht-hero-lead-body,
        .ht-hero-lead-overlay {
            padding: 16px 18px 18px !important;
            display: flex !important;
            flex-direction: column !important;
            flex: 1 1 auto !important;
            justify-content: space-between !important;
            box-sizing: border-box !important;
            position: static !important;
            background: transparent !important;
        }
        .ht-hero-lead-title {
            font-size: 1.25rem !important;
            font-weight: 700 !important;
            line-height: 1.45 !important;
            margin: 0 0 10px 0 !important;
            display: -webkit-box !important;
            -webkit-line-clamp: 2 !important;
            -webkit-box-orient: vertical !important;
            overflow: hidden !important;
        }
        .ht-hero-lead-title a,
        .ht-hero-title,
        .ht-hero-title a {
            color: var(--ht-text-primary) !important;
            text-shadow: none !important;
            text-decoration: none !important;
            transition: color 0.2s ease !important;
        }
        .ht-hero-lead-title a:hover {
            color: var(--ht-primary) !important;
        }
        .ht-hero-lead-excerpt,
        .ht-hero-excerpt {
            font-size: 0.88rem !important;
            color: var(--ht-text-secondary) !important;
            line-height: 1.55 !important;
            text-shadow: none !important;
            margin: 0 0 12px 0 !important;
            display: -webkit-box !important;
            -webkit-line-clamp: 2 !important;
            -webkit-box-orient: vertical !important;
            overflow: hidden !important;
        }
        .ht-hero-lead-card .ht-card-meta {
            display: flex !important;
            align-items: center !important;
            gap: 12px !important;
            font-size: 0.80rem !important;
            color: var(--ht-text-muted) !important;
            margin-top: auto !important;
            padding-top: 10px !important;
            border-top: 1px solid var(--ht-surface-border) !important;
            flex-wrap: wrap !important;
        }
        .ht-hero-author {
            display: inline-flex !important;
            align-items: center !important;
            gap: 6px !important;
            font-weight: 600 !important;
            color: var(--ht-text-primary) !important;
        }
        .ht-hero-author-avatar-badge {
            display: inline-flex !important;
            align-items: center !important;
            justify-content: center !important;
            width: 20px !important;
            height: 20px !important;
            border-radius: 50% !important;
            background: var(--ht-surface-hover) !important;
            border: 1px solid var(--ht-surface-border) !important;
            color: var(--ht-primary) !important;
            flex-shrink: 0 !important;
            margin-right: 6px !important;
            vertical-align: middle !important;
        }
        .ht-hero-author-avatar-badge svg {
            width: 13px !important;
            height: 13px !important;
            fill: currentColor !important;
            display: block !important;
        }
        /* Hero 1+3 Grid Balanced Height */
        .ht-hero-grid {
            display: grid !important;
            grid-template-columns: 1.4fr 1fr !important;
            gap: 20px !important;
            align-items: stretch !important;
        }
        .ht-hero-sub-grid {
            display: flex !important;
            flex-direction: column !important;
            justify-content: space-between !important;
            gap: 14px !important;
            height: 100% !important;
        }
        .ht-hero-sub-card {
            display: flex !important;
            gap: 14px !important;
            background: var(--ht-surface-card) !important;
            border: 1px solid var(--ht-surface-border) !important;
            border-radius: var(--ht-radius-md) !important;
            padding: 12px !important;
            flex: 1 1 0 !important;
            min-height: 0 !important;
            box-sizing: border-box !important;
        }
        @media (max-width: 991px) {
            .ht-hero-grid {
                grid-template-columns: 1fr !important;
                gap: 20px !important;
            }
            .ht-hero-sub-grid {
                flex-direction: column !important;
                height: auto !important;
                gap: 14px !important;
            }
            .ht-hero-sub-card {
                height: auto !important;
                min-height: 100px !important;
                flex: auto !important;
            }
        }
        /* 4-Column Multi-Category Grid */
        .ht-multi-cat-grid {
            display: grid !important;
            grid-template-columns: repeat(4, minmax(0, 1fr)) !important;
            gap: 20px !important;
            width: 100% !important;
        }
        .ht-multi-cat-col {
            min-width: 0 !important;
            width: 100% !important;
            overflow: hidden !important;
            box-sizing: border-box !important;
        }
        @media (max-width: 1024px) {
            .ht-multi-cat-grid {
                grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
                gap: 18px !important;
            }
        }
        @media (max-width: 640px) {
            .ht-multi-cat-grid {
                grid-template-columns: 1fr !important;
                gap: 16px !important;
            }
        }
        /* Mobile Drawer Overlay Guarantee */
        .ht-drawer-overlay {
            position: fixed !important;
            inset: 0 !important;
            width: 100vw !important;
            height: 100vh !important;
            background: rgba(15, 23, 42, 0.6) !important;
            backdrop-filter: blur(2px) !important;
            -webkit-backdrop-filter: blur(2px) !important;
            z-index: 10000 !important;
            cursor: pointer !important;
            touch-action: auto !important;
        }
        .ht-drawer-overlay.ht-open {
            display: block !important;
        }
        .ht-mobile-drawer {
            z-index: 10001 !important;
        }
    </style>
</head>

<body <?php body_class(); ?>>
<?php wp_body_open(); ?>

<!-- Skip to content for accessibility -->
<a class="skip-link screen-reader-text" href="#primary"><?php esc_html_e('Skip to content', 'helptrickbd'); ?></a>

<div id="page" class="ht-site-wrapper">

    <!-- Top Bar: Breaking Notice, Countdown & Date -->
    <aside class="ht-topbar" aria-label="<?php esc_attr_e('Notice and time ticker', 'helptrickbd'); ?>">
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
                                            <span class="ht-ticker-title"><?php the_title(); ?></span>
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
                        <button type="button" class="ht-ticker-ctrl-btn" id="ht-ticker-prev" aria-label="<?php esc_attr_e('Previous notice', 'helptrickbd'); ?>" title="<?php esc_attr_e('Previous notice', 'helptrickbd'); ?>">
                            <?php ht_m3_icon('keyboard_arrow_left', 16); ?>
                        </button>
                        <button type="button" class="ht-ticker-ctrl-btn" id="ht-ticker-next" aria-label="<?php esc_attr_e('Next notice', 'helptrickbd'); ?>" title="<?php esc_attr_e('Next notice', 'helptrickbd'); ?>">
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
            <button class="ht-menu-toggle" id="ht-menu-toggle" aria-label="<?php esc_attr_e('Explore All Categories & Menu', 'helptrickbd'); ?>" title="<?php esc_attr_e('Explore All Categories & Menu', 'helptrickbd'); ?>" aria-expanded="false">
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
                        <span class="ht-logo-tagline"><?php esc_html_e('Education & Technology Resource Portal', 'helptrickbd'); ?></span>
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
                <button type="button" class="ht-nav-scroll-btn ht-nav-scroll-prev" id="ht-nav-prev" aria-label="<?php esc_attr_e('Scroll navigation left', 'helptrickbd'); ?>" style="display: none;">
                    <?php ht_m3_icon('keyboard_arrow_left', 18); ?>
                </button>
                <nav id="site-navigation" class="ht-nav" aria-label="<?php esc_attr_e('Primary Navigation', 'helptrickbd'); ?>">
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
                            ['url' => home_url('/'), 'label' => __('Home', 'helptrickbd'), 'slug' => 'home', 'name' => 'Home', 'color' => '#2563eb', 'bg' => 'rgba(37,99,235,0.08)', 'border' => 'rgba(37,99,235,0.2)'],
                            ['url' => home_url('/category/education-guide/'), 'label' => __('Education Guide', 'helptrickbd'), 'slug' => 'education-guide', 'name' => 'Education Guide'],
                            ['url' => home_url('/category/national-university/'), 'label' => __('National University', 'helptrickbd'), 'slug' => 'national-university', 'name' => 'National University'],
                            ['url' => home_url('/category/ssc-dakhil/'), 'label' => __('SSC & Dakhil', 'helptrickbd'), 'slug' => 'ssc-dakhil', 'name' => 'SSC & Dakhil'],
                            ['url' => home_url('/category/political-science/'), 'label' => __('Political Science', 'helptrickbd'), 'slug' => 'political-science', 'name' => 'Political Science'],
                            ['url' => home_url('/category/bangla-1st-paper/'), 'label' => __('Bangla', 'helptrickbd'), 'slug' => 'bangla-1st-paper', 'name' => 'Bangla'],
                            ['url' => home_url('/category/islamic-article/'), 'label' => __('Islamic Article', 'helptrickbd'), 'slug' => 'islamic-article', 'name' => 'Islamic Article'],
                            ['url' => home_url('/category/english-2nd-paper/'), 'label' => __('English', 'helptrickbd'), 'slug' => 'english-2nd-paper', 'name' => 'English'],
                            ['url' => home_url('/category/ict-technology/'), 'label' => __('ICT & Tech', 'helptrickbd'), 'slug' => 'ict-technology', 'name' => 'ICT & Tech'],
                            ['url' => home_url('/category/job-preparation/'), 'label' => __('Job Preparation', 'helptrickbd'), 'slug' => 'job-preparation', 'name' => 'Job Preparation'],
                            ['url' => home_url('/category/university-admission/'), 'label' => __('Admission', 'helptrickbd'), 'slug' => 'university-admission', 'name' => 'Admission'],
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
                <button type="button" class="ht-nav-scroll-btn ht-nav-scroll-next" id="ht-nav-next" aria-label="<?php esc_attr_e('Scroll navigation right', 'helptrickbd'); ?>">
                    <?php ht_m3_icon('keyboard_arrow_right', 18); ?>
                </button>
            </div>

            <!-- Action Controls (Search, Bookmarks, Theme Switcher) -->
            <div class="ht-header-actions">
                
                <?php if (get_theme_mod('ht_header_search_enable', true)) : ?>
                    <!-- Instant Search Trigger (Ctrl+K) -->
                    <button class="ht-search-btn" id="ht-search-trigger" aria-label="<?php esc_attr_e('Search (Ctrl+K)', 'helptrickbd'); ?>">
                        <?php ht_m3_icon('search', 20); ?>
                        <span class="ht-search-text"><?php esc_html_e('Search...', 'helptrickbd'); ?></span>
                        <kbd class="ht-search-kbd">Ctrl+K</kbd>
                    </button>
                <?php endif; ?>

                <?php if (get_theme_mod('ht_header_bookmarks_enable', true)) : ?>
                    <!-- Saved Bookmarks Drawer Trigger -->
                    <button class="ht-action-btn ht-bookmarks-trigger" id="ht-bookmarks-trigger" aria-label="<?php esc_attr_e('Reading List (Bookmarks)', 'helptrickbd'); ?>" title="<?php esc_attr_e('Reading List', 'helptrickbd'); ?>">
                        <?php ht_m3_icon('bookmark', 20); ?>
                        <span class="ht-badge-count" id="ht-bookmark-badge">0</span>
                    </button>
                <?php endif; ?>

                <?php if (get_theme_mod('ht_header_theme_toggle_enable', true)) : ?>
                    <!-- Dark / Light Mode Switcher -->
                    <button class="ht-action-btn ht-theme-toggle" id="ht-theme-toggle" aria-label="<?php esc_attr_e('Toggle Dark / Light Mode', 'helptrickbd'); ?>" title="<?php esc_attr_e('Toggle Theme', 'helptrickbd'); ?>">
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
                <button class="ht-drawer-close" id="ht-drawer-close" aria-label="<?php esc_attr_e('Close Menu', 'helptrickbd'); ?>">
                    <?php ht_m3_icon('close', 20); ?>
                </button>
            </div>
            
            <div class="ht-mobile-drawer-body">
                <!-- Dynamic All Categories Engine (Entire Drawer dedicated to categories) -->
                <div class="ht-drawer-categories-wrap">
                    <div class="ht-drawer-section-header">
                        <span class="ht-drawer-section-title"><?php esc_html_e('সকল ক্যাটাগরি', 'helptrickbd'); ?></span>
                        <?php 
                        $cat_count_total = wp_count_terms(['taxonomy' => 'category', 'hide_empty' => true]);
                        if (!is_wp_error($cat_count_total) && $cat_count_total > 0) :
                        ?>
                            <span class="ht-drawer-cat-total"><?php echo esc_html($cat_count_total); ?></span>
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
                                $cat_icon = function_exists('ht_get_category_icon') ? ht_get_category_icon($d_cat->slug, $d_cat->name) : 'folder';
                                $cat_pal  = function_exists('ht_get_category_palette') ? ht_get_category_palette($d_cat->slug, $d_cat->name) : ['color' => '#2563eb', 'bg' => 'rgba(37,99,235,0.08)', 'border' => 'rgba(37,99,235,0.2)'];
                        ?>
                                <a href="<?php echo esc_url(get_category_link($d_cat->term_id)); ?>" 
                                   class="ht-drawer-cat-item"
                                   style="--cat-color: <?php echo esc_attr($cat_pal['color']); ?>; --cat-bg: <?php echo esc_attr($cat_pal['bg']); ?>; --cat-border: <?php echo esc_attr($cat_pal['border']); ?>;">
                                    <span class="ht-drawer-cat-icon"><?php ht_m3_icon($cat_icon, 18); ?></span>
                                    <span class="ht-drawer-cat-name"><?php echo esc_html($d_cat->name); ?></span>
                                    <span class="ht-drawer-cat-badge"><?php echo esc_html($d_cat->count); ?></span>
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
