<?php
/**
 * Single Article Content Component
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}
?>
<article id="post-<?php the_ID(); ?>" <?php post_class('ht-single-article'); ?>>
  <header class="ht-single-header">
    <div class="ht-single-category">
      <?php htbd_category_badge(get_the_ID(), 'ht-badge accent'); ?>
    </div>

    <h1 class="ht-single-title"><?php the_title(); ?></h1>

    <?php get_template_part('template-parts/single/meta-author'); ?>
  </header>

  <?php if (has_post_thumbnail()) : ?>
    <figure class="ht-single-banner">
      <?php
      the_post_thumbnail('ht-lead-banner', array(
          'loading'  => 'lazy',
          'decoding' => 'async',
          'width'    => 800,
          'height'   => 450,
          'alt'      => esc_attr(get_the_title()),
      ));
      ?>
    </figure>
  <?php endif; ?>

  <div class="ht-entry-content">
    <?php
    the_content();

    wp_link_pages(array(
        'before' => '<div class="page-links">' . esc_html__('পৃষ্ঠা:', 'helptrickbd-edu'),
        'after'  => '</div>',
    ));
    ?>
  </div>

  <footer class="ht-single-footer">
    <?php
    $tags = get_the_tags();
    if (!empty($tags)) :
        ?>
        <div class="ht-post-tags">
          <span class="ht-tag-label"><?php esc_html_e('ট্যাগসমূহ:', 'helptrickbd-edu'); ?></span>
          <?php foreach ($tags as $tag) : ?>
            <a href="<?php echo esc_url(get_tag_link($tag->term_id)); ?>" class="ht-tag-link">
              #<?php echo esc_html($tag->name); ?>
            </a>
          <?php endforeach; ?>
        </div>
    <?php endif; ?>
  </footer>
</article>
