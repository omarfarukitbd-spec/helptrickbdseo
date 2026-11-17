<?php
/**
 * Template part for displaying standard posts
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}
?>

<article id="post-<?php the_ID(); ?>" <?php post_class('ht-standard-post'); ?>>
    <header class="ht-entry-header">
        <?php
        if (is_singular()) :
            the_title('<h1 class="ht-entry-title">', '</h1>');
        else :
            the_title('<h2 class="ht-entry-title"><a href="' . esc_url(get_permalink()) . '" rel="bookmark">', '</a></h2>');
        endif;
        ?>

        <div class="ht-entry-meta">
            <?php ht_post_date(); ?>
            <?php ht_reading_time(); ?>
            <?php ht_category_badge(); ?>
        </div>
    </header>

    <?php if (has_post_thumbnail() && !is_singular()) : ?>
        <div class="ht-post-thumbnail">
            <a href="<?php the_permalink(); ?>">
                <?php the_post_thumbnail('ht-card-thumb', ['class' => 'ht-thumbnail-img', 'loading' => 'lazy']); ?>
            </a>
        </div>
    <?php endif; ?>

    <div class="ht-entry-content">
        <?php
        if (is_singular()) :
            the_content();
            wp_link_pages([
                'before' => '<div class="page-links">' . esc_html__('Pages:', 'helptrickbd'),
                'after'  => '</div>',
            ]);
        else :
            the_excerpt();
        endif;
        ?>
    </div>
</article>
