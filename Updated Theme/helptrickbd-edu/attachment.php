<?php
/**
 * Attachment (Media) Single Template
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}

get_header();
?>

<?php while (have_posts()) : the_post(); ?>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": <?php echo wp_json_encode(get_the_title()); ?>,
  "url": "<?php echo esc_url(get_permalink()); ?>",
  "description": <?php echo wp_json_encode(get_the_excerpt() ?: get_the_title() . ' — HelpTrickBD মিডিয়া'); ?>,
  "inLanguage": "bn-BD",
  "datePublished": "<?php echo esc_attr(get_the_date(DATE_W3C)); ?>",
  "dateModified": "<?php echo esc_attr(get_the_modified_date(DATE_W3C)); ?>",
  "publisher": {
    "@type": "Organization",
    "name": "HelpTrickBD",
    "url": "<?php echo esc_url(home_url('/')); ?>"
  }
}
</script>

<div class="ht-container">
  <nav class="ht-breadcrumb" aria-label="<?php esc_attr_e('ব্রেডক্রাম্ব', 'helptrickbd-edu'); ?>">
    <a href="<?php echo esc_url(home_url('/')); ?>"><?php esc_html_e('হোম', 'helptrickbd-edu'); ?></a>
    <span aria-hidden="true"> › </span>
    <?php if (wp_get_post_parent_id(get_the_ID())) : ?>
      <a href="<?php echo esc_url(get_permalink(wp_get_post_parent_id(get_the_ID()))); ?>">
        <?php echo esc_html(get_the_title(wp_get_post_parent_id(get_the_ID()))); ?>
      </a>
      <span aria-hidden="true"> › </span>
    <?php endif; ?>
    <span aria-current="page"><?php the_title(); ?></span>
  </nav>

  <div class="ht-single-layout">
    <div class="ht-single-main">
      <article id="post-<?php the_ID(); ?>" <?php post_class('ht-single-article ht-attachment-article'); ?>>
        <header class="ht-single-header">
          <h1 class="ht-single-title"><?php the_title(); ?></h1>
          <div class="meta" style="margin-top: 8px;">
            <span><?php echo esc_html(get_the_date('j F, Y')); ?></span>
          </div>
        </header>

        <div class="ht-attachment-media" style="margin: 24px 0; text-align: center;">
          <?php
          $mime = get_post_mime_type();
          if (strpos($mime, 'image') !== false) {
              $full_src = wp_get_attachment_image_src(get_the_ID(), 'full');
              if ($full_src) {
                  printf(
                      '<figure><img src="%s" width="%d" height="%d" alt="%s" loading="lazy" decoding="async" style="max-width:100%%;height:auto;border-radius:var(--ht-radius-md);"><figcaption>%s</figcaption></figure>',
                      esc_url($full_src[0]),
                      (int) $full_src[1],
                      (int) $full_src[2],
                      esc_attr(get_the_title()),
                      esc_html(get_the_excerpt() ?: get_the_title())
                  );
              }
          } elseif (strpos($mime, 'video') !== false) {
              echo '<figure>';
              // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped
              echo wp_video_shortcode(array('src' => esc_url(wp_get_attachment_url())));
              echo '</figure>';
          } elseif (strpos($mime, 'audio') !== false) {
              echo '<figure>';
              // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped
              echo wp_audio_shortcode(array('src' => esc_url(wp_get_attachment_url())));
              echo '</figure>';
          } else {
              printf(
                  '<p><a href="%s" class="ht-btn ht-btn-primary" download>%s</a></p>',
                  esc_url(wp_get_attachment_url()),
                  esc_html__('ফাইলটি ডাউনলোড করুন', 'helptrickbd-edu')
              );
          }
          ?>
        </div>

        <?php if (get_the_content()) : ?>
          <div class="ht-entry-content">
            <?php the_content(); ?>
          </div>
        <?php endif; ?>

        <div class="ht-attachment-nav" style="margin-top: 32px; display: flex; gap: 16px; justify-content: space-between; border-top: 1px solid var(--ht-border); padding-top: 16px;">
          <?php
          $prev_att = get_adjacent_post(false, '', true);
          $next_att = get_adjacent_post(false, '', false);
          if ($prev_att) :
              ?>
            <a href="<?php echo esc_url(get_permalink($prev_att->ID)); ?>" rel="prev" class="ht-btn">
              &larr; <?php esc_html_e('পূর্ববর্তী', 'helptrickbd-edu'); ?>
            </a>
          <?php endif; ?>
          <?php if ($next_att) : ?>
            <a href="<?php echo esc_url(get_permalink($next_att->ID)); ?>" rel="next" class="ht-btn" style="margin-left: auto;">
              <?php esc_html_e('পরবর্তী', 'helptrickbd-edu'); ?> &rarr;
            </a>
          <?php endif; ?>
        </div>
      </article>
    </div>
  </div>
</div>

<?php endwhile; ?>

<?php
get_footer();
