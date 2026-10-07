# 04_LABEL_TAXONOMY_GOVERNANCE.md — Category & Taxonomy Architecture
### Helptrickbd.com WordPress Hierarchical Categories & AdSense Balance Governance

> [!IMPORTANT]
> **AdSense Navigation Quality & Silo Governance**: Empty or 1-post categories trigger Google AdSense "Under Construction" or "Low Value Content" flags. In WordPress, we enforce strict hierarchical parent-child categories and rich targeted tags.

---

## 1. Category Permission Gate (অনুমোদন ছাড়া ক্যাটাগরি তৈরি নিষিদ্ধ)
1. **Strict User Consent**:
   - The agent MUST NOT create a new parent category without user approval.
2. **Pre-Publish Category Inquiry**:
   - Before publishing or updating any article, assign at least 1 established primary category and 1 sub-category if applicable.

---

## 2. Core WordPress Taxonomy & Approved Clusters
Helptrickbd.com maintains established thematic pillars. Every article must belong to one of these core clusters:

| Parent Category | Sub-Categories (Slug) | কন্টেন্ট টাইপ | টার্গেট অডিয়েন্স |
|-----------------|----------------------|--------------|-------------------|
| Education (`education-guide`) | `ssc-dakhil`, `national-university`, `degree-pass` | বোর্ড রুলস, সার্টিফিকেট সংশোধন, সাজেশন | স্কুল, কলেজ ও বিশ্ববিদ্যালয় শিক্ষার্থী |
| Technology (`ict-tech`) | `computer-basics`, `cyber-security`, `programming` | কম্পিউটার, ক্লাউড, সাইবার নিরাপত্তা, ট্রিকস | প্রযুক্তিপ্রেমী, শিক্ষার্থী ও শিক্ষক |
| Political Science (`political-science`) | `honours-notes`, `masters-notes`, `theories` | অনার্স/মাস্টার্স হ্যান্ডনোট, থিওরি, রাষ্ট্রচিন্তা | জাতীয় বিশ্ববিদ্যালয় শিক্ষার্থী |
| Job Preparation (`job-prep`) | `bcs-prep`, `primary-viva`, `bank-job` | বিসিএস, প্রাইমারি শিক্ষক ভাইভা, ব্যাংক জব | চাকরি প্রার্থী ও সাধারণ পরীক্ষার্থী |
| Islamic (`islamic-article`) | `qasida-lyrics`, `history-translation` | ক্বাসিদা, অনুবাদ, ইসলামিক ইতিহাস ও তাৎপর্য | ধর্মপ্রাণ পাঠক ও গবেষক |

---

## 3. Category Balance Rules for AdSense Approval
1. **The 4–5 Post Minimum Rule**:
   - Every active category MUST contain at least **4 to 5 published, in-depth posts**.
   - Categories with only 1 or 2 posts must not be placed in the primary header navigation menu.
2. **Tags vs Categories Separation**:
   - Categories represent broad academic silos (`Education Guide`, `Political Science`).
   - Tags represent granular search topics (e.g., `অনার্স ২য় বর্ষ সাজেশন`, `সৃজনশীল প্রশ্নব্যাংক`).
3. **Crawl Budget Optimization**:
   - Assign maximum 1 Primary Category and 1 Sub-category per post.
   - Assign 3 to 6 targeted bilingual tags per post.
