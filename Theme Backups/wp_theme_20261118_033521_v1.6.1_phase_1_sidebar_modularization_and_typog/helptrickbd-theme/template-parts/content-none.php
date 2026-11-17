<?php
/**
 * Template part for displaying a message that posts cannot be found
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}
?>

<div class="ht-empty-state">
    <?php ht_m3_icon('search', 48, 'ht-empty-icon'); ?>
    <h3 class="ht-empty-title">
        <?php
        if (is_search()) :
            esc_html_e('কোনো ফলাফল পাওয়া যায়নি', 'helptrickbd');
        else :
            esc_html_e('কোনো তথ্য বা পোস্ট পাওয়া যায়নি', 'helptrickbd');
        endif;
        ?>
    </h3>
    <p class="ht-empty-desc">
        <?php
        if (is_home() && current_user_can('publish_posts')) :
            printf(
                wp_kses(
                    /* translators: 1: link to WP admin new post page. */
                    __('প্রথম পোস্ট প্রকাশ করতে প্রস্তুত? <a href="%1$s">এখানে শুরু করুন</a>।', 'helptrickbd'),
                    ['a' => ['href' => []]]
                ),
                esc_url(admin_url('post-new.php'))
            );
        elseif (is_search()) :
            esc_html_e('দুঃখিত, আপনার অনুসন্ধানের সাথে মিলে এমন কোনো হ্যান্ডনোট বা গাইড পাওয়া যায়নি। অনুগ্রহ করে ভিন্ন কি-ওয়ার্ড দিয়ে আবার চেষ্টা করুন।', 'helptrickbd');
        else :
            esc_html_e('আপনি যা খুঁজছেন তা এই মুহূর্তে পাওয়া যায়নি। উপরের সার্চ বক্সে কি-ওয়ার্ড লিখে অনুসন্ধান করতে পারেন।', 'helptrickbd');
        endif;
        ?>
    </p>

    <div class="ht-empty-search-box">
        <?php get_search_form(); ?>
    </div>
</div>
