<?php
/**
 * Single Post Component: Article Main Content & Pagination
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}
?>
<!-- Article Main Content -->
<div class="ht-article-content ht-entry-content" id="ht-article-body">
    <?php
    the_content();

    wp_link_pages([
        'before'      => '<div class="ht-page-links"><span class="ht-page-links-title">' . esc_html__('পৃষ্ঠাসমূহ:', 'helptrickbd') . '</span>',
        'after'       => '</div>',
        'link_before' => '<span class="ht-page-number">',
        'link_after'  => '</span>',
    ]);
    ?>
</div>
