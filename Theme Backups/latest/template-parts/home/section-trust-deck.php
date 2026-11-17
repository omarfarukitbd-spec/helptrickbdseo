<?php
/**
 * Homepage Section 8: Institutional Trust Deck & Utility Columns
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

if (!get_theme_mod('htbd_show_sec_trust', get_theme_mod('ht_show_sec_trust', true))) {
    return;
}

$exam_date_ssc = get_theme_mod('htbd_exam_date_ssc', get_theme_mod('ht_exam_date_ssc', '2027-02-01T09:00:00'));

// Query 4 popular/recent posts for trust sidebar with 6-hr transient caching
$trust_post_ids = get_transient('ht_trust_pop_ids');
if (false === $trust_post_ids) {
    $pop_q = new WP_Query(array(
        'posts_per_page'      => 4,
        'post_status'         => 'publish',
        'ignore_sticky_posts' => 1,
        'fields'              => 'ids',
        'no_found_rows'       => true,
    ));
    $trust_post_ids = !empty($pop_q->posts) ? $pop_q->posts : array();
    set_transient('ht_trust_pop_ids', $trust_post_ids, 6 * HOUR_IN_SECONDS);
}

$categories = get_categories(array(
    'orderby'    => 'count',
    'order'      => 'DESC',
    'number'     => 6,
    'hide_empty' => true,
));
?>
<section class="n-sec" aria-label="<?php esc_attr_e('প্রাতিষ্ঠানিক সম্পাদকীয় নীতি ও তথ্য ভাণ্ডার', 'helptrickbd'); ?>">
  <div class="n-two">
    <!-- Left Column: E-E-A-T Academic Pledge & Editorial Standards -->
    <div>
      <div class="n-sec-head">
        <h3><?php esc_html_e('হেল্পট্রিকবিডি প্রাতিষ্ঠানিক তথ্য যাচাই ও সম্পাদকীয় নীতি', 'helptrickbd'); ?></h3>
        <span class="rule" aria-hidden="true"></span>
      </div>
      <div class="n-trust-box">
        <p>
          <?php esc_html_e('প্রতিটি সাজেশন, প্রশ্নব্যাংক ও সমাধান প্রকাশের পূর্বে আমরা সংশ্লিষ্ট শিক্ষা বোর্ড ও বিশ্ববিদ্যালয়ের অফিসিয়াল সার্কুলারের সঙ্গে পুঙ্খানুপুঙ্খভাবে মিলিয়ে দেখি। পুরনো বা বাতিল তথ্য যেন নতুন মোড়কে শিক্ষার্থীদের বিভ্রান্ত না করে — সেদিকে আমাদের সম্পাদকীয় টিমের সার্বক্ষণিক নজর থাকে।', 'helptrickbd'); ?>
        </p>
        <p>
          <?php esc_html_e('শিক্ষার্থীদের পরীক্ষার প্রস্তুতিকে শতভাগ নির্ভুল ও সময়োপযোগী রাখা আমাদের প্রাতিষ্ঠানিক অঙ্গীকার। কোনো তথ্যগত ভুল পরিলক্ষিত হলে আমাদের সম্পাদকীয় ডেস্কে জানান — আমরা দ্রুততম সময়ে তা যাচাই করে হালনাগাদ করব।', 'helptrickbd'); ?>
        </p>
        <div class="ht-meta-bar" style="margin-top:14px;">
          <span class="ht-meta-item">
            <?php htbd_icon('check-circle', array('width' => 16, 'height' => 16, 'class' => 'ht-verified-icon')); ?>
            <strong><?php esc_html_e('ভেরিফাইড একাডেমিক রিসোর্স', 'helptrickbd'); ?></strong>
          </span>
          <span class="ht-meta-item">
            <a href="mailto:contact@helptrickbd.com">contact@helptrickbd.com</a>
          </span>
        </div>
      </div>
    </div>

    <!-- Right Column: Popular Posts + Category Pills + Exam Dates -->
    <div>
      <!-- Popular Posts -->
      <div class="n-popbox">
        <h4><?php esc_html_e('সর্বাধিক পঠিত হ্যান্ডনোট', 'helptrickbd'); ?></h4>
        <ol>
          <?php
          if (!empty($trust_post_ids)) :
              $trust_query = new WP_Query(array(
                  'post__in'            => $trust_post_ids,
                  'orderby'             => 'post__in',
                  'posts_per_page'      => count($trust_post_ids),
                  'ignore_sticky_posts' => 1,
                  'no_found_rows'       => true,
              ));

              if ($trust_query->have_posts()) :
                  while ($trust_query->have_posts()) :
                      $trust_query->the_post();
                      $read_time = function_exists('ht_get_reading_time') ? ht_get_reading_time(get_the_ID()) : '৩ মিনিট পড়া';
                      ?>
                      <li>
                        <a href="<?php the_permalink(); ?>"><?php the_title(); ?></a>
                        <div class="meta">
                          <span><?php echo esc_html($read_time); ?></span>
                        </div>
                      </li>
                      <?php
                  endwhile;
                  wp_reset_postdata();
              endif;
          endif;
          ?>
        </ol>
      </div>

      <!-- Categories Pill Grid -->
      <div class="n-sec-head" style="margin-top:24px;">
        <h3 style="font-size:1.15rem;"><?php esc_html_e('সকল বিষয় ও বিভাগ', 'helptrickbd'); ?></h3>
        <span class="rule" aria-hidden="true"></span>
      </div>
      <div class="n-pillgrid">
        <?php foreach ($categories as $cat) : ?>
          <a href="<?php echo esc_url(get_category_link($cat->term_id)); ?>" class="n-pill">
            <span class="pn"><?php echo esc_html($cat->name); ?></span>
            <span class="pc"><?php echo esc_html(function_exists('ht_bn_number') ? ht_bn_number($cat->count) : $cat->count); ?></span>
          </a>
        <?php endforeach; ?>
      </div>

      <!-- Academic Exam Countdown Calendar -->
      <div class="n-exambox">
        <h4><?php esc_html_e('আসন্ন পরীক্ষার লাইভ দিনপঞ্জি ও কাউন্টডাউন', 'helptrickbd'); ?></h4>
        
        <!-- Live Ticking Exam Countdown (Zero CLS, Horizontal Grid) -->
        <div class="ht-exam-timer-card" data-countdown-date="<?php echo esc_attr($exam_date_ssc); ?>" style="margin-bottom:14px;padding:12px;background:var(--ht-surface);border:1px solid var(--ht-border);border-radius:var(--ht-radius-sm);">
          <div style="display:flex;align-items:center;justify-content:space-between;gap:8px;margin-bottom:8px;">
            <span style="font-weight:700;font-size:0.9rem;color:var(--ht-text-primary);">
              <?php esc_html_e('এসএসসি ও দাখিল পরীক্ষা ২০২৭', 'helptrickbd'); ?>
            </span>
            <span style="font-size:0.75rem;color:var(--ht-accent);font-weight:700;background:var(--ht-accent-soft);padding:2px 8px;border-radius:999px;">
              <?php esc_html_e('বাকি সময়', 'helptrickbd'); ?>
            </span>
          </div>
          <div class="ht-countdown-grid">
            <div class="ht-countdown-cell">
              <span class="ht-countdown-val" data-cd-days>--</span>
              <span class="ht-countdown-label"><?php esc_html_e('দিন', 'helptrickbd'); ?></span>
            </div>
            <div class="ht-countdown-cell">
              <span class="ht-countdown-val" data-cd-hours>--</span>
              <span class="ht-countdown-label"><?php esc_html_e('ঘণ্টা', 'helptrickbd'); ?></span>
            </div>
            <div class="ht-countdown-cell">
              <span class="ht-countdown-val" data-cd-minutes>--</span>
              <span class="ht-countdown-label"><?php esc_html_e('মিনিট', 'helptrickbd'); ?></span>
            </div>
            <div class="ht-countdown-cell">
              <span class="ht-countdown-val" data-cd-seconds>--</span>
              <span class="ht-countdown-label"><?php esc_html_e('সেকেন্ড', 'helptrickbd'); ?></span>
            </div>
          </div>
        </div>

        <div class="row">
          <span><?php esc_html_e('জাতীয় বিশ্ববিদ্যালয় ডিগ্রি পরীক্ষা', 'helptrickbd'); ?></span>
          <b style="color:var(--ht-primary);"><?php esc_html_e('চলমান / রুটিন দেখুন', 'helptrickbd'); ?></b>
        </div>
        <div class="row">
          <span><?php esc_html_e('৪৭তম বিসিএস প্রিলিমিনারি', 'helptrickbd'); ?></span>
          <b><?php esc_html_e('পিএসসি সার্কুলার', 'helptrickbd'); ?></b>
        </div>
      </div>
    </div>
  </div>
</section>