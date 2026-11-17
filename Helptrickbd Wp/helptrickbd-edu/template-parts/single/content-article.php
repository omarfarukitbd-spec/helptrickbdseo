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
        'before' => '<div class="page-links">' . esc_html__('Pages:', 'helptrickbd-edu'),
        'after'  => '</div>',
    ));
    ?>
  </div>

  <?php
  // Output FAQPage Schema.org JSON-LD if 2+ FAQ pairs detected in content
  if (function_exists('htbd_output_faq_schema')) {
      htbd_output_faq_schema(get_the_ID());
  }
  ?>

  <footer class="ht-single-footer">
    <?php
    $tags = get_the_tags();
    if (!empty($tags)) :
        ?>
        <div class="ht-post-tags">
          <span class="ht-tag-label"><?php esc_html_e('Tags:', 'helptrickbd-edu'); ?></span>
          <?php foreach ($tags as $tag) : ?>
            <a href="<?php echo esc_url(get_tag_link($tag->term_id)); ?>" class="ht-tag-link">
              #<?php echo esc_html($tag->name); ?>
            </a>
          <?php endforeach; ?>
        </div>
    <?php endif; ?>
  </footer>

  <?php
  // BlogPosting Schema.org JSON-LD (Skipped if Rank Math or Yoast handles schema)
  if (!function_exists('rank_math_the_seo_title') && !defined('WPSEO_VERSION')) :
      $post_id         = get_the_ID();
      $post_obj        = get_post($post_id);
      $author_id       = (int) ($post_obj ? $post_obj->post_author : get_the_author_meta('ID'));
      $headline        = wp_strip_all_tags(get_the_title($post_id));
      $excerpt         = has_excerpt($post_id) ? get_the_excerpt($post_id) : wp_trim_words(strip_shortcodes($post_obj ? $post_obj->post_content : ''), 35, '...');
      $description     = wp_strip_all_tags($excerpt);
      $content_clean   = strip_tags(strip_shortcodes($post_obj ? $post_obj->post_content : ''));
      $words           = preg_split('/\s+/u', trim($content_clean), -1, PREG_SPLIT_NO_EMPTY);
      $word_count      = is_array($words) ? count($words) : 0;
      $date_published  = get_the_date('c', $post_id);
      $date_modified   = get_the_modified_date('c', $post_id);

      if (has_post_thumbnail($post_id)) {
          $image_url = get_the_post_thumbnail_url($post_id, 'full');
      } else {
          $image_url = function_exists('htbd_get_default_thumbnail') ? htbd_get_default_thumbnail() : get_template_directory_uri() . '/assets/images/default-thumbnail.webp';
      }

      $publisher_logo = get_template_directory_uri() . '/assets/images/logo.png';
      $custom_logo_id = get_theme_mod('custom_logo');
      if ($custom_logo_id) {
          $logo_src = wp_get_attachment_image_src($custom_logo_id, 'full');
          if (!empty($logo_src[0])) {
              $publisher_logo = $logo_src[0];
          }
      }

      $schema_blog_posting = array(
          '@context'         => 'https://schema.org',
          '@type'            => 'BlogPosting',
          'headline'         => esc_html($headline),
          'description'      => esc_html($description),
          'image'            => esc_url($image_url),
          'author'           => array(
              '@type' => 'Person',
              'name'  => esc_html(get_the_author_meta('display_name', $author_id)),
              'url'   => esc_url(get_author_posts_url($author_id)),
          ),
          'publisher'        => array(
              '@type' => 'Organization',
              'name'  => 'HelpTrickBD',
              'logo'  => array(
                  '@type' => 'ImageObject',
                  'url'   => esc_url($publisher_logo),
              ),
          ),
          'datePublished'    => $date_published,
          'dateModified'     => $date_modified,
          'mainEntityOfPage' => array(
              '@type' => 'WebPage',
              '@id'   => esc_url(get_permalink($post_id)),
          ),
          'wordCount'        => (int) $word_count,
          'inLanguage'       => 'bn-BD',
      );
      ?>
      <script type="application/ld+json">
      <?php echo wp_json_encode($schema_blog_posting, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT); ?>
      </script>
  <?php endif; ?>
</article>
