/**
 * HelpTrickBD EduPortal - Main Global JavaScript
 * Fast Vanilla ES6 Engine (Zero jQuery, Zero Bloat)
 */

(function () {
  'use strict';

  // 1. Dark / Light Mode Switcher (Default: Light Mode)
  const themeToggle = document.getElementById('ht-theme-toggle');
  const savedTheme = localStorage.getItem('ht_theme') || 'light';

  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('ht_theme', theme);
  }

  // Apply default light mode or saved choice
  applyTheme(savedTheme);

  if (themeToggle) {
    themeToggle.addEventListener('click', function () {
      const current = document.documentElement.getAttribute('data-theme') || 'light';
      const target = current === 'dark' ? 'light' : 'dark';
      applyTheme(target);
    });
  }

  // 2. Search Modal Engine (Button + Ctrl+K Shortcut)
  const searchModal = document.getElementById('ht-search-modal');
  const searchTriggers = document.querySelectorAll('.ht-search-trigger');
  const searchClose = document.getElementById('ht-search-close');
  const searchInput = document.getElementById('ht-search-input');

  function openSearch() {
    if (!searchModal) return;
    searchModal.classList.add('active');
    document.body.style.overflow = 'hidden';
    setTimeout(() => {
      if (searchInput) searchInput.focus();
    }, 100);
  }

  function closeSearch() {
    if (!searchModal) return;
    searchModal.classList.remove('active');
    document.body.style.overflow = '';
  }

  searchTriggers.forEach(btn => btn.addEventListener('click', openSearch));
  if (searchClose) searchClose.addEventListener('click', closeSearch);

  // Keyboard shortcut Ctrl+K / Cmd+K and Esc
  document.addEventListener('keydown', function (e) {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      if (searchModal && searchModal.classList.contains('active')) {
        closeSearch();
      } else {
        openSearch();
      }
    } else if (e.key === 'Escape') {
      closeSearch();
      closeDrawer();
    }
  });

  // 3. Mobile Off-Canvas Drawer Engine
  const drawer = document.getElementById('ht-mobile-drawer');
  const drawerToggle = document.getElementById('ht-drawer-toggle');
  const drawerClose = document.getElementById('ht-drawer-close');

  function openDrawer() {
    if (!drawer) return;
    drawer.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeDrawer() {
    if (!drawer) return;
    drawer.classList.remove('active');
    document.body.style.overflow = '';
  }

  if (drawerToggle) drawerToggle.addEventListener('click', openDrawer);
  if (drawerClose) drawerClose.addEventListener('click', closeDrawer);

  // 4. Back To Top Smooth Scroll
  const backToTop = document.getElementById('ht-back-to-top');
  if (backToTop) {
    backToTop.addEventListener('click', function (e) {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }
})();
