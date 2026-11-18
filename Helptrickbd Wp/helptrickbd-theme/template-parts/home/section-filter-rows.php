<?php
/**
 * Homepage Section 5: Subject-Based Posts & Dynamic Filter Rows ("বিষয়ভিত্তিক পোস্ট")
 * Features 2-column card grid on computer, mobile 1-column, and robust multi-category queries
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

if (!get_theme_mod('htbd_show_sec_filter', get_theme_mod('ht_show_sec_filter', true))) {
    return;
}

$is_en = function_exists('ht_is_bangla_locale') && !ht_is_bangla_locale();

$sec_title = get_theme_mod('htbd_sec_filter_title', get_theme_mod('ht_sec_filter_title', ''));
if (empty($sec_title)) {
    $sec_title = $is_en ? 'Explore by Academic Subject' : 'বিষয়ভিত্তিক হ্যান্ডনোট ও গাইড';
}

$link_text = get_theme_mod('htbd_sec_filter_link_text', get_theme_mod('ht_sec_filter_link_text', ''));
if (empty($link_text)) {
    $link_text = $is_en ? 'All Articles →' : 'সকল পোস্ট দেখুন →';
}

// Define tabs with verified slugs and display labels in authentic Bengali and English
$tabs = array(
    'all'                 => $is_en ? 'All Subjects' : 'সকল বিষয়',
    'ssc-dakhil'          => $is_en ? 'SSC & Dakhil' : 'এসএসসি ও দাখিল',
    'political-science'   => $is_en ? 'Political Science' : 'রাষ্ট্রবিজ্ঞান',
    'bangla-1st-paper'    => $is_en ? 'Bangla 1st Paper' : 'বাংলা ১ম পত্র',
    'islamic-article'     => $is_en ? 'Islamic Articles' : 'ইসলামিক প্রবন্ধ',
    'national-university' => $is_en ? 'National University' : 'জাতীয় বিশ্ববিদ্যালয়',
    'ict-technology'      => $is_en ? 'ICT & Tech' : 'আইসিটি ও প্রযুক্তি',
);

// 6-Hour Locale-Aware Transient Caching for Homepage Filter Posts
$transient_key  = 'ht_home_filter_posts_cache_' . ($is_en ? 'en' : 'bn');
$all_posts_data = get_transient($transient_key);

if (false === $all_posts_data) {
    $rendered_ids = array();
    $all_posts_data = array();

    // 1. Initial 8 posts for 'all'
    $all_args = array(
        'posts_per_page'      => 8,
        'post_status'         => 'publish',
        'ignore_sticky_posts' => 1,
        'no_found_rows'       => true,
    );
    if (function_exists('pll_the_languages') && $is_en) {
        $all_args['lang'] = 'en';
    }
    $all_query = new WP_Query($all_args);

    if ($all_query->have_posts()) {
        while ($all_query->have_posts()) {
            $all_query->the_post();
            $pid = get_the_ID();
            $cats = get_the_category();
            $cat_slugs = array('all');
            $first_slug = 'ssc-dakhil';
            if (!empty($cats)) {
                $first_slug = $cats[0]->slug;
                foreach ($cats as $c) {
                    $cat_slugs[] = $c->slug;
                }
            }
            $rendered_ids[$pid] = $cat_slugs;
            $read_text = function_exists('ht_get_localized_reading_time') ? ht_get_localized_reading_time($pid) : ($is_en ? '3 min read' : '৩ মিনিট পড়া');
            $date_text = function_exists('ht_get_localized_post_date') ? ht_get_localized_post_date($pid) : get_the_date('j F, Y');
            $all_posts_data[] = array(
                'id'       => $pid,
                'title'    => get_the_title(),
                'url'      => get_permalink(),
                'cats'     => $cat_slugs,
                'cat_slug' => $first_slug,
                'cat_name' => !empty($cats) ? (function_exists('ht_get_localized_term_name') ? ht_get_localized_term_name($cats[0]) : $cats[0]->name) : ($is_en ? 'Article' : 'হ্যান্ডনোট'),
                'date'     => $date_text,
                'read'     => $read_text,
                'thumb'    => has_post_thumbnail($pid) ? get_the_post_thumbnail_url($pid, 'ht-card-thumb') : '',
                'initial'  => true,
            );
        }
        wp_reset_postdata();
    }

    // 2. Query up to 6 posts for each specific category tab
    foreach ($tabs as $slug => $label) {
        if ($slug === 'all') {
            continue;
        }

        $cat_obj = get_category_by_slug($slug);
        if (!$cat_obj) {
            continue;
        }

        $cat_args = array(
            'cat'                 => $cat_obj->term_id,
            'posts_per_page'      => 8,
            'post_status'         => 'publish',
            'ignore_sticky_posts' => 1,
            'no_found_rows'       => true,
        );
        if (function_exists('pll_the_languages') && $is_en) {
            $cat_args['lang'] = 'en';
        }
        $cat_query = new WP_Query($cat_args);

        if ($cat_query->have_posts()) {
            while ($cat_query->have_posts()) {
                $cat_query->the_post();
                $pid = get_the_ID();

                if (isset($rendered_ids[$pid])) {
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
                    $cats = get_the_category();
                    $cat_slugs = array($slug);
                    if (!empty($cats)) {
                        foreach ($cats as $c) {
                            $cat_slugs[] = $c->slug;
                        }
                    }
                    $rendered_ids[$pid] = $cat_slugs;
                    $read_text = function_exists('ht_get_localized_reading_time') ? ht_get_localized_reading_time($pid) : ($is_en ? '3 min read' : '৩ মিনিট পড়া');
                    $date_text = function_exists('ht_get_localized_post_date') ? ht_get_localized_post_date($pid) : get_the_date('j F, Y');
                    $all_posts_data[] = array(
                        'id'       => $pid,
                        'title'    => get_the_title(),
                        'url'      => get_permalink(),
                        'cats'     => $cat_slugs,
                        'cat_slug' => $slug,
                        'cat_name' => function_exists('ht_get_localized_term_name') ? ht_get_localized_term_name($cat_obj) : $cat_obj->name,
                        'date'     => $date_text,
                        'read'     => $read_text,
                        'thumb'    => has_post_thumbnail($pid) ? get_the_post_thumbnail_url($pid, 'ht-card-thumb') : '',
                        'initial'  => false,
                    );
                }
            }
            wp_reset_postdata();
        }
    }

    set_transient($transient_key, $all_posts_data, 6 * HOUR_IN_SECONDS);
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
  <div class="n-thumb-tabs" role="tablist" aria-label="<?php echo $is_en ? esc_attr__('Filter by academic subject', 'helptrickbd') : esc_attr__('বিষয় অনুযায়ী ফিল্টার', 'helptrickbd'); ?>">
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

        // Dynamic category-based fallback thumbnail
        $fallback_img = 'ssc.webp';
        $slug_check = !empty($item['cat_slug']) ? $item['cat_slug'] : '';
        if (strpos($slug_check, 'political') !== false) {
            $fallback_img = 'political_science.webp';
        } elseif (strpos($slug_check, 'islamic') !== false) {
            $fallback_img = 'islamic.webp';
        } elseif (strpos($slug_check, 'national') !== false || strpos($slug_check, 'nu') !== false) {
            $fallback_img = 'nu.webp';
        } elseif (strpos($slug_check, 'ict') !== false || strpos($slug_check, 'tech') !== false) {
            $fallback_img = 'ict.webp';
        }
        $fallback_url = 'https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/Thumbnail%20BG/' . $fallback_img;
        ?>
        <a href="<?php echo esc_url($item['url']); ?>" 
           class="n-trow" 
           data-cats="<?php echo esc_attr($cat_classes); ?>"
           style="<?php echo $is_visible ? 'display:grid;' : 'display:none;'; ?>">
          <div class="th">
            <?php if (!empty($item['thumb'])) : ?>
              <img src="<?php echo esc_url($item['thumb']); ?>" loading="lazy" decoding="async" width="110" height="78" alt="" aria-hidden="true">
            <?php else : ?>
              <img src="<?php echo esc_url($fallback_url); ?>" loading="lazy" decoding="async" width="110" height="78" alt="" aria-hidden="true">
            <?php endif; ?>
          </div>

          <div class="info">
            <span class="tag"><?php echo esc_html($item['cat_name']); ?></span>
            <h4><?php echo esc_html($item['title']); ?></h4>
          </div>

          <div class="arr" aria-hidden="true">&rarr;</div>
        </a>
    <?php endforeach; ?>
  </div>
</section>