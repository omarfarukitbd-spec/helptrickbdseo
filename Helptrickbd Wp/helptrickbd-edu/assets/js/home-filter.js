/**
 * HelpTrickBD EduPortal - Homepage Interactive Subject Filter Engine
 * Fast Client-Side Filtering (Instant Display/Hide with Zero Latency)
 */

(function () {
  'use strict';

  const tabButtons = document.querySelectorAll('.n-thumb-tab-btn');
  const rows = document.querySelectorAll('.n-trow');

  if (!tabButtons.length || !rows.length) {
    return;
  }

  tabButtons.forEach(btn => {
    btn.addEventListener('click', function () {
      const selectedCat = this.getAttribute('data-cat') || 'all';

      // Update active button state
      tabButtons.forEach(b => {
        b.classList.remove('active');
        b.setAttribute('aria-pressed', 'false');
      });
      this.classList.add('active');
      this.setAttribute('aria-pressed', 'true');

      // Filter rows
      rows.forEach(row => {
        const rowCats = (row.getAttribute('data-cats') || '').split(' ');
        if (selectedCat === 'all' || rowCats.includes(selectedCat)) {
          row.style.display = 'grid';
        } else {
          row.style.display = 'none';
        }
      });
    });
  });
})();
