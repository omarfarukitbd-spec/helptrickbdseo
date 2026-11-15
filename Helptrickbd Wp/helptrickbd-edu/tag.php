<?php
/**
 * Tag Archive Template
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}

get_header();

$tag_obj  = get_queried_object();
$tag_name = isset($tag_obj->name) ? $tag_obj->name : '';
$tag_desc = isset($tag_obj->description) ? $tag_obj->description : '';
$tag_url  = isset($tag_obj->term_id) ? esc_url(get_tag_link($tag_obj->term_id)) : esc_url(get_pagenum_link());
?>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": <?php echo wp_json_encode('ট্যাগ: ' . $tag_name); ?>,
  "description": <?php echo wp_json_encode($tag_desc ?: '"' . $tag_name . '" ট্যাগের সকল আর্টিকেল'); ?>,
  "url": "<?php echo esc_url($tag_url); ?>",
  "inLanguage": "bn-BD",
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
    <span><?php esc_html_e('ট্যাগ', 'helptrickbd-edu'); ?></span>
    <?php if ($tag_name) : ?>
      <span aria-hidden="true"> › </span>
      <span aria-current="page"><?php echo esc_html($tag_name); ?></span>
    <?php endif; ?>
  </nav>

  <div class="n-catpage">
    <div class="n-sec-head" style="border-top:0;padding-top:4px;">
      <h1>
        <?php
        printf(
            /* translators: %s: tag name */
            esc_html__('ট্যাগ: %s', 'helptrickbd-edu'),
            esc_html($tag_name)
        );
        ?>
      </h1>
      <?php if ($tag_desc) : ?>
        <p class="ht-archive-desc"><?php echo esc_html($tag_desc); ?></p>
      <?php endif; ?>
      <span class="rule" aria-hidden="true"></span>
    </div>

    <div class="n-toolbar">
      <span class="lab"><?php esc_html_e('আর্টিকেল তালিকা:', 'helptrickbd-edu'); ?></span>
      <span class="cnt">
        <?php
        global $wp_query;
        printf(
            /* translators: %s: number of posts */
            esc_html__('মোট %sটি আর্টিকেল', 'helptrickbd-edu'),
            esc_html(htbd_bengali_number($wp_query->found_posts))
        );
        ?>
      </span>
    </div>

    <?php if (have_posts()) : ?>
      <div class="n-list">
        <?php
        $post_index = 1;
        while (have_posts()) :
            the_post();
            ?>
            <article>
              <div class="no" aria-hidden="true">
                <?php echo esc_html(htbd_bengali_number(sprintf('%02d', $post_index))); ?>
              </div>

              <?php if (has_post_thumbnail()) : ?>
                <a href="<?php the_permalink(); ?>" class="lth-wrap">
                  <?php
                  the_post_thumbnail(array(108, 80), array(
                      'class'    => 'lth',
                      'loading'  => 'lazy',
                      'decoding' => 'async',
                      'width'    => 108,
                      'height'   => 80,
                      'alt'      => esc_attr(get_the_title()),
                  ));
                  ?>
                </a>
              <?php endif; ?>

              <div class="info">
                <h2 class="ht-list-title">
                  <a href="<?php the_permalink(); ?>"><?php the_title(); ?></a>
                </h2>
                <p><?php echo esc_html(wp_trim_words(get_the_excerpt(), 22, '...')); ?></p>
                <div class="meta">
                  <span><?php echo esc_html(get_the_date('j F, Y')); ?></span> &bull;
                  <span><?php echo esc_html(htbd_reading_time()); ?></span>
                </div>
              </div>
            </article>
            <?php
            $post_index++;
        endwhile;
        ?>
      </div>

      <div class="ht-pagination" style="margin: 32px 0;">
        <?php
        the_posts_pagination(array(
            'mid_size'  => 2,
            'prev_text' => '&larr; পূর্ববর্তী',
            'next_text' => 'পরবর্তী &rarr;',
        ));
        ?>
      </div>

    <?php else : ?>
      <div class="ht-no-posts" style="padding: 40px 0; text-align: center;">
        <p><?php esc_html_e('এই ট্যাগে বর্তমানে কোনো পোস্ট পাওয়া যায়নি।', 'helptrickbd-edu'); ?></p>
      </div>
    <?php endif; ?>
  </div>
</div>

<?php
get_footer();
