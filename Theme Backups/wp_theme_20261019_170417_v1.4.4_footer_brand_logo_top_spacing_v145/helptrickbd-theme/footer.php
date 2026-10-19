<?php
/**
 * The Footer for HelpTrickBD Pro
 * 4-Column Footer, Mobile Bottom Dock, Circular Progress, Spotlight Modal & Bookmarks Drawer.
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}
?>
    </div><!-- #content -->

    <!-- Main Footer -->
    <footer id="colophon" class="ht-footer">
        
        <!-- Pre-Footer Community Bar -->
        <?php if (get_theme_mod('ht_pre_footer_enable', true)) : ?>
            <div class="ht-pre-footer">
                <div class="ht-container ht-pre-footer-inner">
                    <div class="ht-pre-footer-content">
                        <div class="ht-pre-footer-icon-badge" aria-hidden="true">
                            <?php ht_m3_icon('campaign', 26); ?>
                        </div>
                        <div class="ht-pre-footer-text">
                            <span class="ht-pre-footer-title"><?php echo esc_html(get_theme_mod('ht_pre_footer_title', 'সবার আগে পরীক্ষার রুটিন ও স্পেশাল সাজেশন পেতে চান?')); ?></span>
                            <span class="ht-pre-footer-sub"><?php echo esc_html(get_theme_mod('ht_pre_footer_sub', 'আমাদের অফিসিয়াল হোয়াটসঅ্যাপ ও টেলিগ্রাম স্টাডি চ্যানেলে যুক্ত হোন।')); ?></span>
                        </div>
                    </div>
                    <div class="ht-pre-footer-btns">
                        <?php
                        $wa_link = get_theme_mod('ht_whatsapp_url', 'https://whatsapp.com/channel/0029Vb956jgCHDyrx1wkUh2a');
                        if (empty($wa_link) || $wa_link === 'https://chat.whatsapp.com/') {
                            $wa_link = 'https://whatsapp.com/channel/0029Vb956jgCHDyrx1wkUh2a';
                        }
                        $tg_link = get_theme_mod('ht_telegram_url', 'https://t.me/helptrickbd_official');
                        ?>
                        <a href="<?php echo esc_url($wa_link); ?>" target="_blank" rel="noopener noreferrer" class="ht-btn ht-btn-whatsapp">
                            <?php ht_m3_icon('whatsapp', 18); ?>
                            <span>হোয়াটসঅ্যাপ চ্যানেল</span>
                        </a>
                        <a href="<?php echo esc_url($tg_link); ?>" target="_blank" rel="noopener noreferrer" class="ht-btn ht-btn-telegram">
                            <?php ht_m3_icon('telegram', 18); ?>
                            <span>টেলিগ্রাম চ্যানেল</span>
                        </a>
                    </div>
                </div>
            </div>
        <?php endif; ?>

        <!-- 4-Column Main Footer Grid -->
        <div class="ht-container ht-footer-main">
            <div class="ht-footer-grid">

                <!-- Column 1: Brand & Bio -->
                <div class="ht-footer-col ht-footer-col-brand">
                    <a href="<?php echo esc_url(home_url('/')); ?>" class="ht-footer-logo">
                        <span class="ht-logo-text">HelpTrick<span class="ht-logo-accent">BD</span></span>
                    </a>
                    <p class="ht-footer-desc">
                        <?php echo esc_html(get_theme_mod('ht_footer_desc', 'হেল্পট্রিকবিডি একটি উন্মুক্ত শিক্ষামূলক তথ্য ও প্রযুক্তি পোর্টাল। এখানে জাতীয় বিশ্ববিদ্যালয়ের পরীক্ষার রুটিন, এসএসসি ও দাখিল সাজেশন, বিসিএস প্রস্তুতি, রাষ্ট্রবিজ্ঞান হ্যান্ডনোট ও তথ্যপ্রযুক্তি নির্দেশিকা নিয়মিত প্রকাশ করা হয়।')); ?>
                    </p>
                    <div class="ht-footer-trust">
                        <?php ht_m3_icon('verified', 16, 'ht-icon-verified'); ?>
                        <span><?php echo esc_html(get_theme_mod('ht_footer_trust_text', '১০০% বিশ্বস্ত ও শিক্ষাবিদ দ্বারা যাচাইকৃত কনটেন্ট')); ?></span>
                    </div>
                </div>

                <!-- Column 2: Quick Links -->
                <div class="ht-footer-col">
                    <h4 class="ht-footer-title"><?php esc_html_e('গুরুত্বপূর্ণ বিষয়সমূহ', 'helptrickbd'); ?></h4>
                    <ul class="ht-footer-links">
                        <li><a href="<?php echo esc_url(home_url('/category/national-university/')); ?>"><?php esc_html_e('জাতীয় বিশ্ববিদ্যালয়', 'helptrickbd'); ?></a></li>
                        <li><a href="<?php echo esc_url(home_url('/category/education-guide/')); ?>"><?php esc_html_e('এডুকেশন ও রুটিন', 'helptrickbd'); ?></a></li>
                        <li><a href="<?php echo esc_url(home_url('/category/ssc-dakhil/')); ?>"><?php esc_html_e('এসএসসি ও দাখিল সাজেশন', 'helptrickbd'); ?></a></li>
                        <li><a href="<?php echo esc_url(home_url('/category/political-science/')); ?>"><?php esc_html_e('রাষ্ট্রবিজ্ঞান হ্যান্ডনোট', 'helptrickbd'); ?></a></li>
                        <li><a href="<?php echo esc_url(home_url('/category/ict-technology/')); ?>"><?php esc_html_e('আইসিটি ও প্রযুক্তি', 'helptrickbd'); ?></a></li>
                        <li><a href="<?php echo esc_url(home_url('/category/job-preparation/')); ?>"><?php esc_html_e('চাকরি ও বিসিএস প্রস্তুতি', 'helptrickbd'); ?></a></li>
                    </ul>
                </div>

                <!-- Column 3: Exam Categories & Guides -->
                <div class="ht-footer-col">
                    <h4 class="ht-footer-title"><?php esc_html_e('রুটিন ও গাইড', 'helptrickbd'); ?></h4>
                    <?php if (has_nav_menu('footer-menu')) : ?>
                        <?php
                        wp_nav_menu([
                            'theme_location' => 'footer-menu',
                            'container'      => false,
                            'menu_class'     => 'ht-footer-links',
                            'depth'          => 1,
                            'fallback_cb'    => false,
                        ]);
                        ?>
                    <?php else : ?>
                        <ul class="ht-footer-links">
                            <li><a href="<?php echo esc_url(home_url('/nu-honours-2nd-year-exam-routine-2026/')); ?>"><?php esc_html_e('অনার্স ২য় বর্ষ রুটিন ২০২৬', 'helptrickbd'); ?></a></li>
                            <li><a href="<?php echo esc_url(home_url('/nu-honours-2nd-year-exam-guide-and/')); ?>"><?php esc_html_e('অনার্স প্রমোশন ও পাস মার্ক নিয়ম', 'helptrickbd'); ?></a></li>
                            <li><a href="<?php echo esc_url(home_url('/dhaka-board-certificate-name-age-correction-guide-2026/')); ?>"><?php esc_html_e('সার্টিফিকেট নাম ও বয়স সংশোধন', 'helptrickbd'); ?></a></li>
                            <li><a href="<?php echo esc_url(home_url('/nu-cgpa-calculator/')); ?>"><?php esc_html_e('এনইউ সিজিপিএ ক্যালকুলেটর', 'helptrickbd'); ?></a></li>
                            <li><a href="<?php echo esc_url(home_url('/category/islamic-article/')); ?>"><?php esc_html_e('ইসলামিক প্রবন্ধ ও দোয়া', 'helptrickbd'); ?></a></li>
                        </ul>
                    <?php endif; ?>
                </div>

                <!-- Column 4: Legal & Pages -->
                <div class="ht-footer-col">
                    <h4 class="ht-footer-title"><?php esc_html_e('আইনি ও সহায়তা', 'helptrickbd'); ?></h4>
                    <ul class="ht-footer-links">
                        <li><a href="<?php echo esc_url(home_url('/about-us/')); ?>"><?php esc_html_e('আমাদের সম্পর্কে', 'helptrickbd'); ?></a></li>
                        <li><a href="<?php echo esc_url(home_url('/contact-us/')); ?>"><?php esc_html_e('যোগাযোগ', 'helptrickbd'); ?></a></li>
                        <li><a href="<?php echo esc_url(home_url('/privacy-policy/')); ?>"><?php esc_html_e('গোপনীয়তা নীতিমালা', 'helptrickbd'); ?></a></li>
                        <li><a href="<?php echo esc_url(home_url('/terms-conditions/')); ?>"><?php esc_html_e('শর্তাবলী', 'helptrickbd'); ?></a></li>
                        <li><a href="<?php echo esc_url(home_url('/disclaimer/')); ?>"><?php esc_html_e('দাবিত্যাগ (Disclaimer)', 'helptrickbd'); ?></a></li>
                    </ul>
                </div>

            </div>
        </div>

        <!-- Footer Bottom Bar: Copyright -->
        <div class="ht-footer-bottom">
            <div class="ht-container ht-footer-bottom-inner">
                <div class="ht-copyright">
                    <?php
                    $custom_copy = get_theme_mod('ht_footer_copyright', '');
                    if (!empty($custom_copy)) :
                        echo esc_html($custom_copy);
                    else :
                    ?>
                        &copy; <?php echo esc_html(date('Y')); ?> <a href="<?php echo esc_url(home_url('/')); ?>">HelpTrickBD.com</a> &mdash; <?php esc_html_e('সর্বস্বত্ব সংরক্ষিত।', 'helptrickbd'); ?>
                    <?php endif; ?>
                </div>
                <div class="ht-credit">
                    <?php echo esc_html(get_theme_mod('ht_footer_credit', esc_html__('উন্মুক্ত শিক্ষা ও জ্ঞান প্রসারে নিবেদিত', 'helptrickbd'))); ?>
                </div>
            </div>
        </div>

    </footer>

    <?php if (get_theme_mod('ht_mobile_dock_enable', true)) : ?>
        <!-- Mobile Bottom App Dock -->
        <nav class="ht-mobile-dock" aria-label="<?php esc_attr_e('Mobile Navigation Dock', 'helptrickbd'); ?>">
            <a href="<?php echo esc_url(home_url('/')); ?>" class="ht-dock-item <?php echo is_front_page() ? 'ht-active' : ''; ?>">
                <?php ht_m3_icon('home', 20); ?>
                <span>হোম</span>
            </a>
            <button class="ht-dock-item" id="ht-dock-menu-btn" aria-label="<?php esc_attr_e('ক্যাটাগরি', 'helptrickbd'); ?>">
                <?php ht_m3_icon('category', 20); ?>
                <span>ক্যাটাগরি</span>
            </button>
            <a href="<?php echo esc_url(get_theme_mod('ht_telegram_url', 'https://t.me/helptrickbd_official')); ?>" target="_blank" rel="noopener noreferrer" class="ht-dock-item ht-dock-telegram" aria-label="<?php esc_attr_e('টেলিগ্রাম চ্যানেল', 'helptrickbd'); ?>">
                <?php ht_m3_icon('telegram', 20); ?>
                <span>টেলিগ্রাম</span>
            </a>
            <button class="ht-dock-item" id="ht-dock-bookmark-btn" aria-label="<?php esc_attr_e('পড়ার তালিকা', 'helptrickbd'); ?>">
                <?php ht_m3_icon('bookmark', 20); ?>
                <span class="ht-dock-badge" id="ht-dock-bm-count">0</span>
                <span>পড়ার তালিকা</span>
            </button>
            <button class="ht-dock-item" id="ht-dock-search-btn" aria-label="<?php esc_attr_e('অনুসন্ধান', 'helptrickbd'); ?>">
                <?php ht_m3_icon('search', 20); ?>
                <span>অনুসন্ধান</span>
            </button>
        </nav>
    <?php endif; ?>

    <?php if (get_theme_mod('ht_back_to_top_enable', true)) : ?>
        <!-- Circular Scroll-to-Top Progress Indicator -->
        <button class="ht-scroll-top" id="ht-scroll-top" aria-label="<?php esc_attr_e('Scroll to top', 'helptrickbd'); ?>" title="<?php esc_attr_e('Scroll to top', 'helptrickbd'); ?>">
            <svg class="ht-progress-ring" width="48" height="48" viewBox="0 0 48 48">
                <circle class="ht-progress-bg" cx="24" cy="24" r="20" fill="none" stroke-width="3"></circle>
                <circle class="ht-progress-bar" id="ht-progress-circle" cx="24" cy="24" r="20" fill="none" stroke-width="3" stroke-dasharray="125.66" stroke-dashoffset="125.66"></circle>
            </svg>
            <span class="ht-scroll-icon"><?php ht_m3_icon('keyboard_arrow_up', 22); ?></span>
        </button>
    <?php endif; ?>

    <!-- "Ctrl+K" Spotlight Instant Search Modal -->
    <div class="ht-modal ht-spotlight-modal" id="ht-spotlight-modal" aria-hidden="true" role="dialog" aria-label="<?php esc_attr_e('তাত্ক্ষণিক অনুসন্ধান', 'helptrickbd'); ?>">
        <div class="ht-spotlight-overlay" id="ht-spotlight-overlay"></div>
        <div class="ht-spotlight-dialog">
            <div class="ht-spotlight-header">
                <?php ht_m3_icon('search', 22, 'ht-spotlight-icon'); ?>
                <input type="search" id="ht-spotlight-input" class="ht-spotlight-input" placeholder="<?php esc_attr_e('হ্যান্ডনোট, রুটিন বা বিষয় লিখে খুঁজুন...', 'helptrickbd'); ?>" autocomplete="off" enterkeyhint="search">
                <button class="ht-spotlight-close" id="ht-spotlight-close" aria-label="<?php esc_attr_e('সার্চ বন্ধ করুন', 'helptrickbd'); ?>">
                    <kbd>ESC</kbd>
                </button>
            </div>
            <div class="ht-spotlight-body" id="ht-spotlight-results">
                <!-- Trending suggestions default state -->
                <div class="ht-spotlight-trending">
                    <span class="ht-spotlight-section-title"><?php esc_html_e('জনপ্রিয় অনুসন্ধানসমূহ', 'helptrickbd'); ?></span>
                    <div class="ht-trending-tags">
                        <button class="ht-trending-tag" data-query="অনার্স ২য় বর্ষ রুটিন">অনার্স ২য় বর্ষ রুটিন</button>
                        <button class="ht-trending-tag" data-query="এসএসসি বাংলা ১ম পত্র">এসএসসি বাংলা ১ম পত্র</button>
                        <button class="ht-trending-tag" data-query="সার্টিফিকেট নাম সংশোধন">সার্টিফিকেট সংশোধন</button>
                        <button class="ht-trending-tag" data-query="রাষ্ট্রবিজ্ঞান হ্যান্ডনোট">রাষ্ট্রবিজ্ঞান হ্যান্ডনোট</button>
                        <button class="ht-trending-tag" data-query="কম্পিউটার ভাইরাস">কম্পিউটার ভাইরাস</button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- LocalStorage Saved Bookmarks Drawer ("পড়ার তালিকা") -->
    <aside class="ht-drawer ht-bookmarks-drawer" id="ht-bookmarks-drawer" aria-hidden="true">
        <div class="ht-drawer-header">
            <div class="ht-drawer-title-wrap">
                <?php ht_m3_icon('bookmark', 20); ?>
                <span class="ht-drawer-title"><?php esc_html_e('আপনার পড়ার তালিকা', 'helptrickbd'); ?></span>
            </div>
            <button class="ht-drawer-close" id="ht-bm-close" aria-label="<?php esc_attr_e('ড্রয়ার বন্ধ করুন', 'helptrickbd'); ?>">
                <?php ht_m3_icon('close', 20); ?>
            </button>
        </div>
        <div class="ht-drawer-body" id="ht-bookmarks-list">
            <!-- Dynamically populated from localStorage -->
            <div class="ht-empty-bookmarks">
                <?php ht_m3_icon('bookmark', 48, 'ht-empty-icon'); ?>
                <p><?php esc_html_e('আপনার পড়ার তালিকা বর্তমানে খালি রয়েছে।', 'helptrickbd'); ?></p>
                <span><?php esc_html_e('যেকোনো পোস্ট সেভ করে অফলাইনে পড়তে বুকমার্ক আইকনে ক্লিক করুন।', 'helptrickbd'); ?></span>
            </div>
        </div>
        <div class="ht-drawer-footer">
            <button class="ht-btn ht-btn-sm ht-btn-outline" id="ht-clear-bookmarks"><?php esc_html_e('তালিকা খালি করুন', 'helptrickbd'); ?></button>
        </div>
    </aside>
    <div class="ht-drawer-overlay" id="ht-bm-overlay"></div>

    <!-- Polite AdBlocker Notice Modal -->
    <?php if (get_theme_mod('ht_adblock_notice_enable', true)) : ?>
        <div class="ht-modal ht-adblock-modal" id="ht-adblock-modal" aria-hidden="true">
            <div class="ht-adblock-dialog">
                <?php ht_m3_icon('shield', 44, 'ht-adblock-icon'); ?>
                <h3 class="ht-adblock-title"><?php esc_html_e('একটি বিনীত অনুরোধ', 'helptrickbd'); ?></h3>
                <p class="ht-adblock-desc">
                    <?php esc_html_e('হেল্পট্রিকবিডি একটি উন্মুক্ত শিক্ষামূলক প্ল্যাটফর্ম। শিক্ষার্থীদের জন্য মানসম্মত কনটেন্ট নিয়মিত প্রকাশ করতে আমাদের কার্যক্রম বিজ্ঞাপন সমর্থিত। অনুগ্রহ করে আপনার অ্যাডব্লকারে সাইটটি অনুমোদিত (হোয়াইটলিস্ট) করুন।', 'helptrickbd'); ?>
                </p>
                <button class="ht-btn ht-btn-primary" id="ht-adblock-dismiss"><?php esc_html_e('বুঝেছি, ধন্যবাদ', 'helptrickbd'); ?></button>
            </div>
        </div>
    <?php endif; ?>

    <!-- Cookie Consent Banner -->
    <div class="ht-cookie-banner" id="ht-cookie-banner">
        <div class="ht-cookie-inner">
            <div class="ht-cookie-text">
                <?php ht_m3_icon('shield', 18, 'ht-cookie-icon'); ?>
                <span><?php esc_html_e('আপনার ব্রাউজিং অভিজ্ঞতা উন্নত করতে এবং সঠিক শিক্ষামূলক তথ্য প্রদানে আমরা কুকিজ ব্যবহার করি। সাইটটি ব্যবহারের মাধ্যমে আপনি আমাদের নীতিমালায় সম্মত হচ্ছেন।', 'helptrickbd'); ?></span>
            </div>
            <div class="ht-cookie-actions">
                <a href="<?php echo esc_url(home_url('/privacy-policy/')); ?>" class="ht-cookie-link"><?php esc_html_e('বিস্তারিত পড়ুন', 'helptrickbd'); ?></a>
                <button class="ht-btn ht-btn-sm ht-btn-primary" id="ht-cookie-accept"><?php esc_html_e('সম্মতি দিচ্ছি', 'helptrickbd'); ?></button>
            </div>
        </div>
    </div>

</div><!-- #page -->

<?php wp_footer(); ?>
</body>
</html>
