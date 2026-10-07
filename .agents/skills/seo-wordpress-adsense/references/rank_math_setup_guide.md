# র্যাংক ম্যাথ এসইও ও ইনস্ট্যান্ট ইনডেক্সিং সেটআপ গাইড (Rank Math Setup Guide)

এই রেফারেন্স গাইডে হেল্পট্রিকবিডি ওয়ার্ডপ্রেস সাইটের জন্য র্যাংক ম্যাথ প্লাগিন কনফিগারেশনের সুনির্দিষ্ট সেটিংস দেওয়া হলো:

---

## ১. জেনারেল সেটিংস (General Settings)
1. **Links:**
   * Strip Category Base: `OFF` (ক্যাটাগরি ইউআরএল স্বাভাবিক রাখা)।
   * Nofollow External Links: `ON` (বাহ্যিক লিংকের জন্য সেফটি)।
   * Open External Links in New Tab/Window: `ON`.
2. **Breadcrumbs:**
   * Enable Breadcrumbs: `ON`.
   * Separator: `/` বা `>` (থিম নেটিভ ব্রেডক্রাম্ব সমর্থন করে)।
   * Show Category in Breadcrumb: `ON`.
3. **Webmaster Tools:**
   * Google Search Console ভেরিফিকেশন কোড যুক্ত করা।

---

## ২. টাইটেল ও মেটা (Titles & Meta)
1. **Global Meta:**
   * Robots Meta: `Index`.
   * Advanced Robots Meta: Max Snippet: `-1`, Max Video Preview: `-1`, Max Image Preview: `Large`.
2. **Posts Meta:**
   * Single Post Title: `%title% | %sitename%`.
   * Single Post Description: `%excerpt%`.
   * Schema Type: `Article` (Article Type: `Blog Posting`).
3. **Categories Meta:**
   * Category Archive Title: `%category% সংক্রান্ত সকল গাইড ও সাজেশন | %sitename%`.
   * Category Archive Description: `%category_description%`.
   * Category Robots Meta: `Index`.
4. **Tags Meta:**
   * Tag Archives: `Noindex` (গুগলে ক্রল বাজেট বাঁচাতে এবং পাতলা আর্কাইভ রোধ করতে ট্যাগ নো-ইনডেক্স রাখা উত্তম)।

---

## ৩. সাইটম্যাপ সেটিংস (Sitemap Settings)
1. **General:**
   * Links per Sitemap: `200`.
   * Images in Sitemap: `Include Featured Images`.
2. **Post Types:**
   * Posts: `Included`.
   * Pages: `Included`.
3. **Taxonomies:**
   * Categories: `Included`.
   * Tags: `Excluded`.

---

## ৪. ইনস্ট্যান্ট ইনডেক্সিং এপিআই সেটিংস (Instant Indexing Settings)
1. **Console API:**
   * Google Cloud Console-এর `service_account.json` ফাইলের কন্টেন্ট র্যাংক ম্যাথের Instant Indexing সেকশনে পেস্ট করুন।
2. **Search Console Permission:**
   * সার্ভিস একাউন্টের ইমেইল অ্যাড্রেসটি Google Search Console-এর `sc-domain:helptrickbd.com` প্রপার্টিতে **Owner** বা **Full** পারমিশনে যুক্ত থাকতে হবে।
3. **Action Target:**
   * Posts ও Pages-এ স্বয়ংক্রিয় পাবলিশ বা আপডেটে `URL_UPDATED` অ্যাকশন কার্যকর হবে।
