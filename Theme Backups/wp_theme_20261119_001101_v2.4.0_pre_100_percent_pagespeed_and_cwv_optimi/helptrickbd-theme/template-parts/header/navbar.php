<?php
/**
 * Header Navigation Component (Sticky Newspaper Nav, Category Pills, Search Pill, Mobile Toggle)
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

$categories = get_categories(array(
    'orderby'    => 'count',
    'order'      => 'DESC',
    'number'     => 10,
    'hide_empty' => false,
));

$nav_home_text = get_theme_mod('htbd_nav_home_text', get_theme_mod('ht_nav_home_text', ''));
if (function_exists('ht_is_bangla_locale') && !ht_is_bangla_locale()) {
    $nav_home_text = (!empty($nav_home_text) && $nav_home_text !== 'মূল পাতা') ? $nav_home_text : esc_html__('Home', 'helptrickbd');
} else {
    $nav_home_text = !empty($nav_home_text) ? $nav_home_text : esc_html__('মূল পাতা', 'helptrickbd');
}
?>
<div class="n-navwrap">
  <div class="ht-container">
    <nav class="n-nav-inner" aria-label="<?php echo (function_exists('ht_is_bangla_locale') && !ht_is_bangla_locale()) ? esc_attr__('Primary Navigation', 'helptrickbd') : esc_attr__('মূল নেভিগেশন মেনু', 'helptrickbd'); ?>">
      <!-- Mobile Drawer Toggle Button -->
      <button type="button" id="ht-drawer-toggle" class="n-mobile-toggle" aria-label="<?php echo (function_exists('ht_is_bangla_locale') && !ht_is_bangla_locale()) ? esc_attr__('Open Menu', 'helptrickbd') : esc_attr__('মেনু খুলুন', 'helptrickbd'); ?>">
        <?php htbd_icon('menu', array('width' => 22, 'height' => 22)); ?>
      </button>

      <!-- Category Pill Track (Horizontal Touch Scrollable with | Dividers) -->
      <div class="n-nav-track">
        <a href="<?php echo esc_url(home_url('/')); ?>" class="n-nav-item <?php echo is_front_page() ? 'active' : ''; ?>">
          <?php echo esc_html($nav_home_text); ?>
        </a>

        <?php if (has_nav_menu('primary-menu') || has_nav_menu('primary-nav')) : ?>
          <?php
          $menu_location = has_nav_menu('primary-menu') ? 'primary-menu' : 'primary-nav';
          wp_nav_menu(array(
              'theme_location' => $menu_location,
              'container'      => false,
              'items_wrap'     => '%3$s',
              'fallback_cb'    => false,
              'depth'          => 1,
          ));
          ?>
        <?php else : ?>
          <?php if (!empty($categories)) : ?>
            <?php
            $primary_cats  = array_slice($categories, 0, 7);
            $overflow_cats = array_slice($categories, 7);
            ?>
            <?php foreach ($primary_cats as $cat) : ?>
              <span class="n-nav-sep" aria-hidden="true">|</span>
              <a href="<?php echo esc_url(get_category_link($cat->term_id)); ?>" class="n-nav-item">
                <?php echo esc_html(function_exists('ht_get_localized_term_name') ? ht_get_localized_term_name($cat) : $cat->name); ?>
              </a>
            <?php endforeach; ?>

            <?php if (!empty($overflow_cats)) : ?>
              <span class="n-nav-sep" aria-hidden="true">|</span>
              <div class="n-nav-more-wrapper">
                <button type="button" class="n-nav-item n-nav-more-btn" aria-haspopup="true" aria-expanded="false">
                  <span><?php echo (function_exists('ht_is_bangla_locale') && !ht_is_bangla_locale()) ? esc_html__('More', 'helptrickbd') : esc_html__('আরও বিষয়', 'helptrickbd'); ?></span>
                  <span class="n-more-arrow" aria-hidden="true">&#9662;</span>
                </button>
                <div class="n-nav-more-menu" role="menu">
                  <?php foreach ($overflow_cats as $ocat) : ?>
                    <a href="<?php echo esc_url(get_category_link($ocat->term_id)); ?>" class="n-nav-more-item" role="menuitem">
                      <?php echo esc_html(function_exists('ht_get_localized_term_name') ? ht_get_localized_term_name($ocat) : $ocat->name); ?>
                    </a>
                  <?php endforeach; ?>
                </div>
              </div>
            <?php endif; ?>
          <?php endif; ?>
        <?php endif; ?>
      </div>
    </nav>
  </div>
</div>
