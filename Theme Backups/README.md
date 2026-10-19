# 🛡️ Theme Backups (থিম প্রি-এডিট ব্যাকআপ ভল্ট)

এই ফোল্ডারে হেল্পট্রিকবিডি প্রো ওয়ার্ডপ্রেস থিমের **প্রতিটি কাজের শুরুর পূর্বে** স্বয়ংক্রিয়ভাবে একটি সম্পূর্ণ প্রি-এডিট ব্যাকআপ সংরক্ষিত হয়।

---

## 📌 ব্যাকআপের উদ্দেশ্য ও কাঠামো:
থিমের কোনো পিএইচপি (PHP), সিএসএস (CSS), জাভাস্ক্রিপ্ট (JS) বা কনফিগারেশন ফাইল সম্পাদনা করার পূর্বে এই ফোল্ডারে টাইমস্ট্যাম্প অনুযায়ী ফোল্ডার তৈরি হয়:

```
Theme Backups/
├── wp_theme_YYYYMMDD_HHMMSS_v<version>_<reason>/
│   ├── helptrickbd-theme/                         # সম্পূর্ণ থিমের আনপ্যাকড সোর্স কোড
│   ├── helptrickbd-theme-v<version>-<time>.zip    # ইনস্ট্যান্ট সিপ্যানেল/ওয়ার্ডপ্রেস রেডি জিপ
│   └── metadata.json                              # ব্যাকআপের তারিখ, কারণ, ভার্সন ও ফাইল তথ্য
└── latest/                                        # সর্বশেষ ব্যাকআপ সংস্করণের সরাসরি স্ন্যাপশট
```

---

## ⚡ ১-ক্লিক রিস্টোর বা রোলব্যাক কমান্ড (Instant 1-Click Rollback):
যদি কোনো কাজের পর লাইভ সাইট বা থিমে কোনো ত্রুটি দেখা দেয়, তবে মুহূর্তেই পূর্বাবস্থায় ফিরিয়ে আনতে টার্মিনালে রান করুন:

```bash
# সর্বশেষ সচল ব্যাকআপে ফিরে যেতে:
python tools/backup_manager/theme_backup_manager.py restore

# নির্দিষ্ট কোনো ব্যাকআপে ফিরে যেতে:
python tools/backup_manager/theme_backup_manager.py restore --timestamp YYYYMMDD_HHMMSS
```

---

## 🛠️ নতুন ব্যাকআপ তৈরির কমান্ড (Manual / Pre-Task Backup):
```bash
python tools/backup_manager/theme_backup_manager.py backup --reason "<আপনার কাজের বিবরণ>"
```
