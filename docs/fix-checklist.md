# HelpTrickBD — অডিটের ২০টি সমস্যার ঠিক করার তালিকা

- অডিট: ২০২৬-১১-০৯ (শুধু পাবলিক দিক থেকে পড়া হয়েছে, লগইন করা হয়নি)
- সাইট: https://www.helptrickbd.com (WordPress; Blogger থেকে মাইগ্রেট করা)
- রিপো: omarfarukitbd-spec/helptrickbdseo
- প্রস্তুত ফাইল: এই ফোল্ডারে `redirects-404-map.txt` (৩ নম্বর) আর `llms.txt` (১১ নম্বর) তৈরি আছে।
- খেয়াল: Editor রোলে পোস্ট/পাতার লেখা বদলানো যায়, কিন্তু 301 রিডাইরেক্ট, ক্যাটাগরি এক করা, থিম/CSS বদল, robots.txt — এগুলোতে Administrator লাগবে।

| # | সমস্যা | কোথায় | কার দায়িত্ব | অবস্থা | নোট |
|---|--------|--------|--------------|--------|-----|
| 1 | ভাঙা বাংলা অক্ষর (mojibake) — "���" একাধিক পোস্টে | অডিট পোস্ট, নামতা পোস্ট, অ্যাডমিশন পোস্ট, CGPA ক্যালকুলেটর; যেমন https://www.helptrickbd.com/honours-3rd-year-audit-and-assurance-suggestion/ | সাইট (wp-admin) | pending | সব পোস্টে "���" খুঁজে সার্চ-রিপ্লেসে ঠিক করতে হবে; নতুন পোস্টে এনকোডিং যাচাই করতে হবে। |
| 2 | ভাঙা ৪০৪ লিংক — "অনার্স ৩য় বর্ষ উন্নত হিসাববিজ্ঞান ১ সাজেশন 2026" | https://www.helptrickbd.com/honours-3rd-year-audit-and-assurance-suggestion/ পোস্ট থেকে http://www.helptrickbd.com/honours-3rd-year-advanced-accounting-1-suggestion/ (2026-11-09 যাচাই: HTTP 404) | সাইট (wp-admin) | pending | পোস্টটি বানাতে হবে, অথবা লিংকটি সরাতে হবে। হোমপেজে রিডাইরেক্ট নয়। |
| 3 | পুরনো /p/*.html ঠিকানা ডুপ্লিকেট — 301 রিডাইরেক্ট লাগবে | https://www.helptrickbd.com/p/about-us.html, /p/contact-us.html, /p/terms-conditions.html | রিপো + সাইট | pending | ম্যাপ তৈরি: এই ফোল্ডারের `redirects-404-map.txt`। WordPress-এ Redirection প্লাগইন বা হোস্টের 301 দিয়ে বসাতে হবে (Blogger-এ নয়)। Administrator লাগবে। |
| 4 | http:// ছবি ও লিংক — https করতে হবে | লেখকের ছবি http://www.helptrickbd.com/wp-content/uploads/2026/11/faruk_sir.webp; About ও Privacy Policy পাতায় http লিংক | সাইট (wp-admin) | pending | ছবি/লিংকের ঠিকানা https দিয়ে বদলাতে হবে। |
| 5 | একই বিষয়ের দুটো SSC ক্যাটাগরি | https://www.helptrickbd.com/category/ssc-dakhil/ (১০ পোস্ট) বনাম https://www.helptrickbd.com/category/ssc-%E0%A6%93-%E0%A6%A6%E0%A6%BE%E0%A6%96%E0%A6%BF%E0%A6%B2/ (২ পোস্ট) | সাইট (wp-admin) | pending | একটিতে রিডাইরেক্ট করে পোস্টগুলো এক জায়গায় আনতে হবে। Administrator লাগবে। |
| 6 | FAQ অংশে ডুপ্লিকেশন — আগের কনটেন্ট ভাঙা Q/A আকারে আবার এসেছে | অডিট পোস্ট ও নামতা পোস্টের শেষের FAQ অংশ | সাইট (wp-admin) | pending | ভাঙা FAQ অংশটি সরাতে বা ঠিকমতো সাজাতে হবে। |
| 7 | নামতা পোস্টে ৬ নম্বর অংশ নেই, প্র্যাকটিস শিট নেই, ভূমিকা দুবার | https://www.helptrickbd.com/namta-1-to-20/ | সাইট (wp-admin) | pending | ৬ নম্বর অংশ ও প্র্যাকটিস শিট যোগ করতে হবে, অথবা সূচিপত্র ঠিক করতে হবে; ডুপ্লিকেট ভূমিকা সরাতে হবে। |
| 8 | কাটা স্লাগ (URL মাঝপথে কাটা) | …/secularism-vs-islamic-values-in/, …/federal-government-features-and/, …/ssc-english-2nd-paper-right-form-of/, …/politics-indeveloping-countries-controls-the-economy/, …/bcs-preliminary-marks-distribution_01436475916/ | সাইট (wp-admin) | pending | নতুন পোস্টে সতর্ক থাকতে হবে; পুরনো স্লাগ বদলালে 301 রিডাইরেক্ট দিতে হবে। |
| 9 | টাইটেলে "Best Complete Guide 2026" পুনরাবৃত্তি — একঘেয়ে ও লম্বা | প্রায় সব পোস্টের টাইটেল | সাইট (wp-admin) | pending | টাইটেল ছোট ও আলাদা করতে হবে। |
| 10 | ছক মোবাইল-রেসপন্সিভ নয় — আড়াআড়ি স্ক্রল করতে হয় | প্রায় সব পোস্টের ছক | সাইট (থিম/CSS) | pending | থিম/CSS বদলাতে হবে। Administrator লাগবে। |
| 11 | llms.txt-এ ভুল ক্যাটাগরি লিংক + কাঁচা `&hellip;` | https://www.helptrickbd.com/llms.txt | রিপো + সাইট | pending | ঠিক করা ফাইল তৈরি: এই ফোল্ডারের `llms.txt`। ক্যাটাগরি education-guide / ict-technology / islamic-article দিয়ে ঠিক করা হয়েছে; Online Income-এর কোনো ক্যাটাগরি নেই বলে ওই লাইনটি সরানো হয়েছে; `&hellip;` → `…` করা হয়েছে। সাইটের মূল llms.txt-এ বসাতে হবে। |
| 12 | তারিখের ফরম্যাট অসঙ্গত | হোমপেজ ও পোস্টের কার্ড (যেমন "October 29, 2026" আবার "29 October, 2026") | সাইট (থিম/সেটিংস) | pending | এক ফরম্যাট করতে হবে (বাংলা সাইটে বাংলা তারিখ ভালো)। |
| 13 | অতিরিক্ত লম্বা পোস্ট ভাগ করা দরকার | অডিট পোস্ট (৫,৬৮২ লাইন; কার্ডে "২৬২ মিনিট পড়া") | সাইট (wp-admin) | pending | অধ্যায়ভিত্তিক আলাদা পোস্ট বা পেজিনেশন দিতে হবে। |
| 14 | সূত্রহীন পরিসংখ্যান + পুরনো তথ্য | অ্যাডমিশন পোস্টে "প্রায় ৯২% শিক্ষার্থী…", "৬০–৭০% প্রশ্ন রিপিট হয়"; সাইটম্যাপে "আলিম পরীক্ষার রুটিন ২০২৫"; HSC রেজাল্ট ২০২৬ সংক্রান্ত লেখা | সাইট (wp-admin) | pending | দাবিগুলোতে সূত্র যোগ করতে হবে অথবা সরাতে হবে; পুরনো তথ্য হালনাগাদ করতে হবে। |
| 15 | About পাতা শুধু ইংরেজিতে; ছবি, টিম, সোশ্যাল লিংক নেই | https://www.helptrickbd.com/about-us/ | সাইট (wp-admin) | pending | বাংলায় লিখতে হবে; ছবি, টিম ও সোশ্যাল লিংক যোগ করতে হবে। রিপোতে ইংরেজি টেমপ্লেট আছে: templates/legal_pages/about-us.html। |
| 16 | পোস্টের শেষে সম্পর্কিত পোস্ট, ট্যাগ, শেয়ার বোতাম নেই | ফ্ল্যাগশিপ পোস্টগুলো | সাইট (থিম/প্লাগইন) | pending | থিম বা প্লাগইন দিয়ে যোগ করতে হবে। Administrator লাগবে। |
| 17 | মেটা ডেসক্রিপশন যাচাই করা হয়নি | সব পোস্ট | সাইট (wp-admin) | pending | প্রতিটি পোস্টে আলাদা মেটা ডেসক্রিপশন (১৫৫ অক্ষরের মধ্যে) আছে কি না লাইভ পরীক্ষায় দেখতে হবে — টেক্সট ফেচ থেকে দেখা যায়নি। |
| 18 | CGPA ক্যালকুলেটর প্রথম খুললেই 0.00 CGPA-সহ নমুনা রিপোর্ট দেখায় | সাইটের CGPA ক্যালকুলেটর পাতা | সাইট (wp-admin) | pending | খালি অবস্থায় শুধু ইনপুট ফরম দেখাতে হবে। ("দেশের প্রথম… ক্যালকুলেটর" দাবিটিও যাচাইহীন।) |
| 19 | Privacy Policy জেনেরিক টেমপ্লেট, পুরনো পরিভাষা, তারিখে অসঙ্গতি | https://www.helptrickbd.com/privacy-policy/ | সাইট + রিপো | pending | "Google DoubleClick DART Cookie" তোলা, বাংলা সংস্করণ যোগ করা, তারিখ ঠিক করা। রিপোতে টেমপ্লেট আছে: templates/legal_pages/privacy-policy.html। |
| 20 | হোমপেজে একই পোস্টের পুনরাবৃত্তি | হোমপেজ (ফিচার, National University, Education Guide অংশে একই ৪টি অডিট পোস্ট) | সাইট (থিম/সেটিংস) | pending | ফিচার, ক্যাটাগরি ও সাম্প্রতিক অংশে আলাদা পোস্ট দেখাতে হবে। |
