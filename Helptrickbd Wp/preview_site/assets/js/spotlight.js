/**
 * HelpTrickBD Pro - "Ctrl+K" Spotlight Live Search
 * Debounced AJAX, Keyboard Navigation (Arrow Keys / Enter), Trending Tags.
 */

(function () {
    'use strict';

    const triggerBtn = document.getElementById('ht-search-trigger');
    const dockSearchBtn = document.getElementById('ht-dock-search-btn');
    const modal = document.getElementById('ht-spotlight-modal');
    const overlay = document.getElementById('ht-spotlight-overlay');
    const closeBtn = document.getElementById('ht-spotlight-close');
    const searchInput = document.getElementById('ht-spotlight-input');
    const resultsContainer = document.getElementById('ht-spotlight-results');

    let debounceTimer = null;
    let selectedIndex = -1;

    // Default Trending HTML
    const defaultTrendingHTML = resultsContainer ? resultsContainer.innerHTML : '';

    function openSpotlight() {
        if (!modal) return;
        modal.classList.add('ht-open');
        document.body.style.overflow = 'hidden';
        setTimeout(() => {
            if (searchInput) {
                searchInput.focus();
                searchInput.select();
            }
        }, 50);
    }

    function closeSpotlight() {
        if (!modal) return;
        modal.classList.remove('ht-open');
        document.body.style.overflow = '';
        if (searchInput) searchInput.value = '';
        if (resultsContainer) resultsContainer.innerHTML = defaultTrendingHTML;
        bindTrendingTags();
        selectedIndex = -1;
    }

    if (triggerBtn) triggerBtn.addEventListener('click', openSpotlight);
    if (dockSearchBtn) dockSearchBtn.addEventListener('click', openSpotlight);
    if (closeBtn) closeBtn.addEventListener('click', closeSpotlight);
    if (overlay) overlay.addEventListener('click', closeSpotlight);

    // Global Keyboard Shortcut: Ctrl+K or Cmd+K
    document.addEventListener('keydown', function (e) {
        if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
            e.preventDefault();
            if (modal && modal.classList.contains('ht-open')) {
                closeSpotlight();
            } else {
                openSpotlight();
            }
        } else if (e.key === 'Escape' && modal && modal.classList.contains('ht-open')) {
            closeSpotlight();
        }
    });

    // Trending Tags Click Handler
    function bindTrendingTags() {
        document.querySelectorAll('.ht-trending-tag').forEach(tag => {
            tag.addEventListener('click', function () {
                const query = this.getAttribute('data-query');
                if (searchInput) {
                    searchInput.value = query;
                    performSearch(query);
                }
            });
        });
    }

    bindTrendingTags();

    // AJAX Search Execution
    function performSearch(query) {
        query = query.trim();
        if (query.length < 2) {
            if (resultsContainer) resultsContainer.innerHTML = defaultTrendingHTML;
            bindTrendingTags();
            return;
        }

        if (!resultsContainer || !window.htConfig) return;

        resultsContainer.innerHTML = '<div class="ht-search-loading" style="padding:24px;text-align:center;color:var(--ht-text-muted);">অনুসন্ধান করা হচ্ছে...</div>';

        const formData = new FormData();
        formData.append('action', 'ht_live_search');
        formData.append('nonce', window.htConfig.searchNonce);
        formData.append('query', query);

        fetch(window.htConfig.ajaxUrl, {
            method: 'POST',
            body: formData,
        })
            .then(res => res.json())
            .then(data => {
                if (data.success && data.data && data.data.results && data.data.results.length > 0) {
                    renderSearchResults(data.data.results);
                } else {
                    resultsContainer.innerHTML = `
                        <div class="ht-search-no-results" style="padding:28px 12px;text-align:center;color:var(--ht-text-muted);">
                            <p style="font-weight:600;margin-bottom:6px;">"${escapeHtml(query)}" এর জন্য কোনো ফলাফল পাওয়া যায়নি</p>
                            <span style="font-size:0.85rem;">বানান পরীক্ষা করুন বা অন্য কোনো সাধারণ বিষয় অনুসন্ধান করুন।</span>
                        </div>`;
                }
            })
            .catch(() => {
                resultsContainer.innerHTML = '<div style="padding:20px;text-align:center;color:var(--ht-danger);">অনুসন্ধানে সমস্যা হয়েছে। পুনরায় চেষ্টা করুন।</div>';
            });
    }

    function renderSearchResults(results) {
        let html = '<ul class="ht-search-results-list" id="ht-search-list">';
        results.forEach((item, index) => {
            const thumbHtml = item.thumbnail
                ? `<img src="${item.thumbnail}" class="ht-search-res-thumb" alt="${escapeHtml(item.title)}">`
                : `<div class="ht-search-res-thumb" style="background:var(--ht-surface-hover);display:flex;align-items:center;justify-content:center;"><svg class="ht-m3-icon" width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l-5.5 9h11z"/></svg></div>`;

            html += `
                <li class="ht-search-result-item" data-index="${index}">
                    <a href="${item.url}">
                        ${thumbHtml}
                        <div class="ht-search-res-info">
                            <h4 class="ht-search-res-title">${escapeHtml(item.title)}</h4>
                            <div class="ht-search-res-meta">
                                <span>${escapeHtml(item.category)}</span> &bull; <span>${escapeHtml(item.date)}</span>
                            </div>
                        </div>
                    </a>
                </li>`;
        });
        html += '</ul>';
        resultsContainer.innerHTML = html;
        selectedIndex = -1;
    }

    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    // Input Typing Debounce Listener
    if (searchInput) {
        searchInput.addEventListener('input', function () {
            clearTimeout(debounceTimer);
            const query = this.value;
            debounceTimer = setTimeout(() => {
                performSearch(query);
            }, 260);
        });

        // Keyboard Navigation (Arrow Keys & Enter)
        searchInput.addEventListener('keydown', function (e) {
            const items = document.querySelectorAll('.ht-search-result-item');
            if (items.length === 0) return;

            if (e.key === 'ArrowDown') {
                e.preventDefault();
                selectedIndex = (selectedIndex + 1) % items.length;
                updateSelection(items);
            } else if (e.key === 'ArrowUp') {
                e.preventDefault();
                selectedIndex = (selectedIndex - 1 + items.length) % items.length;
                updateSelection(items);
            } else if (e.key === 'Enter') {
                if (selectedIndex > -1 && items[selectedIndex]) {
                    e.preventDefault();
                    const link = items[selectedIndex].querySelector('a');
                    if (link) window.location.href = link.href;
                }
            }
        });
    }

    function updateSelection(items) {
        items.forEach((item, idx) => {
            if (idx === selectedIndex) {
                item.classList.add('ht-selected');
                item.scrollIntoView({ block: 'nearest' });
            } else {
                item.classList.remove('ht-selected');
            }
        });
    }

})();
