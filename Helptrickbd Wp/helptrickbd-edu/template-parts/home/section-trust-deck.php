<?php
/**
 * Homepage Section 8: Institutional Trust Deck & Utility Columns
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}

// Query 4 popular/recent posts for trust sidebar
$popular_query = new WP_Query(array(
    'posts_per_page'      => 4,
    'post_status'         => 'publish',
    'ignore_sticky_posts' => 1,
    'no_found_rows'       => true,
));

$categories = get_categories(array(
    'orderby'    => 'count',
    'order'      => 'DESC',
    'number'     => 6,
    'hide_empty' => false,
));
?>
<section class="n-sec" aria-label="<?php esc_attr_e('প্রাতিষ্ঠানিক সম্পাদকীয় নীতি ও তথ্য ভাণ্ডার', 'helptrickbd-edu'); ?>">
  <div class="n-two">
    <!-- Left Column: E-E-A-T Academic Pledge & Editorial Standards -->
    <div>
      <div class="n-sec-head">
        <h3><?php esc_html_e('হেল্পট্রিকবিডি প্রাতিষ্ঠানিক তথ্য যাচাই ও সম্পাদকীয় নীতি', 'helptrickbd-edu'); ?></h3>
        <span class="rule" aria-hidden="true"></span>
      </div>
      <div class="n-trust-box">
        <p>
          <?php esc_html_e('প্রতিটি সাজেশন, প্রশ্নব্যাংক ও সমাধান প্রকাশের পূর্বে আমরা সংশ্লিষ্ট শিক্ষা বোর্ড ও বিশ্ববিদ্যালয়ের অফিসিয়াল সার্কুলারের সঙ্গে পুঙ্খানুপুঙ্খভাবে মিলিয়ে দেখি। পুরনো বা বাতিল তথ্য যেন নতুন মোড়কে শিক্ষার্থীদের বিভ্রান্ত না করে — সেদিকে আমাদের সম্পাদকীয় টিমের সার্বক্ষণিক নজর থাকে।', 'helptrickbd-edu'); ?>
        </p>
        <p>
          <?php esc_html_e('শিক্ষার্থীদের পরীক্ষার প্রস্তুতিকে শতভাগ নির্ভুল ও সময়োপযোগী রাখা আমাদের প্রাতিষ্ঠানিক অঙ্গীকার। কোনো তথ্যগত ভুল পরিলক্ষিত হলে আমাদের সম্পাদকীয় ডেস্কে জানান — আমরা দ্রুততম সময়ে তা যাচাই করে হালনাগাদ করব।', 'helptrickbd-edu'); ?>
        </p>
        <div class="ht-meta-bar" style="margin-top:14px;">
          <span class="ht-meta-item">
            <?php htbd_icon('check-circle', array('width' => 16, 'height' => 16, 'class' => 'ht-verified-icon')); ?>
            <strong><?php esc_html_e('ভেরিফাইড একাডেমিক রিসোর্স', 'helptrickbd-edu'); ?></strong>
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
        <h4><?php esc_html_e('সর্বাধিক পঠিত হ্যান্ডনোট', 'helptrickbd-edu'); ?></h4>
        <ol>
          <?php
          if ($popular_query->have_posts()) :
              while ($popular_query->have_posts()) :
                  $popular_query->the_post();
                  ?>
                  <li>
                    <a href="<?php the_permalink(); ?>"><?php the_title(); ?></a>
                    <div class="meta">
                      <span><?php echo esc_html(htbd_reading_time()); ?></span>
                    </div>
                  </li>
                  <?php
              endwhile;
              wp_reset_postdata();
          endif;
          ?>
        </ol>
      </div>

      <!-- Categories Pill Grid -->
      <div class="n-sec-head" style="margin-top:24px;">
        <h3 style="font-size:1.15rem;"><?php esc_html_e('সকল বিষয় ও বিভাগ', 'helptrickbd-edu'); ?></h3>
        <span class="rule" aria-hidden="true"></span>
      </div>
      <div class="n-pillgrid">
        <?php foreach ($categories as $cat) : ?>
          <a href="<?php echo esc_url(get_category_link($cat->term_id)); ?>" class="n-pill">
            <span class="pn"><?php echo esc_html($cat->name); ?></span>
            <span class="pc"><?php echo esc_html(htbd_bengali_number($cat->count)); ?></span>
          </a>
        <?php endforeach; ?>
      </div>

      <!-- Academic Exam Countdown Calendar -->
      <div class="n-exambox">
        <h4><?php esc_html_e('আসন্ন পরীক্ষার সম্ভাব্য দিনপঞ্জি', 'helptrickbd-edu'); ?></h4>
        <div class="row">
          <span><?php esc_html_e('এসএসসি ও দাখিল পরীক্ষা ২০২৭', 'helptrickbd-edu'); ?></span>
          <b><?php esc_html_e('ফেব্রুয়ারি ২০২৭', 'helptrickbd-edu'); ?></b>
        </div>
        <div class="row">
          <span><?php esc_html_e('জাতীয় বিশ্ববিদ্যালয় ডিগ্রি পরীক্ষা', 'helptrickbd-edu'); ?></span>
          <b><?php esc_html_e('চলমান / রুটিন দেখুন', 'helptrickbd-edu'); ?></b>
        </div>
        <div class="row">
          <span><?php esc_html_e('৪৭তম বিসিএস প্রিলিমিনারি', 'helptrickbd-edu'); ?></span>
          <b><?php esc_html_e('পিএসসি সার্কুলার', 'helptrickbd-edu'); ?></b>
        </div>
      </div>
    </div>
  </div>
</section>
