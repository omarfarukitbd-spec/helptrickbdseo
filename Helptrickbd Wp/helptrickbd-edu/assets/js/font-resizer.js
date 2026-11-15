/**
 * HelpTrickBD EduPortal - Newspaper Font Resizer Engine
 * Scales Typography Fluidly (ছোট = 0.9, মাঝারি = 1.0, বড় = 1.15)
 */

(function () {
  'use strict';

  const SCALE_MAP = {
    'sm': '0.9',
    'md': '1.0',
    'lg': '1.15'
  };

  const buttons = document.querySelectorAll('.n-fsbtn');
  const savedScale = localStorage.getItem('ht_font_scale') || 'md';

  function applyFontScale(scaleKey) {
    const scaleVal = SCALE_MAP[scaleKey] || '1.0';
    document.documentElement.style.setProperty('--ht-font-scale', scaleVal);
    localStorage.setItem('ht_font_scale', scaleKey);

    buttons.forEach(btn => {
      if (btn.getAttribute('data-scale') === scaleKey) {
        btn.classList.add('active');
        btn.setAttribute('aria-pressed', 'true');
      } else {
        btn.classList.remove('active');
        btn.setAttribute('aria-pressed', 'false');
      }
    });
  }

  // Apply on initial load
  applyFontScale(savedScale);

  // Bind click handlers
  buttons.forEach(btn => {
    btn.addEventListener('click', function () {
      const scaleKey = this.getAttribute('data-scale');
      if (scaleKey && SCALE_MAP[scaleKey]) {
        applyFontScale(scaleKey);
      }
    });
  });
})();
