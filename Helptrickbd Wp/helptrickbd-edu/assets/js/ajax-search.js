/**
 * Live AJAX Instant Search for HelpTrickBD EduPortal
 * Debounced REST API query with zero-CLS suggestions dropdown, full ARIA & keyboard navigation
 *
 * @package HelpTrickBD_EduPortal
 */

(function () {
  'use strict';

  var searchInput = document.getElementById('ht-search-input');
  var resultsBox = document.getElementById('ht-live-search-results');

  if (!searchInput || !resultsBox) {
    return;
  }

  // --- ARIA Setup for Combobox & Listbox Pattern ---
  searchInput.setAttribute('role', 'combobox');
  searchInput.setAttribute('aria-autocomplete', 'list');
  searchInput.setAttribute('aria-expanded', 'false');
  searchInput.setAttribute('aria-controls', 'ht-live-search-results');

  resultsBox.setAttribute('role', 'listbox');
  resultsBox.setAttribute('aria-label', '\u0985\u09a8\u09c1\u09b8\u09a8\u09cd\u09a7\u09be\u09a8\u09c7\u09b0 \u09ab\u09b2\u09be\u09ab\u09b2'); // অনুসন্ধানের ফলাফল

  var debounceTimer = null;
  var currentQuery = '';
  var selectedIndex = -1;
  var currentAbortController = null;

  var restUrl = (window.htbdEduSettings && window.htbdEduSettings.restUrl)
    ? window.htbdEduSettings.restUrl
    : '/wp-json/wp/v2/';

  function decodeHtml(html) {
    var txt = document.createElement('textarea');
    txt.innerHTML = html;
    return txt.value;
  }

  function clearResults() {
    resultsBox.innerHTML = '';
    resultsBox.style.display = 'none';
    selectedIndex = -1;
    searchInput.setAttribute('aria-expanded', 'false');
    searchInput.removeAttribute('aria-activedescendant');
  }

  function updateActiveOption(newIndex) {
    var items = resultsBox.querySelectorAll('.ht-live-search-item');
    if (!items.length) {
      selectedIndex = -1;
      searchInput.removeAttribute('aria-activedescendant');
      return;
    }

    if (newIndex < 0) {
      newIndex = items.length - 1;
    } else if (newIndex >= items.length) {
      newIndex = 0;
    }

    selectedIndex = newIndex;

    items.forEach(function (item, idx) {
      if (idx === selectedIndex) {
        item.classList.add('active');
        item.setAttribute('aria-selected', 'true');
        searchInput.setAttribute('aria-activedescendant', item.id);
        if (typeof item.scrollIntoView === 'function') {
          item.scrollIntoView({ block: 'nearest' });
        }
      } else {
        item.classList.remove('active');
        item.setAttribute('aria-selected', 'false');
      }
    });
  }

  function renderResults(posts) {
    window.requestAnimationFrame(function () {
      if (!posts || posts.length === 0) {
        resultsBox.innerHTML = '<div style="padding:14px;text-align:center;color:var(--ht-text-muted);font-size:0.875rem;" role="status">\u0995\u09cb\u09a8\u09cb \u09ab\u09b2\u09be\u09ab\u09b2 \u09aa\u09be\u0993\u09df\u09be \u09af\u09be\u09df\u09a8\u09bf\u0964 \u09b8\u09ae\u09cd\u09aa\u09c2\u09b0\u09cd\u09a3 \u0985\u09a8\u09c1\u09b8\u09a8\u09cd\u09a7\u09be\u09a8\u09c7\u09b0 \u099c\u09a8\u09cd\u09af \u098f\u09a8\u09cd\u099f\u09be\u09b0 \u099a\u09be\u09aa\u09c1\u09a8\u0964</div>';
        resultsBox.style.display = 'block';
        searchInput.setAttribute('aria-expanded', 'true');
        selectedIndex = -1;
        return;
      }

      var html = '';
      posts.forEach(function (post, index) {
        var title = decodeHtml(post.title.rendered);
        var link = post.link;
        var thumb = '';
        var itemId = 'ht-search-item-' + index;

        if (post._embedded && post._embedded['wp:featuredmedia'] && post._embedded['wp:featuredmedia'][0]) {
          var media = post._embedded['wp:featuredmedia'][0];
          thumb = media.source_url || (media.media_details && media.media_details.sizes && media.media_details.sizes.thumbnail && media.media_details.sizes.thumbnail.source_url);
        }

        html += '<a href="' + link + '" class="ht-live-search-item" id="' + itemId + '" role="option" aria-selected="false" tabindex="-1">';
        if (thumb) {
          html += '<img src="' + thumb + '" alt="" class="ht-live-search-thumb" loading="lazy" width="48" height="48">';
        }
        html += '<div style="flex:1;overflow:hidden;">';
        html += '<div class="ht-live-search-title">' + title + '</div>';
        html += '<div class="ht-live-search-meta">\u098f\u0995\u09be\u09a1\u09c7\u09ae\u09bf\u0995 \u09b9\u09cd\u09af\u09be\u09a8\u09cd\u09a1\u09a8\u09cb\u099f</div>'; // একাডেমিক হ্যান্ডনোট
        html += '</div>';
        html += '</a>';
      });

      resultsBox.innerHTML = html;
      resultsBox.style.display = 'flex';
      searchInput.setAttribute('aria-expanded', 'true');
      selectedIndex = -1;

      // Enable mouse hover interaction with keyboard sync
      var renderedItems = resultsBox.querySelectorAll('.ht-live-search-item');
      renderedItems.forEach(function (item, idx) {
        item.addEventListener('mouseenter', function () {
          updateActiveOption(idx);
        });
      });
    });
  }

  function renderError(message) {
    window.requestAnimationFrame(function () {
      resultsBox.innerHTML = '<div style="padding:12px;text-align:center;color:var(--ht-text-muted);font-size:0.85rem;" role="alert">' + message + '</div>';
      resultsBox.style.display = 'block';
      searchInput.setAttribute('aria-expanded', 'true');
      selectedIndex = -1;
    });
  }

  // Input listener with 250ms Debounce & AbortController
  searchInput.addEventListener('input', function (e) {
    var q = e.target.value.trim();

    if (debounceTimer) {
      clearTimeout(debounceTimer);
    }

    if (q.length < 2) {
      clearResults();
      currentQuery = '';
      if (currentAbortController) {
        currentAbortController.abort();
      }
      return;
    }

    currentQuery = q;

    debounceTimer = setTimeout(function () {
      if (typeof navigator !== 'undefined' && !navigator.onLine) {
        renderError('\u0987\u09a8\u09cd\u099f\u09be\u09b0\u09a8\u09c7\u099f \u09b8\u0982\u09af\u09cb\u0997 \u09a8\u09c7\u0987\u0964 \u0985\u09ab\u09b2\u09be\u0987\u09a8\u09c7 \u09b8\u09be\u09b0\u09cd\u099a \u0995\u09b0\u09be \u09b8\u09ae\u09cd\u09ad\u09ac \u09a8\u09df\u0964'); // ইন্টারনেট সংযোগ নেই
        return;
      }

      if (currentAbortController) {
        currentAbortController.abort();
      }

      if (typeof AbortController !== 'undefined') {
        currentAbortController = new AbortController();
      }

      var fetchUrl = restUrl + 'posts?search=' + encodeURIComponent(q) + '&_embed=1&per_page=5';
      var fetchOptions = currentAbortController ? { signal: currentAbortController.signal } : {};

      fetch(fetchUrl, fetchOptions)
        .then(function (res) {
          if (!res.ok) {
            throw new Error('HTTP ' + res.status);
          }
          return res.json();
        })
        .then(function (data) {
          if (searchInput.value.trim() === currentQuery) {
            renderResults(data);
          }
        })
        .catch(function (err) {
          if (err.name === 'AbortError') return;
          renderError('\u09b8\u09be\u09b0\u09cd\u099a\u09c7 \u09b8\u09ae\u09b8\u09cd\u09af\u09be \u09b9\u09df\u09c7\u099b\u09c7\u0964 \u09b8\u09ae\u09cd\u09aa\u09c2\u09b0\u09cd\u09a3 \u09aa\u09c7\u099c\u09c7 \u0996\u09c1\u0981\u099c\u09a4\u09c7 \u098f\u09a8\u09cd\u099f\u09be\u09b0 \u099a\u09be\u09aa\u09c1\u09a8\u0964'); // সার্চে সমস্যা হয়েছে
        });
    }, 250);
  });

  // Keyboard Navigation: Arrow Up/Down, Enter, and Escape
  searchInput.addEventListener('keydown', function (e) {
    var isResultsOpen = resultsBox.style.display !== 'none' && resultsBox.querySelectorAll('.ht-live-search-item').length > 0;

    if (e.key === 'ArrowDown') {
      if (isResultsOpen) {
        e.preventDefault();
        updateActiveOption(selectedIndex + 1);
      }
    } else if (e.key === 'ArrowUp') {
      if (isResultsOpen) {
        e.preventDefault();
        updateActiveOption(selectedIndex - 1);
      }
    } else if (e.key === 'Enter') {
      if (isResultsOpen && selectedIndex >= 0) {
        var items = resultsBox.querySelectorAll('.ht-live-search-item');
        if (items[selectedIndex]) {
          e.preventDefault();
          items[selectedIndex].click();
        }
      }
    } else if (e.key === 'Escape') {
      if (resultsBox.style.display !== 'none') {
        e.preventDefault();
        e.stopPropagation();
        clearResults();
      }
    }
  });

  // Document Click to dismiss suggestions
  document.addEventListener('click', function (e) {
    if (!resultsBox.contains(e.target) && e.target !== searchInput) {
      if (resultsBox.style.display !== 'none') {
        clearResults();
      }
    }
  });
})();
