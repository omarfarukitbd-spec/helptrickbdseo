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
    $is_en = function_exists('ht_is_bangla_locale') && !ht_is_bangla_locale();
    $tags_label = $is_en ? esc_html__('Tags:', 'helptrickbd') : esc_html__('ট্যাগ:', 'helptrickbd');
    $tags_aria  = $is_en ? esc_attr__('Article Tags', 'helptrickbd') : esc_attr__('বিষয়ভিত্তিক ট্যাগসমূহ', 'helptrickbd');
?>
    <div class="ht-tags-list" aria-label="<?php echo esc_attr($tags_aria); ?>">
        <span class="ht-tags-label"><?php echo esc_html($tags_label); ?></span>
        <?php foreach ($tags as $tag) : ?>
            <a href="<?php echo esc_url(get_tag_link($tag->term_id)); ?>" class="ht-tag-chip">
                #<?php echo esc_html($tag->name); ?>
            </a>
        <?php endforeach; ?>
    </div>
<?php endif; ?>
