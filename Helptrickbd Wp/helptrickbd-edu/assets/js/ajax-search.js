/**
 * Live AJAX Instant Search for HelpTrickBD EduPortal
 * Debounced REST API query with zero-CLS suggestions dropdown
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

  var debounceTimer = null;
  var currentQuery = '';

  var restUrl = (window.htbdEduSettings && window.htbdEduSettings.restUrl)
    ? window.htbdEduSettings.restUrl
    : '/wp-json/wp/v2/';

  function decodeHtml(html) {
    var txt = document.createElement('textarea');
    txt.innerHTML = html;
    return txt.value;
  }

  function renderResults(posts) {
    if (!posts || posts.length === 0) {
      resultsBox.innerHTML = '<div style="padding:14px;text-align:center;color:var(--ht-text-muted);font-size:0.875rem;">কোনো ফলাফল পাওয়া যায়নি। সম্পূর্ণ অনুসন্ধানের জন্য এন্টার চাপুন।</div>';
      resultsBox.style.display = 'block';
      return;
    }

    var html = '';
    posts.forEach(function (post) {
      var title = decodeHtml(post.title.rendered);
      var link = post.link;
      var thumb = '';

      if (post._embedded && post._embedded['wp:featuredmedia'] && post._embedded['wp:featuredmedia'][0]) {
        var media = post._embedded['wp:featuredmedia'][0];
        thumb = media.source_url || (media.media_details && media.media_details.sizes && media.media_details.sizes.thumbnail && media.media_details.sizes.thumbnail.source_url);
      }

      html += '<a href="' + link + '" class="ht-live-search-item" role="option">';
      if (thumb) {
        html += '<img src="' + thumb + '" alt="" class="ht-live-search-thumb" loading="lazy">';
      }
      html += '<div style="flex:1;overflow:hidden;">';
      html += '<div class="ht-live-search-title">' + title + '</div>';
      html += '<div class="ht-live-search-meta">একাডেমিক হ্যান্ডনোট</div>';
      html += '</div>';
      html += '</a>';
    });

    resultsBox.innerHTML = html;
    resultsBox.style.display = 'flex';
  }

  searchInput.addEventListener('input', function (e) {
    var q = e.target.value.trim();

    if (debounceTimer) {
      clearTimeout(debounceTimer);
    }

    if (q.length < 2) {
      resultsBox.innerHTML = '';
      resultsBox.style.display = 'none';
      currentQuery = '';
      return;
    }

    currentQuery = q;

    debounceTimer = setTimeout(function () {
      var fetchUrl = restUrl + 'posts?search=' + encodeURIComponent(q) + '&_embed=1&per_page=5';

      fetch(fetchUrl)
        .then(function (res) {
          if (!res.ok) throw new Error('Network error');
          return res.json();
        })
        .then(function (data) {
          if (searchInput.value.trim() === currentQuery) {
            renderResults(data);
          }
        })
        .catch(function () {
          resultsBox.innerHTML = '<div style="padding:10px;text-align:center;color:var(--ht-text-muted);font-size:0.85rem;">সার্চে সমস্যা হয়েছে। সম্পূর্ণ পেজে খুঁজতে এন্টার চাপুন।</div>';
          resultsBox.style.display = 'block';
        });
    }, 250);
  });
})();
