# 🚀 HelpTrickBD - Google Instant Indexing API Setup Guide

এই গাইডের মাধ্যমে আপনি গুগলের অফিশিয়াল **Google Indexing API** সেটআপ করতে পারবেন, যার ফলে আপনার ব্লগের যেকোনো নতুন বা আপডেট করা পোস্ট **২৪ থেকে ৪৮ ঘণ্টার মধ্যে** গুগলবট ক্রল ও ইনডেক্স করতে আসবে।

---

## 📌 ধাপ ১: Google Cloud Project তৈরি ও Indexing API Enable করা

1. [Google Cloud Console](https://console.cloud.google.com/)-এ যান (আপনার মূল Gmail দিয়ে লগইন করুন)।
2. উপরে **Select a project**-এ ক্লিক করে **New Project** তৈরি করুন (যেমন নাম দিন: `helptrickbd-indexing`)।
3. প্রজেক্ট সিলেক্ট করার পর বাম পাশের মেনু থেকে **APIs & Services > Library**-তে যান।
4. সার্চ বক্সে লিখুন: `Indexing API`।
5. **Web Search Indexing API** সিলেক্ট করে **Enable** বাটনে ক্লিক করুন।

---

## 📌 ধাপ ২: Service Account তৈরি ও JSON কী ডাউনলোড

1. বাম পাশের মেনু থেকে **IAM & Admin > Service Accounts**-এ যান।
2. উপরে **+ CREATE SERVICE ACCOUNT** বাটনে ক্লিক করুন।
3. **Service account name** দিন: `helptrickbd-bot` এবং **Create and Continue**-এ ক্লিক করুন।
4. **Role** হিসেবে সিলেক্ট করুন: **Owner** (বা `Project > Owner`) এবং **Done** দিন।
5. এখন তৈরি হওয়া সার্ভিস অ্যাকাউন্টের ওপর ক্লিক করুন এবং **Keys** ট্যাবে যান।
6. **Add Key > Create new key** সিলেক্ট করুন, ফরম্যাট **JSON** নির্বাচন করে **Create** দিন।
7. একটি `.json` ফাইল ডাউনলোড হবে। ফাইলটির নাম পরিবর্তন করে রাখুন:
   ```text
   service_account.json
   ```
8. এই `service_account.json` ফাইলটি আপনার এই প্রজেক্টের `tools/indexer/` ফোল্ডারে রেখে দিন।
   *(নোট: এই ফাইলটি কখনো কাউকে দেবেন না বা গিটহাবে পুশ করবেন না; `.gitignore` ফাইলে এটি সুরক্ষিত রাখা হয়েছে।)*

---

## 📌 ধাপ ৩: Google Search Console-এ সার্ভিস অ্যাকাউন্ট যুক্ত করা (অত্যন্ত গুরুত্বপূর্ণ)

1. আপনার `service_account.json` ফাইলটি ওপেন করলে ভিতরে `client_email` দেখতে পাবেন (যেমন: `helptrickbd-bot@helptrickbd-indexing.iam.gserviceaccount.com`)। এই ইমেইলটি কপি করুন।
2. [Google Search Console](https://search.google.com/search-console)-এ যান।
3. আপনার ডোমেইন সিলেক্ট করুন (`https://www.helptrickbd.com/`)।
4. বাম পাশের মেনু থেকে **Settings > Users and permissions**-এ যান।
5. **Add User** বাটনে ক্লিক করে কপি করা সার্ভিস অ্যাকাউন্ট ইমেইলটি পেস্ট করুন।
6. **Permission** অবশ্যই **Owner** সিলেক্ট করে **Add** করুন।

---

## 📌 ধাপ ৪: ডিপেনডেন্সি ইনস্টল ও স্ক্রিপ্ট চালানো

টার্মিনালে এই কমান্ডগুলো রান করুন:

```powershell
# tools/indexer ফোল্ডারে থাকা ডিপেনডেন্সি ইনস্টল করুন
pip install -r tools/indexer/requirements.txt
```

### ব্যবহারের কমান্ডসমূহ:

#### ১. একটি নির্দিষ্ট পোস্টের ইনডেক্সিং রিকোয়েস্ট পাঠানো:
```powershell
python tools/indexer/index_now.py --url https://www.helptrickbd.com/2026/01/sarbobhoumotto-ki-songga-boishisto-o-prokarved.html
```

#### ২. সব পোস্ট একসাথে ব্যাচ আকারে সাবমিট করা (`urls.txt` থেকে):
```powershell
python tools/indexer/index_now.py --file tools/indexer/urls.txt
```

#### ৩. সরাসরি লাইভ সাইটম্যাপ থেকে সব পোস্ট অটোমেটিক ইনডেক্স করা:
```powershell
python tools/indexer/index_now.py --sitemap https://www.helptrickbd.com/sitemap.xml
```

#### ৪. ডিলিট করা কোনো পোস্ট গুগল ইনডেক্স থেকে দ্রুত রিমুভ করার রিকোয়েস্ট:
```powershell
python tools/indexer/index_now.py --url https://www.helptrickbd.com/old-deleted-post.html --type URL_DELETED
```

---

## 📊 হিস্ট্রি ও রেজাল্ট চেক:
প্রতিবার স্ক্রিপ্ট রান করলে তা `indexing_history.log` ফাইলে সেভ হয়ে থাকবে যাতে আপনি বুঝতে পারেন কোন কোন পোস্ট গুগলে সফলভাবে সাবমিট হয়েছে।
