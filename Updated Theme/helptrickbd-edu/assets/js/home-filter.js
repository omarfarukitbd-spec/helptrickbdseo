/**
 * HelpTrickBD EduPortal - Homepage Interactive Subject Filter Engine
 * Fast Client-Side Filtering with URL Hash Navigation & Accessible Empty State
 *
 * @package HelpTrickBD_EduPortal
 */

(function () {
  'use strict';

  var tabButtons = document.querySelectorAll('.n-thumb-tab-btn');
  var rows = document.querySelectorAll('.n-trow');
  var listContainer = document.querySelector('.n-thumb-list');

  if (!tabButtons.length || !rows.length) {
    return;
  }

  // --- ARIA Tablist Pattern Setup ---
  var tabsContainer = document.querySelector('.n-thumb-tabs');
  if (tabsContainer) {
    tabsContainer.setAttribute('role', 'tablist');
    tabsContainer.setAttribute('aria-label', '\u09ac\u09bf\u09b7\u09df \u0985\u09a8\u09c1\u09af\u09be\u09df\u09c0 \u09ab\u09bf\u09b2\u09cd\u099f\u09be\u09b0'); // বিষয় অনুযায়ী ফিল্টার
  }

  tabButtons.forEach(function (btn) {
    btn.setAttribute('role', 'tab');
    var isInitiallyActive = btn.classList.contains('active');
    btn.setAttribute('aria-selected', isInitiallyActive ? 'true' : 'false');
  });

  // --- Empty State Notice Helper ---
  var emptyNoticeId = 'ht-filter-empty-notice';

  function getOrCreateEmptyNotice() {
    var notice = document.getElementById(emptyNoticeId);
    if (!notice && listContainer) {
      notice = document.createElement('div');
      notice.id = emptyNoticeId;
      notice.className = 'n-filter-empty';
      notice.setAttribute('role', 'status');
      notice.style.cssText = 'grid-column: 1 / -1; width: 100%; text-align: center; padding: 36px 16px; color: var(--ht-text-muted); font-size: 0.95rem; border: 1px dashed var(--ht-border); border-radius: var(--ht-radius-sm); margin: 12px 0; background: var(--ht-surface);';
      notice.innerHTML = '<div style="font-size:1.5rem;margin-bottom:8px;" aria-hidden="true">\uD83D\uDCDD</div>\u098f\u0987 \u0995\u09cd\u09af\u09be\u099f\u09be\u0997\u09b0\u09bf\u09a4\u09c7 \u09ac\u09b0\u09cd\u09a4\u09ae\u09be\u09a8\u09c7 \u0995\u09cb\u09a8\u09cb \u09aa\u09cb\u09b8\u09cd\u099f \u09a8\u09c7\u0987\u0964'; // এই ক্যাটাগরিতে বর্তমানে কোনো পোস্ট নেই।
      listContainer.appendChild(notice);
    }
    return notice;
  }

  function filterCategory(targetCat, updateHash) {
    var selectedCat = targetCat || 'all';

    window.requestAnimationFrame(function () {
      // 1. Update button states
      tabButtons.forEach(function (btn) {
        var cat = btn.getAttribute('data-cat') || 'all';
        if (cat === selectedCat) {
          btn.classList.add('active');
          btn.setAttribute('aria-selected', 'true');
          btn.setAttribute('aria-pressed', 'true');
        } else {
          btn.classList.remove('active');
          btn.setAttribute('aria-selected', 'false');
          btn.setAttribute('aria-pressed', 'false');
        }
      });

      // 2. Filter matching rows
      var visibleCount = 0;
      rows.forEach(function (row) {
        var rowCats = (row.getAttribute('data-cats') || '').split(/\s+/);
        if (selectedCat === 'all' || rowCats.indexOf(selectedCat) !== -1) {
          row.style.display = 'grid';
          visibleCount++;
        } else {
          row.style.display = 'none';
        }
      });

      // 3. Handle Empty State
      var emptyNotice = getOrCreateEmptyNotice();
      if (emptyNotice) {
        emptyNotice.style.display = visibleCount === 0 ? 'block' : 'none';
      }

      // 4. Update URL Hash without unwanted scrolling
      if (updateHash && window.history && window.history.replaceState) {
        var newHash = selectedCat === 'all' ? '' : '#filter-' + encodeURIComponent(selectedCat);
        var currentUrl = window.location.pathname + window.location.search + newHash;
        window.history.replaceState(null, '', currentUrl);
      }
    });
  }

  function getCatFromHash() {
    var hash = window.location.hash.replace(/^#/, '');
    if (!hash) return null;
    if (hash.indexOf('filter-') === 0) {
      return decodeURIComponent(hash.substring(7));
    }
    if (hash.indexOf('cat-') === 0) {
      return decodeURIComponent(hash.substring(4));
    }
    return decodeURIComponent(hash);
  }

  // Bind click handlers to tab buttons
  tabButtons.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var cat = this.getAttribute('data-cat') || 'all';
      filterCategory(cat, true);
    });
  });

  // Listen to browser Back/Forward hash changes
  window.addEventListener('hashchange', function () {
    var cat = getCatFromHash();
    if (cat) {
      filterCategory(cat, false);
    } else {
      filterCategory('all', false);
    }
  });

  // Restore filter on initial load if hash is present
  var initialCat = getCatFromHash();
  if (initialCat) {
    var matchedBtn = Array.prototype.slice.call(tabButtons).some(function (b) {
      return b.getAttribute('data-cat') === initialCat;
    });
    if (matchedBtn) {
      filterCategory(initialCat, false);
    }
  }
})();
