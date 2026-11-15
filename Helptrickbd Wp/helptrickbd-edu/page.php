<?php
/**
 * Static Page Template
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
  "description": <?php echo wp_json_encode(get_the_excerpt() ?: get_the_title() . ' — HelpTrickBD'); ?>,
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
    <?php
    $ancestors = get_post_ancestors(get_the_ID());
    if (!empty($ancestors)) {
        $ancestors = array_reverse($ancestors);
        foreach ($ancestors as $ancestor_id) {
            printf(
                '<a href="%s">%s</a><span aria-hidden="true"> › </span>',
                esc_url(get_permalink($ancestor_id)),
                esc_html(get_the_title($ancestor_id))
            );
        }
    }
    ?>
    <span aria-current="page"><?php the_title(); ?></span>
  </nav>

  <div class="ht-single-layout">
    <div class="ht-single-main">
      <article id="post-<?php the_ID(); ?>" <?php post_class('ht-single-article'); ?>>
        <header class="ht-single-header">
          <h1 class="ht-single-title"><?php the_title(); ?></h1>
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
      </article>

      <?php
      if (comments_open() || get_comments_number()) :
          comments_template();
      endif;
      ?>
    </div>
  </div>
</div>
<?php endwhile; ?>

<?php
get_footer();
