/**
 * Smooth Reading Progress Indicator for HelpTrickBD EduPortal
 * Passive scroll listener with RAF throttling for 100/100 Core Web Vitals
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

    bar.style.width = progress + '%';
    ticking = false;
  }

  window.addEventListener('scroll', function () {
    if (!ticking) {
      window.requestAnimationFrame(updateProgress);
      ticking = true;
    }
  }, { passive: true });

  updateProgress();
})();
