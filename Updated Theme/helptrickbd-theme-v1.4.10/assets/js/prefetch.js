/**
 * HelpTrickBD Pro - Instant Hover Preloader
 * Dynamically pre-fetches internal links on 65ms hover for < 100ms perceived page loads.
 */

(function () {
    'use strict';

    const prefetchedUrls = new Set();
    const siteOrigin = window.location.origin;

    function prefetchUrl(url) {
        if (prefetchedUrls.has(url)) return;
        prefetchedUrls.add(url);

        const link = document.createElement('link');
        link.rel = 'prefetch';
        link.href = url;
        document.head.appendChild(link);
    }

    let hoverTimer = null;

    document.addEventListener('mouseover', function (e) {
        const anchor = e.target.closest('a');
        if (!anchor || !anchor.href) return;

        const href = anchor.href;
        if (!href.startsWith(siteOrigin) || href.includes('#') || href.includes('wp-admin') || href.includes('wp-login')) {
            return;
        }

        hoverTimer = setTimeout(() => {
            prefetchUrl(href);
        }, 65);
    }, { passive: true });

    document.addEventListener('mouseout', function () {
        clearTimeout(hoverTimer);
    }, { passive: true });

})();
