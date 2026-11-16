<?php
/**
 * Homepage Section 5: Subject-Based Posts & Dynamic Filter Rows ("বিষয়ভিত্তিক পোস্ট")
 * Features 2-column card grid on computer, mobile 1-column, and robust multi-category queries
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}

if (!get_theme_mod('htbd_show_sec_filter', true)) {
    return;
}

$sec_title  = get_theme_mod('htbd_sec_filter_title', 'বিষয়ভিত্তিক পোস্ট');
$link_text  = get_theme_mod('htbd_sec_filter_link_text', 'সব লেখা →');

// Define tabs with verified slugs and display labels
$tabs = array(
    'all'                 => 'সব বিষয়',
    'ssc-dakhil'          => 'এসএসসি ও দাখিল',
    'political-science'   => 'রাষ্ট্রবিজ্ঞান',
    'bangla-1st-paper'    => 'বাংলা ১ম পত্র',
    'islamic-article'     => 'ইসলামিক আর্টিকেল',
    'national-university' => 'জাতীয় বিশ্ববিদ্যালয়',
    'ict-technology'      => 'আইসিটি ও প্রযুক্তি',
);

// Collect posts for each tab ensuring every tab has 6 relevant posts
$rendered_ids = array();
$all_posts_data = array();

// 1. Initial 8 posts for 'all'
$all_query = new WP_Query(array(
    'posts_per_page'      => 8,
    'post_status'         => 'publish',
    'ignore_sticky_posts' => 1,
    'no_found_rows'       => true,
));

if ($all_query->have_posts()) {
    while ($all_query->have_posts()) {
        $all_query->the_post();
        $pid = get_the_ID();
        $cats = get_the_category();
        $cat_slugs = array('all');
        if (!empty($cats)) {
            foreach ($cats as $c) {
                $cat_slugs[] = $c->slug;
            }
        }
        $rendered_ids[$pid] = $cat_slugs;
        $all_posts_data[] = array(
            'id'       => $pid,
            'title'    => get_the_title(),
            'url'      => get_permalink(),
            'cats'     => $cat_slugs,
            'cat_name' => !empty($cats) ? $cats[0]->name : 'হ্যান্ডনোট',
            'date'     => get_the_date('j F, Y'),
            'read'     => htbd_reading_time($pid),
            'thumb'    => has_post_thumbnail($pid) ? get_the_post_thumbnail_url($pid, 'ht-thumb-row') : '',
            'initial'  => true,
        );
    }
    wp_reset_postdata();
}

// 2. Query up to 6 posts for each specific category tab to guarantee non-empty tabs
foreach ($tabs as $slug => $label) {
    if ($slug === 'all') {
        continue;
    }

    $cat_obj = get_category_by_slug($slug);
    if (!$cat_obj) {
        continue;
    }

    $cat_query = new WP_Query(array(
        'cat'                 => $cat_obj->term_id,
        'posts_per_page'      => 6,
        'post_status'         => 'publish',
        'ignore_sticky_posts' => 1,
        'no_found_rows'       => true,
    ));

    if ($cat_query->have_posts()) {
        while ($cat_query->have_posts()) {
            $cat_query->the_post();
            $pid = get_the_ID();

            if (isset($rendered_ids[$pid])) {
                // Already in list, ensure this category slug is present in data-cats
                if (!in_array($slug, $rendered_ids[$pid], true)) {
                    $rendered_ids[$pid][] = $slug;
                    foreach ($all_posts_data as &$pd) {
                        if ($pd['id'] === $pid && !in_array($slug, $pd['cats'], true)) {
                            $pd['cats'][] = $slug;
                        }
                    }
                    unset($pd);
                }
            } else {
                // New post not yet rendered
                $cats = get_the_category();
                $cat_slugs = array($slug);
                if (!empty($cats)) {
                    foreach ($cats as $c) {
                        $cat_slugs[] = $c->slug;
                    }
                }
                $rendered_ids[$pid] = $cat_slugs;
                $all_posts_data[] = array(
                    'id'       => $pid,
                    'title'    => get_the_title(),
                    'url'      => get_permalink(),
                    'cats'     => $cat_slugs,
                    'cat_name' => $cat_obj->name,
                    'date'     => get_the_date('j F, Y'),
                    'read'     => htbd_reading_time($pid),
                    'thumb'    => has_post_thumbnail($pid) ? get_the_post_thumbnail_url($pid, 'ht-thumb-row') : '',
                    'initial'  => false, // Hidden until this tab is selected
                );
            }
        }
        wp_reset_postdata();
    }
}

if (empty($all_posts_data)) {
    return;
}
?>
<section class="n-sec n-sec-filter-posts" aria-label="<?php echo esc_attr($sec_title); ?>">
  <div class="n-sec-head">
    <h3><?php echo esc_html($sec_title); ?></h3>
    <span class="rule" aria-hidden="true"></span>
    <a href="<?php echo esc_url(home_url('/blog/')); ?>">
      <?php echo esc_html($link_text); ?>
    </a>
  </div>

  <!-- Interactive Filter Tabs (All Categories Guaranteed to Have Posts) -->
  <div class="n-thumb-tabs" role="tablist" aria-label="<?php esc_attr_e('বিষয় অনুযায়ী ফিল্টার', 'helptrickbd-edu'); ?>">
    <?php foreach ($tabs as $slug => $label) : ?>
      <button type="button" 
              class="n-thumb-tab-btn <?php echo $slug === 'all' ? 'active' : ''; ?>" 
              data-cat="<?php echo esc_attr($slug); ?>" 
              role="tab" 
              aria-selected="<?php echo $slug === 'all' ? 'true' : 'false'; ?>">
        <?php echo esc_html($label); ?>
      </button>
    <?php endforeach; ?>
  </div>

  <!-- Rows List: 2-Column Grid on Computer, 1-Column on Mobile -->
  <div class="n-thumb-list">
    <?php foreach ($all_posts_data as $item) : 
        $cat_classes = implode(' ', array_unique($item['cats']));
        $is_visible = $item['initial'];
        ?>
        <a href="<?php echo esc_url($item['url']); ?>" 
           class="n-trow" 
           data-cats="<?php echo esc_attr($cat_classes); ?>"
           style="<?php echo $is_visible ? 'display:grid;' : 'display:none;'; ?>">
          <div class="th">
            <?php if (!empty($item['thumb'])) : ?>
              <img src="<?php echo esc_url($item['thumb']); ?>" loading="lazy" decoding="async" width="110" height="78" alt="<?php echo esc_attr($item['title']); ?>">
            <?php else : ?>
              <img src="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/Thumbnail%20BG/ssc.webp" loading="lazy" decoding="async" width="110" height="78" alt="<?php echo esc_attr($item['title']); ?>">
            <?php endif; ?>
          </div>

          <div class="info">
            <span class="tag"><?php echo esc_html($item['cat_name']); ?></span>
            <h4><?php echo esc_html($item['title']); ?></h4>
            <div class="meta">
              <span><?php echo esc_html($item['date']); ?></span> &bull; 
              <span><?php echo esc_html($item['read']); ?></span>
            </div>
          </div>

          <div class="arr" aria-hidden="true">&rarr;</div>
        </a>
    <?php endforeach; ?>
  </div>
</section>
