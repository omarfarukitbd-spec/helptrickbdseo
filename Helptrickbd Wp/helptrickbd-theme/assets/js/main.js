/**
 * HelpTrickBD Pro - Main JavaScript
 * Dark Mode, Circular Scroll, Bookmarks, Countdown & Cookie Consent.
 * Zero jQuery, Pure Vanilla JavaScript.
 */

(function () {
    'use strict';

    // -------------------------------------------------------------
    // 1. Toast Notification Helper
    // -------------------------------------------------------------
    window.htToast = function (message) {
        let toast = document.getElementById('ht-toast');
        if (!toast) {
            toast = document.createElement('div');
            toast.id = 'ht-toast';
            toast.className = 'ht-toast';
            document.body.appendChild(toast);
        }
        toast.textContent = message;
        toast.classList.add('ht-show');
        setTimeout(() => {
            toast.classList.remove('ht-show');
        }, 3000);
    };

    // Helper: English to Bengali Numerals
    function toBnNumber(num) {
        const en = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
        const bn = ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯'];
        return String(num).replace(/[0-9]/g, (w) => bn[+w]);
    }

    // -------------------------------------------------------------
    // 2. Dark / Light Mode Switcher
    // -------------------------------------------------------------
    const themeToggle = document.getElementById('ht-theme-toggle');
    const htmlEl = document.documentElement;

    function initTheme() {
        const savedTheme = localStorage.getItem('ht_theme');
        if (savedTheme) {
            htmlEl.setAttribute('data-theme', savedTheme);
        } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            htmlEl.setAttribute('data-theme', 'dark');
        } else {
            htmlEl.setAttribute('data-theme', 'light');
        }
    }

    if (themeToggle) {
        themeToggle.addEventListener('click', function () {
            const current = htmlEl.getAttribute('data-theme');
            const next = current === 'dark' ? 'light' : 'dark';
            htmlEl.setAttribute('data-theme', next);
            localStorage.setItem('ht_theme', next);
        });
    }

    initTheme();

    // -------------------------------------------------------------
    // 3. Circular Scroll-to-Top Progress Indicator
    // -------------------------------------------------------------
    const scrollTopBtn = document.getElementById('ht-scroll-top');
    const progressCircle = document.getElementById('ht-progress-circle');
    const circumference = 2 * Math.PI * 20; // r=20 -> ~125.66

    if (progressCircle) {
        progressCircle.style.strokeDasharray = `${circumference} ${circumference}`;
        progressCircle.style.strokeDashoffset = circumference;
    }

    function updateScrollProgress() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const progress = scrollHeight > 0 ? scrollTop / scrollHeight : 0;

        if (progressCircle) {
            const offset = circumference - (progress * circumference);
            progressCircle.style.strokeDashoffset = offset;
        }

        if (scrollTopBtn) {
            if (scrollTop > 300) {
                scrollTopBtn.classList.add('ht-visible');
            } else {
                scrollTopBtn.classList.remove('ht-visible');
            }
        }
    }

    window.addEventListener('scroll', updateScrollProgress, { passive: true });

    if (scrollTopBtn) {
        scrollTopBtn.addEventListener('click', function () {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // -------------------------------------------------------------
    // 4. Live Exam Countdown Timer
    // -------------------------------------------------------------
    function initExamCountdown() {
        if (!window.htConfig || !window.htConfig.countdownDate) return;

        const targetDate = new Date(window.htConfig.countdownDate).getTime();
        const now = new Date().getTime();
        const diff = targetDate - now;

        const days = Math.max(0, Math.ceil(diff / (1000 * 60 * 60 * 24)));
        const daysBn = toBnNumber(days);

        const topVal = document.getElementById('ht-countdown-val');
        if (topVal) {
            topVal.textContent = `${daysBn} দিন বাকি`;
        }

        const sideVal = document.getElementById('ht-sidebar-days-val');
        if (sideVal) {
            sideVal.textContent = daysBn;
        }

        const drawerVal = document.getElementById('ht-drawer-countdown-val');
        if (drawerVal) {
            drawerVal.textContent = `${daysBn} দিন বাকি`;
        }
    }

    initExamCountdown();

    // -------------------------------------------------------------
    // 5. Mobile Drawer Navigation
    // -------------------------------------------------------------
    const menuToggle = document.getElementById('ht-menu-toggle');
    const drawer = document.getElementById('ht-mobile-drawer');
    const drawerOverlay = document.getElementById('ht-drawer-overlay');
    const drawerClose = document.getElementById('ht-drawer-close');
    const dockMenuBtn = document.getElementById('ht-dock-menu-btn');

    function openMobileDrawer() {
        if (drawer) drawer.classList.add('ht-open');
        if (drawerOverlay) drawerOverlay.classList.add('ht-open');
    }

    function closeMobileDrawer() {
        if (drawer) drawer.classList.remove('ht-open');
        if (drawerOverlay) drawerOverlay.classList.remove('ht-open');
    }

    if (menuToggle) menuToggle.addEventListener('click', openMobileDrawer);
    if (dockMenuBtn) dockMenuBtn.addEventListener('click', openMobileDrawer);
    if (drawerClose) drawerClose.addEventListener('click', closeMobileDrawer);
    if (drawerOverlay) drawerOverlay.addEventListener('click', closeMobileDrawer);

    // -------------------------------------------------------------
    // 6. LocalStorage Bookmarks Drawer ("পড়ার তালিকা")
    // -------------------------------------------------------------
    const bmTrigger = document.getElementById('ht-bookmarks-trigger');
    const dockBmBtn = document.getElementById('ht-dock-bookmark-btn');
    const bmDrawer = document.getElementById('ht-bookmarks-drawer');
    const bmOverlay = document.getElementById('ht-bm-overlay');
    const bmClose = document.getElementById('ht-bm-close');
    const bmList = document.getElementById('ht-bookmarks-list');
    const bmBadge = document.getElementById('ht-bookmark-badge');
    const dockBmCount = document.getElementById('ht-dock-bm-count');
    const clearBmBtn = document.getElementById('ht-clear-bookmarks');

    function getBookmarks() {
        try {
            return JSON.parse(localStorage.getItem('ht_bookmarks') || '[]');
        } catch (e) {
            return [];
        }
    }

    function saveBookmarks(bms) {
        localStorage.setItem('ht_bookmarks', JSON.stringify(bms));
        updateBookmarksUI();
    }

    function updateBookmarksUI() {
        const bms = getBookmarks();
        const count = bms.length;
        const countBn = toBnNumber(count);

        if (bmBadge) bmBadge.textContent = countBn;
        if (dockBmCount) dockBmCount.textContent = countBn;

        // Update card buttons
        document.querySelectorAll('.ht-bookmark-toggle').forEach(btn => {
            const id = btn.getAttribute('data-id');
            const exists = bms.some(item => item.id == id);
            if (exists) {
                btn.classList.add('ht-saved');
            } else {
                btn.classList.remove('ht-saved');
            }
        });

        // Render in drawer
        if (bmList) {
            if (count === 0) {
                bmList.innerHTML = `
                    <div class="ht-empty-bookmarks">
                        <svg class="ht-m3-icon ht-empty-icon" width="48" height="48" viewBox="0 0 24 24" fill="currentColor"><path d="M17 3H7c-1.1 0-1.99.9-1.99 2L5 21l7-3 7 3V5c0-1.1-.9-2-2-2z"/></svg>
                        <p>আপনার পড়ার তালিকায় এখনো কোনো হ্যান্ডনোট নেই।</p>
                        <span>যেকোনো পোস্টের বুকমার্ক আইকনে ক্লিক করে সংরক্ষণ করুন।</span>
                    </div>`;
            } else {
                let html = '<div class="ht-bm-items-wrap">';
                bms.forEach(item => {
                    html += `
                        <div class="ht-bm-item">
                            <a href="${item.url}" class="ht-bm-title">${item.title}</a>
                            <button class="ht-bm-remove" data-id="${item.id}" aria-label="মুছে ফেলুন">
                                <svg class="ht-m3-icon" width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/></svg>
                            </button>
                        </div>`;
                });
                html += '</div>';
                bmList.innerHTML = html;

                // Bind remove buttons
                bmList.querySelectorAll('.ht-bm-remove').forEach(rmBtn => {
                    rmBtn.addEventListener('click', function () {
                        const id = this.getAttribute('data-id');
                        const updated = getBookmarks().filter(i => i.id != id);
                        saveBookmarks(updated);
                        window.htToast('পড়ার তালিকা থেকে মুছে ফেলা হয়েছে');
                    });
                });
            }
        }
    }

    function toggleBookmark(id, title, url) {
        let bms = getBookmarks();
        const index = bms.findIndex(i => i.id == id);
        if (index > -1) {
            bms.splice(index, 1);
            saveBookmarks(bms);
            window.htToast('পড়ার তালিকা থেকে অপসারিত হয়েছে');
        } else {
            bms.unshift({ id, title, url });
            saveBookmarks(bms);
            window.htToast('পড়ার তালিকায় সফলভাবে সংরক্ষিত হয়েছে');
        }
    }

    // Bind bookmark toggle buttons globally
    document.addEventListener('click', function (e) {
        const btn = e.target.closest('.ht-bookmark-toggle');
        if (btn) {
            e.preventDefault();
            const id = btn.getAttribute('data-id');
            const title = btn.getAttribute('data-title');
            const url = btn.getAttribute('data-url');
            toggleBookmark(id, title, url);
        }
    });

    function openBookmarksDrawer() {
        if (bmDrawer) bmDrawer.classList.add('ht-open');
        if (bmOverlay) bmOverlay.classList.add('ht-open');
        updateBookmarksUI();
    }

    function closeBookmarksDrawer() {
        if (bmDrawer) bmDrawer.classList.remove('ht-open');
        if (bmOverlay) bmOverlay.classList.remove('ht-open');
    }

    if (bmTrigger) bmTrigger.addEventListener('click', openBookmarksDrawer);
    if (dockBmBtn) dockBmBtn.addEventListener('click', openBookmarksDrawer);
    if (bmClose) bmClose.addEventListener('click', closeBookmarksDrawer);
    if (bmOverlay) bmOverlay.addEventListener('click', closeBookmarksDrawer);

    if (clearBmBtn) {
        clearBmBtn.addEventListener('click', function () {
            if (confirm('আপনি কি পড়ার তালিকার সকল হ্যান্ডনোট মুছে ফেলতে চান?')) {
                saveBookmarks([]);
                window.htToast('সকল বুকমার্ক মুছে ফেলা হয়েছে');
            }
        });
    }

    updateBookmarksUI();

    // -------------------------------------------------------------
    // 7. Cookie Consent Banner & Polite AdBlocker Modal
    // -------------------------------------------------------------
    const cookieBanner = document.getElementById('ht-cookie-banner');
    const cookieAcceptBtn = document.getElementById('ht-cookie-accept');

    if (cookieBanner && !localStorage.getItem('ht_cookie_accepted')) {
        setTimeout(() => {
            cookieBanner.style.display = 'block';
        }, 1500);
    }

    if (cookieAcceptBtn) {
        cookieAcceptBtn.addEventListener('click', function () {
            localStorage.setItem('ht_cookie_accepted', 'true');
            if (cookieBanner) cookieBanner.style.display = 'none';
        });
    }

    // Polite AdBlocker Check
    const adblockModal = document.getElementById('ht-adblock-modal');
    const adblockDismiss = document.getElementById('ht-adblock-dismiss');

    if (adblockDismiss && adblockModal) {
        adblockDismiss.addEventListener('click', function () {
            adblockModal.classList.remove('ht-open');
            sessionStorage.setItem('ht_adblock_dismissed', 'true');
        });
    }

    function checkAdBlocker() {
        if (sessionStorage.getItem('ht_adblock_dismissed')) return;
        const testAd = document.createElement('div');
        testAd.innerHTML = '&nbsp;';
        testAd.className = 'adsbox pub_300x250 pub_300x250m pub_728x90 text-ad textAd text_ad text_ads text-ads text-ad-links';
        testAd.style.position = 'absolute';
        testAd.style.top = '-999px';
        document.body.appendChild(testAd);

        setTimeout(() => {
            if (testAd.offsetHeight === 0 && adblockModal) {
                adblockModal.classList.add('ht-open');
            }
            testAd.remove();
        }, 2000);
    }

    // -------------------------------------------------------------
    // 8. Sidebar Top Instant AJAX Live Search
    // -------------------------------------------------------------
    const sideSearchInput = document.getElementById('ht-side-search-input');
    const sideSearchResults = document.getElementById('ht-side-search-results');
    const sideSearchClear = document.getElementById('ht-side-search-clear');
    const sideSearchSpinner = document.getElementById('ht-side-search-spinner');
    let sideSearchTimer = null;

    if (sideSearchInput && sideSearchResults) {
        function executeSideSearch(query) {
            query = query.trim();
            if (query.length < 2) {
                sideSearchResults.style.display = 'none';
                sideSearchResults.innerHTML = '';
                if (sideSearchSpinner) sideSearchSpinner.style.display = 'none';
                return;
            }

            if (!window.htConfig) return;

            if (sideSearchSpinner) sideSearchSpinner.style.display = 'block';

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
                if (sideSearchSpinner) sideSearchSpinner.style.display = 'none';

                if (data.success && data.data && data.data.results && data.data.results.length > 0) {
                    let html = '<div class="ht-side-results-list">';
                    data.data.results.forEach(item => {
                        const thumbHtml = item.thumbnail 
                            ? `<img src="${item.thumbnail}" class="ht-side-result-thumb" alt="" loading="lazy">` 
                            : `<div class="ht-side-result-thumb-fallback"><svg class="ht-m3-icon" width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/></svg></div>`;

                        html += `
                            <a href="${item.url}" class="ht-side-result-item">
                                ${thumbHtml}
                                <div class="ht-side-result-info">
                                    <span class="ht-side-result-cat">${item.category}</span>
                                    <h5 class="ht-side-result-title">${item.title}</h5>
                                    <span class="ht-side-result-date">${item.date}</span>
                                </div>
                            </a>
                        `;
                    });
                    html += `
                        <a href="${window.htConfig.siteUrl}/?s=${encodeURIComponent(query)}" class="ht-side-result-all">
                            <span>সকল ফলাফল দেখুন</span>
                            <svg class="ht-m3-icon" width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
                        </a>
                    </div>`;
                    sideSearchResults.innerHTML = html;
                    sideSearchResults.style.display = 'block';
                } else {
                    sideSearchResults.innerHTML = '<div class="ht-side-result-none">কোন ফলাফল পাওয়া যায়নি</div>';
                    sideSearchResults.style.display = 'block';
                }
            })
            .catch(() => {
                if (sideSearchSpinner) sideSearchSpinner.style.display = 'none';
            });
        }

        sideSearchInput.addEventListener('input', function () {
            const val = this.value;
            if (sideSearchClear) {
                sideSearchClear.style.display = val.length > 0 ? 'inline-flex' : 'none';
            }

            clearTimeout(sideSearchTimer);
            sideSearchTimer = setTimeout(() => {
                executeSideSearch(val);
            }, 280);
        });

        if (sideSearchClear) {
            sideSearchClear.addEventListener('click', function () {
                sideSearchInput.value = '';
                sideSearchClear.style.display = 'none';
                sideSearchResults.style.display = 'none';
                sideSearchResults.innerHTML = '';
                sideSearchInput.focus();
            });
        }

        // Close dropdown when clicking outside
        document.addEventListener('click', function (e) {
            if (!e.target.closest('.ht-side-search-box')) {
                sideSearchResults.style.display = 'none';
            }
        });

        // Close on Escape key
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && sideSearchResults.style.display === 'block') {
                sideSearchResults.style.display = 'none';
            }
        });
    }

})();

