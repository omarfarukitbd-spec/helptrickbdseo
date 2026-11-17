<?php
/**
 * Offline Bookmarks Drawer Component
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}
?>

<div id="ht-bookmark-drawer" class="ht-drawer" aria-hidden="true" role="dialog" aria-modal="true" aria-label="<?php esc_attr_e('Saved Handnotes', 'helptrickbd-edu'); ?>">
  <div class="ht-drawer-overlay ht-bookmark-close"></div>
  <div class="ht-drawer-panel">
    <div class="ht-drawer-header">
      <div style="display:flex;align-items:center;gap:8px;">
        <?php htbd_icon('bookmark', array('width' => 20, 'height' => 20)); ?>
        <h3 class="ht-drawer-title" style="margin:0;font-size:1.15rem;font-weight:800;">
          <?php esc_html_e('Saved Handnotes', 'helptrickbd-edu'); ?>
        </h3>
      </div>
      <button type="button" class="ht-icon-btn ht-bookmark-close" aria-label="<?php esc_attr_e('Close', 'helptrickbd-edu'); ?>">
        <?php htbd_icon('close', array('width' => 18, 'height' => 18)); ?>
      </button>
    </div>

    <div class="ht-drawer-body">
      <div id="ht-bookmark-items" class="ht-bookmark-drawer-list">
        <!-- Injected via JavaScript from localStorage -->
      </div>
      <div id="ht-bookmark-empty" style="text-align:center;padding:40px 16px;color:var(--ht-text-muted);">
        <div style="font-size:2.5rem;margin-bottom:8px;" aria-hidden="true">🔖</div>
        <p style="font-size:0.95rem;line-height:1.6;margin:0;">
          <?php esc_html_e('You have not bookmarked any handnotes yet. Click the bookmark icon on any article to save it for quick offline study.', 'helptrickbd-edu'); ?>
        </p>
      </div>
    </div>

    <div class="ht-drawer-footer" style="justify-content:space-between;align-items:center;">
      <span style="font-size:0.8rem;color:var(--ht-text-muted);">
        <?php esc_html_e('Saved locally on this device', 'helptrickbd-edu'); ?>
      </span>
      <button type="button" id="ht-clear-bookmarks" class="ht-btn" style="background:transparent;border:1px solid var(--ht-border);padding:4px 10px;font-size:0.75rem;border-radius:var(--ht-radius-sm);cursor:pointer;color:var(--ht-accent);">
        <?php esc_html_e('Clear All', 'helptrickbd-edu'); ?>
      </button>
    </div>
  </div>
</div>
