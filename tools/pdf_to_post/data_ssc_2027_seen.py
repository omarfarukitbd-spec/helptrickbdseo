#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/pdf_to_post/data_ssc_2027_seen.py
-----------------------------------------
100% faithful data for Seen Passages (Q1-3) from the 37-page scanned PDF.
Contains:
1. All 33 Seen Passages (Unit, Lesson, Title Snippet, Stars, Board Years)
2. Dakhil 2026 Model (Zahir Raihan, Pages 30-31) complete with MCQ, Q/A, Gap Fill
3. Exclusive Model Test (Climate Change, Pages 34-35) complete with MCQ, Q/A, Gap Fill
"""

SEEN_PASSAGES_33 = [
    {
        "id": 1,
        "stars": "***",
        "title": "Meherjan lives in a slum on the ........... in our towns and villages every year.",
        "unit": "Unit-2",
        "lesson": "Lesson-1(A)",
        "page_pdf": 25,
        "boards": "Ctg.B., Dinj.B. '19, B.B. '22, J.B. '23, C. B., Syl. B., M. B. '26",
        "priority": "Top Priority (Most Probable)"
    },
    {
        "id": 2,
        "stars": "*",
        "title": "Bangladesh is now in the grip of ............. help prevent soil and pollution.",
        "unit": "Unit-2",
        "lesson": "Lesson-2(B)",
        "page_pdf": 32,
        "boards": "J. B. '26",
        "priority": "Moderate"
    },
    {
        "id": 3,
        "stars": "***",
        "title": "Humans can neither change the sun's ............ dioxide when we clear forests.",
        "unit": "Unit-2",
        "lesson": "Lesson-3(A)",
        "page_pdf": 38,
        "boards": "D. B., Ctg. B. '26",
        "priority": "Top Priority (Most Probable)"
    },
    {
        "id": 4,
        "stars": "**",
        "title": "LET'S SAVE OUR PLANET! Everyone ......... old cans to make new ones.",
        "unit": "Unit-2",
        "lesson": "Lesson-5(B)",
        "page_pdf": 51,
        "boards": "Syl.B. '22, R. B. '26",
        "priority": "High Priority"
    },
    {
        "id": 5,
        "stars": "*",
        "title": "Hi, I'm Shyam. I'm from Magura.......... will be my most favourite pastime.",
        "unit": "Unit-3",
        "lesson": "Lesson-1(G)",
        "page_pdf": 60,
        "boards": "B. B. '26",
        "priority": "Moderate"
    },
    {
        "id": 6,
        "stars": "**",
        "title": "Childhood outdoor pastimes ................. and learning outside the classroom.\"",
        "unit": "Unit-3",
        "lesson": "Lesson-3(A)",
        "page_pdf": 69,
        "boards": "Dinj. B. '26",
        "priority": "High Priority"
    },
    {
        "id": 7,
        "stars": "***",
        "title": "May Day or International Workers' ................... better pay and better lives.",
        "unit": "Unit-4",
        "lesson": "Lesson-2(B)",
        "page_pdf": 84,
        "boards": "Dakhil Exam-2019; C.B. '24, D.B. '20, '22, '25, Dinj.B. '25",
        "priority": "Top Priority (Most Probable)"
    },
    {
        "id": 8,
        "stars": "***",
        "title": "21 February is a memorable day in our national .......... of independence movement of Bangladesh.",
        "unit": "Unit-4",
        "lesson": "Lesson-3(B)",
        "page_pdf": 90,
        "boards": "Dakhil Exam-2017; R.B. '23",
        "priority": "Top Priority (Most Probable)"
    },
    {
        "id": 9,
        "stars": "**",
        "title": "21 February is observed as ...... and cultural diversity and multilingualism.",
        "unit": "Unit-4",
        "lesson": "Lesson-4(B)",
        "page_pdf": 95,
        "boards": "Dakhil Exam-2022; C.B. '19",
        "priority": "High Priority"
    },
    {
        "id": 10,
        "stars": "***",
        "title": "26 March, our Independence Day ................. in other places in the country.",
        "unit": "Unit-4",
        "lesson": "Lesson-5(B)",
        "page_pdf": 100,
        "boards": "J.B. '19, Syl. B. '19, '20; Dinj.B., B.B. '20; D.B. '23",
        "priority": "Top Priority (Most Probable)"
    },
    {
        "id": 11,
        "stars": "*",
        "title": "'Pahela Boishakh' is the first ........... of cultural unity for the whole nation.",
        "unit": "Unit-4",
        "lesson": "Lesson-6(B)",
        "page_pdf": 107,
        "boards": "Dakhil Exam-2018, B.B. '23",
        "priority": "Moderate"
    },
    {
        "id": 12,
        "stars": "*",
        "title": "\"Is there anybody here who .......... Jamil. \"You did the right thing, Jamil.\"",
        "unit": "Unit-5",
        "lesson": "Lesson-1(B)",
        "page_pdf": 112,
        "boards": "Standard Textbook Review",
        "priority": "Moderate"
    },
    {
        "id": 13,
        "stars": "*",
        "title": "The class comes up with different ......... houses built here and there.\"",
        "unit": "Unit-5",
        "lesson": "Lesson-3(C)",
        "page_pdf": 116,
        "boards": "Standard Textbook Review",
        "priority": "Moderate"
    },
    {
        "id": 14,
        "stars": "*",
        "title": "In the next class Ms Choudhury ...... Carmichael College, Rangpur.",
        "unit": "Unit-5",
        "lesson": "Lesson-4(B)",
        "page_pdf": 122,
        "boards": "R.B. '22",
        "priority": "Moderate"
    },
    {
        "id": 15,
        "stars": "**",
        "title": "\"Today there are many jobs ........ see how we can learn English.\"",
        "unit": "Unit-5",
        "lesson": "Lesson-5(D)",
        "page_pdf": 127,
        "boards": "C.B. '22",
        "priority": "High Priority"
    },
    {
        "id": 16,
        "stars": "**",
        "title": "The Republic of Maldives is an island...................... the country assumed its present name.",
        "unit": "Unit-6",
        "lesson": "Lesson-3(B)",
        "page_pdf": 144,
        "boards": "Standard Board Review",
        "priority": "High Priority"
    },
    {
        "id": 17,
        "stars": "*",
        "title": "The Maldives is famous as a.......... to cut their carbon emissions.",
        "unit": "Unit-6",
        "lesson": "Lesson-3(B)",
        "page_pdf": 148,
        "boards": "D.B. '19",
        "priority": "Moderate"
    },
    {
        "id": 18,
        "stars": "*",
        "title": "Bhutan is called the Jewel of ............. eighth happiest country in the world.",
        "unit": "Unit-6",
        "lesson": "Lesson-5(A)",
        "page_pdf": 158,
        "boards": "Standard Board Review",
        "priority": "Moderate"
    },
    {
        "id": 19,
        "stars": "*",
        "title": "Zainul Abedin (29 December, 1914 ....... away on 28 May, 1976 in Dhaka.",
        "unit": "Unit-7",
        "lesson": "Lesson-1(B)",
        "page_pdf": 164,
        "boards": "Standard Board Review",
        "priority": "Moderate"
    },
    {
        "id": 20,
        "stars": "**",
        "title": "Culturally rich Bangladesh is ........... out from the dream institution. ........",
        "unit": "Unit-7",
        "lesson": "Lesson-2(B)",
        "page_pdf": 174,
        "boards": "Standard Board Review",
        "priority": "High Priority"
    },
    {
        "id": 21,
        "stars": "**",
        "title": "It was late summer, 26 August ....................... of the poor in the slums of Kolkata.",
        "unit": "Unit-7",
        "lesson": "Lesson-3(B)",
        "page_pdf": 181,
        "boards": "Ctg. B. '24",
        "priority": "High Priority"
    },
    {
        "id": 22,
        "stars": "**",
        "title": "Mother Teresa was moved by the ....................... smile, lives on in our mind.",
        "unit": "Unit-7",
        "lesson": "Lesson-5(A)",
        "page_pdf": 186,
        "boards": "R.B. '20, M.B. '22, Ctg.B. '23, '25",
        "priority": "High Priority"
    },
    {
        "id": 23,
        "stars": "*",
        "title": "Steven Paul Jobs (24 February .......... in 2006, when Disney acquired Pixar.",
        "unit": "Unit-7",
        "lesson": "Lesson-6(B)",
        "page_pdf": 191,
        "boards": "Standard Board Review",
        "priority": "Moderate"
    },
    {
        "id": 24,
        "stars": "***",
        "title": "'Heritage' is what we inherit ....... best architectural beauties of Bangladesh.",
        "unit": "Unit-8",
        "lesson": "Lesson-1(B)",
        "page_pdf": 202,
        "boards": "Dakhil Exam-2020; M.B., J.B., Ctg.B. '20, Dinj.B. '24, R.B., J.B. '25",
        "priority": "Top Priority (Most Probable)"
    },
    {
        "id": 25,
        "stars": "*",
        "title": "Paharpur is an important archaeological ............... downs of its benefactors.",
        "unit": "Unit-8",
        "lesson": "Lesson-2(A)",
        "page_pdf": 209,
        "boards": "Standard Board Review",
        "priority": "Moderate"
    },
    {
        "id": 26,
        "stars": "*",
        "title": "The French sculptor Frederic ........ of Liberty from anywhere in the world.",
        "unit": "Unit-8",
        "lesson": "Lesson-3(D)",
        "page_pdf": 217,
        "boards": "Standard Board Review",
        "priority": "Moderate"
    },
    {
        "id": 27,
        "stars": "**",
        "title": "Pritilata Waddedar was born in........ she couldn't see it during her lifetime.",
        "unit": "Unit-10",
        "lesson": "Lesson-3(B)",
        "page_pdf": 241,
        "boards": "Standard Board Review",
        "priority": "High Priority"
    },
    {
        "id": 28,
        "stars": "***",
        "title": "Eid is the main religious festival............... makes them feel empty and lost.",
        "unit": "Unit-12",
        "lesson": "Lesson-1(B)",
        "page_pdf": 279,
        "boards": "Dakhil Exam. '25, M.B. '23, '25",
        "priority": "Top Priority (Most Probable)"
    },
    {
        "id": 29,
        "stars": "***",
        "title": "Mainul Islam is a qualified farmer .............. to be respectful of their roots.",
        "unit": "Unit-12",
        "lesson": "Lesson-2(D)",
        "page_pdf": 285,
        "boards": "SSC All Boards '18, C.B. '23",
        "priority": "Top Priority (Most Probable)"
    },
    {
        "id": 30,
        "stars": "**",
        "title": "Michael Madhusudan Dutt ............. Bangla epic Meghnad Badh Kabya.",
        "unit": "Unit-12",
        "lesson": "Lesson-3(A)",
        "page_pdf": 291,
        "boards": "Dinj.B. '23, M.B. '24",
        "priority": "High Priority"
    },
    {
        "id": 31,
        "stars": "*",
        "title": "In a speech at the 90th Science ............. of mankind in the 21st century.",
        "unit": "Unit-14",
        "lesson": "Lesson-1(B)",
        "page_pdf": 332,
        "boards": "Standard Board Review",
        "priority": "Moderate"
    },
    {
        "id": 32,
        "stars": "***",
        "title": "Countries of the world rely ................... can be used as energy source too.",
        "unit": "Unit-14",
        "lesson": "Lesson-2(B)",
        "page_pdf": 338,
        "boards": "Ctg.B. '22, B.B. '24, Syl.B. '25",
        "priority": "Top Priority (Most Probable)"
    },
    {
        "id": 33,
        "stars": "***",
        "title": "The Internet technology has helped............. should be shared with others.",
        "unit": "Unit-15",
        "lesson": "Lesson-2(B)",
        "page_pdf": 352,
        "boards": "R.B. '19, C.B. '20, D.B., J.B., Syl.B. '24",
        "priority": "Top Priority (Most Probable)"
    }
]

# ─────────────────────────────────────────────────────────────────────────────
# DAKHIL 2026 BOARD EXAM PAPER (Pages 30-31)
# ─────────────────────────────────────────────────────────────────────────────
DAKHIL_2026_SEEN_MODEL = {
    "source": "Dakhil Examination 2026 (Board Question)",
    "passage": (
        "Zahir Raihan was one of the most talented film makers in Bangladesh. He was born on 19 August 1935 in the "
        "village Majupur in Feni district. He was an active worker of the Language Movement. He was one of the ten "
        "students to go out in a procession on 21 February 1952 despite a ban on such activities imposed by the "
        "authorities. As a result, he and many others were arrested and taken to prison. Raihan was also present at the "
        "historical meeting of Amtala on 21 February 1952. He also took part in the mass movement in 1969. In 1971, he "
        "joined the Liberation War. All through his life, Zahir Raihan dreamt for a democratic society, a society that "
        "would ensure freedom of speech. He had many dreams about our film industry too. He made a legendary film "
        "\"Jibon Theke Neya\" based on the Language Movement of 1952. It was a protest against the autocratic "
        "government then ruling our country. The family portrayed in that film symbolically represented East Pakistan. "
        "The family was ruled by an autocrat who had to go to prison for her conspiracy. During the Liberation War in 1971, "
        "this film was shown outside Bangladesh. Celebrated film makers like Satyajit Ray, Mrinal Sen, and Ritwik Ghatak "
        "appreciated the film. Raihan gave all the money the film made to the Freedom Fighters' trust.\n"
        "Besides, his great documentary on Pakistani atrocities, \"Stop Genocide\", helped create world sentiment in "
        "favour of our Liberation War.\n"
        "On 30 December 1971, someone informed Raihan about an address somewhere at Mirpur where he might find "
        "his brother, the famous writer Shahidullah Kaiser, who had gone missing from 14 December 1971. Kaiser was "
        "captured and killed by the Pakistani army and the local collaborators during the last days of the war. "
        "Accordingly, Raihan left home to get his brother back but he never returned.\n"
        "Zahir Raihan's dream was fulfilled. But it's a pity that this dreamer could not live to see his dream come true."
    ),
    "mcq_questions": [
        {
            "id": "a",
            "question": "Zahir Raihan's dream was —.",
            "options": ["(i) a developed country", "(ii) a rich society", "(iii) a democratic society", "(iv) a Pakistani society"],
            "answer": "(iii) a democratic society",
            "explanation": "According to the text: 'All through his life, Zahir Raihan dreamt for a democratic society, a society that would ensure freedom of speech.'"
        },
        {
            "id": "b",
            "question": "When was the Language Movement held?",
            "options": ["(i) 16 December 1971", "(ii) 26 March 1972", "(iii) 25 March 1971", "(iv) 21 February 1952"],
            "answer": "(iv) 21 February 1952",
            "explanation": "The procession was carried out on 21 February 1952 despite the ban."
        },
        {
            "id": "c",
            "question": "Who participated in the mass movement and when?",
            "options": [
                "(i) Shahidullah Kaiser in 1972",
                "(ii) Zahir Raihan on 16 December, 1971",
                "(iii) Zainul Abedeen in 1975",
                "(iv) Zahir Raihan in 1969"
            ],
            "answer": "(iv) Zahir Raihan in 1969",
            "explanation": "Text confirms: 'He also took part in the mass movement in 1969.'"
        },
        {
            "id": "d",
            "question": "What does the word 'talented' mean?",
            "options": ["(i) Meritorious", "(ii) Defame", "(iii) Graceful", "(iv) Happy"],
            "answer": "(i) Meritorious",
            "explanation": "'Talented' means possessing natural gift or ability, synonymous with 'meritorious' or 'gifted'."
        },
        {
            "id": "e",
            "question": "The home district of Zahir Raihan is —.",
            "options": ["(i) Madaripur", "(ii) Bagherhat", "(iii) Feni", "(iv) Dhaka"],
            "answer": "(iii) Feni",
            "explanation": "Born in village Majupur in Feni district."
        },
        {
            "id": "f",
            "question": "Zahir Raihan's legendary film \"Jibon Theke Neya\" was based on —.",
            "options": [
                "(i) the Language Movement",
                "(ii) the Liberation War",
                "(iii) Anti-British Movement",
                "(iv) mass movement"
            ],
            "answer": "(i) the Language Movement",
            "explanation": "The text states: 'He made a legendary film \"Jibon Theke Neya\" based on the Language Movement of 1952.'"
        },
        {
            "id": "g",
            "question": "When had Shahidullah Kaiser gone missing?",
            "options": ["(i) 13 February 1971", "(ii) 16 December 1971", "(iii) 14 December 1971", "(iv) 26 March 1971"],
            "answer": "(iii) 14 December 1971",
            "explanation": "Text confirms: '...his brother, the famous writer Shahidullah Kaiser, who had gone missing from 14 December 1971.'"
        }
    ],
    "open_questions": [
        {
            "id": "a",
            "question": "What do you know about Zahir Raihan?",
            "answer": "Zahir Raihan was one of the most talented filmmakers, writers, and cultural activists of Bangladesh. Born on 19 August 1935 in Feni, he actively participated in the Language Movement of 1952, the 1969 mass uprising, and the 1971 Liberation War through his visionary cinema."
        },
        {
            "id": "b",
            "question": "Why was he arrested?",
            "answer": "He was arrested because on 21 February 1952, he was among the brave group of ten students who defied Section 144 and led a procession demanding state language status for Bengali."
        },
        {
            "id": "c",
            "question": "When did he take part in the mass movement?",
            "answer": "Zahir Raihan took an active part in the historic mass movement against the Pakistani autocracy in 1969."
        },
        {
            "id": "d",
            "question": "What is \"Jibon Theke Neya\"?",
            "answer": "\"Jibon Theke Neya\" is a legendary political satirical film directed by Zahir Raihan based on the 1952 Language Movement. Through an autocratic family household, it symbolically portrayed the totalitarian Pakistani regime and East Pakistan's struggle for liberation."
        },
        {
            "id": "e",
            "question": "Why is Zahir Raihan considered a freedom fighter though he was a film maker?",
            "answer": "Zahir Raihan is considered a freedom fighter because he contributed directly to the Liberation War by donating all proceeds from 'Jibon Theke Neya' to the Freedom Fighters' Trust and making the world-renowned documentary 'Stop Genocide' to rally global support against Pakistani atrocities."
        }
    ],
    "gap_fill": {
        "text": "Zahir Raihan was an active (a) [......] of the Language Movement. He (b) [......] in the mass movement and also joined in the Liberation War. He desired a democratic society that will (c) [......] freedom of speech. He worked to organise world (d) [......] by his great documentary 'Stop Genocide'. He (e) [......] his life for the freedom of the country.",
        "answers": {
            "a": "worker / activist / participant",
            "b": "participated / took part",
            "c": "ensure / guarantee",
            "d": "sentiment / opinion / support",
            "e": "sacrificed / gave / dedicated"
        }
    }
}

# ─────────────────────────────────────────────────────────────────────────────
# EXCLUSIVE MODEL TEST (Pages 34-35)
# ─────────────────────────────────────────────────────────────────────────────
EXCLUSIVE_MODEL_TEST_SEEN = {
    "source": "Exclusive Model Test (Exam 2027 Pattern)",
    "passage": (
        "Humans can neither change the sun's radiation nor the earth's orbit around the sun. But they can control the "
        "increase in the amount of greenhouse gases and its effect on the atmosphere. Only during the last hundred years "
        "the carbon dioxide concentration has been raised alarmingly in the atmosphere and we humans can be held "
        "responsible for this. The main cause of the increase in carbon dioxide level in the atmosphere is the burning of "
        "fossil fuels. Since the end of the 19th century, industrial activities increased rapidly giving rise to many "
        "factories. These factories required energy, which was produced through the combustion of coal. Besides coal, "
        "other sources of energy such as mineral oil and natural gas were also burned to heat our houses, run cars and "
        "airplanes or to produce electricity. Nowadays, about 85 million barrels of crude oil are burned daily. Every time "
        "a fossil raw material is burned, it releases carbon dioxide into the air.\n"
        "Therefore, it is clear that more and more greenhouse gases like carbon dioxide are being generated worldwide "
        "by humans. Moreover, we are also strengthening the greenhouse effect by deforestation, which means cutting "
        "down trees. Trees that are burned up release large volumes of carbon dioxide gas into the air. On the other hand, "
        "as forests absorb a lot of carbon dioxide from the air and deliver oxygen instead, we also destroy an important "
        "storehouse of carbon dioxide when we clear forests."
    ),
    "mcq_questions": [
        {
            "id": "a",
            "question": "What has alarmingly increased in the atmosphere over the last hundred years?",
            "options": ["(i) Oxygen", "(ii) Carbon dioxide", "(iii) Nitrogen", "(iv) Hydrogen"],
            "answer": "(ii) Carbon dioxide",
            "explanation": "Text: 'Only during the last hundred years the carbon dioxide concentration has been raised alarmingly in the atmosphere...'"
        },
        {
            "id": "b",
            "question": "What is the main source of carbon dioxide emission?",
            "options": ["(i) Solar energy", "(ii) Burning of fossil fuels", "(iii) Wind power", "(iv) Hydropower"],
            "answer": "(ii) Burning of fossil fuels",
            "explanation": "Text: 'The main cause of the increase in carbon dioxide level in the atmosphere is the burning of fossil fuels.'"
        },
        {
            "id": "c",
            "question": "What is another major greenhouse gas besides carbon dioxide?",
            "options": ["(i) Nitrogen", "(ii) Methane", "(iii) Argon", "(iv) Oxygen"],
            "answer": "(ii) Methane",
            "explanation": "Methane is universally classified as a potent greenhouse gas along with carbon dioxide."
        },
        {
            "id": "d",
            "question": "How many barrels of crude oil are burned every day?",
            "options": ["(i) 85,000", "(ii) 850,000", "(iii) 85 million", "(iv) 8.5 billion"],
            "answer": "(iii) 85 million",
            "explanation": "Text: 'Nowadays, about 85 million barrels of crude oil are burned daily.'"
        },
        {
            "id": "e",
            "question": "Why are greenhouse gases harmful?",
            "options": ["(i) They increase oxygen levels.", "(ii) They trap heat.", "(iii) They cool the Earth.", "(iv) They absorb sunlight."],
            "answer": "(ii) They trap heat.",
            "explanation": "Greenhouse gases trap thermal radiation in the atmosphere, leading to global warming."
        },
        {
            "id": "f",
            "question": "What does \"storehouse of carbon dioxide\" refer to?",
            "options": ["(i) Atmosphere", "(ii) Oceans", "(iii) Forests", "(iv) Fossil fuels"],
            "answer": "(iii) Forests",
            "explanation": "Text explicitly says: 'as forests absorb a lot of carbon dioxide... we destroy an important storehouse of carbon dioxide when we clear forests.'"
        },
        {
            "id": "g",
            "question": "What term refers to the energy source used by factories?",
            "options": ["(i) Renewable energy", "(ii) Fossil fuels", "(iii) Nuclear energy", "(iv) Solar energy"],
            "answer": "(ii) Fossil fuels",
            "explanation": "Text notes factories produced energy through combustion of coal, mineral oil, and natural gas (fossil fuels)."
        }
    ],
    "open_questions": [
        {
            "id": "a",
            "question": "What are the two major activities responsible for releasing carbon dioxide into the atmosphere?",
            "answer": "The two major human activities responsible for emitting carbon dioxide are the combustion of fossil fuels (coal, crude oil, natural gas) in industries/vehicles, and widespread deforestation."
        },
        {
            "id": "b",
            "question": "What is the relationship between trees and carbon dioxide?",
            "answer": "Trees act as a natural storehouse for carbon by absorbing carbon dioxide from the air and replenishing it with oxygen through photosynthesis. Burning or clearing trees releases that stored carbon back into the atmosphere."
        },
        {
            "id": "c",
            "question": "How does the burning of fossil fuels affect the earth's atmosphere?",
            "answer": "Burning fossil fuels releases massive amounts of carbon dioxide and other greenhouse gases into the atmosphere, which trap heat and cause global warming and unpredictable climate changes."
        },
        {
            "id": "d",
            "question": "What steps can humans take to control greenhouse gas emissions?",
            "answer": "Humans can transition to renewable energy sources (solar, wind, hydroelectric), adopt energy-efficient technology, reduce reliance on crude oil and coal, stop deforestation, and initiate massive afforestation campaigns."
        },
        {
            "id": "e",
            "question": "Why do industrial activities rely heavily on coal and crude oil?",
            "answer": "Since the end of the 19th century, industrial activities expanded rapidly and relied on coal and crude oil because they provided readily available, concentrated energy required to power machinery, heat factories, and generate electricity."
        }
    ],
    "gap_fill": {
        "text": "Fossil fuels are burned at an alarming rate due to (a) [......]. Coal is one of the fuels used for (b) [......] energy. Our atmosphere is being polluted for the (c) [......] of greenhouse gases day by day. Our (d) [......] on fossil fuels should be reduced. We should not destroy our (e) [......] which play a vital role to produce oxygen.",
        "answers": {
            "a": "industrialization / rapid industrial growth",
            "b": "generating / producing",
            "c": "emission / concentration / increase",
            "d": "dependence / reliance",
            "e": "forests / trees"
        }
    }
}
