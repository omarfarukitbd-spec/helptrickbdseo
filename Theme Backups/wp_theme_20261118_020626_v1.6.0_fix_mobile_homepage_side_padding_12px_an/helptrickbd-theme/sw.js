/**
 * HelpTrickBD Pro - Advanced Progressive Web App Service Worker
 * Stale-While-Revalidate for CSS/JS/Fonts, Network-First for HTML, Offline Fallback.
 * Version: 1.2.6
 */

const CACHE_VERSION = 'helptrickbd-pwa-v1.2.6';
const STATIC_CACHE = `ht-static-${CACHE_VERSION}`;
const DYNAMIC_CACHE = `ht-dynamic-${CACHE_VERSION}`;
const OFFLINE_URL = '/wp-content/themes/helptrickbd-theme/offline.html';

const PRECACHE_ASSETS = [
    '/',
    OFFLINE_URL,
    '/wp-content/themes/helptrickbd-theme/style.css',
    '/wp-content/themes/helptrickbd-theme/assets/css/main.css',
    '/wp-content/themes/helptrickbd-theme/assets/js/main.js',
    '/wp-content/themes/helptrickbd-theme/manifest.json',
    '/wp-content/themes/helptrickbd-theme/assets/images/icon-192.png'
];

// Install Event - Precache critical assets
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(STATIC_CACHE).then((cache) => {
            return cache.addAll(PRECACHE_ASSETS).catch((err) => {
                console.warn('[SW] Pre-caching partial failure:', err);
            });
        })
    );
    self.skipWaiting();
});

// Activate Event - Clean up stale cache versions
self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((keys) => {
            return Promise.all(
                keys.map((key) => {
                    if (key !== STATIC_CACHE && key !== DYNAMIC_CACHE) {
                        return caches.delete(key);
                    }
                })
            );
        })
    );
    self.clients.claim();
});

// Fetch Event - Smart routing strategy
self.addEventListener('fetch', (event) => {
    const { request } = event;
    const url = new URL(request.url);

    // Skip non-GET, admin, login, and REST/AJAX requests
    if (
        request.method !== 'GET' ||
        url.pathname.includes('/wp-admin') ||
        url.pathname.includes('/wp-login') ||
        url.pathname.includes('admin-ajax.php')
    ) {
        return;
    }

    // 1. Navigation requests (HTML pages) -> Network first, fallback to cache, fallback to offline.html
    if (request.mode === 'navigate') {
        event.respondWith(
            fetch(request)
                .then((networkResponse) => {
                    if (networkResponse && networkResponse.status === 200) {
                        const responseClone = networkResponse.clone();
                        caches.open(DYNAMIC_CACHE).then((cache) => {
                            cache.put(request, responseClone);
                        });
                    }
                    return networkResponse;
                })
                .catch(() => {
                    return caches.match(request).then((cachedResponse) => {
                        return cachedResponse || caches.match(OFFLINE_URL);
                    });
                })
        );
        return;
    }

    // 2. Static Assets (CSS, JS, Web Fonts, Images) -> Stale-While-Revalidate
    if (
        request.destination === 'style' ||
        request.destination === 'script' ||
        request.destination === 'font' ||
        request.destination === 'image'
    ) {
        event.respondWith(
            caches.match(request).then((cachedResponse) => {
                const fetchPromise = fetch(request)
                    .then((networkResponse) => {
                        if (networkResponse && networkResponse.status === 200) {
                            const responseClone = networkResponse.clone();
                            caches.open(DYNAMIC_CACHE).then((cache) => {
                                cache.put(request, responseClone);
                            });
                        }
                        return networkResponse;
                    })
                    .catch(() => cachedResponse);

                return cachedResponse || fetchPromise;
            })
        );
        return;
    }

    // Default fetch
    event.respondWith(
        caches.match(request).then((cachedResponse) => {
            return cachedResponse || fetch(request);
        })
    );
});
