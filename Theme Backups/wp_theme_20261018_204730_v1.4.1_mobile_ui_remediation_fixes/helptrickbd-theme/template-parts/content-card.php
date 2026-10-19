<?php
/**
 * Template part for displaying posts in a card grid
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}
?>

<article id="post-<?php the_ID(); ?>" <?php post_class('ht-card'); ?>>
    <div class="ht-card-thumb-wrap">
        <a href="<?php the_permalink(); ?>">
            <?php ht_the_thumbnail(get_the_ID(), 'ht-card-thumb'); ?>
        </a>
        <button class="ht-card-bm-btn ht-bookmark-toggle" data-id="<?php the_ID(); ?>" data-title="<?php echo esc_attr(get_the_title()); ?>" data-url="<?php the_permalink(); ?>" aria-label="<?php esc_attr_e('Save to reading list', 'helptrickbd'); ?>">
            <?php ht_m3_icon('bookmark', 18); ?>
        </button>
        <div class="ht-card-cat-float">
            <?php ht_category_badge(); ?>
        </div>
    </div>

    <div class="ht-card-body">
        <h2 class="ht-card-title">
            <a href="<?php the_permalink(); ?>"><?php the_title(); ?></a>
        </h2>
        <p class="ht-card-excerpt">
            <?php echo esc_html(wp_trim_words(get_the_excerpt(), 18)); ?>
        </p>
        <div class="ht-card-footer">
            <div class="ht-card-author">
                <span class="ht-card-author-avatar">
                    <?php 
                    $card_author_id = get_the_author_meta('ID');
                    $card_avatar_url = function_exists('ht_get_author_avatar_url') ? ht_get_author_avatar_url($card_author_id) : '';
                    if (!empty($card_avatar_url)) : 
                    ?>
                        <img src="<?php echo esc_url($card_avatar_url); ?>" alt="<?php echo esc_attr(get_the_author()); ?>" class="ht-card-avatar-img" width="24" height="24" loading="lazy">
                    <?php else : ?>
                        <?php echo get_avatar($card_author_id, 24, '', esc_attr(get_the_author()), ['class' => 'ht-card-avatar-img']); ?>
                    <?php endif; ?>
                </span>
                <span class="ht-card-author-name"><?php the_author(); ?></span>
            </div>
            <div class="ht-card-meta-right">
                <?php ht_post_date(); ?>
                <?php ht_reading_time(); ?>
            </div>
        </div>
    </div>
</article>
