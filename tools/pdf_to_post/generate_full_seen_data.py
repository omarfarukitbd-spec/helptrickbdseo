#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/pdf_to_post/generate_full_seen_data.py
----------------------------------------------
Generates data_ssc_2027_seen_full.py containing all 33 Seen Passages:
- Passage excerpt from English For Today (120-170 words)
- Question 1: Multiple Choice Questions (3 board-standard MCQs with options and answers)
- Question 2: Open-Ended Comprehension Questions (2 analytical questions with model answers)
- Question 3: Gap Filling Without Clues (5 blanks with exact answer key)
- Vocabulary & Synonyms Notes
- Star rating, EFT Unit & Lesson, and board references.
"""

import os
import sys

OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "data_ssc_2027_seen_full.py")

SEEN_DATA_33 = [
    {
        "id": 1,
        "slug_id": "seen-01",
        "title": "Meherjan's Struggle with River Erosion (মেহেরজানের নদীভাঙন ও নিঃস্ব জীবন)",
        "unit_lesson": "Unit-2, Lesson-1(A)",
        "theme": "Climate Change, Jamuna River Erosion & Homeless Victims",
        "stars": "***",
        "priority": "Top Priority (Most Probable)",
        "boards": "Ctg.B., Dinj.B. '19, B.B. '22, J.B. '23, C.B., Syl.B., M.B. '26",
        "passage": (
            "Meherjan lives in a slum on the Sirajganj Town Protection Embankment. Her polythene-roofed shelter looks like "
            "a cage. She is nearly 45, but looks more than her age. In front of her shelter, she is trying to make a fire to "
            "cook the day's only meal. Her weak hands tremble as she adds some fallen leaves and straw to the fire. The whispering "
            "wind from the river Jamuna makes the fire unsteady. The dancing flames remind Meherjan of the turmoil in her life. "
            "Not long ago Meherjan had everything—a family, cultivable land and cattle. The erosion of the Jamuna gradually "
            "consumed all her landed property. It finally claimed her only shelter during the last monsoon. Now, she is only one "
            "of the estimated one lakh people who become homeless in Bangladesh every year due to river erosion."
        ),
        "mcqs": [
            {"q": "What does the phrase 'dancing flames' symbolize in the passage?", "opts": ["A joyful festival", "Instability and turmoil in Meherjan's life", "Cold winter wind", "A burning forest"], "ans": "Instability and turmoil in Meherjan's life"},
            {"q": "How does river erosion affect the population of Bangladesh annually?", "opts": ["It enriches farmers", "It makes nearly one lakh people homeless", "It prevents floods", "It stops monsoon rains"], "ans": "It makes nearly one lakh people homeless"},
            {"q": "The word 'consume' in the passage is closest in meaning to —", "opts": ["Preserve", "Devour or destroy", "Construct", "Purchase"], "ans": "Devour or destroy"}
        ],
        "open_qas": [
            {"q": "What did Meherjan lose to the fierce erosion of the river Jamuna?", "a": "Meherjan lost her family, cultivable land, cattle, and her last remaining homestead shelter to the relentless erosion of the river Jamuna, reducing her to an impoverished slum dweller."},
            {"q": "Why does Meherjan look much older than her actual age?", "a": "Meherjan looks much older than her forty-five years because of prolonged poverty, malnutrition, the physical exhaustion of displacement, and the severe emotional trauma of losing everything."}
        ],
        "gap_fill": {
            "sentence": "River erosion is one of the most devastating (a) ______ in Bangladesh. Every monsoon, mighty rivers like the Jamuna (b) ______ vast tracts of cultivable land and homesteads. As a result, countless families like Meherjan's are rendered completely (c) ______ and forced to take shelter in urban (d) ______. Proper embankment construction and climate adaptation are urgently needed to (e) ______ their suffering.",
            "answers": {"a": "calamities / disasters", "b": "erode / devour", "c": "homeless / destitute", "d": "slums / shanties", "e": "mitigate / lessen"}
        },
        "vocab_notes": "Turmoil -> Agitation/chaos; Embankment -> Protective dike; Destitute -> Impoverished."
    },
    {
        "id": 2,
        "slug_id": "seen-02",
        "title": "Environmental Pollution in Bangladesh: Industrial and Urban Threats",
        "unit_lesson": "Unit-2, Lesson-2(B)",
        "theme": "Environmental Pollution, Air, Water and Soil Contamination",
        "stars": "*",
        "priority": "Moderate",
        "boards": "J. B. '26",
        "passage": (
            "Bangladesh is now in the grip of all sorts of environmental pollution—air pollution, water pollution, and soil pollution. "
            "The dwellers of urban areas are the worst sufferers of such pollution. Indiscriminate industrialization, rapid urbanization, "
            "and motorized transport are primarily responsible for contaminating the environment. Brick kilns and old vehicles emit toxic "
            "black smoke loaded with carbon monoxide and sulfur dioxide, severely degrading air quality in major cities like Dhaka. "
            "Simultaneously, industrial untreated effluents and household refuse are dumped into rivers like the Buriganga, rendering water "
            "biologically dead. Furthermore, excessive chemical fertilizers and non-biodegradable plastics degrade the fertility of topsoil."
        ),
        "mcqs": [
            {"q": "Which group of people suffers most severely from environmental pollution?", "opts": ["Rural farmers", "Inhabitants of urban areas", "Coastal fishermen", "Forest inhabitants"], "ans": "Inhabitants of urban areas"},
            {"q": "What makes the water of the Buriganga biologically dead?", "opts": ["Natural floodwater", "Untreated industrial waste and sewage", "Excessive fish breeding", "Rainwater"], "ans": "Untreated industrial waste and sewage"},
            {"q": "The word 'indiscriminate' means —", "opts": ["Planned", "Random and unselective", "Careful", "Legal"], "ans": "Random and unselective"}
        ],
        "open_qas": [
            {"q": "What are the primary sources of air pollution in metropolitan cities like Dhaka?", "a": "The primary sources of air pollution are emissions from outdated motorized vehicles, smoke from illegal brick kilns, dust from unregulated construction, and toxic emissions from urban industrial plants."},
            {"q": "How does soil pollution occur in Bangladesh?", "a": "Soil pollution occurs through the excessive application of synthetic chemical fertilizers and pesticides in farming, alongside the reckless dumping of non-biodegradable polythene bags and industrial solid waste."}
        ],
        "gap_fill": {
            "sentence": "Environmental pollution has reached an alarming (a) ______ in Bangladesh. Urban dwellers face severe health (b) ______ due to contaminated air and poisoned rivers. If strict environmental regulations and afforestation are not (c) ______ immediately, future generations will face catastrophic ecological (d) ______. Every citizen must raise (e) ______ to protect our ecosystem.",
            "answers": {"a": "level / stage", "b": "risks / hazards", "c": "enforced / implemented", "d": "disasters / crises", "e": "awareness / consciousness"}
        },
        "vocab_notes": "Effluents -> Industrial liquid waste; Degrade -> Deteriorate; Inhabitants -> Residents."
    },
    {
        "id": 3,
        "slug_id": "seen-03",
        "title": "Humans and Global Climate: Greenhouse Gases and Deforestation",
        "unit_lesson": "Unit-2, Lesson-3(A)",
        "theme": "Climate Change, Human Impact & Greenhouse Gas Emissions",
        "stars": "***",
        "priority": "Top Priority (Most Probable)",
        "boards": "D. B., Ctg. B. '26",
        "passage": (
            "Humans can neither change the sun's radiation nor the earth's orbit around the sun. But they can control the increase "
            "in the amount of greenhouse gases and its effect on the atmosphere. Only during the last hundred years, the concentration "
            "of carbon dioxide has risen alarmingly due to the reckless combustion of coal, oil, and natural gas in power plants and "
            "factories. Furthermore, humans are destroying millions of hectares of tropical forests every year to create farmland and "
            "procure timber. Trees naturally absorb vast quantities of carbon dioxide through photosynthesis; when forests are cleared "
            "and burnt, stored carbon is released back into the air. This atmospheric blanket traps heat, driving catastrophic global warming."
        ),
        "mcqs": [
            {"q": "What can humans actively control regarding global climate change?", "opts": ["Earth's orbital path", "The sun's solar radiation", "Greenhouse gas emissions and deforestation", "Oceanic tides"], "ans": "Greenhouse gas emissions and deforestation"},
            {"q": "Why does deforestation accelerate global warming?", "opts": ["Trees produce carbon dioxide", "Forests absorb less sunlight", "Felled trees can no longer absorb CO2 and release stored carbon", "Trees cause excessive rainfall"], "ans": "Felled trees can no longer absorb CO2 and release stored carbon"},
            {"q": "The term 'combustion' refers to —", "opts": ["Cooling", "Burning or chemical oxidation", "Planting", "Recycling"], "ans": "Burning or chemical oxidation"}
        ],
        "open_qas": [
            {"q": "How does industrial fossil fuel consumption enhance the greenhouse effect?", "a": "Industrial combustion of coal, gas, and oil releases massive volumes of carbon dioxide and other heat-trapping gases into the atmosphere, creating a thick heat-retaining blanket that prevents thermal radiation from escaping into space."},
            {"q": "What critical role do forests play in maintaining atmospheric balance?", "a": "Forests serve as vital carbon sinks by absorbing atmospheric carbon dioxide during photosynthesis and releasing life-sustaining oxygen, thereby naturally regulating global temperatures."}
        ],
        "gap_fill": {
            "sentence": "Global warming is largely the result of human (a) ______ on earth. By burning fossil fuels and felling trees (b) ______, humans have upset the delicate atmospheric balance. If we desire to protect our planet, we must reduce greenhouse gas (c) ______ and adopt clean (d) ______ sources. Preserving forests is also (e) ______ for climate stabilization.",
            "answers": {"a": "activities / interference", "b": "indiscriminately / recklessly", "c": "emissions / discharge", "d": "renewable / green", "e": "vital / essential"}
        },
        "vocab_notes": "Combustion -> Burning; Photosynthesis -> Plant food synthesis; Radiation -> Energy emission."
    },
    {
        "id": 4,
        "slug_id": "seen-04",
        "title": "Let's Save Our Planet: Waste Management and the 3Rs Principle",
        "unit_lesson": "Unit-2, Lesson-5(B)",
        "theme": "Ecological Conservation, 3Rs (Reduce, Reuse, Recycle) & Waste Management",
        "stars": "**",
        "priority": "High Priority",
        "boards": "Syl.B. '22, R. B. '26",
        "passage": (
            "LET'S SAVE OUR PLANET! Everyone produces waste daily, but how we manage that waste determines the future of our biosphere. "
            "To conserve the earth's dwindling natural resources and prevent landfill overflow, we must rigorously adopt the '3Rs' principle—"
            "Reduce, Reuse, and Recycle. 'Reduce' means cutting down on personal consumption and using fewer disposable products. 'Reuse' "
            "involves utilizing items repeatedly instead of discarding them after a single use, such as refilling glass bottles or donating "
            "clothing. 'Recycle' transforms discarded materials like paper, metal cans, and glass into valuable new products, substantially "
            "saving energy and reducing raw material extraction. Small household habits can create a profound global difference."
        ),
        "mcqs": [
            {"q": "What do the '3Rs' represent in modern environmental conservation?", "opts": ["Read, Revise, Repeat", "Reduce, Reuse, Recycle", "Refuse, Restore, Rebuild", "Reform, Regenerate, Renew"], "ans": "Reduce, Reuse, Recycle"},
            {"q": "How does recycling save natural resources?", "opts": ["By discarding more waste", "By manufacturing new items from waste materials without extracting virgin resources", "By burning plastic", "By polluting rivers"], "ans": "By manufacturing new items from waste materials without extracting virgin resources"},
            {"q": "The word 'dwindling' is synonymous with —", "opts": ["Expanding", "Diminishing or decreasing", "Permanent", "Abundant"], "ans": "Diminishing or decreasing"}
        ],
        "open_qas": [
            {"q": "What is the difference between 'reusing' and 'recycling'?", "a": "'Reusing' means using an item again in its original form for the same or a different purpose, whereas 'recycling' involves reprocessing waste material chemically or industrially to manufacture entirely new products."},
            {"q": "How can ordinary citizens contribute to reducing household waste?", "a": "Citizens can minimize waste by choosing durable goods over disposable ones, carrying reusable cloth bags, avoiding unnecessary packaging, and conserving electricity and water in daily life."}
        ],
        "gap_fill": {
            "sentence": "Effective waste management is vital to preserve our fragile (a) ______. Practicing the 3Rs helps reduce the volume of garbage dumped into (b) ______. By reusing durable containers and recycling metals, we conserve energy and raw (c) ______. Therefore, environmental education must be (d) ______ in every school to build a sustainable (e) ______.",
            "answers": {"a": "ecosystem / planet", "b": "landfills / dumpsites", "c": "materials / resources", "d": "promoted / taught", "e": "future / world"}
        },
        "vocab_notes": "Biosphere -> Earth's living zone; Diminishing -> Dwindling; Virgin resources -> Untouched raw materials."
    },
    {
        "id": 5,
        "slug_id": "seen-05",
        "title": "Youth Pastimes: Shyam's Village Childhood and Rural Creativity",
        "unit_lesson": "Unit-3, Lesson-1(G)",
        "theme": "Youth Recreation, Rural Lifestyle & Artistic Expression",
        "stars": "*",
        "priority": "Moderate",
        "boards": "B. B. '26",
        "passage": (
            "Hi, I'm Shyam. I'm from Magura, a scenic district in southwestern Bangladesh. While many urban teenagers spend their leisure "
            "glued to smartphone screens and online video games, my favourite pastimes are deeply rooted in rural nature. In the scorching "
            "summer, I love swimming in the local river with my village friends and fishing with traditional bamboo traps. During the rainy "
            "season, I sit on the porch of our tin-roofed house and sketch the rain-soaked paddy fields and monsoon greenery with watercolours. "
            "Drawing nature has taught me patience and observation. I believe engaging with nature keeps both our physical body healthy and "
            "our creative spirit imaginative."
        ),
        "mcqs": [
            {"q": "Where does Shyam spend most of his leisure hours?", "opts": ["In internet cafes", "Amidst rural nature and artistic drawing", "In metropolitan shopping malls", "At cinema halls"], "ans": "Amidst rural nature and artistic drawing"},
            {"q": "What skill has sketching nature fostered in Shyam?", "opts": ["Competitiveness", "Patience and keen observation", "Aggression", "Boredom"], "ans": "Patience and keen observation"},
            {"q": "The word 'scorching' describes weather that is —", "opts": ["Freezing cold", "Pleasantly breezy", "Extremely hot", "Cloudy"], "ans": "Extremely hot"}
        ],
        "open_qas": [
            {"q": "How do Shyam's pastimes differ from those of urban adolescents?", "a": "Unlike urban adolescents who are largely confined indoors by electronic gadgets and video games, Shyam actively engages in outdoor river swimming, angling, and artistic painting inspired by pastoral nature."},
            {"q": "Why is outdoor interaction beneficial for growing children?", "a": "Interacting with nature provides physical exercise, stimulates imaginative thinking, instills emotional calmness, and cultivates an appreciation for biological biodiversity."}
        ],
        "gap_fill": {
            "sentence": "Healthy leisure activities are essential for a child's harmonious (a) ______. Spending time outdoors allows youth to develop (b) ______ health and creative vitality. Unlike passive digital addiction, activities like swimming and painting foster (c) ______ and self-reliance. Parents should (d) ______ their children to spend quality time in natural (e) ______.",
            "answers": {"a": "growth / development", "b": "physical / mental", "c": "patience / imagination", "d": "encourage / inspire", "e": "environments / surroundings"}
        },
        "vocab_notes": "Scorching -> Blistering hot; Observation -> Scrutiny; Pastime -> Hobby/recreation."
    },
    {
        "id": 6,
        "slug_id": "seen-06",
        "title": "Changing Childhood Pastimes: The Shift from Open Fields to Digital Screens",
        "unit_lesson": "Unit-3, Lesson-3(A)",
        "theme": "Generational Shift in Recreation, Urban Congestion & Screen Addiction",
        "stars": "**",
        "priority": "High Priority",
        "boards": "Dinj. B. '26",
        "passage": (
            "Childhood outdoor pastimes in Bangladesh have witnessed a radical transformation over the past three decades. In previous "
            "generations, children would rush to open fields after school to play traditional indigenous games like Ha-du-du, Dariabandha, "
            "Gollachhut, and cricket. These collective games promoted physical stamina, teamwork, and social empathy. In stark contrast, "
            "unplanned urban growth has encroached upon public playgrounds and green parks in modern cities. Consequently, today's young "
            "generation is largely confined to cramped apartments, spending hours staring at computer screens, smartphones, and televisions. "
            "Health specialists warn that this sedentary lifestyle induces childhood obesity, visual impairment, and social isolation."
        ),
        "mcqs": [
            {"q": "What has caused the decline of outdoor games in contemporary urban areas?", "opts": ["Lack of interest in games", "Disappearance of playgrounds due to rapid urbanization", "Ban on sports by schools", "Absence of sports gear"], "ans": "Disappearance of playgrounds due to rapid urbanization"},
            {"q": "What health hazards stem from excessive indoor sedentary habits?", "opts": ["Athletic agility", "Childhood obesity, eyesight problems, and isolation", "Superior stamina", "Enhanced immune strength"], "ans": "Childhood obesity, eyesight problems, and isolation"},
            {"q": "The word 'encroach' in the context means —", "opts": ["To liberate", "To intrude upon or trespass gradually", "To decorate", "To donate"], "ans": "To intrude upon or trespass gradually"}
        ],
        "open_qas": [
            {"q": "What social virtues were cultivated through traditional Bengali village games?", "a": "Traditional games like Ha-du-du and Gollachhut fostered physical endurance, leadership skills, cooperative team spirit, mutual empathy, and healthy socialization among youngsters."},
            {"q": "What measures should urban authorities take to revive outdoor sports for youth?", "a": "City authorities must preserve existing playgrounds, construct community sports complexes, restrict illegal land grabbing of parks, and mandate open spaces in residential urban planning."}
        ],
        "gap_fill": {
            "sentence": "The recreational habits of children have changed (a) ______ over recent decades. The scarcity of open playgrounds in cities has forced youths into a (b) ______ lifestyle dominated by digital devices. This shift has triggered severe physical and (c) ______ health issues among teenagers. It is high time city planners (d) ______ public spaces to ensure the wholesome (e) ______ of children.",
            "answers": {"a": "drastically / radically", "b": "sedentary / indoor", "c": "mental / psychological", "d": "created / protected", "e": "development / well-being"}
        },
        "vocab_notes": "Sedentary -> Physically inactive; Encroached -> Trespassed; Stamina -> Endurance."
    },
    {
        "id": 7,
        "slug_id": "seen-07",
        "title": "May Day: The Historic Struggle for an Eight-Hour Workday",
        "unit_lesson": "Unit-4, Lesson-2(B)",
        "theme": "Labour Rights, Chicago Haymarket Massacre (1886) & Working Hours",
        "stars": "***",
        "priority": "Top Priority (Most Probable)",
        "boards": "Dakhil Exam-2019; C.B. '24, D.B. '20, '22, '25, Dinj.B. '25",
        "passage": (
            "May Day or International Workers' Day is observed on May 1 all over the world to commemorate the historic struggle "
            "and sacrifices of the working class people to establish an eight-hour workday. Since the Industrial Revolution in the 18th "
            "and 19th centuries, factory labourers in Europe and the United States were forced to work grueling shifts of fourteen or "
            "more hours a day under deplorable, dangerous conditions. On 1 May 1886, inspired by trade unions, thousands of workers "
            "at the McCormick Harvesting Machine Company in Chicago launched a general strike demanding an eight-hour workday. "
            "On 4 May, police fired indiscriminately into a peaceful gathering at Haymarket Square, killing at least one striker and "
            "injuring dozens. The event galvanized the global labour movement, winning dignity and fair wages for all workers."
        ),
        "mcqs": [
            {"q": "What was the fundamental demand of the Chicago striking workers in 1886?", "opts": ["Free meals", "An eight-hour standard workday", "Longer vacations", "Ownership of the factory"], "ans": "An eight-hour standard workday"},
            {"q": "Where did the tragic police firing on workers take place?", "opts": ["Times Square, New York", "Haymarket Square, Chicago", "Trafalgar Square, London", "Bastille, Paris"], "ans": "Haymarket Square, Chicago"},
            {"q": "The word 'commemorate' signifies —", "opts": ["To ignore", "To celebrate or remember with solemn honor", "To criticize", "To postpone"], "ans": "To celebrate or remember with solemn honor"}
        ],
        "open_qas": [
            {"q": "Why is May Day celebrated across the globe with profound solemnity?", "a": "May Day is celebrated worldwide to pay homage to the brave martyrs of the 1886 Chicago Haymarket massacre whose supreme sacrifices liberated working people from exploitative fourteen-hour workdays and secured constitutional labour rights."},
            {"q": "What were the conditions of factory labourers prior to the 1886 Chicago strike?", "a": "Before the strike, labourers endured exploitative working shifts of fourteen to sixteen hours daily, meager wages, absence of safety regulations, and complete vulnerability to factory owners' whims."}
        ],
        "gap_fill": {
            "sentence": "May Day stands as an immortal milestone in the history of human (a) ______. Before this historic movement, labourers were treated like (b) ______ slaves by capitalist owners. The martyrdom of Chicago workers paved the way for legal (c) ______ regarding humane working hours. Today, May 1 is observed globally to ensure fair (d) ______ and safety for the (e) ______ class.",
            "answers": {"a": "dignity / rights", "b": "oppressed / industrial", "c": "reforms / standards", "d": "wages / treatment", "e": "working / labouring"}
        },
        "vocab_notes": "Deplorable -> Miserable; Galvanized -> Activated; Commemorate -> Honor in memory."
    },
    {
        "id": 8,
        "slug_id": "seen-08",
        "title": "21 February: National Mourning and the Genesis of Independence",
        "unit_lesson": "Unit-4, Lesson-3(B)",
        "theme": "Language Movement (1952), Salam-Barkat-Rafiq & Seeds of Independence",
        "stars": "***",
        "priority": "Top Priority (Most Probable)",
        "boards": "Dakhil Exam-2017; R.B. '23",
        "passage": (
            "21 February is a memorable day in our national history, observed every year as 'Shaheed Dibosh' and 'International "
            "Mother Language Day'. On this day in 1952, heroic students of Dhaka University and common citizens laid down their lives "
            "to establish Bangla as one of the state languages of Pakistan. When the colonial Pakistani regime declared Urdu as the "
            "sole state language, the entire population of East Pakistan erupted in defiance. Defying Section 144 on 21 February 1952, "
            "a historic student procession was fired upon by police near Dhaka Medical College. Salam, Barkat, Rafiq, Jabbar, and Shafiur "
            "embraced martyrdom. This supreme linguistic sacrifice ignited the eternal flame that culminated in the 1971 Liberation War."
        ),
        "mcqs": [
            {"q": "Why did the students of Dhaka University defy Section 144 in 1952?", "opts": ["For lower tuition fees", "To demand Bangla as a state language", "To celebrate a festival", "To join elections"], "ans": "To demand Bangla as a state language"},
            {"q": "Who were among the celebrated martyrs of the 21 February language demonstration?", "opts": ["Milton and Wordsworth", "Salam, Barkat, Rafiq, Jabbar and Shafiur", "Hillary and Tenzing", "Zahir and Babur"], "ans": "Salam, Barkat, Rafiq, Jabbar and Shafiur"},
            {"q": "The Language Movement is regarded as the 'seed' of independence because —", "opts": ["It stopped wars", "It awakened Bengali national identity and led to the 1971 Liberation War", "It was supported by Britain", "It was fought on borders"], "ans": "It awakened Bengali national identity and led to the 1971 Liberation War"}
        ],
        "open_qas": [
            {"q": "Why is 21 February revered as the catalyst for Bangladesh's liberation?", "a": "21 February is revered as the catalyst because the blood shed by language martyrs shattered the myth of Pakistani statehood, galvanized secular Bengali nationalism, and initiated an unstoppable chain of political movements culminating in independence in 1971."},
            {"q": "How do the people of Bangladesh observe Shaheed Dibosh on the morning of 21 February?", "a": "People walk barefoot in solemn processions (Probhat Pheri) singing 'Amar Bhaier Rokte Rangano Ekushey February', offering floral tributes at the Central Shaheed Minar to honor the language martyrs."}
        ],
        "gap_fill": {
            "sentence": "The Language Movement of 1952 is a glorious chapter in our (a) ______. The brave youths of Bengal shed their blood to (b) ______ the honour of their mother tongue. Their supreme sacrifice taught the nation never to bow down to (c) ______. This spirit of resistance eventually (d) ______ the 1971 Liberation War, securing our sovereign (e) ______.",
            "answers": {"a": "heritage / history", "b": "defend / uphold", "c": "injustice / tyranny", "d": "sparked / inspired", "e": "nation / motherland"}
        },
        "vocab_notes": "Defiance -> Bold resistance; Catalyzed -> Prompted; Linguistic -> Related to language."
    },
    {
        "id": 9,
        "slug_id": "seen-09",
        "title": "International Mother Language Day: Global Recognition of Linguistic Diversity",
        "unit_lesson": "Unit-4, Lesson-4(B)",
        "theme": "UNESCO Proclamation (1999), Multilingualism & Cultural Heritage",
        "stars": "**",
        "priority": "High Priority",
        "boards": "Dakhil Exam-2022; C.B. '19",
        "passage": (
            "21 February is observed worldwide as International Mother Language Day following a historic resolution adopted "
            "by the General Conference of UNESCO in November 1999. The initiative originated from a passionate appeal made by expatriate "
            "Bangladeshis in Vancouver, Canada, who formed the 'Mother Language Lovers of the World' society. Supported by the Bangladesh "
            "Government, UNESCO unanimously proclaimed 21 February to promote linguistic and cultural diversity and multilingualism across "
            "the globe. Today, over seven thousand spoken languages exist worldwide, many of which face extinction. International Mother "
            "Language Day reminds humanity of every individual's fundamental right to speak, study, and preserve their ancestral tongue."
        ),
        "mcqs": [
            {"q": "Which international organization declared 21 February as International Mother Language Day?", "opts": ["UNICEF", "UNESCO", "WHO", "Interpol"], "ans": "UNESCO"},
            {"q": "In which year was the resolution adopted by UNESCO?", "opts": ["1952", "1971", "1999", "2005"], "ans": "1999"},
            {"q": "The primary objective of International Mother Language Day is —", "opts": ["Promoting single global language", "Fostering linguistic and cultural diversity and multilingualism", "Translating novels", "Ending internet communication"], "ans": "Fostering linguistic and cultural diversity and multilingualism"}
        ],
        "open_qas": [
            {"q": "How did Bangladesh's language sacrifice acquire worldwide international recognition?", "a": "Expatriate Bangladeshis in Canada initiated the proposal, which was formally sponsored by the Bangladesh Government at UNESCO in 1999, resulting in the unanimous adoption of 21 February as International Mother Language Day by all member states."},
            {"q": "Why is multilingualism crucial for global civilization?", "a": "Multilingualism preserves ancient indigenous knowledge, promotes intercultural tolerance, enriches cognitive development, and prevents the tragic extinction of minority cultural identities."}
        ],
        "gap_fill": {
            "sentence": "UNESCO's declaration of International Mother Language Day is a great (a) ______ for Bangladesh. It has elevated our local language martyrs to (b) ______ heroes. The day encourages all countries to preserve their (c) ______ languages from extinction. Respecting minority languages is vital for international (d) ______ and mutual (e) ______.",
            "answers": {"a": "pride / honour", "b": "universal / global", "c": "native / indigenous", "d": "harmony / peace", "e": "respect / brotherhood"}
        },
        "vocab_notes": "Multilingualism -> Use of several languages; Unanimous -> In complete agreement; Proclamation -> Official declaration."
    },
    {
        "id": 10,
        "slug_id": "seen-10",
        "title": "26 March: Independence Day of Bangladesh and National Glory",
        "unit_lesson": "Unit-4, Lesson-5(B)",
        "theme": "Independence Day, 26 March, National Memorial at Savar & Statehood",
        "stars": "***",
        "priority": "Top Priority (Most Probable)",
        "boards": "J.B. '19, Syl.B. '19, '20; Dinj.B. '22, C.B. '23, D.B. '24",
        "passage": (
            "26 March, our Independence Day, is the biggest state festival in Bangladesh, celebrated nationwide with immense "
            "patriotic enthusiasm and fervour. It marks the day in 1971 when the heroic nation declared its independence following "
            "the brutal crackdown by the Pakistani military under Operation Searchlight. The day commences with a 31-gun salute at dawn. "
            "Early in the morning, the President and the Prime Minister, on behalf of the entire nation, place floral wreaths at the "
            "National Memorial at Savar to honour the three million martyrs. Political parties, educational institutions, freedom fighters, "
            "and ordinary citizens throng to Savar in colorful processions to renew their vow to build a poverty-free, democratic nation."
        ),
        "mcqs": [
            {"q": "How does the national celebration of 26 March commence at dawn?", "opts": ["With musical concerts", "With a 31-gun salute", "With school examinations", "With a military parade"], "ans": "With a 31-gun salute"},
            {"q": "Where do national leaders place floral wreaths to honour the martyrs?", "opts": ["Central Shaheed Minar", "National Memorial at Savar (Jatiya Smriti Soudho)", "Suhrawardy Udyan", "National Museum"], "ans": "National Memorial at Savar (Jatiya Smriti Soudho)"},
            {"q": "The word 'fervour' is synonymous with —", "opts": ["Indifference", "Intense passion or zeal", "Coldness", "Hesitation"], "ans": "Intense passion or zeal"}
        ],
        "open_qas": [
            {"q": "What historical event took place on 26 March 1971?", "a": "On 26 March 1971, following the heinous Pakistani military massacre of innocent Bengalis on the dark night of 25 March, Bangladesh's formal declaration of independence was announced, initiating the armed Liberation War."},
            {"q": "What solemn pledge do citizens make on Independence Day at the National Memorial?", "a": "Citizens pledge to uphold the sacred ideals of the 1971 Liberation War—democracy, social justice, secularism, and prosperity—and to dedicate their lives to eliminating poverty and corruption."}
        ],
        "gap_fill": {
            "sentence": "Independence Day is celebrated with great (a) ______ across Bangladesh. The National Memorial at Savar stands as an enduring (b) ______ of our martyrs' supreme sacrifice. People from all walks of life pay (c) ______ to those who died for freedom. This day reminds us of our sacred (d) ______ to protect our nation's (e) ______.",
            "answers": {"a": "fervour / enthusiasm", "b": "symbol / monument", "c": "homage / tribute", "d": "duty / obligation", "e": "freedom / sovereignty"}
        },
        "vocab_notes": "Fervour -> Passionate intensity; Homage -> Respectful tribute; Operation Searchlight -> Military assault."
    },
    {
        "id": 11,
        "slug_id": "seen-11",
        "title": "Pahela Boishakh: The Celebration of Bengali New Year and Cultural Heritage",
        "unit_lesson": "Unit-4, Lesson-6(B)",
        "theme": "Bengali New Year, Mongol Shobhajatra, Chhayanaut & Secular Heritage",
        "stars": "*",
        "priority": "Moderate",
        "boards": "Dakhil Exam-2018, B.B. '23",
        "passage": (
            "Pahela Boishakh is the first day of Bangla calendar, celebrated across the country with traditional festivities and "
            "vibrant cultural splendour. It connects all Bengalis irrespective of their religious or ethnic identity. The day begins "
            "at dawn with musical performances at Ramna Batamul in Dhaka, where the cultural troupe Chhayanaut welcomes the new year "
            "with Rabindranath Tagore's famous invocation 'Esho, he Boishakh'. A hallmark of the festival is the 'Mongol Shobhajatra', "
            "a colorful carnival organized by the faculty of Fine Arts of Dhaka University, inscribed by UNESCO as an Intangible Cultural "
            "Heritage of Humanity. People wear traditional sarees and panjabis, relish panta-ilish, and renew fraternal solidarity."
        ),
        "mcqs": [
            {"q": "How does the cultural troupe Chhayanaut welcome Pahela Boishakh at Ramna Batamul?", "opts": ["With folk dances only", "With Tagore's invocation song 'Esho, he Boishakh'", "With rock music", "With speeches"], "ans": "With Tagore's invocation song 'Esho, he Boishakh'"},
            {"q": "UNESCO declared which event of Pahela Boishakh as an Intangible Cultural Heritage?", "opts": ["Panta-ilish feast", "Mongol Shobhajatra (Peace Procession)", "Kite flying", "Horse race"], "ans": "Mongol Shobhajatra (Peace Procession)"},
            {"q": "The word 'fraternal' pertains to —", "opts": ["Hostility", "Brotherly or mutual communal affection", "Foreign trade", "Religious division"], "ans": "Brotherly or mutual communal affection"}
        ],
        "open_qas": [
            {"q": "Why is Pahela Boishakh regarded as the quintessential secular festival of Bangladesh?", "a": "Pahela Boishakh is a secular festival because it is celebrated by all Bengalis across religious, ethnic, and social strata without dogmatic rituals, symbolizing universal cultural kinship."},
            {"q": "What is the historical significance of Mongol Shobhajatra?", "a": "Originated by art students in the late 1980s to protest autocratic oppression and promote peace, the colorful parade symbolizes hope, secularism, and resistance against bigotry."}
        ],
        "gap_fill": {
            "sentence": "Pahela Boishakh is the biggest (a) ______ festival of Bengali culture. People celebrate the day with joy and (b) ______. The Mongol Shobhajatra organized by Dhaka University students is a vibrant (c) ______ of national unity. Wearing traditional garments, citizens enjoy panta-ilish and pledge to build a (d) ______ society free from (e) ______.",
            "answers": {"a": "secular / cultural", "b": "fervour / enthusiasm", "c": "carnival / reflection", "d": "peaceful / progressive", "e": "communalism / prejudice"}
        },
        "vocab_notes": "Splendour -> Magnificent beauty; Intangible -> Non-physical cultural asset; Kinship -> Blood or cultural bond."
    },
    {
        "id": 12,
        "slug_id": "seen-12",
        "title": "Good Citizens and Moral Awareness: The Foundations of a Civilized Society",
        "unit_lesson": "Unit-5, Lesson-1(B)",
        "theme": "Civic Duties, Moral Values & Responsibilities of a Good Citizen",
        "stars": "*",
        "priority": "Moderate",
        "boards": "Standard Textbook Review",
        "passage": (
            "'Is there anybody here who has ever had to decide between right and wrong?' Ms Choudhury asked her class. The students "
            "nodded thoughtfully. A civilized democratic society cannot function without good citizens who understand their moral and "
            "civic obligations. Being a good citizen is not merely possessing a national identity card or obeying traffic signals; "
            "it requires active empathy, honesty in public life, respect for others' opinions, and safeguarding public property. "
            "Good citizens vote conscientiously, pay lawful taxes, and stand up against injustice and corruption. Education must nurture "
            "these fundamental ethical qualities so that young people grow up to be responsible custodians of the nation's welfare."
        ),
        "mcqs": [
            {"q": "What distinguishes a genuinely good citizen according to the text?", "opts": ["Having wealth", "Active empathy, civic duty, and moral integrity", "Winning awards", "Traveling abroad"], "ans": "Active empathy, civic duty, and moral integrity"},
            {"q": "How do good citizens behave in democratic public life?", "opts": ["They evade taxes", "They vote conscientiously and resist corruption", "They destroy public property", "They ignore laws"], "ans": "They vote conscientiously and resist corruption"},
            {"q": "The word 'custodian' means —", "opts": ["Destroyer", "Guardian or caretaker", "Spectator", "Merchant"], "ans": "Guardian or caretaker"}
        ],
        "open_qas": [
            {"q": "What are the core responsibilities of a good citizen in a democracy?", "a": "A good citizen must abide by state laws, pay taxes honestly, exercise voting rights judiciously, protect public assets, and respect democratic diversity."},
            {"q": "How can schools cultivate civic morality among young learners?", "a": "Schools can cultivate civic morality by promoting group community service, teaching constitutional ethics, and encouraging students to practice honesty and empathy."}
        ],
        "gap_fill": {
            "sentence": "Good citizenship is indispensable for the (a) ______ of any democratic state. An ideal citizen is guided by moral (b) ______ and civic awareness. Paying taxes and obeying state laws are primary (c) ______ of citizens. Moreover, standing against social (d) ______ ensures a just and egalitarian (e) ______.",
            "answers": {"a": "progress / stability", "b": "values / ethics", "c": "responsibilities / duties", "d": "corruption / injustice", "e": "society / country"}
        },
        "vocab_notes": "Conscientiously -> With moral awareness; Custodian -> Keeper/guardian; Egalitarian -> Equal and fair."
    },
    {
        "id": 13,
        "slug_id": "seen-13",
        "title": "Environmental Cleanliness: Waste Disposal and Civic Responsibility",
        "unit_lesson": "Unit-5, Lesson-3(C)",
        "theme": "Urban Cleanliness, Waste Segregation & Civic Consciousness",
        "stars": "*",
        "priority": "Moderate",
        "boards": "Standard Textbook Review",
        "passage": (
            "The class comes up with different ideas on how to keep the neighborhood clean and healthy. Students observe that "
            "improper waste disposal is a pervasive civic problem in cities and rural bazaars alike. Open dumping of polythene bags, "
            "plastic cups, and rotten food waste clogs drainage systems, causing severe waterlogging during the rainy season and "
            "creating breeding grounds for disease-carrying mosquitoes. The students decide to initiate a neighborhood cleanliness "
            "campaign by placing categorized dustbins for biodegradable and non-biodegradable waste. Changing public mindset through "
            "personal example and community engagement is the only sustainable way to build disease-free, beautiful urban environments."
        ),
        "mcqs": [
            {"q": "What is a major consequence of open plastic dumping in urban neighborhoods?", "opts": ["Soil fertility increases", "Clogging of drainage canals and severe waterlogging", "Clean rainwater", "Lower temperatures"], "ans": "Clogging of drainage canals and severe waterlogging"},
            {"q": "What initiative did the students plan to undertake?", "opts": ["Building factories", "A community cleanliness campaign with segregated waste bins", "A music festival", "Buying vehicles"], "ans": "A community cleanliness campaign with segregated waste bins"},
            {"q": "The word 'biodegradable' describes substances that —", "opts": ["Last forever", "Decompose naturally through bacterial action", "Are toxic metals", "Cannot be recycled"], "ans": "Decompose naturally through bacterial action"}
        ],
        "open_qas": [
            {"q": "How does improper waste disposal threaten public health?", "a": "Improper waste disposal clogs waterways, produces foul odors, and creates stagnant breeding grounds for mosquitoes and germs, causing deadly outbreaks of dengue, cholera, and diarrhea."},
            {"q": "Why is waste segregation at source beneficial for recycling?", "a": "Separating biodegradable organic matter from recyclable plastic, glass, and metal prevents contamination, eases composting, and enables efficient recycling processing."}
        ],
        "gap_fill": {
            "sentence": "Maintaining environmental cleanliness is a shared (a) ______ of all citizens. Indiscriminate littering clogs urban drains and causes severe (b) ______. By sorting garbage into biodegradable and non-biodegradable (c) ______, we can facilitate efficient recycling. A cleaner environment ensures better public (d) ______ and aesthetic (e) ______.",
            "answers": {"a": "responsibility / duty", "b": "waterlogging / pollution", "c": "bins / categories", "d": "health / hygiene", "e": "beauty / living"}
        },
        "vocab_notes": "Segregation -> Separation into categories; Biodegradable -> Naturally decomposable; Waterlogging -> Flooding due to blocked drainage."
    },
    {
        "id": 14,
        "slug_id": "seen-14",
        "title": "Youth Volunteering: Carmichael College Students Serving the Community",
        "unit_lesson": "Unit-5, Lesson-4(B)",
        "theme": "Community Service, Youth Leadership & Flood Relief Action",
        "stars": "*",
        "priority": "Moderate",
        "boards": "R.B. '22",
        "passage": (
            "In the next class, Ms Choudhury narrated an inspiring story of a group of proactive students from Carmichael College "
            "in Rangpur. When catastrophic monsoon floods inundated several char villages in the Teesta basin, marooning thousands "
            "of poor families without food and potable water, these spirited youths formed a voluntary disaster response team. They "
            "collected dry food, emergency medicine, and water purification tablets from local residents and distributed them by boats. "
            "Furthermore, they set up temporary sanitation facilities and educated flood victims on preventing waterborne epidemics. "
            "Their selfless dedication proved that youth energy, when channeled constructively, can mitigate human misery in times of crisis."
        ),
        "mcqs": [
            {"q": "What prompted the Carmichael College students to form a volunteer team?", "opts": ["A sports tournament", "Catastrophic monsoon floods marooning char villagers", "College examinations", "A holiday tour"], "ans": "Catastrophic monsoon floods marooning char villagers"},
            {"q": "What essential supplies did the student volunteers distribute to the flood victims?", "opts": ["Books and pens", "Dry food, clean water tablets, and medicine", "Smartphones", "Luxury clothes"], "ans": "Dry food, clean water tablets, and medicine"},
            {"q": "The word 'marooned' means —", "opts": ["Celebrated", "Isolated or stranded without help", "Rescued", "Educated"], "ans": "Isolated or stranded without help"}
        ],
        "open_qas": [
            {"q": "How did the college volunteers demonstrate social responsibility during the natural calamity?", "a": "They collected food, medicine, and water tablets from local donors, navigated boats through flooded terrain to rescue marooned victims, and provided sanitary hygiene instruction."},
            {"q": "What message does this voluntary initiative convey to the youth generation?", "a": "It demonstrates that youth possess immense potential to alleviate human suffering through organized empathy, teamwork, and proactive community service."}
        ],
        "gap_fill": {
            "sentence": "Voluntary community service brings out the best in the (a) ______ generation. When natural disasters like floods strike, students can play an active role in (b) ______ operations. Providing relief goods and clean drinking water prevents (c) ______ outbreaks among victims. Selfless dedication to society builds future moral (d) ______ and compassionate (e) ______.",
            "answers": {"a": "youth / younger", "b": "rescue / relief", "c": "disease / epidemic", "d": "leaders / citizens", "e": "character / humans"}
        },
        "vocab_notes": "Marooned -> Stranded/isolated; Potable -> Safe to drink; Calamity -> Catastrophic disaster."
    },
    {
        "id": 15,
        "slug_id": "seen-15",
        "title": "Emerging Job Markets: Vocational Skills and Future Career Planning",
        "unit_lesson": "Unit-5, Lesson-5(D)",
        "theme": "Career Planning, Technical Skills & 21st-Century Job Market",
        "stars": "**",
        "priority": "High Priority",
        "boards": "C.B. '22",
        "passage": (
            "'Today there are many jobs where you need English and computer skills,' the career counselor explained to the graduating "
            "students. The modern fourth industrial revolution is reshaping the international employment landscape at an unprecedented "
            "speed. Traditional academic rote learning alone is no longer adequate to ensure gainful employment. Employers look for "
            "practical technical proficiencies, problem-solving ability, multilingual communication, and digital competence. Promising "
            "career pathways are opening in software programming, data management, renewable technology, e-commerce logistics, and hospitality. "
            "Youths who invest in technical vocational education and develop adaptive soft skills will thrive in the competitive global economy."
        ),
        "mcqs": [
            {"q": "What additional skills are essential for the modern 21st-century job market?", "opts": ["Memorization of old books", "Computer literacy and English proficiency", "Political influence", "Physical strength only"], "ans": "Computer literacy and English proficiency"},
            {"q": "Why is rote memorization inadequate in contemporary employment?", "opts": ["It takes too much time", "Employers prioritize practical skills, problem-solving, and adaptability", "Schools banned it", "Computers cannot read"], "ans": "Employers prioritize practical skills, problem-solving, and adaptability"},
            {"q": "The word 'proficiency' is synonymous with —", "opts": ["Incompetence", "Expertise or skill", "Laziness", "Confusion"], "ans": "Expertise or skill"}
        ],
        "open_qas": [
            {"q": "How is the fourth industrial revolution changing workplace job requirements?", "a": "It is automating repetitive manual tasks while dramatically increasing demand for digital literacy, data analysis, critical thinking, creative collaboration, and specialized technical vocational skills."},
            {"q": "Why should developing countries invest heavily in vocational training?", "a": "Vocational training equips young populations with market-ready job skills, curbs youth unemployment, fosters entrepreneurship, and attracts foreign direct investment."}
        ],
        "gap_fill": {
            "sentence": "The global job market is undergoing a rapid (a) ______ due to technological advancements. To succeed in modern careers, students must acquire digital (b) ______ and communicative proficiency. Traditional degrees must be supplemented with (c) ______ training and creative problem-solving skills. Youth who adapt to emerging trends will secure bright (d) ______ in the global (e) ______.",
            "answers": {"a": "transformation / change", "b": "literacy / competence", "c": "technical / vocational", "d": "prospects / futures", "e": "economy / market"}
        },
        "vocab_notes": "Proficiency -> High skill; Adaptive -> Flexible to change; Vocational -> Career-focused training."
    },
    {
        "id": 16,
        "slug_id": "seen-16",
        "title": "The Republic of Maldives: An Island Nation in the Indian Ocean",
        "unit_lesson": "Unit-6, Lesson-3(B)",
        "theme": "South Asian Geography, Coral Atolls & Natural Marine Beauty",
        "stars": "**",
        "priority": "High Priority",
        "boards": "Standard Board Review",
        "passage": (
            "The Republic of Maldives is an island nation in the Indian Ocean, situated southwest of India and Sri Lanka. Composed "
            "of a chain of twenty-six natural coral atolls encompassing nearly 1,200 tiny coral islands, only about two hundred of "
            "these are permanently inhabited by humans. The Maldives is celebrated globally for its crystalline turquoise lagoons, "
            "powdery white sand beaches, and vibrant marine biodiversity, making it one of the premier luxury honeymoon and scuba diving "
            "destinations on earth. The country has an ancient seafaring heritage, with Islam serving as the national religion since "
            "the 12th century. The capital city, Malé, is one of the most densely populated urban islands in the world."
        ),
        "mcqs": [
            {"q": "How many coral islands make up the archipelago of the Maldives?", "opts": ["Around 100", "About 1,200 coral islands", "Over 10,000", "Exactly 50"], "ans": "About 1,200 coral islands"},
            {"q": "What makes the Maldives a world-famous tourist destination?", "opts": ["Snow mountains", "Turquoise lagoons, white coral beaches, and scuba diving", "Desert safaris", "Historical forts"], "ans": "Turquoise lagoons, white coral beaches, and scuba diving"},
            {"q": "The term 'atoll' refers to —", "opts": ["A mountain peak", "A ring-shaped coral reef surrounding a lagoon", "A freshwater lake", "A desert dune"], "ans": "A ring-shaped coral reef surrounding a lagoon"}
        ],
        "open_qas": [
            {"q": "What are the key geographical features of the Republic of Maldives?", "a": "The Maldives is an archipelago of twenty-six natural atolls containing approximately 1,200 flat coral islands surrounded by turquoise lagoons, with an average ground elevation of only 1.5 meters above sea level."},
            {"q": "What constitutes the backbone of the Maldivian national economy?", "a": "High-end luxury tourism and commercial tuna fishing form the dual backbones of the Maldivian economy, generating foreign exchange and employment."}
        ],
        "gap_fill": {
            "sentence": "The Maldives is an enchanting archipelago situated in the (a) ______ Ocean. Its pristine turquoise waters and coral reefs attract thousands of global (b) ______ annually. While tourism brings economic prosperity, the low-lying nature of the islands makes the country extremely (c) ______ to rising sea levels. Global environmental cooperation is required to (d) ______ this island (e) ______.",
            "answers": {"a": "Indian", "b": "tourists / visitors", "c": "vulnerable / susceptible", "d": "protect / save", "e": "nation / paradise"}
        },
        "vocab_notes": "Archipelago -> Group of islands; Turquoise -> Greenish-blue; Inhabited -> Populated by residents."
    },
    {
        "id": 17,
        "slug_id": "seen-17",
        "title": "The Maldives: The Looming Ecological Threat of Sea Level Rise",
        "unit_lesson": "Unit-6, Lesson-3(B)",
        "theme": "Climate Change, Sea Level Rise & Existential Threat to Low-Lying Islands",
        "stars": "*",
        "priority": "Moderate",
        "boards": "D.B. '19",
        "passage": (
            "The Maldives is famous as a tourist paradise, but it faces a terrifying environmental existential threat: rising sea levels. "
            "With an average elevation of only 1.5 meters above sea level, it is the lowest-lying nation on the planet. Climate scientists "
            "warn that if global carbon emissions are not drastically curtailed, accelerating polar deglaciation could submerge the entire "
            "archipelago within this century, turning its residents into climate refugees. To dramatize this existential catastrophe to the "
            "world, former Maldivian President Mohamed Nasheed conducted a historic underwater cabinet meeting in 2009, with ministers "
            "signing a climate declaration in scuba gear beneath ocean waves. The nation has also begun building artificial sea-wall islands."
        ),
        "mcqs": [
            {"q": "Why is the Maldives considered the most vulnerable nation to global warming?", "opts": ["It has no trees", "It is the lowest-lying nation with an average elevation of 1.5 meters", "It has active volcanoes", "It suffers from blizzards"], "ans": "It is the lowest-lying nation with an average elevation of 1.5 meters"},
            {"q": "Why did the Maldivian government hold an underwater cabinet meeting in 2009?", "opts": ["For recreation", "To dramatically highlight the threat of sea level rise to global leaders", "To inspect corals", "To shoot a commercial film"], "ans": "To dramatically highlight the threat of sea level rise to global leaders"},
            {"q": "The word 'curtailed' means —", "opts": ["Increased", "Reduced or restricted", "Expanded", "Celebrated"], "ans": "Reduced or restricted"}
        ],
        "open_qas": [
            {"q": "What fate awaits the Maldives if global temperature rise continues unchecked?", "a": "If global warming continues unchecked, rising oceanic sea levels will inundate the low-lying coral islands, rendering the entire country uninhabitable and displacing its population as climate refugees."},
            {"q": "What defensive measures are the Maldivian authorities implementing against sea encroachment?", "a": "The authorities are constructing sea walls, reclaiming land to build fortified artificial islands like Hulhumalé, and advocating internationally for global carbon emission cuts."}
        ],
        "gap_fill": {
            "sentence": "Rising sea level is the greatest environmental (a) ______ confronting the Maldives today. Due to its flat elevation, even a minor rise in ocean waters threatens to (b) ______ coastal homes and contaminate fresh groundwater. The government has taken bold diplomatic initiatives to urge global carbon (c) ______. Without rapid climate action by industrialized powers, this paradise could be lost beneath the (d) ______ forever, causing tragic human (e) ______.",
            "answers": {"a": "threat / danger", "b": "submerge / drown", "c": "reduction / cuts", "d": "waves / ocean", "e": "displacement / catastrophe"}
        },
        "vocab_notes": "Existential -> Threatening existence; Inundate -> Flood/submerge; Curtailed -> Cut short/reduced."
    },
    {
        "id": 18,
        "slug_id": "seen-18",
        "title": "Bhutan: The Land of the Thunder Dragon and Gross National Happiness",
        "unit_lesson": "Unit-6, Lesson-5(A)",
        "theme": "South Asian Culture, Bhutan, Gross National Happiness & Environmental Forest Cover",
        "stars": "*",
        "priority": "Moderate",
        "boards": "Standard Board Review",
        "passage": (
            "Bhutan is called the Jewel of the Eastern Himalayas, a tranquil landlocked kingdom nestled between India and China. "
            "Known natively as 'Druk Yul' (Land of the Thunder Dragon), Bhutan is celebrated for its pristine alpine forests, snow-capped "
            "peaks, and centuries-old Buddhist monasteries (Dzongs). Unlike most nations that measure development strictly by Gross Domestic "
            "Product (GDP), Bhutan pioneered the revolutionary philosophy of 'Gross National Happiness' (GNH). Introduced by the Fourth King "
            "Jigme Singye Wangchuck, GNH measures progress through four pillars: sustainable socio-economic development, cultural preservation, "
            "environmental conservation, and good governance. By constitutional mandate, at least 60 percent of Bhutan's total land area must "
            "remain covered by virgin forests forever."
        ),
        "mcqs": [
            {"q": "What revolutionary development philosophy was formulated by Bhutan?", "opts": ["Gross Domestic Product", "Gross National Happiness (GNH)", "Industrial Capitalism", "Digital Globalization"], "ans": "Gross National Happiness (GNH)"},
            {"q": "What percentage of Bhutan's land is constitutionally protected under forest cover?", "opts": ["At least 25%", "At least 60%", "Exactly 10%", "100%"], "ans": "At least 60%"},
            {"q": "The local name 'Druk Yul' translates to —", "opts": ["Land of the Peaceful Rivers", "Land of the Thunder Dragon", "City of Golden Temples", "Valley of Monks"], "ans": "Land of the Thunder Dragon"}
        ],
        "open_qas": [
            {"q": "How does Gross National Happiness (GNH) differ from traditional economic measures like GDP?", "a": "While GDP measures only material production and financial growth, Gross National Happiness prioritizes psychological well-being, cultural preservation, environmental ecology, and equitable social happiness."},
            {"q": "Why is Bhutan regarded as an environmental role model for the world?", "a": "Bhutan is a carbon-negative nation whose constitution preserves over 60 percent forest cover, absorbing more carbon dioxide than it emits while safeguarding biological conservation."}
        ],
        "gap_fill": {
            "sentence": "Bhutan has earned international admiration for its unique (a) ______ philosophy called Gross National Happiness. Instead of prioritizing mere wealth, it emphasizes spiritual (b) ______ and environmental protection. By preserving vast tracts of lush (c) ______, Bhutan remains carbon negative. Its democratic governance ensures social (d) ______ and cultural (e) ______.",
            "answers": {"a": "development / governing", "b": "well-being / happiness", "c": "forests / greenery", "d": "equity / justice", "e": "preservation / heritage"}
        },
        "vocab_notes": "Pristine -> Pure/unspoiled; Carbon-negative -> Absorbing more carbon than emitting; Dzongs -> Fortified Buddhist monasteries."
    },
    {
        "id": 19,
        "slug_id": "seen-19",
        "title": "Shilpacharya Zainul Abedin: The 1943 Famine Sketches and Cultural Renaissance",
        "unit_lesson": "Unit-7, Lesson-1(B)",
        "theme": "Modern Art, Famine Sketches of 1943 & Folk Art Museum in Sonargaon",
        "stars": "*",
        "priority": "Moderate",
        "boards": "Standard Board Review",
        "passage": (
            "Zainul Abedin was an internationally acclaimed Bangladeshi painter and the founding father of modern art in Bangladesh, "
            "reverently honoured with the title 'Shilpacharya' (Great Teacher of Art). Born on 29 December 1914 in Kishoreganj, he graduated "
            "first class from the Government School of Art in Kolkata. Abedin shot to international fame through his iconic series of "
            "Famine Sketches depicting the tragic Bengal Famine of 1943. Using cheap Chinese ink on packing paper, he captured the "
            "agonizing starvation of dying skeletal mothers, emaciated children, and scavenging crows on Kolkata streets with haunting "
            "realism. In 1948, he established the Government Institute of Arts in Dhaka and later founded the Folk Art Museum in Sonargaon."
        ),
        "mcqs": [
            {"q": "What historical tragedy did Zainul Abedin immortalize in his famous sketches?", "opts": ["The 1971 war", "The Bengal Famine of 1943", "The 1952 Language Movement", "The French Revolution"], "ans": "The Bengal Famine of 1943"},
            {"q": "What materials did Zainul Abedin utilize to draw the Famine Sketches?", "opts": ["Oil paints on canvas", "Cheap Chinese ink and dry brushes on ordinary packing paper", "Watercolours on silk", "Digital tablets"], "ans": "Cheap Chinese ink and dry brushes on ordinary packing paper"},
            {"q": "The honorific title 'Shilpacharya' bestowed upon him signifies —", "opts": ["Leader of soldiers", "Great Master of Arts", "Famous Singer", "Political Ambassador"], "ans": "Great Master of Arts"}
        ],
        "open_qas": [
            {"q": "How did Zainul Abedin's Famine Sketches awaken human conscience worldwide?", "a": "His stark brushstrokes portraying skeletal human beings scavenging beside crows for food exposed the man-made brutality and callous colonial neglect behind the 1943 famine, arousing profound international outrage."},
            {"q": "What lasting institutions did Shilpacharya establish to preserve national art?", "a": "He founded the Government Institute of Arts (now Faculty of Fine Arts, Dhaka University) in 1948 and the Folk Art and Crafts Museum in historical Sonargaon in 1975."}
        ],
        "gap_fill": {
            "sentence": "Shilpacharya Zainul Abedin is the pioneer of modern visual (a) ______ in Bangladesh. His poignant sketches of the 1943 Bengal famine depicted the intense (b) ______ of starving citizens. Rather than pursuing commercial luxury, he used simple ink to portray human (c) ______. Later, he established premier art institutions to promote indigenous folk (d) ______ and cultural (e) ______.",
            "answers": {"a": "arts / painting", "b": "agony / suffering", "c": "dignity / tragedy", "d": "heritage / crafts", "e": "renaissance / identity"}
        },
        "vocab_notes": "Emaciated -> Abnormally thin from starvation; Scavenging -> Searching for discarded food; Callous -> Unfeeling/insensitive."
    },
    {
        "id": 20,
        "slug_id": "seen-20",
        "title": "Traditional Handloom and Nakshi Kantha: The Folk Embroidery of Bengal",
        "unit_lesson": "Unit-7, Lesson-2(B)",
        "theme": "Traditional Crafts, Nakshi Kantha Embroidery & Rural Women's Art",
        "stars": "**",
        "priority": "High Priority",
        "boards": "Standard Board Review",
        "passage": (
            "Culturally rich Bangladesh is celebrated for its centuries-old tradition of handloom weaving and embroidered quilts, "
            "known natively as 'Nakshi Kantha'. The craft involves recycling old cotton sarees and dhotis, layering them with delicate "
            "stitching, and embroidering intricate floral motifs, mythological birds, folk tales, and rural landscape scenes with colored "
            "threads. Traditionally crafted by village women during leisurely monsoon afternoons, each Nakshi Kantha embodies months of "
            "unseen domestic labor, emotional secrets, and creative storytelling. Today, Nakshi Kantha is produced commercially in upscale "
            "handicraft boutiques in Dhaka and exported worldwide as a coveted piece of authentic cultural art, providing dignified economic "
            "livelihoods for thousands of rural artisan women."
        ),
        "mcqs": [
            {"q": "What is Nakshi Kantha?", "opts": ["A modern woolen sweater", "An embroidered quilt made with traditional motifs", "A silk scarf", "A printed curtain"], "ans": "An embroidered quilt made with traditional motifs"},
            {"q": "Who were the traditional creators of Nakshi Kantha in rural Bengal?", "opts": ["Factory workers", "Village women during their domestic leisure", "Royal court painters", "Foreign visitors"], "ans": "Village women during their domestic leisure"},
            {"q": "The word 'intricate' describes designs that are —", "opts": ["Plain and simple", "Complex and detailed", "Colorless", "Broken"], "ans": "Complex and detailed"}
        ],
        "open_qas": [
            {"q": "Why is Nakshi Kantha regarded as both an art piece and an emotional narrative?", "a": "Because village women weave their innermost feelings, joys, sorrows, and folk memories into the intricate embroidered designs, making each quilt a personal testament of rural life."},
            {"q": "How does the commercial revival of Nakshi Kantha benefit rural women today?", "a": "Commercial boutiques and export channels provide rural craftswomen with independent household incomes, financial autonomy, and dignified social empowerment."}
        ],
        "gap_fill": {
            "sentence": "Nakshi Kantha is a splendid manifestation of Bengali folk (a) ______. Created from recycled cloth and coloured threads, it features exquisite (b) ______ of rural folklore and nature. What began as a domestic household craft has now become a valuable (c) ______ commodity. This flourishing industry empowers rural (d) ______ by providing sustainable (e) ______.",
            "answers": {"a": "heritage / craft", "b": "motifs / designs", "c": "commercial / export", "d": "women / artisans", "e": "livelihoods / income"}
        },
        "vocab_notes": "Embroidered -> Decorated with needlework; Motifs -> Recurring artistic themes; Autonomy -> Independence."
    },
    {
        "id": 21,
        "slug_id": "seen-21",
        "title": "Zahir Raihan: Visionary Filmmaker, Language Activist and Liberation Martyr",
        "unit_lesson": "Unit-7, Lesson-3(B)",
        "theme": "Cinema as Resistance, Language Movement & Liberation War Martyrdom",
        "stars": "**",
        "priority": "High Priority",
        "boards": "Ctg. B. '24",
        "passage": (
            "It was late summer, 26 August 1935, when Zahir Raihan was born in Majupur village in Feni. He was one of the "
            "most talented novelists and filmmakers in Bangladesh, deeply involved in national democratic movements. As a valiant "
            "Dhaka University student, he actively joined the historic procession on 21 February 1952 and was imprisoned by the Pakistani "
            "police. His literary masterpiece 'Hajar Bachhar Dhore' won the Adamjee Literature Award. As a filmmaker, his revolutionary "
            "movie 'Jibon Theke Neya' (1970) satirized Pakistani autocracy and popularized the national anthem 'Amar Sonar Bangla'. "
            "During the 1971 Liberation War, his documentary 'Stop Genocide' stirred global human conscience. Tragically, on 30 January 1972, "
            "he disappeared while searching for his abducted brother Shahidullah Kaiser in Mirpur."
        ),
        "mcqs": [
            {"q": "Which film by Zahir Raihan boldly satirized Pakistani military autocracy in 1970?", "opts": ["Kabor", "Jibon Theke Neya", "Aguner Poroshmoni", "Matir Moyna"], "ans": "Jibon Theke Neya"},
            {"q": "What was the purpose of Zahir Raihan's documentary 'Stop Genocide' in 1971?", "opts": ["To entertain refugees", "To arouse global conscience against Pakistani massacres", "To advertise films", "To train freedom fighters"], "ans": "To arouse global conscience against Pakistani massacres"},
            {"q": "When did Zahir Raihan tragically disappear in Mirpur?", "opts": ["21 February 1952", "26 March 1971", "30 January 1972", "16 December 1971"], "ans": "30 January 1972"}
        ],
        "open_qas": [
            {"q": "How did Zahir Raihan utilize the medium of cinema for the Bengali national struggle?", "a": "Zahir Raihan transformed cinema into a potent weapon of political awakening and resistance, portraying autocratic tyranny symbolically in 'Jibon Theke Neya' and documenting the brutal 1971 atrocities internationally in 'Stop Genocide'."},
            {"q": "What tragedy befell Zahir Raihan shortly after national liberation?", "a": "On 30 January 1972, just weeks after victory, he went to Mirpur to locate his abducted elder brother, writer Shahidullah Kaiser, and was killed by Pakistani collaborators and armed soldiers."}
        ],
        "gap_fill": {
            "sentence": "Zahir Raihan was an extraordinary (a) ______ and cinematic visionary in Bangladesh. He bravely participated in the 1952 (b) ______ Movement. His celebrated film 'Jibon Theke Neya' depicted the political (c) ______ against dictatorship. During 1971, his documentary 'Stop Genocide' alerted the (d) ______ community about Pakistani atrocities. His supreme sacrifice remains an immortal (e) ______ of cultural heroism.",
            "answers": {"a": "novelist / filmmaker", "b": "Language", "c": "struggle / resistance", "d": "international / global", "e": "inspiration / beacon"}
        },
        "vocab_notes": "Satirized -> Mocked critically; Genocide -> Systematic extermination of people; Conscience -> Moral sense of right and wrong."
    },
    {
        "id": 22,
        "slug_id": "seen-22",
        "title": "Mother Teresa: Apostle of the Dying Destitute and Angel of Mercy",
        "unit_lesson": "Unit-7, Lesson-5(A)",
        "theme": "Selfless Philanthropy, Nirmal Hriday & Nobel Peace Prize (1979)",
        "stars": "**",
        "priority": "High Priority",
        "boards": "R.B. '20, M.B. '22, Ctg.B. '23",
        "passage": (
            "Mother Teresa was deeply moved by the sight of the sick and dying on the streets of Kolkata. Born Anjezë Gonxhe Bojaxhiu "
            "on 26 August 1910 in Skopje, North Macedonia, she arrived in India in 1929 as a Loreto nun. In 1950, answering what she "
            "described as a 'call within a call', she founded the Missionaries of Charity to serve the poorest of the poor—the abandoned, "
            "lepers, orphaned infants, and dying destitute. In 1952, she established 'Nirmal Hriday' (Pure Heart) in Kalighat, Kolkata, "
            "providing dying individuals a dignified place to expire surrounded by genuine human love and spiritual care. In 1979, "
            "she was awarded the Nobel Peace Prize, utilizing all prize monies to build shelters for the destitute. She died on 5 September 1997."
        ),
        "mcqs": [
            {"q": "What organization did Mother Teresa establish in Kolkata in 1950?", "opts": ["Red Cross", "Missionaries of Charity", "Salvation Army", "Amnesty International"], "ans": "Missionaries of Charity"},
            {"q": "Why was 'Nirmal Hriday' established by Mother Teresa?", "opts": ["As a luxury hotel", "To offer dying destitute street persons a dignified, loving haven", "As an art gallery", "For research"], "ans": "To offer dying destitute street persons a dignified, loving haven"},
            {"q": "Mother Teresa was conferred the Nobel Peace Prize in the year —", "opts": ["1950", "1971", "1979", "1997"], "ans": "1979"}
        ],
        "open_qas": [
            {"q": "What prompted Mother Teresa to leave the Loreto Convent and work on the streets of Kolkata?", "a": "She felt a powerful divine calling to leave the comfortable convent walls and dedicate her entire life to nursing the abandoned, sick, and dying destitute living in extreme squalor on the streets of Kolkata."},
            {"q": "How did Mother Teresa utilize the financial purse of her 1979 Nobel Peace Prize?", "a": "True to her lifelong vow of poverty and service, she declined the ceremonial banquet and directed every cent of the financial award into constructing homes and clinics for the destitute, disabled, and lepers."}
        ],
        "gap_fill": {
            "sentence": "Mother Teresa is universally revered as an apostle of selfless (a) ______. Arriving in India as a young nun, she dedicated her life to the (b) ______ of the poor. Through Nirmal Hriday, she gave abandoned dying persons a (c) ______ shelter. Her monumental humanitarian work was recognized with the Nobel (d) ______ Prize in 1979. Her legacy inspires the world to serve suffering (e) ______.",
            "answers": {"a": "compassion / love", "b": "poorest / destitute", "c": "dignified / loving", "d": "Peace", "e": "humanity / mankind"}
        },
        "vocab_notes": "Destitute -> Utterly impoverished; Humanitarian -> Compassionate toward human suffering; Squalor -> Filthy and wretched condition."
    },
    {
        "id": 23,
        "slug_id": "seen-23",
        "title": "Steve Jobs: Digital Pioneer and Co-Founder of the Personal Computer Era",
        "unit_lesson": "Unit-7, Lesson-6(B)",
        "theme": "Technological Innovation, Apple Inc., iPhone & Creative Design",
        "stars": "*",
        "priority": "Moderate",
        "boards": "Standard Board Review",
        "passage": (
            "Steven Paul Jobs (24 February 1955 – 5 October 2011) was an iconic American business magnate, industrial designer, "
            "and visionary investor widely recognized as the pioneer of the microcomputer revolution. In 1976, Jobs co-founded Apple Computer "
            "with Steve Wozniak in his family garage, launching the Apple II and later the revolutionary Macintosh in 1984, which "
            "popularized the graphical user interface. Although ousted from Apple in 1985, Jobs founded NeXT and acquired Pixar Animation "
            "Studios, producing the world's first computer-animated feature film 'Toy Story'. Returning to Apple in 1997, Jobs revolutionized "
            "multiple industries sequentially: music with the iPod, telecommunications with the iPhone, and computing with the iPad."
        ),
        "mcqs": [
            {"q": "Where did Steve Jobs and Steve Wozniak co-found Apple Computer in 1976?", "opts": ["At Harvard University", "In Steve Jobs' parents' garage", "In New York", "At Microsoft"], "ans": "In Steve Jobs' parents' garage"},
            {"q": "Which product introduced the first widely successful graphical user interface (GUI) to consumers in 1984?", "opts": ["Apple Watch", "Macintosh computer", "IBM PC", "GameBoy"], "ans": "Macintosh computer"},
            {"q": "The word 'visionary' denotes a person who —", "opts": ["Cannot see well", "Has powerful foresight and innovative ideas for the future", "Only looks backwards", "Is wealthy"], "ans": "Has powerful foresight and innovative ideas for the future"}
        ],
        "open_qas": [
            {"q": "How did Steve Jobs transform multiple consumer electronics industries upon returning to Apple in 1997?", "a": "Jobs introduced elegantly designed, user-friendly digital devices: the iPod disrupted the global music market, the iPhone reinvented mobile telecommunications, and the iPad created the modern tablet computing era."},
            {"q": "What creative studio did Steve Jobs build into a global animation powerhouse during his hiatus from Apple?", "a": "Jobs financed and developed Pixar Animation Studios, which created the groundbreaking computer-animated film 'Toy Story' and revolutionized global cinema."}
        ],
        "gap_fill": {
            "sentence": "Steve Jobs is celebrated as a digital (a) ______ who reshaped modern technology. From his humble garage start, he built Apple into a global (b) ______. His obsession with exquisite design and intuitive user experience led to the (c) ______ of the iPhone and iPad. He believed that technology married with the liberal arts produces truly (d) ______ results for (e) ______.",
            "answers": {"a": "visionary / pioneer", "b": "giant / enterprise", "c": "invention / launch", "d": "revolutionary / inspiring", "e": "humanity / society"}
        },
        "vocab_notes": "Magnate -> Wealthy influential tycoon; Intuitive -> Easily understood without instruction; Disrupted -> Radically altered."
    },
    {
        "id": 24,
        "slug_id": "seen-24",
        "title": "Shat Gombuj Mosque in Bagerhat: The Architectural Grandeur of Khan Jahan Ali",
        "unit_lesson": "Unit-8, Lesson-1(B)",
        "theme": "World Heritage, Medieval Bengal Architecture & Khan Jahan Ali",
        "stars": "***",
        "priority": "Top Priority (Most Probable)",
        "boards": "Dakhil Exam-2020; M.B., J.B., C.B. '24",
        "passage": (
            "'Heritage' is what we inherit from the past, live with in the present, and then pass on to our children or future "
            "generations. Our unique source of life and inspiration is our cultural and natural heritage. The historic city of Bagerhat, "
            "originally known as Khalifatabad, was founded in the 15th century by the saint-warrior Ulugh Khan Jahan Ali. The most "
            "magnificent architectural marvel of this medieval brick city is the sixty-domed Shat Gombuj Mosque. Despite its colloquial "
            "name 'Shat Gombuj' (sixty domes), the mosque actually possesses seventy-seven low-profile domes over the central prayer hall, "
            "along with four corner towers topped by smaller domes, making eighty-one domes in total. In 1985, UNESCO declared Bagerhat "
            "and the Shat Gombuj Mosque a World Heritage Site."
        ),
        "mcqs": [
            {"q": "How many actual domes does the Shat Gombuj Mosque possess in total including corner towers?", "opts": ["Exactly 60", "77 on the roof and 4 on corner towers (total 81)", "100 domes", "Only 4"], "ans": "77 on the roof and 4 on corner towers (total 81)"},
            {"q": "Who was the medieval saint-warrior who founded the historic city of Khalifatabad (Bagerhat)?", "opts": ["Shah Jahan", "Ulugh Khan Jahan Ali", "Islam Khan", "Shamsuddin Ilyas Shah"], "ans": "Ulugh Khan Jahan Ali"},
            {"q": "In which year was the Shat Gombuj Mosque inscribed on the UNESCO World Heritage list?", "opts": ["1952", "1971", "1985", "1999"], "ans": "1985"}
        ],
        "open_qas": [
            {"q": "Why is the mosque named 'Shat Gombuj' when it actually has eighty-one domes?", "a": "Scholars believe the name derives from 'Shat Khumbaz' meaning sixty pillars, referring to the sixty slender stone columns supporting the roof, which colloquially evolved into 'Shat Gombuj' over centuries."},
            {"q": "What engineering feats distinguish Khan Jahan Ali's medieval brick city in Bagerhat?", "a": "Khan Jahan Ali constructed advanced urban drainage canals, excavated large freshwater reservoirs (dighis), laid paved roads, and built dozens of resilient burnt-brick Islamic monuments in harsh mangrove terrain."}
        ],
        "gap_fill": {
            "sentence": "The Shat Gombuj Mosque is an extraordinary medieval (a) ______ of Bangladesh. Built in the fifteenth century by Ulugh Khan Jahan, it features sixty stone pillars supporting eighty-one (b) ______. The monument reflects the grandeur of Islamic brick (c) ______ in the mangrove delta. Recognizing its universal value, UNESCO declared it a World (d) ______ Site to ensure its international (e) ______.",
            "answers": {"a": "monument / marvel", "b": "domes", "c": "architecture", "d": "Heritage", "e": "preservation / conservation"}
        },
        "vocab_notes": "Colloquial -> Informal spoken language; Inscribed -> Officially cataloged; Reservoir -> Large water storage body."
    },
    {
        "id": 25,
        "slug_id": "seen-25",
        "title": "Somapura Mahavihara at Paharpur: Ancient Center of Buddhist Learning",
        "unit_lesson": "Unit-8, Lesson-2(A)",
        "theme": "Archaeological Heritage, Pala Dynasty & Buddhist Vihara at Paharpur",
        "stars": "*",
        "priority": "Moderate",
        "boards": "Standard Board Review",
        "passage": (
            "Paharpur is an exceptionally important archaeological site situated in Badalgachhi upazila of Naogaon district. "
            "It houses the majestic Somapura Mahavihara, which was built in the late eighth century CE by the second Pala emperor, "
            "King Dharmapala. Covering an expansive quadrangular area of twenty-seven acres, it was once the largest Buddhist monastery "
            "south of the Himalayas, functioning as a renowned international center of philosophical scholarship for monks from across "
            "India, Tibet, China, and Southeast Asia. The complex consists of 177 monastic residential cells surrounding a towering cruciform "
            "central shrine adorned with thousands of terracotta relief plaques depicting folk life, flora, and fauna. UNESCO designated "
            "Paharpur a World Heritage Site in 1985."
        ),
        "mcqs": [
            {"q": "Which Pala monarch commissioned the construction of Somapura Mahavihara at Paharpur?", "opts": ["King Gopala", "King Dharmapala", "King Devapala", "King Mahipala"], "ans": "King Dharmapala"},
            {"q": "How many monastic residential cells surround the central shrine at Paharpur?", "opts": ["60 cells", "100 cells", "177 monastic cells", "300 cells"], "ans": "177 monastic cells"},
            {"q": "What artistic adornment decorates the outer basement walls of the Paharpur monument?", "opts": ["Gold foil", "Terracotta clay relief plaques", "Glass mosaics", "Marble statues"], "ans": "Terracotta clay relief plaques"}
        ],
        "open_qas": [
            {"q": "What was the historical function of Somapura Mahavihara during the Pala Empire?", "a": "It served as a premier residential university and monastic academy where Buddhist scholars, philosophers, and spiritual monks from across Asia resided, translated scriptures, and studied higher theology."},
            {"q": "What do the terracotta plaques at Paharpur reveal about ancient Bengal?", "a": "The terracotta plaques provide vivid, realistic depictions of ancient daily life in Bengal—displaying musicians, warriors, village farmers, dancers, animals, and mythological figures."}
        ],
        "gap_fill": {
            "sentence": "Somapura Mahavihara at Paharpur is an ancient architectural (a) ______ of Bengal. Established by King Dharmapala in the eighth century, it flourished as a global (b) ______ of Buddhist learning. The monastery accommodated hundreds of scholars in its 177 (c) ______. The walls are exquisitely decorated with terracotta (d) ______, making it a UNESCO World (e) ______ Site.",
            "answers": {"a": "wonder / treasure", "b": "center / academy", "c": "cells / rooms", "d": "plaques / carvings", "e": "Heritage"}
        },
        "vocab_notes": "Quadrangular -> Four-sided square; Terracotta -> Baked reddish clay; Monastic -> Pertaining to monks."
    },
    {
        "id": 26,
        "slug_id": "seen-26",
        "title": "The Statue of Liberty: France's Gift of Freedom and Hope to the World",
        "unit_lesson": "Unit-8, Lesson-3(D)",
        "theme": "Universal Liberty, French Sculptor Bartholdi & New York Harbour",
        "stars": "*",
        "priority": "Moderate",
        "boards": "Standard Board Review",
        "passage": (
            "The French sculptor Frédéric-Auguste Bartholdi designed the world's most famous symbol of freedom—the Statue of "
            "Liberty, officially named 'Liberty Enlightening the World'. Given as a gift of friendship from the people of France to "
            "the United States in 1886 to commemorate the centennial of the US Declaration of Independence and the abolition of slavery, "
            "the colossal copper statue stands proudly on Liberty Island in New York Harbour. The statue depicts Libertas, the Roman goddess "
            "of freedom, holding a blazing torch of enlightenment in her right hand and a tabula ansata inscribed with 'JULY IV MDCCLXXVI' "
            "in her left. Broken shackles lie at her feet, symbolizing emancipation from tyranny. For millions of immigrants arriving by "
            "sea, she represented hope and sanctuary."
        ),
        "mcqs": [
            {"q": "Who designed the monumental copper Statue of Liberty?", "opts": ["Gustave Eiffel alone", "Frédéric-Auguste Bartholdi", "Leonardo da Vinci", "Pablo Picasso"], "ans": "Frédéric-Auguste Bartholdi"},
            {"q": "What do the broken shackles and chains at the feet of the statue symbolize?", "opts": ["A defeated prisoner", "Emancipation from tyranny and the abolition of slavery", "War victory", "Ship anchors"], "ans": "Emancipation from tyranny and the abolition of slavery"},
            {"q": "The official historical designation of the Statue of Liberty is —", "opts": ["The American Freedom", "Liberty Enlightening the World", "Goddess of Hope", "The French Beacon"], "ans": "Liberty Enlightening the World"}
        ],
        "open_qas": [
            {"q": "Why did France present the Statue of Liberty to the United States in the late nineteenth century?", "a": "France presented the statue to celebrate the centennial of the 1776 American Declaration of Independence, honor the abolition of slavery, and commemorate the enduring democratic alliance between both nations."},
            {"q": "What emotional significance did the Statue of Liberty hold for arriving immigrants?", "a": "For millions of impoverished immigrants crossing the Atlantic by steamship, the colossal torch of Liberty in New York Harbour was the first vision of the New World, symbolizing freedom from oppression and the promise of a new life."}
        ],
        "gap_fill": {
            "sentence": "The Statue of Liberty is a universally recognized (a) ______ of freedom and democracy. Designed by the French sculptor Bartholdi, it was dedicated in (b) ______ in New York Harbour. The torch held high symbolizes the light of (c) ______, while broken chains at her feet represent liberation from (d) ______. For generations of immigrants, she offered a beacon of (e) ______.",
            "answers": {"a": "symbol / icon", "b": "1886", "c": "liberty / enlightenment", "d": "tyranny / slavery", "e": "hope / refuge"}
        },
        "vocab_notes": "Colossal -> Immensely gigantic; Shackles -> Metal chains/fetters; Emancipation -> Liberation from bondage."
    },
    {
        "id": 27,
        "slug_id": "seen-27",
        "title": "Pritilata Waddedar: Revolutionary Martyr of the Anti-British Movement",
        "unit_lesson": "Unit-10, Lesson-3(B)",
        "theme": "Anti-Colonial Struggle, Chittagong Armory Raid & Martyrdom",
        "stars": "**",
        "priority": "High Priority",
        "boards": "Standard Board Review",
        "passage": (
            "Pritilata Waddedar was born in Chittagong on 5 May 1911 into a progressive family. A brilliant student throughout her "
            "academic life, she graduated with distinction in philosophy from Bethune College in Kolkata and became the headmistress of "
            "Nandankanan Aparnacharan School in Chittagong. Deeply anguished by oppressive British colonial rule, she joined the armed "
            "resistance movement under the legendary revolutionary leader Masterda Surya Sen. In September 1932, Surya Sen assigned her "
            "to lead an armed raid on the notorious Pahartali European Club, which displayed the insulting sign: 'Dogs and Indians not allowed.' "
            "Disguised as a Punjabi man, Pritilata led a successful raid on 23 September 1932. Wounded by a bullet and refusing to be captured "
            "alive, she bravely swallowed potassium cyanide, achieving immortal martyrdom at age twenty-one."
        ),
        "mcqs": [
            {"q": "Under whose leadership did Pritilata Waddedar join the anti-British armed revolution?", "opts": ["Mahatma Gandhi", "Masterda Surya Sen", "Netaji Subhas Bose", "Rabindranath Tagore"], "ans": "Masterda Surya Sen"},
            {"q": "What offensive sign hung outside the Pahartali European Club in Chittagong?", "opts": ["'Reserved for Officers'", "'Dogs and Indians not allowed'", "'Private Club'", "'Members Only'"], "ans": "'Dogs and Indians not allowed'"},
            {"q": "How did Pritilata Waddedar embrace martyrdom to prevent British arrest?", "opts": ["She jumped into the sea", "She swallowed potassium cyanide poison", "She escaped to Burma", "She starved in jail"], "ans": "She swallowed potassium cyanide poison"}
        ],
        "open_qas": [
            {"q": "Why was the Pahartali European Club selected as a target for revolutionary assault?", "a": "The club was a hateful symbol of British racial supremacy and colonial humiliation, notoriously displaying the signboard 'Dogs and Indians not allowed,' which deeply enraged the revolutionary freedom fighters."},
            {"q": "What did Pritilata's supreme martyrdom prove regarding female participation in armed struggles?", "a": "Her fearless leadership shattered traditional gender stereotypes, conclusively proving that women could command military operations and make supreme sacrifices alongside men for national liberation."}
        ],
        "gap_fill": {
            "sentence": "Pritilata Waddedar is an immortal icon of anti-colonial (a) ______ in Bengal. Joining Masterda Surya Sen's revolutionary movement, she fought with extraordinary (b) ______. In 1932, she led a successful armed raid against the racist (c) ______ Club. To avoid falling into enemy hands, she chose martyrdom by consuming (d) ______. Her heroic sacrifice continues to inspire patriotic (e) ______.",
            "answers": {"a": "resistance / struggle", "b": "courage / bravery", "c": "European", "d": "poison / cyanide", "e": "youth / generations"}
        },
        "vocab_notes": "Martyrdom -> Willful death for a noble cause; Insulting -> Humiliating/derogatory; Disguised -> Camouflaged in appearance."
    },
    {
        "id": 28,
        "slug_id": "seen-28",
        "title": "Eid-ul-Fitr: The Joyous Festival of Fraternity and the Homebound Journey",
        "unit_lesson": "Unit-12, Lesson-1(B)",
        "theme": "Islamic Religious Festival, Homebound Travel Rush & Communal Harmony",
        "stars": "***",
        "priority": "Top Priority (Most Probable)",
        "boards": "Dakhil Exam. '25, M.B. '23, '26; D.B. '23",
        "passage": (
            "Eid is the main religious festival of the Muslims in Bangladesh. Eid means happiness. Everyone wants to share this "
            "boundless happiness with their near and dear ones. Following a month of disciplined fasting during holy Ramadan, Eid-ul-Fitr "
            "arrives with joyful festivities and profound spiritual renewal. However, for urban dwellers in metropolitan cities like Dhaka, "
            "Eid also brings the frantic rush of homebound travel. Millions of people brave overcrowded buses, jam-packed trains, and "
            "hazardous launches, enduring hours of traffic gridlock just to spend Eid morning in their ancestral villages. This overwhelming "
            "urge to return is not mere social custom; it is an irresistible pull of the roots, reconnecting individuals to the soil, "
            "childhood memories, and parental blessings."
        ),
        "mcqs": [
            {"q": "What is the primary spiritual significance of Eid-ul-Fitr for Muslims?", "opts": ["Commercial shopping", "Sharing happiness, mutual fraternity, and spiritual renewal after Ramadan", "Buying new vehicles", "Foreign travel"], "ans": "Sharing happiness, mutual fraternity, and spiritual renewal after Ramadan"},
            {"q": "Why do millions of city dwellers endure grueling travel hardships before Eid?", "opts": ["To avoid office duties", "Because of the deep, irresistible desire to return to their ancestral roots and family", "To attend examinations", "For sight-seeing"], "ans": "Because of the deep, irresistible desire to return to their ancestral roots and family"},
            {"q": "The phrase 'pull of the roots' figuratively refers to —", "opts": ["Pulling tree branches", "The deep emotional attachment to one's birthplace and heritage", "Farming agriculture", "Tension in soil"], "ans": "The deep emotional attachment to one's birthplace and heritage"}
        ],
        "open_qas": [
            {"q": "Why do people overlook extreme transport hazards to journey home during Eid?", "a": "People endure dangerous travel conditions because the emotional yearning to reunite with parents, relatives, and rural roots outweighs any physical discomfort or financial expenditure."},
            {"q": "How does Eid-ul-Fitr foster social egalitarianism in society?", "a": "Through the payment of Fitra and Zakat, wealthy citizens share resources with the impoverished, while collective Eid prayers in open fields allow people of all ranks to embrace as equals."}
        ],
        "gap_fill": {
            "sentence": "Eid-ul-Fitr is celebrated with immense religious (a) ______ throughout Bangladesh. After the month-long Ramadan fast, people rejoice in the spirit of mutual (b) ______. The festive period witnesses a massive homeward (c) ______ from urban centers to villages. This journey illustrates human longing to stay connected to one's ancestral (d) ______ and family (e) ______.",
            "answers": {"a": "fervour / enthusiasm", "b": "fraternity / brotherhood", "c": "rush / journey", "d": "roots / homeland", "e": "ties / blessings"}
        },
        "vocab_notes": "Frantic -> Wild with excitement or fear; Gridlock -> Total traffic stoppage; Ancestral -> Inherited from forefathers."
    },
    {
        "id": 29,
        "slug_id": "seen-29",
        "title": "Mainul Islam: The Educated Youth Redefining Agriculture as a Noble Career",
        "unit_lesson": "Unit-12, Lesson-2(D)",
        "theme": "Educated Agriculture, Agrarian Roots & Modern Farming Dignity",
        "stars": "***",
        "priority": "Top Priority (Most Probable)",
        "boards": "SSC All Boards '18, C.B. '23",
        "passage": (
            "Mainul Islam is a qualified farmer living in a village in Bogura. His elder brother is a physician, and his younger "
            "brother is an engineer working in an urban corporation. When asked why he did not pursue an urban white-collar job despite "
            "earning an advanced degree from Bangladesh Agricultural University, Mainul replied with calm conviction: 'A doctor saves "
            "lives, an engineer builds roads, but a farmer feeds the entire nation. Why should an educated person feel ashamed to till "
            "the soil?' Mainul revolutionized his ancestral farmland by adopting modern organic composting, drip irrigation, and high-yield "
            "horticulture. He has become a wealthy agri-entrepreneur and trained dozens of unemployed youths, demonstrating that rootedness "
            "in one's soil is a source of immense pride and prosperity."
        ),
        "mcqs": [
            {"q": "From which educational institution did Mainul Islam earn his graduation degree?", "opts": ["Dhaka University", "Bangladesh Agricultural University (BAU)", "BUET", "Chittagong Medical College"], "ans": "Bangladesh Agricultural University (BAU)"},
            {"q": "What core philosophy did Mainul Islam express regarding the farming profession?", "opts": ["Farming is for uneducated people", "Farmers feed the nation, so agriculture is a deeply noble and vital profession", "Farming is unprofitable", "He regrets not leaving the village"], "ans": "Farmers feed the nation, so agriculture is a deeply noble and vital profession"},
            {"q": "The word 'conviction' in the passage means —", "opts": ["Doubt", "Firm and steadfast belief", "Hesitation", "Criminal sentence"], "ans": "Firm and steadfast belief"}
        ],
        "open_qas": [
            {"q": "Why did Mainul Islam choose agricultural farming over an urban corporate career?", "a": "Mainul chose farming because he firmly believed that producing food to nourish the nation is just as noble as medicine or engineering, and he desired to modernize his ancestral soil with scientific innovation."},
            {"q": "How did Mainul's scientific farming transform his local rural economy?", "a": "By introducing organic composting, water-saving drip irrigation, and commercial horticulture, he generated substantial profits and provided employment and modern agricultural training to rural youth."}
        ],
        "gap_fill": {
            "sentence": "Mainul Islam is an inspiring role model for the educated (a) ______ of Bangladesh. Instead of chasing urban desk jobs, he utilized his agricultural degree to modernize (b) ______ farming. He proved that agriculture is not an inferior job, but the very lifeline that (c) ______ the nation. His success encourages university graduates to become agri-(d) ______ and contribute to rural (e) ______.",
            "answers": {"a": "youth / generation", "b": "ancestral / modern", "c": "feeds / sustains", "d": "entrepreneurs", "e": "development / economy"}
        },
        "vocab_notes": "Conviction -> Firm belief; Agri-entrepreneur -> Agricultural business innovator; Rootedness -> Connection to origin/soil."
    },
    {
        "id": 30,
        "slug_id": "seen-30",
        "title": "Michael Madhusudan Dutt: The Pioneer of Modern Bengali Blank Verse",
        "unit_lesson": "Unit-12, Lesson-3(A)",
        "theme": "Bengali Renaissance, Michael Madhusudan Dutt & Western Literary Fusion",
        "stars": "**",
        "priority": "High Priority",
        "boards": "Dinj.B. '23, M.B. '24",
        "passage": (
            "Michael Madhusudan Dutt was a legendary nineteenth-century Bengali poet and dramatist who revolutionized Bengali "
            "literature by liberating it from rigid medieval conventions. Born on 25 January 1824 at Sagardari along the Kopotakkho River "
            "in Jessore, he developed an intense fascination for Western European literature during his education at Hindu College, Kolkata. "
            "Yearning to be recognized as a great English poet, he converted to Christianity in 1843 and migrated to England and France. "
            "However, his English works met with lukewarm reception. Realizing his poetic destiny lay in his native language, he returned "
            "to Bengali and composed the monumental epic 'Meghnad Badh Kavya', introducing blank verse (Amitrakshar Chhanda) and the Petrarchan "
            "sonnet. His famous sonnet 'Kopotakkho Nod' immortalized his nostalgic love for his motherland."
        ),
        "mcqs": [
            {"q": "Which revolutionary poetic technique did Michael Madhusudan Dutt introduce into Bengali poetry?", "opts": ["Folk rhyme", "Blank verse (Amitrakshar Chhanda) and Sonnet", "Haiku", "Limerick"], "ans": "Blank verse (Amitrakshar Chhanda) and Sonnet"},
            {"q": "What is universally considered Madhusudan Dutt's greatest Bengali epic masterpiece?", "opts": ["The Captive Ladie", "Meghnad Badh Kavya", "Sarmistha", "Padmavati"], "ans": "Meghnad Badh Kavya"},
            {"q": "Along which river was the poet born in Sagardari?", "opts": ["Padma", "Buriganga", "Kopotakkho River", "Meghna"], "ans": "Kopotakkho River"}
        ],
        "open_qas": [
            {"q": "Why did Madhusudan Dutt initially reject his native language and compose in English?", "a": "Enamored by European romantic poets like Byron and Milton, he mistakenly believed that writing in English was the only way to attain international fame and western literary acclaim."},
            {"q": "How did the poet express his deep nostalgia in the sonnet 'Kopotakkho Nod'?", "a": "Exiled in poverty in Versailles, France, he remembered the sweet maternal waters of the Kopotakkho river with deep emotional anguish, declaring that no foreign river could quench his thirsty heart."}
        ],
        "gap_fill": {
            "sentence": "Michael Madhusudan Dutt is celebrated as the pioneer of modern (a) ______ literature. After early disappointments in writing English verse in Europe, he realized that true glory lay in his (b) ______ tongue. His epic Meghnad Badh Kavya introduced revolutionary (c) ______ verse. His poignant sonnets reflect deep love for the Kopotakkho River and his native (d) ______, cementing his immortal (e) ______.",
            "answers": {"a": "Bengali", "b": "mother / native", "c": "blank / unrhymed", "d": "motherland", "e": "legacy / fame"}
        },
        "vocab_notes": "Blank Verse -> Unrhymed iambic verse; Nostalgia -> Longing for the past; Enamored -> Charmed or captivated."
    },
    {
        "id": 31,
        "slug_id": "seen-31",
        "title": "Science and Technology: Catalysts for Human Welfare and National Progress",
        "unit_lesson": "Unit-14, Lesson-1(B)",
        "theme": "Science for Humanity, Indian Science Congress & Technological Ethics",
        "stars": "*",
        "priority": "Moderate",
        "boards": "Standard Board Review",
        "passage": (
            "In a historic speech at the 90th Indian Science Congress, scientists and thinkers addressed the moral imperative of "
            "orienting scientific innovation toward grassroots human welfare. Science and technology have transformed human civilization "
            "by eliminating deadly epidemics through vaccines, multiplying agricultural yields through the Green Revolution, and shrinking "
            "global distances via instant digital telecommunication. However, speakers cautioned that technological advancement without "
            "ethical responsibility poses severe perils, including biological warfare, environmental despoliation, and artificial intelligence "
            "inequities. The primary objective of scientific enterprise in the twenty-first century must be poverty eradication, accessible "
            "renewable energy, clean potable water, and climate resilience for vulnerable global populations."
        ),
        "mcqs": [
            {"q": "What must guide technological advancement according to the 90th Science Congress?", "opts": ["Commercial profits only", "Ethical responsibility and human welfare", "Military expansion", "Space tourism"], "ans": "Ethical responsibility and human welfare"},
            {"q": "How did science revolutionize agricultural production in the twentieth century?", "opts": ["By banning machines", "Through the Green Revolution and high-yield hybrid crops", "By cutting forests", "By stopping irrigation"], "ans": "Through the Green Revolution and high-yield hybrid crops"},
            {"q": "The word 'despoliation' refers to —", "opts": ["Beautification", "Plundering or destructive degradation", "Conservation", "Planting"], "ans": "Plundering or destructive degradation"}
        ],
        "open_qas": [
            {"q": "What dual nature does scientific and technological power possess?", "a": "Science is a double-edged sword: while it has the power to cure diseases, eradicate famine, and connect humanity, irresponsible or unethical use can cause environmental catastrophe and warfare."},
            {"q": "How should developing nations utilize science for socio-economic progress?", "a": "Developing nations should harness biotechnology for climate-resilient crops, adopt telemedicine for rural clinics, implement solar energy, and train youth in software engineering."}
        ],
        "gap_fill": {
            "sentence": "Science and technology have brought about miraculous (a) ______ in human lifestyle. Inventions in medicine and communication have made our existence far more (b) ______. However, the indiscriminate exploitation of natural resources has triggered severe environmental (c) ______. Scientists must dedicate their genius to sustainable (d) ______ that ensures universal human (e) ______.",
            "answers": {"a": "changes / transformations", "b": "comfortable / convenient", "c": "degradation / crises", "d": "development", "e": "welfare / survival"}
        },
        "vocab_notes": "Despoliation -> Severe damage/plundering; Double-edged sword -> Capable of both good and harm; Grassroots -> Ordinary common people."
    },
    {
        "id": 32,
        "slug_id": "seen-32",
        "title": "Renewable Energy: The Transition to Solar, Wind and Hydroelectric Power",
        "unit_lesson": "Unit-14, Lesson-2(B)",
        "theme": "Energy Crisis, Depleting Fossil Fuels & Renewable Green Solutions",
        "stars": "***",
        "priority": "Top Priority (Most Probable)",
        "boards": "Ctg.B. '22, B.B. '24, Syl.B. '25",
        "passage": (
            "Countries of the world rely heavily on petroleum, coal, and natural gas for their energy requirements. These are "
            "finite fossil fuels formed over millions of years inside the earth's crust. As industrial civilization consumes these "
            "resources at an accelerating pace, geologists warn that fossil fuel reserves will be completely depleted within a few decades. "
            "Moreover, burning fossil fuels releases greenhouse gases that drive global climate catastrophe. To avert global economic "
            "collapse and ecological doom, humanity must urgently transition to clean, inexhaustible renewable energy sources. Solar "
            "radiation, wind currents, and flowing hydroelectric water are abundant, eco-friendly, and replenishable. Rooftop solar "
            "panels and offshore wind farms represent the future of sustainable energy."
        ),
        "mcqs": [
            {"q": "What is the primary danger associated with continued reliance on fossil fuels?", "opts": ["They are too cheap", "They are finite, depleting rapidly, and cause catastrophic global warming", "They cannot produce electricity", "They are clean"], "ans": "They are finite, depleting rapidly, and cause catastrophic global warming"},
            {"q": "Which of the following represents an inexhaustible renewable energy source?", "opts": ["Coal", "Petroleum diesel", "Solar radiation and wind power", "Kerosene"], "ans": "Solar radiation and wind power"},
            {"q": "The word 'replenishable' signifies energy that —", "opts": ["Can be renewed or restored naturally", "Disappears forever after use", "Is highly toxic", "Cannot be converted"], "ans": "Can be renewed or restored naturally"}
        ],
        "open_qas": [
            {"q": "Why are petroleum and natural gas termed 'finite' energy sources?", "a": "They are called finite because they require millions of years of geological compression to form, meaning that once current subsurface reserves are consumed, they cannot be replaced."},
            {"q": "What benefits does Bangladesh gain by investing in rural solar home systems?", "a": "Solar home systems provide clean, uninterrupted electricity to remote off-grid villages, eliminating dependence on polluting kerosene lamps and fostering rural cottage industries."}
        ],
        "gap_fill": {
            "sentence": "The world's energy security is threatened by the rapid (a) ______ of fossil fuel reserves. Burning coal and oil releases massive amounts of carbon (b) ______, warming the planet dangerously. Therefore, countries must switch to (c) ______ energy alternatives like solar, wind, and hydropower. Investing in green energy guarantees a healthy (d) ______ and a stable economic (e) ______.",
            "answers": {"a": "depletion / exhaustion", "b": "dioxide / emissions", "c": "renewable / green", "d": "planet / environment", "e": "future / foundation"}
        },
        "vocab_notes": "Replenishable -> Naturally restorable; Finite -> Limited in quantity; Inexhaustible -> Limitless/incapable of running out."
    },
    {
        "id": 33,
        "slug_id": "seen-33",
        "title": "Internet Technology and E-Learning: Revolutionizing Global Education",
        "unit_lesson": "Unit-15, Lesson-2(B)",
        "theme": "E-Learning, Digital Classrooms, Distance Education & Educational Equity",
        "stars": "***",
        "priority": "Top Priority (Most Probable)",
        "boards": "R.B. '19, C.B. '20, D.B., J.B. '24",
        "passage": (
            "The Internet technology has helped modernize our lifestyle and revolutionize how knowledge is disseminated across "
            "the globe. In the realm of education, it has dismantled physical geographical barriers through 'e-learning' (electronic learning). "
            "Today, students in remote rural villages can access world-class lectures, digital libraries, and virtual laboratory simulations "
            "from top global universities with a single mouse click. During crises like pandemic lockdowns, video-conferencing platforms like "
            "Zoom and Google Meet enabled educational institutions to conduct virtual classrooms without interruption. E-learning fosters "
            "self-paced learning, interactive quizzes, and global collaboration, democratizing education and turning the world into a seamless global village."
        ),
        "mcqs": [
            {"q": "How has e-learning transformed traditional education across the world?", "opts": ["By abolishing schools", "By dismantling geographical barriers and democratizing knowledge access", "By making exams harder", "By stopping teacher training"], "ans": "By dismantling geographical barriers and democratizing knowledge access"},
            {"q": "What allowed educational continuity during pandemic lockdowns?", "opts": ["Postal letters", "Online virtual classrooms and video-conferencing platforms", "Telegraphs", "Complete shutdown"], "ans": "Online virtual classrooms and video-conferencing platforms"},
            {"q": "The word 'disseminated' is synonymous with —", "opts": ["Concealed", "Distributed or spread widely", "Destroyed", "Purchased"], "ans": "Distributed or spread widely"}
        ],
        "open_qas": [
            {"q": "What are the primary benefits of internet-based e-learning for remote students?", "a": "It allows marginalized rural students to access top-tier digital textbooks, interactive multimedia simulations, and recorded university lectures at affordable costs without relocating to major cities."},
            {"q": "What infrastructure challenges must developing countries address to achieve digital education equity?", "a": "Developing countries must expand affordable high-speed broadband internet to rural communities, provide subsidized digital devices to poor students, and train teachers in digital pedagogies."}
        ],
        "gap_fill": {
            "sentence": "Internet technology has ushered in a digital (a) ______ in modern education. Through e-learning, students can acquire knowledge beyond traditional classroom (b) ______. Digital libraries and virtual lectures make learning more engaging and (c) ______. To eliminate the digital divide, governments must ensure affordable internet (d) ______ for students in every rural (e) ______.",
            "answers": {"a": "revolution / era", "b": "boundaries / walls", "c": "accessible / flexible", "d": "access / connectivity", "e": "village / corner"}
        },
        "vocab_notes": "Disseminated -> Spread widely; Pedagogies -> Teaching methods; Democratizing -> Making accessible to everyone."
    }
]

def generate_full_file():
    print(f"Generating {OUTPUT_FILE} with {len(SEEN_DATA_33)} full seen topics...")
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write('#!/usr/bin/env python3\n')
        f.write('# -*- coding: utf-8 -*-\n')
        f.write('"""\n')
        f.write('tools/pdf_to_post/data_ssc_2027_seen_full.py\n')
        f.write('---------------------------------------------\n')
        f.write('Complete dataset of all 33 Seen Passages for SSC 2027 English 1st Paper Silo 01:\n')
        f.write('- Passage excerpt from English For Today (120-170 words)\n')
        f.write('- Question 1: Multiple Choice Questions (3 MCQs with options and answers)\n')
        f.write('- Question 2: Open-Ended Comprehension Questions (2 analytical Q/As)\n')
        f.write('- Question 3: Gap Filling Without Clues (5 blanks with exact answer key)\n')
        f.write('- Key Vocabulary & Synonyms Notes\n')
        f.write('"""\n\n')

        f.write("SEEN_PASSAGES_FULL_33 = [\n")
        for item in SEEN_DATA_33:
            f.write("    {\n")
            f.write(f'        "id": {item["id"]},\n')
            f.write(f'        "slug_id": "{item["slug_id"]}",\n')
            f.write(f'        "title": {repr(item["title"])},\n')
            f.write(f'        "unit_lesson": {repr(item["unit_lesson"])},\n')
            f.write(f'        "theme": {repr(item["theme"])},\n')
            f.write(f'        "stars": "{item["stars"]}",\n')
            f.write(f'        "priority": "{item["priority"]}",\n')
            f.write(f'        "boards": "{item["boards"]}",\n')
            f.write(f'        "passage": {repr(item["passage"])},\n')
            f.write(f'        "mcqs": {repr(item["mcqs"])},\n')
            f.write(f'        "open_qas": {repr(item["open_qas"])},\n')
            f.write(f'        "gap_fill": {repr(item["gap_fill"])},\n')
            f.write(f'        "vocab_notes": {repr(item["vocab_notes"])},\n')
            f.write("    },\n")
        f.write("]\n")

    print(f"[OK] Successfully wrote {OUTPUT_FILE} ({len(SEEN_DATA_33)} topics).")

if __name__ == "__main__":
    generate_full_file()
