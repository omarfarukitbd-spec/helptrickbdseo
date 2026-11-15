/**
 * 1-Click Code & Question Copy Engine for HelpTrickBD EduPortal
 * Modern Clipboard API with elegant toast notification
 *
 * @package HelpTrickBD_EduPortal
 */

(function () {
  'use strict';

  var toast = document.getElementById('ht-copy-toast');
  var toastMsg = document.getElementById('ht-copy-toast-msg');
  var toastTimeout = null;

  function showToast(msg) {
    if (!toast) return;
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
  }

  function setupCopyButtons() {
    // 1. Target code blocks (pre > code)
    var codeBlocks = document.querySelectorAll('.ht-entry-content pre');
    codeBlocks.forEach(function (pre) {
      if (pre.querySelector('.ht-copy-btn')) return;

      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'ht-copy-btn';
      btn.innerHTML = '📋 কপি করুন';
      btn.setAttribute('aria-label', 'কোড কপি করুন');
      btn.style.cssText = 'position:absolute;top:8px;right:8px;z-index:2;';

      pre.style.position = 'relative';
      pre.appendChild(btn);

      btn.addEventListener('click', function () {
        var code = pre.querySelector('code');
        var text = code ? code.innerText : pre.innerText;
        // Strip the button label if it got caught
        text = text.replace('📋 কপি করুন', '').trim();

        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(text).then(function () {
            showToast('কোড ক্লিপবোর্ডে কপি হয়েছে!');
          });
        }
      });
    });

    // 2. Target question blocks with class .ht-copyable-item
    var copyables = document.querySelectorAll('.ht-copyable-item');
    copyables.forEach(function (el) {
      if (el.querySelector('.ht-copy-btn')) return;

      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'ht-copy-btn';
      btn.innerHTML = '📋 কপি';
      btn.setAttribute('aria-label', 'প্রশ্ন কপি করুন');

      el.appendChild(btn);

      btn.addEventListener('click', function () {
        var text = el.innerText.replace('📋 কপি', '').trim();
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(text).then(function () {
            showToast('প্রশ্ন ক্লিপবোর্ডে কপি হয়েছে!');
          });
        }
      });
    });
  }

  document.addEventListener('DOMContentLoaded', setupCopyButtons);
})();
