/**
 * Real-Time Academic Exam Countdown Ticker for HelpTrickBD EduPortal
 * Bengali Digit Localization & Zero-Jank Animation
 *
 * @package HelpTrickBD_EduPortal
 */

(function () {
  'use strict';

  var timerCards = document.querySelectorAll('.ht-exam-timer-card');
  if (!timerCards.length) {
    return;
  }

  var bengaliDigits = ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯'];

  function toBengali(num) {
    var str = String(num);
    var res = '';
    for (var i = 0; i < str.length; i++) {
      var d = parseInt(str[i], 10);
      res += isNaN(d) ? str[i] : bengaliDigits[d];
    }
    return res;
  }

  function pad(n) {
    return n < 10 ? '0' + n : String(n);
  }

  function tick() {
    var now = new Date().getTime();

    timerCards.forEach(function (card) {
      var targetStr = card.getAttribute('data-countdown-date');
      if (!targetStr) return;

      var targetTime = new Date(targetStr).getTime();
      var diff = targetTime - now;

      var daysEl = card.querySelector('[data-cd-days]');
      var hoursEl = card.querySelector('[data-cd-hours]');
      var minsEl = card.querySelector('[data-cd-minutes]');
      var secsEl = card.querySelector('[data-cd-seconds]');

      if (diff <= 0) {
        if (daysEl) daysEl.textContent = '০০';
        if (hoursEl) hoursEl.textContent = '০০';
        if (minsEl) minsEl.textContent = '০০';
        if (secsEl) secsEl.textContent = '০০';
        return;
      }

      var days = Math.floor(diff / (1000 * 60 * 60 * 24));
      var hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      var minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
      var seconds = Math.floor((diff % (1000 * 60)) / 1000);

      if (daysEl) daysEl.textContent = toBengali(days);
      if (hoursEl) hoursEl.textContent = toBengali(pad(hours));
      if (minsEl) minsEl.textContent = toBengali(pad(minutes));
      if (secsEl) secsEl.textContent = toBengali(pad(seconds));
    });
  }

  tick();
  setInterval(tick, 1000);
})();
