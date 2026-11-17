<?php
/**
 * Academic Author & Editorial Profile Template (E-E-A-T Compliant)
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}

get_header();

$curauth = (isset($_GET['author_name'])) ? get_user_by('slug', $author_name) : get_userdata(intval($author));
$author_id = $curauth ? $curauth->ID : get_the_author_meta('ID');
$author_name = $curauth ? $curauth->display_name : get_the_author();
$author_desc = get_the_author_meta('description', $author_id);
$author_avatar = get_avatar_url($author_id, array('size' => 160));
$post_count = count_user_posts($author_id);
?>

<div class="ht-container">
  <div class="n-catpage" style="margin-top:20px;">
    <!-- Author Bio & E-E-A-T Card -->
    <div class="n-author-card" style="background:var(--ht-surface);border:1px solid var(--ht-border);border-radius:var(--ht-radius-lg);padding:30px;display:flex;gap:24px;align-items:flex-start;margin-bottom:30px;flex-wrap:wrap;">
      <div class="n-author-avatar-wrap" style="flex-shrink:0;">
        <img src="<?php echo esc_url($author_avatar); ?>" alt="<?php echo esc_attr($author_name); ?>" width="100" height="100" loading="lazy" decoding="async" style="width:100px;height:100px;border-radius:50%;object-fit:cover;border:3px solid var(--ht-primary);">
      </div>
      <div class="n-author-info" style="flex:1;min-width:240px;">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;flex-wrap:wrap;">
          <h1 style="font-size:1.5rem;font-weight:800;margin:0;color:var(--ht-text-primary);">
            <?php echo esc_html($author_name); ?>
          </h1>
          <span style="display:inline-flex;align-items:center;gap:4px;background:var(--ht-primary-soft);color:var(--ht-primary);padding:3px 10px;border-radius:999px;font-size:0.75rem;font-weight:700;">
            <?php htbd_icon('check-circle', array('width' => 14, 'height' => 14)); ?>
            <?php esc_html_e('ভেরিফাইড শিক্ষক ও গবেষক', 'helptrickbd-edu'); ?>
          </span>
        </div>
        <p style="font-size:0.95rem;color:var(--ht-text-secondary);line-height:1.6;margin:0 0 14px;">
          <?php
          if (!empty($author_desc)) {
              echo esc_html($author_desc);
          } else {
              esc_html_e('হেল্পট্রিকবিডি একাডেমিক প্ল্যাটফর্মের জ্যেষ্ঠ শিক্ষক ও কনটেন্ট কিউরেটর। শিক্ষার্থীদের পরীক্ষায় শতভাগ নিশ্চিত ফলাফলের জন্য নির্ভুল হ্যান্ডনোট ও অধ্যায়ভিত্তিক সাজেশন প্রণয়ন করেন।', 'helptrickbd-edu');
          }
          ?>
        </p>
        <div class="ht-meta-bar" style="font-size:0.875rem;color:var(--ht-text-muted);display:flex;gap:18px;flex-wrap:wrap;">
          <span><strong><?php echo esc_html(htbd_bengali_number($post_count)); ?></strong> <?php esc_html_e('টি প্রকাশিত হ্যান্ডনোট', 'helptrickbd-edu'); ?></span>
          <span><?php esc_html_e('প্রাতিষ্ঠানিক ইমেইল:', 'helptrickbd-edu'); ?> <a href="mailto:contact@helptrickbd.com">contact@helptrickbd.com</a></span>
        </div>
      </div>
    </div>

    <!-- Author Articles Section Header -->
    <div class="n-sec-head" style="margin-bottom:20px;">
      <h2 style="font-size:1.3rem;font-weight:800;margin:0 0 6px;">
        <?php printf(esc_html__('%s-এর প্রকাশিত সকল হ্যান্ডনোট ও স্টাডি গাইড', 'helptrickbd-edu'), esc_html($author_name)); ?>
      </h2>
      <span class="rule" aria-hidden="true"></span>
    </div>

    <?php if (have_posts()) : ?>
      <!-- Grid -->
      <div class="n-catgrid" style="display:grid;grid-template-columns:repeat(auto-fill, minmax(280px, 1fr));gap:20px;">
        <?php
        while (have_posts()) :
            the_post();
            $post_id  = get_the_ID();
            $thumb    = get_the_post_thumbnail_url($post_id, 'medium');
            if (!$thumb) {
                $thumb = htbd_get_default_thumbnail();
            }
            $cat_data = htbd_primary_category($post_id);
            ?>
            <article class="n-catcard" style="background:var(--ht-surface);border:1px solid var(--ht-border);border-radius:var(--ht-radius-md);overflow:hidden;display:flex;flex-direction:column;">
              <a href="<?php the_permalink(); ?>" class="thumb-wrap" style="aspect-ratio:16/9;overflow:hidden;position:relative;background:var(--ht-surface-alt);display:block;">
                <img src="<?php echo esc_url($thumb); ?>" alt="<?php the_title_attribute(); ?>" width="300" height="169" loading="lazy" decoding="async" style="width:100%;height:100%;object-fit:cover;">
                <span class="badge" style="position:absolute;top:10px;left:10px;background:var(--ht-primary);color:#ffffff;font-size:0.75rem;padding:3px 8px;border-radius:var(--ht-radius-sm);font-weight:700;">
                  <?php echo esc_html($cat_data['name']); ?>
                </span>
              </a>
              <div class="body" style="padding:16px;display:flex;flex-direction:column;flex:1;">
                <h3 style="font-size:1.05rem;font-weight:700;line-height:1.45;margin:0 0 10px;">
                  <a href="<?php the_permalink(); ?>" style="color:var(--ht-text-primary);text-decoration:none;">
                    <?php the_title(); ?>
                  </a>
                </h3>
                <p style="font-size:0.875rem;color:var(--ht-text-secondary);line-height:1.6;margin:0 0 14px;flex:1;">
                  <?php echo esc_html(wp_trim_words(get_the_excerpt(), 18)); ?>
                </p>
                <div class="ht-meta-bar" style="font-size:0.8rem;color:var(--ht-text-muted);display:flex;justify-content:space-between;padding-top:10px;border-top:1px solid var(--ht-border);">
                  <span><?php echo esc_html(htbd_bengali_date(get_the_time('U'))); ?></span>
                  <span><?php echo esc_html(htbd_reading_time($post_id)); ?></span>
                </div>
              </div>
            </article>
            <?php
        endwhile;
        ?>
      </div>

      <!-- Pagination -->
      <?php htbd_advanced_pagination(); ?>

    <?php else : ?>
      <p style="text-align:center;padding:40px;color:var(--ht-text-muted);">
        <?php esc_html_e('এই শিক্ষকের কোনো পোস্ট এখনও প্রকাশিত হয়নি।', 'helptrickbd-edu'); ?>
      </p>
    <?php endif; ?>
  </div>
</div>

<?php
get_footer();
