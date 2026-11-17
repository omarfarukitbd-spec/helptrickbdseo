<?php
/**
 * Single Article Author & Metadata Component
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}

$ht_author_id   = (int) get_the_author_meta('ID');
$ht_author_name = get_the_author_meta('display_name', $ht_author_id);
$ht_author_url  = get_author_posts_url($ht_author_id);
?>
<div class="ht-single-meta">
  <div class="ht-author-box" itemprop="author" itemscope itemtype="https://schema.org/Person">
    <meta itemprop="name" content="<?php echo esc_attr($ht_author_name); ?>">
    <link itemprop="url" href="<?php echo esc_url($ht_author_url); ?>">
    <?php htbd_author_badge($ht_author_id); ?>
  </div>

  <div class="ht-date-read">
    <span class="ht-meta-item">
      <?php htbd_icon('calendar', array('width' => 14, 'height' => 14)); ?>
      <time class="entry-date published" itemprop="datePublished" datetime="<?php echo esc_attr(get_the_date(DATE_W3C)); ?>"><?php echo esc_html(get_the_date('j F, Y')); ?></time>
      <meta itemprop="dateModified" content="<?php echo esc_attr(get_the_modified_date(DATE_W3C)); ?>">
    </span>

    <span class="ht-meta-item">
      <?php htbd_icon('clock', array('width' => 14, 'height' => 14)); ?>
      <span><?php echo esc_html(htbd_reading_time()); ?></span>
    </span>

    <button type="button" class="ht-bookmark-btn" data-post-id="<?php the_ID(); ?>" data-post-title="<?php echo esc_attr(get_the_title()); ?>" data-post-url="<?php echo esc_url(get_permalink()); ?>" aria-label="<?php esc_attr_e('Bookmark this handnote', 'helptrickbd-edu'); ?>" title="<?php esc_attr_e('Save Handnote', 'helptrickbd-edu'); ?>">
      <?php htbd_icon('bookmark', array('width' => 16, 'height' => 16)); ?>
    </button>
  </div>
</div>
