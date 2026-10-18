<?php
/**
 * The Template for displaying 404 pages (Not Found)
 * 100% Google Search Central & Google AdSense Policy Compliant.
 * SolaimanLipi High-Precision Typography, Interactive Search, Category Pills & Dynamic Post Grid.
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

// Ensure strict HTTP 404 response header & prevent incorrect search engine caching
status_header(404);
nocache_headers();

get_header();
?>

<main id="primary" class="ht-main-site ht-404-site">
    <div class="ht-container">

        <!-- Breadcrumbs Navigation -->
        <?php ht_breadcrumbs(); ?>

        <div class="ht-404-wrapper">

            <!-- 404 Hero Card -->
            <div class="ht-404-hero-card">
                <div class="ht-404-badge-wrap">
                    <span class="ht-404-status-badge">
                        <?php ht_m3_icon('help_outline', 16); ?>
                        <span>এরর ৪০৪</span>
                    </span>
                    <div class="ht-404-num" aria-hidden="true">404</div>
                </div>

                <h1 class="ht-404-title"><?php esc_html_e('দুঃখিত, কাঙ্ক্ষিত পাতাটি পাওয়া যায়নি!', 'helptrickbd'); ?></h1>
                <p class="ht-404-desc">
                    <?php esc_html_e('আপনি যে পাতা বা লিঙ্কটি খুঁজছেন তা হয়তো সরানো হয়েছে, নাম পরিবর্তন করা হয়েছে অথবা সাময়িকভাবে অনুপলব্ধ। নিচের সার্চ বক্স ব্যবহার করে অথবা জনপ্রিয় ক্যাটাগরিগুলো থেকে আপনার প্রয়োজনীয় তথ্যটি সহজে খুঁজে নিতে পারেন।', 'helptrickbd'); ?>
                </p>

                <!-- Prominent Search Bar -->
                <div class="ht-404-search-box">
                    <form role="search" method="get" class="ht-404-search-form" action="<?php echo esc_url(home_url('/')); ?>">
                        <label for="ht-404-search-field" class="screen-reader-text"><?php esc_html_e('ওয়েবসাইট অনুসন্ধান', 'helptrickbd'); ?></label>
                        <div class="ht-404-search-input-wrap">
                            <span class="ht-404-search-icon" aria-hidden="true">
                                <?php ht_m3_icon('search', 22); ?>
                            </span>
                            <input 
                                type="search" 
                                id="ht-404-search-field"
                                class="ht-404-search-input" 
                                placeholder="<?php esc_attr_e('আপনি কী খুঁজছেন? যেমন: ডিগ্রি রুটিন, বিসিএস প্রস্তুতি...', 'helptrickbd'); ?>" 
                                value="<?php echo esc_attr(get_search_query()); ?>" 
                                name="s" 
                                required 
                                autocomplete="off"
                            />
                            <button type="submit" class="ht-404-search-btn" aria-label="<?php esc_attr_e('অনুসন্ধান করুন', 'helptrickbd'); ?>">
                                <span><?php esc_html_e('অনুসন্ধান', 'helptrickbd'); ?></span>
                                <?php ht_m3_icon('arrow_forward', 18); ?>
                            </button>
                        </div>
                    </form>
                </div>

                <!-- Popular Categories Pills -->
                <div class="ht-404-categories-section">
                    <div class="ht-404-cat-label">
                        <?php ht_m3_icon('category', 16); ?>
                        <span><?php esc_html_e('জনপ্রিয় বিষয় ও ক্যাটাগরি:', 'helptrickbd'); ?></span>
                    </div>
                    <div class="ht-404-cat-pills">
                        <a href="<?php echo esc_url(home_url('/category/national-university/')); ?>" class="ht-404-cat-pill ht-cat-nu">
                            <?php ht_m3_icon('school', 16); ?>
                            <span><?php esc_html_e('জাতীয় বিশ্ববিদ্যালয়', 'helptrickbd'); ?></span>
                        </a>
                        <a href="<?php echo esc_url(home_url('/category/job-preparation/')); ?>" class="ht-404-cat-pill ht-cat-job">
                            <?php ht_m3_icon('work', 16); ?>
                            <span><?php esc_html_e('বিসিএস ও চাকরি প্রস্তুতি', 'helptrickbd'); ?></span>
                        </a>
                        <a href="<?php echo esc_url(home_url('/category/education-guide/')); ?>" class="ht-404-cat-pill ht-cat-edu">
                            <?php ht_m3_icon('menu_book', 16); ?>
                            <span><?php esc_html_e('শিক্ষা সহায়িকা ও রুটিন', 'helptrickbd'); ?></span>
                        </a>
                        <a href="<?php echo esc_url(home_url('/category/ssc-dakhil/')); ?>" class="ht-404-cat-pill ht-cat-ssc">
                            <?php ht_m3_icon('history_edu', 16); ?>
                            <span><?php esc_html_e('এসএসসি ও দাখিল', 'helptrickbd'); ?></span>
                        </a>
                        <a href="<?php echo esc_url(home_url('/category/ict-technology/')); ?>" class="ht-404-cat-pill ht-cat-ict">
                            <?php ht_m3_icon('laptop_mac', 16); ?>
                            <span><?php esc_html_e('আইসিটি ও প্রযুক্তি', 'helptrickbd'); ?></span>
                        </a>
                        <a href="<?php echo esc_url(home_url('/category/political-science/')); ?>" class="ht-404-cat-pill ht-cat-poli">
                            <?php ht_m3_icon('balance', 16); ?>
                            <span><?php esc_html_e('রাষ্ট্রবিজ্ঞান বিভাগ', 'helptrickbd'); ?></span>
                        </a>
                    </div>
                </div>

                <!-- Recovery Actions -->
                <div class="ht-404-actions">
                    <a href="<?php echo esc_url(home_url('/')); ?>" class="ht-btn ht-btn-primary ht-404-home-btn">
                        <?php ht_m3_icon('home', 20); ?>
                        <span><?php esc_html_e('মূল পাতায় ফিরে যান', 'helptrickbd'); ?></span>
                    </a>
                    <a href="<?php echo esc_url(home_url('/contact/')); ?>" class="ht-btn ht-404-contact-btn">
                        <?php ht_m3_icon('chat_bubble_outline', 18); ?>
                        <span><?php esc_html_e('ভুল লিঙ্ক রিপোর্ট / যোগাযোগ', 'helptrickbd'); ?></span>
                    </a>
                </div>
            </div>

            <!-- Trending / Recommended Articles Section -->
            <section class="ht-404-articles-section" aria-labelledby="ht-404-rec-title">
                <div class="ht-404-section-head">
                    <div class="ht-404-section-badge">
                        <?php ht_m3_icon('trending_up', 18); ?>
                        <span><?php esc_html_e('প্রয়োজনীয় গাইডলাইন', 'helptrickbd'); ?></span>
                    </div>
                    <h2 id="ht-404-rec-title" class="ht-404-section-title"><?php esc_html_e('জনপ্রিয় ও সর্বশেষ প্রকাশনাসমূহ', 'helptrickbd'); ?></h2>
                    <p class="ht-404-section-sub"><?php esc_html_e('আপনার কাঙ্ক্ষিত তথ্যটি হয়তো নিচের শীর্ষ আর্টিকেলগুলোর মধ্যে রয়েছে:', 'helptrickbd'); ?></p>
                </div>

                <div class="ht-cards-grid ht-404-cards-grid">
                    <?php
                    $ht_rec_query = new WP_Query([
                        'post_type'           => 'post',
                        'post_status'         => 'publish',
                        'posts_per_page'      => 4,
                        'ignore_sticky_posts' => true,
                        'orderby'             => 'date',
                        'order'               => 'DESC',
                    ]);

                    if ($ht_rec_query->have_posts()) :
                        while ($ht_rec_query->have_posts()) :
                            $ht_rec_query->the_post();
                            get_template_part('template-parts/content', 'card');
                        endwhile;
                        wp_reset_postdata();
                    endif;
                    ?>
                </div>
            </section>

        </div><!-- .ht-404-wrapper -->

    </div><!-- .ht-container -->
</main><!-- #primary -->

<?php
get_footer();
