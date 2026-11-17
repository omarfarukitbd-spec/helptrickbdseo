<?php
/**
 * The Template for displaying Author Archive pages
 * Author Profile Card, Total Posts Count, E-E-A-T credentials & posts grid.
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

get_header();

$curauth = (get_query_var('author_name')) ? get_user_by('slug', get_query_var('author_name')) : get_userdata(get_query_var('author'));
$total_author_posts = count_user_posts($curauth->ID, 'post', true);
?>

<main id="primary" class="ht-main-site ht-author-site">
    <div class="ht-container">

        <!-- Breadcrumbs Navigation -->
        <?php ht_breadcrumbs(); ?>

        <!-- Author Profile Banner -->
        <?php
        $is_bn = function_exists('ht_is_bangla_locale') ? ht_is_bangla_locale() : true;
        ?>
        <header class="ht-author-profile-card">
            <div class="ht-author-profile-avatar">
                <?php echo get_avatar($curauth->ID, 96, '', '', ['class' => 'ht-avatar-lg']); ?>
            </div>
            <div class="ht-author-profile-info">
                <div class="ht-author-profile-badge-row">
                    <span class="ht-author-role"><?php echo $is_bn ? esc_html__('শিক্ষক ও লেখক', 'helptrickbd') : esc_html__('Educator & Author', 'helptrickbd'); ?></span>
                    <?php ht_eeat_badge(); ?>
                </div>
                <h1 class="ht-author-profile-name">
                    <?php echo esc_html($curauth->display_name); ?>
                </h1>
                <p class="ht-author-profile-bio">
                    <?php
                    $bio = get_the_author_meta('description', $curauth->ID);
                    $default_bio = $is_bn
                        ? 'হেল্পট্রিকবিডির নিয়মিত লেখক, গবেষক ও শিক্ষা বিষয়ক কন্টেন্ট বিশেষজ্ঞ।'
                        : 'Education and technology researcher, writer, and regular content contributor at HelpTrickBD.';
                    echo esc_html($bio ? $bio : $default_bio);
                    ?>
                </p>
                <div class="ht-author-profile-meta">
                    <span class="ht-author-count">
                        <?php ht_m3_icon('auto_stories', 16); ?>
                        <strong><?php echo esc_html(function_exists('ht_number') ? ht_number($total_author_posts) : (function_exists('ht_bn_number') ? ht_bn_number($total_author_posts) : $total_author_posts)); ?></strong> <?php echo $is_bn ? esc_html__('টি প্রকাশিত লেখা', 'helptrickbd') : esc_html__('Published Articles', 'helptrickbd'); ?>
                    </span>
                </div>
            </div>
        </header>

        <div class="ht-layout-row">

            <!-- Primary 70% Content Area -->
            <div class="ht-content-area">

                <div class="ht-section-header">
                    <h2 class="ht-section-title">
                        <?php ht_m3_icon('format_list_bulleted', 20, 'ht-icon-primary'); ?>
                        <span><?php echo $is_bn ? esc_html__('লেখকের সকল আর্টিকেল', 'helptrickbd') : esc_html__('Articles by Author', 'helptrickbd'); ?></span>
                    </h2>
                </div>

                <?php if (have_posts()) : ?>
                    <div class="ht-cards-grid">
                        <?php
                        while (have_posts()) :
                            the_post();
                            get_template_part('template-parts/content', 'card');
                        endwhile;
                        ?>
                    </div><!-- .ht-cards-grid -->

                    <!-- Numbered Pagination -->
                    <div class="ht-pagination-wrap">
                        <?php
                        $prev_text = $is_bn ? esc_html__('পূর্ববর্তী', 'helptrickbd') : esc_html__('Previous', 'helptrickbd');
                        $next_text = $is_bn ? esc_html__('পরবর্তী', 'helptrickbd') : esc_html__('Next', 'helptrickbd');
                        the_posts_pagination([
                            'prev_text' => ht_m3_icon('arrow_back', 16, '', false) . ' ' . $prev_text,
                            'next_text' => $next_text . ' ' . ht_m3_icon('arrow_forward', 16, '', false),
                        ]);
                        ?>
                    </div>

                <?php else : ?>
                    <p class="ht-no-posts"><?php echo $is_bn ? esc_html__('এই লেখকের কোনো প্রকাশিত পোস্ট পাওয়া যায়নি।', 'helptrickbd') : esc_html__('No posts published by this author yet.', 'helptrickbd'); ?></p>
                <?php endif; ?>

            </div><!-- .ht-content-area -->

            <!-- Sidebar (30%) -->
            <aside class="ht-sidebar-area">
                <?php get_sidebar(); ?>
            </aside>

        </div><!-- .ht-layout-row -->

    </div><!-- .ht-container -->
</main><!-- #primary -->

<?php
get_footer();
