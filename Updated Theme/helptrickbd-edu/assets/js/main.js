/**
 * HelpTrickBD EduPortal - Main Global JavaScript Engine
 * Fast Vanilla ES6 Engine (Zero jQuery, 100/100 Core Web Vitals, Full A11y)
 *
 * @package HelpTrickBD_EduPortal
 */

(function () {
  'use strict';

  // --- Safe LocalStorage Helpers (Private Browsing Resilient) ---
  function safeGetItem(key, fallback) {
    try {
      var val = localStorage.getItem(key);
      return val !== null ? val : fallback;
    } catch (e) {
      return fallback;
    }
  }

  function safeSetItem(key, val) {
    try {
      localStorage.setItem(key, val);
    } catch (e) {
      // Storage unavailable or quota exceeded
    }
  }

  // --- Reusable Focus Trap Controller ---
  var FOCUSABLE_SELECTORS = 'a[href], button:not([disabled]), input:not([disabled]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])';

  function getFocusableElements(container) {
    if (!container) return [];
    var elements = Array.prototype.slice.call(container.querySelectorAll(FOCUSABLE_SELECTORS));
    return elements.filter(function (el) {
      return el.offsetWidth > 0 || el.offsetHeight > 0 || el.getClientRects().length > 0;
    });
  }

  function handleFocusTrap(container, e) {
    if (e.key !== 'Tab') return;

    var focusables = getFocusableElements(container);
    if (focusables.length === 0) {
      e.preventDefault();
      return;
    }

    var firstEl = focusables[0];
    var lastEl = focusables[focusables.length - 1];

    if (e.shiftKey) {
      if (document.activeElement === firstEl || !container.contains(document.activeElement)) {
        e.preventDefault();
        lastEl.focus();
      }
    } else {
      if (document.activeElement === lastEl || !container.contains(document.activeElement)) {
        e.preventDefault();
        firstEl.focus();
      }
    }
  }

  // 1. Dark / Light Mode Switcher (Default: Light Mode)
  var themeToggle = document.getElementById('ht-theme-toggle');
  var savedTheme = safeGetItem('ht_theme', 'light');

  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    safeSetItem('ht_theme', theme);
    var metaScheme = document.querySelector('meta[name="color-scheme"]');
    if (metaScheme) {
      metaScheme.setAttribute('content', theme);
    }
    if (themeToggle) {
      themeToggle.setAttribute('aria-pressed', theme === 'dark' ? 'true' : 'false');
    }
  }

  applyTheme(savedTheme);

  if (themeToggle) {
    themeToggle.addEventListener('click', function () {
      var current = document.documentElement.getAttribute('data-theme') || 'light';
      var target = current === 'dark' ? 'light' : 'dark';
      applyTheme(target);
    });
  }

  // --- Accessibility Background Inactivation Helpers ---
  var pageContainer = document.getElementById('page');
  var mainContainer = document.getElementById('primary') || document.querySelector('main');

  function setBackgroundInert(inert) {
    if (inert) {
      if (pageContainer) pageContainer.setAttribute('aria-hidden', 'true');
      if (mainContainer) mainContainer.setAttribute('aria-hidden', 'true');
    } else {
      if (pageContainer) pageContainer.removeAttribute('aria-hidden');
      if (mainContainer) mainContainer.removeAttribute('aria-hidden');
    }
  }

  // 2. Search Modal Engine (Button + Ctrl+K Shortcut + Focus Trap)
  var searchModal = document.getElementById('ht-search-modal');
  var searchTriggers = document.querySelectorAll('.ht-search-trigger');
  var searchClose = document.getElementById('ht-search-close');
  var searchInput = document.getElementById('ht-search-input');
  var lastActiveSearchTrigger = null;

  if (searchModal) {
    searchModal.setAttribute('role', 'dialog');
    searchModal.setAttribute('aria-modal', 'true');
    searchModal.setAttribute('aria-label', '\u0985\u09a8\u09c1\u09b8\u09a8\u09cd\u09a7\u09be\u09a8'); // অনুসন্ধান
    searchModal.setAttribute('aria-hidden', 'true');
  }

  function openSearch(e) {
    if (!searchModal) return;
    lastActiveSearchTrigger = (e && e.currentTarget) ? e.currentTarget : document.activeElement;

    searchModal.classList.add('active');
    searchModal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    setBackgroundInert(true);

    window.requestAnimationFrame(function () {
      if (searchInput) {
        searchInput.focus();
        if (searchInput.select) searchInput.select();
      }
    });
  }

  function closeSearch() {
    if (!searchModal || !searchModal.classList.contains('active')) return;

    searchModal.classList.remove('active');
    searchModal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
    setBackgroundInert(false);

    if (lastActiveSearchTrigger && typeof lastActiveSearchTrigger.focus === 'function') {
      lastActiveSearchTrigger.focus();
    }
    lastActiveSearchTrigger = null;
  }

  searchTriggers.forEach(function (btn) {
    btn.addEventListener('click', openSearch);
  });

  if (searchClose) {
    searchClose.addEventListener('click', closeSearch);
  }

  // 3. Mobile Off-Canvas Drawer Engine + Focus Trap
  var drawer = document.getElementById('ht-mobile-drawer');
  var drawerToggle = document.getElementById('ht-drawer-toggle');
  var drawerClose = document.getElementById('ht-drawer-close');
  var drawerBackdrop = document.getElementById('ht-drawer-backdrop');
  var lastActiveDrawerToggle = null;

  if (drawer) {
    drawer.setAttribute('role', 'dialog');
    drawer.setAttribute('aria-modal', 'true');
    drawer.setAttribute('aria-label', '\u09ae\u09cb\u09ac\u09be\u0987\u09b2 \u09ae\u09c7\u09a8\u09c1'); // মোবাইল মেনু
    drawer.setAttribute('aria-hidden', 'true');
  }

  function openDrawer(e) {
    if (!drawer) return;
    lastActiveDrawerToggle = (e && e.currentTarget) ? e.currentTarget : document.activeElement;

    drawer.classList.add('active');
    drawer.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    if (drawerToggle) drawerToggle.setAttribute('aria-expanded', 'true');

    window.requestAnimationFrame(function () {
      var focusables = getFocusableElements(drawer);
      if (focusables.length > 0) {
        focusables[0].focus();
      }
    });
  }

  function closeDrawer() {
    if (!drawer || !drawer.classList.contains('active')) return;

    drawer.classList.remove('active');
    drawer.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
    if (drawerToggle) drawerToggle.setAttribute('aria-expanded', 'false');

    if (lastActiveDrawerToggle && typeof lastActiveDrawerToggle.focus === 'function') {
      lastActiveDrawerToggle.focus();
    }
    lastActiveDrawerToggle = null;
  }

  if (drawerToggle) {
    drawerToggle.setAttribute('aria-expanded', 'false');
    drawerToggle.addEventListener('click', openDrawer);
  }

  if (drawerClose) {
    drawerClose.addEventListener('click', closeDrawer);
  }

  if (drawerBackdrop) {
    drawerBackdrop.addEventListener('click', closeDrawer);
  }

  // Global Keyboard Shortcuts (Ctrl+K, Escape, and Focus Traps)
  document.addEventListener('keydown', function (e) {
    var isSearchOpen = searchModal && searchModal.classList.contains('active');
    var isDrawerOpen = drawer && drawer.classList.contains('active');

    // Ctrl+K / Cmd+K search shortcut
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      if (isSearchOpen) {
        closeSearch();
      } else {
        openSearch(e);
      }
      return;
    }

    // Escape Key Handling
    if (e.key === 'Escape') {
      if (isSearchOpen) {
        closeSearch();
      }
      if (isDrawerOpen) {
        closeDrawer();
      }
      return;
    }

    // Modal Focus Trap
    if (isSearchOpen) {
      handleFocusTrap(searchModal, e);
    } else if (isDrawerOpen) {
      handleFocusTrap(drawer, e);
    }
  });

  // 4. Back To Top Smooth Scroll with Passive Listener
  var backToTop = document.getElementById('ht-back-to-top');
  if (backToTop) {
    backToTop.addEventListener('click', function (e) {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    var bttVisible = false;
    window.addEventListener('scroll', function () {
      var shouldShow = window.pageYOffset > 400;
      if (shouldShow !== bttVisible) {
        bttVisible = shouldShow;
        window.requestAnimationFrame(function () {
          if (bttVisible) {
            backToTop.classList.add('visible');
          } else {
            backToTop.classList.remove('visible');
          }
        });
      }
    }, { passive: true });
  }
})();
