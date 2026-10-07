<?php
/**
 * The Template for displaying 404 pages (Not Found)
 * High-conversion search box & popular recommendations.
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

get_header();
?>

<main id="primary" class="ht-main-site ht-404-site">
    <div class="ht-container">

        <!-- Breadcrumbs Navigation -->
        <?php ht_breadcrumbs(); ?>

        <div class="ht-404-wrapper">
            <div class="ht-404-icon-wrap">
                <?php ht_m3_icon('help_outline', 64, 'ht-icon-404'); ?>
            </div>
            <h1 class="ht-404-title">৪০৪: কাঙ্ক্ষিত পৃষ্ঠাটি পাওয়া যায়নি</h1>
            <p class="ht-404-desc">
                আপনি যে পেজটিতে প্রবেশের চেষ্টা করছেন সেটি হয়তো মুছে ফেলা হয়েছে, নাম পরিবর্তন হয়েছে অথবা লিংকটি ভুল ছিল। অনুগ্রহ করে নিচে অনুসন্ধান করুন অথবা আমাদের জনপ্রিয় বিভাগগুলো দেখুন।
            </p>

            <!-- Search Form -->
            <div class="ht-404-search-box">
                <?php get_search_form(); ?>
            </div>

            <!-- Popular Quick Links -->
            <div class="ht-404-suggestions">
                <span class="ht-404-sug-title">জনপ্রিয় বিষয়শ্রেণী:</span>
                <div class="ht-404-tags">
                    <a href="<?php echo esc_url(home_url('/category/national-university/')); ?>" class="ht-tab-btn">জাতীয় বিশ্ববিদ্যালয়</a>
                    <a href="<?php echo esc_url(home_url('/category/education-guide/')); ?>" class="ht-tab-btn">শিক্ষা গাইড</a>
                    <a href="<?php echo esc_url(home_url('/category/ssc-dakhil/')); ?>" class="ht-tab-btn">এসএসসি ও দাখিল</a>
                    <a href="<?php echo esc_url(home_url('/category/political-science/')); ?>" class="ht-tab-btn">রাষ্ট্রবিজ্ঞান</a>
                    <a href="<?php echo esc_url(home_url('/category/ict-technology/')); ?>" class="ht-tab-btn">আইসিটি</a>
                </div>
            </div>

            <div class="ht-404-back-home">
                <a href="<?php echo esc_url(home_url('/')); ?>" class="ht-btn ht-btn-primary">
                    <?php ht_m3_icon('home', 18); ?>
                    <span>হোমপেজে ফিরে যান</span>
                </a>
            </div>

        </div>

    </div><!-- .ht-container -->
</main><!-- #primary -->

<?php
get_footer();
