<?php
/**
 * Sidebar Widget 4: Categories & Departments 2-Column Cards Grid
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

if (!get_theme_mod('ht_sidebar_cats_enable', true)) {
    return;
}

$sidebar_cats = get_categories(array(
    'orderby'    => 'count',
    'order'      => 'DESC',
    'hide_empty' => true,
));

if (empty($sidebar_cats)) {
    return;
}

$is_en = function_exists('ht_is_bangla_locale') && !ht_is_bangla_locale();
$widget_title = $is_en ? esc_html__('Topics & Departments', 'helptrickbd') : esc_html__('সকল বিষয় ও বিভাগ', 'helptrickbd');
?>
<div class="n-sidebar-cats-widget" aria-label="<?php echo esc_attr($widget_title); ?>" style="margin-top:16px;">
  <div class="n-sec-head" style="margin-top:0;margin-bottom:10px;">
    <h3 style="font-size:1.15rem;"><?php echo esc_html($widget_title); ?></h3>
    <span class="rule" aria-hidden="true"></span>
  </div>

  <div class="n-cats-grid-2col">
    <?php
    foreach ($sidebar_cats as $cat) :
        if ($cat->slug === 'uncategorized' || (int) $cat->count === 0) {
            continue;
        }
        ?>
        <a href="<?php echo esc_url(get_category_link($cat->term_id)); ?>" class="n-cat-card">
          <span class="n-cat-name"><?php echo esc_html($cat->name); ?></span>
          <span class="n-cat-count"><?php echo esc_html(function_exists('ht_number') ? ht_number($cat->count) : (function_exists('ht_bn_number') ? ht_bn_number($cat->count) : $cat->count)); ?></span>
        </a>
        <?php
    endforeach;
    ?>
  </div>
</div>
