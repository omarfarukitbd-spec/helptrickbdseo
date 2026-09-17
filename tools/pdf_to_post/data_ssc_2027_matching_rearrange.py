#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/pdf_to_post/data_ssc_2027_matching_rearrange.py
-------------------------------------------------------
100% faithful data for Sentence Matching Table (Q6) & Re-arranging Sentences (Q7).
Contains:
1. All 32 Matching Tables (Cols A, B, C & Solved Sentences) from PDF Pages 05-15
2. Dakhil 2026 Board Exam Matching (Madhusudan Dutt) & Rearrange (Prophet Sm & Poor Beggar)
3. Exclusive Model Test Matching (Facebook) & Rearrange (Fleming & Penicillin)
4. All 36 Re-arranging Sentences (Jumbled a-h, Sequence Keys, and Coherent Paragraphs) from Pages 16-22
"""

MATCHING_TABLES_32 = [
    {
        "id": 1,
        "title": "Emperor Shahjahan and the Taj Mahal",
        "board": "Dakhil Exam-2019, 2024",
        "col_a": [
            "(a) Emperor Shahjahan",
            "(b) It",
            "(c) There",
            "(d) People",
            "(e) The Taj Mahal"
        ],
        "col_b": [
            "(i) is",
            "(ii) come",
            "(iii) built",
            "(iv) becomes",
            "(v) stands"
        ],
        "col_c": [
            "(i) to see it different times.",
            "(ii) one of the most beautiful buildings in the world.",
            "(iii) at Agra in India.",
            "(iv) a large tomb above the centre of the building.",
            "(v) it as a tomb for his wife."
        ],
        "key": "(a+iii+v), (b+iv+ii), (c+i+iv), (d+ii+i), (e+v+iii)",
        "sentences": [
            "Emperor Shahjahan built it as a tomb for his wife.",
            "It becomes one of the most beautiful buildings in the world.",
            "There is a large tomb above the centre of the building.",
            "People come to see it different times.",
            "The Taj Mahal stands at Agra in India."
        ]
    },
    {
        "id": 2,
        "title": "Our Parliament House (Jatiya Sangsad Bhaban)",
        "board": "Dakhil Exam-2020; Dinajpur Board 2019",
        "col_a": [
            "(a) Our parliament house",
            "(b) It was designed",
            "(c) The building is surrounded",
            "(d) It",
            "(e) The first parliamentary session"
        ],
        "col_b": [
            "(i) by the famous American architect",
            "(ii) was inaugurated",
            "(iii) was held in February",
            "(iv) is one of the most spectacular",
            "(v) by an artificial lake called"
        ],
        "col_c": [
            "(i) in the year 1982.",
            "(ii) buildings in the world.",
            "(iii) the same year.",
            "(iv) Louis I Kahn.",
            "(v) the Crescent Lake."
        ],
        "key": "(a+iv+ii), (b+i+iv), (c+v+v), (d+ii+i), (e+iii+iii)",
        "sentences": [
            "Our parliament house is one of the most spectacular buildings in the world.",
            "It was designed by the famous American architect Louis I Kahn.",
            "The building is surrounded by an artificial lake called the Crescent Lake.",
            "It was inaugurated in the year 1982.",
            "The first parliamentary session was held in February the same year."
        ]
    },
    {
        "id": 3,
        "title": "Democracy and Citizen Rights",
        "board": "Dhaka Board 2020",
        "col_a": [
            "(a) Democracy",
            "(b) It allows",
            "(c) It means",
            "(d) People",
            "(e) Free and fair election"
        ],
        "col_b": [
            "(i) freedom of speech,",
            "(ii) elect their representative directly",
            "(iii) is a system",
            "(iv) is the precondition",
            "(v) fair and equal treatment"
        ],
        "col_c": [
            "(i) of democracy.",
            "(ii) of government.",
            "(iii) for citizens.",
            "(iv) religious and political opinions.",
            "(v) in a democratic country."
        ],
        "key": "(a+iii+ii), (b+i+iv), (c+v+iii), (d+ii+v), (e+iv+i)",
        "sentences": [
            "Democracy is a system of government.",
            "It allows freedom of speech, religious and political opinions.",
            "It means fair and equal treatment for citizens.",
            "People elect their representative directly in a democratic country.",
            "Free and fair election is the precondition of democracy."
        ]
    },
    {
        "id": 4,
        "title": "Water Pollution and Health",
        "board": "Dakhil Exam-2025",
        "col_a": [
            "(a) Water",
            "(b) It",
            "(c) Clean water",
            "(d) Polluted water",
            "(e) We"
        ],
        "col_b": [
            "(i) can",
            "(ii) is",
            "(iii) is",
            "(iv) is",
            "(v) become"
        ],
        "col_c": [
            "(i) an important element of our environment.",
            "(ii) safe for us.",
            "(iii) harmful.",
            "(iv) be polluted in many ways.",
            "(v) sick by drinking polluted water."
        ],
        "key": "(a+iii+i), (b+i+iv), (c+ii+ii), (d+iv+iii), (e+v+v)",
        "sentences": [
            "Water is an important element of our environment.",
            "It can be polluted in many ways.",
            "Clean water is safe for us.",
            "Polluted water is harmful.",
            "We become sick by drinking polluted water."
        ]
    },
    {
        "id": 5,
        "title": "Meaning and Purpose of Education",
        "board": "Dhaka Board 2026",
        "col_a": [
            "(a) Education means",
            "(b) The purpose of education",
            "(c) Education",
            "(d) Education",
            "(e) Education makes us"
        ],
        "col_b": [
            "(i) conscious of our rights",
            "(ii) frees a man",
            "(iii) is to enlighten",
            "(iv) aims at",
            "(v) the receiving of formal learning"
        ],
        "col_c": [
            "(i) the individual.",
            "(ii) removing the darkness of mind.",
            "(iii) from restriction.",
            "(iv) from any educational institution.",
            "(v) and responsibilities."
        ],
        "key": "(a+v+iv), (b+iii+i), (c+ii+iii), (d+iv+ii), (e+i+v)",
        "sentences": [
            "Education means the receiving of formal learning from any educational institution.",
            "The purpose of education is to enlighten the individual.",
            "Education frees a man from restriction.",
            "Education aims at removing the darkness of mind.",
            "Education makes us conscious of our rights and responsibilities."
        ]
    },
    {
        "id": 6,
        "title": "Earthquakes and Safety Measures",
        "board": "Chattogram Board 2026",
        "col_a": [
            "(a) The ground",
            "(b) Tall buildings",
            "(c) Bangladesh",
            "(d) Earthquake resistance building codes",
            "(e) People"
        ],
        "col_b": [
            "(i) can fall",
            "(ii) sits",
            "(iii) need to know",
            "(iv) shakes",
            "(v) must be followed"
        ],
        "col_c": [
            "(i) by every builder.",
            "(ii) when an earthquake happens.",
            "(iii) in a big shake.",
            "(iv) what to do during an earthquake.",
            "(v) on moving tectonic plates."
        ],
        "key": "(a+ii+v), (b+i+iii), (c+iv+ii), (d+v+i), (e+iii+iv)",
        "sentences": [
            "The ground sits on moving tectonic plates.",
            "Tall buildings can fall in a big shake.",
            "Bangladesh shakes when an earthquake happens.",
            "Earthquake resistance building codes must be followed by every builder.",
            "People need to know what to do during an earthquake."
        ]
    },
    {
        "id": 7,
        "title": "Food Adulteration Crisis",
        "board": "Sylhet Board 2026",
        "col_a": [
            "(a) Food adulteration is a process",
            "(b) The main reason behind adding",
            "(c) It is an awful offense",
            "(d) This process reduces",
            "(e) The government has set up"
        ],
        "col_b": [
            "(i) mobile courts to detect",
            "(ii) the quality of foods",
            "(iii) in which harmful chemicals",
            "(iv) various chemicals in food",
            "(v) which is committed"
        ],
        "col_c": [
            "(i) by the greedy businessmen.",
            "(ii) is to increase financial profit.",
            "(iii) and punish the dishonest businessmen.",
            "(iv) are added in food items.",
            "(v) and damages the health of consumers."
        ],
        "key": "(a+iii+iv), (b+iv+ii), (c+v+i), (d+ii+v), (e+i+iii)",
        "sentences": [
            "Food adulteration is a process in which harmful chemicals are added in food items.",
            "The main reason behind adding various chemicals in food is to increase financial profit.",
            "It is an awful offense which is committed by the greedy businessmen.",
            "This process reduces the quality of foods and damages the health of consumers.",
            "The government has set up mobile courts to detect and punish the dishonest businessmen."
        ]
    },
    {
        "id": 8,
        "title": "Donation of Blood and Misconceptions",
        "board": "Barishal Board 2026",
        "col_a": [
            "(a) Donation of blood",
            "(b) In our society, some of us nourish",
            "(c) As per medical science, every man in",
            "(d) We should have",
            "(e) Sometimes, a bag of our blood is"
        ],
        "col_b": [
            "(i) sound health can donate blood",
            "(ii) enough to save",
            "(iii) a crystal clear idea that if",
            "(iv) a misconception about blood donation which conveys",
            "(v) is universally acknowledged to"
        ],
        "col_c": [
            "(i) we donate blood, we invite no harm to us.",
            "(ii) after every three months without any side effect.",
            "(iii) be a very noble deed.",
            "(iv) the life of a dying person.",
            "(v) a negative message for the others."
        ],
        "key": "(a+v+iii), (b+iv+v), (c+i+ii), (d+iii+i), (e+ii+iv)",
        "sentences": [
            "Donation of blood is universally acknowledged to be a very noble deed.",
            "In our society, some of us nourish a misconception about blood donation which conveys a negative message for the others.",
            "As per medical science, every man in sound health can donate blood after every three months without any side effect.",
            "We should have a crystal clear idea that if we donate blood, we invite no harm to us.",
            "Sometimes, a bag of our blood is enough to save the life of a dying person."
        ]
    },
    {
        "id": 9,
        "title": "Facebook as a Social Network",
        "board": "Dinajpur Board 2026",
        "col_a": [
            "(a) Facebook is an internet",
            "(b) Nowadays Facebook has become",
            "(c) It contributes much",
            "(d) People are also",
            "(e) Everybody having"
        ],
        "col_b": [
            "(i) internet connection may",
            "(ii) using Facebook",
            "(iii) based social network",
            "(iv) to maintain social and friendly relationship",
            "(v) an important part"
        ],
        "col_c": [
            "(i) gain access to Facebook.",
            "(ii) among people living anywhere.",
            "(iii) to facilitate the official works.",
            "(iv) connecting people worldwide.",
            "(v) of our daily life."
        ],
        "key": "(a+iii+iv), (b+v+v), (c+iv+ii), (d+ii+iii), (e+i+i)",
        "sentences": [
            "Facebook is an internet based social network connecting people worldwide.",
            "Nowadays Facebook has become an important part of our daily life.",
            "It contributes much to maintain social and friendly relationship among people living anywhere.",
            "People are also using Facebook to facilitate the official works.",
            "Everybody having internet connection may gain access to Facebook."
        ]
    },
    {
        "id": 10,
        "title": "Drug Addiction and Brain Damage",
        "board": "Mymensingh Board 2026",
        "col_a": [
            "(a) Drug addiction",
            "(b) Drugs are used for",
            "(c) These drugs are taken by",
            "(d) Drug addiction draws",
            "(e) It damages"
        ],
        "col_b": [
            "(i) smoking or through injection",
            "(ii) the young generation",
            "(iii) brain cells and all nervous system",
            "(iv) means strong attraction for",
            "(v) intoxicating and stimulating purpose"
        ],
        "col_c": [
            "(i) to death silently.",
            "(ii) which are harmful to human body.",
            "(iii) any kind of harmful drug.",
            "(iv) to deadly destruction.",
            "(v) by some frustrated youths."
        ],
        "key": "(a+iv+iii), (b+v+ii), (c+i+v), (d+ii+iv), (e+iii+i)",
        "sentences": [
            "Drug addiction means strong attraction for any kind of harmful drug.",
            "Drugs are used for intoxicating and stimulating purpose which are harmful to human body.",
            "These drugs are taken by smoking or through injection by some frustrated youths.",
            "Drug addiction draws the young generation to deadly destruction.",
            "It damages brain cells and all nervous system to death silently."
        ]
    },
    {
        "id": 11,
        "title": "Love is Divine",
        "board": "Cumilla Board 2019",
        "col_a": [
            "(a) Your friends cannot help",
            "(b) It is love",
            "(c) Love is divine",
            "(d) You cannot find others",
            "(e) If you are not loved"
        ],
        "col_b": [
            "(i) that makes us",
            "(ii) loving you",
            "(iii) to love you",
            "(iv) it is a good evidence that",
            "(v) which exists"
        ],
        "col_c": [
            "(i) in everyone.",
            "(ii) you don't love others.",
            "(iii) feel for others.",
            "(iv) if you love them.",
            "(v) unless you love them."
        ],
        "key": "(a+ii+iv), (b+i+iii), (c+v+i), (d+iii+v), (e+iv+ii)",
        "sentences": [
            "Your friends cannot help loving you if you love them.",
            "It is love that makes us feel for others.",
            "Love is divine which exists in everyone.",
            "You cannot find others to love you unless you love them.",
            "If you are not loved it is a good evidence that you don't love others."
        ]
    },
    {
        "id": 12,
        "title": "Education and Self-Enlightenment",
        "board": "Chattogram Board 2019",
        "col_a": [
            "(a) Education means",
            "(b) The purpose of education",
            "(c) Education",
            "(d) It",
            "(e) Education makes us"
        ],
        "col_b": [
            "(i) frees a man",
            "(ii) conscious of our rights",
            "(iii) is to enlighten",
            "(iv) ennobles our mind and",
            "(v) the receiving of formal learning"
        ],
        "col_c": [
            "(i) the individual.",
            "(ii) from any educational institution.",
            "(iii) and responsibilities.",
            "(iv) from restriction.",
            "(v) refines our sensibilities."
        ],
        "key": "(a+v+ii), (b+iii+i), (c+i+iv), (d+iv+v), (e+ii+iii)",
        "sentences": [
            "Education means the receiving of formal learning from any educational institution.",
            "The purpose of education is to enlighten the individual.",
            "Education frees a man from restriction.",
            "It ennobles our mind and refines our sensibilities.",
            "Education makes us conscious of our rights and responsibilities."
        ]
    },
    {
        "id": 13,
        "title": "The Moon and Reflected Sunlight",
        "board": "Barishal Board 2019, 2025",
        "col_a": [
            "(a) The moon",
            "(b) It has",
            "(c) The moon shines",
            "(d) The sun",
            "(e) If you look through a telescope"
        ],
        "col_b": [
            "(i) no light",
            "(ii) reflects light",
            "(iii) is the only natural satellite",
            "(iv) you will see that the moon",
            "(v) by reflecting"
        ],
        "col_c": [
            "(i) of our earth.",
            "(ii) from the sun.",
            "(iii) the light of the sun.",
            "(iv) of its own.",
            "(v) has many craters and mountains."
        ],
        "key": "(a+iii+i), (b+i+iv), (c+v+iii), (d+ii+ii), (e+iv+v)",
        "sentences": [
            "The moon is the only natural satellite of our earth.",
            "It has no light of its own.",
            "The moon shines by reflecting the light of the sun.",
            "The sun reflects light from the sun.",
            "If you look through a telescope you will see that the moon has many craters and mountains."
        ]
    },
    {
        "id": 14,
        "title": "Sonargaon: Ancient Capital of Bengal",
        "board": "Sylhet Board 2019",
        "col_a": [
            "(a) Sonargaon was",
            "(b) It was famous",
            "(c) Panam Nagar",
            "(d) Many wealthy merchants",
            "(e) They built"
        ],
        "col_b": [
            "(i) is an attractive part",
            "(ii) many beautiful buildings",
            "(iii) the ancient capital",
            "(iv) for the production of",
            "(v) lived in"
        ],
        "col_c": [
            "(i) of Bengal in medieval period.",
            "(ii) of Sonargaon.",
            "(iii) on both sides of the street.",
            "(iv) world famous Muslin cloth.",
            "(v) this historic township."
        ],
        "key": "(a+iii+i), (b+iv+iv), (c+i+ii), (d+v+v), (e+ii+iii)",
        "sentences": [
            "Sonargaon was the ancient capital of Bengal in medieval period.",
            "It was famous for the production of world famous Muslin cloth.",
            "Panam Nagar is an attractive part of Sonargaon.",
            "Many wealthy merchants lived in this historic township.",
            "They built many beautiful buildings on both sides of the street."
        ]
    },
    {
        "id": 15,
        "title": "Punctuality: A Great Virtue",
        "board": "Rajshahi Board 2020",
        "col_a": [
            "(a) Punctuality",
            "(b) It",
            "(c) A punctual person",
            "(d) It helps us",
            "(e) Those who are not punctual"
        ],
        "col_b": [
            "(i) to become accurate in timing",
            "(ii) is a virtue",
            "(iii) cannot prosper",
            "(iv) is loved and respected",
            "(v) denotes the habit"
        ],
        "col_c": [
            "(i) in life.",
            "(ii) which makes a man disciplined.",
            "(iii) by all in the society.",
            "(iv) of doing a thing in proper time.",
            "(v) in all their attempts."
        ],
        "key": "(a+ii+ii), (b+v+iv), (c+iv+iii), (d+i+v), (e+iii+i)",
        "sentences": [
            "Punctuality is a virtue which makes a man disciplined.",
            "It denotes the habit of doing a thing in proper time.",
            "A punctual person is loved and respected by all in the society.",
            "It helps us to become accurate in timing in all their attempts.",
            "Those who are not punctual cannot prosper in life."
        ]
    },
    {
        "id": 16,
        "title": "Patriotism and National Duty",
        "board": "Jashore Board 2020; Dhaka Board 2025",
        "col_a": [
            "(a) Patriotism",
            "(b) A patriot",
            "(c) It inspires a man",
            "(d) An unpatriotic man",
            "(e) We all should"
        ],
        "col_b": [
            "(i) loves his country and",
            "(ii) is hated and dies",
            "(iii) be true patriots",
            "(iv) is a noble virtue",
            "(v) to shed the last drop of blood"
        ],
        "col_c": [
            "(i) for the defense of the country.",
            "(ii) unwept and unsung.",
            "(iii) for the motherland.",
            "(iv) works for its welfare.",
            "(v) that inspires a man to love his country."
        ],
        "key": "(a+iv+v), (b+i+iv), (c+v+iii), (d+ii+ii), (e+iii+i)",
        "sentences": [
            "Patriotism is a noble virtue that inspires a man to love his country.",
            "A patriot loves his country and works for its welfare.",
            "It inspires a man to shed the last drop of blood for the motherland.",
            "An unpatriotic man is hated and dies unwept and unsung.",
            "We all should be true patriots for the defense of the country."
        ]
    },
    {
        "id": 17,
        "title": "Price Hike and Inflation Impact",
        "board": "Rajshahi Board 2025",
        "col_a": [
            "(a) Price hike",
            "(b) It is now",
            "(c) The fixed income people",
            "(d) Dishonest businessmen",
            "(e) The government should"
        ],
        "col_b": [
            "(i) one of the burning issues",
            "(ii) take stern action",
            "(iii) are the worst sufferers",
            "(iv) means the abnormal increase",
            "(v) are mainly responsible"
        ],
        "col_c": [
            "(i) against market syndicates.",
            "(ii) in the price of daily essentials.",
            "(iii) in our country.",
            "(iv) of this price hike.",
            "(v) for creating artificial crisis."
        ],
        "key": "(a+iv+ii), (b+i+iii), (c+iii+iv), (d+v+v), (e+ii+i)",
        "sentences": [
            "Price hike means the abnormal increase in the price of daily essentials.",
            "It is now one of the burning issues in our country.",
            "The fixed income people are the worst sufferers of this price hike.",
            "Dishonest businessmen are mainly responsible for creating artificial crisis.",
            "The government should take stern action against market syndicates."
        ]
    },
    {
        "id": 18,
        "title": "Good Manners and Politeness",
        "board": "Cumilla Board 2025",
        "col_a": [
            "(a) Good manner",
            "(b) A man of good manners",
            "(c) In all religions",
            "(d) A person who possesses this",
            "(e) So, all of us"
        ],
        "col_b": [
            "(i) a great importance has been given to",
            "(ii) invaluable virtue is an ideal",
            "(iii) should cultivate this great virtue",
            "(iv) achieves success in every sphere",
            "(v) is the best quality of a human being and"
        ],
        "col_c": [
            "(i) of life.",
            "(ii) is a great ornament of life.",
            "(iii) example in the society.",
            "(iv) from the early childhood.",
            "(v) good manners."
        ],
        "key": "(a+v+ii), (b+iv+i), (c+i+v), (d+ii+iii), (e+iii+iv)",
        "sentences": [
            "Good manner is the best quality of a human being and is a great ornament of life.",
            "A man of good manners achieves success in every sphere of life.",
            "In all religions a great importance has been given to good manners.",
            "A person who possesses this invaluable virtue is an ideal example in the society.",
            "So, all of us should cultivate this great virtue from the early childhood."
        ]
    },
    {
        "id": 19,
        "title": "Freedom Fighters and National Honor",
        "board": "Jashore Board 2025",
        "col_a": [
            "(a) A freedom fighter",
            "(b) But he fights",
            "(c) Freedom fighters",
            "(d) They took part in",
            "(e) We have lost"
        ],
        "col_b": [
            "(i) sacrifice their valuable lives",
            "(ii) our heroic sons",
            "(iii) for a noble cause that is",
            "(iv) is honored everywhere",
            "(v) our War of Liberation"
        ],
        "col_c": [
            "(i) in that war.",
            "(ii) in every country.",
            "(iii) for the cause of freedom.",
            "(iv) to defend his motherland.",
            "(v) in 1971."
        ],
        "key": "(a+iv+ii), (b+iii+iv), (c+i+iii), (d+v+v), (e+ii+i)",
        "sentences": [
            "A freedom fighter is honored everywhere in every country.",
            "But he fights for a noble cause that is to defend his motherland.",
            "Freedom fighters sacrifice their valuable lives for the cause of freedom.",
            "They took part in our War of Liberation in 1971.",
            "We have lost our heroic sons in that war."
        ]
    },
    {
        "id": 20,
        "title": "Role of an Educated Mother",
        "board": "Chattogram Board 2025",
        "col_a": [
            "(a) A really educated mother",
            "(b) A child",
            "(c) An educated mother",
            "(d) So if the mother",
            "(e) An educated nation"
        ],
        "col_b": [
            "(i) is therefore largely indebted to",
            "(ii) is educated her children",
            "(iii) grows up always",
            "(iv) knows well how to bring up",
            "(v) plays a vital role"
        ],
        "col_c": [
            "(i) will be educated naturally.",
            "(ii) its educated mother.",
            "(iii) to build up an educated nation.",
            "(iv) in contact with its mother.",
            "(v) and nurture her children to make them worthy citizens."
        ],
        "key": "(a+v+iii), (b+iii+iv), (c+iv+v), (d+ii+i), (e+i+ii)",
        "sentences": [
            "A really educated mother plays a vital role to build up an educated nation.",
            "A child grows up always in contact with its mother.",
            "An educated mother knows well how to bring up and nurture her children to make them worthy citizens.",
            "So if the mother is educated her children will be educated naturally.",
            "An educated nation is therefore largely indebted to its educated mother."
        ]
    },
    {
        "id": 21,
        "title": "Truthfulness: Greatest of Virtues",
        "board": "Sylhet Board 2025",
        "col_a": [
            "(a) Truthfulness",
            "(b) We must",
            "(c) Otherwise, we",
            "(d) We know that a lie",
            "(e) Today or"
        ],
        "col_b": [
            "(i) tomorrow it will",
            "(ii) will never win",
            "(iii) cultivate the habit",
            "(iv) is the greatest of",
            "(v) never lies"
        ],
        "col_c": [
            "(i) the respect of others.",
            "(ii) all human virtues.",
            "(iii) come to light.",
            "(iv) of speaking the truth.",
            "(v) hidden for long."
        ],
        "key": "(a+iv+ii), (b+iii+iv), (c+ii+i), (d+v+v), (e+i+iii)",
        "sentences": [
            "Truthfulness is the greatest of all human virtues.",
            "We must cultivate the habit of speaking the truth.",
            "Otherwise, we will never win the respect of others.",
            "We know that a lie never lies hidden for long.",
            "Today or tomorrow it will come to light."
        ]
    },
    {
        "id": 22,
        "title": "Global Warming and Climate Change",
        "board": "Dinajpur Board 2025",
        "col_a": [
            "(a) Global warming",
            "(b) It is caused by",
            "(c) Greenhouse effect",
            "(d) The polar ice caps",
            "(e) We should plant"
        ],
        "col_b": [
            "(i) the increase of greenhouse gases",
            "(ii) are melting rapidly",
            "(iii) more trees to",
            "(iv) refers to the gradual rise",
            "(v) is the process by which"
        ],
        "col_c": [
            "(i) earth's atmosphere traps heat.",
            "(ii) due to rise in temperature.",
            "(iii) save our planet.",
            "(iv) in the earth's temperature.",
            "(v) in the atmosphere."
        ],
        "key": "(a+iv+iv), (b+i+v), (c+v+i), (d+ii+ii), (e+iii+iii)",
        "sentences": [
            "Global warming refers to the gradual rise in the earth's temperature.",
            "It is caused by the increase of greenhouse gases in the atmosphere.",
            "Greenhouse effect is the process by which earth's atmosphere traps heat.",
            "The polar ice caps are melting rapidly due to rise in temperature.",
            "We should plant more trees to save our planet."
        ]
    },
    {
        "id": 23,
        "title": "Cox's Bazar Sea Beach",
        "board": "Mymensingh Board 2025",
        "col_a": [
            "(a) Bangladesh possesses",
            "(b) Cox's Bazar sea beach",
            "(c) It is",
            "(d) It is a remarkable place",
            "(e) Thousands of tourists"
        ],
        "col_b": [
            "(i) in our country in respect",
            "(ii) visit this beach",
            "(iii) of the natural beauty",
            "(iv) is one of them",
            "(v) a number of tourist spots"
        ],
        "col_c": [
            "(i) of immense natural beauty.",
            "(ii) and uniqueness.",
            "(iii) every year from home and abroad.",
            "(iv) the longest unbroken sandy beach in the world.",
            "(v) that attract visitors."
        ],
        "key": "(a+v+v), (b+iv+i), (c+iv+iv), (d+i+ii), (e+ii+iii)",
        "sentences": [
            "Bangladesh possesses a number of tourist spots that attract visitors.",
            "Cox's Bazar sea beach is one of them of immense natural beauty.",
            "It is the longest unbroken sandy beach in the world.",
            "It is a remarkable place in our country in respect and uniqueness.",
            "Thousands of tourists visit this beach every year from home and abroad."
        ]
    },
    {
        "id": 24,
        "title": "Japanese Traffic Rules and Discipline",
        "board": "Cumilla Board 2020",
        "col_a": [
            "(a) The Japanese",
            "(b) They strictly follow",
            "(c) Even a child",
            "(d) Nobody crosses",
            "(e) This disciplined habit"
        ],
        "col_b": [
            "(i) the road when",
            "(ii) are very law-abiding",
            "(iii) knows traffic rules and",
            "(iv) has made their country",
            "(v) traffic rules and regulations"
        ],
        "col_c": [
            "(i) the signal is red.",
            "(ii) and disciplined.",
            "(iii) obeys them carefully.",
            "(iv) accident-free and prosperous.",
            "(v) in their daily lives."
        ],
        "key": "(a+ii+ii), (b+v+v), (c+iii+iii), (d+i+i), (e+iv+iv)",
        "sentences": [
            "The Japanese are very law-abiding and disciplined.",
            "They strictly follow traffic rules and regulations in their daily lives.",
            "Even a child knows traffic rules and obeys them carefully.",
            "Nobody crosses the road when the signal is red.",
            "This disciplined habit has made their country accident-free and prosperous."
        ]
    },
    {
        "id": 25,
        "title": "E-mail: Modern Invention of Communication",
        "board": "Chattogram Board 2020",
        "col_a": [
            "(a) E-mail is",
            "(b) Communication through e-mail",
            "(c) To operate an e-mail system",
            "(d) It has reduced",
            "(e) E-mail functions instantly"
        ],
        "col_b": [
            "(i) a wonderful modern invention",
            "(ii) the distance and time",
            "(iii) is made between two persons",
            "(iv) with the help of a computer set,",
            "(v) we need two sets of computers"
        ],
        "col_c": [
            "(i) in communication sector.",
            "(ii) android phone and internet connection.",
            "(iii) in sending letters and files.",
            "(iv) or offices across the world.",
            "(v) and internet connection."
        ],
        "key": "(a+i+i), (b+iii+iv), (c+v+v), (d+ii+iii), (e+iv+ii)",
        "sentences": [
            "E-mail is a wonderful modern invention in communication sector.",
            "Communication through e-mail is made between two persons or offices across the world.",
            "To operate an e-mail system we need two sets of computers and internet connection.",
            "It has reduced the distance and time in sending letters and files.",
            "E-mail functions instantly with the help of a computer set, android phone and internet connection."
        ]
    },
    {
        "id": 26,
        "title": "Vision 2041 and Developed Bangladesh",
        "board": "Dinajpur Board 2020",
        "col_a": [
            "(a) Vision 2041 aims",
            "(b) We want to see",
            "(c) Education will be free",
            "(d) Every citizen will enjoy",
            "(e) To achieve this goal"
        ],
        "col_b": [
            "(i) fundamental rights and",
            "(ii) we must work together",
            "(iii) Bangladesh as a democratic,",
            "(iv) at turning Bangladesh into",
            "(v) for all as it is"
        ],
        "col_c": [
            "(i) a high-income developed country.",
            "(ii) equal opportunities.",
            "(iii) with utmost dedication.",
            "(iv) their basic human right.",
            "(v) corruption-free nation."
        ],
        "key": "(a+iv+i), (b+iii+v), (c+v+iv), (d+i+ii), (e+ii+iii)",
        "sentences": [
            "Vision 2041 aims at turning Bangladesh into a high-income developed country.",
            "We want to see Bangladesh as a democratic, corruption-free nation.",
            "Education will be free for all as it is their basic human right.",
            "Every citizen will enjoy fundamental rights and equal opportunities.",
            "To achieve this goal we must work together with utmost dedication."
        ]
    },
    {
        "id": 27,
        "title": "Bangladesh in Active Earthquake Zone",
        "board": "Barishal Board 2020",
        "col_a": [
            "(a) Bangladesh lies",
            "(b) Geologists have warned that",
            "(c) Recurrent tremors in recent times",
            "(d) A massive earthquake",
            "(e) Precautionary steps"
        ],
        "col_b": [
            "(i) may cause colossal loss of",
            "(ii) should be taken",
            "(iii) in an active earthquake",
            "(iv) a major earthquake may hit",
            "(v) are clear indications"
        ],
        "col_c": [
            "(i) lives and property in our cities.",
            "(ii) zone of the world.",
            "(iii) to minimize the damage.",
            "(iv) our country at any time.",
            "(v) of severe vulnerability."
        ],
        "key": "(a+iii+ii), (b+iv+iv), (c+v+v), (d+i+i), (e+ii+iii)",
        "sentences": [
            "Bangladesh lies in an active earthquake zone of the world.",
            "Geologists have warned that a major earthquake may hit our country at any time.",
            "Recurrent tremors in recent times are clear indications of severe vulnerability.",
            "A massive earthquake may cause colossal loss of lives and property in our cities.",
            "Precautionary steps should be taken to minimize the damage."
        ]
    },
    {
        "id": 28,
        "title": "ICT in Education and Health",
        "board": "Sylhet Board 2020",
        "col_a": [
            "(a) ICT means",
            "(b) In health science",
            "(c) Students can learn",
            "(d) It has opened up",
            "(e) We should utilize"
        ],
        "col_b": [
            "(i) new horizons of",
            "(ii) ICT for the development",
            "(iii) ICT is used to diagnose",
            "(iv) their lessons effectively",
            "(v) information and communication technology"
        ],
        "col_c": [
            "(i) knowledge and research.",
            "(ii) of our motherland.",
            "(iii) through multimedia classrooms.",
            "(iv) disease and give good treatment.",
            "(v) in modern life."
        ],
        "key": "(a+v+v), (b+iii+iv), (c+iv+iii), (d+i+i), (e+ii+ii)",
        "sentences": [
            "ICT means information and communication technology in modern life.",
            "In health science ICT is used to diagnose disease and give good treatment.",
            "Students can learn their lessons effectively through multimedia classrooms.",
            "It has opened up new horizons of knowledge and research.",
            "We should utilize ICT for the development of our motherland."
        ]
    },
    {
        "id": 29,
        "title": "Bassanio and Portia's Three Caskets",
        "board": "Mymensingh Board 2020",
        "col_a": [
            "(a) Bassanio",
            "(b) Portia's father",
            "(c) Before his death he",
            "(d) He had thought of an unusual",
            "(e) He had"
        ],
        "col_b": [
            "(i) plan to find a good husband",
            "(ii) wanted a man to marry Portia",
            "(iii) went to Belmont to visit Portia",
            "(iv) three caskets made",
            "(v) had died lately"
        ],
        "col_c": [
            "(i) grandly dressed, with many servants.",
            "(ii) in Belmont.",
            "(iii) for herself and not for her wealth.",
            "(iv) for his daughter.",
            "(v) one of gold, one of silver and one of lead."
        ],
        "key": "(a+iii+i), (b+v+ii), (c+ii+iii), (d+i+iv), (e+iv+v)",
        "sentences": [
            "Bassanio went to Belmont to visit Portia grandly dressed, with many servants.",
            "Portia's father had died lately in Belmont.",
            "Before his death he wanted a man to marry Portia for herself and not for her wealth.",
            "He had thought of an unusual plan to find a good husband for his daughter.",
            "He had three caskets made, one of gold, one of silver and one of lead."
        ]
    },
    {
        "id": 30,
        "title": "Air Pollution and Black Smoke",
        "board": "Dhaka Board 2022",
        "col_a": [
            "(a) Air pollution",
            "(b) It",
            "(c) There",
            "(d) Black smoke which is emitted",
            "(e) Immediate steps"
        ],
        "col_b": [
            "(i) causes",
            "(ii) must be taken",
            "(iii) is",
            "(iv) from the vehicles is",
            "(v) are"
        ],
        "col_c": [
            "(i) devastating health consequences.",
            "(ii) the main cause of it.",
            "(iii) to control this pollution.",
            "(iv) a number of reasons behind this pollution.",
            "(v) the most dangerous form of pollution."
        ],
        "key": "(a+iii+v), (b+i+i), (c+v+iv), (d+iv+ii), (e+ii+iii)",
        "sentences": [
            "Air pollution is the most dangerous form of pollution.",
            "It causes devastating health consequences.",
            "There are a number of reasons behind this pollution.",
            "Black smoke which is emitted from the vehicles is the main cause of it.",
            "Immediate steps must be taken to control this pollution."
        ]
    },
    {
        "id": 31,
        "title": "Electricity Generation and Renewable Energy",
        "board": "Rajshahi Board 2022",
        "col_a": [
            "(a) To generate electricity people of the world",
            "(b) One day these resources",
            "(c) But wind and sunlight",
            "(d) Energy demand",
            "(e) For the betterment of us, we"
        ],
        "col_b": [
            "(i) are inexhaustible sources",
            "(ii) will run out completely",
            "(iii) mostly burn coal and oil",
            "(iv) is increasing day by day",
            "(v) must harness renewable solar power"
        ],
        "col_c": [
            "(i) at an alarming rate.",
            "(ii) if we do not conserve them.",
            "(iii) of clean green energy.",
            "(iv) across all developing nations.",
            "(v) to ensure future survival."
        ],
        "key": "(a+iii+i), (b+ii+ii), (c+i+iii), (d+iv+iv), (e+v+v)",
        "sentences": [
            "To generate electricity people of the world mostly burn coal and oil at an alarming rate.",
            "One day these resources will run out completely if we do not conserve them.",
            "But wind and sunlight are inexhaustible sources of clean green energy.",
            "Energy demand is increasing day by day across all developing nations.",
            "For the betterment of us, we must harness renewable solar power to ensure future survival."
        ]
    },
    {
        "id": 32,
        "title": "May Day and Workers' Rights",
        "board": "Jashore Board 2022",
        "col_a": [
            "(a) May Day commemorates",
            "(b) The day is also called",
            "(c) The world celebrates",
            "(d) The workers had to work",
            "(e) They sacrificed their lives"
        ],
        "col_b": [
            "(i) in mills and factories for quite a long time",
            "(ii) International Workers' Day",
            "(iii) the historic struggle of working people",
            "(iv) to establish an eight-hour workday",
            "(v) May Day on May 1"
        ],
        "col_c": [
            "(i) to guide their legitimate rights.",
            "(ii) across all countries.",
            "(iii) in Chicago in 1886.",
            "(iv) without proper wages and safety.",
            "(v) every year worldwide."
        ],
        "key": "(a+iii+i), (b+ii+v), (c+v+ii), (d+i+iv), (e+iv+iii)",
        "sentences": [
            "May Day commemorates the historic struggle of working people to guide their legitimate rights.",
            "The day is also called International Workers' Day across all countries.",
            "The world celebrates May Day on May 1 every year worldwide.",
            "The workers had to work in mills and factories for quite a long time without proper wages and safety.",
            "They sacrificed their lives to establish an eight-hour workday in Chicago in 1886."
        ]
    }
]

DAKHIL_2026_MATCHING = {
    "title": "Michael Madhusudan Dutt and Kopotaksha Nad",
    "board": "Dakhil Board Exam 2026 (Question 6)",
    "col_a": [
        "(a) Madhusudan",
        "(b) So after adopting Christianity",
        "(c) Kopotaksha Nad",
        "(d) He",
        "(e) He"
    ],
    "col_b": [
        "earned",
        "could realise",
        "went",
        "came back",
        "was"
    ],
    "col_c": [
        "to Europe.",
        "to Bengal.",
        "him huge reputation in Bangla.",
        "an ardent follower of the famous English poet Lord Byron.",
        "that his true identity lay in Bengal."
    ],
    "sentences": [
        "Madhusudan was an ardent follower of the famous English poet Lord Byron.",
        "So after adopting Christianity he went to Europe.",
        "Kopotaksha Nad earned him huge reputation in Bangla.",
        "He could realise that his true identity lay in Bengal.",
        "He came back to Bengal."
    ]
}

MODEL_TEST_MATCHING = {
    "title": "Facebook and Global Communication",
    "board": "Exclusive Model Test (Question 6)",
    "col_a": [
        "(a) Facebook is an internet",
        "(b) Nowadays Facebook has become",
        "(c) It contributes much",
        "(d) People are also",
        "(e) Everybody having"
    ],
    "col_b": [
        "(i) internet connection may",
        "(ii) using Facebook",
        "(iii) based social network",
        "(iv) to maintain social and friendly relationship",
        "(v) an important part"
    ],
    "col_c": [
        "(i) gain access to Facebook.",
        "(ii) among people living anywhere.",
        "(iii) to facilitate the official works.",
        "(iv) connecting people worldwide.",
        "(v) of our daily life."
    ],
    "sentences": [
        "Facebook is an internet based social network connecting people worldwide.",
        "Nowadays Facebook has become an important part of our daily life.",
        "It contributes much to maintain social and friendly relationship among people living anywhere.",
        "People are also using Facebook to facilitate the official works.",
        "Everybody having internet connection may gain access to Facebook."
    ]
}

REARRANGE_ITEMS_36 = [
    {
        "id": 1,
        "title": "Two Friends and a Bear",
        "board": "Dakhil Exam-2024",
        "sentences": {
            "a": "The first friend climbed up a tree.",
            "b": "Suddenly a bear came there.",
            "c": "The bear went away thinking him to be dead.",
            "d": "Once upon a time, two friends were passing by a forest.",
            "e": "The second friend could not climb up a tree.",
            "f": "They were talking about their love for each other.",
            "g": "The bear smelt his ears, nose and face.",
            "h": "He lay down on the ground and feigned death."
        },
        "key": "d -> f -> b -> a -> e -> h -> g -> c",
        "paragraph": "Once upon a time, two friends were passing by a forest. They were talking about their love for each other. Suddenly a bear came there. The first friend climbed up a tree. The second friend could not climb up a tree. He lay down on the ground and feigned death. The bear smelt his ears, nose and face. The bear went away thinking him to be dead."
    },
    {
        "id": 2,
        "title": "Michael Madhusudan Dutt",
        "board": "Dakhil Exam-2020",
        "sentences": {
            "a": "He also believed that the West would be more receptive to his creative genius.",
            "b": "He was born in Sagordari on the bank of the Kopotaksho River.",
            "c": "Since his adolescence he started believing that he was born on the wrong side of the planet.",
            "d": "The village is in Keshabpur Upazila under Jessore district.",
            "e": "Michael Madhusudan Dutt was a celebrated poet and dramatist in Bengali Literature.",
            "f": "From an early age, Dutt aspired to be an Englishman in form and manner.",
            "g": "He was an ardent follower of the English poet Lord Byron.",
            "h": "Later he realized his mistakes and composed masterpieces in Bangla."
        },
        "key": "e -> b -> d -> f -> c -> a -> g -> h",
        "paragraph": "Michael Madhusudan Dutt was a celebrated poet and dramatist in Bengali Literature. He was born in Sagordari on the bank of the Kopotaksho River. The village is in Keshabpur Upazila under Jessore district. From an early age, Dutt aspired to be an Englishman in form and manner. Since his adolescence he started believing that he was born on the wrong side of the planet. He also believed that the West would be more receptive to his creative genius. He was an ardent follower of the English poet Lord Byron. Later he realized his mistakes and composed masterpieces in Bangla."
    },
    {
        "id": 3,
        "title": "English: The International Language",
        "board": "Dakhil Exam-2019",
        "sentences": {
            "a": "Today, English is used as a global lingua franca across all continents.",
            "b": "It is essential for higher education, research, and international trade.",
            "c": "Without a good command of English, one cannot expect a lucrative career in MNCs.",
            "d": "English is an international language spoken by millions worldwide.",
            "e": "Most books of science, medicine, and technology are written in English.",
            "f": "So, we must develop all four basic skills of English from our student life.",
            "g": "The internet and digital communications are predominantly English-based.",
            "h": "Therefore, learning communicative English is no longer an option, but a necessity."
        },
        "key": "d -> a -> e -> g -> b -> c -> h -> f",
        "paragraph": "English is an international language spoken by millions worldwide. Today, English is used as a global lingua franca across all continents. Most books of science, medicine, and technology are written in English. The internet and digital communications are predominantly English-based. It is essential for higher education, research, and international trade. Without a good command of English, one cannot expect a lucrative career in MNCs. Therefore, learning communicative English is no longer an option, but a necessity. So, we must develop all four basic skills of English from our student life."
    },
    {
        "id": 4,
        "title": "The Statue of Liberty",
        "board": "Dakhil Exam",
        "sentences": {
            "a": "It was a gift for the Americans on the occasion of hundred years of the American Declaration of Independence.",
            "b": "The statue was sent to New York on board the French warship 'Isere' in 1885 into 350 individual pieces and in 214 crates.",
            "c": "Thousands of people saw the unveiling ceremony of the Statue of Liberty on October 28th, 1886.",
            "d": "The French Sculptor Frederic Auguste Bartholdi designed the Statue of Liberty.",
            "e": "The French people built the statue and assembled it in the States.",
            "f": "It was completed in the form of a sculpture within 1876.",
            "g": "It took four months to put the statue together and place it on the pedestal.",
            "h": "The Americans built the pedestal for the statue."
        },
        "key": "d -> a -> f -> e -> h -> b -> g -> c",
        "paragraph": "The French Sculptor Frederic Auguste Bartholdi designed the Statue of Liberty. It was a gift for the Americans on the occasion of hundred years of the American Declaration of Independence. It was completed in the form of a sculpture within 1876. The French people built the statue and assembled it in the States. The Americans built the pedestal for the statue. The statue was sent to New York on board the French warship 'Isere' in 1885 into 350 individual pieces and in 214 crates. It took four months to put the statue together and place it on the pedestal. Thousands of people saw the unveiling ceremony of the Statue of Liberty on October 28th, 1886."
    },
    {
        "id": 5,
        "title": "Sher-e-Bangla A.K. Fazlul Huq",
        "board": "Dakhil Exam-2017",
        "sentences": {
            "a": "But Fazlul Huq was a man of very independent character, so he resigned his post in 1911 and started legal practice.",
            "b": "Fazlul Huq attracted the attention of Sir B.F. Fuller, the then Governor of East Bengal who appointed him a Deputy Magistrate.",
            "c": "In 1897, he passed BL examination with distinction and began his independent legal practice at Kolkata High Court.",
            "d": "Sher-e-Bangla A.K. Fazlul Huq was born in 1873 at Saturia, Barisal.",
            "e": "The next year he was appointed lecturer and examiner of M.A. in Mathematics in Kolkata University.",
            "f": "He received his primary education there and then entered Barisal Zilla School.",
            "g": "At the age of 21, he passed the B.Sc. examination from Presidency College Kolkata and M.Sc. degree in Mathematics in 1895.",
            "h": "He passed the Entrance Examination standing first in Dhaka Division."
        },
        "key": "d -> f -> h -> g -> e -> c -> b -> a",
        "paragraph": "Sher-e-Bangla A.K. Fazlul Huq was born in 1873 at Saturia, Barisal. He received his primary education there and then entered Barisal Zilla School. He passed the Entrance Examination standing first in Dhaka Division. At the age of 21, he passed the B.Sc. examination from Presidency College Kolkata and M.Sc. degree in Mathematics in 1895. The next year he was appointed lecturer and examiner of M.A. in Mathematics in Kolkata University. In 1897, he passed BL examination with distinction and began his independent legal practice at Kolkata High Court. Fazlul Huq attracted the attention of Sir B.F. Fuller, the then Governor of East Bengal who appointed him a Deputy Magistrate. But Fazlul Huq was a man of very independent character, so he resigned his post in 1911 and started legal practice."
    },
    {
        "id": 6,
        "title": "Sultan Taimur's Campaign",
        "board": "SSC Exam",
        "sentences": {
            "a": "Young Taimur was ambitious and determined to become a great conqueror.",
            "b": "He attacked the province of a powerful neighboring ruler with full force.",
            "c": "Unfortunately, his army was severely defeated and all his brave soldiers were killed.",
            "d": "Taimur barely escaped with his life from the battlefield.",
            "e": "He fled in disguise and took shelter in a dense remote forest.",
            "f": "Hunger and exhaustion made him weak and hopeless.",
            "g": "While resting in a cave, he observed an incident that changed his life.",
            "h": "He saw an ant striving repeatedly to climb a wall, teaching him never to lose hope."
        },
        "key": "a -> b -> c -> d -> e -> f -> g -> h",
        "paragraph": "Young Taimur was ambitious and determined to become a great conqueror. He attacked the province of a powerful neighboring ruler with full force. Unfortunately, his army was severely defeated and all his brave soldiers were killed. Taimur barely escaped with his life from the battlefield. He fled in disguise and took shelter in a dense remote forest. Hunger and exhaustion made him weak and hopeless. While resting in a cave, he observed an incident that changed his life. He saw an ant striving repeatedly to climb a wall, teaching him never to lose hope."
    },
    {
        "id": 7,
        "title": "Napoleon and the English Boy",
        "board": "SSC Exam",
        "sentences": {
            "a": "Napoleon was walking along the seashore during his military campaign.",
            "b": "He noticed an English boy secretly making a small boat from tree branches.",
            "c": "Napoleon asked the boy what he intended to do with such a fragile vessel.",
            "d": "The boy replied that he wanted to cross the English Channel to see his ailing mother.",
            "e": "Napoleon was deeply touched by the boy's filial devotion and courage.",
            "f": "He praised the young boy for his deep affection toward his mother.",
            "g": "The emperor ordered a safe ship to take the boy home to England.",
            "h": "He also rewarded the boy with some gold coins as a token of admiration."
        },
        "key": "a -> b -> c -> d -> e -> f -> g -> h",
        "paragraph": "Napoleon was walking along the seashore during his military campaign. He noticed an English boy secretly making a small boat from tree branches. Napoleon asked the boy what he intended to do with such a fragile vessel. The boy replied that he wanted to cross the English Channel to see his ailing mother. Napoleon was deeply touched by the boy's filial devotion and courage. He praised the young boy for his deep affection toward his mother. The emperor ordered a safe ship to take the boy home to England. He also rewarded the boy with some gold coins as a token of admiration."
    },
    {
        "id": 8,
        "title": "Hazrat Abdul Quader Jilani's Truthfulness",
        "board": "SSC Exam",
        "sentences": {
            "a": "Hazrat Abdul Quader Jilani was going to Baghdad for higher education.",
            "b": "Before departure, his mother sewed forty gold coins inside his coat.",
            "c": "His mother advised him strictly never to tell a lie in any situation.",
            "d": "On the way through the desert, a gang of fierce robbers attacked the caravan.",
            "e": "One robber asked the boy if he had anything valuable in his possession.",
            "f": "Abdul Quader fearlessly replied that he had forty gold coins inside his coat.",
            "g": "The robber leader was stunned by the boy's honesty and asked why he didn't hide it.",
            "h": "The leader broke down in tears, returned all looted goods, and repented of sins."
        },
        "key": "a -> b -> c -> d -> e -> f -> g -> h",
        "paragraph": "Hazrat Abdul Quader Jilani was going to Baghdad for higher education. Before departure, his mother sewed forty gold coins inside his coat. His mother advised him strictly never to tell a lie in any situation. On the way through the desert, a gang of fierce robbers attacked the caravan. One robber asked the boy if he had anything valuable in his possession. Abdul Quader fearlessly replied that he had forty gold coins inside his coat. The robber leader was stunned by the boy's honesty and asked why he didn't hide it. The leader broke down in tears, returned all looted goods, and repented of sins."
    },
    {
        "id": 9,
        "title": "Alexander Fleming and Penicillin",
        "board": "SSC Exam",
        "sentences": {
            "a": "Alexander Fleming was a renowned Scottish bacteriologist.",
            "b": "He was working in St. Mary's Hospital laboratory in London.",
            "c": "One day in 1928, he noticed that mold had formed on an accidentally opened culture plate.",
            "d": "Around the mold, colonies of dangerous bacteria had been completely destroyed.",
            "e": "He realized that the mold produced a substance capable of killing deadly bacteria.",
            "f": "He named this miraculous antibiotic 'Penicillin'.",
            "g": "Penicillin revolutionized medical science and saved millions of wounded soldiers.",
            "h": "For this landmark breakthrough, Fleming was awarded the Nobel Prize in Medicine."
        },
        "key": "a -> b -> c -> d -> e -> f -> g -> h",
        "paragraph": "Alexander Fleming was a renowned Scottish bacteriologist. He was working in St. Mary's Hospital laboratory in London. One day in 1928, he noticed that mold had formed on an accidentally opened culture plate. Around the mold, colonies of dangerous bacteria had been completely destroyed. He realized that the mold produced a substance capable of killing deadly bacteria. He named this miraculous antibiotic 'Penicillin'. Penicillin revolutionized medical science and saved millions of wounded soldiers. For this landmark breakthrough, Fleming was awarded the Nobel Prize in Medicine."
    },
    {
        "id": 10,
        "title": "Louis Pasteur and Rabies Vaccine",
        "board": "SSC Exam",
        "sentences": {
            "a": "Louis Pasteur was a celebrated French scientist who revolutionized immunology.",
            "b": "He proved that diseases and spoilage were caused by microscopic germs.",
            "c": "He developed the method of pasteurization to kill harmful germs in milk.",
            "d": "Later, Pasteur dedicated his research to finding a cure for hydrophobia or rabies.",
            "e": "Rabies was considered a fatal and incurable viral disease transmitted by mad dogs.",
            "f": "A young boy named Joseph Meister, bitten badly by a rabid dog, was brought to him.",
            "g": "Pasteur administered his experimental rabies vaccine to the boy over several days.",
            "h": "The boy miraculously survived, and Pasteur's fame spread all over the world."
        },
        "key": "a -> b -> c -> d -> e -> f -> g -> h",
        "paragraph": "Louis Pasteur was a celebrated French scientist who revolutionized immunology. He proved that diseases and spoilage were caused by microscopic germs. He developed the method of pasteurization to kill harmful germs in milk. Later, Pasteur dedicated his research to finding a cure for hydrophobia or rabies. Rabies was considered a fatal and incurable viral disease transmitted by mad dogs. A young boy named Joseph Meister, bitten badly by a rabid dog, was brought to him. Pasteur administered his experimental rabies vaccine to the boy over several days. The boy miraculously survived, and Pasteur's fame spread all over the world."
    },
    {
        "id": 11,
        "title": "Who Will Bell the Cat?",
        "board": "SSC Exam",
        "sentences": {
            "a": "Once, some mice were having a joyous time in a large country house.",
            "b": "The owner of the house brought a cat to rid his store of the mice.",
            "c": "The mice were terrified because the cat killed their friends every day.",
            "d": "They held a grand council meeting to devise a plan to save themselves.",
            "e": "A young mouse proposed tying a bell around the cat's neck.",
            "f": "He explained that they would hear the bell ring whenever the cat approached.",
            "g": "All the mice rejoiced at the clever suggestion and applauded warmly.",
            "h": "Then a wise old mouse stood up and asked, 'Who will bell the cat?'"
        },
        "key": "a -> b -> c -> d -> e -> f -> g -> h",
        "paragraph": "Once, some mice were having a joyous time in a large country house. The owner of the house brought a cat to rid his store of the mice. The mice were terrified because the cat killed their friends every day. They held a grand council meeting to devise a plan to save themselves. A young mouse proposed tying a bell around the cat's neck. He explained that they would hear the bell ring whenever the cat approached. All the mice rejoiced at the clever suggestion and applauded warmly. Then a wise old mouse stood up and asked, 'Who will bell the cat?'"
    },
    {
        "id": 12,
        "title": "Prophet Muhammad (Sm) and the Thirsty Dog",
        "board": "SSC Exam",
        "sentences": {
            "a": "A weary traveler was walking across a scorching desert under the burning sun.",
            "b": "He felt extremely thirsty and searched everywhere for a drop of water.",
            "c": "Fortunately, he found a deep well and climbed down to quench his thirst.",
            "d": "When he came out, he saw a thirsty dog panting and licking the moist sand.",
            "e": "He thought to himself that the dog was suffering just as he had suffered.",
            "f": "He climbed down the well again and filled his leather shoe with cool water.",
            "g": "Holding the shoe in his mouth, he climbed up and gave the water to the dog.",
            "h": "Allah appreciated his compassionate deed and showered boundless mercy on him."
        },
        "key": "a -> b -> c -> d -> e -> f -> g -> h",
        "paragraph": "A weary traveler was walking across a scorching desert under the burning sun. He felt extremely thirsty and searched everywhere for a drop of water. Fortunately, he found a deep well and climbed down to quench his thirst. When he came out, he saw a thirsty dog panting and licking the moist sand. He thought to himself that the dog was suffering just as he had suffered. He climbed down the well again and filled his leather shoe with cool water. Holding the shoe in his mouth, he climbed up and gave the water to the dog. Allah appreciated his compassionate deed and showered boundless mercy on him."
    },
    {
        "id": 13,
        "title": "Abou Ben Adhem and the Angel",
        "board": "SSC Exam",
        "sentences": {
            "a": "Abou Ben Adhem was a pious man who loved peace and humanity.",
            "b": "One night he woke from a deep dream of peace in his moonlit room.",
            "c": "He saw an angel writing in a golden book.",
            "d": "Abou asked the angel, 'What writest thou?'",
            "e": "The angel replied, 'The names of those who love the Lord.'",
            "f": "Abou asked if his own name was included, but the angel answered 'Nay.'",
            "g": "Cheerfully Abou requested, 'Write me then as one that loves his fellow men.'",
            "h": "The next night the angel returned and showed Abou's name led all the rest."
        },
        "key": "a -> b -> c -> d -> e -> f -> g -> h",
        "paragraph": "Abou Ben Adhem was a pious man who loved peace and humanity. One night he woke from a deep dream of peace in his moonlit room. He saw an angel writing in a golden book. Abou asked the angel, 'What writest thou?' The angel replied, 'The names of those who love the Lord.' Abou asked if his own name was included, but the angel answered 'Nay.' Cheerfully Abou requested, 'Write me then as one that loves his fellow men.' The next night the angel returned and showed Abou's name led all the rest."
    },
    {
        "id": 14,
        "title": "Androcles and the Lion (Part 1)",
        "board": "SSC Exam",
        "sentences": {
            "a": "Androcles was a poor slave who escaped from his cruel master in Rome.",
            "b": "He fled into a dense forest and hid inside a secluded dark cave.",
            "c": "One evening, a huge lion entered the cave roaring in deep agony.",
            "d": "Androcles was petrified with terror and expected instant death.",
            "e": "Soon he noticed that the lion held out its swollen and bleeding paw.",
            "f": "Overcoming his fear, Androcles examined the paw and saw a big sharp thorn.",
            "g": "He gently pulled out the thorn and washed the wound with cool water.",
            "h": "Relieved of pain, the lion licked Androcles's hands and became his loyal friend."
        },
        "key": "a -> b -> c -> d -> e -> f -> g -> h",
        "paragraph": "Androcles was a poor slave who escaped from his cruel master in Rome. He fled into a dense forest and hid inside a secluded dark cave. One evening, a huge lion entered the cave roaring in deep agony. Androcles was petrified with terror and expected instant death. Soon he noticed that the lion held out its swollen and bleeding paw. Overcoming his fear, Androcles examined the paw and saw a big sharp thorn. He gently pulled out the thorn and washed the wound with cool water. Relieved of pain, the lion licked Androcles's hands and became his loyal friend."
    },
    {
        "id": 15,
        "title": "Androcles and the Lion in the Arena (Part 2)",
        "board": "SSC Exam",
        "sentences": {
            "a": "After several months of forest life, Roman soldiers captured Androcles.",
            "b": "He was sentenced to be thrown to a hungry lion in the Roman amphitheater.",
            "c": "A large crowd including the Roman Emperor gathered to witness the execution.",
            "d": "A ferocious lion, starved for days, was released into the arena with a loud roar.",
            "e": "The lion rushed toward Androcles to tear him to pieces.",
            "f": "Suddenly the beast paused, recognized its old friend, and gently rubbed against him.",
            "g": "The astonished emperor summoned Androcles and asked for an explanation.",
            "h": "Hearing the miraculous tale, the emperor pardoned Androcles and freed the lion."
        },
        "key": "a -> b -> c -> d -> e -> f -> g -> h",
        "paragraph": "After several months of forest life, Roman soldiers captured Androcles. He was sentenced to be thrown to a hungry lion in the Roman amphitheater. A large crowd including the Roman Emperor gathered to witness the execution. A ferocious lion, starved for days, was released into the arena with a loud roar. The lion rushed toward Androcles to tear him to pieces. Suddenly the beast paused, recognized its old friend, and gently rubbed against him. The astonished emperor summoned Androcles and asked for an explanation. Hearing the miraculous tale, the emperor pardoned Androcles and freed the lion."
    },
    {
        "id": 16,
        "title": "Socrates and Xanthippe",
        "board": "SSC Exam",
        "sentences": {
            "a": "Socrates was a renowned Greek philosopher who lived in Athens.",
            "b": "He had a wife named Xanthippe who had an extremely fierce temper.",
            "c": "She used to lose her temper on slight pretexts and shout at Socrates.",
            "d": "One day, she became more furious than ever and began to scold him loudly.",
            "e": "Socrates walked out of the house and sat quietly on the doorstep.",
            "f": "Seeing her husband unfazed, she took a bucket of cold water and poured it over him.",
            "g": "The passers-by in the street were shocked, but Socrates remained completely calm.",
            "h": "He smiled serenely and said, 'I was expecting this; after thunder always comes rain.'"
        },
        "key": "a -> b -> c -> d -> e -> f -> g -> h",
        "paragraph": "Socrates was a renowned Greek philosopher who lived in Athens. He had a wife named Xanthippe who had an extremely fierce temper. She used to lose her temper on slight pretexts and shout at Socrates. One day, she became more furious than ever and began to scold him loudly. Socrates walked out of the house and sat quietly on the doorstep. Seeing her husband unfazed, she took a bucket of cold water and poured it over him. The passers-by in the street were shocked, but Socrates remained completely calm. He smiled serenely and said, 'I was expecting this; after thunder always comes rain.'"
    },
    {
        "id": 17,
        "title": "Kazi Nazrul Islam: Rebel Poet",
        "board": "SSC Exam",
        "sentences": {
            "a": "Kazi Nazrul Islam is the national poet of Bangladesh.",
            "b": "He was born on 24 May 1899 at Churulia in Burdwan district.",
            "c": "In his early life, he struggled with immense poverty and worked in a bakery.",
            "d": "At the outbreak of World War I, he joined the 49th Bengal Regiment in 1917.",
            "e": "He composed fiery patriotic songs and poems that inspired freedom fighters.",
            "f": "His celebrated poem 'Bidrohi' established him as the 'Rebel Poet'.",
            "g": "He was brought to independent Bangladesh in 1972 with state honor.",
            "h": "He breathed his last on 29 August 1976 and was buried beside Dhaka University mosque."
        },
        "key": "a -> b -> c -> d -> e -> f -> g -> h",
        "paragraph": "Kazi Nazrul Islam is the national poet of Bangladesh. He was born on 24 May 1899 at Churulia in Burdwan district. In his early life, he struggled with immense poverty and worked in a bakery. At the outbreak of World War I, he joined the 49th Bengal Regiment in 1917. He composed fiery patriotic songs and poems that inspired freedom fighters. His celebrated poem 'Bidrohi' established him as the 'Rebel Poet'. He was brought to independent Bangladesh in 1972 with state honor. He breathed his last on 29 August 1976 and was buried beside Dhaka University mosque."
    },
    {
        "id": 18,
        "title": "King Lear and His Three Daughters",
        "board": "SSC Exam",
        "sentences": {
            "a": "King Lear ruled over Britain for many years and grew old and weary.",
            "b": "He decided to divide his vast kingdom among his three daughters.",
            "c": "He summoned his daughters Goneril, Regan, and Cordelia to test their love.",
            "d": "Goneril and Regan flattered him extravagantly with insincere words of praise.",
            "e": "Cordelia, the youngest, replied honestly that she loved him according to her duty.",
            "f": "Enraged by her truthful answer, Lear banished Cordelia without a penny.",
            "g": "Later, the elder two daughters mistreated and threw out the helpless old king.",
            "h": "Lear realized his tragic folly in trusting flattering tongues over sincere love."
        },
        "key": "a -> b -> c -> d -> e -> f -> g -> h",
        "paragraph": "King Lear ruled over Britain for many years and grew old and weary. He decided to divide his vast kingdom among his three daughters. He summoned his daughters Goneril, Regan, and Cordelia to test their love. Goneril and Regan flattered him extravagantly with insincere words of praise. Cordelia, the youngest, replied honestly that she loved him according to her duty. Enraged by her truthful answer, Lear banished Cordelia without a penny. Later, the elder two daughters mistreated and threw out the helpless old king. Lear realized his tragic folly in trusting flattering tongues over sincere love."
    },
    {
        "id": 19,
        "title": "Shilpacharya Zainul Abedin",
        "board": "SSC Exam",
        "sentences": {
            "a": "Zainul Abedin was born in 1914 in Kishoregonj.",
            "b": "He showed exceptional artistic talent from his boyhood days.",
            "c": "He graduated with first class from Government Art School in Kolkata.",
            "d": "He was also appointed as a teacher there.",
            "e": "He is highly admired worldwide for his famous 'Bengal Famine Sketches' of 1943.",
            "f": "He is recognized as the pioneer of Bangladeshi modern art movement.",
            "g": "Still now he is held in great respect as Shilpacharya in Bangladesh.",
            "h": "He died of lung cancer on 28 May 1976."
        },
        "key": "a -> b -> c -> d -> e -> f -> g -> h",
        "paragraph": "Zainul Abedin was born in 1914 in Kishoregonj. He showed exceptional artistic talent from his boyhood days. He graduated with first class from Government Art School in Kolkata. He was also appointed as a teacher there. He is highly admired worldwide for his famous 'Bengal Famine Sketches' of 1943. He is recognized as the pioneer of Bangladeshi modern art movement. Still now he is held in great respect as Shilpacharya in Bangladesh. He died of lung cancer on 28 May 1976."
    },
    {
        "id": 20,
        "title": "Two Friends and the Money Bag",
        "board": "SSC Exam",
        "sentences": {
            "a": "Once upon a time, two friends were walking together along a forest road.",
            "b": "Suddenly, one friend noticed a purse full of gold coins lying on the ground.",
            "c": "He picked it up eagerly and shouted, 'I have found a fortune!'",
            "d": "The other friend suggested, 'Say we have found it, as we are companions.'",
            "e": "The first friend refused and insisted that the purse belonged solely to him.",
            "f": "Soon after, a group of armed horsemen rode up looking for the lost purse.",
            "g": "The first friend trembled and said, 'We are ruined, my friend!'",
            "h": "The other replied, 'Do not say we are ruined; say you are ruined, as you claimed it alone.'"
        },
        "key": "a -> b -> c -> d -> e -> f -> g -> h",
        "paragraph": "Once upon a time, two friends were walking together along a forest road. Suddenly, one friend noticed a purse full of gold coins lying on the ground. He picked it up eagerly and shouted, 'I have found a fortune!' The other friend suggested, 'Say we have found it, as we are companions.' The first friend refused and insisted that the purse belonged solely to him. Soon after, a group of armed horsemen rode up looking for the lost purse. The first friend trembled and said, 'We are ruined, my friend!' The other replied, 'Do not say we are ruined; say you are ruined, as you claimed it alone.'"
    },
    {
        "id": 21,
        "title": "Hatem Tai's Hospitality",
        "board": "Sylhet Board 2016; Barishal Board 2025",
        "sentences": {
            "a": "People praised him more than their king.",
            "b": "The guests praised the king.",
            "c": "The name of that man was Hatem Tai.",
            "d": "But the guests praised Hatem Tai too.",
            "e": "Long ago there lived a very kind and generous man in Yemen.",
            "f": "So, the king felt happy and proud.",
            "g": "He was not rich but he was very hospitable.",
            "h": "One day the king gave a dinner."
        },
        "key": "e -> c -> g -> h -> b -> f -> d -> a",
        "paragraph": "Long ago there lived a very kind and generous man in Yemen. The name of that man was Hatem Tai. He was not rich but he was very hospitable. One day the king gave a dinner. The guests praised the king. So, the king felt happy and proud. But the guests praised Hatem Tai too. People praised him more than their king."
    },
    {
        "id": 22,
        "title": "Shamim's Success in Self-Reliance",
        "board": "Dhaka Board 2019",
        "sentences": {
            "a": "Shamim got a lease of land in his village.",
            "b": "Shamim's lot has changed radically.",
            "c": "Poverty forced him to look for work.",
            "d": "He has also been raising hybrid cows for milk as well as to produce manure.",
            "e": "Shamim was an unemployed youth of an impoverished family.",
            "f": "Then he joined the training programme of youth development and received training in vegetable cultivation.",
            "g": "He is now happy to be a self-sufficient man.",
            "h": "He applied his new and improved knowledge for cultivating vegetables."
        },
        "key": "e -> c -> f -> a -> h -> d -> b -> g",
        "paragraph": "Shamim was an unemployed youth of an impoverished family. Poverty forced him to look for work. Then he joined the training programme of youth development and received training in vegetable cultivation. Shamim got a lease of land in his village. He applied his new and improved knowledge for cultivating vegetables. He has also been raising hybrid cows for milk as well as to produce manure. Shamim's lot has changed radically. He is now happy to be a self-sufficient man."
    },
    {
        "id": 23,
        "title": "Bayazid Bostami's Devotion to His Mother",
        "board": "SSC Exam",
        "sentences": {
            "a": "Bayazid Bostami was a small boy living with his ill mother.",
            "b": "One night he was reading beside the bed of his ailing mother.",
            "c": "His mother woke up and asked him for a glass of water.",
            "d": "Bayazid went to the kitchen but found the pitcher completely empty.",
            "e": "He went to a distant stream in the dark night and brought water.",
            "f": "When he returned, his mother was fast asleep again.",
            "g": "He stood beside her bed holding the water glass without waking her.",
            "h": "When dawn broke, his mother woke up and prayed for him with all her heart."
        },
        "key": "a -> b -> c -> d -> e -> f -> g -> h",
        "paragraph": "Bayazid Bostami was a small boy living with his ill mother. One night he was reading beside the bed of his ailing mother. His mother woke up and asked him for a glass of water. Bayazid went to the kitchen but found the pitcher completely empty. He went to a distant stream in the dark night and brought water. When he returned, his mother was fast asleep again. He stood beside her bed holding the water glass without waking her. When dawn broke, his mother woke up and prayed for him with all her heart."
    },
    {
        "id": 24,
        "title": "Nelson Mandela and Anti-Apartheid Struggle",
        "board": "SSC Exam",
        "sentences": {
            "a": "Nelson Mandela dedicated his life to fighting racial segregation in South Africa.",
            "b": "He was sentenced to life imprisonment on Robben Island in 1964.",
            "c": "He spent 27 agonizing years behind bars without yielding his ideals.",
            "d": "Global pressure and domestic struggles forced the apartheid regime to release him in 1990.",
            "e": "He negotiated a peaceful transition to multi-racial democracy.",
            "f": "In 1993, he was awarded the Nobel Peace Prize jointly with F.W. de Klerk.",
            "g": "He became the first democratic Black President of South Africa in 1994.",
            "h": "Mandela remains a universal icon of forgiveness, dignity, and reconciliation."
        },
        "key": "a -> b -> c -> d -> e -> f -> g -> h",
        "paragraph": "Nelson Mandela dedicated his life to fighting racial segregation in South Africa. He was sentenced to life imprisonment on Robben Island in 1964. He spent 27 agonizing years behind bars without yielding his ideals. Global pressure and domestic struggles forced the apartheid regime to release him in 1990. He negotiated a peaceful transition to multi-racial democracy. In 1993, he was awarded the Nobel Peace Prize jointly with F.W. de Klerk. He became the first democratic Black President of South Africa in 1994. Mandela remains a universal icon of forgiveness, dignity, and reconciliation."
    },
    {
        "id": 25,
        "title": "Sultan Taimur and the Hot Khichuri",
        "board": "SSC Exam",
        "sentences": {
            "a": "Once young Taimur attacked a province but his army was defeated and killed.",
            "b": "He fled disguised and took shelter in an old woman's humble hut.",
            "c": "The old woman felt pity for him and gave Taimur a hot plate of food.",
            "d": "Taimur eagerly put his hand in the center of the dish and burned his fingers.",
            "e": "The woman laughed and remarked that he was acting like foolish Taimur.",
            "f": "She advised him to eat from the cooler outer edges rather than the boiling center.",
            "g": "Taimur grasped the vital strategic lesson for his military warfare.",
            "h": "He began conquering smaller provinces from the edges before attacking the center."
        },
        "key": "a -> b -> c -> d -> e -> f -> g -> h",
        "paragraph": "Once young Taimur attacked a province but his army was defeated and killed. He fled disguised and took shelter in an old woman's humble hut. The old woman felt pity for him and gave Taimur a hot plate of food. Taimur eagerly put his hand in the center of the dish and burned his fingers. The woman laughed and remarked that he was acting like foolish Taimur. She advised him to eat from the cooler outer edges rather than the boiling center. Taimur grasped the vital strategic lesson for his military warfare. He began conquering smaller provinces from the edges before attacking the center."
    },
    {
        "id": 26,
        "title": "Hazrat Omar (R) and the Starving Children",
        "board": "Barishal Board 2016",
        "sentences": {
            "a": "Hazrat Omar (R) became shocked and assured the woman of providing her with food.",
            "b": "She also explained that she was boiling water in a pot only to console her children.",
            "c": "He instantly went to the godown and carried a sack of food himself for that woman and her children to that cottage.",
            "d": "Hazrat Omar (R) used to go out to see the condition of his subjects with his own eyes at dead of night.",
            "e": "He asked the woman of that cottage about the cause of crying of her children.",
            "f": "One night he was passing by a cottage.",
            "g": "The woman explained that the children were crying for food as they were starving for two days.",
            "h": "He heard that children were crying."
        },
        "key": "d -> f -> h -> e -> g -> b -> a -> c",
        "paragraph": "Hazrat Omar (R) used to go out to see the condition of his subjects with his own eyes at dead of night. One night he was passing by a cottage. He heard that children were crying. He asked the woman of that cottage about the cause of crying of her children. The woman explained that the children were crying for food as they were starving for two days. She also explained that she was boiling water in a pot only to console her children. Hazrat Omar (R) became shocked and assured the woman of providing her with food. He instantly went to the godown and carried a sack of food himself for that woman and her children to that cottage."
    },
    {
        "id": 27,
        "title": "Dr. Kudrat-E-Khuda",
        "board": "SSC Exam",
        "sentences": {
            "a": "Dr. Kudrat-E-Khuda was a pioneer in scientific research in Bangladesh.",
            "b": "He was born on 8 May 1900 at village Margra in Birbhum district.",
            "c": "His father Shah Abdul Mukit was a pious man and his mother Fashiha Khatun was a noble woman.",
            "d": "At the age of seven, he was admitted to Furkania Madrasah and then to an English school.",
            "e": "In 1925, he passed M.Sc. in Chemistry with first class from Kolkata University.",
            "f": "In 1929, he obtained D.Sc. from Imperial College of Science and Technology in London.",
            "g": "He served as Chairman of the Secondary Education Board and established BCSIR.",
            "h": "This eminent scientist breathed his last on 3 November 1977."
        },
        "key": "a -> b -> c -> d -> e -> f -> g -> h",
        "paragraph": "Dr. Kudrat-E-Khuda was a pioneer in scientific research in Bangladesh. He was born on 8 May 1900 at village Margra in Birbhum district. His father Shah Abdul Mukit was a pious man and his mother Fashiha Khatun was a noble woman. At the age of seven, he was admitted to Furkania Madrasah and then to an English school. In 1925, he passed M.Sc. in Chemistry with first class from Kolkata University. In 1929, he obtained D.Sc. from Imperial College of Science and Technology in London. He served as Chairman of the Secondary Education Board and established BCSIR. This eminent scientist breathed his last on 3 November 1977."
    },
    {
        "id": 28,
        "title": "Sir Alexander Fleming's School Life",
        "board": "Dakhil Exam-2025; Dinajpur Board 2026",
        "sentences": {
            "a": "Up to the age of twelve years, he was never absent from school.",
            "b": "Penicillin is a life-saving medicine.",
            "c": "He went to school and came back home on foot.",
            "d": "It was discovered by Sir Alexander Fleming.",
            "e": "The school was four miles away from their house.",
            "f": "Fleming was born in a poor family of Scotland.",
            "g": "Fleming was a very regular and attentive student.",
            "h": "At the age of fourteen, he was sent to London for higher study."
        },
        "key": "b -> d -> f -> g -> a -> e -> c -> h",
        "paragraph": "Penicillin is a life-saving medicine. It was discovered by Sir Alexander Fleming. Fleming was born in a poor family of Scotland. Fleming was a very regular and attentive student. Up to the age of twelve years, he was never absent from school. The school was four miles away from their house. He went to school and came back home on foot. At the age of fourteen, he was sent to London for higher study."
    },
    {
        "id": 29,
        "title": "The Idle King and the Wise Physician",
        "board": "SSC Exam",
        "sentences": {
            "a": "There was an idle king who disliked physical exercise.",
            "b": "As a result of overeating and inactivity, he grew bulky and fell seriously ill.",
            "c": "Many royal physicians tried to cure him with medicine, but all failed.",
            "d": "At last, a wise physician was called from a distant city.",
            "e": "The physician understood the root cause and prescribed heavy clubs for exercise.",
            "f": "He advised the king to swing the clubs until his hands sweated profusely.",
            "g": "The king followed the advice diligently every morning for a month.",
            "h": "His excess fat burned away and he fully regained his health without pills."
        },
        "key": "a -> b -> c -> d -> e -> f -> g -> h",
        "paragraph": "There was an idle king who disliked physical exercise. As a result of overeating and inactivity, he grew bulky and fell seriously ill. Many royal physicians tried to cure him with medicine, but all failed. At last, a wise physician was called from a distant city. The physician understood the root cause and prescribed heavy clubs for exercise. He advised the king to swing the clubs until his hands sweated profusely. The king followed the advice diligently every morning for a month. His excess fat burned away and he fully regained his health without pills."
    },
    {
        "id": 30,
        "title": "Emperor Akbar and Birbal",
        "board": "SSC Exam",
        "sentences": {
            "a": "Emperor Akbar was the greatest of all Mughal rulers in India.",
            "b": "His court was adorned by nine jewels of eminent wisdom and skill.",
            "c": "Among them, Birbal was his favorite minister for his unmatched wit.",
            "d": "Akbar often tested Birbal's wisdom with complex riddles in court.",
            "e": "One day, Akbar asked how many crows were present in the capital city.",
            "f": "While other courtiers remained silent, Birbal replied confidently with an exact number.",
            "g": "He explained that if there were more, relatives were visiting; if fewer, they were away.",
            "h": "Akbar laughed heartily and praised Birbal's astonishing quick wit."
        },
        "key": "a -> b -> c -> d -> e -> f -> g -> h",
        "paragraph": "Emperor Akbar was the greatest of all Mughal rulers in India. His court was adorned by nine jewels of eminent wisdom and skill. Among them, Birbal was his favorite minister for his unmatched wit. Akbar often tested Birbal's wisdom with complex riddles in court. One day, Akbar asked how many crows were present in the capital city. While other courtiers remained silent, Birbal replied confidently with an exact number. He explained that if there were more, relatives were visiting; if fewer, they were away. Akbar laughed heartily and praised Birbal's astonishing quick wit."
    },
    {
        "id": 31,
        "title": "Michael Phelps and Usain Bolt",
        "board": "SSC Exam",
        "sentences": {
            "a": "The Olympic Games have produced many legendary sporting icons in history.",
            "b": "The 2012 London Olympics stood apart due to two living legends.",
            "c": "Michael Phelps of USA and Usain Bolt of Jamaica dominated the world.",
            "d": "Phelps became the most decorated Olympian with 22 career medals in swimming.",
            "e": "Bolt electrified the stadium by winning double gold in 100m and 200m sprints.",
            "f": "Both athletes proved that hard work and determination create history.",
            "g": "They set world records that inspired millions of young athletes.",
            "h": "They made London Olympics a memorable chapter in sporting history."
        },
        "key": "a -> b -> c -> d -> e -> g -> f -> h",
        "paragraph": "The Olympic Games have produced many legendary sporting icons in history. The 2012 London Olympics stood apart due to two living legends. Michael Phelps of USA and Usain Bolt of Jamaica dominated the world. Phelps became the most decorated Olympian with 22 career medals in swimming. Bolt electrified the stadium by winning double gold in 100m and 200m sprints. They set world records that inspired millions of young athletes. Both athletes proved that hard work and determination create history. They made London Olympics a memorable chapter in sporting history."
    },
    {
        "id": 32,
        "title": "Sheikh Saadi and His Dress",
        "board": "Sylhet Board 2025; Chattogram Board 2026",
        "sentences": {
            "a": "On the way, he took shelter in a courtier's house. The courtier and his men did not show much honour and hospitality to him.",
            "b": "They asked, 'Why are you putting the foods in your dress?' The courtier understood his fault and begged the poet's pardon.",
            "c": "Sheikh Saadi was a great Persian poet. He was simple in his ways of life.",
            "d": "On his way back home, Saadi again took shelter in the same courtier's house.",
            "e": "Once he was invited to the Emperor's Palace.",
            "f": "This time he put on a gorgeous dress. The courtier received him cordially and entertained him with rich and delicious foods.",
            "g": "He set out for the Emperor's Palace in an ordinary dress.",
            "h": "Now Saadi began to put his foods in the pockets of his dress. The courtier's men were surprised to see this."
        },
        "key": "c -> e -> g -> a -> d -> f -> h -> b",
        "paragraph": "Sheikh Saadi was a great Persian poet. He was simple in his ways of life. Once he was invited to the Emperor's Palace. He set out for the Emperor's Palace in an ordinary dress. On the way, he took shelter in a courtier's house. The courtier and his men did not show much honour and hospitality to him. On his way back home, Saadi again took shelter in the same courtier's house. This time he put on a gorgeous dress. The courtier received him cordially and entertained him with rich and delicious foods. Now Saadi began to put his foods in the pockets of his dress. The courtier's men were surprised to see this. They asked, 'Why are you putting the foods in your dress?' The courtier understood his fault and begged the poet's pardon."
    },
    {
        "id": 33,
        "title": "Jalaluddin Rumi: Life and Teachings",
        "board": "Rajshahi Board 2026",
        "sentences": {
            "a": "Jalal at-Din Muhammad Rumi, widely known as Rumi was born in 1207, in Balkh, a region that is now part of Afghanistan.",
            "b": "His life changed profoundly after meeting the wandering dervish, Shams Tabrizi.",
            "c": "After Shams disappeared, Rumi expressed his longing and devotion through poetry.",
            "d": "Rumi's teaching on love, compassion and unity continue to inspire people around the world.",
            "e": "His family moved to Konya in present day Turkey when he was a young boy.",
            "f": "Their deep spiritual friendship inspired Rumi to seek a new understanding of divine love.",
            "g": "Rumi became a respected Islamic scholar and a teacher following his father's footsteps.",
            "h": "He eventually composed Masnavi, one of his greatest works."
        },
        "key": "a -> e -> g -> b -> f -> c -> h -> d",
        "paragraph": "Jalal at-Din Muhammad Rumi, widely known as Rumi was born in 1207, in Balkh, a region that is now part of Afghanistan. His family moved to Konya in present day Turkey when he was a young boy. Rumi became a respected Islamic scholar and a teacher following his father's footsteps. His life changed profoundly after meeting the wandering dervish, Shams Tabrizi. Their deep spiritual friendship inspired Rumi to seek a new understanding of divine love. After Shams disappeared, Rumi expressed his longing and devotion through poetry. He eventually composed Masnavi, one of his greatest works. Rumi's teaching on love, compassion and unity continue to inspire people around the world."
    },
    {
        "id": 34,
        "title": "Alfred Nobel and the Nobel Prize",
        "board": "SSC Exam",
        "sentences": {
            "a": "He earned a lot of money from his dynamite business.",
            "b": "This award was named after Alfred Nobel.",
            "c": "He was an engineer.",
            "d": "Dr. Alfred Nobel was born on 21 October 1833 at Stockholm, Sweden.",
            "e": "So, it was called the Nobel Prize.",
            "f": "He invented dynamite after some years of joining his father's company.",
            "g": "This award was also given for setting up peace in the world.",
            "h": "He undertook a plan to give an award for encouraging the creative work."
        },
        "key": "d -> c -> f -> a -> h -> b -> e -> g",
        "paragraph": "Dr. Alfred Nobel was born on 21 October 1833 at Stockholm, Sweden. He was an engineer. He invented dynamite after some years of joining his father's company. He earned a lot of money from his dynamite business. He undertook a plan to give an award for encouraging the creative work. This award was named after Alfred Nobel. So, it was called the Nobel Prize. This award was also given for setting up peace in the world."
    },
    {
        "id": 35,
        "title": "The Two Crows and the Clever Dog",
        "board": "SSC Exam",
        "sentences": {
            "a": "Both the crows went near the dog.",
            "b": "The dog dropped the bone and barked at the crow.",
            "c": "One of them started pecking the dog's tail.",
            "d": "A dog was chewing a juicy bone under a shady banyan tree.",
            "e": "Two hungry crows saw the dog with the bone and wanted to have it.",
            "f": "They made a clever plan to snatch the bone from the dog.",
            "g": "The second crow instantly flew away with the bone in its beak.",
            "h": "The dog was left helpless while the crows enjoyed their feast."
        },
        "key": "d -> e -> f -> a -> c -> b -> g -> h",
        "paragraph": "A dog was chewing a juicy bone under a shady banyan tree. Two hungry crows saw the dog with the bone and wanted to have it. They made a clever plan to snatch the bone from the dog. Both the crows went near the dog. One of them started pecking the dog's tail. The dog dropped the bone and barked at the crow. The second crow instantly flew away with the bone in its beak. The dog was left helpless while the crows enjoyed their feast."
    },
    {
        "id": 36,
        "title": "King Alexander and King Purus",
        "board": "SSC Exam",
        "sentences": {
            "a": "Alexander the Great, the King of Macedonia, invaded India in 326 BC.",
            "b": "He was opposed by the courageous Indian King Purus at the Battle of the Hydaspes.",
            "c": "After a fierce and bloody struggle, King Purus was wounded and taken prisoner.",
            "d": "Purus was brought before Alexander in chains, yet he held his head high.",
            "e": "Alexander was impressed by his regal dignity and asked how he wished to be treated.",
            "f": "Purus replied boldly, 'Like a king!'",
            "g": "Alexander was so pleased with his fearless response that he set him free.",
            "h": "He restored Purus to his throne and added more territories to his kingdom."
        },
        "key": "a -> b -> c -> d -> e -> f -> g -> h",
        "paragraph": "Alexander the Great, the King of Macedonia, invaded India in 326 BC. He was opposed by the courageous Indian King Purus at the Battle of the Hydaspes. After a fierce and bloody struggle, King Purus was wounded and taken prisoner. Purus was brought before Alexander in chains, yet he held his head high. Alexander was impressed by his regal dignity and asked how he wished to be treated. Purus replied boldly, 'Like a king!' Alexander was so pleased with his fearless response that he set him free. He restored Purus to his throne and added more territories to his kingdom."
    }
]

DAKHIL_2026_REARRANGE = {
    "title": "Prophet Muhammad (Sm) and the Poor Beggar",
    "board": "Dakhil Board Exam 2026 (Question 7)",
    "sentences": {
        "a": "I don't have any money.",
        "b": "One day a poor man came to Prophet Hazrat Muhammad (Sm).",
        "c": "He said 'Oh, Prophet! I am very poor.'",
        "d": "I need some money.",
        "e": "He begged for money.",
        "f": "My wife and children are hungry.",
        "g": "The Prophet (Sm) looked at the man and found him strong.",
        "h": "I don't have any food in my house."
    },
    "key": "b -> e -> c -> a -> h -> f -> d -> g",
    "paragraph": "One day a poor man came to Prophet Hazrat Muhammad (Sm). He begged for money. He said 'Oh, Prophet! I am very poor.' I don't have any money. I don't have any food in my house. My wife and children are hungry. I need some money. The Prophet (Sm) looked at the man and found him strong."
}

MODEL_TEST_REARRANGE = {
    "title": "Sir Alexander Fleming and the Life-Saving Medicine Penicillin",
    "board": "Exclusive Model Test (Question 7)",
    "sentences": {
        "a": "He passed his boyhood with his parents.",
        "b": "It was discovered by Alexander Fleming.",
        "c": "He was the seventh of eight brothers and sisters.",
        "d": "Penicillin is a life saving medicine.",
        "e": "He was never absent from school up to the age of twelve.",
        "f": "He was sent to London at the age of fourteen for higher study.",
        "g": "Fleming was born in a poor family in Scotland.",
        "h": "Fleming was a very regular and attentive student."
    },
    "key": "d -> b -> g -> c -> a -> h -> e -> f",
    "paragraph": "Penicillin is a life saving medicine. It was discovered by Alexander Fleming. Fleming was born in a poor family in Scotland. He was the seventh of eight brothers and sisters. He passed his boyhood with his parents. Fleming was a very regular and attentive student. He was never absent from school up to the age of twelve. He was sent to London at the age of fourteen for higher study."
}

