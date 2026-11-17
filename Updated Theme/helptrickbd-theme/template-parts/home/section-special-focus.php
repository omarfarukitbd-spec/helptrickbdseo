<?php
/**
 * Homepage Section 5: National University & Special Focus (Single Clean Container)
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}

if (!get_theme_mod('htbd_show_sec_nu', true)) {
    return;
}

$sec_title  = get_theme_mod('htbd_sec_nu_title', 'National University & Higher Studies');
if ($sec_title === 'জাতীয় বিশ্ববিদ্যালয় ও উচ্চশিক্ষা' || $sec_title === 'জাতীয় বিশ্ববিদ্যালয় ও উচ্চশিক্ষা') {
    $sec_title = 'National University & Higher Studies';
}
$cat_id     = (int) get_theme_mod('htbd_sec_nu_category', 0);
$post_count = (int) get_theme_mod('htbd_sec_nu_count', 6);
$link_text  = get_theme_mod('htbd_sec_nu_link_text', 'All NU Handnotes →');
if ($link_text === 'সব হ্যান্ডনোট →' || $link_text === 'সব লেখা →') {
    $link_text = 'All NU Handnotes →';
}

$query_args = array(
    'posts_per_page'      => $post_count > 0 ? $post_count : 6,
    'post_status'         => 'publish',
    'ignore_sticky_posts' => 1,
    'no_found_rows'       => true,
);

if ($cat_id > 0) {
    $query_args['cat'] = $cat_id;
    $target_link = get_category_link($cat_id);
} else {
    $nu_term = get_category_by_slug('national-university');
    if ($nu_term) {
        $query_args['cat'] = $nu_term->term_id;
        $target_link = get_category_link($nu_term->term_id);
    } else {
        $target_link = home_url('/category/national-university/');
    }
}

$focus_query = new WP_Query($query_args);

if (!$focus_query->have_posts()) {
    return;
}
?>
<section class="n-sec" aria-label="<?php echo esc_attr($sec_title); ?>">
  <div class="n-sec-head">
    <h3><?php echo esc_html($sec_title); ?></h3>
    <span class="rule" aria-hidden="true"></span>
    <a href="<?php echo esc_url($target_link); ?>">
      <?php echo esc_html($link_text); ?>
    </a>
  </div>

  <div class="n-label-grid">
    <?php
    while ($focus_query->have_posts()) :
        $focus_query->the_post();
        ?>
        <a href="<?php the_permalink(); ?>" class="n-lrow">
          <?php if (has_post_thumbnail()) : ?>
            <?php
            the_post_thumbnail('medium', array(
                'loading'  => 'lazy',
                'decoding' => 'async',
                'class'    => 'n-lrow-img',
                'width'    => 96,
                'height'   => 68,
                'alt'      => esc_attr(get_the_title()),
            ));
            ?>
          <?php else : ?>
            <img src="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/Thumbnail%20BG/nu.webp" loading="lazy" decoding="async" class="n-lrow-img" width="96" height="68" alt="<?php the_title_attribute(); ?>">
          <?php endif; ?>

          <div class="n-lrow-text">
            <span class="lt-t"><?php the_title(); ?></span>
            <span class="lt-m"><?php echo esc_html(get_the_date('j F, Y')); ?></span>
          </div>
        </a>
        <?php
    endwhile;
    wp_reset_postdata();
    ?>
  </div>
</section>
