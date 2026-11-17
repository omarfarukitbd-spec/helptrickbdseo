<?php
/**
 * Single Post Component: Article Header (Badges, Title, Meta, Freshness, Share, Toolbelt, Ad & TOC)
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}
?>
<!-- Article Header -->
<header class="ht-article-header">
    <div class="ht-header-top-badges">
        <?php ht_category_badge(); ?>
        <?php ht_eeat_badge(); ?>
    </div>

    <h1 class="ht-article-title"><?php the_title(); ?></h1>

    <div class="ht-article-meta-row">
        <!-- Date, Reading Time, Views -->
        <div class="ht-meta-stats">
            <?php ht_post_date(); ?>
            <?php ht_reading_time(); ?>
            <?php ht_post_views(); ?>
        </div>
    </div>

    <!-- Dynamic Last Updated Freshness Signal -->
    <?php ht_last_updated(); ?>

    <!-- Social Share Pills (Top) -->
    <?php ht_social_share_bar('top'); ?>

    <!-- Student Reading Toolbelt -->
    <?php get_template_part('template-parts/single/reading-toolbelt'); ?>

    <!-- Ad Slot Below Title -->
    <?php ht_render_ad('ht_ad_below_title', 'ht-ad-single-top', 250); ?>

    <!-- Auto Table of Contents (সূচিপত্র) Container -->
    <?php get_template_part('template-parts/single/toc'); ?>

</header>
