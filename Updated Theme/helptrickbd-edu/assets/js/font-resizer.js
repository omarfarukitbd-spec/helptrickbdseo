/**
 * HelpTrickBD EduPortal - Newspaper Font Resizer Engine
 * Fluid Typography Scaling with LocalStorage Persistence & Full A11y (sm=0.9, md=1.0, lg=1.15)
 *
 * @package HelpTrickBD_EduPortal
 */

(function () {
  'use strict';

  var STORAGE_KEY = 'ht_font_scale';

  var SCALE_MAP = {
    'sm': '0.9',
    'md': '1.0',
    'lg': '1.15'
  };

  function getSavedScale() {
    try {
      var val = localStorage.getItem(STORAGE_KEY);
      return val && SCALE_MAP[val] ? val : 'md';
    } catch (e) {
      return 'md';
    }
  }

  function setSavedScale(scaleKey) {
    try {
      localStorage.setItem(STORAGE_KEY, scaleKey);
    } catch (e) {
      // Storage unavailable or disabled
    }
  }

  function applyFontScale(scaleKey) {
    var scaleVal = SCALE_MAP[scaleKey] || '1.0';
    document.documentElement.style.setProperty('--ht-font-scale', scaleVal);
    setSavedScale(scaleKey);

    window.requestAnimationFrame(function () {
      var buttons = document.querySelectorAll('.n-fsbtn');
      buttons.forEach(function (btn) {
        var btnScale = btn.getAttribute('data-scale');
        if (btnScale === scaleKey) {
          btn.classList.add('active');
          btn.setAttribute('aria-pressed', 'true');
        } else {
          btn.classList.remove('active');
          btn.setAttribute('aria-pressed', 'false');
        }
      });
    });
  }

  function initFontResizer() {
    var buttons = document.querySelectorAll('.n-fsbtn');
    var currentScale = getSavedScale();

    // Restore preference
    applyFontScale(currentScale);

    buttons.forEach(function (btn) {
      // Avoid duplicate bindings
      if (btn.hasAttribute('data-fs-bound')) return;
      btn.setAttribute('data-fs-bound', 'true');

      btn.addEventListener('click', function () {
        var scaleKey = this.getAttribute('data-scale');
        if (scaleKey && SCALE_MAP[scaleKey]) {
          applyFontScale(scaleKey);
        }
      });
    });
  }

  // Restore immediately to minimize layout shifts
  applyFontScale(getSavedScale());

  // Bind handlers on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initFontResizer);
  } else {
    initFontResizer();
  }
})();
