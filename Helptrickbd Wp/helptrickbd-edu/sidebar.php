<?php
/**
 * Academic Sidebar Component
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}
?>

<aside id="secondary" class="ht-sidebar-area" aria-label="<?php esc_attr_e('সাইডবার উইজেট', 'helptrickbd-edu'); ?>">
  <?php if (is_active_sidebar('sidebar-main')) : ?>
    <?php dynamic_sidebar('sidebar-main'); ?>
  <?php else : ?>
    <!-- Fallback 1: Popular Academic Handnotes -->
    <div class="ht-widget n-popbox" style="margin-bottom:24px;">
      <div class="n-sec-head" style="margin-bottom:14px;">
        <h3 style="font-size:1.15rem;font-weight:800;margin:0 0 4px;"><?php esc_html_e('জনপ্রিয় হ্যান্ডনোট', 'helptrickbd-edu'); ?></h3>
        <span class="rule" aria-hidden="true"></span>
      </div>
      <ol style="padding-left:18px;margin:0;">
        <?php
        $pop_side_query = new WP_Query(array(
            'posts_per_page'      => 4,
            'post_status'         => 'publish',
            'ignore_sticky_posts' => 1,
            'no_found_rows'       => true,
        ));
        if ($pop_side_query->have_posts()) :
            while ($pop_side_query->have_posts()) :
                $pop_side_query->the_post();
                ?>
                <li style="margin-bottom:12px;line-height:1.4;">
                  <a href="<?php the_permalink(); ?>" style="color:var(--ht-text-primary);text-decoration:none;font-weight:600;font-size:0.925rem;">
                    <?php the_title(); ?>
                  </a>
                  <div style="font-size:0.775rem;color:var(--ht-text-muted);margin-top:2px;">
                    <?php echo esc_html(htbd_reading_time(get_the_ID())); ?>
                  </div>
                </li>
                <?php
            endwhile;
            wp_reset_postdata();
        endif;
        ?>
      </ol>
    </div>

    <!-- Fallback 2: Exam Routine Calendar -->
    <div class="ht-widget n-exambox" style="margin-bottom:24px;background:var(--ht-surface-alt);padding:18px;border:1px solid var(--ht-border);border-radius:var(--ht-radius-md);">
      <h4 style="font-size:1rem;font-weight:800;color:var(--ht-primary);margin:0 0 10px;"><?php esc_html_e('আসন্ন পরীক্ষার সম্ভাব্য তারিখ', 'helptrickbd-edu'); ?></h4>
      <div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid var(--ht-border);font-size:0.875rem;">
        <span><?php esc_html_e('এসএসসি ও দাখিল ২০২৭', 'helptrickbd-edu'); ?></span>
        <b style="color:var(--ht-accent);"><?php esc_html_e('ফেব্রুয়ারি ২০২৭', 'helptrickbd-edu'); ?></b>
      </div>
      <div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid var(--ht-border);font-size:0.875rem;">
        <span><?php esc_html_e('ডিগ্রি ১ম বর্ষ পরীক্ষা', 'helptrickbd-edu'); ?></span>
        <b style="color:var(--ht-primary);"><?php esc_html_e('চলমান', 'helptrickbd-edu'); ?></b>
      </div>
      <div style="display:flex;justify-content:space-between;padding:6px 0;font-size:0.875rem;">
        <span><?php esc_html_e('৪৭তম বিসিএস প্রিলিমিনারি', 'helptrickbd-edu'); ?></span>
        <b><?php esc_html_e('পিএসসি সার্কুলার', 'helptrickbd-edu'); ?></b>
      </div>
    </div>
  <?php endif; ?>
</aside>
