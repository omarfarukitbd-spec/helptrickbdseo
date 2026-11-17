<?php
/**
 * Single Post Component: Live Reading Progress Bar
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

if (!get_theme_mod('ht_reading_progress_enable', true)) {
    return;
}
?>
<!-- Live Reading Progress Bar -->
<div class="ht-reading-progress" id="ht-reading-progress" aria-hidden="true">
    <div class="ht-progress-fill" id="ht-progress-fill"></div>
</div>
