<?php
/**
 * Master WordPress Customizer Loader for HelpTrickBD Pro
 * Micro-Modular Architecture (Enterprise Grade)
 * Loads each customizer section from inc/customizer/ directory.
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

$customizer_dir = get_template_directory() . '/inc/customizer/';

// 1. Base Panel & Sanitizers
require_once $customizer_dir . 'customizer-base.php';

// 2. Typography Suite (Heading & Body Fonts)
require_once $customizer_dir . 'section-typography.php';

// 3. Header & Navigation Controls
require_once $customizer_dir . 'section-header.php';

// 4. Homepage Sections & Educational Hubs
require_once $customizer_dir . 'section-homepage.php';

// 5. Sidebar Modules
require_once $customizer_dir . 'section-sidebar.php';

// 6. Social & Community Links
require_once $customizer_dir . 'section-community.php';

// 7. Footer & Copyright
require_once $customizer_dir . 'section-footer.php';

// 8. Single Post & Study Tools
require_once $customizer_dir . 'section-single.php';

// 9. Google AdSense & Monetization
require_once $customizer_dir . 'section-ads.php';

// 10. Dynamic CSS Generation (Single Source of Truth)
require_once $customizer_dir . 'dynamic-css.php';
