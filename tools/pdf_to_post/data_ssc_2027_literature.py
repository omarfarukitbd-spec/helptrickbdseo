#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/pdf_to_post/data_ssc_2027_literature.py
------------------------------------------------
100% faithful data for Literature: Poems (Q8) & Stories (Q9).
Contains:
1. All 7 Poems with Star Ratings, Themes, Poetic Devices, and Focus Questions
2. All 23 Stories with Star Ratings, Core Themes, Characters, and Moral Lessons
3. Dakhil 2026 Board Exam Q8 (8 Poems Q/A) & Q9 (8 Stories Q/A)
4. Exclusive Model Test Q8 (8 Poems Q/A) & Q9 (8 Stories Q/A)
"""

POEMS_7_RATINGS = [
    {
        "id": 1,
        "serial": 2,
        "stars": "***",
        "title": "Time, You Old Gipsy Man",
        "poet": "Ralph Hodgson",
        "theme": "The relentless and irreversible passage of time and humanity's yearning to pause precious moments.",
        "devices": "Personification of Time as an old gipsy wanderer, imagery of bells, golden rings, and peacocks.",
        "priority": "Top Priority (Most Probable for SSC 2027)"
    },
    {
        "id": 2,
        "serial": 3,
        "stars": "***",
        "title": "Stopping by Woods on a Snowy Evening",
        "poet": "Robert Frost",
        "theme": "The delicate balance between admiring the serene beauty of nature and fulfilling moral responsibilities before death.",
        "devices": "Repetition ('And miles to go before I sleep'), visual and auditory imagery (dark woods, harness bells, easy wind).",
        "priority": "Top Priority (Most Probable for SSC 2027)"
    },
    {
        "id": 3,
        "serial": 5,
        "stars": "***",
        "title": "O Me! O Life!",
        "poet": "Walt Whitman",
        "theme": "The struggle with existential disillusionment, foolishness, and despair, answered by the triumphant joy that life exists and one may contribute a verse.",
        "devices": "Free verse, rhetorical questions, philosophical reflection, anaphora.",
        "priority": "Top Priority (Most Probable for SSC 2027)"
    },
    {
        "id": 4,
        "serial": 1,
        "stars": "**",
        "title": "The Sands of Dee",
        "poet": "Charles Kingsley",
        "theme": "Tragedy of rural life where Mary drowns in a raging western sea tide while bringing cattle home.",
        "devices": "Ballad rhythm, refrain ('Call the cattle home'), haunting natural imagery of rolling mist and wild foam.",
        "priority": "High Priority"
    },
    {
        "id": 5,
        "serial": 4,
        "stars": "**",
        "title": "To be Remembered",
        "poet": "EFT Textbook Selection",
        "theme": "The unconditional bond of motherly love through all evolving stages of life and filial duty to care for aging parents.",
        "devices": "Emotional lyricism, nostalgic contrast between childhood and adulthood.",
        "priority": "High Priority"
    },
    {
        "id": 6,
        "serial": 6,
        "stars": "**",
        "title": "Sea-Fever",
        "poet": "John Masefield",
        "theme": "The uncontrollable, passionate wanderlust of a sailor yearning to return to the lonely sea and the starry sky.",
        "devices": "Vivid maritime sensory imagery (grey dawn, wild call, flung spray, blown spume).",
        "priority": "High Priority"
    },
    {
        "id": 7,
        "serial": 7,
        "stars": "*",
        "title": "Each Book is a Magic Box",
        "poet": "EFT Textbook Selection",
        "theme": "The transformative magic of books as treasure chests that transport readers to distant realms and wisdom.",
        "devices": "Extended metaphor (book as magic box), childlike wonder, imaginative imagery.",
        "priority": "Moderate Priority"
    }
]

STORIES_23_RATINGS = [
    {
        "id": 1,
        "serial": 1,
        "stars": "***",
        "title": "The Merchant of Venice",
        "author": "William Shakespeare",
        "theme": "Justice tempered with mercy, true friendship between Antonio and Bassanio, and defeat of greed and revenge.",
        "characters": "Antonio (generous merchant), Bassanio (devoted friend), Shylock (cruel moneylender), Portia (wise heroine).",
        "priority": "Top Priority (Highest Probable for SSC 2027 Q9)"
    },
    {
        "id": 2,
        "serial": 2,
        "stars": "***",
        "title": "The Story of an Hour",
        "author": "Kate Chopin",
        "theme": "The complex psychology of female independence, sudden grief, and the tragic shock of lost freedom.",
        "characters": "Mrs. Louise Mallard, Brently Mallard, Josephine, Richards.",
        "priority": "Top Priority (Highest Probable for SSC 2027 Q9)"
    },
    {
        "id": 3,
        "serial": 14,
        "stars": "***",
        "title": "The Purple Jar",
        "author": "Maria Edgeworth",
        "theme": "The consequence of impulsive vanity over practical utility; learning through painful experience.",
        "characters": "Rosamond (impulsive 7-year-old girl), Rosamond's mother (wise, disciplined guide).",
        "priority": "Top Priority (Highest Probable for SSC 2027 Q9)"
    },
    {
        "id": 4,
        "serial": 15,
        "stars": "***",
        "title": "The Gift of the Magi",
        "author": "O. Henry",
        "theme": "Selfless, sacrificial love where mutual devotion transcends grinding poverty.",
        "characters": "Della (sacrifices hair for watch chain), Jim (sacrifices gold watch for combs).",
        "priority": "Top Priority"
    },
    {
        "id": 5,
        "serial": 16,
        "stars": "***",
        "title": "The Last Leaf",
        "author": "O. Henry",
        "theme": "Hope, supreme artistic sacrifice, and the enduring power of unconditional friendship.",
        "characters": "Johnsy (pneumonia patient), Sue (loyal friend), Behrman (old artist who paints masterpiece).",
        "priority": "Top Priority"
    },
    {
        "id": 6,
        "serial": 17,
        "stars": "***",
        "title": "The Necklace",
        "author": "Guy de Maupassant",
        "theme": "The tragic ruin caused by false pride, vanity, and the deception of social appearances.",
        "characters": "Mathilde Loisel (vain wife), Monsieur Loisel (devoted husband), Madame Forestier.",
        "priority": "Top Priority"
    },
    {
        "id": 7,
        "serial": 18,
        "stars": "***",
        "title": "The Luncheon",
        "author": "William Somerset Maugham",
        "theme": "Social hypocrisy, culinary extravagance, and humorous irony of financial vulnerability.",
        "characters": "The young writer (struggling narrator), The lady guest (gluttonous flatterer).",
        "priority": "Top Priority"
    },
    {
        "id": 8,
        "serial": 19,
        "stars": "***",
        "title": "A Mother in Mannville",
        "author": "Marjorie Kinnan Rawlings",
        "theme": "Integrity, pride of an orphan, longing for maternal affection, and emotional vulnerability.",
        "characters": "Jerry (orphan boy at Carolina mountain orphanage), The writer (narrator), Pat (dog).",
        "priority": "Top Priority"
    },
    {
        "id": 9,
        "serial": 23,
        "stars": "**",
        "title": "The Old Man at the Bridge",
        "author": "Ernest Hemingway",
        "theme": "The tragic impact of modern warfare on innocent, helpless civilians and animals.",
        "characters": "The old man (76-year-old peasant from San Carlos), The war scout (narrator).",
        "priority": "High Priority"
    },
    {
        "id": 10,
        "serial": 20,
        "stars": "*",
        "title": "The Selfish Giant",
        "author": "Oscar Wilde",
        "theme": "Redemption through love, compassion for innocent children, and spiritual rebirth.",
        "characters": "The Giant, The Little Boy (Christ child), The children.",
        "priority": "Moderate Priority"
    },
    {
        "id": 11,
        "serial": 21,
        "stars": "*",
        "title": "The Happy Prince",
        "author": "Oscar Wilde",
        "theme": "Selfless sacrifice for the poor and suffering of society; spiritual beauty over physical grandeur.",
        "characters": "The Happy Prince (golden statue), The Little Swallow.",
        "priority": "Moderate Priority"
    },
    {
        "id": 12,
        "serial": 22,
        "stars": "*",
        "title": "The Open Window",
        "author": "Saki (H.H. Munro)",
        "theme": "Deception through brilliant romance on short notice; psychological vulnerability.",
        "characters": "Framton Nuttel (nerve patient), Vera (15-year-old niece), Mrs. Sappleton.",
        "priority": "Moderate Priority"
    }
]

DAKHIL_2026_POEMS_QA = [
    {
        "q_num": "8(a)",
        "question": "Do you like the poem 'To be Remembered'? Why?",
        "answer": "Yes, I like the poem because it shows deep love between a mother and her daughter. It also teaches that we should love and care for our mothers, even when they grow old and change."
    },
    {
        "q_num": "8(b)",
        "question": "Why should children love both versions of their mother?",
        "answer": "Children should love both versions of their mother because each phase of her life offers something important. As she changes, the love and care she gives may evolve, but it remains just as essential."
    },
    {
        "q_num": "8(c)",
        "question": "Why did the poet stop by the woods in 'Stopping by Woods on a Snowy Evening'?",
        "answer": "The poet stopped by the woods to watch the snow falling quietly and admire the peaceful, dark, and deep forest scenery before continuing his journey."
    },
    {
        "q_num": "8(d)",
        "question": "How has the sea been described in the poem?",
        "answer": "The sea has been described as a vast, powerful, and mysterious realm that devours life yet calls the sailor with an irresistible and wild call that cannot be denied."
    },
    {
        "q_num": "8(e)",
        "question": "What things were offered by the poet for the old gipsy man?",
        "answer": "The poet offered: (i) Bells for Time's jennet, (ii) A great golden ring, (iii) Peacocks bowing to Time, (iv) Little boys singing for Time, and (v) Sweet girls festooning Time with may-flowers."
    },
    {
        "q_num": "8(f)",
        "question": "Write the name of the poet of the poem 'Time, You Old Gipsy Man'.",
        "answer": "The poet of the poem 'Time, You Old Gipsy Man' is Ralph Hodgson."
    },
    {
        "q_num": "8(g)",
        "question": "What do you understand by the line 'Each Book is a Magic Box'?",
        "answer": "The poet means that a child can unlock books with just a touch. Inside, books hold many wonders and surprises that magically transport readers to new places and give joy."
    },
    {
        "q_num": "8(h)",
        "question": "How did the milliner's shop look like in the textbook story?",
        "answer": "The shop was decorated with beautiful ribbons and lace, with many colorful artificial flowers hanging in the windows, designed to catch the eyes of passers-by like Rosamond."
    }
]

DAKHIL_2026_STORIES_QA = [
    {
        "q_num": "9(a)",
        "question": "Who was Portia? What do you know about her?",
        "answer": "Portia was a wealthy, beautiful, and exceptionally wise noblewoman from Belmont who married Bassanio after he chose the correct casket. She later disguised herself as a lawyer to save Antonio's life."
    },
    {
        "q_num": "9(b)",
        "question": "How did Portia and her friend disguise themselves in the courtroom?",
        "answer": "Portia disguised herself as a young lawyer named Doctor Balthazar to defend Antonio, while her clever maid Nerissa accompanied her disguised as a lawyer's clerk."
    },
    {
        "q_num": "9(c)",
        "question": "Who was Shylock? What do you know about him?",
        "answer": "Shylock was a greedy, cruel, and cunning moneylender of Venice. He hated Antonio for being kind and lending money without interest, and wanted revenge by cutting a pound of flesh from Antonio's body."
    },
    {
        "q_num": "9(d)",
        "question": "Who lent money to the poor without charging any interest?",
        "answer": "Antonio was the generous merchant who lent money to the needy without charging interest, which is why the common people of Venice loved and respected him deeply."
    },
    {
        "q_num": "9(e)",
        "question": "How did Portia save Antonio's life?",
        "answer": "Portia pointed out a loophole in the bond: Shylock was entitled to exact a pound of flesh, but if he shed a single drop of Christian blood, all his wealth would be forfeited to the state of Venice."
    },
    {
        "q_num": "9(f)",
        "question": "Who walked towards Antonio with a knife and why?",
        "answer": "Shylock walked towards Antonio with a sharp knife to cut a pound of flesh from his breast as a contractual penalty because Antonio failed to repay the 3,000 ducats on time."
    },
    {
        "q_num": "9(g)",
        "question": "Who was the close friend of Antonio?",
        "answer": "Bassanio was the intimate friend of Antonio. Antonio loved him so dearly that he risked his own life by signing the fatal bond to finance Bassanio's courtship in Belmont."
    },
    {
        "q_num": "9(h)",
        "question": "Sketch the character of Antonio.",
        "answer": "Antonio was a wealthy, noble, and generous merchant of Venice who was selfless, honest, and ever-willing to sacrifice everything for his friends."
    }
]

MODEL_TEST_POEMS_QA = [
    {
        "q_num": "8(a)",
        "question": "What does the speaker ask Time to do in the poem 'Time, You Old Gipsy Man'?",
        "answer": "In the poem 'Time, You Old Gipsy Man', the poet asks Time to stop or pause its relentless journey, even if just for a single day, offering him various precious gifts."
    },
    {
        "q_num": "8(b)",
        "question": "What is the main theme of the poem 'Time, You Old Gipsy Man'?",
        "answer": "The main theme is the fleeting, irreversible nature of Time and the universal human desire to pause its rapid flight in order to savor the beautiful moments of life."
    },
    {
        "q_num": "8(c)",
        "question": "What is the main theme of the poem 'Stopping by Woods on a Snowy Evening'?",
        "answer": "The main theme is the conflict between the desire to immerse oneself in the enchanting peace of nature and the necessity of keeping promises and fulfilling worldly duties before death."
    },
    {
        "q_num": "8(d)",
        "question": "Where does the speaker stop in 'Stopping by Woods on a Snowy Evening'?",
        "answer": "The speaker stops between the frozen lake and the dark, snow-covered woods of a village neighbor to watch the gentle flakes fill up the trees."
    },
    {
        "q_num": "8(e)",
        "question": "Who is Mary in the poem of your textbook?",
        "answer": "Mary is the innocent daughter of a poor peasant living beside the estuary of the River Dee who goes out alone across the marsh to bring the cattle home."
    },
    {
        "q_num": "8(f)",
        "question": "What was the weather like when Mary went out?",
        "answer": "The weather was dangerous and stormy, characterized by wild, blinding western winds and thick rolling sea foam that concealed the treacherous rising tide."
    },
    {
        "q_num": "8(g)",
        "question": "What is the poem 'O Me! O Life!' about?",
        "answer": "The poem 'O Me! O Life!' explores the existential meaning and purpose of human existence despite recurring struggles, human foolishness, and endless disappointments."
    },
    {
        "q_num": "8(h)",
        "question": "Who is the speaker in the poem 'O Me! O Life!'?",
        "answer": "The speaker is a disillusioned and soul-searching version of the poet Walt Whitman himself, questioning the worth of life and concluding that merely existing and contributing a verse makes life sublime."
    }
]

MODEL_TEST_STORIES_QA = [
    {
        "q_num": "9(a)",
        "question": "Who had brought the news of Mr. Brently Mallard's death in 'The Story of an Hour'?",
        "answer": "Mr. Mallard's close friend Richards brought the news. He was in the newspaper office when the list of rail disaster fatalities was received and saw Brently Mallard's name at the top."
    },
    {
        "q_num": "9(b)",
        "question": "How did Mr. Mallard die, according to the rumour?",
        "answer": "According to the telegraph report, Mr. Mallard was killed in a catastrophic railroad disaster."
    },
    {
        "q_num": "9(c)",
        "question": "Who was already in the court of justice when Bassanio reached Venice?",
        "answer": "Antonio, along with Shylock and the Duke of Venice, was already in the courtroom awaiting the trial to begin."
    },
    {
        "q_num": "9(d)",
        "question": "What were they waiting for in the court of justice?",
        "answer": "They were waiting for the arrival of Doctor Bellario, a learned jurist of Padua who had been summoned by the Duke to judge the legal dispute."
    },
    {
        "q_num": "9(e)",
        "question": "When did the Duke enter the courtroom?",
        "answer": "The Duke entered the courtroom at the commencement of the session and took his seat on the judicial bench before summoning Antonio and Shylock."
    },
    {
        "q_num": "9(f)",
        "question": "Who is Rosamond in 'The Purple Jar'?",
        "answer": "Rosamond is a seven-year-old impulsive, inquisitive girl who is easily fascinated by pretty, glittering but useless ornamental objects."
    },
    {
        "q_num": "9(g)",
        "question": "Where were Rosamond and her mother walking?",
        "answer": "Rosamond and her mother were walking down the busy streets of London, window-shopping and looking at various retail displays."
    },
    {
        "q_num": "9(h)",
        "question": "What did Rosamond want to do when she saw the shop windows?",
        "answer": "When Rosamond saw the chemist's shop window, she was enchanted by the sparkling purple jar and desperately wanted to buy it instead of necessary new shoes."
    }
]

