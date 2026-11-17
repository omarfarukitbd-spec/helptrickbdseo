<?php
/**
 * Off-Canvas Mobile Drawer Component
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}

$categories = get_categories(array(
    'orderby'    => 'count',
    'order'      => 'DESC',
    'number'     => 12,
    'hide_empty' => false,
));
?>
<div id="ht-mobile-drawer" class="ht-drawer" role="dialog" aria-modal="true" aria-label="<?php esc_attr_e('Mobile Menu', 'helptrickbd-edu'); ?>">
  <div class="ht-drawer-backdrop" id="ht-drawer-backdrop"></div>
  <div class="ht-drawer-panel">
    <div class="ht-drawer-header">
      <div class="ht-drawer-brand">
        <span class="ht-drawer-logo">HelpTrickBD</span>
        <span class="ht-drawer-sub">HELPTRICKBD.COM</span>
      </div>
      <button type="button" id="ht-drawer-close" class="ht-icon-btn" aria-label="<?php esc_attr_e('Close Menu', 'helptrickbd-edu'); ?>">
        <?php htbd_icon('close', array('width' => 20, 'height' => 20)); ?>
      </button>
    </div>

    <div class="ht-drawer-body">
      <div class="ht-drawer-section-title"><?php esc_html_e('Categories & Departments', 'helptrickbd-edu'); ?></div>
      <ul class="ht-drawer-menu">
        <li>
          <a href="<?php echo esc_url(home_url('/')); ?>">
            <?php htbd_icon('book', array('width' => 16, 'height' => 16)); ?>
            <span><?php esc_html_e('Home / All Posts', 'helptrickbd-edu'); ?></span>
          </a>
        </li>
        <?php if (!empty($categories)) : ?>
          <?php foreach ($categories as $cat) : ?>
            <li>
              <a href="<?php echo esc_url(get_category_link($cat->term_id)); ?>">
                <?php htbd_icon('graduation-cap', array('width' => 16, 'height' => 16)); ?>
                <span><?php echo esc_html($cat->name); ?></span>
                <span class="ht-drawer-count"><?php echo esc_html($cat->count); ?></span>
              </a>
            </li>
          <?php endforeach; ?>
        <?php endif; ?>
      </ul>
    </div>

    <div class="ht-drawer-footer">
      <a href="<?php echo esc_url(home_url('/about-us/')); ?>"><?php esc_html_e('About Us', 'helptrickbd-edu'); ?></a>
      <a href="<?php echo esc_url(home_url('/contact-us/')); ?>"><?php esc_html_e('Contact Us', 'helptrickbd-edu'); ?></a>
      <a href="<?php echo esc_url(home_url('/privacy-policy/')); ?>"><?php esc_html_e('Privacy Policy', 'helptrickbd-edu'); ?></a>
    </div>
  </div>
</div>
