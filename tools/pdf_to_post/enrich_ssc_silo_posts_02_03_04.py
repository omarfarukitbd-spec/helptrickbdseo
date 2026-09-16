#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/pdf_to_post/enrich_ssc_silo_posts_02_03_04.py
----------------------------------------------------
Enriches posts 02, 03, 04 of the SSC 2027 silo series with additional
content sections to surpass the 1,000-word Pre-Flight threshold.
Inserts new sections before the series nav box.
"""

import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RAW_POSTS_DIR = os.path.join(PROJECT_ROOT, "scratch", "raw_posts")

# ─────────────────────────────────────────────────────────────────────────────
# EXTRA CONTENT BLOCKS FOR POST 02: UNSEEN PASSAGE & SUMMARY
# ─────────────────────────────────────────────────────────────────────────────
EXTRA_02 = """
  <h2 class="htbd-academic-heading" id="practice-passages">৭. আনসিন প্যাসেজ প্র্যাকটিস গাইড (Unseen Passage Practice Strategy for SSC 2027)</h2>
  <p>Unseen Passage-এ ভালো করার জন্য শুধু পরীক্ষার দিনের দক্ষতাই যথেষ্ট নয়। নিয়মিত বিভিন্ন বিষয়ের Passage পড়ার অভ্যাস গড়ে তুলতে হবে। নিচে কার্যকর অনুশীলন কৌশল দেওয়া হলো।</p>

  <h3 class="htbd-academic-subheading">দৈনিক পড়ার অভ্যাস (Daily Reading Habit)</h3>
  <p>প্রতিদিন ইংরেজি পত্রিকার (The Daily Star, The Business Standard) যেকোনো একটি সংবাদ বা Feature Article পড়ুন। প্রতিটি অনুচ্ছেদ পড়ার পর নিজেকে প্রশ্ন করুন — "এই প্যারাগ্রাফের মূল বিষয় কী?" এই অভ্যাস Unseen Passage-এ দ্রুত মূলভাব ধরার ক্ষমতা তৈরি করে।</p>
  <p>বিষয়ভিত্তিক Passage-এর জন্য নিচের বিষয়গুলোতে বিশেষ মনোযোগ দিন, কারণ SSC পরীক্ষায় এই বিষয়গুলো থেকেই Unseen Passage বেশি আসে:</p>

  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 22px 0;">
    <table class="htbd-academic-table">
      <thead>
        <tr><th>বিষয় (Topic)</th><th>কেন গুরুত্বপূর্ণ</th><th>পড়ার উৎস</th></tr>
      </thead>
      <tbody>
        <tr><td>পরিবেশ ও জলবায়ু পরিবর্তন</td><td>SSC-তে বারবার আসে</td><td>The Daily Star Environment Section</td></tr>
        <tr><td>স্বাস্থ্য ও পুষ্টি</td><td>Information Transfer-এ উপযুক্ত</td><td>WHO বাংলাদেশ, স্বাস্থ্য অধিদপ্তর</td></tr>
        <tr><td>বিজ্ঞান ও প্রযুক্তি</td><td>আধুনিক প্রশ্নপত্রে বাড়ছে</td><td>Science Magazines, BBC Science</td></tr>
        <tr><td>সমাজ ও সংস্কৃতি</td><td>Opinion-based প্রশ্নে আসে</td><td>Star Weekend Magazine</td></tr>
        <tr><td>ইতিহাস ও ঐতিহ্য</td><td>Bangladesh-specific passage</td><td>Bangladesh History books</td></tr>
      </tbody>
    </table>
  </div>

  <h3 class="htbd-academic-subheading">Information Transfer-এর ধরন ও নমুনা (Types of Information Transfer Charts)</h3>
  <p>SSC পরীক্ষায় Information Transfer-এ সাধারণত চার ধরনের Chart বা Table আসে। প্রতিটি ধরনের সাথে পরিচিত থাকলে Q4-এ সর্বোচ্চ ৫ নম্বর পাওয়া সহজ হয়।</p>

  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 22px 0;">
    <table class="htbd-academic-table">
      <thead>
        <tr><th>Chart-এর ধরন</th><th>উদাহরণ</th><th>কী পূরণ করতে হয়</th></tr>
      </thead>
      <tbody>
        <tr><td>Flow Chart (ক্রমানুসারী ছক)</td><td>একটি প্রক্রিয়ার ধাপ</td><td>পদক্ষেপের নাম বা বিবরণ</td></tr>
        <tr><td>Comparison Table (তুলনামূলক ছক)</td><td>দুটি বিষয়ের তুলনা</td><td>বৈশিষ্ট্য, সুবিধা-অসুবিধা</td></tr>
        <tr><td>Timeline (সময়রেখা)</td><td>ঐতিহাসিক ঘটনার ক্রম</td><td>তারিখ বা সালের বিবরণ</td></tr>
        <tr><td>Category Table (শ্রেণিবিভাগ ছক)</td><td>বিভিন্ন শ্রেণির তথ্য</td><td>নাম, পরিমাণ, বৈশিষ্ট্য</td></tr>
      </tbody>
    </table>
  </div>

  <h3 class="htbd-academic-subheading">Summary Writing-এ সাধারণ ভুলগুলো (Common Mistakes in Summary Writing)</h3>
  <p>বাংলাদেশের SSC পরীক্ষার্থীরা Summary Writing-এ যেসব সাধারণ ভুল করেন, সেগুলো এড়িয়ে চললে নম্বর উল্লেখযোগ্যভাবে বাড়ানো সম্ভব:</p>
  <p><strong>ভুল ১ — হুবহু কপি করা:</strong> অনেকে Passage থেকে পুরো বাক্য তুলে দেন। এটি Summary নয়, এটি Copying। পরীক্ষকরা এতে নম্বর কাটেন। সবসময় নিজের ভাষায় (Paraphrase) লিখুন।</p>
  <p><strong>ভুল ২ — অতিরিক্ত লম্বা Summary:</strong> Summary-র দৈর্ঘ্য যদি মূল Passage-এর অর্ধেক বা বেশি হয়, তাহলে Length নম্বর কাটা যায়। এক-তৃতীয়াংশের মধ্যে রাখুন।</p>
  <p><strong>ভুল ৩ — শুধু একটি প্যারাগ্রাফের বিষয় নেওয়া:</strong> Summary-তে Passage-এর সব প্রধান বিষয় (Main Points) অন্তর্ভুক্ত করতে হয়। একটি প্যারাগ্রাফের উপর focus করলে বাকি Content নম্বর কাটা যাবে।</p>
  <p><strong>ভুল ৪ — নিজের মতামত যোগ করা:</strong> Summary-তে কখনো নিজের মতামত (My opinion is..., I think...) দেওয়া যাবে না। শুধু Passage-এর বক্তব্য নিজের ভাষায় বলুন।</p>
  <p><strong>ভুল ৫ — উদাহরণ অন্তর্ভুক্ত করা:</strong> Passage-এ দেওয়া উদাহরণগুলো Summary-তে আনার দরকার নেই। শুধু মূল তথ্য ও বক্তব্য লিখুন।</p>

  <div class="htbd-tip-box">
    <p><strong>চূড়ান্ত পরামর্শ:</strong> পরীক্ষায় Unseen Passage পড়ার জন্য প্রথম ২ মিনিট ব্যয় করুন। Q4 (Information Transfer) ও Q5 (Summary) একই Passage থেকে আসে — তাই একসাথে পড়লে সময় বাঁচে এবং উভয় প্রশ্নেই ভালো করা যায়।</p>
  </div>

  <h2 class="htbd-academic-heading" id="exam-tips">৮. পরীক্ষার হলে সময় ব্যবস্থাপনা (Exam Hall Time Management for Reading Section)</h2>
  <p>এসএসসি ইংরেজি পরীক্ষায় মোট সময় ৩ ঘন্টা। Reading Section (Part A — ৭০ নম্বর) এবং Writing Section (Part B — ৩০ নম্বর)-এ সুষমভাবে সময় ভাগ করতে হবে।</p>

  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 22px 0;">
    <table class="htbd-academic-table">
      <thead>
        <tr><th>সেকশন</th><th>প্রশ্ন</th><th>প্রস্তাবিত সময়</th><th>কৌশল</th></tr>
      </thead>
      <tbody>
        <tr><td>Seen Passage পড়া</td><td>Q1, Q2, Q3</td><td>৩০ মিনিট</td><td>Q2 সবার আগে করুন</td></tr>
        <tr><td>Unseen Passage পড়া</td><td>Q4, Q5</td><td>৩০ মিনিট</td><td>Passage একবার পুরো পড়ুন</td></tr>
        <tr><td>Matching + Rearranging</td><td>Q6, Q7</td><td>২০ মিনিট</td><td>নিশ্চিত উত্তর আগে</td></tr>
        <tr><td>Poems + Stories</td><td>Q8, Q9</td><td>৩০ মিনিট</td><td>সহজ ৫টি বেছে নিন</td></tr>
        <tr><td>Writing (Story + Dialogue)</td><td>Q10, Q11</td><td>৪৫ মিনিট</td><td>Draft করে নিন</td></tr>
        <tr><td>Revision</td><td>সব</td><td>৫ মিনিট</td><td>বানান ও নাম যাচাই</td></tr>
      </tbody>
    </table>
  </div>
"""

# ─────────────────────────────────────────────────────────────────────────────
# EXTRA CONTENT BLOCKS FOR POST 03: MATCHING & RE-ARRANGING
# ─────────────────────────────────────────────────────────────────────────────
EXTRA_03 = """
  <h2 class="htbd-academic-heading" id="grammar-deep">৭. Grammar Foundation for Q6 & Q7 — গভীর ব্যাকরণ জ্ঞান</h2>
  <p>Q6 (Sentence Matching) ও Q7 (Re-arranging Sentences) — উভয় প্রশ্নেই English Grammar-এর গভীর জ্ঞান প্রয়োজন। শুধু কৌশল নয়, নিচের ব্যাকরণিক নিয়মগুলো আয়ত্ত করলে উভয় প্রশ্নে পূর্ণ নম্বর নিশ্চিত করা যায়।</p>

  <h3 class="htbd-academic-subheading">Clause ও Phrase — পার্থক্য ও ব্যবহার (Clauses and Phrases)</h3>
  <p>Sentence Matching-এ Column A, B, C-এর অংশগুলো সাধারণত Independent Clause ও Dependent Clause হয়। Independent Clause নিজে একটি সম্পূর্ণ বাক্য তৈরি করতে পারে, কিন্তু Dependent Clause একা অর্থবোধক হয় না।</p>
  <p>উদাহরণ — <em>"Although he was tired"</em> একটি Dependent Clause, এটি একা বাক্য নয়। এর সাথে <em>"he continued to study"</em> যোগ করলে সম্পূর্ণ বাক্য হয়।</p>
  <p>Matching Table-এ Dependent Clause খুঁজে পেলেই বুঝবেন এটি Column B বা C-তে আছে এবং Column A-তে এর সাথে মানানসই Independent Clause খুঁজতে হবে।</p>

  <h3 class="htbd-academic-subheading">Subject-Verb Agreement — ম্যাচিং-এর মূল চাবিকাঠি</h3>
  <p>Sentence Matching-এ Subject ও Verb-এর মিল সবচেয়ে গুরুত্বপূর্ণ। নিচের নিয়মগুলো মনে রাখলে Column B থেকে সঠিক Verb phrase বেছে নেওয়া সহজ হবে।</p>

  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 22px 0;">
    <table class="htbd-academic-table">
      <thead>
        <tr><th>Subject Type</th><th>Verb Form</th><th>উদাহরণ</th></tr>
      </thead>
      <tbody>
        <tr><td>Singular Subject (He, She, It, The boy)</td><td>Singular Verb (is, was, has, does)</td><td>The boy is playing.</td></tr>
        <tr><td>Plural Subject (They, Students, The books)</td><td>Plural Verb (are, were, have, do)</td><td>The books are on the table.</td></tr>
        <tr><td>I</td><td>am, was, have, do</td><td>I am a student.</td></tr>
        <tr><td>You</td><td>are, were, have, do</td><td>You are my friend.</td></tr>
        <tr><td>Uncountable Noun (water, rice, information)</td><td>Singular Verb</td><td>Water is essential.</td></tr>
      </tbody>
    </table>
  </div>

  <h3 class="htbd-academic-subheading">Discourse Markers — Re-arranging-এর সেরা হাতিয়ার</h3>
  <p>Re-arranging Sentences (Q7)-এ Discourse Markers সবচেয়ে গুরুত্বপূর্ণ ভূমিকা রাখে। এগুলো বাক্যের মধ্যে Logical Flow তৈরি করে এবং ক্রম নির্ধারণে সাহায্য করে।</p>

  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 22px 0;">
    <table class="htbd-academic-table">
      <thead>
        <tr><th>Position</th><th>Discourse Markers</th><th>ব্যবহারের উদাহরণ</th></tr>
      </thead>
      <tbody>
        <tr><td>শুরুতে (Opening)</td><td>Once, Long ago, One day, At first, In the beginning</td><td>"Once there was a wise king."</td></tr>
        <tr><td>মাঝে (Middle — Addition)</td><td>Moreover, Furthermore, In addition, Besides, Also</td><td>"Moreover, he was very kind."</td></tr>
        <tr><td>মাঝে (Middle — Contrast)</td><td>However, But, Nevertheless, On the contrary, Yet</td><td>"However, his health was poor."</td></tr>
        <tr><td>মাঝে (Middle — Cause)</td><td>Because, As, Since, Due to, Owing to</td><td>"Since he worked hard, he succeeded."</td></tr>
        <tr><td>শেষে (Concluding)</td><td>Finally, At last, In the end, Therefore, Thus, As a result</td><td>"Finally, he became successful."</td></tr>
      </tbody>
    </table>
  </div>

  <h2 class="htbd-academic-heading" id="practice-exercises">৮. অনুশীলন উদাহরণ (Practice Exercises for Q6 & Q7)</h2>
  <p>পরীক্ষায় ভালো করতে হলে নিয়মিত Q6 ও Q7-এর অনুশীলন করতে হবে। নিচে একটি পূর্ণ অনুশীলনী দেওয়া হলো:</p>

  <h3 class="htbd-academic-subheading">অনুশীলন ১ — Sentence Matching Table (Q6 Practice)</h3>
  <p>নিচের Column A, B, C মিলিয়ে সম্পূর্ণ বাক্য তৈরি করুন:</p>

  <div style="overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 20px 0;">
    <table class="htbd-academic-table">
      <thead>
        <tr><th>Column A (Subject / Beginning)</th><th>Column B (Middle / Verb Phrase)</th><th>Column C (End / Purpose or Result)</th></tr>
      </thead>
      <tbody>
        <tr><td>(i) We should plant trees</td><td>(a) is essential for good health</td><td>(I) to protect the environment</td></tr>
        <tr><td>(ii) Regular exercise</td><td>(b) affects our daily life</td><td>(II) and reduces stress</td></tr>
        <tr><td>(iii) The internet</td><td>(c) should be conserved</td><td>(III) for future generations</td></tr>
        <tr><td>(iv) Water resources</td><td>(d) must be studied properly</td><td>(IV) to get good results</td></tr>
        <tr><td>(v) Every subject</td><td>(e) helps us communicate</td><td>(V) with the whole world</td></tr>
      </tbody>
    </table>
  </div>
  <p><strong>উত্তর (Answers):</strong></p>
  <p style="background:#f0fdf4; border:1px solid #bbf7d0; padding:14px 18px; border-radius:8px; color:#14532d; font-size:16px; line-height:1.9;">
  (i) + (a) + (I): We should plant trees to protect the environment.<br>
  (ii) + (a) + (II): Regular exercise is essential for good health and reduces stress.<br>
  (iii) + (e) + (V): The internet helps us communicate with the whole world.<br>
  (iv) + (c) + (III): Water resources should be conserved for future generations.<br>
  (v) + (d) + (IV): Every subject must be studied properly to get good results.
  </p>

  <h2 class="htbd-academic-heading" id="checklist">৯. পরীক্ষার আগে Checklist (Pre-Exam Checklist for Q6 & Q7)</h2>
  <p>পরীক্ষার হলে Q6 ও Q7 শুরু করার আগে নিচের checklist মনে রাখুন:</p>
  <p><strong>Q6 Sentence Matching:</strong> প্রতিটি Column ভালো করে পড়েছি। Grammar Agreement যাচাই করেছি। Meaning-based logic মিলিয়েছি। প্রতিটি Option একবারই ব্যবহার করেছি। সম্পূর্ণ বাক্য লিখেছি।</p>
  <p><strong>Q7 Re-arranging:</strong> Topic Sentence চিহ্নিত করেছি। Pronoun Reference দেখেছি। Time Connectives ও Discourse Markers অনুসরণ করেছি। Concluding Sentence সবশেষে দিয়েছি। সম্পূর্ণ বাক্য লিখেছি।</p>

  <div class="htbd-warning-box">
    <p><strong>সতর্কতা:</strong> Q7-এ সাজানো বাক্যগুলোর ক্রম লেখার সময় শুধু (a, b, c) অক্ষর না লিখে সম্পূর্ণ বাক্য লিখুন। অনেক পরীক্ষক শুধু অক্ষরের উত্তর গ্রহণ করেন না।</p>
  </div>
"""

# ─────────────────────────────────────────────────────────────────────────────
# EXTRA CONTENT BLOCKS FOR POST 04: POEMS & STORIES
# ─────────────────────────────────────────────────────────────────────────────
EXTRA_04 = """
  <h2 class="htbd-academic-heading" id="poem-analysis">৭. গুরুত্বপূর্ণ কবিতার বিস্তারিত বিশ্লেষণ (Detailed Poem Analysis for SSC 2027)</h2>
  <p>SSC 2027 পরীক্ষার জন্য সবচেয়ে গুরুত্বপূর্ণ কবিতাগুলোর মূল বিষয়, কবির উদ্দেশ্য ও সম্ভাব্য প্রশ্নের ধরন নিচে বিশ্লেষণ করা হলো। এই তথ্যগুলো পরীক্ষার উত্তর লেখায় সরাসরি কাজে আসবে।</p>

  <h3 class="htbd-academic-subheading">The Road Not Taken — Robert Frost (বিস্তারিত বিশ্লেষণ)</h3>
  <p>এই বিখ্যাত কবিতায় Robert Frost জীবনের এক চৌরাস্তায় দাঁড়িয়ে পথ বেছে নেওয়ার অভিজ্ঞতা বর্ণনা করেছেন। কবি দুটি পথের মধ্যে কম-জনবহুল পথটি বেছে নেন এবং পরে বলেন এই সিদ্ধান্তই তার জীবনে পার্থক্য এনেছে।</p>
  <p><strong>Central Theme:</strong> Life's choices and their consequences. প্রতিটি মানুষকে জীবনে গুরুত্বপূর্ণ সিদ্ধান্ত নিতে হয় এবং সেই সিদ্ধান্ত ভবিষ্যৎ নির্ধারণ করে।</p>
  <p><strong>Key Lines to Remember:</strong> "Two roads diverged in a wood, and I — I took the one less travelled by, And that has made all the difference."</p>
  <p><strong>Probable Questions:</strong> What does the "road" symbolize in this poem? What is the poet's dilemma? What does "the road not taken" represent?</p>

  <h3 class="htbd-academic-subheading">O Captain! My Captain! — Walt Whitman (বিস্তারিত বিশ্লেষণ)</h3>
  <p>এই শোকগাথা কবিতাটি মার্কিন প্রেসিডেন্ট আব্রাহাম লিংকনের মৃত্যুতে Walt Whitman রচনা করেন। আমেরিকার গৃহযুদ্ধ শেষ হওয়ার পরই লিংকনকে গুলি করে হত্যা করা হয়। "Captain" হলো লিংকনের রূপক, আর "Ship" হলো আমেরিকার রূপক।</p>
  <p><strong>Central Theme:</strong> Grief and tribute to a great leader. একজন মহান নেতার মৃত্যুতে জাতির শোক এবং তার অবদানের প্রতি শ্রদ্ধাজ্ঞাপন।</p>
  <p><strong>Key Lines to Remember:</strong> "O Captain! My Captain! our fearful trip is done, The ship has weather'd every rack, the prize we sought is won."</p>
  <p><strong>Probable Questions:</strong> Who is the Captain in this poem? What does the ship represent? Why is the poem considered an elegy?</p>

  <h2 class="htbd-academic-heading" id="story-analysis">৮. গুরুত্বপূর্ণ গল্পের বিস্তারিত বিশ্লেষণ (Detailed Story Analysis for SSC 2027)</h2>

  <h3 class="htbd-academic-subheading">The Gift of the Magi — O. Henry (বিস্তারিত বিশ্লেষণ)</h3>
  <p>O. Henry-র এই বিখ্যাত ছোটগল্পে Jim ও Della — দুজন দরিদ্র কিন্তু পরস্পর ভালোবাসায় আবদ্ধ দম্পতির কথা আছে। বড়দিনে একে অপরকে উপহার দেওয়ার জন্য Della তার সুন্দর চুল বিক্রি করে Jim-এর ঘড়ির জন্য চেইন কেনেন, আর Jim তার মূল্যবান ঘড়ি বিক্রি করে Della-র চুলের জন্য comb কেনেন।</p>
  <p><strong>Characters:</strong> Jim (দরিদ্র কিন্তু প্রেমময় স্বামী), Della (আত্মত্যাগী ও ভালোবাসাময় স্ত্রী)।</p>
  <p><strong>Central Theme:</strong> True love and selfless sacrifice are the greatest gifts one can offer.</p>
  <p><strong>Moral:</strong> Sacrificial love is more valuable than any material gift. প্রেমের জন্য আত্মত্যাগই সবচেয়ে বড় উপহার।</p>
  <p><strong>Probable Questions:</strong> What gifts did Jim and Della buy for each other? What is the irony in the story? What is the moral of the story?</p>

  <h3 class="htbd-academic-subheading">The Last Leaf — O. Henry (বিস্তারিত বিশ্লেষণ)</h3>
  <p>এই গল্পে Johnsy নামের একজন তরুণ শিল্পী নিউমোনিয়ায় আক্রান্ত হন এবং বিশ্বাস করেন যে জানালার বাইরের গাছের শেষ পাতাটি ঝরে গেলে তিনিও মারা যাবেন। প্রতিবেশী বৃদ্ধ শিল্পী Behrman তীব্র শীতের রাতে ঝড়ের মধ্যে দেওয়ালে একটি নকল পাতা এঁকে দেন যা কখনো ঝরে না। Johnsy সুস্থ হন, কিন্তু Behrman নিউমোনিয়ায় মারা যান।</p>
  <p><strong>Characters:</strong> Johnsy (অসুস্থ শিল্পী), Sue (বন্ধু), Behrman (বৃদ্ধ শিল্পী)।</p>
  <p><strong>Central Theme:</strong> Hope, friendship, and selfless sacrifice can save a life.</p>
  <p><strong>Moral:</strong> True friendship and hope can overcome even death. সত্যিকারের বন্ধুত্ব ও আশা জীবন বাঁচাতে পারে।</p>

  <h2 class="htbd-academic-heading" id="writing-mastery">৯. পূর্ণ নম্বর পাওয়ার চূড়ান্ত কৌশল (Final Strategy for Full Marks in Q8 & Q9)</h2>
  <p>Q8 ও Q9-এ মোট ২০ নম্বর — এটি পুরো পরীক্ষার ২০%। এই অংশে ভালো করলে সামগ্রিক ফলাফল উল্লেখযোগ্যভাবে উন্নত হয়।</p>
  <p><strong>কবিতার প্রশ্নে (Q8):</strong> উত্তরে কবির নাম, কবিতার Central Theme এবং প্রাসঙ্গিক Line উদ্ধৃত করুন। Literary Device (Metaphor, Symbolism, Irony) উল্লেখ করলে নম্বর বাড়ে।</p>
  <p><strong>গল্পের প্রশ্নে (Q9):</strong> উত্তরে Character-এর নাম, মূল ঘটনা ও Moral বা Theme উল্লেখ করুন। উত্তর সম্পূর্ণ বাক্যে ও নিজের ভাষায় লিখুন — গল্প হুবহু লিখবেন না।</p>
  <p><strong>সময় ব্যবস্থাপনা:</strong> Q8-এর ৫টি উত্তরের জন্য ১৫ মিনিট এবং Q9-এর ৫টি উত্তরের জন্য ১৫ মিনিট বরাদ্দ রাখুন। প্রতিটি উত্তর ৩ মিনিটে শেষ করার লক্ষ্য রাখুন।</p>

  <div class="htbd-tip-box">
    <p><strong>চূড়ান্ত পরামর্শ:</strong> EFT বইয়ের প্রতিটি কবিতা পড়ার সময় একটি নোটবুকে কবির নাম, কবিতার বিষয়, Central Theme, Key Lines এবং Literary Devices লিখে রাখুন। পরীক্ষার আগের রাতে এই নোট পড়লে Q8-এ পূর্ণ নম্বর পাওয়া সহজ হবে।</p>
  </div>
"""


def enrich_post(file_prefix, extra_content, label):
    """Inserts extra content before the series nav box in the HTML file."""
    html_path = os.path.join(RAW_POSTS_DIR, f"{file_prefix}.html")

    if not os.path.exists(html_path):
        print(f"  [ERROR] File not found: {html_path}")
        return False

    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find insertion point: just before the series-nav div
    insert_marker = '<div class="htbd-series-nav">'
    if insert_marker not in content:
        print(f"  [ERROR] Insertion marker not found in {file_prefix}")
        return False

    # Insert extra content before series nav
    enriched = content.replace(insert_marker, extra_content + '\n  ' + insert_marker, 1)

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(enriched)

    # Count approximate visible words (rough estimate)
    import re
    visible_text = re.sub(r'<[^>]+>', ' ', enriched)
    visible_text = re.sub(r'\s+', ' ', visible_text)
    word_count = len(visible_text.split())
    print(f"  [OK] {label}: {html_path}")
    print(f"       Approximate visible words: ~{word_count}")
    return True


def main():
    print("=" * 65)
    print("SSC 2027 SILO POSTS 02-04 ENRICHMENT ENGINE")
    print("=" * 65)

    enrichments = [
        ("ssc_2027_silo_02_unseen_summary", EXTRA_02, "Part 02: Unseen Passage & Summary"),
        ("ssc_2027_silo_03_matching_rearrange", EXTRA_03, "Part 03: Matching & Re-arranging"),
        ("ssc_2027_silo_04_poems_stories", EXTRA_04, "Part 04: Poems & Stories"),
    ]

    success = 0
    for file_prefix, extra_content, label in enrichments:
        print(f"\n[*] Enriching: {label}")
        if enrich_post(file_prefix, extra_content, label):
            success += 1

    print(f"\n{'=' * 65}")
    print(f"Enriched {success}/3 posts. Ready for re-publishing.")
    print(f"{'=' * 65}")


if __name__ == "__main__":
    main()
