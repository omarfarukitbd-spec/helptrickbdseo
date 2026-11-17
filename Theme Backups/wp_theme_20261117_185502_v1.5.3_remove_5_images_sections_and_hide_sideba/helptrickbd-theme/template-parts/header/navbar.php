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

$nav_home_text = get_theme_mod('htbd_nav_home_text', get_theme_mod('ht_nav_home_text', 'মূল পাতা'));
if (empty($nav_home_text) || $nav_home_text === 'All Posts') {
    $nav_home_text = 'মূল পাতা';
}
?>
<div class="n-navwrap">
  <div class="ht-container">
    <nav class="n-nav-inner" aria-label="<?php esc_attr_e('মূল নেভিগেশন মেনু', 'helptrickbd'); ?>">
      <!-- Mobile Drawer Toggle Button -->
      <button type="button" id="ht-drawer-toggle" class="n-mobile-toggle" aria-label="<?php esc_attr_e('মেনু খুলুন', 'helptrickbd'); ?>">
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
            <?php foreach ($categories as $cat) : ?>
              <span class="n-nav-sep" aria-hidden="true">|</span>
              <a href="<?php echo esc_url(get_category_link($cat->term_id)); ?>" class="n-nav-item">
                <?php echo esc_html($cat->name); ?>
              </a>
            <?php endforeach; ?>
          <?php endif; ?>
        <?php endif; ?>
      </div>
    </nav>
  </div>
</div>
