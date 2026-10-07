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
                    <div class="ht-pre-footer-text">
                        <span class="ht-pre-footer-title"><?php echo esc_html(get_theme_mod('ht_pre_footer_title', 'পরীক্ষার রুটিন ও স্পেশাল সাজেশন সবার আগে পেতে চান?')); ?></span>
                        <span class="ht-pre-footer-sub"><?php echo esc_html(get_theme_mod('ht_pre_footer_sub', 'আমাদের অফিসিয়াল হোয়াটসঅ্যাপ ও টেলিগ্রাম গ্রুপে যুক্ত হোন।')); ?></span>
                    </div>
                    <div class="ht-pre-footer-btns">
                        <?php
                        $wa_link = get_theme_mod('ht_whatsapp_url', 'https://chat.whatsapp.com/');
                        $tg_link = get_theme_mod('ht_telegram_url', 'https://t.me/helptrickbd');
                        ?>
                        <a href="<?php echo esc_url($wa_link); ?>" target="_blank" rel="noopener noreferrer" class="ht-btn ht-btn-whatsapp">
                            <?php ht_m3_icon('whatsapp', 18); ?>
                            <span>WhatsApp গ্রুপ</span>
                        </a>
                        <a href="<?php echo esc_url($tg_link); ?>" target="_blank" rel="noopener noreferrer" class="ht-btn ht-btn-telegram">
                            <?php ht_m3_icon('telegram', 18); ?>
                            <span>Telegram চ্যানেল</span>
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
                        <?php echo esc_html(get_theme_mod('ht_footer_desc', 'Help Trick BD বাংলাদেশের শিক্ষার্থীদের জন্য জাতীয় বিশ্ববিদ্যালয়, এসএসসি/দাখিল, বিসিএস প্রস্তুতি, রাষ্ট্রবিজ্ঞান অ্যাকাডেমিক হ্যান্ডনোট এবং আধুনিক তথ্যপ্রযুক্তি নির্দেশিকার একটি নির্ভরযোগ্য শিক্ষা পোর্টাল।')); ?>
                    </p>
                    <div class="ht-footer-trust">
                        <?php ht_m3_icon('verified', 16, 'ht-icon-verified'); ?>
                        <span><?php echo esc_html(get_theme_mod('ht_footer_trust_text', '১০০% প্রামাণ্য তথ্য ও শিক্ষক-পর্যালোচিত কন্টেন্ট')); ?></span>
                    </div>
                </div>

                <!-- Column 2: Quick Links -->
                <div class="ht-footer-col">
                    <h4 class="ht-footer-title">গুরুত্বপূর্ণ বিষয়</h4>
                    <ul class="ht-footer-links">
                        <li><a href="<?php echo esc_url(home_url('/category/national-university/')); ?>">জাতীয় বিশ্ববিদ্যালয়</a></li>
                        <li><a href="<?php echo esc_url(home_url('/category/education-guide/')); ?>">শিক্ষা ও রুটিন গাইড</a></li>
                        <li><a href="<?php echo esc_url(home_url('/category/ssc-dakhil/')); ?>">এসএসসি ও দাখিল সাজেশন</a></li>
                        <li><a href="<?php echo esc_url(home_url('/category/political-science/')); ?>">রাষ্ট্রবিজ্ঞান হ্যান্ডনোট</a></li>
                        <li><a href="<?php echo esc_url(home_url('/category/ict-technology/')); ?>">তথ্য ও যোগাযোগ প্রযুক্তি</a></li>
                        <li><a href="<?php echo esc_url(home_url('/category/job-preparation/')); ?>">চাকরি ও বিসিএস স্টাডি</a></li>
                    </ul>
                </div>

                <!-- Column 3: Exam Categories -->
                <div class="ht-footer-col">
                    <h4 class="ht-footer-title">রুটিন ও গাইডলাইন</h4>
                    <ul class="ht-footer-links">
                        <li><a href="<?php echo esc_url(home_url('/nu-honours-2nd-year-exam-routine-2026/')); ?>">অনার্স ২য় বর্ষ পরীক্ষার রুটিন</a></li>
                        <li><a href="<?php echo esc_url(home_url('/nu-honours-2nd-year-exam-guide-and/')); ?>">অনার্স ৩য় বর্ষ প্রমোশনের নিয়মাবলী</a></li>
                        <li><a href="<?php echo esc_url(home_url('/alim-exam-routine-2025/')); ?>">আলিম পরীক্ষার রুটিন ও গাইড</a></li>
                        <li><a href="<?php echo esc_url(home_url('/dhaka-board-certificate-name-age-correction-guide-2026/')); ?>">সার্টিফিকেট নাম ও বয়স সংশোধন</a></li>
                        <li><a href="<?php echo esc_url(home_url('/category/islamic-article/')); ?>">ইসলামিক প্রবন্ধ ও ক্বাসিদা</a></li>
                    </ul>
                </div>

                <!-- Column 4: Legal & Pages -->
                <div class="ht-footer-col">
                    <h4 class="ht-footer-title">আইনি ও সহায়তা</h4>
                    <ul class="ht-footer-links">
                        <li><a href="<?php echo esc_url(home_url('/about-us/')); ?>">আমাদের সম্পর্কে</a></li>
                        <li><a href="<?php echo esc_url(home_url('/contact-us/')); ?>">যোগাযোগ</a></li>
                        <li><a href="<?php echo esc_url(home_url('/privacy-policy/')); ?>">গোপনীয়তা নীতি (Privacy Policy)</a></li>
                        <li><a href="<?php echo esc_url(home_url('/terms-and-conditions/')); ?>">ব্যবহারের শর্তাবলী (Terms)</a></li>
                        <li><a href="<?php echo esc_url(home_url('/disclaimer/')); ?>">দাবিত্যাগ (Disclaimer)</a></li>
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
                        &copy; <?php echo esc_html(ht_bn_number(date('Y'))); ?> <a href="<?php echo esc_url(home_url('/')); ?>">HelpTrickBD.com</a> — সর্বস্বত্ব সংরক্ষিত।
                    <?php endif; ?>
                </div>
                <div class="ht-credit">
                    <?php echo esc_html(get_theme_mod('ht_footer_credit', 'নির্মিত হয়েছে শিক্ষা ও উন্মুক্ত জ্ঞানের প্রসারে')); ?>
                </div>
            </div>
        </div>

    </footer>

    <?php if (get_theme_mod('ht_mobile_dock_enable', true)) : ?>
        <!-- Mobile Bottom App Dock -->
        <nav class="ht-mobile-dock" aria-label="মোবাইল নেভিগেশন বার">
            <a href="<?php echo esc_url(home_url('/')); ?>" class="ht-dock-item <?php echo is_front_page() ? 'ht-active' : ''; ?>">
                <?php ht_m3_icon('home', 22); ?>
                <span>হোম</span>
            </a>
            <button class="ht-dock-item" id="ht-dock-menu-btn" aria-label="বিষয়শ্রেণী">
                <?php ht_m3_icon('category', 22); ?>
                <span>ক্যাটাগরি</span>
            </button>
            <button class="ht-dock-item" id="ht-dock-bookmark-btn" aria-label="পড়ার তালিকা">
                <?php ht_m3_icon('bookmark', 22); ?>
                <span class="ht-dock-badge" id="ht-dock-bm-count">০</span>
                <span>তালিকা</span>
            </button>
            <button class="ht-dock-item" id="ht-dock-search-btn" aria-label="সার্চ">
                <?php ht_m3_icon('search', 22); ?>
                <span>অনুসন্ধান</span>
            </button>
        </nav>
    <?php endif; ?>

    <?php if (get_theme_mod('ht_back_to_top_enable', true)) : ?>
        <!-- Circular Scroll-to-Top Progress Indicator -->
        <button class="ht-scroll-top" id="ht-scroll-top" aria-label="উপরে যান" title="উপরে যান">
            <svg class="ht-progress-ring" width="48" height="48" viewBox="0 0 48 48">
                <circle class="ht-progress-bg" cx="24" cy="24" r="20" fill="none" stroke-width="3"></circle>
                <circle class="ht-progress-bar" id="ht-progress-circle" cx="24" cy="24" r="20" fill="none" stroke-width="3" stroke-dasharray="125.66" stroke-dashoffset="125.66"></circle>
            </svg>
            <span class="ht-scroll-icon"><?php ht_m3_icon('keyboard_arrow_up', 22); ?></span>
        </button>
    <?php endif; ?>

    <!-- "Ctrl+K" Spotlight Instant Search Modal -->
    <div class="ht-modal ht-spotlight-modal" id="ht-spotlight-modal" aria-hidden="true" role="dialog" aria-label="তাৎক্ষণিক সার্চ">
        <div class="ht-spotlight-overlay" id="ht-spotlight-overlay"></div>
        <div class="ht-spotlight-dialog">
            <div class="ht-spotlight-header">
                <?php ht_m3_icon('search', 22, 'ht-spotlight-icon'); ?>
                <input type="search" id="ht-spotlight-input" class="ht-spotlight-input" placeholder="যেকোনো বিষয়, সাজেশন বা রুটিন খুঁজুন..." autocomplete="off" enterkeyhint="search">
                <button class="ht-spotlight-close" id="ht-spotlight-close" aria-label="বন্ধ করুন">
                    <kbd>ESC</kbd>
                </button>
            </div>
            <div class="ht-spotlight-body" id="ht-spotlight-results">
                <!-- Trending suggestions default state -->
                <div class="ht-spotlight-trending">
                    <span class="ht-spotlight-section-title">জনপ্রিয় অনুসন্ধান</span>
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
                <span class="ht-drawer-title">আপনার পড়ার তালিকা</span>
            </div>
            <button class="ht-drawer-close" id="ht-bm-close" aria-label="বন্ধ করুন">
                <?php ht_m3_icon('close', 20); ?>
            </button>
        </div>
        <div class="ht-drawer-body" id="ht-bookmarks-list">
            <!-- Dynamically populated from localStorage -->
            <div class="ht-empty-bookmarks">
                <?php ht_m3_icon('bookmark', 48, 'ht-empty-icon'); ?>
                <p>আপনার পড়ার তালিকায় এখনো কোনো হ্যান্ডনোট বা রুটিন যুক্ত করা হয়নি।</p>
                <span>যেকোনো পোস্টের বুকমার্ক আইকনে ক্লিক করে এখানে সেভ রাখতে পারবেন।</span>
            </div>
        </div>
        <div class="ht-drawer-footer">
            <button class="ht-btn ht-btn-sm ht-btn-outline" id="ht-clear-bookmarks">তালিকা খালি করুন</button>
        </div>
    </aside>
    <div class="ht-drawer-overlay" id="ht-bm-overlay"></div>

    <!-- Polite AdBlocker Notice Modal -->
    <?php if (get_theme_mod('ht_adblock_notice_enable', true)) : ?>
        <div class="ht-modal ht-adblock-modal" id="ht-adblock-modal" aria-hidden="true">
            <div class="ht-adblock-dialog">
                <?php ht_m3_icon('shield', 44, 'ht-adblock-icon'); ?>
                <h3 class="ht-adblock-title">একটি বিনীত অনুরোধ</h3>
                <p class="ht-adblock-desc">
                    HelpTrickBD একটি সম্পূর্ণ উন্মুক্ত ও বিনামূল্যে সেবা প্রদানকারী শিক্ষা পোর্টাল। আমাদের ওয়েবসাইটের কার্যক্রম পরিচালনা করার জন্য বিজ্ঞাপনের রাজস্ব অত্যন্ত প্রয়োজন। অনুগ্রহ করে আপনার এড-ব্লকারটি এই সাইটের জন্য বন্ধ (Whitelist) রাখুন।
                </p>
                <button class="ht-btn ht-btn-primary" id="ht-adblock-dismiss">বুঝেছি ও ধন্যবাদ</button>
            </div>
        </div>
    <?php endif; ?>

    <!-- Cookie Consent Banner -->
    <div class="ht-cookie-banner" id="ht-cookie-banner">
        <div class="ht-cookie-inner">
            <div class="ht-cookie-text">
                <?php ht_m3_icon('shield', 18, 'ht-cookie-icon'); ?>
                <span>আমরা আপনার অভিজ্ঞতা উন্নত করতে এবং মানসম্মত বিজ্ঞাপন প্রদর্শনের জন্য কুকি ব্যবহার করি। সাইটটি ব্যবহারের মাধ্যমে আপনি আমাদের নীতিতে সম্মতি জানাচ্ছেন।</span>
            </div>
            <div class="ht-cookie-actions">
                <a href="<?php echo esc_url(home_url('/privacy-policy/')); ?>" class="ht-cookie-link">বিস্তারিত</a>
                <button class="ht-btn ht-btn-sm ht-btn-primary" id="ht-cookie-accept">সম্মতি দিচ্ছি</button>
            </div>
        </div>
    </div>

</div><!-- #page -->

<?php wp_footer(); ?>
</body>
</html>
