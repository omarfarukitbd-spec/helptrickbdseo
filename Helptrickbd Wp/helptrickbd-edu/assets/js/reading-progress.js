/**
 * Smooth Reading Progress Indicator for HelpTrickBD EduPortal
 * Passive scroll & resize listeners with RAF throttling for 100/100 Core Web Vitals & full ARIA
 *
 * @package HelpTrickBD_EduPortal
 */

(function () {
  'use strict';

  var bar = document.getElementById('ht-reading-progress');
  var content = document.querySelector('.ht-entry-content');

  if (!bar || !content) {
    return;
  }

  // --- ARIA Progressbar Setup ---
  bar.setAttribute('role', 'progressbar');
  bar.setAttribute('aria-valuemin', '0');
  bar.setAttribute('aria-valuemax', '100');
  bar.setAttribute('aria-valuenow', '0');
  bar.setAttribute('aria-label', '\u09aa\u09dc\u09be\u09b0 \u0985\u0997\u09cd\u09b0\u0997\u09a4\u09bf'); // পড়ার অগ্রগতি (U+09DC precomposed ড়)

  var ticking = false;

  function updateProgress() {
    var rect = content.getBoundingClientRect();
    var windowHeight = window.innerHeight;
    var totalHeight = content.offsetHeight;
    var currentTop = -rect.top;

    var progress = 0;
    if (totalHeight > 0) {
      progress = (currentTop / (totalHeight - windowHeight + 100)) * 100;
    }

    if (progress < 0) progress = 0;
    if (progress > 100) progress = 100;

    var roundedProgress = Math.round(progress);
    bar.style.width = progress + '%';
    bar.setAttribute('aria-valuenow', String(roundedProgress));

    ticking = false;
  }

  function requestTick() {
    if (!ticking) {
      window.requestAnimationFrame(updateProgress);
      ticking = true;
    }
  }

  window.addEventListener('scroll', requestTick, { passive: true });
  window.addEventListener('resize', requestTick, { passive: true });

  // Initial calculation
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', updateProgress);
  } else {
    updateProgress();
  }
})();
