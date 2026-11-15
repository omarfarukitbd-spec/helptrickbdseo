/**
 * Offline Bookmarks Manager for HelpTrickBD EduPortal
 * Ultra-lightweight localStorage persistence with zero-latency drawer
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

  function getBookmarks() {
    try {
      var data = localStorage.getItem(STORAGE_KEY);
      return data ? JSON.parse(data) : [];
    } catch (e) {
      return [];
    }
  }

  function saveBookmarks(list) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(list));
    } catch (e) {
      console.warn('LocalStorage unavailable');
    }
    updateUI();
  }

  function updateUI() {
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
          html += '<button type="button" class="ht-bookmark-remove" data-index="' + index + '" aria-label="মুছে ফেলুন">&times;</button>';
          html += '</li>';
        });
        itemsEl.innerHTML = html;
      }
    }

    // 3. Update bookmark button states on the page
    var pageButtons = document.querySelectorAll('.ht-bookmark-btn');
    pageButtons.forEach(function (btn) {
      var id = btn.getAttribute('data-post-id');
      var isSaved = list.some(function (b) { return b.id == id; });
      if (isSaved) {
        btn.classList.add('bookmarked');
        btn.setAttribute('aria-pressed', 'true');
        btn.setAttribute('title', 'সংরক্ষণ করা হয়েছে');
      } else {
        btn.classList.remove('bookmarked');
        btn.setAttribute('aria-pressed', 'false');
        btn.setAttribute('title', 'সংরক্ষণ করুন');
      }
    });
  }

  // Drawer Toggle
  if (triggerBtn && drawerEl) {
    triggerBtn.addEventListener('click', function () {
      drawerEl.classList.add('active');
      drawerEl.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
      updateUI();
    });

    var closeTriggers = drawerEl.querySelectorAll('.ht-bookmark-close');
    closeTriggers.forEach(function (el) {
      el.addEventListener('click', function () {
        drawerEl.classList.remove('active');
        drawerEl.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
      });
    });
  }

  // Clear all bookmarks
  if (clearBtn) {
    clearBtn.addEventListener('click', function () {
      if (confirm('আপনি কি সকল সংরক্ষিত হ্যান্ডনোট মুছে ফেলতে চান?')) {
        saveBookmarks([]);
      }
    });
  }

  // Delegated bookmark remove inside drawer
  if (itemsEl) {
    itemsEl.addEventListener('click', function (e) {
      if (e.target && e.target.classList.contains('ht-bookmark-remove')) {
        var index = parseInt(e.target.getAttribute('data-index'), 10);
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
    var existingIndex = list.findIndex(function (b) { return b.id == id; });

    if (existingIndex > -1) {
      list.splice(existingIndex, 1);
    } else {
      list.push({ id: id, title: title, url: url });
    }

    saveBookmarks(list);
  });

  // Initial render
  document.addEventListener('DOMContentLoaded', updateUI);
})();
