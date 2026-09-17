#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/pdf_to_post/generate_full_unseen_data.py
------------------------------------------------
Generates data_ssc_2027_unseen_full.py containing all 41 Unseen Topics:
- Passage context (120-160 words)
- Question 4: Information Transfer Table (headers, 4-5 rows with blanks, exact answers)
- Question 5: Model Summary (60-80 words, 4-5 sentences, academic paraphrasing)
- Paraphrasing / Vocabulary notes
- Star rating, board reference, and priority.
"""

import os
import sys

OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "data_ssc_2027_unseen_full.py")

DATA_ITEMS = [
    {
        "id": 1,
        "slug_id": "unseen-01",
        "title": "Dear Moly (An Informal Letter on True Friendship & Literary Leisure)",
        "bn_title": "ডিয়ার মলি (বন্ধুত্ব ও অবসরে বই পড়ার আনন্দ নিয়ে চিঠি)",
        "theme": "Informal Letter / Value of Reading & Friendship",
        "stars": "***",
        "priority": "Top Priority",
        "boards": "Dakhil Exam-2024",
        "page_pdf": 377,
        "passage": (
            "Dear Moly, I know it has been a long time since I last wrote to you. You will be glad to know that I have "
            "recently finished reading several inspirational books during the vacation. Reading books not only enriches "
            "our vocabulary but also broadens our outlook on life. Among them, a biography of Hellen Keller touched me "
            "deeply. Her struggle against blindness and deafness proves that determination can overcome any physical "
            "obstacle. I hope you are also spending your leisure productively with good literature. Please convey my best "
            "regards to your parents. Hope to hear from you soon. With love, Orin."
        ),
        "info_table": {
            "headers": ["Who / What", "Action / Experience", "Time / When", "Subject / Impact"],
            "rows": [
                ["Orin", "wrote a letter", "after a long time", "to (i) [......]"],
                ["Orin", "read inspirational books", "(ii) [......]", "to broaden outlook"],
                ["(iii) [......]", "struggled with determination", "during her lifetime", "against blindness and deafness"],
                ["Good literature", "(iv) [......]", "throughout life", "enriches vocabulary and mind"],
                ["Moly", "is advised to spend time", "in leisure", "(v) [......]"]
            ]
        },
        "answers": {
            "i": "Moly (her friend)",
            "ii": "during the vacation",
            "iii": "Hellen Keller",
            "iv": "broadens outlook and vocabulary",
            "v": "productively with good literature"
        },
        "model_summary": (
            "In this informal letter, Orin reflects on the profound intellectual and emotional rewards of reading "
            "inspirational literature during vacations. Highlighting Helen Keller's heroic triumph over physical disabilities, "
            "the writer emphasizes how determination conquers adversity. Furthermore, she encourages her friend Moly to "
            "cultivate reading habits productively to expand her knowledge and worldview."
        ),
        "vocab_notes": "Inspirational -> Uplifting; Determination -> Perseverance; Productively -> Fruitfully."
    },
    {
        "id": 2,
        "slug_id": "unseen-02",
        "title": "Facebook and Modern Social Networking: Opportunities and Challenges",
        "bn_title": "ফেসবুক ও আধুনিক সোশ্যাল নেটওয়ার্কিং: সুবিধা ও সতর্কতা",
        "theme": "Social Media, Digital Communication & Global Networking",
        "stars": "***",
        "priority": "Top Priority",
        "boards": "Dakhil Exam-2023",
        "page_pdf": 378,
        "passage": (
            "Facebook is the leading social networking service that was launched in February 2004 by Mark Zuckerberg "
            "with his college roommates at Harvard University. Initially restricted to Harvard students, it gradually "
            "expanded to other universities and eventually to anyone worldwide aged 13 and older. Today, billions of active "
            "users interact on Facebook by sharing thoughts, photos, news links, and digital messages. Users can create "
            "profiles, join interest groups, and comment on their friends' posts. While it has revolutionized global "
            "communication and digital commerce, excessive usage often leads to distraction among students and cyber security risks."
        ),
        "info_table": {
            "headers": ["Entity / Founder", "Event / Achievement", "Year / Date", "Location / Scope"],
            "rows": [
                ["Mark Zuckerberg & roommates", "founded Facebook", "(i) [......]", "Harvard University"],
                ["The service", "was initially limited", "in 2004", "(ii) [......]"],
                ["(iii) [......]", "can join the network worldwide", "at present", "anyone aged 13 and above"],
                ["Facebook users", "share photos and thoughts", "daily", "(iv) [......]"],
                ["Excessive screen time", "causes distraction and risks", "today", "among (v) [......]"]
            ]
        },
        "answers": {
            "i": "February 2004",
            "ii": "to Harvard students",
            "iii": "Billions of active users",
            "iv": "through personal profiles and groups",
            "v": "students and internet users"
        },
        "model_summary": (
            "Founded in 2004 by Mark Zuckerberg at Harvard University, Facebook has evolved from an exclusive college platform "
            "into a dominant global social networking giant. It enables billions of individuals worldwide to exchange ideas, "
            "multimedia content, and commercial updates instantly. However, despite enhancing worldwide connectivity, "
            "unrestrained consumption poses significant productivity losses for learners and critical privacy concerns."
        ),
        "vocab_notes": "Revolutionized -> Transformed; Connectivity -> Global linkage; Distraction -> Loss of focus."
    },
    {
        "id": 3,
        "slug_id": "unseen-03",
        "title": "Humayun Ahmed: Life and Literary Legacy of a Renaissance Storyteller",
        "bn_title": "হুমায়ূন আহমেদ: বাংলা সাহিত্যের কালজয়ী কথাসাহিত্যিক",
        "theme": "Biography / Modern Bengali Literature & Filmmaking",
        "stars": "***",
        "priority": "Top Priority",
        "boards": "Dakhil Exam-2020",
        "page_pdf": 380,
        "passage": (
            "Humayun Ahmed was a distinguished chemistry professor, novelist, dramatist, and filmmaker who revitalized "
            "contemporary Bengali literature. Born on 13 November 1948 in Kutubpur, Netrokona, he achieved his PhD in "
            "chemistry from North Dakota State University. His debut novel 'Nondito Noroke' (1972) brought him immediate fame. "
            "He authored over two hundred fiction and non-fiction books, captivating generations of readers through iconic "
            "characters like Himu and Misir Ali. As a filmmaker, his masterpieces including 'Aguner Poroshmoni' and 'Srabon "
            "Megher Din' earned multiple National Film Awards. He breathed his last on 19 July 2012 in New York and was buried "
            "in his beloved Nuhash Palli."
        ),
        "info_table": {
            "headers": ["Who / Novelist", "Major Event / Landmark", "Year / Date", "Place / Achievement"],
            "rows": [
                ["Humayun Ahmed", "was born", "13 November 1948", "(i) [......]"],
                ["He", "published debut novel 'Nondito Noroke'", "(ii) [......]", "gained instant acclaim"],
                ["He", "obtained PhD in Chemistry", "during higher studies", "(iii) [......]"],
                ["His films like Aguner Poroshmoni", "won prestigious awards", "in cinema", "(iv) [......]"],
                ["The legendary writer", "passed away", "19 July 2012", "buried at (v) [......]"]
            ]
        },
        "answers": {
            "i": "Kutubpur, Netrokona",
            "ii": "in 1972",
            "iii": "North Dakota State University",
            "iv": "National Film Awards",
            "v": "Nuhash Palli (Gazipur)"
        },
        "model_summary": (
            "Humayun Ahmed (1948–2012) was a multifaceted Bangladeshi professor, literary maestro, and acclaimed filmmaker. "
            "Beginning with 'Nondito Noroke', his engaging storytelling and memorable fictional archetypes mesmerized "
            "millions of readers across decades. Furthermore, his cinematic ventures on the 1971 Liberation War earned "
            "national laurels, sealing his indelible status in the cultural heritage of Bangladesh."
        ),
        "vocab_notes": "Multifaceted -> Versatile; Maestro -> Master craftsman; Indelible -> Enduring."
    },
    {
        "id": 4,
        "slug_id": "unseen-04",
        "title": "Mughal Emperor Humayun: Triumph, Exile, and the Restoration of the Empire",
        "bn_title": "মুঘল সম্রাট হুমায়ূন: সিংহাসন লাভ, নির্বাসন ও সাম্রাজ্য পুনরুদ্ধার",
        "theme": "Mughal History / Emperor Humayun & Suri Conflict",
        "stars": "***",
        "priority": "Top Priority",
        "boards": "Dakhil Exam-2019",
        "page_pdf": 381,
        "passage": (
            "Humayun was the eldest son of Emperor Babur, the founder of the Mughal dynasty in India. Ascending the throne "
            "in 1530 at Agra, Humayun faced immense internal rivalry from his ambitious brothers and severe external threats "
            "from Afghan leaders. His most formidable adversary was Sher Shah Suri, who decisively defeated Humayun in the "
            "battles of Chausa (1539) and Kannauj (1540). Consequently, Humayun was driven into exile and took refuge in "
            "Persia. With the diplomatic and military backing of the Persian Shah Tahmasp, he recaptured Kabul and eventually "
            "re-established Mughal sovereignty over Delhi and Agra in 1555. However, he died shortly after in 1556 from a tragic library fall."
        ),
        "info_table": {
            "headers": ["Who / Emperor", "Historical Occurrence", "Year / Date", "Location / Result"],
            "rows": [
                ["Humayun", "ascended the Mughal throne", "1530", "(i) [......]"],
                ["(ii) [......]", "defeated Humayun in battles", "1539 and 1540", "at Chausa and Kannauj"],
                ["Humayun", "spent years in exile", "after 1540", "in (iii) [......]"],
                ["The Mughal ruler", "recaptured Delhi and Agra", "(iv) [......]", "restored Mughal rule"],
                ["Humayun", "died tragically", "1556", "by (v) [......]"]
            ]
        },
        "answers": {
            "i": "at Agra",
            "ii": "Sher Shah Suri",
            "iii": "Persia (Iran)",
            "iv": "in 1555",
            "v": "falling from his library stairs"
        },
        "model_summary": (
            "Emperor Humayun inherited the Mughal throne in 1530 but suffered devastating military setbacks against Afghan leader "
            "Sher Shah Suri, forcing him into a fifteen-year exile in Persia. Demonstrating remarkable resilience, he secured "
            "Persian allied support, reconquered Kabul, and triumphantly reclaimed the throne of Delhi in 1555. His perseverance "
            "paved the way for the golden era of the Mughal Empire under Akbar."
        ),
        "vocab_notes": "Ascended -> Assumed reign; Adversary -> Opponent; Resilience -> Tenacity."
    },
    {
        "id": 5,
        "slug_id": "unseen-05",
        "title": "Interpol: The International Criminal Police Organization and Global Justice",
        "bn_title": "ইন্টারপোল: আন্তর্জাতিক অপরাধ পুলিশ সংস্থা ও বৈশ্বিক নিরাপত্তা",
        "theme": "International Law, Transnational Policing & Global Security",
        "stars": "***",
        "priority": "Top Priority",
        "boards": "Dakhil Exam-2018",
        "page_pdf": 391,
        "passage": (
            "Interpol, officially known as the International Criminal Police Organization, is the world's largest intergovernmental "
            "police network. Established in 1923 at the International Police Congress in Vienna, its primary mission is to facilitate "
            "cross-border police cooperation to combat transnational crime, terrorism, human trafficking, and cyber offences. "
            "Headquartered in Lyon, France, Interpol operates National Central Bureaus (NCBs) in nearly two hundred member states. "
            "It does not possess executive arrest powers; rather, it issues Red Notices to alert law enforcement worldwide regarding "
            "wanted fugitives. In 1956, it adopted its modern constitution and official designation."
        ),
        "info_table": {
            "headers": ["Agency / Term", "Function / Landmark", "Year / Date", "City / Authority"],
            "rows": [
                ["Interpol", "was founded at Police Congress", "(i) [......]", "Vienna, Austria"],
                ["The organization", "established current headquarters", "modern era", "in (ii) [......]"],
                ["Interpol", "adopted its present constitution", "(iii) [......]", "as an international body"],
                ["(iv) [......]", "alerts global police forces", "regularly", "about wanted fugitives"],
                ["Member countries", "maintain police coordination", "worldwide", "through (v) [......]"]
            ]
        },
        "answers": {
            "i": "in 1923",
            "ii": "Lyon, France",
            "iii": "in 1956",
            "iv": "Red Notice",
            "v": "National Central Bureaus (NCBs)"
        },
        "model_summary": (
            "Interpol, established in Vienna in 1923 and headquartered in Lyon, is the premier intergovernmental organization "
            "coordinating international police efforts against transnational criminality. Connecting almost two hundred nations, "
            "it assists global law enforcement agencies by sharing intelligence and circulating Red Notices for fugitives. "
            "It functions as a vital cooperative bridge ensuring worldwide safety without infringing on state sovereignties."
        ),
        "vocab_notes": "Transnational -> Cross-border; Fugitives -> Wanted escapees; Intergovernmental -> Multi-nation."
    },
    {
        "id": 6,
        "slug_id": "unseen-06",
        "title": "Bir Shrestha Captain Mohiuddin Jahangir: The Hero of Chapainawabganj",
        "bn_title": "বীরশ্রেষ্ঠ ক্যাপ্টেন মহিউদ্দীন জাহাঙ্গীর: চাঁপাইনবাবগঞ্জের অমর যোদ্ধা",
        "theme": "Liberation War Hero / Bir Shrestha Supreme Sacrifice",
        "stars": "***",
        "priority": "Top Priority",
        "boards": "D.B. '24",
        "page_pdf": 393,
        "passage": (
            "Captain Mohiuddin Jahangir was one of the seven great martyrs honored with the highest gallantry award 'Bir Shrestha'. "
            "Born on 7 March 1949 at Rahimganj in Barishal, he joined the Pakistan Army Corps of Engineers in 1967. When the Liberation "
            "War commenced in 1971, he was posted in West Pakistan. Braving grave danger, he escaped across the border to join Sector 7 "
            "of the Mukti Bahini in the Rajshahi sector. He led numerous audacious raids against Pakistani entrenched positions. "
            "On 14 December 1971, just two days before final victory, he was martyred while leading a frontal assault across the Mahananda "
            "River in Chapainawabganj. He was laid to rest beside the historic Choto Sona Mosque."
        ),
        "info_table": {
            "headers": ["Who / Hero", "Military Feat / Event", "Year / Date", "Location / Honour"],
            "rows": [
                ["Mohiuddin Jahangir", "was born", "7 March 1949", "(i) [......]"],
                ["He", "escaped West Pakistan to join war", "1971", "joined (ii) [......]"],
                ["The courageous captain", "led fierce attacks", "December 1971", "along the (iii) [......]"],
                ["He", "embraced martyrdom in battle", "(iv) [......]", "Chapainawabganj"],
                ["He", "was buried with military honours", "after martyrdom", "near (v) [......]"]
            ]
        },
        "answers": {
            "i": "Rahimganj, Barishal",
            "ii": "Sector 7 of Mukti Bahini",
            "iii": "Mahananda River",
            "iv": "14 December 1971",
            "v": "Choto Sona Mosque"
        },
        "model_summary": (
            "Bir Shrestha Captain Mohiuddin Jahangir (1949–1971) was a legendary freedom fighter who defected from the Pakistan "
            "Army to command daring guerrilla operations in Sector 7 during the 1971 Liberation War. Displaying matchless courage, "
            "he spearheaded a decisive offensive across the Mahananda River on 14 December 1971 and made the supreme sacrifice. "
            "His unyielding patriotism remains an immortal beacon of national heroism."
        ),
        "vocab_notes": "Gallantry -> Supreme valour; Audacious -> Daring; Defected -> Broke allegiance."
    },
    {
        "id": 7,
        "slug_id": "unseen-07",
        "title": "Munier Chowdhury: Martyred Intellectual, Visionary Dramatist and Linguist",
        "bn_title": "মুনীর চৌধুরী: শহীদ বুদ্ধিজীবী, পথপ্রদর্শক নাট্যকার ও ভাষাবিদ",
        "theme": "Martyred Intellectual & Modern Bengali Drama",
        "stars": "**",
        "priority": "High Priority",
        "boards": "Standard Board Review",
        "page_pdf": 396,
        "passage": (
            "Munier Chowdhury was an eminent Bangladeshi dramatist, literary critic, and martyred intellectual. Born on "
            "27 November 1925 in Manikganj, he completed his higher education in English and Bengali at Dhaka University and "
            "Harvard University. A valiant participant in the Language Movement, he was incarcerated in 1952, during which he wrote "
            "his historic allegorical play 'Kabor' (The Grave). He also engineered the 'Munier Optima Keyboard', revolutionizing "
            "Bengali typewriter technology. On 14 December 1971, on the eve of national independence, he was abducted from his "
            "residence by the Al-Badr militia and brutally martyred at Rayerbazar killing grounds."
        ),
        "info_table": {
            "headers": ["Who / Intellectual", "Contribution / Occurrence", "Year / Era", "Place / Work"],
            "rows": [
                ["Munier Chowdhury", "was born", "27 November 1925", "(i) [......]"],
                ["He", "composed iconic drama 'Kabor'", "(ii) [......]", "while imprisoned in jail"],
                ["He", "developed Bengali typing layout", "mid-twentieth century", "named (iii) [......]"],
                ["The Al-Badr militia", "abducted the scholar", "(iv) [......]", "from his Dhaka home"],
                ["The martyred scholar", "was assassinated", "December 1971", "at (v) [......]"]
            ]
        },
        "answers": {
            "i": "Manikganj, Bangladesh",
            "ii": "in 1952 (or 1953 in prison)",
            "iii": "Munier Optima Keyboard",
            "iv": "14 December 1971",
            "v": "Rayerbazar killing field (Dhaka)"
        },
        "model_summary": (
            "Munier Chowdhury (1925–1971) was a towering Bengali playwright, linguistic reformer, and passionate advocate "
            "of linguistic autonomy who penned the masterpiece 'Kabor' during imprisonment for the Language Movement. "
            "His invention of the Optima keyboard modernized Bengali writing mechanization. Tragic victim of the targeted "
            "intellectual massacre on 14 December 1971, his progressive ideals remain immortal."
        ),
        "vocab_notes": "Incarcerated -> Imprisoned; Allegorical -> Symbolic; Autonomous -> Self-governing."
    },
    {
        "id": 8,
        "slug_id": "unseen-08",
        "title": "Bir Shrestha Munshi Abdur Rouf: Indomitable Valour at Burighat",
        "bn_title": "বীরশ্রেষ্ঠ মুন্সী আব্দুর রউফ: বুড়িঘাটের প্রতিরক্ষার অমর নায়ক",
        "theme": "Bir Shrestha / East Pakistan Rifles (EPR) & War Hero",
        "stars": "*",
        "priority": "Moderate",
        "boards": "Standard Board Review",
        "page_pdf": 398,
        "passage": (
            "Munshi Abdur Rouf was an iconic hero of Bangladesh's Liberation War who was posthumously decorated with 'Bir Shrestha'. "
            "Born on 1 May 1943 at Salamatpur in Faridpur, he joined the East Pakistan Rifles (EPR) in 1963. In April 1971, during "
            "the early weeks of the war, his unit was assigned to guard the strategic waterway at Burighat in the Chittagong Hill "
            "Tracts. When heavily armed Pakistani troops attacked their defensive positions with gunboats and mortars on 8 April 1971, "
            "Rouf single-handedly manned a machine gun, drawing enemy fire onto himself to enable his hundred comrades to retreat to safety. "
            "He was martyred by a mortar shell."
        ),
        "info_table": {
            "headers": ["Soldier / Hero", "Activity / Event", "Year / Date", "Location / Unit"],
            "rows": [
                ["Munshi Abdur Rouf", "was born", "1 May 1943", "(i) [......]"],
                ["He", "enlisted as a rifleman", "1963", "in (ii) [......]"],
                ["His company", "defended water channel", "April 1971", "at (iii) [......]"],
                ["Rouf", "fired heavy machine gun alone", "(iv) [......]", "to save fellow freedom fighters"],
                ["The brave warrior", "attained martyrdom", "8 April 1971", "buried at (v) [......]"]
            ]
        },
        "answers": {
            "i": "Salamatpur, Faridpur",
            "ii": "East Pakistan Rifles (EPR)",
            "iii": "Burighat, Rangamati",
            "iv": "8 April 1971",
            "v": "Naniarchar (Rangamati)"
        },
        "model_summary": (
            "Bir Shrestha Munshi Abdur Rouf demonstrated extraordinary heroism during the 1971 Liberation War at Burighat in "
            "the Chittagong Hill Tracts. Facing overwhelming enemy gunboats on 8 April 1971, he valiantly engaged the opposing "
            "forces single-handedly with a machine gun, sacrificing his life so that over a hundred comrades could withdraw safely. "
            "His unselfish martyrdom epitomizes supreme military bravery."
        ),
        "vocab_notes": "Single-handedly -> Unassisted; Retreat -> Strategic withdrawal; Epitomizes -> Personifies."
    },
    {
        "id": 9,
        "slug_id": "unseen-09",
        "title": "Louis Pasteur: Pioneer of Microbiology and the Saviour of Lives",
        "bn_title": "লুই পাস্তুর: অণুজীববিজ্ঞানের জনক ও প্রতিষেধকের পথপ্রদর্শক",
        "theme": "Science & Medicine / Germ Theory, Pasteurization & Rabies Vaccine",
        "stars": "*",
        "priority": "Moderate",
        "boards": "Standard Board Review",
        "page_pdf": 411,
        "passage": (
            "Louis Pasteur was a distinguished French chemist and microbiologist whose discoveries fundamentally transformed "
            "modern medicine and public health. Born on 27 December 1822 in Dole, France, he proved that microorganisms cause "
            "fermentation and disease, disproving the prevailing theory of spontaneous generation. He invented the process "
            "known as pasteurization, which kills harmful microbes in milk and wine by gentle heating. Pasteur later developed "
            "groundbreaking vaccines against anthrax, chicken cholera, and rabies. In 1885, he successfully saved a boy bitten by "
            "a rabid dog using his rabies vaccine. He passed away on 28 September 1895 at the age of 72."
        ),
        "info_table": {
            "headers": ["Scientist / Invention", "Scientific Milestone", "Year / Date", "Impact / Subject"],
            "rows": [
                ["Louis Pasteur", "was born", "27 December 1822", "in (i) [......]"],
                ["He", "disproved spontaneous generation", "mid-1800s", "through (ii) [......]"],
                ["Pasteurization", "was invented", "1860s", "to purify (iii) [......]"],
                ["Pasteur", "administered first rabies vaccine", "(iv) [......]", "saved a young boy"],
                ["The renowned scientist", "passed away", "28 September 1895", "at the age of (v) [......]"]
            ]
        },
        "answers": {
            "i": "Dole, France",
            "ii": "germ theory of disease",
            "iii": "milk and wine",
            "iv": "in 1885",
            "v": "72 years"
        },
        "model_summary": (
            "Louis Pasteur (1822–1895) was a seminal French microbiologist whose germ theory revolutionized medical science and "
            "sanitation. By developing pasteurization to eliminate pathogenic bacteria and pioneering vaccines for anthrax and rabies, "
            "he saved countless lives across the globe. His scientific breakthroughs laid the bedrock of modern immunology and "
            "preventive healthcare."
        ),
        "vocab_notes": "Fermentation -> Biochemical breakdown; Pathogenic -> Disease-causing; Seminal -> Highly influential."
    },
    {
        "id": 10,
        "slug_id": "unseen-10",
        "title": "Education: The Catalyst for Socio-Economic Transformation and Poverty Alleviation",
        "bn_title": "শিক্ষা: আর্থ-সামাজিক উন্নয়ন ও দারিদ্র্য বিমোচনের প্রধান চালিকাশক্তি",
        "theme": "Socio-Economic Development, Human Capital & Eradication of Poverty",
        "stars": "***",
        "priority": "Top Priority",
        "boards": "National Board Focus",
        "page_pdf": 422,
        "passage": (
            "Education plays an indispensable role in the socio-economic advancement of any nation. It enlightens the human mind, "
            "fosters rational thinking, and equips individuals with essential vocational and technological skills. In developing "
            "societies like Bangladesh, widespread literacy directly contributes to the eradication of poverty by enhancing "
            "employability and entrepreneurship. Educated citizens make informed choices regarding healthcare, civic responsibilities, "
            "and environmental sustainability. Moreover, female education has demonstrated unprecedented positive effects on reducing "
            "maternal mortality and boosting household earnings. Therefore, investing in inclusive and quality education is the most "
            "effective tool for sustainable national development."
        ),
        "info_table": {
            "headers": ["Concept / Factor", "Positive Influence", "Context / Area", "Outcome / Benefit"],
            "rows": [
                ["Education", "enlightens the human mind", "in society", "promotes (i) [......]"],
                ["Widespread literacy", "eradicates poverty", "in developing countries", "by increasing (ii) [......]"],
                ["Educated individuals", "make conscious decisions", "in daily life", "about (iii) [......]"],
                ["(iv) [......]", "lowers maternal mortality", "at family level", "boosts household income"],
                ["Quality education", "acts as vital catalyst", "nationwide", "for (v) [......]"]
            ]
        },
        "answers": {
            "i": "rational and progressive thinking",
            "ii": "employability and entrepreneurship",
            "iii": "healthcare and civic duties",
            "iv": "Female education",
            "v": "sustainable national development"
        },
        "model_summary": (
            "Education serves as the cornerstone of national progress, illuminating human intellect and cultivating technical competence. "
            "By empowering individuals with job skills and rational judgment, it directly alleviates poverty, improves public health "
            "awareness, and drives economic productivity. In particular, educating women yields profound familial and societal benefits, "
            "rendering educational investment vital for sustainable growth."
        ),
        "vocab_notes": "Indispensable -> Crucial; Alleviates -> Diminishes; Competence -> Capability."
    },
    {
        "id": 11,
        "slug_id": "unseen-11",
        "title": "Jibanananda Das: The Solitary Poet of Ruposhi Bangla and Modern Consciousness",
        "bn_title": "জীবনানন্দ দাশ: রূপসী বাংলার নির্জনতম আধুনিক কবি",
        "theme": "Bengali Poetry, Nature Imagery & Modernist Sensibility",
        "stars": "***",
        "priority": "Top Priority",
        "boards": "C.B. '24",
        "page_pdf": 425,
        "passage": (
            "Jibanananda Das was one of the foremost modernist poets in twentieth-century Bengali literature, celebrated as the "
            "'Poet of Beautiful Bengal' (Ruposhi Bangla). Born on 17 February 1899 in Barishal, he studied English literature at "
            "Presidency College, Kolkata, and taught at various institutions. Unlike his contemporaries, Das expressed a deeply "
            "introspective and melancholic connection with nature, employing haunting rural imagery, lush foliage, and historical "
            "allusions. His iconic poems, including 'Banalata Sen', 'Dhushor Pandulipi', and 'Banalata Sen', introduced surrealist "
            "and existential dimensions to Bengali poetry. He was struck by a tram in Kolkata and died on 22 October 1954."
        ),
        "info_table": {
            "headers": ["Poet / Scholar", "Life Event / Poetry Book", "Year / Date", "Place / Distinct Feature"],
            "rows": [
                ["Jibanananda Das", "was born", "17 February 1899", "in (i) [......]"],
                ["He", "studied English literature", "early 1920s", "at (ii) [......]"],
                ["(iii) [......]", "established his romantic fame", "modern era", "celebrated Bengali poem"],
                ["His unique poetry", "reflected rural beauty and sorrow", "twentieth century", "termed (iv) [......]"],
                ["The great poet", "passed away after tram injury", "(v) [......]", "in Kolkata"]
            ]
        },
        "answers": {
            "i": "Barishal, Bengal",
            "ii": "Presidency College, Kolkata",
            "iii": "Banalata Sen",
            "iv": "Ruposhi Bangla (Beautiful Bengal)",
            "v": "22 October 1954"
        },
        "model_summary": (
            "Jibanananda Das (1899–1954) was a preeminent modernist Bengali poet renowned for his poignant nature imagery and "
            "existential contemplation. Immortalizing the pastoral splendour of Bengal in collections like 'Ruposhi Bangla' and "
            "'Banalata Sen', he introduced novel surrealist metaphors into Bengali verse. His unique poetic voice captured both "
            "the sublime beauty of the rural landscape and modern human alienation."
        ),
        "vocab_notes": "Preeminent -> Foremost; Poignant -> Emotionally moving; Splendour -> Magnificent beauty."
    },
    {
        "id": 12,
        "slug_id": "unseen-12",
        "title": "Prophet Muhammad (Sm): Life, Sublime Character and Universal Teachings",
        "bn_title": "হযরত মুহাম্মদ (সা.): জীবনাদর্শ, অনুপম চরিত্র ও বৈশ্বিক দিকনির্দেশনা",
        "theme": "Islamic History / Life & Teachings of Prophet Muhammad (Sm)",
        "stars": "**",
        "priority": "High Priority",
        "boards": "Standard Islamic Review",
        "page_pdf": 426,
        "passage": (
            "Hazrat Muhammad (Sm) is the last and greatest prophet of Islam, whose life exemplifies supreme integrity, justice, "
            "and compassion. Born in 570 CE in Makkah into the noble Quraish tribe, he was orphaned in early childhood. Known "
            "throughout Arabia as 'Al-Amin' (The Trustworthy) for his immaculate honesty, he received divine revelation at the "
            "age of forty in the Cave of Hira. Facing persecution from Makkan pagans, he migrated to Madinah in 622 CE (The Hijrah), "
            "where he established a model welfare state based on the Charter of Madinah. He championed human equality, women's "
            "rights, and racial harmony until his demise in 632 CE."
        ),
        "info_table": {
            "headers": ["Entity / Prophet", "Landmark Event", "Year / Age", "Location / Significance"],
            "rows": [
                ["Hazrat Muhammad (Sm)", "was born into Quraish clan", "570 CE", "in (i) [......]"],
                ["He", "was bestowed title 'Al-Amin'", "youth", "due to (ii) [......]"],
                ["The Prophet", "received first revelation", "(iii) [......]", "in the Cave of Hira"],
                ["He", "migrated to Madinah", "622 CE", "marked as (iv) [......]"],
                ["He", "formulated Charter of Madinah", "seventh century", "to ensure (v) [......]"]
            ]
        },
        "answers": {
            "i": "Makkah, Arabia",
            "ii": "his honesty and truthfulness",
            "iii": "at the age of forty (610 CE)",
            "iv": "the Hijrah",
            "v": "harmony, equality, and civic rights"
        },
        "model_summary": (
            "Prophet Muhammad (Sm) (570–632 CE) transformed human society through an unblemished character grounded in truthfulness, "
            "justice, and universal mercy. Receiving divine prophethood at forty, he endured severe hardships before establishing "
            "the pioneering democratic commonwealth in Madinah. His teachings dismantled racial stratification, protected minority "
            "liberties, and laid timeless moral codes for humanity."
        ),
        "vocab_notes": "Unblemished -> Pure and flawless; Prophethood -> Divine mission; Stratification -> Social division."
    },
    {
        "id": 13,
        "slug_id": "unseen-13",
        "title": "Liberation War of Bangladesh: The Sacred Heritage of Victory Day (16 December)",
        "bn_title": "বাংলাদেশের মুক্তিযুদ্ধ: ১৬ই ডিসেম্বর মহান বিজয় দিবসের চেতনা",
        "theme": "National Sovereignty, 1971 Liberation War & Victory Day",
        "stars": "*",
        "priority": "Moderate",
        "boards": "Standard Board Review",
        "page_pdf": 431,
        "passage": (
            "Bangladesh emerged as an independent sovereign nation through an epic nine-month armed struggle in 1971. Following the "
            "brutal genocide initiated on 25 March by the Pakistani occupation forces, the freedom-loving people of Bangladesh "
            "rallied under the inspiring leadership of Bangabandhu Sheikh Mujibur Rahman. The Mukti Bahini, composed of students, "
            "farmers, soldiers, and ordinary citizens, waged heroic guerrilla warfare across all sectors. Finally, on 16 December 1971, "
            "over ninety thousand Pakistani troops surrendered unconditionally at the historic Suhrawardy Udyan in Dhaka. Thus, "
            "16 December is proudly celebrated as our glorious Victory Day, commemorating the supreme sacrifice of three million martyrs."
        ),
        "info_table": {
            "headers": ["Force / People", "Historical Milestone", "Year / Date", "Place / Consequence"],
            "rows": [
                ["Pakistani military", "launched brutal genocide", "25 March 1971", "across (i) [......]"],
                ["Freedom fighters", "formed Mukti Bahini", "1971", "under (ii) [......]"],
                ["The Bengali nation", "fought bravely for nine months", "from March to December", "to achieve (iii) [......]"],
                ["Pakistani troops", "signed instrument of surrender", "(iv) [......]", "at Suhrawardy Udyan"],
                ["Bangladesh", "celebrates Victory Day", "16 December", "in honour of (v) [......]"]
            ]
        },
        "answers": {
            "i": "East Pakistan (Bangladesh)",
            "ii": "the leadership of Bangabandhu",
            "iii": "sovereign national independence",
            "iv": "16 December 1971",
            "v": "three million martyrs"
        },
        "model_summary": (
            "Bangladesh achieved national liberation in 1971 following a grueling nine-month war of independence against oppressive "
            "occupation forces. Led by the resolute spirit of Bangabandhu, courageous freedom fighters resisted tenaciously across "
            "the country until the historic surrender of Pakistani forces on 16 December 1971. Victory Day stands as an enduring "
            "symbol of boundless patriotism and ultimate sacrifice."
        ),
        "vocab_notes": "Sovereign -> Autonomous; Grueling -> Exhausting and demanding; Resolute -> Determined."
    },
    {
        "id": 14,
        "slug_id": "unseen-14",
        "title": "Charles Babbage: The Visionary Father of the Modern Computing Era",
        "bn_title": "চার্লস ব্যাবেজ: আধুনিক কম্পিউটার বিজ্ঞানের স্বপ্নদ্রষ্টা ও জনক",
        "theme": "History of Science / Father of the Computer & Analytical Engine",
        "stars": "**",
        "priority": "High Priority",
        "boards": "J.B. '24, B.B. '19, '25",
        "page_pdf": 435,
        "passage": (
            "Charles Babbage was an illustrious English mathematician, philosopher, and mechanical engineer widely recognized "
            "as the 'Father of the Computer'. Born on 26 December 1791 in London, he studied mathematics at Trinity College, Cambridge. "
            "Frustrated by pervasive human errors in manual mathematical tables, Babbage conceived the 'Difference Engine' in 1822 "
            "to automate complex calculations. Later, he conceptualized the revolutionary 'Analytical Engine', which incorporated "
            "an arithmetic logic unit, conditional branching, and memory storage using punch cards—features that mirror modern "
            "digital computers. Collaborating with Ada Lovelace, the first computer programmer, Babbage laid computing's architectural "
            "foundation before his death on 18 October 1871."
        ),
        "info_table": {
            "headers": ["Scholar / Machine", "Inventive Breakthrough", "Year / Date", "Impact / Mechanism"],
            "rows": [
                ["Charles Babbage", "was born", "26 December 1791", "in (i) [......]"],
                ["He", "graduated with honors", "early 19th century", "from (ii) [......]"],
                ["Difference Engine", "was designed to compute tables", "(iii) [......]", "without manual errors"],
                ["Analytical Engine", "featured memory and ALU", "1830s-1840s", "using (iv) [......]"],
                ["The pioneer inventor", "died in London", "(v) [......]", "at the age of 79"]
            ]
        },
        "answers": {
            "i": "London, England",
            "ii": "Cambridge University",
            "iii": "in 1822",
            "iv": "punched card technology",
            "v": "18 October 1871"
        },
        "model_summary": (
            "Charles Babbage (1791–1871) was a pioneering English polymath who originated the core principles of programmable computing. "
            "Driven by a desire to eliminate manual calculation errors, he conceived the Difference Engine and the far more versatile "
            "Analytical Engine. His inclusion of memory, input, and processing units anticipated the foundational architecture of "
            "today's digital computing age."
        ),
        "vocab_notes": "Polymath -> Multi-disciplinary genius; Versatile -> Adaptable; Anticipated -> Foretold."
    },
    {
        "id": 15,
        "slug_id": "unseen-15",
        "title": "Dr. Muhammad Qudrat-i-Khuda: Eminent Chemist, Researcher and Educationist",
        "bn_title": "ড. মুহম্মদ কুদরাত-এ-খুদা: প্রথিতযশা বিজ্ঞানী, গবেষক ও শিক্ষাবিদ",
        "theme": "Eminent Scientist / Indigenous Scientific Research & National Education",
        "stars": "*",
        "priority": "Moderate",
        "boards": "Dinj.B. '24",
        "page_pdf": 436,
        "passage": (
            "Dr. Muhammad Qudrat-i-Khuda was a preeminent Bengali chemist, educationist, and scientific visionary who championed "
            "indigenous research in undivided Bengal and Bangladesh. Born on 1 December 1900 in Birbhum, West Bengal, he obtained "
            "his Doctorate of Science from the University of London in 1929. He conducted groundbreaking research on natural "
            "products, extracting biochemical compounds from local herbs, jute, and molasses. Following national independence, "
            "Bangabandhu appointed him chairman of the National Education Commission in 1972, which drafted a modern scientific "
            "curriculum known as the 'Qudrat-i-Khuda Education Commission Report'. He was awarded the Ekushey Padak in 1976 and "
            "Independence Award in 1984."
        ),
        "info_table": {
            "headers": ["Scientist / Leader", "Academic Feat / Post", "Year / Date", "Institution / Award"],
            "rows": [
                ["Dr. Qudrat-i-Khuda", "was born", "1 December 1900", "in (i) [......]"],
                ["He", "earned DSc in Chemistry", "(ii) [......]", "from University of London"],
                ["He", "investigated indigenous resources", "career", "such as (iii) [......]"],
                ["The chemist", "led National Education Commission", "(iv) [......]", "to reform curriculum"],
                ["He", "received Independence Award", "1984", "for (v) [......]"]
            ]
        },
        "answers": {
            "i": "Birbhum, West Bengal",
            "ii": "in 1929",
            "iii": "jute, herbs, and molasses",
            "iv": "in 1972 (under Bangabandhu)",
            "v": "lifelong contribution to science and education"
        },
        "model_summary": (
            "Dr. Muhammad Qudrat-i-Khuda (1900–1977) was a distinguished chemist who dedicated his career to applying scientific "
            "innovation to domestic agricultural products like jute and medicinal plants. Appointed in 1972 by Bangabandhu to direct "
            "the National Education Commission, he formulated a progressive, secular, and science-oriented educational roadmap for "
            "the newly independent nation."
        ),
        "vocab_notes": "Indigenous -> Native/local; Formulated -> Devised; Progressive -> Forward-looking."
    },
    {
        "id": 16,
        "slug_id": "unseen-16",
        "title": "Tourism in Bangladesh: Natural Wonders, Heritage Sites and Economic Prospects",
        "bn_title": "বাংলাদেশের পর্যটন শিল্প: প্রাকৃতিক সৌন্দর্য, ঐতিহাসিক নিদর্শন ও অর্থনৈতিক সম্ভাবনা",
        "theme": "Heritage Tourism, Sundarbans, Cox's Bazar & Economic Growth",
        "stars": "*",
        "priority": "Moderate",
        "boards": "Standard Board Review",
        "page_pdf": 440,
        "passage": (
            "Tourism in Bangladesh is an expanding economic sector blessed with an extraordinary blend of natural wonders and "
            "historical architecture. The country boasts Cox's Bazar, the longest unbroken natural sea beach in the world, stretching "
            "over 120 kilometers along the Bay of Bengal. In the southwest lies the Sundarbans, the world's largest mangrove forest "
            "and a UNESCO World Heritage Site, home to the Royal Bengal Tiger and diverse wildlife. In addition, archaeological "
            "jewels like the sixty-domed Shat Gombuj Mosque in Bagerhat, Buddhist Viharas in Paharpur, and tea gardens in Sylhet "
            "attract local and global travellers. Modernizing infrastructure and eco-friendly hospitality can establish tourism as "
            "a premier foreign exchange earner."
        ),
        "info_table": {
            "headers": ["Destination / Wonder", "Distinguishing Feature", "Location / Scope", "Global Recognition"],
            "rows": [
                ["Cox's Bazar", "longest natural sea beach", "(i) [......]", "120 km unbroken coastline"],
                ["The Sundarbans", "largest mangrove forest", "south-west Bangladesh", "(ii) [......]"],
                ["(iii) [......]", "houses Royal Bengal Tiger", "Sundarbans delta", "unique ecosystem"],
                ["Shat Gombuj Mosque", "medieval architectural marvel", "Bagerhat", "(iv) [......]"],
                ["Tourism industry", "boosts foreign exchange", "nationwide", "requires (v) [......]"]
            ]
        },
        "answers": {
            "i": "along the Bay of Bengal",
            "ii": "UNESCO World Heritage Site",
            "iii": "Mangrove wildlife",
            "iv": "historical Islamic monument",
            "v": "modern infrastructure and eco-tourism"
        },
        "model_summary": (
            "Bangladesh possesses tremendous tourism potential, ranging from Cox's Bazar's expansive sandy coastline to the "
            "biodiverse mangrove labyrinths of the Sundarbans. Furthermore, historic UNESCO sites like Bagerhat's Shat Gombuj Mosque "
            "and Paharpur's Buddhist monuments showcase centuries of rich cultural heritage. Upgrading transport infrastructure and "
            "promoting sustainable eco-tourism will substantially accelerate national foreign currency earnings."
        ),
        "vocab_notes": "Biodiverse -> Ecologically varied; Expansive -> Vast; Substantially -> Significantly."
    },
    {
        "id": 17,
        "slug_id": "unseen-17",
        "title": "Sir Jagadish Chandra Bose: Pioneer of Plant Physiology and Millimeter Radio Waves",
        "bn_title": "স্যার জগদীশ চন্দ্র বসু: উদ্ভিদ শারীরতত্ত্ব ও বেতার তরঙ্গের পথিকৃৎ",
        "theme": "Biophysics, Botany / Crescograph & Wireless Communication",
        "stars": "*",
        "priority": "Moderate",
        "boards": "Standard Board Review",
        "page_pdf": 443,
        "passage": (
            "Sir Jagadish Chandra Bose was a legendary Bengali polymath who pioneered wireless telecommunication and plant "
            "physiology. Born on 30 November 1858 in Munshiganj, he obtained degrees from Cambridge University and the University "
            "of London. In 1895, Bose demonstrated the transmission of microwave radio waves in Kolkata, predating Guglielmo Marconi's "
            "public experiments, yet he refused to patent his work, believing knowledge should benefit humanity freely. Later, he "
            "shifted focus to biophysics and invented the 'Crescograph', a delicate device capable of measuring microscopic plant "
            "growth. Through it, he demonstrated that plants possess responsive nervous systems and experience pain. He founded the "
            "Bose Institute in 1917."
        ),
        "info_table": {
            "headers": ["Scientist / Invention", "Scientific Discovery", "Year / Date", "Field / Impact"],
            "rows": [
                ["Jagadish Chandra Bose", "was born", "30 November 1858", "in (i) [......]"],
                ["He", "demonstrated microwave radio waves", "(ii) [......]", "in Kolkata"],
                ["(iii) [......]", "measured minute plant growth", "early 20th century", "invented by Bose"],
                ["His biological studies", "proved plants feel sensation", "experimental research", "in (iv) [......]"],
                ["The scientist", "established Bose Institute", "(v) [......]", "for higher scientific research"]
            ]
        },
        "answers": {
            "i": "Munshiganj, Bengal",
            "ii": "in 1895",
            "iii": "The Crescograph",
            "iv": "plant physiology and biophysics",
            "v": "in 1917 (Kolkata)"
        },
        "model_summary": (
            "Sir Jagadish Chandra Bose (1858–1937) was an extraordinary Bengali scientist whose investigations encompassed both "
            "physics and botanical physiology. After successfully demonstrating millimeter radio transmissions in 1895, he invented "
            "the Crescograph, conclusively proving that plants exhibit emotional and physiological responses to stimuli. His unselfish "
            "refusal to commercialize patents exemplifies true scientific idealism."
        ),
        "vocab_notes": "Polymath -> Multi-talented genius; Stimuli -> External impulses; Conclusively -> Decisively."
    },
    {
        "id": 18,
        "slug_id": "unseen-18",
        "title": "Geography, Heritage and Economy of South Asia: The Bangladesh Context",
        "bn_title": "দক্ষিণ এশিয়ার ভূগোল, ঐতিহ্য ও অর্থনীতি: বাংলাদেশের প্রেক্ষাপট",
        "theme": "South Asian Geography, River Delta & Economic Interdependence",
        "stars": "*",
        "priority": "Moderate",
        "boards": "Standard Board Review",
        "page_pdf": 445,
        "passage": (
            "Bangladesh occupies a strategic geopolitical location in South Asia, nestled in the deltaic confluence of the Ganges, "
            "Brahmaputra, and Meghna rivers. Bordered primarily by India, with Myanmar to the southeast and the Bay of Bengal to the "
            "south, the country features the world's largest active delta. South Asian nations share deep historical, linguistic, "
            "and ecological affinities, while simultaneously managing common challenges like river water distribution, monsoon "
            "flooding, and climate change. Bangladesh has transformed its agrarian economy into a dynamic manufacturing hub, "
            "principally via ready-made garments (RMG) and remittance inflows, cementing vital bilateral trade ties across the region."
        ),
        "info_table": {
            "headers": ["Entity / Region", "Geographical / Economic Trait", "Boundary / River", "Strategic Outcome"],
            "rows": [
                ["Bangladesh", "forms world's largest delta", "(i) [......]", "rich agricultural plains"],
                ["The country", "shares land borders", "on three sides", "with (ii) [......]"],
                ["South Asian countries", "face shared vulnerabilities", "monsoon season", "like (iii) [......]"],
                ["(iv) [......]", "fuels national foreign exchange", "modern era", "along with remittance"],
                ["Regional commerce", "connects South Asian markets", "Bay of Bengal region", "promotes (v) [......]"]
            ]
        },
        "answers": {
            "i": "Ganges-Brahmaputra-Meghna basin",
            "ii": "India and Myanmar",
            "iii": "floods and climate change",
            "iv": "Ready-Made Garments (RMG)",
            "v": "economic interdependence and growth"
        },
        "model_summary": (
            "Situated across the fertile delta of major river systems, Bangladesh holds an essential geopolitical position within "
            "South Asia. While confronting seasonal climate hazards alongside neighbouring countries, it has rapidly diversified "
            "from an agrarian base into an industrial apparel powerhouse. Expanding cross-border commerce and resource sharing "
            "remains fundamental to mutual regional prosperity."
        ),
        "vocab_notes": "Geopolitical -> Strategic regional; Confluence -> Junction of waters; Diversified -> Expanded."
    },
    {
        "id": 19,
        "slug_id": "unseen-19",
        "title": "Dr. APJ Abdul Kalam: The Missile Man, Inspirational Scientist and People's President",
        "bn_title": "ড. এ পি জে আবদুল কালাম: মিসাইল ম্যান ও প্রজাবৎসল রাষ্ট্রপতি",
        "theme": "Scientific Innovation, Aerospace & Youth Inspiration",
        "stars": "***",
        "priority": "Top Priority",
        "boards": "Standard Board Review",
        "page_pdf": 459,
        "passage": (
            "Dr. APJ Abdul Kalam was an esteemed Indian aerospace scientist and statesman who served as the 11th President "
            "of India from 2002 to 2007. Born on 15 October 1931 in Rameswaram, Tamil Nadu, into a modest boatman's family, he "
            "funded his education through arduous paper distribution. Joining the Defence Research and Development Organisation (DRDO) "
            "and Indian Space Research Organisation (ISRO), he played a pivotal role in developing ballistic missiles like Agni and "
            "Prithvi, earning the sobriquet 'Missile Man of India'. Renowned for his humility, vegetarian lifestyle, and passion for "
            "youth education, his autobiography 'Wings of Fire' inspired millions worldwide. He died while lecturing students on 27 July 2015."
        ),
        "info_table": {
            "headers": ["Statesman / Scientist", "Landmark Contribution", "Year / Date", "Location / Organisation"],
            "rows": [
                ["APJ Abdul Kalam", "was born into humble family", "15 October 1931", "at (i) [......]"],
                ["He", "engineered launch vehicles & missiles", "late 20th century", "at (ii) [......]"],
                ["He", "earned the prestigious moniker", "scientific career", "named (iii) [......]"],
                ["Dr. Kalam", "served as President of India", "(iv) [......]", "known as People's President"],
                ["The beloved teacher", "collapsed while addressing students", "27 July 2015", "in (v) [......]"]
            ]
        },
        "answers": {
            "i": "Rameswaram, Tamil Nadu",
            "ii": "DRDO and ISRO",
            "iii": "'Missile Man of India'",
            "iv": "from 2002 to 2007",
            "v": "Shillong, Meghalaya"
        },
        "model_summary": (
            "Dr. APJ Abdul Kalam (1931–2015) rose from humble origins in Rameswaram to become India's foremost aerospace scientist "
            "and 11th President. Renowned as the 'Missile Man' for spearheading indigenous space and defense programs, his life "
            "epitomized simplicity, dedication, and unyielding optimism. He devoted his presidency and post-tenure years to motivating "
            "young generations toward scientific pursuit and ethical nation-building."
        ),
        "vocab_notes": "Sobriquet -> Popular nickname; Epitomized -> Personified; Indigenous -> Domestically developed."
    },
    {
        "id": 20,
        "slug_id": "unseen-20",
        "title": "Begum Sufia Kamal: Pioneering Poet, Social Reformer and Champion of Women's Rights",
        "bn_title": "বেগম সুফিয়া কামাল: জননী সাহসিকা ও নারী জাগরণের অগ্রদূত",
        "theme": "Pioneering Female Poet, Women's Rights & Democratic Movements",
        "stars": "***",
        "priority": "Top Priority",
        "boards": "Standard Board Review",
        "page_pdf": 463,
        "passage": (
            "Begum Sufia Kamal was a revered Bangladeshi poet, pioneering social activist, and fearless champion of women's "
            "emancipation. Born on 20 June 1911 in Shayestabad, Barishal, she was deprived of formal institutional schooling due "
            "to conservative societal conventions. Nevertheless, she mastered Bengali, English, and Urdu independently at home. "
            "Encouraged by Begum Rokeya and Rabindranath Tagore, she penned emotive verses celebrating nature, humanity, and social "
            "justice. Sufia Kamal actively participated in the 1952 Language Movement, the 1969 Mass Uprising, and the 1971 Liberation War. "
            "She founded the 'Bangladesh Mahila Parishad' to defend women's dignity. She passed away on 20 November 1999."
        ),
        "info_table": {
            "headers": ["Activist / Poet", "Historic Involvement", "Year / Date", "Field / Organization"],
            "rows": [
                ["Begum Sufia Kamal", "was born", "20 June 1911", "in (i) [......]"],
                ["She", "learned literature self-taught", "childhood", "inspired by (ii) [......]"],
                ["She", "rallied democratic movements", "1952 and 1969", "for (iii) [......]"],
                ["The iconic leader", "founded premier women's body", "1970", "named (iv) [......]"],
                ["The venerable poet", "passed away in Dhaka", "(v) [......]", "honoured as Jononi Sahosika"]
            ]
        },
        "answers": {
            "i": "Shayestabad, Barishal",
            "ii": "Begum Rokeya and Tagore",
            "iii": "mother language and civil rights",
            "iv": "Bangladesh Mahila Parishad",
            "v": "20 November 1999"
        },
        "model_summary": (
            "Begum Sufia Kamal (1911–1999) overcame rigid social orthodoxies through domestic self-education to emerge as a prominent "
            "poet and women's rights pioneer in Bangladesh. A courageous civic voice, she stood at the forefront of the Language Movement, "
            "democratic uprisings, and the 1971 Liberation War. Through the establishment of the Mahila Parishad, she created an "
            "enduring framework for female empowerment."
        ),
        "vocab_notes": "Emancipation -> Liberation; Orthodoxy -> Rigid conservatism; Venerable -> Deeply respected."
    },
    {
        "id": 21,
        "slug_id": "unseen-21",
        "title": "The Nobel Prize and Wilhelm Röntgen's Epochal Discovery of X-rays",
        "bn_title": "নোবেল পুরস্কার ও উইলহেম রন্টজেনের এক্স-রে আবিষ্কার",
        "theme": "Global Laureates, Physics & Invention of X-rays",
        "stars": "***",
        "priority": "Top Priority",
        "boards": "Standard Board Review",
        "page_pdf": 464,
        "passage": (
            "The Nobel Prize is widely acknowledged as the world's most prestigious intellectual accolade, established in "
            "accordance with the 1895 will of Swedish industrialist and dynamite inventor Alfred Nobel. Commencing in 1901, "
            "Nobel Prizes are conferred annually in Physics, Chemistry, Physiology or Medicine, Literature, and Peace (with Economics "
            "added in 1968). The very first Nobel Prize in Physics in 1901 was awarded to German physicist Wilhelm Conrad Röntgen "
            "for his accidental discovery of X-rays in 1895. Röntgen observed mysterious fluorescent rays that could penetrate "
            "opaque paper and human flesh, capturing the iconic skeletal radiograph of his wife's hand. He generously refused "
            "to patent X-rays so that medical diagnostics could flourish freely."
        ),
        "info_table": {
            "headers": ["Entity / Scientist", "Discovery / Achievement", "Year / Date", "Discipline / Impact"],
            "rows": [
                ["Alfred Nobel", "bequeathed his fortune in will", "1895", "for (i) [......]"],
                ["Nobel Prizes", "were inaugurated globally", "(ii) [......]", "in five original categories"],
                ["Wilhelm Röntgen", "detected mysterious rays", "1895", "named (iii) [......]"],
                ["Röntgen", "won inaugural Nobel Prize", "1901", "in (iv) [......]"],
                ["The German physicist", "renounced patent rights", "after discovery", "to enable (v) [......]"]
            ]
        },
        "answers": {
            "i": "international awards for human benefit",
            "ii": "in 1901",
            "iii": "X-rays (electromagnetic radiation)",
            "iv": "Physics",
            "v": "free medical diagnostic progress"
        },
        "model_summary": (
            "Inaugurated in 1901 pursuant to Alfred Nobel's testamentary bequest, the Nobel Prizes celebrate transformative human "
            "accomplishments across science, literature, and peace. The premier Physics award honored Wilhelm Conrad Röntgen for "
            "his 1895 discovery of penetrating X-rays. Exemplifying profound scientific altruism, Röntgen declined commercial "
            "patents, thereby revolutionizing clinical radiology and diagnostic healthcare for worldwide humanity."
        ),
        "vocab_notes": "Accolade -> Esteemed recognition; Altruism -> Selfless philanthropy; Radiograph -> Photographic X-ray."
    },
    {
        "id": 22,
        "slug_id": "unseen-22",
        "title": "Mount Everest: Hillary, Tenzing and the Conquest of the World's Summit",
        "bn_title": "মাউন্ট এভারেস্ট: হিলারি, তেনজিং ও পৃথিবীর শীর্ষ বিজয়",
        "theme": "Mountaineering, Himalayan Peaks & Extreme Human Endurance",
        "stars": "*",
        "priority": "Moderate",
        "boards": "D. B. '26",
        "page_pdf": 470,
        "passage": (
            "Mount Everest, standing majestically at 8,848.86 meters above sea level in the Mahalangur Himal sub-range of the "
            "Himalayas, is the highest peak on Earth. Known as 'Sagarmatha' in Nepal and 'Chomolungma' in Tibet, its perilous "
            "altitude, treacherous icefalls, and biting sub-zero temperatures defeated numerous mountaineering expeditions for decades. "
            "However, on 29 May 1953, New Zealand climber Edmund Hillary and Nepali Sherpa Tenzing Norgay achieved the first verified "
            "summit climb via the South Col route. Reaching the peak at 11:30 AM, they spent fifteen memorable minutes taking "
            "photographs and offering sweets. Their historic ascent proved that human perseverance can master nature's fiercest barriers."
        ),
        "info_table": {
            "headers": ["Peak / Climber", "Ascent / Expedition Detail", "Year / Date", "Altitude / Route"],
            "rows": [
                ["Mount Everest", "is the tallest peak on Earth", "permanent", "elevated at (i) [......]"],
                ["The peak", "is called 'Sagarmatha'", "locally", "in (ii) [......]"],
                ["Hillary and Tenzing", "stepped onto the summit", "(iii) [......]", "via South Col route"],
                ["The triumphant climbers", "remained at the peak", "11:30 AM", "for (iv) [......]"],
                ["Their historic triumph", "inspired global mountaineering", "1953 onward", "symbolized (v) [......]"]
            ]
        },
        "answers": {
            "i": "8,848.86 meters",
            "ii": "Nepal",
            "iii": "29 May 1953",
            "iv": "fifteen minutes",
            "v": "boundless human perseverance"
        },
        "model_summary": (
            "Mount Everest, situated in the Himalayas as Earth's loftiest summit, long resisted human exploration due to its lethal "
            "conditions and extreme cold. On 29 May 1953, Edmund Hillary and Tenzing Norgay triumphed over the forbidding terrain, "
            "attaining the apex via the South Col. Their monumental feat demonstrated that discipline, meticulous preparation, and "
            "indomitable fortitude can conquer nature's most daunting physical frontiers."
        ),
        "vocab_notes": "Loftiest -> Highest; Forbidding -> Hostile and menacing; Fortitude -> Mental courage."
    },
    {
        "id": 23,
        "slug_id": "unseen-23",
        "title": "Sher-e-Bangla A.K. Fazlul Huq: Voice of the Peasants and Bengal Statesman",
        "bn_title": "শেরে বাংলা এ কে ফজলুল হক: কৃষক-প্রজার কণ্ঠস্বর ও অবিসংবাদিত নেতা",
        "theme": "Historic Statesman, Bengal Debt Settlement & Educational Reform",
        "stars": "***",
        "priority": "Top Priority",
        "boards": "Syl. B. '24",
        "page_pdf": 472,
        "passage": (
            "Abul Kashem Fazlul Huq, universally acclaimed as 'Sher-e-Bangla' (The Tiger of Bengal), was an illustrious political "
            "statesman, orator, and advocate of the oppressed peasant masses. Born on 26 October 1873 in Saturia, Jhalokati, he earned "
            "degrees in mathematics, physics, and law with distinction. Founding the Krishak Proja Party, he championed peasant rights "
            "and served as the first Prime Minister of undivided Bengal in 1937. He enacted the revolutionary 'Bengal Agricultural "
            "Debtors Act' (1938), emancipating millions of poor peasants from the predatory clutches of moneylenders (Mahajans). "
            "A tireless education reformer, he established Islamia College in Kolkata and Eden Girls' College in Dhaka. He passed away on 27 April 1962."
        ),
        "info_table": {
            "headers": ["Statesman / Reformer", "Historic Role / Legislation", "Year / Date", "Place / Beneficiaries"],
            "rows": [
                ["A.K. Fazlul Huq", "was born", "26 October 1873", "in (i) [......]"],
                ["He", "formed Krishak Proja Party", "early 20th century", "to defend (ii) [......]"],
                ["Sher-e-Bangla", "governed as Prime Minister of Bengal", "(iii) [......]", "in undivided Bengal"],
                ["Agricultural Debtors Act", "relieved peasant indebtedness", "1938", "from exploitative (iv) [......]"],
                ["The venerable leader", "passed away in Dhaka", "(v) [......]", "mourned by the whole nation"]
            ]
        },
        "answers": {
            "i": "Saturia, Jhalokati",
            "ii": "peasant and tenant rights",
            "iii": "in 1937",
            "iv": "moneylenders (Mahajans)",
            "v": "27 April 1962"
        },
        "model_summary": (
            "Sher-e-Bangla A.K. Fazlul Huq (1873–1962) was a legendary Bengali statesman and orator who dedicated his political "
            "leadership to emancipating marginalized agrarian tenants. As the premier of undivided Bengal, he instituted the landmark "
            "Agricultural Debtors Act, rescuing impoverished farmers from debt slavery. Furthermore, his establishment of premier "
            "colleges democratized higher education for underrepresented communities."
        ),
        "vocab_notes": "Emancipating -> Liberating; Marginalized -> Disadvantaged; Landmark -> Historic turning point."
    },
    {
        "id": 24,
        "slug_id": "unseen-24",
        "title": "Hazrat Ali (R): Fourth Caliph of Islam, Exemplar of Wisdom and Chivalry",
        "bn_title": "হযরত আলী (রা.): ইসলামের চতুর্থ খলিফা, জ্ঞান ও বীরত্বের প্রতীক",
        "theme": "Islamic History / Caliphate, Wisdom & Valor in Islam",
        "stars": "*",
        "priority": "Moderate",
        "boards": "C.B. '15",
        "page_pdf": 475,
        "passage": (
            "Hazrat Ali (R) was the cousin, son-in-law, and close companion of Prophet Muhammad (Sm), as well as the fourth "
            "Rightly Guided Caliph of Islam. Born in Makkah inside the sacred Kaaba around 600 CE, he was the first youth to accept "
            "Islam at the dawn of revelation. Renowned for his fearless valor on the battlefield, he earned the title 'Asadullah' "
            "(The Lion of Allah) for his legendary prowess at the Battle of Khaybar. Equally celebrated for profound judicial intellect, "
            "Prophet Muhammad (Sm) proclaimed: 'I am the city of knowledge, and Ali is its gate.' Assuming the Caliphate in 656 CE, "
            "he governed with strict justice until his martyrdom on 21 Ramadan (27 January 661 CE) in Kufa."
        ),
        "info_table": {
            "headers": ["Entity / Companion", "Distinction / Event", "Year / Date", "Location / Title"],
            "rows": [
                ["Hazrat Ali (R)", "was born inside Kaaba", "circa 600 CE", "at (i) [......]"],
                ["He", "embraced Islam in early youth", "610 CE", "first among (ii) [......]"],
                ["The brave warrior", "captured fortress of Khaybar", "early Islamic era", "earned title (iii) [......]"],
                ["Hazrat Ali (R)", "assumed the Caliphate", "(iv) [......]", "fourth Caliph of Islam"],
                ["The Caliph", "embraced martyrdom", "27 January 661 CE", "in (v) [......]"]
            ]
        },
        "answers": {
            "i": "Makkah, Arabia",
            "ii": "youths / children",
            "iii": "'Asadullah' (Lion of Allah)",
            "iv": "in 656 CE",
            "v": "Kufa (Iraq)"
        },
        "model_summary": (
            "Hazrat Ali (R) (600–661 CE) was an iconic figure in Islamic history revered for his unmatched physical bravery and "
            "deep philosophical wisdom. Embracing the faith in his boyhood, he defended the nascent Islamic community gallantly, "
            "most notably during the conquest of Khaybar. As the fourth Caliph, his rigorous adherence to social equity and legal "
            "scholarship left an indelible heritage of righteous governance."
        ),
        "vocab_notes": "Chivalry -> Noble valour; Nascent -> Newly emerging; Rigorous -> Strict and thorough."
    },
    {
        "id": 25,
        "slug_id": "unseen-25",
        "title": "Cricket in Bangladesh: From ICC Trophy Triumph to Global Test Status",
        "bn_title": "বাংলাদেশে ক্রিকেট: আইসিসি ট্রফি জয় থেকে আন্তর্জাতিক টেস্ট মর্যাদা",
        "theme": "Sports History, Bangladesh Cricket Team & National Unity",
        "stars": "**",
        "priority": "High Priority",
        "boards": "Standard Board Review",
        "page_pdf": 477,
        "passage": (
            "Cricket is by far the most popular and passionately celebrated sport in Bangladesh, serving as a tremendous catalyst "
            "for national unity. Bangladesh entered the international cricket arena prominently by winning the ICC Trophy in Malaysia "
            "in 1997 under Akram Khan's captaincy. This victory secured qualification for the 1999 Cricket World Cup in England, where "
            "Bangladesh stunned former champions Pakistan in a historic match. Acknowledging this remarkable trajectory, the International "
            "Cricket Council (ICC) granted Bangladesh full Test-playing status on 26 June 2000. Over subsequent decades, legendary cricketers "
            "like Shakib Al Hasan and Mashrafe Mortaza propelled the Tigers to memorable victories against all top Test nations."
        ),
        "info_table": {
            "headers": ["Team / Captain", "Cricketing Landmark", "Year / Date", "Venue / Opponent"],
            "rows": [
                ["Bangladesh Team", "won the ICC Trophy", "(i) [......]", "in Malaysia"],
                ["The Tigers", "qualified for Cricket World Cup", "1999", "hosted in (ii) [......]"],
                ["Bangladesh", "defeated Pakistan", "1999 World Cup", "at (iii) [......]"],
                ["ICC", "conferred full Test status", "(iv) [......]", "10th Test-playing nation"],
                ["Star players", "elevated Bangladesh cricket", "21st century", "against (v) [......]"]
            ]
        },
        "answers": {
            "i": "in 1997",
            "ii": "England",
            "iii": "Northampton",
            "iv": "26 June 2000",
            "v": "all leading Test-playing nations"
        },
        "model_summary": (
            "Cricket has blossomed into Bangladesh's foremost national sporting passion and a potent vehicle for civic solidarity. "
            "The monumental 1997 ICC Trophy victory in Malaysia heralded Bangladesh's arrival, culminating in a sensational World Cup "
            "upset against Pakistan in 1999. Attaining prestigious Test status in 2000, Bangladesh evolved into a competitive "
            "international cricketing force capable of toppling elite world teams."
        ),
        "vocab_notes": "Solidarity -> Collective unity; Heralded -> Signaled; Toppling -> Defeating."
    },
    {
        "id": 26,
        "slug_id": "unseen-26",
        "title": "Altaf Mahmud: Musical Maestro, Language Song Composer and Liberation Martyr",
        "bn_title": "আলতাফ মাহমুদ: সুরকার, অমর একুশের গানের স্রষ্টা ও শহীদ মুক্তিযোদ্ধা",
        "theme": "Cultural Movement, Language Martyrs' Song & 1971 Martyrdom",
        "stars": "**",
        "priority": "High Priority",
        "boards": "C.B. '19",
        "page_pdf": 478,
        "passage": (
            "Altaf Mahmud was a prominent Bangladeshi musician, cultural composer, and martyred freedom fighter. Born on "
            "23 December 1933 in Patuakhali, he displayed innate musical genius from childhood and participated vigorously in progressive "
            "cultural struggles. In 1954, he composed the immortal musical tune for Abdul Gaffar Choudhury's poem 'Amar Bhaier Rokte Rangano "
            "Ekushey February', which became the sacred anthem of the Bengali Language Movement. During the 1971 Liberation War, "
            "Mahmud's Dhaka residence served as a secret arms depository and communication refuge for the daring urban guerrilla unit "
            "'Crack Platoon'. On 30 August 1971, Pakistani forces captured him; he was brutally tortured and executed."
        ),
        "info_table": {
            "headers": ["Musician / Patriot", "Historic Creation / Event", "Year / Date", "Significance / Location"],
            "rows": [
                ["Altaf Mahmud", "was born", "23 December 1933", "in (i) [......]"],
                ["He", "composed tune of 'Amar Bhaier Rokte'", "(ii) [......]", "written by Gaffar Choudhury"],
                ["The song", "became emotional anthem", "post-1952", "for (iii) [......]"],
                ["His Dhaka residence", "harboured secret arms", "1971", "for (iv) [......]"],
                ["The patriotic artist", "was abducted and martyred", "(v) [......]", "by Pakistani military"]
            ]
        },
        "answers": {
            "i": "Patuakhali, Bengal",
            "ii": "in 1954",
            "iii": "the Language Movement / Ekushey February",
            "iv": "Crack Platoon (guerrilla fighters)",
            "v": "30 August 1971 (or early September)"
        },
        "model_summary": (
            "Altaf Mahmud (1933–1971) was an inspirational Bengali composer who immortalized the Language Movement by setting "
            "'Amar Bhaier Rokte Rangano' to its solemn, enduring musical tune in 1954. During the 1971 Liberation War, he courageously "
            "sheltered urban freedom fighters of the Crack Platoon and concealed weapons in his home. Captured and martyred by "
            "enemy forces, his artistic and patriotic legacy remains eternal."
        ),
        "vocab_notes": "Solemn -> Deeply reverent; Concealed -> Hid securely; Depository -> Storage facility."
    },
    {
        "id": 27,
        "slug_id": "unseen-27",
        "title": "Dengue Fever: Epidemiology, Transmission Vector, and Preventive Measures",
        "bn_title": "ডেঙ্গু জ্বর: বিস্তার, লক্ষণ ও কার্যকর প্রতিরোধমূলক পদক্ষেপ",
        "theme": "Epidemiology, Aedes Mosquito Vector & Public Health Hygiene",
        "stars": "**",
        "priority": "High Priority",
        "boards": "Health Board Focus",
        "page_pdf": 480,
        "passage": (
            "Dengue fever is a severe viral infection transmitted to humans through the bites of infected female Aedes mosquitoes, "
            "principally Aedes aegypti. The virus proliferates in tropical and subtropical urban environments, especially following "
            "monsoon rains when stagnant water collects in flower pots, discarded tyres, and rooftop containers. Common symptoms include "
            "abrupt high fever, debilitating joint and muscle pain, severe headache, retro-orbital pain, and skin rashes. Severe cases "
            "can escalate into Dengue Hemorrhagic Fever, characterized by precipitous platelet drops and internal bleeding. Because no "
            "universal antiviral drug exists, preventing mosquito breeding by draining standing water and using mosquito nets remains "
            "the most effective defense."
        ),
        "info_table": {
            "headers": ["Disease / Vector", "Transmission / Condition", "Time / Habitat", "Prevention / Risk"],
            "rows": [
                ["Dengue fever", "is transmitted to humans", "by (i) [......]", "female Aedes mosquitoes"],
                ["Aedes mosquitoes", "breed prolifically", "monsoon season", "in (ii) [......]"],
                ["Infected patients", "experience painful symptoms", "acute phase", "such as (iii) [......]"],
                ["(iv) [......]", "causes critical complications", "severe cases", "causing internal bleeding"],
                ["Communities", "must eliminate standing water", "regularly", "to prevent (v) [......]"]
            ]
        },
        "answers": {
            "i": "infected mosquito bites",
            "ii": "stagnant water in pots and tyres",
            "iii": "high fever and joint pains",
            "iv": "Dengue Hemorrhagic Fever",
            "v": "mosquito larvae propagation"
        },
        "model_summary": (
            "Dengue fever is a dangerous mosquito-borne viral malady prevalent in warm urban settings, disseminated primarily by "
            "Aedes mosquitoes breeding in clean stagnant water. Manifesting through intense fevers, muscular aches, and potential "
            "hemorrhagic crises, it poses substantial health hazards. In the absence of targeted pharmacological cures, meticulous "
            "environmental sanitation and the systematic eradication of standing water reservoirs constitute the primary shield."
        ),
        "vocab_notes": "Disseminated -> Spread widely; Malady -> Illness/disease; Meticulous -> Rigorously careful."
    },
    {
        "id": 28,
        "slug_id": "unseen-28",
        "title": "The Historic Hijrah: The Migration from Makkah to Madinah (622 CE)",
        "bn_title": "ঐতিহাসিক হিজরত: মক্কা থেকে মদিনায় নবীজির প্রস্থান (৬২২ খ্রি.)",
        "theme": "Islamic History / The Hijrah, Islamic Calendar & Statehood",
        "stars": "***",
        "priority": "Top Priority",
        "boards": "Dakhil Exam. '25",
        "page_pdf": 484,
        "passage": (
            "The Hijrah signifies the momentous migration of Prophet Muhammad (Sm) and his companions from Makkah to the city of "
            "Yathrib (subsequently renamed Madinah) in 622 CE. For over a decade, early Muslims in Makkah endured merciless ostracism, "
            "boycotts, and physical torture from the pagan Quraysh elite. When a sinister plot to assassinate the Prophet in his home "
            "was uncovered, he departed secretly with his loyal confidant Hazrat Abu Bakr (R), taking refuge in the Cave of Thawr. "
            "Reaching Yathrib safely, the Prophet was welcomed warmly by the Ansar (Helpers). This historic migration marks the inception "
            "of the Islamic Hijri calendar and laid the foundation for the first constitutional Islamic commonwealth."
        ),
        "info_table": {
            "headers": ["Entity / Leader", "Sacred Journey / Milestone", "Year / Date", "Location / Consequence"],
            "rows": [
                ["Prophet Muhammad (Sm)", "migrated from Makkah", "(i) [......]", "to Yathrib (Madinah)"],
                ["Early Muslims", "suffered intense persecution", "610-622 CE", "from (ii) [......]"],
                ["The Prophet & Abu Bakr (R)", "hid from pursuers", "during flight", "inside (iii) [......]"],
                ["The people of Madinah", "received the migrants", "622 CE", "designated as (iv) [......]"],
                ["The Hijrah event", "commenced a new calendar era", "622 CE", "known as (v) [......]"]
            ]
        },
        "answers": {
            "i": "in 622 CE",
            "ii": "the pagan Quraysh",
            "iii": "the Cave of Thawr",
            "iv": "Ansar (Helpers)",
            "v": "the Islamic Hijri calendar"
        },
        "model_summary": (
            "The Hijrah of 622 CE designates the strategic migration of Prophet Muhammad (Sm) and his persecuted followers from "
            "oppressive Makkah to the hospitable sanctuary of Madinah. Evading a coordinated assassination conspiracy with Hazrat Abu "
            "Bakr (R), he reached Madinah where the local Ansar welcomed them. This watershed event initiated the Islamic Hijri era "
            "and catalyzed the establishment of a sovereign, ethical commonwealth."
        ),
        "vocab_notes": "Momentous -> Highly significant; Sanctuary -> Safe haven; Watershed -> Pivotal turning point."
    },
    {
        "id": 29,
        "slug_id": "unseen-29",
        "title": "Polli Kobi Jasimuddin: The Melodious Bard of Rural Bengal's Soil and Soul",
        "bn_title": "পল্লীকবি জসীম উদ্‌দীন: বাংলার আবহমান পল্লীপ্রকৃতি ও সাধারণ মানুষের চারণকবি",
        "theme": "Rural Bengali Poetry, Folk Ballads & Nakshi Kanthar Math",
        "stars": "***",
        "priority": "Top Priority",
        "boards": "B.B. '23, Chat.B. '25",
        "page_pdf": 505,
        "passage": (
            "Jasimuddin, reverently styled as 'Polli Kobi' (The Rural Poet), was a celebrated Bengali poet and folklorist who "
            "depicted the pastoral rhythms, passions, and sorrows of rural Bangladesh with unmatched lyricism. Born on 1 January 1903 "
            "in Tambulkhana, Faridpur, his iconic poem 'Kabor' (The Grave) was incorporated into the matriculation curriculum while "
            "he was still an undergraduate student at Calcutta University. His epic verse novel 'Nakshi Kanthar Math' (Field of the "
            "Embroidered Quilt), translated into English and numerous world languages, garnered international acclaim. Works like "
            "'Sojan Badiyar Ghat' and 'Rakhali' reflect deep empathy for peasant life. He was posthumously honored with the Swadhinata "
            "Puraskar before his passing on 13 March 1976."
        ),
        "info_table": {
            "headers": ["Poet / Masterpiece", "Literary Creation / Distinction", "Year / Date", "Place / Achievement"],
            "rows": [
                ["Jasimuddin", "was born", "1 January 1903", "in (i) [......]"],
                ["His poem 'Kabor'", "was selected for textbooks", "undergraduate days", "at (ii) [......]"],
                ["(iii) [......]", "achieved international fame", "1929", "translated as 'The Embroidered Quilt'"],
                ["His rural ballads", "portrayed peasant emotions", "20th century", "awarded (iv) [......]"],
                ["The rural poet", "passed away in Dhaka", "(v) [......]", "buried at Gobindapur"]
            ]
        },
        "answers": {
            "i": "Tambulkhana, Faridpur",
            "ii": "Calcutta University",
            "iii": "Nakshi Kanthar Math",
            "iv": "Swadhinata Puraskar / Ekushey Padak",
            "v": "13 March 1976"
        },
        "model_summary": (
            "Polli Kobi Jasimuddin (1903–1976) captured the authentic rustic spirit of Bengal through melodic verse steeped in rural "
            "folklore and pastoral imagery. Gaining early prominence with 'Kabor', his magnum opus 'Nakshi Kanthar Math' attained global "
            "celebrity for its poignant dramatization of rural love and tragedy. His poetry remains a timeless mirror of Bangladesh's "
            "village soul and agricultural civilization."
        ),
        "vocab_notes": "Rustic -> Rural/pastoral; Magnum opus -> Greatest masterpiece; Poignant -> Touchingly sad."
    },
    {
        "id": 30,
        "slug_id": "unseen-30",
        "title": "Communal Harmony and Cultural Pluralism in Bangladesh: A Millennial Tradition",
        "bn_title": "বাংলাদেশে সাম্প্রদায়িক সম্প্রীতি ও বহুত্ববাদী সংস্কৃতি: হাজার বছরের ঐতিহ্য",
        "theme": "Communal Harmony, Pluralism & Interfaith Coexistence",
        "stars": "**",
        "priority": "High Priority",
        "boards": "Standard Board Review",
        "page_pdf": 508,
        "passage": (
            "Bangladesh is a land of inspiring communal harmony where diverse religious and ethnic communities have coexisted "
            "peacefully for centuries. Although Muslims constitute the majority, Hindus, Buddhists, Christians, and indigenous "
            "populations participate jointly in national celebrations. Festivals like Eid-ul-Fitr, Durga Puja, Buddha Purnima, "
            "and Christmas are marked by widespread interfaith greetings and mutual hospitality. The national secular ethos is "
            "succinctly captured in the Bengali adage: 'Religion belongs to individuals, but festivals belong to all' (Dhormo jaar "
            "jaar, utsob sobar). This enduring social cohesion has fortified Bangladesh against sectarian intolerance and remains "
            "a pillar of stability."
        ),
        "info_table": {
            "headers": ["Country / Value", "Social Trait / Festival", "Community / Base", "Outcome / Principle"],
            "rows": [
                ["Bangladesh", "exhibits communal harmony", "for centuries", "among (i) [......]"],
                ["Religious festivals", "are celebrated collectively", "throughout year", "such as (ii) [......]"],
                ["(iii) [......]", "reflects secular philosophy", "cultural tradition", "'Festivals belong to everyone'"],
                ["Social cohesion", "protects civil stability", "nationwide", "against (iv) [......]"],
                ["Interfaith brotherhood", "strengthens national identity", "modern era", "promotes (v) [......]"]
            ]
        },
        "answers": {
            "i": "diverse religious and ethnic groups",
            "ii": "Eid, Durga Puja, and Christmas",
            "iii": "The national ethos",
            "iv": "sectarian hatred and extremism",
            "v": "peaceful coexistence and unity"
        },
        "model_summary": (
            "Bangladesh enjoys a rich millennial heritage of interfaith harmony, where people of Muslim, Hindu, Buddhist, and "
            "Christian backgrounds share social bonds harmoniously. Citizens actively exchange goodwill across distinct religious "
            "festivals, embodying the pluralistic ideal that cultural celebrations transcend sectarian lines. This profound "
            "communal solidarity serves as a foundational bulwark for national peace."
        ),
        "vocab_notes": "Pluralistic -> Diverse and inclusive; Bulwark -> Strong defensive wall; Coexistence -> Living together peacefully."
    },
    {
        "id": 31,
        "slug_id": "unseen-31",
        "title": "Emperor Babur: Founder of the Mughal Empire and Renowned Memoirist",
        "bn_title": "সম্রাট বাবর: মুঘল সাম্রাজ্যের প্রতিষ্ঠাতা ও বিদগ্ধ আত্মজীবনীকার",
        "theme": "Mughal Empire, First Battle of Panipat (1526) & Baburnama",
        "stars": "**",
        "priority": "High Priority",
        "boards": "Standard Board Review",
        "page_pdf": 510,
        "passage": (
            "Zahir-ud-din Muhammad Babur was the brilliant military commander and founder of the Mughal Empire in the Indian "
            "subcontinent. Descended from both Timur and Genghis Khan, he was born on 14 February 1483 in the Fergana Valley (Uzbekistan). "
            "Inheriting Fergana at age twelve, he encountered repeated reversals before capturing Kabul in 1504. In 1526, invited by "
            "disaffected nobles, Babur marched into India and decisively routed Ibrahim Lodi's massive army at the First Battle of "
            "Panipat through innovative artillery tactics. He subsequently vanquished Rana Sanga at Khanwa in 1527. Beyond warfare, "
            "Babur was an exquisite poet and diarist whose autobiography 'Baburnama' is praised as world-class literature. He died in 1530 at age 47."
        ),
        "info_table": {
            "headers": ["Ruler / Battle", "Military Milestone", "Year / Date", "Location / Weaponry"],
            "rows": [
                ["Babur", "was born in Central Asia", "14 February 1483", "in (i) [......]"],
                ["He", "secured kingdom of Kabul", "1504", "after losing (ii) [......]"],
                ["Battle of Panipat", "routed Ibrahim Lodi's army", "(iii) [......]", "using field artillery"],
                ["Babur", "wrote celebrated autobiography", "lifetime", "named (iv) [......]"],
                ["The Mughal founder", "passed away", "(v) [......]", "at the age of 47"]
            ]
        },
        "answers": {
            "i": "Fergana Valley (Uzbekistan)",
            "ii": "his ancestral throne of Fergana",
            "iii": "in 1526",
            "iv": "Baburnama (Tuzk-e-Babri)",
            "v": "26 December 1530"
        },
        "model_summary": (
            "Babur (1483–1530), a descendant of Timur and Genghis Khan, established the Mughal dynasty in India following his decisive "
            "victory at the First Battle of Panipat in 1526. Employing superior cannon artillery, he dismantled the Delhi Sultanate "
            "and consolidated authority across northern India. Concurrently, his autobiographical memoir 'Baburnama' revealed him "
            "as an observant naturalist and refined man of letters."
        ),
        "vocab_notes": "Artillery -> Cannons and heavy weaponry; Consolidated -> Strengthened and united; Naturalist -> Observer of nature."
    },
    {
        "id": 32,
        "slug_id": "unseen-32",
        "title": "William Wordsworth: The High Priest of Nature and Romantic English Poetry",
        "bn_title": "উইলিয়াম ওয়ার্ডসওয়ার্থ: প্রকৃতিপূজারী ও রোমান্টিক ইংরেজি কাব্যের পথিকৃৎ",
        "theme": "English Romanticism, Nature Worship & Lyrical Ballads",
        "stars": "**",
        "priority": "High Priority",
        "boards": "Standard Board Review",
        "page_pdf": 521,
        "passage": (
            "William Wordsworth was the preeminent English Romantic poet who inaugurated the Romantic Age in English literature "
            "alongside Samuel Taylor Coleridge. Born on 7 April 1770 in Cockermouth, Cumberland, he developed an abiding spiritual "
            "communion with the picturesque landscapes of the English Lake District. In 1798, Wordsworth and Coleridge published "
            "'Lyrical Ballads', introducing poetry written in the common language of ordinary men, which defined poetry as 'the "
            "spontaneous overflow of powerful feelings recollected in tranquility'. Celebrated as the 'High Priest of Nature', masterpieces "
            "like 'The Solitary Reaper', 'Daffodils', and 'The Prelude' view nature as a divine teacher and moral healer. He served as "
            "Poet Laureate until his death on 23 April 1850."
        ),
        "info_table": {
            "headers": ["Poet / Publication", "Literary Achievement", "Year / Date", "Place / Philosophy"],
            "rows": [
                ["William Wordsworth", "was born", "7 April 1770", "in (i) [......]"],
                ["Lyrical Ballads", "commenced English Romantic movement", "(ii) [......]", "co-authored with Coleridge"],
                ["Wordsworth", "defined poetic creation", "1800 Preface", "as (iii) [......]"],
                ["Famous nature lyric", "celebrated golden daffodils", "1804", "inspired by (iv) [......]"],
                ["The poet laureate", "passed away", "(v) [......]", "at Rydal Mount"]
            ]
        },
        "answers": {
            "i": "Cockermouth, Lake District",
            "ii": "in 1798",
            "iii": "'spontaneous overflow of powerful feelings'",
            "iv": "the serene English Lake District",
            "v": "23 April 1850"
        },
        "model_summary": (
            "William Wordsworth (1770–1850) sparked the English Romantic revival through his collaborative 1798 collection 'Lyrical "
            "Ballads'. Championing vernacular diction and emotional spontaneity, he venerated nature not merely as scenery, but as a "
            "living spiritual mentor capable of soothing the human soul. His timeless verses elevate ordinary rural experiences into "
            "sublime philosophical reflections."
        ),
        "vocab_notes": "Vernacular -> Everyday native speech; Spontaneity -> Natural impulse; Venerated -> Deeply revered."
    },
    {
        "id": 33,
        "slug_id": "unseen-33",
        "title": "Global Warming and Climate Crisis: Ecological Threats to Coastal Bangladesh",
        "bn_title": "বৈশ্বিক উষ্ণায়ন ও জলবায়ু সংকট: উপকূলীয় বাংলাদেশের পরিবেশগত ঝুঁকি",
        "theme": "Global Warming, Greenhouse Effect & Coastal Vulnerability",
        "stars": "***",
        "priority": "Top Priority",
        "boards": "Environment Focus",
        "page_pdf": 537,
        "passage": (
            "Global warming represents the gradual increase in the Earth's average surface temperature, driven primarily by human "
            "activities that emit greenhouse gases like carbon dioxide, methane, and nitrous oxide. Indiscriminate industrial combustion, "
            "deforestation, and fossil fuel consumption trap thermal radiation inside the atmospheric blanket. Consequently, polar "
            "glaciers are melting at an alarming velocity, causing oceanic sea levels to rise. Low-lying riverine countries like Bangladesh "
            "are extraordinarily vulnerable; a projected one-meter rise in sea level could submerge nearly 17 percent of Bangladesh's "
            "coastal land, displacing over thirty million climate refugees and salinizing freshwater aquifers. Transitioning to "
            "renewable solar and wind energy is therefore an urgent international imperative."
        ),
        "info_table": {
            "headers": ["Phenomenon / Threat", "Primary Trigger", "Consequence / Area", "Future Impact"],
            "rows": [
                ["Global warming", "increases atmospheric heat", "worldwide", "through (i) [......]"],
                ["Industrial activities", "burn fossil fuels", "modern era", "emits (ii) [......]"],
                ["Polar ice caps", "melt at high speed", "Arctic and Antarctic", "causing (iii) [......]"],
                ["Bangladesh coastline", "faces sea level inundation", "future projection", "displacing (iv) [......]"],
                ["Global community", "must transition swiftly", "urgent imperative", "towards (v) [......]"]
            ]
        },
        "answers": {
            "i": "greenhouse gas emissions",
            "ii": "carbon dioxide and methane",
            "iii": "rapid sea-level rise",
            "iv": "millions of climate refugees",
            "v": "renewable solar and wind energy"
        },
        "model_summary": (
            "Global warming, induced by excessive fossil fuel emissions and widespread deforestation, poses an existential environmental "
            "crisis worldwide. As trapped greenhouse gases accelerate polar deglaciation, rising sea levels severely imperil low-lying "
            "deltaic territories such as coastal Bangladesh. Substantial land loss, agricultural salinization, and mass displacement "
            "necessitate swift international commitments to renewable green energy alternatives."
        ),
        "vocab_notes": "Deglaciation -> Melting of glaciers; Imperil -> Endanger; Salinization -> Salt intrusion."
    },
    {
        "id": 34,
        "slug_id": "unseen-34",
        "title": "A.K. Fazlul Huq and the Historic Lahore Resolution of 1940",
        "bn_title": "এ কে ফজলুল হক এবং ১৯৪০ সালের ঐতিহাসিক লাহোর প্রস্তাব",
        "theme": "Anti-Colonial Politics, Lahore Resolution & Subcontinental History",
        "stars": "**",
        "priority": "High Priority",
        "boards": "R.B. '24",
        "page_pdf": 539,
        "passage": (
            "The Lahore Resolution of 1940 was a monumental turning point in the political destiny of the South Asian subcontinent. "
            "On 23 March 1940, at the annual general session of the All India Muslim League held at Minto Park in Lahore, Sher-e-Bangla "
            "A.K. Fazlul Huq, then the Premier of undivided Bengal, moved the historic resolution. The resolution formally demanded that "
            "geographically contiguous units in the northwestern and eastern zones of British India, where Muslims were numerically in a "
            "majority, should be grouped to constitute 'Independent States' in which the constituent units should be autonomous and sovereign. "
            "This principle laid the intellectual and political groundwork that eventually guided the trajectory toward the partition of India."
        ),
        "info_table": {
            "headers": ["Statesman / Document", "Historical Event", "Year / Date", "Location / Core Demand"],
            "rows": [
                ["Lahore Resolution", "was formally proposed", "(i) [......]", "at Minto Park, Lahore"],
                ["Sher-e-Bangla Fazlul Huq", "moved the historic motion", "March 1940", "as (ii) [......]"],
                ["The resolution", "identified geographical zones", "British India", "in (iii) [......]"],
                ["Proposed state units", "were to be organized", "post-colonial era", "as (iv) [......]"],
                ["The 1940 declaration", "shaped subcontinental politics", "1940s", "led toward (v) [......]"]
            ]
        },
        "answers": {
            "i": "23 March 1940",
            "ii": "Premier of undivided Bengal",
            "iii": "northwestern and eastern Muslim zones",
            "iv": "'Independent and sovereign states'",
            "v": "the partition of British India in 1947"
        },
        "model_summary": (
            "Moved by Sher-e-Bangla A.K. Fazlul Huq in Lahore on 23 March 1940, the Lahore Resolution constituted a watershed moment "
            "in anti-colonial subcontinental politics. It articulated a demand that Muslim-majority regions in northwestern and eastern "
            "India be constituted into autonomous and sovereign states. This foundational document fundamentally altered the political "
            "trajectory, culminating in the 1947 partition."
        ),
        "vocab_notes": "Contiguous -> Adjacent/connected; Autonomous -> Self-governing; Trajectory -> Path of evolution."
    },
    {
        "id": 35,
        "slug_id": "unseen-35",
        "title": "The Taj Mahal: Monument of Eternal Love and Pinnacle of Mughal Architecture",
        "bn_title": "তাজমহল: অমর প্রেমের প্রতীক ও মুঘল স্থাপত্যকলার শ্রেষ্ঠ নিদর্শন",
        "theme": "Architectural Wonder, Mughal Heritage & UNESCO World Monument",
        "stars": "**",
        "priority": "High Priority",
        "boards": "Standard Board Review",
        "page_pdf": 551,
        "passage": (
            "The Taj Mahal is an ivory-white marble mausoleum located on the south bank of the Yamuna River in Agra, India, "
            "widely regarded as the finest jewel of Indo-Islamic architecture. It was commissioned in 1632 by the Mughal Emperor Shah Jahan "
            "to house the tomb of his favourite wife, Mumtaz Mahal, who died during childbirth. Incorporating Persian, Islamic, and Indian "
            "architectural motifs, the complex took over twenty years and twenty thousand artisans to complete, overseen by master architect "
            "Ustad Ahmad Lahori. The monument is renowned for its symmetrical perfection, central dome flanked by four minarets, and exquisite "
            "floral pietra dura stone inlays. Designated a UNESCO World Heritage Site in 1983, it symbolizes enduring romantic devotion."
        ),
        "info_table": {
            "headers": ["Monument / Emperor", "Construction Landmark", "Year / Period", "Location / Material"],
            "rows": [
                ["Taj Mahal", "was commissioned by Shah Jahan", "(i) [......]", "on banks of Yamuna River"],
                ["The mausoleum", "was built as eternal memorial", "17th century", "for (ii) [......]"],
                ["The project", "employed 20,000 artisans", "1632–1653", "supervised by (iii) [......]"],
                ["(iv) [......]", "decorates white marble surfaces", "exquisite craftsmanship", "precious gemstone inlays"],
                ["UNESCO", "inscribed Taj Mahal as World Heritage", "(v) [......]", "universal architectural treasure"]
            ]
        },
        "answers": {
            "i": "in 1632",
            "ii": "Empress Mumtaz Mahal",
            "iii": "Ustad Ahmad Lahori",
            "iv": "Pietra dura floral inlay",
            "v": "in 1983"
        },
        "model_summary": (
            "Commissioned in 1632 by Emperor Shah Jahan as a mausoleum for his beloved wife Mumtaz Mahal, the Taj Mahal in Agra "
            "represents the zenith of Mughal architectural refinement. Crafted from pure white marble with intricate floral gemstone "
            "inlays and flawless symmetry, the monument employed tens of thousands of skilled craftsmen over two decades. Recognized "
            "as a UNESCO World Heritage site, it remains an immortal tribute to marital devotion."
        ),
        "vocab_notes": "Zenith -> Highest peak; Flanked -> Bordered on both sides; Inscribed -> Officially enrolled."
    },
    {
        "id": 36,
        "slug_id": "unseen-36",
        "title": "Historical Evolution and Cultural Heritage of Dhaka City",
        "bn_title": "ঢাকা নগরীর ঐতিহাসিক বিবর্তন ও সমৃদ্ধ সাংস্কৃতিক ঐতিহ্য",
        "theme": "Urban History, Mughal Capital Jahangirnagar & Modern Metropolis",
        "stars": "**",
        "priority": "High Priority",
        "boards": "Standard Board Review",
        "page_pdf": 559,
        "passage": (
            "Dhaka, the vibrant capital of Bangladesh, is an ancient riverine metropolis with an illustrious history spanning more "
            "than four hundred years. Situated along the banks of the Buriganga River, Dhaka achieved imperial prominence in 1610 when "
            "Mughal Subahdar Islam Khan Chishti declared it the provincial capital of Bengal and renamed it 'Jahangirnagar'. During "
            "Mughal rule, Dhaka was a bustling center of international textile trade, world-renowned for its translucent muslin fabric. "
            "Architectural marvels like Lalbagh Fort, Ahsan Manzil, and Tara Masjid highlight its historic opulence. In the twentieth "
            "century, Dhaka emerged as the epicenter of historic political struggles, notably the 1952 Language Movement and the 1971 "
            "Liberation War. Today, it stands as a bustling megacity and national economic engine."
        ),
        "info_table": {
            "headers": ["City / Subahdar", "Historical Transformation", "Year / Date", "River / Textile"],
            "rows": [
                ["Islam Khan Chishti", "made Dhaka Bengal capital", "(i) [......]", "renamed Jahangirnagar"],
                ["Mughal Dhaka", "became global trading hub", "17th century", "famous for (ii) [......]"],
                ["Lalbagh Fort and Ahsan Manzil", "reflect historical grandeur", "Mughal and colonial eras", "along (iii) [......]"],
                ["The city", "served as nerve center of movements", "1952 and 1971", "for (iv) [......]"],
                ["Modern Dhaka", "evolved into megacity", "at present", "acting as (v) [......]"]
            ]
        },
        "answers": {
            "i": "in 1610",
            "ii": "translucent Muslin fabric",
            "iii": "the Buriganga River",
            "iv": "mother language and national liberation",
            "v": "national political and economic engine"
        },
        "model_summary": (
            "Dhaka's rise to historical prominence commenced in 1610 when it became the Mughal capital of Bengal, quickly gaining global "
            "renown for its exquisite muslin textiles and maritime commerce along the Buriganga. Endowed with monuments like Lalbagh Fort, "
            "it later spearheaded the twentieth-century political and linguistic movements leading to Bangladesh's independence. "
            "Today, it thrives as the nation's vibrant political, commercial, and cultural heartbeat."
        ),
        "vocab_notes": "Metropolis -> Major urban city; Translucent -> Semi-transparent; Spearheaded -> Led."
    },
    {
        "id": 37,
        "slug_id": "unseen-37",
        "title": "Emperor Shah Jahan: Architectural Splendour and His Tragic Final Years",
        "bn_title": "সম্রাট শাহজাহান: মুঘল স্থাপত্যের স্বর্ণযুগ ও অন্তিম বন্দিদশা",
        "theme": "Mughal History / Shah Jahan, Golden Age of Architecture & Deposition",
        "stars": "*",
        "priority": "Moderate",
        "boards": "Standard Board Review",
        "page_pdf": 569,
        "passage": (
            "Shah Jahan was the fifth Mughal Emperor of India, reigning from 1628 to 1658 during what is widely acclaimed as the "
            "golden age of Mughal architecture. The son of Emperor Jahangir, he demonstrated administrative acuity and boundless "
            "passion for grand monuments, constructing the Red Fort and Jama Masjid in Delhi, the Shalimar Gardens in Lahore, and the "
            "peerless Taj Mahal in Agra. However, his later reign was darkened by a ferocious war of succession among his four ambitious "
            "sons. In 1658, his third son, Aurangzeb, emerged victorious, usurped the throne, and confined the aging emperor inside "
            "the Agra Fort. Shah Jahan spent his final eight years in captivity, gazing melancholically at the Taj Mahal across the "
            "Yamuna until his death in 1666."
        ),
        "info_table": {
            "headers": ["Emperor / Usurper", "Reign / Occurrence", "Year / Date", "Place / Architectural Marvel"],
            "rows": [
                ["Shah Jahan", "ascended the Mughal throne", "1628", "succeeded (i) [......]"],
                ["His glorious reign", "produced architectural landmarks", "1630s-1650s", "including (ii) [......]"],
                ["(iii) [......]", "waged war of succession", "1657-1658", "competed for throne"],
                ["Aurangzeb", "imprisoned his father", "(iv) [......]", "in Agra Fort"],
                ["The captive emperor", "spent final years gazing at Taj", "1658 to 1666", "died at age of (v) [......]"]
            ]
        },
        "answers": {
            "i": "Emperor Jahangir",
            "ii": "Red Fort, Jama Masjid & Taj Mahal",
            "iii": "Four ambitious sons of Shah Jahan",
            "iv": "in 1658",
            "v": "74 years (in January 1666)"
        },
        "model_summary": (
            "Emperor Shah Jahan (1592–1666) presided over the zenith of Mughal architectural grandeur, bequeathing monuments of "
            "matchless beauty such as the Taj Mahal and the Red Fort. Yet his triumphant reign concluded in tragedy when his son "
            "Aurangzeb seized the throne amidst a fraternal succession war in 1658. The former sovereign lived out his final eight "
            "years in confinement in Agra Fort, gazing toward his wife's immortal tomb."
        ),
        "vocab_notes": "Zenith -> Apex/highest point; Fraternal -> Among brothers; Confinement -> Captivity."
    },
    {
        "id": 38,
        "slug_id": "unseen-38",
        "title": "Kazi Nazrul Islam: The Rebel Poet and National Icon of Bangladesh",
        "bn_title": "কাজী নজরুল ইসলাম: বিদ্রোহী কবি ও বাংলাদেশের জাতীয় কবি",
        "theme": "Rebel Poet, Anti-Colonial Literature & Communal Harmony",
        "stars": "***",
        "priority": "Top Priority",
        "boards": "Standard Board Review",
        "page_pdf": 571,
        "passage": (
            "Kazi Nazrul Islam is the beloved National Poet of Bangladesh, renowned as the 'Bidrohi Kobi' (Rebel Poet) for his "
            "fiery verses challenging British imperialism, religious fanaticism, and social inequality. Born on 24 May 1899 in "
            "Churulia, Burdwan, he endured severe childhood adversity, working as a baker's boy and joining the British Indian Army "
            "during World War I. In 1921, he published his electrifying poem 'Bidrohi' (The Rebel), shaking the foundations of colonial rule. "
            "Nazrul was a prolific genius who composed nearly four thousand songs (Nazrul Geeti), revolutionizing Bengali music with "
            "classical ragas and Islamic ghazals. Tragically struck by a debilitating neurological illness in 1942, he was brought to "
            "sovereign Bangladesh in 1972 by Bangabandhu and conferred citizenship. He died on 29 August 1976 in Dhaka."
        ),
        "info_table": {
            "headers": ["Poet / Work", "Major Milestone / Output", "Year / Date", "Place / Cause"],
            "rows": [
                ["Kazi Nazrul Islam", "was born", "24 May 1899", "in (i) [......]"],
                ["He", "composed electrifying poem 'Bidrohi'", "(ii) [......]", "challenged colonial oppression"],
                ["Nazrul", "composed nearly 4,000 songs", "prolific career", "known as (iii) [......]"],
                ["The poet", "was brought to sovereign Bangladesh", "(iv) [......]", "by Bangabandhu Sheikh Mujibur Rahman"],
                ["The National Poet", "passed away in Dhaka", "(v) [......]", "buried beside Dhaka University Mosque"]
            ]
        },
        "answers": {
            "i": "Churulia, Burdwan",
            "ii": "in 1921",
            "iii": "Nazrul Geeti",
            "iv": "in 1972",
            "v": "29 August 1976"
        },
        "model_summary": (
            "Kazi Nazrul Islam (1899–1976), Bangladesh's revered National Poet, galvanized anti-colonial consciousness through impassioned "
            "poetry that condemned social tyranny, bigotry, and colonial exploitation. Famously recognized for his 1921 masterpiece "
            "'Bidrohi', his extraordinary versatility produced thousands of melodic songs synthesizing diverse cultural traditions. "
            "Honored as the nation's poetic conscience, his message of human equality remains perpetually inspiring."
        ),
        "vocab_notes": "Galvanized -> Energized into action; Bigotry -> Intolerance; Synthesizing -> Blending harmoniously."
    },
    {
        "id": 39,
        "slug_id": "unseen-39",
        "title": "Electronic Mail (E-mail): The Genesis and Impact of Modern Digital Messaging",
        "bn_title": "ই-মেইল (ইলেকট্রনিক মেইল): ডিজিটাল যোগাযোগের সূচনা ও বিশ্বব্যাপী প্রভাব",
        "theme": "Digital Communication, Internet History & Ray Tomlinson",
        "stars": "*",
        "priority": "Moderate",
        "boards": "Standard Board Review",
        "page_pdf": 573,
        "passage": (
            "Electronic mail, commonly abbreviated as e-mail, is a digital communication method that enables users to transmit "
            "text messages, documents, and multimedia attachments across computer networks. The foundation of modern e-mail was "
            "invented in 1971 by computer engineer Ray Tomlinson on the ARPANET network, who famously introduced the '@' symbol to "
            "separate the user's name from their machine's host location. Unlike traditional postal mail ('snail mail'), which required "
            "days to arrive, e-mail transmits information across the globe in seconds at nominal cost. Today, billions of business and "
            "personal e-mails are sent daily, empowering global commerce, academic collaboration, and administrative governance, "
            "though users must exercise vigilance against phishing scams and spam."
        ),
        "info_table": {
            "headers": ["Technology / Pioneer", "Digital Landmark", "Year / Date", "Network / Feature"],
            "rows": [
                ["Ray Tomlinson", "invented networked e-mail", "(i) [......]", "on the ARPANET system"],
                ["Tomlinson", "introduced landmark character", "1971", "namely the (ii) [......]"],
                ["Electronic mail", "replaces slow postal services", "modern era", "called (iii) [......]"],
                ["Global users", "exchange messages instantly", "worldwide", "at (iv) [......]"],
                ["Internet users", "must remain cautious", "daily communication", "against (v) [......]"]
            ]
        },
        "answers": {
            "i": "in 1971",
            "ii": "'@' (at sign) symbol",
            "iii": "'snail mail'",
            "iv": "nominal cost and high speed",
            "v": "spam, malware, and phishing scams"
        },
        "model_summary": (
            "Invented in 1971 by Ray Tomlinson on the early ARPANET network, electronic mail revolutionized personal and professional "
            "communication by replacing traditional physical post with near-instantaneous digital message exchange. Introducing the "
            "universal '@' symbol, e-mail transformed international commerce and educational coordination through rapid, affordable "
            "data transmission. Despite challenges like cyber fraud, it remains an indispensable backbone of global cyberspace."
        ),
        "vocab_notes": "Instantaneous -> Immediate; Indispensable -> Vital; Cyberspace -> Digital network domain."
    },
    {
        "id": 40,
        "slug_id": "unseen-40",
        "title": "SAARC: Regional Cooperation, Shared Challenges and Opportunities in South Asia",
        "bn_title": "সার্ক: দক্ষিণ এশীয় আঞ্চলিক সহযোগিতা, অভিন্ন চ্যালেঞ্জ ও সম্ভাবনা",
        "theme": "International Relations, SAARC Charter & Regional Integration",
        "stars": "***",
        "priority": "Top Priority",
        "boards": "Dinj.B. '25, '26",
        "page_pdf": 589,
        "passage": (
            "The South Asian Association for Regional Cooperation (SAARC) is a regional intergovernmental organization established "
            "on 8 December 1985 in Dhaka, Bangladesh, following an initiative championed by Bangladeshi President Ziaur Rahman. "
            "Comprising eight member nations—Bangladesh, India, Pakistan, Sri Lanka, Nepal, Bhutan, Maldives, and Afghanistan (joined in 2007)—"
            "SAARC seeks to accelerate economic growth, social progress, and cultural development across South Asia. Its secretariat is "
            "located in Kathmandu, Nepal. SAARC promotes cooperative programs in agriculture, healthcare, rural development, and disaster "
            "management. Despite lingering political disputes among certain member states, SAARC remains a vital multilateral forum for "
            "fostering people-to-people connectivity and regional stability."
        ),
        "info_table": {
            "headers": ["Organization / Member", "Establishment / Expansion", "Year / Date", "Headquarters / Summit"],
            "rows": [
                ["SAARC", "was formally established", "(i) [......]", "in Dhaka, Bangladesh"],
                ["The regional bloc", "expanded to eight members", "(ii) [......]", "when Afghanistan joined"],
                ["Permanent Secretariat", "operates centrally", "established", "in (iii) [......]"],
                ["SAARC objectives", "focus on regional welfare", "collective mandate", "in (iv) [......]"],
                ["Member nations", "collaborate to overcome challenges", "South Asia", "to foster (v) [......]"]
            ]
        },
        "answers": {
            "i": "8 December 1985",
            "ii": "in 2007",
            "iii": "Kathmandu, Nepal",
            "iv": "economy, health, and agriculture",
            "v": "regional stability and connectivity"
        },
        "model_summary": (
            "Founded in Dhaka in 1985 on Bangladesh's initiative, SAARC unites eight South Asian nations to advance shared economic, "
            "cultural, and scientific development. Headquartered in Kathmandu, the alliance facilitates regional cooperation in agriculture, "
            "poverty alleviation, and disaster response. Despite persistent bilateral tensions between member states, it provides a "
            "crucial institutional platform for regional solidarity and civic engagement."
        ),
        "vocab_notes": "Multilateral -> Involving multiple nations; Bilateral -> Between two nations; Solidarity -> Mutual unity."
    },
    {
        "id": 41,
        "slug_id": "unseen-41",
        "title": "Hazrat Omar (R): Nobility, Justice and the Welfare Governance of Caliphate",
        "bn_title": "হযরত ওমর (রা.): সততা, ন্যায়পরায়ণতা ও কল্যাণমূলক রাষ্ট্রনায়কত্ব",
        "theme": "Justice, Compassion and Leadership in Islam (Featured Model)",
        "stars": "***",
        "priority": "Top Priority (Featured Model)",
        "boards": "Featured Model Passage (Page 05)",
        "page_pdf": 228,
        "passage": (
            "Hazrat Omar (R) was the second Caliph of Islam, renowned throughout world history for his unwavering sense of justice, "
            "uncompromising integrity, and compassionate welfare administration. As the leader of a vast Islamic empire, he routinely "
            "patrolled the streets of Madinah at night in disguise to witness his subjects' true living conditions. On one nocturnal "
            "round, he overheard crying children and found a distressed widow boiling stones in water to soothe her starving orphans. "
            "Deeply afflicted, the Caliph rushed to the state treasury (Baitulmal), personally hoisted a sack of flour onto his own "
            "shoulders, and delivered it directly to the family, cooking food himself to feed the hungry children. His governance "
            "remains the gold standard of public servant leadership."
        ),
        "info_table": {
            "headers": ["Caliph / Ruler", "Night Inspection / Deed", "Time / Context", "Place / Entity"],
            "rows": [
                ["Hazrat Omar (R)", "patrolled territory in disguise", "(i) [......]", "in Madinah"],
                ["(ii) [......]", "cried from hunger", "one night", "inside widow's dwelling"],
                ["The distressed mother", "boiled stones in water", "to comfort children", "in (iii) [......]"],
                ["The Caliph", "carried flour sack on his back", "hastily", "from (iv) [......]"],
                ["Hazrat Omar (R)", "personally prepared and fed food", "that night", "to the (v) [......]"]
            ]
        },
        "answers": {
            "i": "at night (nocturnal patrol)",
            "ii": "The starving children / Orphans",
            "iii": "her poverty-stricken home",
            "iv": "the state treasury (Baitulmal)",
            "v": "hungry orphan children"
        },
        "model_summary": (
            "Hazrat Omar (R), the second Caliph of Islam, exemplified supreme justice and selfless welfare governance by secretly "
            "inspecting his subjects' welfare at night. Discovering an impoverished widow boiling stones to console her starving offspring, "
            "he immediately carried heavy provisions from the Baitulmal on his own back and fed the family. His compassionate accountability "
            "remains an eternal model of righteous leadership."
        ),
        "vocab_notes": "Nocturnal -> Nighttime; Afflicted -> Emotionally sorrowful; Accountability -> Moral responsibility."
    }
]

def generate_full_file():
    print(f"Generating {OUTPUT_FILE} with {len(DATA_ITEMS)} full unseen topics...")
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write('#!/usr/bin/env python3\n')
        f.write('# -*- coding: utf-8 -*-\n')
        f.write('"""\n')
        f.write('tools/pdf_to_post/data_ssc_2027_unseen_full.py\n')
        f.write('-----------------------------------------------\n')
        f.write('Complete dataset of all 41 Unseen Topics for SSC 2027 English 1st Paper Silo 02:\n')
        f.write('- Passage context (120-170 words)\n')
        f.write('- Question 4: Information Transfer Table (headers, 5 rows, blanks, exact answer key)\n')
        f.write('- Question 5: Model Summary (60-80 words, 4-5 sentences, curriculum-compliant)\n')
        f.write('- Vocabulary & Paraphrasing Notes\n')
        f.write('"""\n\n')

        f.write("UNSEEN_TOPICS_FULL_41 = [\n")
        for item in DATA_ITEMS:
            f.write("    {\n")
            f.write(f'        "id": {item["id"]},\n')
            f.write(f'        "slug_id": "{item["slug_id"]}",\n')
            f.write(f'        "title": {repr(item["title"])},\n')
            f.write(f'        "bn_title": {repr(item["bn_title"])},\n')
            f.write(f'        "theme": {repr(item["theme"])},\n')
            f.write(f'        "stars": "{item["stars"]}",\n')
            f.write(f'        "priority": "{item["priority"]}",\n')
            f.write(f'        "boards": "{item["boards"]}",\n')
            f.write(f'        "page_pdf": {item["page_pdf"]},\n')
            f.write(f'        "passage": {repr(item["passage"])},\n')
            f.write(f'        "info_table": {repr(item["info_table"])},\n')
            f.write(f'        "answers": {repr(item["answers"])},\n')
            f.write(f'        "model_summary": {repr(item["model_summary"])},\n')
            f.write(f'        "vocab_notes": {repr(item["vocab_notes"])},\n')
            f.write("    },\n")
        f.write("]\n")

    print(f"[OK] Successfully wrote {OUTPUT_FILE} ({len(DATA_ITEMS)} topics).")

if __name__ == "__main__":
    generate_full_file()
