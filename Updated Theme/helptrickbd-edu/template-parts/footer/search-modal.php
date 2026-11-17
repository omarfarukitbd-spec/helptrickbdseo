<?php
/**
 * Fullscreen Search Modal Component
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}
?>
<div id="ht-search-modal" class="ht-search-modal" role="dialog" aria-modal="true" aria-label="<?php esc_attr_e('Search', 'helptrickbd-edu'); ?>">
  <div class="ht-search-backdrop ht-search-trigger"></div>
  <div class="ht-search-dialog">
    <div class="ht-search-header">
      <h3 class="ht-search-title"><?php esc_html_e('Search Articles & Handnotes', 'helptrickbd-edu'); ?></h3>
      <button type="button" id="ht-search-close" class="ht-icon-btn" aria-label="<?php esc_attr_e('Close', 'helptrickbd-edu'); ?>">
        <?php htbd_icon('close', array('width' => 20, 'height' => 20)); ?>
      </button>
    </div>

    <form role="search" method="get" class="ht-search-form" action="<?php echo esc_url(home_url('/')); ?>">
      <div class="ht-search-input-wrap">
        <?php htbd_icon('search', array('class' => 'ht-search-field-icon', 'width' => 20, 'height' => 20)); ?>
        <input type="search" id="ht-search-input" class="ht-search-field" placeholder="<?php esc_attr_e('Search topics, subjects, questions... (e.g. Political Science, SSC)', 'helptrickbd-edu'); ?>" value="<?php echo get_search_query(); ?>" name="s" autocomplete="off">
        <button type="submit" class="ht-btn ht-btn-primary"><?php esc_html_e('Search', 'helptrickbd-edu'); ?></button>
      </div>
    </form>

    <!-- Live AJAX Search Suggestions Container -->
    <div id="ht-live-search-results" class="ht-live-search-results" style="display:none;" aria-live="polite"></div>

    <div class="ht-search-hints">
      <span><?php esc_html_e('Popular Searches:', 'helptrickbd-edu'); ?></span>
      <a href="<?php echo esc_url(home_url('/?s=Political+Science')); ?>">Political Science</a>
      <a href="<?php echo esc_url(home_url('/?s=SSC+Dakhil')); ?>">SSC & Dakhil</a>
      <a href="<?php echo esc_url(home_url('/?s=National+University')); ?>">National University</a>
      <a href="<?php echo esc_url(home_url('/?s=English+Grammar')); ?>">English Grammar</a>
    </div>
  </div>
</div>
