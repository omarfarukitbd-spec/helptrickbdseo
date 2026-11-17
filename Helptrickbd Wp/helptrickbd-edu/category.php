<?php
/**
 * Category Archive Template
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}

get_header();

$cat_obj     = get_queried_object();
$cat_name    = isset($cat_obj->name) ? $cat_obj->name : '';
$cat_desc    = isset($cat_obj->description) ? $cat_obj->description : '';
$cat_url     = isset($cat_obj->term_id) ? esc_url(get_category_link($cat_obj->term_id)) : esc_url(get_pagenum_link());
?>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": <?php echo wp_json_encode($cat_name); ?>,
  "description": <?php echo wp_json_encode($cat_desc ?: $cat_name . ' Archive - HelpTrickBD'); ?>,
  "url": "<?php echo esc_url($cat_url); ?>",
  "inLanguage": "bn-BD",
  "publisher": {
    "@type": "Organization",
    "name": "HelpTrickBD",
    "url": "<?php echo esc_url(home_url('/')); ?>"
  }
}
</script>

<div class="ht-container">
  <nav class="ht-breadcrumb" aria-label="<?php esc_attr_e('Breadcrumbs', 'helptrickbd-edu'); ?>">
    <a href="<?php echo esc_url(home_url('/')); ?>"><?php esc_html_e('Home', 'helptrickbd-edu'); ?></a>
    <span aria-hidden="true"> › </span>
    <span><?php esc_html_e('Categories', 'helptrickbd-edu'); ?></span>
    <?php if ($cat_name) : ?>
      <span aria-hidden="true"> › </span>
      <span aria-current="page"><?php echo esc_html($cat_name); ?></span>
    <?php endif; ?>
  </nav>

  <div class="n-catpage">
    <div class="n-sec-head" style="border-top:0;padding-top:4px;">
      <h1>
        <?php the_archive_title(); ?>
      </h1>
      <?php if ($cat_desc) : ?>
        <p class="ht-archive-desc"><?php echo esc_html($cat_desc); ?></p>
      <?php endif; ?>
      <span class="rule" aria-hidden="true"></span>
    </div>

    <div class="n-toolbar">
      <span class="lab"><?php esc_html_e('Articles:', 'helptrickbd-edu'); ?></span>
      <span class="cnt">
        <?php
        global $wp_query;
        printf(
            /* translators: %s: number of posts */
            esc_html__('Total %s Articles Found', 'helptrickbd-edu'),
            esc_html($wp_query->found_posts)
        );
        ?>
      </span>
    </div>

    <?php if (have_posts()) : ?>
      <div class="n-archive-grid-2col">
        <?php
        while (have_posts()) :
            the_post();
            ?>
            <article class="n-archive-card">
              <a href="<?php the_permalink(); ?>" class="n-archive-card-thumb">
                <?php if (has_post_thumbnail()) : ?>
                  <?php
                  the_post_thumbnail('medium_large', array(
                      'class'    => 'n-card-img',
                      'loading'  => 'lazy',
                      'decoding' => 'async',
                      'alt'      => esc_attr(get_the_title()),
                  ));
                  ?>
                <?php else : ?>
                  <img src="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/Thumbnail%20BG/ssc.webp" width="600" height="338" loading="lazy" decoding="async" class="n-card-img" alt="<?php the_title_attribute(); ?>">
                <?php endif; ?>
              </a>

              <h2 class="n-archive-card-title">
                <a href="<?php the_permalink(); ?>"><?php the_title(); ?></a>
              </h2>
            </article>
            <?php
        endwhile;
        ?>
      </div>

      <?php htbd_advanced_pagination(); ?>

    <?php else : ?>
      <div class="ht-no-posts" style="padding: 40px 0; text-align: center;">
        <p><?php esc_html_e('No articles found in this category.', 'helptrickbd-edu'); ?></p>
      </div>
    <?php endif; ?>
  </div>
</div>

<?php
get_footer();
