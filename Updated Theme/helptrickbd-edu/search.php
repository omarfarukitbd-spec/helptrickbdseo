<?php
/**
 * Academic Search Results Template
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}

get_header();

global $wp_query;
$search_query = get_search_query();
$found_posts  = $wp_query->found_posts;
?>

<div class="ht-container">
  <div class="n-catpage">
    <!-- Search Query Header & Statistics -->
    <header class="n-sec-head" style="margin-bottom:18px;">
      <h1 style="font-size:1.6rem;font-weight:800;margin:0 0 6px;">
        <?php printf(esc_html__('অনুসন্ধানের ফলাফল: "%s"', 'helptrickbd-edu'), esc_html($search_query)); ?>
      </h1>
      <span class="rule" aria-hidden="true"></span>
    </header>

    <!-- Toolbar with Result Count & Search Form -->
    <div class="n-toolbar" style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;margin-bottom:24px;">
      <span class="cnt" style="font-size:0.95rem;color:var(--ht-text-secondary);font-weight:600;">
        <?php printf(esc_html__('মোট %sটি একাডেমিক রিসোর্স ও হ্যান্ডনোট পাওয়া গেছে', 'helptrickbd-edu'), esc_html(htbd_bengali_number($found_posts))); ?>
      </span>
      <form role="search" method="get" class="ht-search-form" action="<?php echo esc_url(home_url('/')); ?>" style="display:flex;gap:6px;">
        <input type="search" name="s" value="<?php echo esc_attr($search_query); ?>" placeholder="<?php esc_attr_e('পুনরায় খুঁজুন...', 'helptrickbd-edu'); ?>" class="n-modal-input" style="padding:7px 14px;border:1px solid var(--ht-border);border-radius:var(--ht-radius-sm);font-family:var(--ht-font-sans);font-size:0.9rem;">
        <button type="submit" class="ht-btn ht-btn-primary" style="padding:7px 16px;background:var(--ht-primary);color:#ffffff;border:none;border-radius:var(--ht-radius-sm);cursor:pointer;font-weight:600;">
          <?php esc_html_e('খুঁজুন', 'helptrickbd-edu'); ?>
        </button>
      </form>
    </div>

    <?php if (have_posts()) : ?>
      <!-- Results Grid -->
      <div class="n-catgrid" style="display:grid;grid-template-columns:repeat(auto-fill, minmax(280px, 1fr));gap:20px;">
        <?php
        while (have_posts()) :
            the_post();
            $post_id = get_the_ID();
            $thumb   = get_the_post_thumbnail_url($post_id, 'medium');
            if (!$thumb) {
                $thumb = htbd_get_default_thumbnail();
            }
            $cat_data = htbd_primary_category($post_id);
            ?>
            <article class="n-catcard" style="background:var(--ht-surface);border:1px solid var(--ht-border);border-radius:var(--ht-radius-md);overflow:hidden;display:flex;flex-direction:column;transition:transform 0.2s,box-shadow 0.2s;">
              <a href="<?php the_permalink(); ?>" class="thumb-wrap" style="aspect-ratio:16/9;overflow:hidden;position:relative;background:var(--ht-surface-alt);display:block;">
                <img src="<?php echo esc_url($thumb); ?>" alt="<?php the_title_attribute(); ?>" width="300" height="169" loading="lazy" decoding="async" style="width:100%;height:100%;object-fit:cover;">
                <span class="badge" style="position:absolute;top:10px;left:10px;background:var(--ht-primary);color:#ffffff;font-size:0.75rem;padding:3px 8px;border-radius:var(--ht-radius-sm);font-weight:700;">
                  <?php echo esc_html($cat_data['name']); ?>
                </span>
              </a>
              <div class="body" style="padding:16px;display:flex;flex-direction:column;flex:1;">
                <h2 style="font-size:1.1rem;font-weight:700;line-height:1.45;margin:0 0 10px;">
                  <a href="<?php the_permalink(); ?>" style="color:var(--ht-text-primary);text-decoration:none;">
                    <?php the_title(); ?>
                  </a>
                </h2>
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
      <div class="n-pagination" style="margin-top:36px;text-align:center;">
        <?php
        echo paginate_links(array(
            'prev_text' => '&laquo; ' . esc_html__('পূর্ববর্তী', 'helptrickbd-edu'),
            'next_text' => esc_html__('পরবর্তী', 'helptrickbd-edu') . ' &raquo;',
            'type'      => 'list',
        ));
        ?>
      </div>

    <?php else : ?>
      <!-- Comprehensive Empty State -->
      <div class="n-empty-search" style="background:var(--ht-surface);border:1px solid var(--ht-border);border-radius:var(--ht-radius-lg);padding:40px 24px;text-align:center;max-width:680px;margin:30px auto;">
        <div style="font-size:3rem;margin-bottom:12px;" aria-hidden="true">🔍</div>
        <h2 style="font-size:1.35rem;font-weight:800;color:var(--ht-text-primary);margin:0 0 10px;">
          <?php printf(esc_html__('দুঃখিত, "%s" সম্পর্কিত কোনো রিসোর্স পাওয়া যায়নি', 'helptrickbd-edu'), esc_html($search_query)); ?>
        </h2>
        <p style="font-size:0.95rem;color:var(--ht-text-secondary);max-width:480px;margin:0 auto 24px;line-height:1.6;">
          <?php esc_html_e('শব্দের বানান সঠিক আছে কি না পরীক্ষা করুন অথবা অন্য কোনো কি-ওয়ার্ড দিয়ে পুনরায় চেষ্টা করুন। নিচের জনপ্রিয় ক্যাটাগরিগুলো ব্রাউজ করতে পারেন:', 'helptrickbd-edu'); ?>
        </p>

        <!-- Popular Category Shortcuts -->
        <div class="n-pillgrid" style="display:flex;flex-wrap:wrap;justify-content:center;gap:8px;">
          <?php
          $cats = get_categories(array('number' => 8, 'orderby' => 'count', 'order' => 'DESC'));
          foreach ($cats as $c) :
              ?>
              <a href="<?php echo esc_url(get_category_link($c->term_id)); ?>" class="n-pill" style="padding:6px 14px;background:var(--ht-surface-alt);border:1px solid var(--ht-border);border-radius:999px;font-size:0.875rem;color:var(--ht-text-primary);text-decoration:none;font-weight:600;">
                <?php echo esc_html($c->name); ?> (<?php echo esc_html(htbd_bengali_number($c->count)); ?>)
              </a>
              <?php
          endforeach;
          ?>
        </div>
      </div>
    <?php endif; ?>
  </div>
</div>

<?php
get_footer();
