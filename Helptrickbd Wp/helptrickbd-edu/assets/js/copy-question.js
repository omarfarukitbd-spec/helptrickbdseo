/**
 * 1-Click Code & Question Copy Engine for HelpTrickBD EduPortal
 * Modern Clipboard API with resilient textarea fallback & accessible toast notifications
 *
 * @package HelpTrickBD_EduPortal
 */

(function () {
  'use strict';

  var toast = document.getElementById('ht-copy-toast');
  var toastMsg = document.getElementById('ht-copy-toast-msg');
  var toastTimeout = null;

  if (toast) {
    toast.setAttribute('role', 'status');
    toast.setAttribute('aria-live', 'polite');
    toast.setAttribute('aria-atomic', 'true');
  }

  function showToast(msg) {
    if (!toast) return;

    window.requestAnimationFrame(function () {
      if (toastMsg && msg) {
        toastMsg.textContent = msg;
      }
      toast.classList.add('show');

      if (toastTimeout) {
        clearTimeout(toastTimeout);
      }
      toastTimeout = setTimeout(function () {
        toast.classList.remove('show');
      }, 2500);
    });
  }

  function copyTextToClipboard(text, successMsg) {
    if (!text) return;

    if (navigator.clipboard && typeof navigator.clipboard.writeText === 'function') {
      navigator.clipboard.writeText(text)
        .then(function () {
          showToast(successMsg);
        })
        .catch(function () {
          // Fallback to legacy execCommand
          fallbackCopy(text, successMsg);
        });
    } else {
      fallbackCopy(text, successMsg);
    }
  }

  function fallbackCopy(text, successMsg) {
    try {
      var textarea = document.createElement('textarea');
      textarea.value = text;
      textarea.setAttribute('readonly', '');
      textarea.style.position = 'fixed';
      textarea.style.top = '-9999px';
      textarea.style.left = '-9999px';
      textarea.style.opacity = '0';
      document.body.appendChild(textarea);
      textarea.focus();
      textarea.select();

      var successful = document.execCommand('copy');
      document.body.removeChild(textarea);

      if (successful) {
        showToast(successMsg);
      } else {
        showToast('\u0995\u09aa\u09bf \u0995\u09b0\u09be \u09b8\u09ae\u09cd\u09ad\u09ac \u09b9\u09df\u09a8\u09bf\u0964'); // কপি করা সম্ভব হয়নি
      }
    } catch (err) {
      showToast('\u0995\u09aa\u09bf \u0995\u09b0\u09be \u09b8\u09ae\u09cd\u09ad\u09ac \u09b9\u09df\u09a8\u09bf\u0964'); // কপি করা সম্ভব হয়নি
    }
  }

  function setupCopyButtons() {
    // 1. Target code blocks (pre)
    var codeBlocks = document.querySelectorAll('.ht-entry-content pre');
    codeBlocks.forEach(function (pre) {
      if (pre.querySelector('.ht-copy-btn')) return;

      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'ht-copy-btn';
      btn.innerHTML = '\uD83D\uDCCB \u0995\u09aa\u09bf \u0995\u09b0\u09c1\u09a8'; // 📋 কপি করুন
      btn.setAttribute('aria-label', '\u0995\u09cb\u09a1 \u0995\u09aa\u09bf \u0995\u09b0\u09c1\u09a8'); // কোড কপি করুন
      btn.style.cssText = 'position:absolute;top:8px;right:8px;z-index:2;';

      pre.style.position = 'relative';
      pre.appendChild(btn);

      btn.addEventListener('click', function () {
        var code = pre.querySelector('code');
        var text = code ? code.innerText : pre.innerText;
        text = text.replace('\uD83D\uDCCB \u0995\u09aa\u09bf \u0995\u09b0\u09c1\u09a8', '').trim();
        copyTextToClipboard(text, '\u0995\u09cb\u09a1 \u0995\u09cd\u09b2\u09bf\u09aa\u09ac\u09cb\u09b0\u09cd\u09a1\u09c7 \u0995\u09aa\u09bf \u09b9\u09df\u09c7\u099b\u09c7!'); // কোড ক্লিপবোর্ডে কপি হয়েছে!
      });
    });

    // 2. Target question blocks with class .ht-copyable-item
    var copyables = document.querySelectorAll('.ht-copyable-item');
    copyables.forEach(function (el) {
      if (el.querySelector('.ht-copy-btn')) return;

      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'ht-copy-btn';
      btn.innerHTML = '\uD83D\uDCCB \u0995\u09aa\u09bf'; // 📋 কপি
      btn.setAttribute('aria-label', '\u09aa\u09cd\u09b0\u09b6\u09cd\u09a8 \u0995\u09aa\u09bf \u0995\u09b0\u09c1\u09a8'); // প্রশ্ন কপি করুন

      el.appendChild(btn);

      btn.addEventListener('click', function () {
        var text = el.innerText.replace('\uD83D\uDCCB \u0995\u09aa\u09bf', '').trim();
        copyTextToClipboard(text, '\u09aa\u09cd\u09b0\u09b6\u09cd\u09a8 \u0995\u09cd\u09b2\u09bf\u09aa\u09ac\u09cb\u09b0\u09cd\u09a1\u09c7 \u0995\u09aa\u09bf \u09b9\u09df\u09c7\u099b\u09c7!'); // প্রশ্ন ক্লিপবোর্ডে কপি হয়েছে!
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setupCopyButtons);
  } else {
    setupCopyButtons();
  }
})();
