/**
 * Offline Bookmarks Manager for HelpTrickBD EduPortal
 * Ultra-lightweight localStorage persistence with zero-latency drawer, focus trapping & full A11y
 *
 * @package HelpTrickBD_EduPortal
 */

(function () {
  'use strict';

  var STORAGE_KEY = 'htbd_edu_bookmarks_v1';
  var badgeEl = document.getElementById('ht-bookmark-badge');
  var drawerEl = document.getElementById('ht-bookmark-drawer');
  var itemsEl = document.getElementById('ht-bookmark-items');
  var emptyEl = document.getElementById('ht-bookmark-empty');
  var triggerBtn = document.getElementById('ht-bookmark-trigger');
  var clearBtn = document.getElementById('ht-clear-bookmarks');
  var lastBookmarkTrigger = null;

  // In-memory fallback if localStorage is blocked (Private/Incognito browsing)
  var memoryBookmarks = [];
  var isStorageAvailable = (function () {
    try {
      var testKey = '__ht_storage_test__';
      localStorage.setItem(testKey, testKey);
      localStorage.removeItem(testKey);
      return true;
    } catch (e) {
      return false;
    }
  })();

  function getBookmarks() {
    if (!isStorageAvailable) {
      return memoryBookmarks.slice();
    }
    try {
      var data = localStorage.getItem(STORAGE_KEY);
      return data ? JSON.parse(data) : [];
    } catch (e) {
      return [];
    }
  }

  function saveBookmarks(list) {
    if (!isStorageAvailable) {
      memoryBookmarks = list.slice();
    } else {
      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(list));
      } catch (e) {
        // Quota exceeded or storage restricted
        memoryBookmarks = list.slice();
      }
    }
    updateUI();
  }

  // --- ARIA Setup for Complementary Drawer Pattern ---
  if (drawerEl) {
    drawerEl.setAttribute('role', 'complementary');
    drawerEl.setAttribute('aria-modal', 'true');
    drawerEl.setAttribute('aria-label', '\u09ac\u09c1\u0995\u09ae\u09be\u09b0\u09cd\u0995 \u09a4\u09be\u09b2\u09bf\u0995\u09be'); // বুকমার্ক তালিকা
    drawerEl.setAttribute('aria-hidden', 'true');
  }

  // --- Focus Trap Helper for Bookmark Drawer ---
  var FOCUSABLE_SELECTORS = 'a[href], button:not([disabled]), input:not([disabled]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])';

  function getDrawerFocusables() {
    if (!drawerEl) return [];
    var elements = Array.prototype.slice.call(drawerEl.querySelectorAll(FOCUSABLE_SELECTORS));
    return elements.filter(function (el) {
      return el.offsetWidth > 0 || el.offsetHeight > 0 || el.getClientRects().length > 0;
    });
  }

  function trapDrawerFocus(e) {
    if (e.key !== 'Tab' || !drawerEl || !drawerEl.classList.contains('active')) return;

    var focusables = getDrawerFocusables();
    if (focusables.length === 0) {
      e.preventDefault();
      return;
    }

    var firstEl = focusables[0];
    var lastEl = focusables[focusables.length - 1];

    if (e.shiftKey) {
      if (document.activeElement === firstEl || !drawerEl.contains(document.activeElement)) {
        e.preventDefault();
        lastEl.focus();
      }
    } else {
      if (document.activeElement === lastEl || !drawerEl.contains(document.activeElement)) {
        e.preventDefault();
        firstEl.focus();
      }
    }
  }

  function openDrawer(e) {
    if (!drawerEl) return;
    lastBookmarkTrigger = (e && e.currentTarget) ? e.currentTarget : (triggerBtn || document.activeElement);

    drawerEl.classList.add('active');
    drawerEl.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    updateUI();

    window.requestAnimationFrame(function () {
      var focusables = getDrawerFocusables();
      if (focusables.length > 0) {
        focusables[0].focus();
      }
    });
  }

  function closeDrawer() {
    if (!drawerEl || !drawerEl.classList.contains('active')) return;

    drawerEl.classList.remove('active');
    drawerEl.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';

    if (lastBookmarkTrigger && typeof lastBookmarkTrigger.focus === 'function') {
      lastBookmarkTrigger.focus();
    }
    lastBookmarkTrigger = null;
  }

  function updateUI() {
    window.requestAnimationFrame(function () {
      var list = getBookmarks();

      // 1. Update topbar badge
      if (badgeEl) {
        if (list.length > 0) {
          badgeEl.textContent = list.length;
          badgeEl.style.display = 'block';
        } else {
          badgeEl.style.display = 'none';
        }
      }

      // 2. Update drawer list
      if (itemsEl && emptyEl) {
        if (list.length === 0) {
          itemsEl.innerHTML = '';
          emptyEl.style.display = 'block';
        } else {
          emptyEl.style.display = 'none';
          var html = '';
          list.forEach(function (item, index) {
            html += '<li class="ht-bookmark-drawer-item">';
            html += '<a href="' + item.url + '">' + item.title + '</a>';
            html += '<button type="button" class="ht-bookmark-remove" data-index="' + index + '" aria-label="\u09ae\u09c1\u099b\u09c7 \u09ab\u09c7\u09b2\u09c1\u09a8">&times;</button>'; // মুছে ফেলুন
            html += '</li>';
          });
          itemsEl.innerHTML = html;
        }
      }

      // 3. Update bookmark button states on the page
      var pageButtons = document.querySelectorAll('.ht-bookmark-btn');
      pageButtons.forEach(function (btn) {
        var id = btn.getAttribute('data-post-id');
        var isSaved = list.some(function (b) { return String(b.id) === String(id); });
        if (isSaved) {
          btn.classList.add('bookmarked');
          btn.setAttribute('aria-pressed', 'true');
          btn.setAttribute('title', '\u09b8\u0982\u09b0\u0995\u09cd\u09b7\u09a3 \u0995\u09b0\u09be \u09b9\u09df\u09c7\u099b\u09c7'); // সংরক্ষণ করা হয়েছে
        } else {
          btn.classList.remove('bookmarked');
          btn.setAttribute('aria-pressed', 'false');
          btn.setAttribute('title', '\u09b8\u0982\u09b0\u0995\u09cd\u09b7\u09a3 \u0995\u09b0\u09c1\u09a8'); // সংরক্ষণ করুন
        }
      });
    });
  }

  // Drawer Toggle Handlers
  if (triggerBtn && drawerEl) {
    triggerBtn.addEventListener('click', openDrawer);

    var closeTriggers = drawerEl.querySelectorAll('.ht-bookmark-close');
    closeTriggers.forEach(function (el) {
      el.addEventListener('click', closeDrawer);
    });
  }

  // Global ESC and Focus Trap for Bookmark Drawer
  document.addEventListener('keydown', function (e) {
    if (!drawerEl || !drawerEl.classList.contains('active')) return;

    if (e.key === 'Escape') {
      closeDrawer();
      return;
    }

    trapDrawerFocus(e);
  });

  // Clear all bookmarks
  if (clearBtn) {
    clearBtn.addEventListener('click', function () {
      if (confirm('\u0986\u09aa\u09a8\u09bf \u0995\u09bf \u09b8\u0995\u09b2 \u09b8\u0982\u09b0\u0995\u09cd\u09b7\u09a3\u09c7\u09b0 \u09b9\u09cd\u09af\u09be\u09a8\u09cd\u09a1\u09a8\u09cb\u099f \u09ae\u09c1\u099b\u09c7 \u09ab\u09c7\u09b2\u09a4\u09c7 \u099a\u09be\u09a8?')) {
        saveBookmarks([]);
      }
    });
  }

  // Delegated bookmark remove inside drawer
  if (itemsEl) {
    itemsEl.addEventListener('click', function (e) {
      var removeBtn = e.target.closest('.ht-bookmark-remove');
      if (removeBtn) {
        var index = parseInt(removeBtn.getAttribute('data-index'), 10);
        var list = getBookmarks();
        if (!isNaN(index) && index >= 0 && index < list.length) {
          list.splice(index, 1);
          saveBookmarks(list);
        }
      }
    });
  }

  // Delegated bookmark toggle on post buttons
  document.addEventListener('click', function (e) {
    var btn = e.target.closest('.ht-bookmark-btn');
    if (!btn) return;

    var id = btn.getAttribute('data-post-id');
    var title = btn.getAttribute('data-post-title') || document.title;
    var url = btn.getAttribute('data-post-url') || window.location.href;

    if (!id) return;

    var list = getBookmarks();
    var existingIndex = list.findIndex(function (b) { return String(b.id) === String(id); });

    if (existingIndex > -1) {
      list.splice(existingIndex, 1);
    } else {
      list.push({ id: id, title: title, url: url });
    }

    saveBookmarks(list);
  });

  // Initial render
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', updateUI);
  } else {
    updateUI();
  }
})();
