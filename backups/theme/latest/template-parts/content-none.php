<?php
/**
 * Template part for displaying a message that posts cannot be found
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}
?>

<div class="ht-empty-state">
    <?php ht_m3_icon('search', 48, 'ht-empty-icon'); ?>
    <h3 class="ht-empty-title">
        <?php
        if (is_search()) :
            esc_html_e('No Results Found', 'helptrickbd');
        else :
            esc_html_e('Nothing Found', 'helptrickbd');
        endif;
        ?>
    </h3>
    <p class="ht-empty-desc">
        <?php
        if (is_home() && current_user_can('publish_posts')) :
            printf(
                wp_kses(
                    /* translators: 1: link to WP admin new post page. */
                    __('Ready to publish your first post? <a href="%1$s">Get started here</a>.', 'helptrickbd'),
                    ['a' => ['href' => []]]
                ),
                esc_url(admin_url('post-new.php'))
            );
        elseif (is_search()) :
            esc_html_e('Sorry, but nothing matched your search terms. Please try again with some different keywords.', 'helptrickbd');
        else :
            esc_html_e('It seems we cannot find what you are looking for. Perhaps searching can help.', 'helptrickbd');
        endif;
        ?>
    </p>

    <div class="ht-empty-search-box">
        <?php get_search_form(); ?>
    </div>
</div>
