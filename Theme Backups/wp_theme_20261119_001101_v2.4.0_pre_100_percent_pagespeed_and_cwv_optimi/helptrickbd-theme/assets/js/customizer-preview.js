/**
 * HelpTrickBD Pro - Customizer Live Preview JavaScript
 * Instantaneous real-time postMessage preview without page reloads.
 *
 * @package HelpTrickBD_Pro
 */

(function ($) {
    'use strict';

    // Site Title
    wp.customize('blogname', function (value) {
        value.bind(function (to) {
            $('.ht-logo-text').text(to);
        });
    });

    // Site Tagline
    wp.customize('blogdescription', function (value) {
        value.bind(function (to) {
            $('.ht-logo-tagline').text(to);
        });
    });

    // Breaking Notice Ticker Text
    wp.customize('ht_ticker_text', function (value) {
        value.bind(function (to) {
            $('.ht-ticker-text, .ht-ticker-link').text(to);
        });
    });

    // Exam Countdown Title
    wp.customize('ht_countdown_title', function (value) {
        value.bind(function (to) {
            $('.ht-countdown-title').text(to + ':');
        });
    });

    // Footer Copyright Text
    wp.customize('ht_footer_copyright', function (value) {
        value.bind(function (to) {
            $('.ht-copyright').text(to);
        });
    });

    // Footer Credit Text
    wp.customize('ht_footer_credit', function (value) {
        value.bind(function (to) {
            $('.ht-credit').text(to);
        });
    });

})(jQuery);
