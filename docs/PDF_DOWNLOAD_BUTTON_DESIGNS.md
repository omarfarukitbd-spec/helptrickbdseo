# 📥 HelpTrickBD PDF Download Section & Button Architecture

এই ডকুমেন্টটি HelpTrickBD-এর সকল পোস্টের জন্য অনুমোদিত অফিশিয়াল PDF ডাউনলোড সেকশন এবং বাটন ডিজাইনের প্রামাণ্য স্পেসিফিকেশন ও ব্যবহারের নির্দেশিকা।

---

## 🏛️ মূল নীতিমালা (Core Governance)
১. **সাদামাটা বা আনস্টাইল্ড লিংক নিষিদ্ধ:** কোনো পোস্টে শুধুমাত্র সাধারণ টেক্সট লিংক বা একক সাধারণ বাটন দিয়ে পিডিএফ ছেড়ে দেওয়া যাবে না।
২. **হেডিং ও ব্যাখ্যামূলক অনুচ্ছেদ বাধ্যতামূলক:** ডাউনলোড সেকশনের শুরুতে অবশ্যই একটি সুস্পষ্ট `<h2>` হেডিং (পিডিএফ আইকনসহ) এবং একটি ব্যাখ্যামূলক প্যারাগ্রাফ থাকবে যা পরিষ্কার করবে এটি কিসের পিডিএফ, এতে কয়টি প্রশ্ন/অধ্যায় রয়েছে, প্রিন্ট কোয়ালিটি (A4 রেডি) এবং পরীক্ষার জন্য এর কার্যকারিতা কী।
৩. **প্রি-পাবলিশ ক্ল্যারিফিকেশন গেট (Mandatory Stop-Gate):** কোনো পিডিএফ শেয়ারিং পোস্ট (সাজেশন, প্রশ্নব্যাংক, রুটিন, নোটিশ বা সিলেবাস) প্রকাশের পূর্বে এজেন্টকে অবশ্যই ব্যবহারকারীকে জিজ্ঞাসা করতে হবে:
   - *এই পোস্টে কি অফিশিয়াল PDF ডাউনলোড সেকশন যুক্ত করা হবে? (হ্যাঁ / না)*
   - *যদি হ্যাঁ হয়, তবে কোন ডিজাইনটি ব্যবহার করা হবে?*
     - **মোড ১:** সাথে সাথে সরাসরি ডাউনলোড বাটন (Direct Mode)
     - **মোড ২:** ৩০ সেকেন্ড কাউন্টডাউন টাইমার বাটন (Timer Mode)
     - **মোড ৩:** উভয় বাটন একসাথে (Dual Mode)
   - *ফাইলটির অফিশিয়াল ডাউনলোড URL কোনটি হবে?*

---

## 🎨 ডিজাইনের ৩টি মোড ও আর্কিটেকচার

### মোড ১: সাথে সাথে সরাসরি ডাউনলোড (Instant Direct Download)
- **উদ্দেশ্য:** যেসব ব্যবহারকারী কোনো প্রকার অপেক্ষা ছাড়া ১-ক্লিকে তাৎক্ষণিক পিডিএফ পেতে চান।
- **বাটন লুক:** ভাইব্র্যান্ট এমারেল্ড-গ্রিন গ্রেডিয়েন্ট (`linear-gradient(135deg, #059669 0%, #047857 100%)`)।
- **আইকন:** ক্লাউড/ডাউনলোড অ্যারো SVG আইকন।
- **টেক্সট:** `⚡ সরাসরি PDF ডাউনলোড (Instant Download)`
- **অ্যাট্রিবিউট:** `target="_blank" rel="noopener noreferrer" download`

```html
<a href="[PDF_URL]" target="_blank" rel="noopener noreferrer" download class="htbd-btn-direct" style="display: inline-flex; align-items: center; gap: 10px; background: linear-gradient(135deg, #059669 0%, #047857 100%); color: #ffffff !important; padding: 14px 28px; border-radius: 10px; font-weight: 700; font-size: 15.5px; text-decoration: none !important; box-shadow: 0 4px 14px rgba(5, 150, 105, 0.3); transition: transform 0.15s ease, box-shadow 0.15s ease; border: none; cursor: pointer; user-select: none;">
  <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
  <span>⚡ সরাসরি PDF ডাউনলোড (Instant Download)</span>
</a>
```

---

### মোড ২: ৩০ সেকেন্ড কাউন্টডাউন টাইমার (30s Countdown Timer)
- **উদ্দেশ্য:** সাইটে ব্যবহারকারীর অবস্থানের সময় (Dwell Time) বৃদ্ধি, গুগল সার্চ র‍্যাঙ্কিং মজবুতকরণ এবং গুগল অ্যাডসেন্স ভিউয়াবিলিটি বহুগুণ বাড়ানো।
- **বাটন লুক:** ভাইব্র্যান্ট রয়্যাল-ব্লু গ্রেডিয়েন্ট (`linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%)`)।
- **আইকন:** টাইমার/ঘড়ি SVG আইকন।
- **টেক্সট:** `⏳ ৩০ সেকেন্ডে হাই-স্পিড ডাউনলোড (Countdown Timer)`
- **ইন্টারঅ্যাক্টিভ বিহেভিয়ার:**
  - বাটনে ক্লিক করামাত্র বাটনটি হাইড হয়ে কাউন্টডাউন বক্স সক্রিয় হয়।
  - লাইভ ৩০ সেকেন্ড কাউন্টার ও স্মুথ ব্লু প্রোগ্রেস বার (১০০% থেকে ০%) অ্যানিমেট হয়।
  - ৩০ সেকেন্ড শেষ হওয়ামাত্র স্বয়ংক্রিয়ভাবে নতুন ট্যাবে পিডিএফ ওপেন হয় এবং বক্সে সবুজ সাকসেস মেসেজ ও স্থায়ী ডাউনলোড বাটন (`📥 এখনই PDF ডাউনলোড করুন`) প্রদর্শিত হয়।

```html
<div id="htbd-timer-wrap-[UNIQUE_ID]" style="display: inline-block;">
  <button id="htbd-timer-btn-[UNIQUE_ID]" onclick="startPdfCountdown('[UNIQUE_ID]', '[PDF_URL]')" class="htbd-btn-timer" style="display: inline-flex; align-items: center; gap: 10px; background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%); color: #ffffff !important; padding: 14px 28px; border-radius: 10px; font-weight: 700; font-size: 15.5px; cursor: pointer; border: none; box-shadow: 0 4px 14px rgba(37, 99, 235, 0.3); user-select: none; transition: transform 0.15s ease, box-shadow 0.15s ease;">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
    <span>⏳ ৩০ সেকেন্ডে হাই-স্পিড ডাউনলোড (Countdown Timer)</span>
  </button>
  <div id="htbd-timer-box-[UNIQUE_ID]" style="display: none; background: #eff6ff; border: 1.5px solid #bfdbfe; border-radius: 10px; padding: 16px 24px; font-size: 15.5px; font-weight: 700; color: #1e40af; text-align: center;">
    <div id="htbd-timer-text-[UNIQUE_ID]">হাই-স্পিড ক্লাউড লিংক তৈরি হচ্ছে... অনুগ্রহ করে <span id="htbd-countdown-[UNIQUE_ID]" style="color: #dc2626; font-size: 20px; font-weight: 800;">30</span> সেকেন্ড অপেক্ষা করুন</div>
    <div style="width: 100%; height: 8px; background: #dbeafe; border-radius: 4px; margin-top: 10px; overflow: hidden;">
      <div id="htbd-progress-[UNIQUE_ID]" style="width: 100%; height: 100%; background: #2563eb; transition: width 1s linear;"></div>
    </div>
  </div>
</div>
```

---

### মোড ৩: ডুয়াল মোড (Dual Mode — উভয় বাটন পাশাপাশি)
- **উদ্দেশ্য:** ব্যবহারকারীকে পূর্ণ স্বাধীনতা প্রদান (সরাসরি ডাউনলোড অথবা হাই-স্পিড ক্লাউড ডাউনলোড)।
- বাটন দুটি পাশাপাশি একটি রেসপনসিভ ফ্লেক্সবক্সে সাজানো থাকে (`display: flex; flex-wrap: wrap; gap: 16px; align-items: center;`)।

---

## 🛠️ পাইথন মডিউলের মাধ্যমে ব্যবহার করার নিয়ম

প্রজেক্টের যেকোনো বিল্ডার বা জেনারেটর স্ক্রিপ্ট থেকে সহজেই এটি ব্যবহার করা যায়:

```python
from tools.post_builders.pdf_download_component import render_pdf_download_section

pdf_section_html = render_pdf_download_section(
    pdf_url="https://www.helptrickbd.com/wp-content/uploads/2026/11/sample.pdf",
    heading_title="উৎপাদন ব্যয় হিসাববিজ্ঞান প্রশ্নব্যাংক ২০১৯-২০২৪ (মাস্টার সল্যুশন)",
    file_spec="ফাইল ফরম্যাট: প্রামাণ্য A4 প্রিন্ট-রেডি ই-বুক • ফাইল সাইজ: ৩.১৫ MB • সংস্করণ: ২০২৬ স্পেশাল",
    description_text="এখানে পোস্ট সম্পর্কিত কাস্টম ব্যাখ্যামূলক অনুচ্ছেদ...",
    mode="timer",  # 'direct', 'timer', অথবা 'dual'
    unique_id="cost2026"
)
```

---

## 🛡️ রুলস রেফারেন্স
- **`.agents/rules/00_AGENT_CONSTITUTION.md`**: Stop-Gate Matrix Rule.
- **`.agents/rules/01_CONTENT_STANDARDS.md`**: Section 17.
- **`AGENTS.md`**: Rule 32.
