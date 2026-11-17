<?php
/**
 * Single Post Template (Slim Modular Controller)
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
    <main class="ht-single-main" id="primary">
      <?php
      while (have_posts()) :
          the_post();
          get_template_part('template-parts/single/content-article');
      endwhile;

      // Related Posts Grid
      get_template_part('template-parts/single/related-posts');

      // Comments & Q&A Discussion
      if (comments_open() || get_comments_number()) :
          comments_template();
      endif;
      ?>
    </main>
    <aside class="ht-single-sidebar" aria-label="<?php esc_attr_e('Sidebar', 'helptrickbd-edu'); ?>">
      <?php get_sidebar(); ?>
    </aside>
  </div>
</div>

<?php
get_footer();
