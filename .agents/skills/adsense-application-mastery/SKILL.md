---
name: adsense-application-mastery
description: Comprehensive Google AdSense application, identity verification, address/PIN setup, and policy compliance blueprint. Use whenever preparing, auditing, or executing an AdSense application for Blogger or custom-domain websites.
---

# Google AdSense Application & Identity Verification Mastery Skill

This skill provides an exhaustive, fail-safe blueprint for preparing, auditing, submitting, and maintaining a website on **Google AdSense**. It covers 100% of all official policies, Digital Identity Verification (KYC), Bangladesh Post Address (PIN) delivery, US Tax (W-8BEN) treaties, Consent Management Platform (CMP / GDPR) mandates, modern impression-based (CPM) monetization architectures, and Invalid Traffic (IVT) defense.

---

## 1. Cardinal Rule: The "One Person, One Account" Policy (এক ব্যক্তি, এক অ্যাকাউন্ট নীতি)

Google enforces a strict **one account per individual/entity** policy worldwide. Violating this is the single most common cause of permanent account rejection ("You already have an AdSense account").

### A. Pre-Application Duplicate Check
Before creating or submitting any AdSense account:
1. **Search All Personal Gmail Accounts:**
   - Search your inbox for emails from `adsense-noreply@google.com`, `google-payments-noreply@google.com`, or subjects containing `AdSense`, `Publisher ID`, `pub-`.
2. **Google Username Recovery:**
   - Use Google Account Recovery (`https://accounts.google.com/signin/usernamerecovery`) using your primary mobile number and full legal name to see all Gmail accounts registered under your identity.
3. **If a Previous Account Exists:**
   - **Scenario A (Accessible):** Log in to the old AdSense account, navigate to **Sites > Add Site**, and submit the new domain there. Never create a second account.
   - **Scenario B (Unwanted Old Account):** Log in to the old AdSense account, go to **Account > Settings > Account information**, and click **Close Account**. Wait at least 3-7 business days for Google's backend to purge the link before applying with a new account.
   - **Scenario C (Lost / Inaccessible Old Account):** If an old account cannot be recovered or closed, the applicant **MUST apply under an immediate family member's legal identity** (Father, Mother, Brother, or Spouse) who is 18+ and has never had an AdSense account.

---

## 2. 100% Identity & Payment Profile Matching (আইডেন্টিটি ও পেমেন্ট প্রোফাইল সামঞ্জস্য)

Every legal, digital, and banking identity data point must match **100% letter-for-letter**. A single typo or variation between documents causes identity verification failure and permanent payout suspension.

### A. The 5-Point Identity Match Checklist
All five entities must have the exact same English spelling:
1. **Google Account (Gmail) Profile Name** (`myaccount.google.com/personal-info`)
2. **Google Payments Profile Name** (`pay.google.com`)
3. **Government-issued Photo ID** (Smart NID Card, Passport, or Driving License)
4. **Bank Account Holder Name** (for SWIFT wire transfer payouts)
5. **US Tax Form W-8BEN Legal Name**

### B. Bangladeshi NID Name Standards
- **Use the English Spelling on Smart NID:**
  - If the Smart NID says `MD. OMAR FARUK`, the Google Account, Payments profile, and Bank account must be `MD. OMAR FARUK` (or `Md Omar Faruk`).
  - Do NOT use abbreviations if the card has the full name, and do NOT expand abbreviations if the card has initials.
  - If the Smart NID contains dots (e.g. `MD.`), standard AdSense forms accept letters and spaces (`Md Omar Faruk`).
- **Date of Birth (DOB):**
  - The applicant MUST be at least 18 years old on the date of application.
  - The DOB set in the Google Account profile MUST match the DOB on the Smart NID/Passport.
- **Account Type:**
  - Select **Individual** (ব্যক্তিগত). Do NOT select "Business" unless you possess a legally registered company with a corporate Bank Account and TIN in the company's name. An Individual account cannot be converted to a Business account later.
- **2-Step Verification (2FA):**
  - The Google Account used for AdSense MUST have 2-Step Verification permanently enabled via Google Authenticator or SMS to comply with Google Payments security standards.

---

## 3. Digital Identity Verification (KYC) Submission Standards (কেওয়াইসি ভেরিফিকেশন নির্দেশিকা)

Once your account reaches the verification threshold, Google prompts you to complete Identity Verification in the AdSense dashboard under **Payments > Verification check**.

### A. The 45-Day Deadline Rule
- From the moment Google requests identity verification, you have exactly **45 days** to successfully submit your documents.
- If you fail to verify within 45 days, ad serving is automatically suspended across your entire site until verification is approved.

### B. Bangladeshi Smart NID Photography Standards
Google's automated computer vision system rejects documents if they do not meet strict visual criteria:
1. **Original Plastic Smart Card Only:**
   - Never upload black-and-white photocopies, laminated paper slips, or digital screenshots from voter databases.
   - Use the official plastic Smart NID card or a valid Bangladesh Passport.
2. **Two-Sided Requirement:**
   - Bangladeshi Smart NID has information on both sides. You MUST capture and upload high-resolution photos of **both the front and the back**.
3. **Capture Conditions:**
   - Place the card on a dark, non-reflective, flat surface (such as a clean wooden table or dark paper).
   - Ensure all **4 corners of the card are clearly visible** inside the camera frame. Do not crop the edges.
   - Use soft, ambient daytime lighting. Avoid camera flash that creates white glare over the name, photo, or National Emblem.
   - Text must be razor-sharp and easily legible without zooming.
4. **File Format:** High-resolution JPG or PNG, file size between 1 MB and 5 MB.

### C. Address Mismatch Handling
- If your current mailing address (e.g. rented residence in Dhaka) differs from the permanent village address printed on your Smart NID:
  - Identity verification verifies *who you are*, not your current address. Use your legal NID for identity.
  - If Google requests secondary address proof, you can upload an official **Bank Account Statement** (with the bank branch seal and signature), a recent **Utility Bill**, or a **National Tax Certificate** showing your legal name and the current mailing address.

---

## 4. Address & Physical PIN Delivery Protocol (ঠিকানা ও ডাক পিন নীতিমালা)

Identity verification must be approved before Google dispatches the Address Verification PIN postcard via standard international airmail from Google Ireland.

### A. Bangladesh Post Delivery Optimization (চিঠি পাওয়ার নিশ্চিত কৌশল)
In Bangladesh, international mail delivered by the Bangladesh Post Office (ডাক বিভাগ) frequently gets delayed or lost if the local postman cannot locate the address. Follow this exact address formatting:

1. **Address Line 1:**
   - Village / House No, Road No / Area, Union / Ward / Sub-district.
   - Example: `House 12, Road 4, Sector 7, Uttara` or `Vill: Chandpur, PO: Madhabpur`.
2. **Address Line 2 (CRITICAL FOR BANGLADESH):**
   - **ALWAYS put your active mobile phone number here.**
   - Example: `Mobile: +88017XXXXXXXX (Call for Delivery)`
   - Reason: Google does NOT print the phone field on the exterior of the paper postcard envelope. But it DOES print Address Line 2. When the postman sees your phone number printed on the envelope, they will call you directly to pick up the letter.
3. **City / District:**
   - Your official administrative district (e.g., `Dhaka`, `Sylhet`, `Chattogram`, `Rajshahi`).
4. **Postal Code (ZIP Code):**
   - The exact **4-digit Postal Code** of your local sub-post office where you can physically visit and collect mail. Never guess or use a generic central code.

### B. What to Do If the PIN Fails to Arrive
- Google allows you to request a replacement PIN every 30 days (up to 4 times).
- After the 4th PIN request (approx. 4 months), Google automatically activates the **Online PIN Troubleshooter / Document Verification**, where you can upload a photo of your Smart NID or Bank Statement with the matching address for instant digital verification.

---

## 5. Website Technical & Ownership Prerequisites (ওয়েবসাইট টেকনিক্যাল ও মালিকানা যাচাই)

Never submit an application until the website satisfies all technical verification gates:

### A. Domain & DNS Configuration
1. **Root Domain Submission:**
   - For custom domains, submit the root domain (`helptrickbd.com`). AdSense will automatically cover `www.helptrickbd.com`.
2. **SSL / HTTPS Active:**
   - Active SSL certificate with 100% HTTPS enforcement. Zero mixed-content warnings (all images and scripts must load via `https://`).
3. **ads.txt Live at Root:**
   - URL: `https://www.helptrickbd.com/ads.txt` and `https://helptrickbd.com/ads.txt`
   - Content: `google.com, pub-5722984027647168, DIRECT, f08c47fec0942fa0`
   - Must return `HTTP 200 OK` with plain text content.
4. **AdSense Snippet in HTML `<head>`:**
   - Must be placed between `<head>` and `</head>` on the homepage and across all template pages:
     ```html
     <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5722984027647168" crossorigin="anonymous"></script>
     ```
5. **Crawler Access (robots.txt):**
   - `robots.txt` must NOT block `User-agent: Mediapartners-Google` or `User-agent: *`.
   - Never disallow post content or feeds needed by Googlebot.

---

## 6. Mandatory Consent Management Platform (CMP / GDPR & Privacy Regulations)

Since January 16, 2024, Google enforces strict user consent mandates for all AdSense publishers worldwide.

### A. European Regulations (GDPR & UK TCF v2.2+)
- If any visitor accesses your site from the European Economic Area (EEA), United Kingdom, or Switzerland, you MUST serve an IAB TCF-certified consent message.
- If a certified CMP is not detected, Google automatically blocks ad rendering for EEA/UK traffic, resulting in zero monetization and account compliance warnings.

### B. Free Built-in AdSense Solution (1-Click Setup)
You do NOT need to purchase expensive third-party tools. Use Google's native certified CMP:
1. In your AdSense dashboard, click **Privacy & messaging** (গোপনীয়তা এবং মেসেজিং).
2. Under **European regulations**, click **Create message**.
3. Select your domain (`helptrickbd.com`), choose the default consent settings ("Consent or pay" or "Do not consent"), and click **Publish**.
4. Repeat for **US state privacy laws** if substantial traffic originates from the United States.
5. The Google AdSense code already in your `<head>` will automatically deliver the certified consent dialog to relevant visitors.

---

## 7. Modern Impression-Based (CPM) Monetization Architecture (২০২৪+ পেমেন্ট মডেল)

In 2024, Google AdSense modernized its revenue model to align with display industry standards:

### A. Transition from CPC to CPM
- AdSense earnings are now predominantly calculated on an **Impression (CPM)** basis rather than solely Cost-Per-Click (CPC).
- While user clicks still signal high advertiser intent and drive up bidding rates, publishers are paid for viewable ad impressions (Active View 50%+ on screen for at least 1 second).

### B. Transparent Revenue Share Split
- Google splits AdSense revenue into separate buy-side (Google Ads/DSP) and sell-side fees.
- Publishers receive an official **80% revenue share** on the sell-side after buy-side fees, preserving historical earning averages.

---

## 8. Invalid Traffic (IVT) Defense & Ad Placement Standards (অবৈধ ট্রাফিক ও বিজ্ঞাপন প্লেসমেন্ট)

The most destructive issue for approved AdSense publishers is the dreaded "Ad serving on your account is currently limited" policy notification caused by invalid clicks.

### A. The Better Ads Standards (Mobile 30% Density Limit)
- Advertisements must never exceed **30% of the total vertical screen height** on mobile devices.
- Long content pages are required so that ads are spaced out naturally. Never stack multiple ad units consecutively without intervening paragraphs.

### B. Accidental Click Prevention
- Never place ads directly adjacent to or touching navigation menus, drop-down buttons, image sliders, or download buttons.
- If users accidentally tap an ad when trying to click a button, Google triggers the **Confirmed Clicks penalty** (where users must click an ad twice to confirm), plummeting your CTR and RPM by 80%.

### C. Zero Self-Clicking & Social Click Rings
- **Never click your own ads under any circumstances.**
- Never ask friends, family, or social media groups to "visit my site and click ads". Google's neural network detects IP proximity, session durations, device fingerprints, and click patterns within minutes.

---

## 9. Editorial & Content Quality Thresholds (সম্পাদকীয় ও কনটেন্ট মানদণ্ড)

AdSense human reviewers and machine learning crawlers evaluate whether the site represents a legitimate, value-adding publication:

### A. Content Volume & Depth
- **Minimum Post Count:** 30 to 50+ posts minimum (HelpTrickBD has 128 posts).
- **Zero Thin Content:** No articles under 600 words. At least 50%+ of all articles must be 1,000 to 1,500+ words.
- **Originality & E-E-A-T:** Real human expertise, structured analysis, curriculum citations, and author attribution cards (`.htbd-author-box`) with clean author thumbnails.
- **No Copyright Infringement:** Zero pirated software, cracked APKs, unauthorized movie/song downloads, or scraped full-text articles from news media.

### B. The 5 Mandatory Legal Trust Pages
Must be accessible via the site's footer and header menus, returning `HTTP 200 OK`:
1. **About Us (`/p/about-us.html`):** Site mission, editorial standards, author background, physical/editorial contact details.
2. **Contact Us (`/p/contact-us.html`):** Working contact form, dedicated email address, social links.
3. **Privacy Policy (`/p/privacy-policy.html`):** Must explicitly state that the site uses Google AdSense, third-party cookies (DoubleClick DART), and explains user privacy choices.
4. **Terms & Conditions (`/p/terms-conditions.html`):** User terms, copyright notices, acceptable use.
5. **Disclaimer (`/p/disclaimer.html`):** Educational/informational disclaimer.

### C. Clean Navigation & Zero Empty Categories
- Every category or label visible in the header menu MUST contain at least 4 to 5 published articles.
- Zero broken links (404 errors) anywhere on the homepage, menus, or footer.

---

## 10. Step-by-Step AdSense Submission Protocol (ধাপে ধাপে আবেদন নির্দেশিকা)

Follow this precise chronological workflow:

### Step 1: Pre-Submission Audit
Run the automated pre-flight audit tool:
```bash
python tools/auditor/run_full_site_360_audit.py
python tools/auditor/scan_live_images_and_links.py
```
Verify:
- Thin content = 0
- Broken links = 0
- Official 16:9 banners = 100%

### Step 2: Google Account & Payments Verification
1. Sign in to your designated Gmail account.
2. Go to `myaccount.google.com/personal-info` and confirm that Name and Date of Birth match your Smart NID.
3. Verify that 2-Step Verification is active.

### Step 3: Sign Up on Google AdSense
1. Visit `https://adsense.google.com/start/`.
2. Enter your site URL: `helptrickbd.com` (without https or www).
3. Enter your Gmail address.
4. Select Country/Territory: **Bangladesh**.
5. Read and accept the Terms and Conditions.
6. Click **Start using AdSense**.

### Step 4: Complete Customer Information (Payment Profile)
1. In the AdSense dashboard, under **Enter Information**:
   - Account Type: **Individual**.
   - Name: Enter your full legal name exactly as shown on your Smart NID.
   - Address Line 1: Village / Road / House / Area.
   - Address Line 2: `Mobile: +88017XXXXXXXX`
   - Town / City: Your district.
   - Postal Code: Exact 4-digit code.
   - Phone Number: Your active mobile number for SMS OTP verification.
2. Click **Submit**.

### Step 5: Connect Your Site
1. Under **Connect your site to AdSense**:
   - Check the box: "I've pasted the code into my site" (if using AdSense code) OR confirm `ads.txt` is verified.
2. Click **Request Review** (অনুরোধ পাঠান).

---

## 11. The Review Period Governance (পর্যালোচনা চলাকালীন নিয়মাবলি)

The AdSense review process typically takes between **48 hours and 14 days**. During this sensitive window, strict rules must be maintained:

1. **Keep Publishing (Do NOT Pause):**
   - Publish at least 1 to 2 high-quality, 1,200+ word articles per week.
   - Why: Google reviewers check if the site is actively maintained. A stagnant site during review signals low commitment.
2. **Zero Structural Changes:**
   - Do NOT change the Blogger theme.
   - Do NOT modify menu structures, labels, or URL slugs.
   - Do NOT delete existing posts.
3. **Zero Artificial Traffic:**
   - Never purchase bot traffic, use auto-surf exchanges, or post spam links on Facebook groups urging people to click.
   - Rely strictly on natural Google Search organic traffic.

---

## 12. Rejection Handling & The Cooldown Protocol (প্রত্যাখ্যান ব্যবস্থাপনা ও পুনরায় আবেদন)

If an application is rejected with "Low Value Content" (স্বল্প মূল্যের কনটেন্ট) or "Site Down or Unavailable":

1. **Do NOT Instantly Reapply:**
   - Clicking "Request Review" the very next day triggers an automated machine rejection.
2. **Mandatory 3 to 4-Week Cooldown:**
   - Spend 20 to 30 days strengthening the site.
   - Write and publish 6 to 10 brand-new, comprehensive 1,500+ word original guides.
   - Verify all new posts are indexed in Google Search Console.
   - Run broken link scanners and verify mobile Core Web Vitals.
3. **Submit Re-review:** Once the site has refreshed Google Search impressions, click Request Review.

---

## 13. Post-Approval Financial & Compliance Setup (অনুমোদন পরবর্তী সেটআপ)

Once you receive the "Good news! Your site is now ready to show AdSense ads" email:

### A. US Tax Information (Form W-8BEN & Bangladesh e-TIN)
1. Go to **Payments > Payments info > Manage settings > United States tax info**.
2. Start the tax form:
   - Type of account: **Individual**.
   - Are you a US citizen/resident? **No**.
   - Select form type: **W-8BEN** (for non-US individuals).
3. **Claim Tax Treaty Benefits (Crucial):**
   - Country of citizenship: **Bangladesh**.
   - Under **Foreign TIN**, enter your official **12-digit Bangladesh e-TIN**.
   - Check the box: "Are you claiming a reduced rate of withholding under a tax treaty?" -> Select **Yes**, country: **Bangladesh**.
   - Select treaty rates:
     * Services (AdSense): 0% reduced treaty rate (instead of 30%).
     * Motion Picture & TV (YouTube if applicable): 10% treaty rate.
     * Other copyright: 10% treaty rate.
4. Digitally sign the form with your legal name and submit.

### B. Bank Wire Transfer (SWIFT Wire)
When earnings reach $10, configure your payout method:
1. Go to **Payments > Payments info > Add payment method > Add new wire transfer details**.
2. Required fields:
   - **Beneficiary ID:** (Optional, leave blank).
   - **Name on Bank Account:** Must match AdSense Payee Name exactly.
   - **Bank Name:** Full official English name of your bank (e.g. `Islami Bank Bangladesh PLC`, `Dutch-Bangla Bank PLC`, `City Bank PLC`, `Eastern Bank PLC`).
   - **SWIFT-BIC:** The 8 or 11-character SWIFT code of your bank's head office (e.g. `IBBLBDDH` for Islami Bank).
   - **Routing Number:** 9-digit branch routing number.
   - **Account Number:** Full numeric bank account number.
3. Set as **Primary payment method**.

---

## 14. Comprehensive 16-Point Pre-Application Checklist Matrix

| # | অডিট চেকলিস্ট আইটেম | প্রয়োজনীয় মান | ভেরিফিকেশন মেথড |
|:---:|:---|:---|:---|
| 01 | **আবেদনকারীর বয়স** | ন্যূনতম ১৮ বছর বা তদূর্ধ্ব | গুগল অ্যাকাউন্ট জন্মতারিখ ও এনআইডি কার্ড |
| 02 | **ডুপ্লিকেট অ্যাকাউন্ট চেক** | অতীতে কোনো এডসেন্স অ্যাকাউন্ট খোলা নেই | জিমেইল ইনবক্স সার্চ ও ইউজারনেম রিকভারি |
| 03 | **এনআইডি ও জিমেইল নামের মিল** | শতভাগ বর্ণে বর্ণে মিল (স্মার্ট এনআইডির ইংরেজি) | জিমেইল প্রোফাইল ও পেমেন্ট প্রোফাইল এডিট |
| 04 | **২-স্টেপ ভেরিফিকেশন (2FA)** | গুগল অ্যাকাউন্টে পার্মানেন্ট ২-ফ্যাক্টর অ্যাক্টিভ | myaccount.google.com সিকিউরিটি চেক |
| 05 | **ঠিকানার সাথে মোবাইল নম্বর** | Address Line 2-তে সক্রিয় মোবাইল নম্বর অন্তর্ভুক্ত | পোস্টম্যান যেন চিঠি পেয়ে সরাসরি কল করতে পারেন |
| 06 | **সঠিক ৪-ডিজিট পোস্টাল কোড** | নিজ স্থানীয় সাব-পোস্ট অফিসের ৪ অঙ্কের কোড | ডাক বিভাগের অফিসিয়াল কোড লিস্ট |
| 07 | **কেওয়াইসি ডকুমেন্টের প্রস্তুতি** | স্মার্ট এনআইডির উভয় পিঠের আসল স্পষ্ট রঙিন ছবি | ৪ কোণ দৃশ্যমান, ফ্ল্যাশ গ্লেয়ার মুক্ত |
| 08 | **৫টি বাধ্যতামূলক লিগ্যাল পেজ** | About Us, Contact Us, Privacy Policy, Terms, Disclaimer | প্রতিটি পেজে HTTP 200 রেসপন্স নিশ্চিত |
| 09 | **ads.txt ফাইল সক্রিয়** | রুট ডোমেনে pub-ID সহ সক্রিয় ads.txt | `https://www.helptrickbd.com/ads.txt` (200 OK) |
| 10 | **এডসেন্স হেড কোড** | `<head>` ব্লকে অফিসিয়াল জাভাস্ক্রিপ্ট কোড যুক্ত | থিমের HTML সোর্সে ca-pub স্ক্রিপ্ট উপস্থিত |
| 11 | **কনটেন্ট গভীরতা ও মোট পোস্ট** | ৩০+ পোস্ট (সাইটে ১২৮টি বিদ্যমান), থিন কনটেন্ট ০ | ৬০০ শব্দের নিচে কোনো পোস্ট নেই |
| 12 | **মেনু ও ক্যাটাগরি ব্যালান্স** | প্রতিটি লেবেলে ন্যুনতম ৪-৫টি পোস্ট, ০টি খালি লেবেল | হেডার মেনুর সমস্ত লিঙ্কে পোস্ট বিদ্যমান |
| 13 | **ব্রোকেন লিঙ্ক ও ইমেজ ALT** | ০টি ব্রোকেন লিঙ্ক, ১০০% ছবিতে ডেসক্রিপটিভ ALT | সাইটওয়াইড স্ক্রিপ্ট স্ক্যানে ভেরিফায়েড |
| 14 | **অর্গানিক সার্চ ট্রাফিক** | সার্চ কনসোলে দৈনিক নিয়মিত ক্লিক ও ইমপ্রেশন | গুগলে আসল মানুষ সাইট ভিজিট করছে |
| 15 | **GDPR CMP কন্সেন্ট মেসেজ** | Privacy & messaging ট্যাবে IAB TCF মেসেজ রেডি | ইউরোপীয় ট্রাফিকের জন্য লিগ্যাল কমপ্লায়েন্স |
| 16 | **মোবাইল অ্যাড ডেনসিটি ৩০%** | দীর্ঘ কনটেন্টে স্বাভাবিক ব্যবধানে অ্যাড ডিসপ্লে | বেটার অ্যাডস স্ট্যান্ডার্ডস ও জিরো আকস্মিক ক্লিক |
