<?php
/**
 * Single Post Component: Tags Cloud
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

$tags = get_the_tags();
if ($tags) :
?>
    <div class="ht-tags-list" aria-label="<?php esc_attr_e('বিষয়ভিত্তিক ট্যাগসমূহ', 'helptrickbd'); ?>">
        <span class="ht-tags-label"><?php esc_html_e('ট্যাগ:', 'helptrickbd'); ?></span>
        <?php foreach ($tags as $tag) : ?>
            <a href="<?php echo esc_url(get_tag_link($tag->term_id)); ?>" class="ht-tag-chip">
                #<?php echo esc_html($tag->name); ?>
            </a>
        <?php endforeach; ?>
    </div>
<?php endif; ?>
