/**
 * Real-Time Academic Exam Countdown Ticker for HelpTrickBD EduPortal
 * Bengali Digit Localization, ARIA Live Politeness & Zero-Jank Animation
 *
 * @package HelpTrickBD_EduPortal
 */

(function () {
  'use strict';

  var timerCards = document.querySelectorAll('.ht-exam-timer-card');
  if (!timerCards.length) {
    return;
  }

  var BENGALI_DIGITS = ['\u09e6', '\u09e7', '\u09e8', '\u09e9', '\u09ea', '\u09eb', '\u09ec', '\u09ed', '\u09ee', '\u09ef']; // ০-৯

  function toBengali(num) {
    var str = String(num);
    var res = '';
    for (var i = 0; i < str.length; i++) {
      var d = parseInt(str[i], 10);
      res += isNaN(d) ? str[i] : BENGALI_DIGITS[d];
    }
    return res;
  }

  function pad(n) {
    return n < 10 ? '0' + n : String(n);
  }

  // Initialize ARIA Live attributes on countdown cells
  timerCards.forEach(function (card) {
    var cells = card.querySelectorAll('.ht-countdown-cell, .ht-countdown-val');
    cells.forEach(function (cell) {
      cell.setAttribute('aria-live', 'polite');
      cell.setAttribute('aria-atomic', 'true');
    });
  });

  function tick() {
    var now = Date.now();

    timerCards.forEach(function (card) {
      var targetStr = card.getAttribute('data-countdown-date');
      if (!targetStr) return;

      var targetDate = new Date(targetStr);
      var targetTime = targetDate.getTime();

      var daysEl = card.querySelector('[data-cd-days]');
      var hoursEl = card.querySelector('[data-cd-hours]');
      var minsEl = card.querySelector('[data-cd-minutes]');
      var secsEl = card.querySelector('[data-cd-seconds]');

      // Error handling: Invalid target date
      if (isNaN(targetTime)) {
        window.requestAnimationFrame(function () {
          if (daysEl) daysEl.textContent = '\u09e6\u09e6';
          if (hoursEl) hoursEl.textContent = '\u09e6\u09e6';
          if (minsEl) minsEl.textContent = '\u09e6\u09e6';
          if (secsEl) secsEl.textContent = '\u09e6\u09e6';
        });
        return;
      }

      var diff = targetTime - now;

      // Error handling / Boundary condition: Exam date has passed
      if (diff <= 0) {
        window.requestAnimationFrame(function () {
          if (daysEl) daysEl.textContent = '\u09e6\u09e6';
          if (hoursEl) hoursEl.textContent = '\u09e6\u09e6';
          if (minsEl) minsEl.textContent = '\u09e6\u09e6';
          if (secsEl) secsEl.textContent = '\u09e6\u09e6';
          card.classList.add('ht-exam-ended');
          var badge = card.querySelector('.ht-exam-status-badge, [data-cd-badge]');
          if (badge) {
            badge.textContent = '\u09aa\u09b0\u09c0\u0995\u09cd\u09b7\u09be \u09b8\u09ae\u09be\u09aa\u09cd\u09a4'; // পরীক্ষা সমাপ্ত
          }
        });
        return;
      }

      var days = Math.floor(diff / (1000 * 60 * 60 * 24));
      var hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      var minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
      var seconds = Math.floor((diff % (1000 * 60)) / 1000);

      var bengaliDays = toBengali(days);
      var bengaliHours = toBengali(pad(hours));
      var bengaliMins = toBengali(pad(minutes));
      var bengaliSecs = toBengali(pad(seconds));

      window.requestAnimationFrame(function () {
        if (daysEl && daysEl.textContent !== bengaliDays) daysEl.textContent = bengaliDays;
        if (hoursEl && hoursEl.textContent !== bengaliHours) hoursEl.textContent = bengaliHours;
        if (minsEl && minsEl.textContent !== bengaliMins) minsEl.textContent = bengaliMins;
        if (secsEl && secsEl.textContent !== bengaliSecs) secsEl.textContent = bengaliSecs;
      });
    });
  }

  tick();
  setInterval(tick, 1000);
})();
