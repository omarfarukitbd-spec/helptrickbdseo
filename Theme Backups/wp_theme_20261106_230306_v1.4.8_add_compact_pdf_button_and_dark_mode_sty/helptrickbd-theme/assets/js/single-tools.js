/**
 * HelpTrickBD Pro - Single Post Academic Tools
 * TOC, Reading Bar, Font Resizer, Focus Mode, Text Highlight, MCQ Engine, Code Runner & Citation.
 */

(function () {
    'use strict';

    const articleBody = document.getElementById('ht-article-body');
    if (!articleBody) return;

    // -------------------------------------------------------------
    // 1. Live Reading Progress Bar
    // -------------------------------------------------------------
    const progressFill = document.getElementById('ht-progress-fill');

    function updateReadingProgress() {
        if (!progressFill) return;
        const rect = articleBody.getBoundingClientRect();
        const articleTop = rect.top + window.pageYOffset;
        const articleHeight = rect.height;
        const currentScroll = window.pageYOffset;
        const windowHeight = window.innerHeight;

        if (currentScroll < articleTop) {
            progressFill.style.width = '0%';
        } else if (currentScroll > (articleTop + articleHeight - windowHeight)) {
            progressFill.style.width = '100%';
        } else {
            const percent = ((currentScroll - articleTop) / (articleHeight - windowHeight)) * 100;
            progressFill.style.width = `${Math.min(100, Math.max(0, percent))}%`;
        }
    }

    window.addEventListener('scroll', updateReadingProgress, { passive: true });

    // -------------------------------------------------------------
    // -------------------------------------------------------------
    // 2. Auto Table of Contents (সূচিপত্র) Generator
    // -------------------------------------------------------------
    const tocContainer = document.getElementById('ht-toc-container');
    const tocNav = document.getElementById('ht-toc-nav');
    const tocToggle = document.getElementById('ht-toc-header');

    if (tocContainer && tocNav) {
        const headings = articleBody.querySelectorAll('h2, h3');

        if (headings.length < 2) {
            tocContainer.style.display = 'none';
        } else {
            // Mobile Specific Behavior: Auto-collapse by default on mobile screens (< 768px)
            const isMobile = window.innerWidth < 768;
            if (isMobile) {
                tocContainer.classList.add('ht-collapsed', 'ht-toc-mobile-mode');
            }

            // Append Chapter/Heading count badge for clear visibility
            const titleWrap = tocContainer.querySelector('.ht-toc-title-wrap');
            if (titleWrap && !titleWrap.querySelector('.ht-toc-count-badge')) {
                const countBadge = document.createElement('span');
                countBadge.className = 'ht-toc-count-badge';
                countBadge.textContent = `${headings.length}টি অধ্যায়`;
                titleWrap.appendChild(countBadge);
            }

            const tocList = document.createElement('ol');
            tocList.className = 'ht-toc-list';

            let currentH2List = null;

            headings.forEach((heading, idx) => {
                const id = heading.id || `ht-section-${idx + 1}`;
                heading.id = id;

                const text = heading.textContent.trim();
                const item = document.createElement('li');
                const link = document.createElement('a');
                link.href = `#${id}`;
                link.textContent = text;

                link.addEventListener('click', function (e) {
                    e.preventDefault();
                    const target = document.getElementById(id);
                    if (target) {
                        const topOffset = target.getBoundingClientRect().top + window.pageYOffset - 85;
                        window.scrollTo({ top: topOffset, behavior: 'smooth' });

                        // On mobile: auto-close TOC after tapping a section link so it doesn't block reading
                        if (window.innerWidth < 768) {
                            tocContainer.classList.add('ht-collapsed');
                        }
                    }
                });

                item.appendChild(link);

                if (heading.tagName.toLowerCase() === 'h2') {
                    tocList.appendChild(item);
                    currentH2List = null;
                } else if (heading.tagName.toLowerCase() === 'h3') {
                    if (!currentH2List) {
                        currentH2List = document.createElement('ul');
                        currentH2List.className = 'ht-toc-sub-list';
                        if (tocList.lastElementChild) {
                            tocList.lastElementChild.appendChild(currentH2List);
                        } else {
                            tocList.appendChild(item);
                        }
                    }
                    if (currentH2List) currentH2List.appendChild(item);
                }
            });

            tocNav.appendChild(tocList);

            if (tocToggle) {
                tocToggle.addEventListener('click', function () {
                    tocContainer.classList.toggle('ht-collapsed');
                });
            }

            // Responsive window resize listener to maintain responsive behavior
            window.addEventListener('resize', function () {
                if (window.innerWidth >= 768) {
                    tocContainer.classList.remove('ht-toc-mobile-mode');
                } else {
                    tocContainer.classList.add('ht-toc-mobile-mode');
                }
            }, { passive: true });

            // Scrollspy: Highlight Active TOC Link
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const id = entry.target.id;
                        document.querySelectorAll('.ht-toc-list a').forEach(a => {
                            if (a.getAttribute('href') === `#${id}`) {
                                a.classList.add('ht-toc-active');
                            } else {
                                a.classList.remove('ht-toc-active');
                            }
                        });
                    }
                });
            }, { rootMargin: '0px 0px -70% 0px' });

            headings.forEach(h => observer.observe(h));
        }
    }

    // -------------------------------------------------------------
    // 3. Dynamic Font Size Resizer (Fully Functional A-, A, A+)
    // -------------------------------------------------------------
    const fontDec = document.getElementById('ht-font-dec');
    const fontReset = document.getElementById('ht-font-reset');
    const fontInc = document.getElementById('ht-font-inc');

    function applyFontSize(size) {
        document.body.classList.remove('ht-font-sm', 'ht-font-lg', 'ht-font-18', 'ht-font-20');
        if (fontDec) fontDec.classList.remove('ht-active');
        if (fontReset) fontReset.classList.remove('ht-active');
        if (fontInc) fontInc.classList.remove('ht-active');

        if (size === 'sm') {
            document.body.classList.add('ht-font-sm');
            if (fontDec) fontDec.classList.add('ht-active');
        } else if (size === 'lg') {
            document.body.classList.add('ht-font-lg');
            if (fontInc) fontInc.classList.add('ht-active');
        } else {
            // Default normal size
            if (fontReset) fontReset.classList.add('ht-active');
        }
        localStorage.setItem('ht_article_font_size', size);
    }

    if (fontDec) {
        fontDec.addEventListener('click', function (e) {
            e.preventDefault();
            applyFontSize('sm');
        });
    }
    if (fontReset) {
        fontReset.addEventListener('click', function (e) {
            e.preventDefault();
            applyFontSize('md');
        });
    }
    if (fontInc) {
        fontInc.addEventListener('click', function (e) {
            e.preventDefault();
            applyFontSize('lg');
        });
    }

    const savedFontSize = localStorage.getItem('ht_article_font_size');
    if (savedFontSize) {
        applyFontSize(savedFontSize);
    }

    // -------------------------------------------------------------
    // 4. Focus Reading Mode Toggle
    // -------------------------------------------------------------
    const focusBtn = document.getElementById('ht-focus-toggle');
    if (focusBtn) {
        focusBtn.addEventListener('click', function () {
            document.body.classList.toggle('ht-focus-mode');
            const isActive = document.body.classList.contains('ht-focus-mode');
            this.classList.toggle('ht-active', isActive);
            if (window.htToast) {
                window.htToast(isActive ? 'ফোকাস রিডিং মোড সক্রিয় হয়েছে' : 'ফোকাস মোড বন্ধ করা হয়েছে');
            }
        });
    }

    // -------------------------------------------------------------
    // 5. 1-Click Print & PDF
    // -------------------------------------------------------------
    const printBtn = document.getElementById('ht-print-btn');
    if (printBtn) {
        printBtn.addEventListener('click', function () {
            window.print();
        });
    }

    // -------------------------------------------------------------
    // 6. Medium-Style Text Highlight Mini-Dock
    // -------------------------------------------------------------
    const highlightDock = document.getElementById('ht-highlight-dock');
    const dockCopyBtn = document.getElementById('ht-dock-copy');
    const dockShareWa = document.getElementById('ht-dock-share-wa');

    document.addEventListener('selectionchange', function () {
        const selection = window.getSelection();
        const selectedText = selection.toString().trim();

        if (selectedText.length > 5 && articleBody.contains(selection.anchorNode)) {
            const range = selection.getRangeAt(0);
            const rect = range.getBoundingClientRect();

            if (highlightDock) {
                highlightDock.style.top = `${rect.top + window.pageYOffset - 44}px`;
                highlightDock.style.left = `${rect.left + window.pageXOffset + (rect.width / 2)}px`;
                highlightDock.style.display = 'flex';
            }
        } else {
            if (highlightDock) highlightDock.style.display = 'none';
        }
    });

    if (dockCopyBtn) {
        dockCopyBtn.addEventListener('click', function () {
            const selectedText = window.getSelection().toString().trim();
            if (selectedText) {
                navigator.clipboard.writeText(selectedText).then(() => {
                    if (window.htToast) window.htToast('টেক্সট ক্লিপবোর্ডে কপি করা হয়েছে');
                    if (highlightDock) highlightDock.style.display = 'none';
                });
            }
        });
    }

    if (dockShareWa) {
        dockShareWa.addEventListener('click', function () {
            const selectedText = window.getSelection().toString().trim();
            if (selectedText) {
                const url = `https://api.whatsapp.com/send?text=${encodeURIComponent('"' + selectedText + '"\n\nপড়ুন বিস্তারিত: ' + window.location.href)}`;
                window.open(url, '_blank');
                if (highlightDock) highlightDock.style.display = 'none';
            }
        });
    }

    // -------------------------------------------------------------
    // 7. 1-Click Code Copy Box
    // -------------------------------------------------------------
    articleBody.querySelectorAll('pre').forEach(pre => {
        const copyBtn = document.createElement('button');
        copyBtn.className = 'ht-code-copy-btn';
        copyBtn.setAttribute('aria-label', 'কোড কপি করুন');
        copyBtn.innerHTML = `
            <svg class="ht-m3-icon" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/>
            </svg>
            <span>কপি করুন</span>`;

        copyBtn.addEventListener('click', function () {
            const code = pre.querySelector('code') || pre;
            navigator.clipboard.writeText(code.textContent).then(() => {
                copyBtn.innerHTML = `
                    <svg class="ht-m3-icon" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/>
                    </svg>
                    <span>কপি সম্পন্ন!</span>`;
                setTimeout(() => {
                    copyBtn.innerHTML = `
                        <svg class="ht-m3-icon" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/>
                        </svg>
                        <span>কপি করুন</span>`;
                }, 2500);
                if (window.htToast) window.htToast('কোড সফলভাবে কপি করা হয়েছে');
            });
        });

        pre.style.position = 'relative';
        pre.appendChild(copyBtn);
    });

    // -------------------------------------------------------------
    // 8. Advanced Multi-Standard Citation Switcher & 1-Click Copy
    // -------------------------------------------------------------
    const citeModule = document.getElementById('ht-citation-module');
    const citeDataEl = document.getElementById('ht-citation-data');
    const citeTextEl = document.getElementById('ht-active-citation-text');
    const citeCopyBtn = document.getElementById('ht-copy-citation-btn');

    if (citeModule && citeDataEl && citeTextEl) {
        let citationData = {};
        try {
            citationData = JSON.parse(citeDataEl.textContent);
        } catch (err) {
            console.error('Failed to parse citation data', err);
        }

        const tabBtns = citeModule.querySelectorAll('.ht-cite-tab-btn');
        tabBtns.forEach(btn => {
            btn.addEventListener('click', function () {
                const format = this.getAttribute('data-cite-format');
                if (format && citationData[format]) {
                    // Update Active Tab State
                    tabBtns.forEach(b => {
                        b.classList.remove('ht-cite-tab-active');
                        b.setAttribute('aria-selected', 'false');
                    });
                    this.classList.add('ht-cite-tab-active');
                    this.setAttribute('aria-selected', 'true');

                    // Update Text Snippet
                    citeTextEl.textContent = citationData[format];
                }
            });
        });

        if (citeCopyBtn) {
            citeCopyBtn.addEventListener('click', function () {
                const textToCopy = citeTextEl.textContent.trim();
                if (!textToCopy) return;

                navigator.clipboard.writeText(textToCopy).then(() => {
                    const labelEl = document.getElementById('ht-copy-citation-label');
                    const readyIcon = citeCopyBtn.querySelector('.ht-copy-icon-ready');
                    const doneIcon = citeCopyBtn.querySelector('.ht-copy-icon-done');

                    citeCopyBtn.classList.add('ht-copied');
                    if (labelEl) labelEl.textContent = 'Copied!';
                    if (readyIcon) readyIcon.style.display = 'none';
                    if (doneIcon) doneIcon.style.display = 'inline-flex';

                    if (window.htToast) {
                        window.htToast('Academic citation copied to clipboard!');
                    }

                    setTimeout(() => {
                        citeCopyBtn.classList.remove('ht-copied');
                        if (labelEl) labelEl.textContent = 'Copy Citation';
                        if (readyIcon) readyIcon.style.display = 'inline-flex';
                        if (doneIcon) doneIcon.style.display = 'none';
                    }, 2500);
                }).catch(err => {
                    console.error('Copy failed', err);
                });
            });
        }
    }

    // -------------------------------------------------------------
    // 9. Interactive MCQ / Quiz Reveal Accordion
    // -------------------------------------------------------------
    document.querySelectorAll('.ht-mcq-reveal-btn').forEach(btn => {
        btn.addEventListener('click', function () {
            const card = this.closest('.ht-mcq-card');
            if (card) {
                const answer = card.querySelector('.ht-mcq-answer');
                if (answer) {
                    answer.classList.toggle('ht-open');
                    this.textContent = answer.classList.contains('ht-open') ? 'উত্তর ও ব্যাখ্যা লুকান' : 'সঠিক উত্তর দেখুন';
                }
            }
        });
    });

    // -------------------------------------------------------------
    // 10. Subject Syllabus Checklist (localStorage persistent)
    // -------------------------------------------------------------
    document.querySelectorAll('.ht-checklist-item').forEach((item, idx) => {
        const pageKey = `ht_check_${window.location.pathname}_${idx}`;
        if (localStorage.getItem(pageKey) === 'true') {
            item.classList.add('ht-checked');
        }

        item.addEventListener('click', function () {
            this.classList.toggle('ht-checked');
            localStorage.setItem(pageKey, this.classList.contains('ht-checked') ? 'true' : 'false');
        });
    });

    // -------------------------------------------------------------
    // 11. Animated PDF Download Button with Timer
    // -------------------------------------------------------------
    document.querySelectorAll('.ht-download-timer-btn').forEach(btn => {
        btn.addEventListener('click', function (e) {
            if (this.getAttribute('data-ready') === 'true') {
                return; // Normal link click
            }

            e.preventDefault();
            const targetUrl = this.getAttribute('data-href') || this.getAttribute('href');
            let seconds = parseInt(window.htConfig.downloadTimer || 5, 10);
            const originalHTML = this.innerHTML;

            this.style.pointerEvents = 'none';
            this.textContent = `ডাউনলোড লিংক তৈরি হচ্ছে: ${seconds} সেকেন্ড...`;

            const interval = setInterval(() => {
                seconds--;
                if (seconds > 0) {
                    this.textContent = `ডাউনলোড লিংক তৈরি হচ্ছে: ${seconds} সেকেন্ড...`;
                } else {
                    clearInterval(interval);
                    this.setAttribute('data-ready', 'true');
                    this.style.pointerEvents = 'auto';
                    this.innerHTML = `
                        <svg class="ht-m3-icon" width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                            <path d="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"/>
                        </svg>
                        <span>এখন ডাউনলোড করুন</span>`;
                    window.location.href = targetUrl;
                }
            }, 1000);
        });
    });

    // -------------------------------------------------------------
    // 12. ICT Live Code Runner / HTML Preview Tab
    // -------------------------------------------------------------
    document.querySelectorAll('.ht-code-runner').forEach(runner => {
        const tabs = runner.querySelectorAll('.ht-runner-tab-btn');
        const panes = runner.querySelectorAll('.ht-runner-pane');
        const codePane = runner.querySelector('.ht-runner-code-pane');
        const previewFrame = runner.querySelector('.ht-runner-preview-frame');

        tabs.forEach(tab => {
            tab.addEventListener('click', function () {
                const target = this.getAttribute('data-tab');
                tabs.forEach(t => t.classList.remove('ht-active'));
                panes.forEach(p => p.classList.remove('ht-active'));

                this.classList.add('ht-active');
                const activePane = runner.querySelector(`.ht-runner-${target}-pane`);
                if (activePane) activePane.classList.add('ht-active');

                // If preview selected, render code in iframe
                if (target === 'preview' && previewFrame && codePane) {
                    const code = codePane.querySelector('code') || codePane;
                    previewFrame.srcdoc = code.textContent;
                }
            });
        });
    });

    // -------------------------------------------------------------
    // 13. Responsive Table Wrapper Automation
    // -------------------------------------------------------------
    articleBody.querySelectorAll('table').forEach(table => {
        if (!table.parentElement.classList.contains('ht-table-wrapper') && !table.parentElement.classList.contains('ht-table-responsive')) {
            const wrapper = document.createElement('div');
            wrapper.className = 'ht-table-responsive';

            const hint = document.createElement('div');
            hint.className = 'ht-table-scroll-hint';
            hint.innerHTML = `
                <svg class="ht-m3-icon" width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M6.99 11L3 15l3.99 4v-3H14v-2H6.99v-3zM21 9l-3.99-4v3H10v2h7.01v3L21 9z"/>
                </svg>
                <span>ডানে-বামে স্ক্রল করে সম্পূর্ণ তালিকা দেখুন</span>`;

            table.parentNode.insertBefore(wrapper, table);
            wrapper.appendChild(hint);
            wrapper.appendChild(table);
        }
    });

    // -------------------------------------------------------------
    // 14. Dark Mode Content Color Normalization for Migrated Articles
    // -------------------------------------------------------------
    function normalizeContentColors() {
        const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
        if (!isDark) return;

        window.requestAnimationFrame(() => {
            const styledElements = articleBody.querySelectorAll('[style*="color"], [style*="background"]');
            styledElements.forEach(el => {
                const style = el.getAttribute('style') || '';
                // Neutralize dark text colors in dark mode
                if (/color\s*:\s*(#[0-6][0-9a-f]{2,5}|#1a73e8|#0c2340|#14532d|#15803d|#0369a1|#047857|#202124|#1e293b|#334155|#64748b|#b45309|#b91c1c|black|rgb\(\s*(?:[0-9]|[1-9][0-9]|1[0-1][0-9])\s*,)/i.test(style)) {
                    el.style.color = '';
                }
                // Neutralize blinding white/light backgrounds in dark mode
                if (/background(-color)?\s*:\s*(#(?:f[0-9a-f]{2,5}|e[0-9a-f]{2,5}|d[0-9a-f]{2,5}|fff(?:fff)?)|white|rgb\(\s*(?:2[0-5][0-9])\s*,|linear-gradient)/i.test(style)) {
                    el.style.backgroundColor = '';
                    el.style.background = '';
                }
            });
        });
    }

    normalizeContentColors();
    const observer = new MutationObserver(() => normalizeContentColors());
    observer.observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] });

    // -------------------------------------------------------------
    // 15. One-Click Social Share Copy Link Tool
    // -------------------------------------------------------------
    document.querySelectorAll('.ht-btn-copy-link').forEach(btn => {
        btn.addEventListener('click', function (e) {
            e.preventDefault();
            const url = this.getAttribute('data-url') || window.location.href;
            if (navigator.clipboard && navigator.clipboard.writeText) {
                navigator.clipboard.writeText(url).then(() => {
                    if (window.htToast) {
                        window.htToast('Article link copied to clipboard!');
                    }
                }).catch(() => {
                    prompt('Press Ctrl+C to copy link:', url);
                });
            } else {
                prompt('Press Ctrl+C to copy link:', url);
            }
        });
    });

    // -------------------------------------------------------------
    // 16. Interactive Post Helpful / Like Reaction Tool
    // -------------------------------------------------------------
    const reactionCard = document.getElementById('ht-reaction-card');
    const likeBtn = document.getElementById('ht-btn-like');
    const countVal = document.getElementById('ht-reaction-count-val');

    if (reactionCard && likeBtn) {
        const postId = reactionCard.getAttribute('data-id') || (window.htConfig ? window.htConfig.currentPostId : 0);
        const storageKey = `ht_liked_post_${postId}`;

        // Check if already liked in this browser
        if (localStorage.getItem(storageKey) === 'true') {
            likeBtn.classList.add('ht-liked');
            likeBtn.setAttribute('title', 'You already liked this article');
        }

        likeBtn.addEventListener('click', function () {
            if (localStorage.getItem(storageKey) === 'true') {
                if (window.htToast) {
                    window.htToast('You already reacted to this article!');
                }
                return;
            }

            if (!window.htConfig || !window.htConfig.ajaxUrl) return;

            // Optimistic UI state
            likeBtn.classList.add('ht-liked', 'ht-animating');
            localStorage.setItem(storageKey, 'true');

            const formData = new FormData();
            formData.append('action', 'ht_like_post');
            formData.append('nonce', window.htConfig.likeNonce);
            formData.append('post_id', postId);

            fetch(window.htConfig.ajaxUrl, {
                method: 'POST',
                body: formData,
            })
                .then(res => res.json())
                .then(data => {
                    likeBtn.classList.remove('ht-animating');
                    if (data.success && data.data) {
                        if (countVal && data.data.count) {
                            countVal.textContent = data.data.count;
                        }
                        if (window.htToast) {
                            window.htToast(data.data.message || 'Thank you for your feedback!');
                        }
                    }
                })
                .catch(() => {
                    likeBtn.classList.remove('ht-animating');
                });
        });
    }

})();


