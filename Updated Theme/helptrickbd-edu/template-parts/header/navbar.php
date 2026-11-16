<?php
/**
 * Header Navigation Component (Sticky Newspaper Nav, Category Pills, Search Pill, Mobile Toggle)
 *
 * @package HelpTrickBD_EduPortal
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
?>
<div class="n-navwrap">
  <div class="ht-container">
    <nav class="n-nav-inner" aria-label="<?php esc_attr_e('প্রধান ন্যাভিগেশন', 'helptrickbd-edu'); ?>">
      <!-- Mobile Drawer Toggle Button -->
      <button type="button" id="ht-drawer-toggle" class="n-mobile-toggle" aria-label="<?php esc_attr_e('মেনু খুলুন', 'helptrickbd-edu'); ?>">
        <?php htbd_icon('menu', array('width' => 22, 'height' => 22)); ?>
      </button>

      <!-- Category Pill Track (Horizontal Touch Scrollable with | Dividers) -->
      <div class="n-nav-track">
        <a href="<?php echo esc_url(home_url('/')); ?>" class="n-nav-item <?php echo is_front_page() ? 'active' : ''; ?>">
          <?php echo esc_html(get_theme_mod('htbd_nav_home_text', 'All Posts')); ?>
        </a>

        <?php if (has_nav_menu('primary-nav')) : ?>
          <?php
          wp_nav_menu(array(
              'theme_location' => 'primary-nav',
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
