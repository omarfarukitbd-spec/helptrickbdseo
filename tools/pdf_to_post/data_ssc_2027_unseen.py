#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/pdf_to_post/data_ssc_2027_unseen.py
-------------------------------------------
100% faithful data for Unseen Passages, Information Transfer & Summary Writing (Q4-5).
Contains:
1. All 41 Unseen Topics from Pages 04-05 with priority stars, snippets, and board references.
2. Model 1: Hazrat Omar (R) (Page 05) with passage, Information Transfer table, and full summary.
3. Model 2: 26 March Independence Day (Dakhil 2026, Pages 31-32) with passage, Information Transfer, and summary.
4. Model 3: John Milton (Model Test, Pages 35-36) with passage, Information Transfer, and summary.
"""

UNSEEN_TOPICS_41 = [
    {
        "id": 1,
        "stars": "***",
        "title": "Dear Moly, I know it ............ Hope to hear from you. With Love Orin.",
        "page_pdf": 377,
        "boards": "Dakhil Exam-2024",
        "theme": "Informal Letter / Friendship",
        "priority": "Top Priority"
    },
    {
        "id": 2,
        "stars": "***",
        "title": "Facebook is the leading social ............can comment on their friends' groups.",
        "page_pdf": 378,
        "boards": "Dakhil Exam-2023",
        "theme": "Social Media & Communication",
        "priority": "Top Priority"
    },
    {
        "id": 3,
        "stars": "***",
        "title": "Humayun Ahmed was a teacher ....................He was buried in Nuhash Palli.",
        "page_pdf": 380,
        "boards": "Dakhil Exam-2020",
        "theme": "Biography / Literature & Filmmaking",
        "priority": "Top Priority"
    },
    {
        "id": 4,
        "stars": "***",
        "title": "Humayun was the eldest son.............. feasts and festivities at Agra and Delhi.",
        "page_pdf": 381,
        "boards": "Dakhil Exam-2019",
        "theme": "Mughal History / Emperor Humayun",
        "priority": "Top Priority"
    },
    {
        "id": 5,
        "stars": "***",
        "title": "Interpol is the International............... Interpol was given a new constitution.",
        "page_pdf": 391,
        "boards": "Dakhil Exam-2018",
        "theme": "International Law & Organizations",
        "priority": "Top Priority"
    },
    {
        "id": 6,
        "stars": "***",
        "title": "Captain Mohiuddin Jahangir..................................distinction, Birshrestho.",
        "page_pdf": 393,
        "boards": "D.B. '24",
        "theme": "Liberation War Hero / Bir Shrestha",
        "priority": "Top Priority"
    },
    {
        "id": 7,
        "stars": "**",
        "title": "Munier Chowdhury was born ...................................body could not be identified.",
        "page_pdf": 396,
        "boards": "Standard Board Review",
        "theme": "Martyred Intellectual & Dramatist",
        "priority": "High Priority"
    },
    {
        "id": 8,
        "stars": "*",
        "title": "Munshi Abdur Rouf was.................................................... of bravery in Bangladesh.",
        "page_pdf": 398,
        "boards": "Standard Board Review",
        "theme": "Bir Shrestha Munshi Abdur Rouf",
        "priority": "Moderate"
    },
    {
        "id": 9,
        "stars": "*",
        "title": "Louis Pasteur, was a French ................................................. 28, 1895 at the age of 72.",
        "page_pdf": 411,
        "boards": "Standard Board Review",
        "theme": "Science & Medicine / Vaccination",
        "priority": "Moderate"
    },
    {
        "id": 10,
        "stars": "***",
        "title": "Education plays a vital role..................................................for alleviation of poverty.",
        "page_pdf": 422,
        "boards": "National Board Focus",
        "theme": "Socio-Economic Development",
        "priority": "Top Priority"
    },
    {
        "id": 11,
        "stars": "***",
        "title": "Jibanananda Das was born in................................ died on October 22, 1954.",
        "page_pdf": 425,
        "boards": "C.B. '24",
        "theme": "Bengali Poetry & Literature",
        "priority": "Top Priority"
    },
    {
        "id": 12,
        "stars": "**",
        "title": "Hazrat Muhammad (Sm) is........................................ the success of his teaching.",
        "page_pdf": 426,
        "boards": "Standard Islamic Review",
        "theme": "Life & Teachings of Prophet Muhammad (Sm)",
        "priority": "High Priority"
    },
    {
        "id": 13,
        "stars": "*",
        "title": "Bangladesh is an independent............................................December is our Victory Day.",
        "page_pdf": 431,
        "boards": "Standard Board Review",
        "theme": "National Sovereignty & Victory",
        "priority": "Moderate"
    },
    {
        "id": 14,
        "stars": "**",
        "title": "Charles Babbage was an English ............. in London on 18 October, 1871.",
        "page_pdf": 435,
        "boards": "J.B. '24, B.B. '19, '25",
        "theme": "Father of the Computer",
        "priority": "High Priority"
    },
    {
        "id": 15,
        "stars": "*",
        "title": "Dr. Muhammad Qudrat-E-Khuda.............. and 'Swadhinata Dibas Puraskar' in 1984.",
        "page_pdf": 436,
        "boards": "Dinj.B. '24",
        "theme": "Eminent Scientist & Educationist",
        "priority": "Moderate"
    },
    {
        "id": 16,
        "stars": "*",
        "title": "Tourism in Bangladesh is a............................................. Bagerhat is also a notable site.",
        "page_pdf": 440,
        "boards": "Standard Board Review",
        "theme": "Heritage Tourism & Economy",
        "priority": "Moderate"
    },
    {
        "id": 17,
        "stars": "*",
        "title": "Jagadish Chandra Bose was..............................................contributions and achievements.",
        "page_pdf": 443,
        "boards": "Standard Board Review",
        "theme": "Botanist & Pioneer of Radio Waves",
        "priority": "Moderate"
    },
    {
        "id": 18,
        "stars": "*",
        "title": "Bangladesh is an independent............................................Its currency is also rupee.",
        "page_pdf": 445,
        "boards": "Standard Board Review",
        "theme": "Geography & Neighboring Economies",
        "priority": "Moderate"
    },
    {
        "id": 19,
        "stars": "***",
        "title": "APJ Abdul Kalam was born ............................................role in international relations.",
        "page_pdf": 459,
        "boards": "Standard Board Review",
        "theme": "Missile Man & People's President",
        "priority": "Top Priority"
    },
    {
        "id": 20,
        "stars": "***",
        "title": "Begum Sufia Kamal, poet, ........................................... Dhaka on 20th November 1999.",
        "page_pdf": 463,
        "boards": "Standard Board Review",
        "theme": "Pioneering Female Poet & Activist",
        "priority": "Top Priority"
    },
    {
        "id": 21,
        "stars": "***",
        "title": "The Nobel Prize is the................................................ 1901 for his inventing X-rays.",
        "page_pdf": 464,
        "boards": "Standard Board Review",
        "theme": "Global Laureates & Discoveries",
        "priority": "Top Priority"
    },
    {
        "id": 22,
        "stars": "*",
        "title": "Mount Everest is the highest...................................given honour of world hero.",
        "page_pdf": 470,
        "boards": "D. B. '26",
        "theme": "Mountaineering & Natural Wonders",
        "priority": "Moderate"
    },
    {
        "id": 23,
        "stars": "***",
        "title": "Sher-E-Bangla is one of the ....................................remember him with gratitude.",
        "page_pdf": 472,
        "boards": "Syl. B. '24",
        "theme": "Historic Statesman AK Fazlul Huq",
        "priority": "Top Priority"
    },
    {
        "id": 24,
        "stars": "*",
        "title": "Hazrat Ali (R) was born on 20.............................died two days later on 27 January 661.",
        "page_pdf": 475,
        "boards": "C.B. '15",
        "theme": "Fourth Caliph of Islam",
        "priority": "Moderate"
    },
    {
        "id": 25,
        "stars": "**",
        "title": "Cricket is one of the most ..................................................... the 6th World Cup Cricket.",
        "page_pdf": 477,
        "boards": "Standard Board Review",
        "theme": "Sports History & Bangladesh Cricket",
        "priority": "High Priority"
    },
    {
        "id": 26,
        "stars": "**",
        "title": "Altaf Mahmud was a musician, cultural ................... culture and the War of Liberation.",
        "page_pdf": 478,
        "boards": "C.B. '19",
        "theme": "Composer of 'Amar Bhaier Rokte Rangano'",
        "priority": "High Priority"
    },
    {
        "id": 27,
        "stars": "**",
        "title": "Dengue fever is a virus .......................................................... for prevention of this disease.",
        "page_pdf": 480,
        "boards": "Health Board Focus",
        "theme": "Epidemiology & Public Health",
        "priority": "High Priority"
    },
    {
        "id": 28,
        "stars": "***",
        "title": "Hazrat Muhammad (Sm) ........................................ is known as Hizrat.",
        "page_pdf": 484,
        "boards": "Dakhil Exam. '25",
        "theme": "The Historic Migration (Hijrah)",
        "priority": "Top Priority"
    },
    {
        "id": 29,
        "stars": "***",
        "title": "Jasimuddin was a famous ......................................... home at Gobindapur.",
        "page_pdf": 505,
        "boards": "B.B. '23, Chat.B. '25",
        "theme": "Polli Kobi Jasimuddin / Rural Poetry",
        "priority": "Top Priority"
    },
    {
        "id": 30,
        "stars": "**",
        "title": "Bangladesh is situated in ............................................................ are living peacefully here.",
        "page_pdf": 508,
        "boards": "Standard Board Review",
        "theme": "Communal Harmony & Geography",
        "priority": "High Priority"
    },
    {
        "id": 31,
        "stars": "**",
        "title": "Emperor Babur is known as.....................................................age of 47 on January 5, 1531.",
        "page_pdf": 510,
        "boards": "Standard Board Review",
        "theme": "Founder of the Mughal Empire",
        "priority": "High Priority"
    },
    {
        "id": 32,
        "stars": "**",
        "title": "William Wordsworth was .................................................... published nothing new in poetry.",
        "page_pdf": 521,
        "boards": "Standard Board Review",
        "theme": "Romantic Nature Poet",
        "priority": "High Priority"
    },
    {
        "id": 33,
        "stars": "***",
        "title": "Global warming is the rise .....................................................warming is not controlled.",
        "page_pdf": 537,
        "boards": "Environment Focus",
        "theme": "Climate Crisis & Greenhouse Impact",
        "priority": "Top Priority"
    },
    {
        "id": 34,
        "stars": "**",
        "title": "Abul Qasem Fazlul Haq.................................................All Indian Muslim League.",
        "page_pdf": 539,
        "boards": "R.B. '24",
        "theme": "Lahore Resolution & Bengali Rights",
        "priority": "High Priority"
    },
    {
        "id": 35,
        "stars": "**",
        "title": "Taj Mahal, one of the seven ......................................... of Iltutmish and an Iron Pillar.",
        "page_pdf": 551,
        "boards": "Standard Board Review",
        "theme": "Architectural Wonder of the World",
        "priority": "High Priority"
    },
    {
        "id": 36,
        "stars": "**",
        "title": "Dhaka is a very ancient and .................................................... war of liberation in 1971.",
        "page_pdf": 559,
        "boards": "Standard Board Review",
        "theme": "Historic City of Dhaka",
        "priority": "High Priority"
    },
    {
        "id": 37,
        "stars": "*",
        "title": "Shah Jahan was one of............................................................eight years till his death.",
        "page_pdf": 569,
        "boards": "Standard Board Review",
        "theme": "Emperor Shah Jahan & Captivity",
        "priority": "Moderate"
    },
    {
        "id": 38,
        "stars": "***",
        "title": "Kazi Nazrul Islam is the ........................................................... where he died in 1976.",
        "page_pdf": 571,
        "boards": "Standard Board Review",
        "theme": "National Poet of Bangladesh",
        "priority": "Top Priority"
    },
    {
        "id": 39,
        "stars": "*",
        "title": "Electronic mail, most commonly.......................................... specific meaning it has today.",
        "page_pdf": 573,
        "boards": "Standard Board Review",
        "theme": "Evolution of Digital Communication",
        "priority": "Moderate"
    },
    {
        "id": 40,
        "stars": "***",
        "title": "SAARC is a regional ............................................. the neighboring countries.",
        "page_pdf": 589,
        "boards": "Dinj.B. '25, '26",
        "theme": "South Asian Regional Cooperation",
        "priority": "Top Priority"
    },
    {
        "id": 41,
        "stars": "***",
        "title": "Hazrat Omar (R) was the second Caliph of Islam. He is well-known to all of us for his nobility and justice.",
        "page_pdf": 228,
        "boards": "Featured Model Passage (Page 05)",
        "theme": "Justice, Compassion and Leadership in Islam",
        "priority": "Top Priority (Full Model Set)"
    }
]

# ─────────────────────────────────────────────────────────────────────────────
# MODEL 1: HAZRAT OMAR (R) (Page 05)
# ─────────────────────────────────────────────────────────────────────────────
MODEL_01_HAZRAT_OMAR = {
    "source": "Suggestion Model Unseen Passage (Page 05)",
    "passage": (
        "Hazrat Omar (R) was the second Caliph of Islam. He is well-known to all of us for his nobility and justice. "
        "As a great Muslim ruler, his fame spread all over the world. Hazrat Omar (R) used to go at night to see the "
        "condition of his country men. One night he was passing by the house of a widow. The widow's children were crying "
        "very loudly. The Caliph reached the house and knocked at the door. He asked her why the children were crying. "
        "The poor woman replied that they were crying for food. She also told Caliph that she was pretending to prepare "
        "food for them. But she was boiling only water. There was no food in her house. The Caliph Omar (R) became very "
        "much shocked at this. The kind Caliph rushed to the Baitulmal at once. He himself put a sack full of flour on his "
        "shoulder and started for the widow's house.\n"
        "On the way he met one of his servants. The servant recognized Caliph and told — \"Master, let me carry your burden.\""
    ),
    "info_transfer_table": {
        "headers": ["Who / What", "Event / Activity", "Time", "Place"],
        "rows": [
            ["Hazrat Omar (R)", "checked on countrymen", "(i) [......]", "his territory"],
            ["(ii) [......]", "cried for food", "one night", "widow's house"],
            ["The widow", "(iii) [......]", "one night", "her house"],
            ["The Caliph", "carried rice sack", "", "(iv) [......]"],
            ["(v) [......]", "offered help", "", "on the street"]
        ]
    },
    "info_transfer_answers": {
        "i": "at night",
        "ii": "Widow's children / The children",
        "iii": "boiled only water / pretended to cook",
        "iv": "from Baitulmal / to widow's house",
        "v": "A servant / One of his servants"
    },
    "model_summary": (
        "Hazrat Omar (R) was a famous and just Caliph of Islam who routinely surveyed his territory at night to protect "
        "his people. One evening, he discovered a poverty-stricken widow boiling plain water to comfort her starving children. "
        "Deeply distressed, the compassionate ruler immediately hurried to the state treasury (Baitulmal), personally carried "
        "a heavy bag of flour on his own back, and brought it to the distressed family without delay."
    )
}

# ─────────────────────────────────────────────────────────────────────────────
# MODEL 2: 26 MARCH INDEPENDENCE DAY (Dakhil 2026 Board Exam, Pages 31-32)
# ─────────────────────────────────────────────────────────────────────────────
MODEL_02_INDEPENDENCE_DAY = {
    "source": "Dakhil Examination 2026 (Board Question Paper, Pages 31-32)",
    "passage": (
        "26 March, our Independence Day, is the biggest state festival. The day is celebrated every year in the country "
        "with great enthusiasm and fervour. It is a national holiday. All offices, educational institutions, shops and "
        "factories remain closed on this day. The day begins with 31 gun salute. Early in the morning the President and "
        "the Prime Minister, on behalf of the nation place floral wreaths at the National Mausoleum at Savar. Then other "
        "leaders, diplomats, political parties, social and cultural organizations, educational institutions and freedom "
        "fighters pay homage to the martyrs. People from all walks of life also go there in rallies and processions. There "
        "are many cultural programmes throughout the day, highlighting the heroic struggle and sacrifice in 1971."
    ),
    "info_transfer_table": {
        "headers": ["Who / What", "Event / Activity", "Time / When", "Place / Where"],
        "rows": [
            ["(i) [......]", "is the biggest state festival", "", "in our country"],
            ["The day is", "(ii) [......]", "every year", "in the country"],
            ["All offices and educational institutions", "remain closed", "(iii) [......]", ""],
            ["The President and the Prime Minister", "place floral wreaths", "(iv) [......]", "at the National mausoleum"],
            ["People from all walks of life", "(v) [......]", "throughout the day", ""]
        ]
    },
    "info_transfer_answers": {
        "i": "26 March / Independence Day",
        "ii": "celebrated with great enthusiasm and fervour",
        "iii": "on 26 March / on this day",
        "iv": "early in the morning",
        "v": "go in rallies and processions / attend cultural programmes"
    },
    "model_summary": (
        "26 March is the Independence Day and the most momentous national festival of Bangladesh, observed nationwide as "
        "a public holiday. Commencing with a 31-gun salute, dignitaries led by the President and Prime Minister lay floral "
        "wreaths at the National Memorial at Savar to honour the 1971 martyrs. Citizens from all walks of life participate "
        "in vibrant processions and patriotic cultural events commemorating the historic liberation struggle."
    )
}

# ─────────────────────────────────────────────────────────────────────────────
# MODEL 3: JOHN MILTON (Exclusive Model Test, Pages 35-36)
# ─────────────────────────────────────────────────────────────────────────────
MODEL_03_JOHN_MILTON = {
    "source": "Exclusive Model Test (Exam 2027 Pattern, Pages 35-36)",
    "passage": (
        "John Milton was one of the famous poets in English literature. He was born on December 9, 1608 in London. "
        "At the age of 17, he went to Cambridge University for study and after seven years of study, he obtained his "
        "MA degree from that University. The next six years, he spent at Horton in unprofessional study. In 1638, he "
        "started his foreign tour. In 1642, he married Mary Powell, a young girl of seventeen. But his wife died in 1652 "
        "leaving him with three daughters. So, he married second time in 1656, but two years after his second wife also "
        "died. Of all his works 'Paradise Lost' is said to be his greatest. He finished composing this great epic in 1663. "
        "But it was published four years later. By this time, he lost his eyesight. At the age of 66, he died on "
        "November 8, 1674."
    ),
    "info_transfer_table": {
        "aims": "Focusing on his personal life and literary work.",
        "lifespan": "66 years.",
        "headers": ["Who / What", "Event", "Year / Time", "Place", "Whom"],
        "rows": [
            ["Milton", "(i) [......]", "1608", "London", ""],
            ["He", "passed MA", "(ii) [......]", "(iii) [......]", ""],
            ["He", "married", "1642", "", "(iv) [......]"],
            ["Paradise Lost", "published", "(v) [......]", "London", ""]
        ]
    },
    "info_transfer_answers": {
        "i": "was born",
        "ii": "in 1632 / at the age of 24 / after seven years",
        "iii": "Cambridge University",
        "iv": "Mary Powell",
        "v": "in 1667 (1663 + 4 years later)"
    },
    "model_summary": (
        "John Milton (1608–1674) was a celebrated English poet who earned his MA from Cambridge University and pursued "
        "intensive classical studies. Despite personal tragedies, including the loss of two wives and total blindness, "
        "he persevered to compose the monumental Christian epic 'Paradise Lost' in 1663, which was published in London "
        "in 1667 and solidified his enduring literary legacy."
    )
}
