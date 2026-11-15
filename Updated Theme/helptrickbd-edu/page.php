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

<div class="ht-container">
  <div class="ht-single-layout">
    <div class="ht-single-main">
      <?php
      while (have_posts()) :
          the_post();
          ?>
          <article id="post-<?php the_ID(); ?>" <?php post_class('ht-single-article'); ?>>
            <header class="ht-single-header">
              <h1 class="ht-single-title"><?php the_title(); ?></h1>
            </header>

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
      endwhile;
      ?>
    </div>
  </div>
</div>

<?php
get_footer();
