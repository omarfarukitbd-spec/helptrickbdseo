#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/pdf_to_post/generate_full_writing_data.py
Constructs data_ssc_2027_writing_full.py containing complete stories & dialogues for SSC 2027.
"""

import os
import sys

OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "data_ssc_2027_writing_full.py")

# Import original prompts and metadata
from data_ssc_2027_writing import (
    COMPLETING_STORIES_34,
    DIALOGUES_32,
    MODEL_STORY_LUCKY_TICKET,
    DAKHIL_2026_STORY,
    MODEL_TEST_STORY,
    MODEL_DIALOGUES_VERBATIM,
    DAKHIL_2026_DIALOGUE,
    MODEL_TEST_DIALOGUE
)

# Complete stories narrative and morals mapped by ID
STORIES_EXTRAS = {
    1: {
        "moral": "Dress does not make a man / Outward appearance is not the measure of true worth.",
        "continuation": """The nobleman treated Sheikh Saadi very coldly and served him ordinary food in a casual manner. Saadi ate quietly and left the following morning without uttering any complaint.

A few months later, Sheikh Saadi was invited to the court once again. This time, he was adorned in a magnificent royal robe made of rich silk and wore precious ornaments. On his journey, night fell, and he again sought shelter at the very same nobleman's house.

Recognizing the regal attire, the nobleman welcomed him with extravagant hospitality, bowed with utmost deference, and escorted him to an opulent dining hall. A grand feast featuring rich pilau, roast meat, and delicious sweets was served before him.

When the meal began, Sheikh Saadi did not eat a morsel. Instead, he took spoonfuls of the delicious dishes and began stuffing them into the wide pockets of his rich robe, saying, "Eat, my fine dress! Eat, rich coat! This sumptuous feast is prepared for you, not for me."

The nobleman was dumbfounded and asked in utter bewilderment, "Respected Sir, why are you feeding your clothes instead of eating yourself?"

Sheikh Saadi replied with calm dignity, "A few months ago, I visited your house in humble, worn clothes, and you served me coarse scraps. Today, I am the exact same human being, yet you treat me like royalty solely because of my luxurious garments. It is evident that your honor is meant for my dress, not for me."

The nobleman realized his foolishness, hung his head in profound shame, and begged Sheikh Saadi's forgiveness. From that day on, he resolved never to judge any person by outward appearance."""
    },
    2: {
        "moral": "Too much greed leads to immense sorrow and ruin.",
        "continuation": """The wise god granted King Midas his coveted wish. Overjoyed, Midas went out into his royal garden to test his new power. He touched an oak branch, and it instantly turned into solid gold. He touched a stone, a rose, and a palace pillar—each transformed into pure, gleaming gold. Midas felt like the most powerful monarch alive.

Soon, he felt hungry and ordered a lavish feast. But the moment he lifted a piece of bread to his mouth, it turned into hard metal. When he tried to drink a goblet of cool water, it turned into liquid gold that choked his throat. Panic gripped his heart as he realized he could neither eat nor drink.

Just then, his beloved little daughter ran into the room to comfort her distressed father. Without thinking, Midas embraced her tenderly. To his horror, the warm, smiling child turned into a cold, lifeless statue of solid gold before his very eyes.

Midas fell to his knees in agony, weeping bitter tears. He realized that all the gold in the universe could not replace the laughter of his darling daughter or a single drop of cool water. He raised his hands toward the heavens and pleaded, "O Lord, take away this dreadful golden touch! Save my daughter!"

Moved by his sincere repentance, the god instructed him to wash in the waters of the River Pactolus and sprinkle that water over everything he had turned to gold. Midas hurried to the river, bathed his hands, and sprinkled the sacred water over his daughter. To his immense joy, the rosy cheeks of his little girl returned to life. Midas renounced his greed and lived in humble gratitude ever after."""
    },
    3: {
        "moral": "Where there is a will, there is a way.",
        "continuation": """The thirsty crow peered inside the jar. The water level was so low at the bottom that its beak could not reach it, no matter how hard it stretched. It attempted to overturn the heavy earthen pitcher, but the vessel was too sturdy to be pushed.

The crow felt exhausted and parched, but it refused to surrender to despair. It paused and began to think deeply. Looking around the courtyard, it noticed a heap of small pebbles lying near a stone wall. A brilliant idea flashed through its sharp mind.

The crow flew to the pile, picked up a pebble in its beak, and dropped it into the jar. Plop! Then it picked another, and another, and dropped them in one by one. With each stone dropped, the water at the bottom began to rise slowly toward the neck of the jar.

The crow worked patiently without tiring. After dropping dozens of pebbles, the cool water finally reached the very brim of the pitcher. Delighted, the clever bird quenched its burning thirst with sweet, fresh water and flew away triumphantly into the blue sky."""
    },
    4: {
        "moral": "A friend in need is a friend indeed.",
        "continuation": """The sudden appearance of the ferocious bear terrified both friends. One of the friends was agile and knew how to climb trees. Thinking solely of his own safety, he quickly leaped toward a tall tree and scrambled up into the high branches, leaving his companion helpless on the ground below.

The second friend could not climb trees. However, he kept his presence of mind and remembered a piece of jungle lore: bears never touch or eat a dead human body. Without losing a second, he threw himself flat upon the grassy earth, closed his eyes, and held his breath, pretending to be lifeless.

The heavy bear lumbered over to him. It sniffed around his ears, nostrils, and chest. The young man lay perfectly motionless like a corpse. Sensing no breath or heartbeat, the wild animal assumed he was dead and quietly wandered back into the thick forest.

After the beast was out of sight, the friend up in the tree slid down to the ground. Chuckling nervously, he asked, "My dear friend, I saw the bear whispering something closely into your ear! What wise advice did the beast impart to you?"

The friend stood up, brushed off the dust from his clothes, and looked him straight in the eye. "The bear gave me a very precious piece of advice," he answered firmly. "It told me never to trust a selfish friend who abandons his companion at the first sign of danger." With these words, he walked away alone, ending their false friendship."""
    },
    5: {
        "moral": "Never trust the sweet words of a flatterer.",
        "continuation": """The hungry fox's mouth watered at the sight of the juicy meat. Being cunning, he knew he could not climb the tall tree to take it by force. Therefore, he decided to employ sweet flattery to outwit the proud bird.

The fox walked politely beneath the branch, looked up with an expression of great admiration, and said, "Good morning, most graceful Queen of birds! How radiant your feathers look today! Surely, a bird with such dazzling plumage and regal beauty must possess an equally sweet and enchanting singing voice. Won't you sing a melodious song for your humble admirer?"

The foolish crow was overwhelmed with vanity. No one had ever praised its appearance or called its harsh voice melodious before. Blinded by pride and eager to prove its musical talent, the crow opened its beak wide and let out a loud, grating "Caw! Caw!"

The instant its beak opened, the precious piece of meat slipped from its grasp and tumbled to the ground. The clever fox leaped forward, snatched the meat in his jaws, and swallowed it greedily. Looking up with a mocking grin, the fox said, "Thank you for the breakfast, friend! You have feathers and vanity, but alas, you lack common sense!" The ashamed crow learned that flatterers always seek personal gain."""
    },
    6: {
        "moral": "One good turn deserves another.",
        "continuation": """The poor ant was struggling desperately against the strong current and was about to drown. Seeing the helpless insect in distress, the kind dove plucked a broad green leaf from a branch and dropped it gently into the water right beside the ant.

The ant climbed onto the floating leaf, dried its drenched wings, and floated safely to the dry bank of the stream. Looking up toward the tree, the ant silently thanked the merciful bird for saving its life and vowed to return the kindness if ever given an opportunity.

A few days later, a cruel hunter entered the woods carrying a bow and arrow. He spotted the lovely dove resting peacefully on a high branch and began to take careful aim at her breast. The dove was completely unaware of the deadly peril lurking below.

Fortunately, the little ant noticed the hunter drawing his bowstring. Without hesitating, the ant crawled rapidly onto the hunter's bare foot and bit him with all its might.

"Ouch!" the hunter yelled in sudden pain, dropping his bow and dropping his aim. The sharp noise alerted the dove instantly. She fluttered her wings and flew away safely into the distant sky. Thus, the tiny ant repaid the noble deed of the dove."""
    },
    7: {
        "moral": "Nobody believes a liar, even when he tells the truth.",
        "continuation": """Whenever the villagers heard his frantic screams of "Tiger! Tiger!", they would abandon their work in the fields, grab heavy sticks and axes, and run panting to the pasture to rescue the young shepherd.

Upon arriving, they would find the mischievous boy rolling on the grass laughing uncontrollably. "Ha! Ha! I fooled all of you! There is no tiger here!" The villagers felt deeply annoyed and warned him sternly never to play such dangerous pranks again. But the reckless boy repeated the same trick a few days later, laughing at their wasted effort.

One afternoon, a real royal Bengal tiger emerged silently from the thick forest. Its eyes burned like fiery coals, and it growled menacingly as it crept toward the cattle.

Terrified out of his wits, the cowboy scrambled up a tree and screamed at the top of his voice, "Help! Help! Tiger! Real tiger! Please come, villagers!"

The villagers heard his distant cries, but this time they shook their heads and smiled cynically. "That wicked boy is trying to deceive us again," they muttered to one another. "We will not waste our energy running to his rescue."

No one came to help. The ferocious tiger attacked the herd, killed several cows, and finally dragged the weeping boy down from the low branches and killed him on the spot. His habitual falsehood cost him his life."""
    },
    8: {
        "moral": "It is easy to propose an idea, but difficult to put it into practice.",
        "continuation": """The mice could no longer forage for food without the constant terror of the prowling cat. Several of their relatives had already been caught and devoured. To solve this crisis of survival, the leader of the mice summoned an urgent general council.

Many suggestions were put forward, but none seemed practical. Finally, an energetic young mouse stood up proudly and addressed the gathering: "Brothers, our enemy moves with silent paws. If we tie a small brass bell around the cat's neck, the bell will tinkle every time she moves! We will hear her approach from afar and easily dart into our holes."

The entire assembly burst into loud applause. The mice cheered enthusiastically and praised the young mouse as a genius strategist.

Amidst the joyful commotion, an old, grey-whiskered mouse who had been sitting quietly in a corner stood up slowly. He raised his paw for silence and said gently, "My dear young friend, your idea is truly ingenious and would certainly protect us all. But allow me to ask just one simple question: Who among us is brave enough to go up to the fierce cat and tie the bell around her neck?"

A dead silence fell upon the assembly. Every mouse looked at one another in fear, but not a single one volunteered to take on the fatal mission. The mice realized that conceiving a brilliant plan is easy, but executing it requires real courage."""
    },
    9: {
        "moral": "Perseverance is the key to success / Failure is the pillar of success.",
        "continuation": MODEL_TEST_STORY["full_story"]
    },
    10: {
        "moral": "Honesty is the best policy.",
        "continuation": """The poor woodcutter sat weeping on the riverbank because the axe was his sole means of earning daily bread for his hungry family. Seeing his plight, a radiant water fairy rose gracefully from the swirling depths of the river.

"Why are you weeping so bitterly, honest woodcutter?" the fairy asked with a gentle voice. The man explained through tears how his iron axe had slipped from his sweaty grasp into the deep water.

The fairy took pity on him. She dove beneath the surface and soon returned holding an axe crafted entirely of sparkling gold. "Is this splendid axe yours?" she inquired. The woodcutter looked at it, shook his head, and replied honestly, "No, kind fairy, this is not my axe. I am a poor man; I cannot claim an axe of gold."

The fairy dove a second time and brought up an axe made of polished silver. "Then this silver axe must surely belong to you?" she asked. The woodcutter replied with humility, "No, fairy, this silver axe does not belong to me either."

For the third time, she plunged into the deep stream and emerged holding the plain, rusty iron axe. The woodcutter's eyes shone with pure joy. "Yes! That is my axe! Thank you, kind fairy!" he cried out in gratitude.

Deeply impressed by his upright conscience and incorruptible honesty, the fairy smiled warmly. "I am overjoyed by your truthfulness," she proclaimed. "Take your iron axe, and accept both the golden and silver axes as rewards for your noble integrity." The honest woodcutter returned home happily and lived in comfort for the rest of his days."""
    },
    11: {
        "moral": "Unconditional devotion to parents earns the highest blessings of God.",
        "continuation": """Finding the pitcher empty in the kitchen, Bayazid did not hesitate. Despite the biting cold of the winter midnight, he took the earthen pitcher and walked through the dark, quiet village to a distant freshwater spring. He filled the pitcher and hurried back home with a glass of cool water.

When he reached his mother's bedside, he found that she had fallen back into a deep sleep due to weakness and medication. Bayazid thought of waking her, but feared disturbing her much-needed rest. On the other hand, he could not bear the thought of placing the glass down, lest she wake up thirsty again.

Therefore, the devoted young boy stood motionless beside her bed, holding the glass of water in his hands all through the freezing night. His fingers grew numb with cold, but his resolve remained unshaken.

As the first light of dawn entered the window, the mother opened her eyes. She was astonished to see her young son standing faithfully by her pillow, holding the glass of water with trembling, frostbitten hands.

Tears welled up in her eyes as she learned that he had remained standing the entire night. Overcome with maternal affection, she drank the water, hugged him to her bosom, and raised her hands in fervent prayer: "O Almighty Allah, bestow Your highest grace upon my dutiful son Bayazid and make him one of Your greatest saints."

Allah granted the heartfelt prayer of the devoted mother. In time, Bayazid Bostami grew to become one of the most revered spiritual masters and Islamic philosophers in history."""
    },
    12: {
        "moral": "Slow and steady wins the race.",
        "continuation": """The race commenced with great excitement. The swift hare darted ahead like an arrow, covering a huge distance in a matter of minutes. When he reached halfway, he looked back and could not see the tortoise anywhere on the dusty trail.

"That sluggish creature will take hours to reach this point," chuckled the hare arrogantly. "The day is warm, and I have plenty of time. Why not take a short nap under this shady banyan tree before finishing the race?"

Confident of his effortless victory, the hare lay down on the soft grass and soon fell into a sound sleep.

Meanwhile, the tortoise continued to plod forward slowly but steadily. It never stopped to rest, never complained of the heat, and never lost sight of the distant goal. Step by step, it covered the ground with quiet determination.

Hours passed. The tortoise quietly passed by the sleeping hare without making a sound. Keeping its eyes fixed ahead, it steadily approached the finish line.

When the hare finally woke up, the sun was setting. He rubbed his eyes, yawned, and bounded toward the finish banner at full speed. But to his utter dismay and humiliation, he saw the patient tortoise already resting across the finish line, surrounded by cheering forest animals. The boastful hare bowed his head in shame."""
    },
    13: {
        "moral": "Always honor your promises, or face severe retribution.",
        "continuation": """The mysterious piper dressed in bright, colorful garments promised the Mayor that he would rid Hamelin of every single rat in exchange for one thousand gold guilders. The desperate Mayor gladly shook hands on the deal, promising double that amount if he succeeded.

The piper stepped onto the town streets and placed his slender pipe to his lips. A strange, haunting melody echoed across the rooftops. Instantly, from every cellar, attic, drain, and bakery, swarms of rats rushed out and followed the piper spellbound. He led the endless army of rodents down to the River Weser, where every single rat plunged into the swirling water and drowned.

Hamelin was saved! But when the piper went to the town hall to claim his rightful fee, the greedy Mayor laughed in his face, saying, "A thousand gold coins for playing a simple tune? Ridiculous! Take fifty coins, or leave empty-handed!"

The piper's eyes flashed with quiet anger. He gave a final warning and walked out. On Saint John's Day, while the adults were gathered in church, the piper returned. This time, he played a sweet, magical tune of enchanting beauty.

Instantly, all the children of Hamelin came running out of their homes, laughing and dancing behind the piper. He led the procession toward Koppen Mountain. A great doorway opened in the rocky cliffside, the piper and the children marched inside, and the mountain closed forever behind them. Only one lame boy who could not keep pace was left behind to tell the grief-stricken townspeople the terrible price of their broken promise."""
    },
    14: {
        "moral": "United we stand, divided we fall / Unity is strength.",
        "continuation": """Realizing that his days on earth were numbered, the wise old farmer devised a practical lesson to teach his quarrelling sons the supreme value of harmony. He summoned all four sons to his bedside and asked a servant to bring a bundle of thick wooden sticks tied securely with rope.

The father handed the bundle to his eldest son and said, "My son, use all your strength and try to break this bundle." The strong young man pulled and strained with all his might, but the bundle remained intact. One by one, the other three brothers tried, but none could snap even a single twig while they were bound together.

Then the old farmer smiled gently and instructed, "Now, untie the rope and hand one single stick to each brother."

The sons did so. "Now break your sticks," the father commanded. With minimal effort, each son snapped his individual stick in two with a simple crack.

The wise father looked tenderly into their eyes and explained, "My dear sons, learn this vital truth from these sticks. As long as you remain united in brotherhood and stand by one another, no enemy on earth can cause you harm. But if you quarrel and drift apart into isolated individuals, your adversaries will break you as easily as you broke those single twigs."

The lesson struck deep into the hearts of the four sons. They embraced with tears of regret, promised never to quarrel again, and lived in peaceful cooperation."""
    },
    15: {
        "moral": "Greed leads to utter ruin / Grasp all, lose all.",
        "continuation": """Holding the stolen chunk of juicy meat firmly between his jaws, the greedy dog looked down into the clear, tranquil water of the stream beneath the wooden bridge.

To his surprise, he saw his own reflection mirrored in the smooth surface. Being a foolish and covetous beast, he mistook the image for another dog carrying an even larger and juicier piece of meat.

His insatiable greed took over his senses. He thought, "If I attack that dog and seize his meat, I will have a double feast today!"

Without thinking of the consequences, he opened his mouth wide and barked fiercely at his reflection: "Woof!"

The moment his jaws opened, his own precious piece of meat slipped from his mouth, plunged into the rushing current with a splash, and sank straight to the bottom of the river.

The foolish dog stared at the empty ripples in disbelief. Not only did he fail to get the second piece, but he lost what he already possessed. He hung his head in bitter disappointment and walked away hungry, having paid the penalty for his greed."""
    },
    16: {
        "moral": "Distrust advice that stems from another person's misfortune.",
        "continuation": """The tailless fox walked onto the platform and addressed the gathering of forest foxes with an air of great authority: "Respected brothers and sisters, why do we drag these long, heavy, bushy tails behind us all our lives? They are dirty, cumbersome when running from hunters, and completely useless. I have cut off my own tail, and I feel extraordinarily light, elegant, and agile! I strongly advise every wise fox among you to chop off your tails immediately."

Many young and inexperienced foxes were almost persuaded by his smooth speech and began looking at their own tails with doubt.

However, an old, experienced fox with a silver muzzle stepped forward, looked at the speaker, and said with a sarcastic smile: "My cunning friend, you speak very eloquently of fashion and agility. But tell us truthfully: would you be offering us this generous advice if you had not accidentally lost your own tail in a steel trap?"

The tailless fox turned red with embarrassment and could not utter a word in reply. The entire assembly of foxes erupted into loud laughter and chased the deceitful creature out of the woods. His selfish trick had failed completely."""
    },
    17: {
        "moral": "Greed brings disaster / Grasp all, lose all.",
        "continuation": """The poor farmer and his wife sold the gleaming golden egg every morning at the village market. Within a few months, their dilapidated hut was replaced by a fine brick house, and they possessed ample wealth and livestock.

However, the wife became increasingly consumed by impatience and boundless greed. She complained, "Waiting twenty-four hours for a single egg is agonizingly slow. This wonderful bird must surely have a vast reservoir of solid gold hidden inside its belly. Why should we wait for days and months when we can become millionaires in a single instant?"

The farmer was initially hesitant, but his wife's persistent persuasion overpowered his judgment. One morning, driven by blind cupidity, they took a sharp kitchen knife and slit open the stomach of the extraordinary goose.

To their horror and heartbreak, they found nothing inside except ordinary organs and blood, exactly like any common fowl. There was no secret hoard of gold whatsoever.

The wonderful goose lay dead on the floor, never to lay another golden egg again. The foolish couple wept bitterly, realizing that their impatient greed had destroyed their source of permanent prosperity and plunged them back into poverty."""
    },
    18: {
        "moral": "Honesty shines brightest in poverty and is always rewarded.",
        "continuation": """Rafiq carried the heavy leather bag inside his modest tin-roofed shack. His heart beat wildly as he unzipped it and found stacks of currency notes totaling two lakh taka alongside dazzling gold ornaments. At that very moment, his young daughter was burning with fever and coughing in the corner, with no money for proper medicine.

For a split second, a tempting thought whispered in his mind that this fortune could cure his child and change his destiny forever. But Rafiq's pious conscience immediately rejected the dishonest impulse. "This wealth does not belong to me," he whispered firmly. "I will not feed my family with stolen sustenance."

Searching through the pockets of the bag, he discovered a business visiting card bearing a doctor's name and residential address in Dhanmondi. Early the next morning, Rafiq paddled his rickshaw across the city and knocked on the gates of the gentleman's residence.

The owner, a retired government officer, was weeping with anxiety, believing his life's savings were lost forever. When Rafiq handed over the bag untouched, the gentleman and his wife were stunned beyond words.

Tears streaming down his face, the gentleman embraced the humble rickshaw puller. He rewarded Rafiq with fifty thousand taka, took full responsibility for his daughter's medical treatment in a specialized hospital, and bought him an auto-rickshaw to secure his family's livelihood. Rafiq's uncompromising integrity proved that honesty is the true crown of human dignity."""
    },
    19: {
        "moral": "When two parties quarrel blindly, a cunning third party reaps the harvest.",
        "continuation": """Unable to settle the division of the stolen bread, the two foolish cats agreed to accept the sly monkey as their impartial judge. The monkey brought out a pair of brass scales and broke the bread into two pieces, intentionally making one piece noticeably larger than the other.

He placed the pieces on the opposite pans. Naturally, the heavier side tipped the balance downward. "Ah, this piece is heavier," observed the monkey with an air of grave concern. "Let me bite off a little to make them equal."

He took a greedy bite from the larger piece and chewed it deliberately. But now, that side became lighter than the other! "Dear me, now the second piece is heavier," said the monkey, biting off a chunk from the other half.

The process repeated itself again and again. The two cats watched with growing alarm as their loaf of bread shrank with every bite into tiny crumbs.

Finally, the cats pleaded, "Sir Judge, please stop! We are satisfied with whatever small portions remain. Give them back to us."

The monkey laughed mockingly, "I have wasted my precious time and legal expertise to settle your dispute. The remaining crumbs are my rightful judicial fee!" With that, he popped the last pieces into his mouth and scampered up a tree, leaving the two foolish cats hungry and regretful."""
    },
    20: {
        "moral": "Even the smallest friend can render immense help to the mighty.",
        "continuation": """The tiny mouse had pleaded for its life, saying, "O King of the jungle, spare my humble life! Someday, I may be able to repay your mercy." The mighty lion had laughed heartily at the ridiculous idea that a little rodent could ever help the monarch of beasts, but he generously lifted his paw and let it go free.

A few months later, the lion was roaming the forest when he stepped into a hunter's snare. Thick, sturdy hemp ropes snapped shut around him, pulling him up against a tree trunk. The lion roared in furious rage, thrashing with all his tremendous power, but the heavy ropes only tightened around his limbs. Exhausted, he let out deep roars of despair.

The little mouse recognized the roar of its benefactor from afar. It scurried swiftly through the bushes and found the trapped lion in agony. "Do not fear, noble King," squeaked the mouse. "I will set you free!"

Using its razor-sharp teeth, the mouse began gnawing diligently at the thick knots. Thread by thread, strand by strand, it severed the heavy cords. Within half an hour, the entire net fell apart, and the lion stepped out into freedom.

The majestic lion looked down at his tiny savior with profound gratitude. He learned that no creature is too small to be valuable, and true kindness is never wasted."""
    },
    21: {
        "moral": "Devotion to parents is the highest religious and moral duty.",
        "continuation": """Shravan Kumar gently rested the shoulder sling carrying his blind parents beneath the cool shade of a tree in the forest of Ayodhya. Hearing their faint whispers of parched thirst, he took an earthen pot and walked quietly to the bank of the Sarayu River.

As he plunged the pot beneath the surface, the water filled it with a distinct gurgling sound: "Ghar... ghar..."

Nearby, King Dasharatha of Ayodhya was hunting in the dense forest. The king possessed the unique skill of shooting arrows guided solely by sound (Shabdabhedi Bana). Mistaking the gurgling noise for a wild elephant or deer drinking water in the dark, the king released a deadly hunting arrow.

The arrow pierced Shravan Kumar's chest with fatal precision. A agonizing cry of human distress echoed through the woods: "Ah! My poor parents! Who will give them water now?"

Horrified, King Dasharatha rushed through the bushes and found the dying youth bathed in blood. Overwhelmed with remorse, the king knelt beside him weeping. Shravan Kumar looked up with fading eyes and whispered, "O King, I do not grieve for my own life. But my aged, blind parents are waiting under yonder tree, dying of thirst. Please take this water to them before you tell them of my death."

With those selfless words on his lips, Shravan Kumar breathed his last. His supreme filial love has remained an eternal symbol of devotion throughout the ages."""
    },
    22: {
        "moral": "Truthfulness is a divine shield that disarms the fiercest evil.",
        "continuation": """The caravan of merchants had not traveled far across the lonely desert when a fierce gang of heavily armed robbers ambushed them. The bandits brandished swords, beat the travelers, and plundered all their merchandise, gold, and baggage.

One of the robbers approached young Abdul Quader, who was standing quietly by his camel. Seeing the boy in simple clothes, the bandit asked casually, "Hey boy, do you have anything of value with you?"

Young Abdul Quader replied calmly and fearlessly, "Yes, I have forty gold dinars."

The robber laughed, thinking the boy was joking, and walked away. Soon, a second robber asked the same question, and Abdul Quader gave the identical reply. Perplexed, the bandits brought the truthful boy before their ruthless gang leader.

The chief glared down and barked, "Is it true that you possess gold coins?"

Abdul Quader unbuttoned his coat and pointed to the inner lining, where forty gleaming dinars were sewn securely. The chief was astonished. "Why did you reveal your hidden treasure when no one would ever have searched your humble coat?"

Abdul Quader replied with serene conviction, "When leaving home, my beloved mother made me promise never to tell a lie, no matter the danger. How could I disobey my mother and commit a sin before Almighty Allah for the sake of mere gold?"

The boy's words struck the hardened robber chief like a bolt of lightning. Tears flowed down his rugged cheeks. "Alas!" the chief cried out. "A young child remains so steadfast in his promise to his mother, while I have spent my entire life violating the laws of my Creator!"

Overcome with remorse, the chief fell at the boy's feet, repented sincerely, returned every item of stolen wealth to the merchants, and disbanded his criminal gang to lead a righteous life."""
    },
    23: {
        "moral": "Worldly wealth cannot buy genuine happiness or replace true love.",
        "continuation": """Realizing that his touch brought death to everything he loved, King Midas spent the darkest night of his life weeping beside the golden statue of his daughter Marigold. The cold glimmer of the gold mocked his helplessness. He felt the gnawing pangs of starvation and the dry torment of dehydration, but dared not touch any morsel.

When morning dawned, the god Dionysus reappeared in the palace hall. Midas flung himself upon the floor, clutching the god's feet. "I am cured of my madness!" he cried out in broken sobs. "Take all my kingdom, take my crown, strip me of every ounce of gold, but give me back my living, breathing daughter!"

The god smiled compassionately, seeing that the king's heart had been thoroughly cleansed of the poison of greed. He directed him to the sacred spring of Pactolus in the mountains.

Midas ran barefoot up the rocky trails, reached the source, and submerged his head into the rushing waters. A visible golden essence washed away from his fingertips into the river sands, leaving the waters permanently laced with gold dust.

He filled an earthen jar with the river water and raced back to the palace. With trembling hands, he sprinkled the drops over Marigold. Instantly, the golden stiffness melted away, the warm flush of life returned to her cheeks, and she opened her eyes, embracing her father with tears of joy. Midas discarded all golden decorations from his life and lived in joyful simplicity."""
    },
    24: {
        "moral": "If you try to please everyone, you will end up pleasing no one.",
        "continuation": """As the miller and his son walked beside the donkey, a group of village women laughed, "Look at those fools! Walking on foot when they have a sturdy donkey to ride!" Hearing this, the miller placed his young son on the donkey's back while he walked alongside.

A mile down the road, some elderly men criticized, "What a disrespectful youth! Riding comfortably while his poor, aged father trudges in the dust!" Ashamed, the boy dismounted, and the miller climbed onto the animal's back.

Further ahead, a group of travelers cried out, "Look at that cruel father! Lounging on the donkey while his little boy can barely keep up!" Wanting to please them, the miller pulled his son up behind him so both rode together.

Near the town gate, a townsman shouted indignantly, "What heartless cruelty! Overloading that poor, exhausted beast! You two are better suited to carry the donkey than have it carry you!"

Perplexed and desperate to satisfy public opinion, the father and son tied the donkey's legs to a long pole and raised it onto their shoulders. As they carried the struggling animal across a wooden bridge, the crowd burst into roars of mocking laughter.

Frightened by the commotion, the donkey kicked violently, broke the ropes, fell over the railing into the deep river, and drowned. The miller and his son returned home empty-handed, learning the bitter lesson that compromising one's own judgment to satisfy idle gossip leads to total disaster."""
    },
    25: {
        "moral": "True wisdom is thoughtful of others, whereas superficial mockery reveals ignorance.",
        "continuation": """The foolish youth chuckled arrogantly and blocked the blind man's path. "Hey old man, you have no sight in your eyes! Daylight and midnight are both pitch black to you. Why on earth do you carry a burning lamp? Are you out of your mind?"

The blind man smiled with serene calmness, set down his heavy pitcher for a moment, and replied softly: "My dear young friend, it is true that this burning lamp cannot give sight to my blind eyes. But I carry it not for myself, but for thoughtless and careless people like you. In this pitch-black night, you might not notice a blind man walking in the shadows, and in your carelessness, you might collide with me, break my earthen pitcher, and spill my precious water."

The words struck the boastful youth like a whip. He felt his cheeks burn with shame as he realized the depth of the blind man's foresight and his own shallow foolishness. He lowered his head, apologized sincerely for his insolent mockery, and assisted the wise man safely across the dark street."""
    },
    26: {
        "moral": "Do not pay too high a price for trivial and fleeting desires.",
        "continuation": """Seven-year-old Benjamin returned home whistling with triumphant delight. However, when his older brothers and sisters saw the cheap toy, they asked him how much money he had paid for it.

When Benjamin proudly confessed that he had handed over every single copper penny in his pockets, they burst into loud laughter. They explained that the simple whistle was worth only a fraction of a penny and pointed out all the wonderful books, candies, and useful tools he could have bought with the rest of his coins.

Benjamin felt so mortified that he burst into tears of humiliation. The thought of his foolish purchase caused him far more sorrow than the whistle ever brought him joy.

However, Benjamin Franklin never forgot that childhood lesson. Throughout his illustrious career as a statesman, scientist, and philosopher, whenever he observed people sacrificing their health for fleeting pleasure, accumulating unnecessary luxuries, or compromising their honor for cheap political fame, he would say to himself: "Alas, that man is paying far too much for his whistle!" The lesson taught him prudent stewardship and wise judgment for life."""
    },
    27: {
        "moral": "Failure is the pillar of success / Never give up.",
        "continuation": """Six times King Robert Bruce had marshaled his loyal troops against the mighty army of the English king, and six times his forces had been crushed. Exiled, hunted, and broken in spirit, Bruce lay in a damp, isolated cave, questioning whether freedom was truly achievable.

His gaze fell upon a tiny spider attempting to cast its silk thread across a wide fissure in the rocky ceiling to weave its web. The tiny creature swung forward with all its energy, but fell short and tumbled down. It climbed back up and tried a second time—only to fail again.

Bruce watched with mounting fascination. Three, four, five, six times the persistent spider leaped into empty air, and six times it slipped and fell—mirroring Bruce's own six heartbreaking military defeats.

"Surely the creature will give up in despair," Bruce whispered.

Instead, the tiny spider rested for a moment, gathered all its remaining vitality, and sprang forward for the seventh time. With supreme tenacity, the silk thread caught the opposite ledge, anchored firmly, and the spider began weaving its web in triumph.

A surge of electrifying determination swept through Bruce's soul. "If a tiny, fragile insect can conquer failure on its seventh attempt, shall a King of Scotland surrender?" he cried aloud.

Bruce emerged from the cave, rallied the clans of Scotland, and met the English army at the historic Battle of Bannockburn. Inspired by their king's indomitable spirit, the Scottish warriors won a decisive victory and established their nation's independence."""
    },
    28: {
        "moral": "Contentment and peace of mind are far more precious than gold.",
        "continuation": """The poor cobbler took the heavy bag containing a hundred shiny gold coins home and hid it under the floorboards beneath his bed. But that very night, a strange transformation overcame his peaceful life.

Every rustle of the wind outside sounded like a burglar attempting to break into his hut. He tossed and turned in agony, unable to sleep for fear of being robbed. The following morning, he was too suspicious to sing his cheerful songs, fearing his neighbors would guess he had hidden treasure. Day by day, his cheerful smile vanished, replaced by anxiety, suspicion, and dark circles under his eyes.

After a week of sleepless misery, the cobbler could bear the burden no longer. He dug up the bag of gold coins and rushed straight back to the rich banker's mansion.

Placing the bag on the mahogany desk, the cobbler said with deep relief: "Respected Sir, take back your hundred gold coins! I was poor, but I was happy, healthy, and slept like a king. Your gold brought me sleepless nights and constant fear. Keep your fortune, and give me back my carefree songs and sweet, tranquil sleep!" The cobbler walked out singing, having realized that true wealth resides in a peaceful conscience."""
    },
    29: {
        "moral": "Practical knowledge and life-saving skills are superior to bookish pride.",
        "continuation": """The scholar smirked haughtily at the humble boatman and asked, "Tell me, have you ever studied astronomy or the movement of celestial bodies?"

"No, sir, I am an illiterate boatman," the humble man replied. "Alas!" the scholar declared pompously. "One quarter of your life is utterly lost!"

A little later, the scholar asked, "Do you know anything about geology or the ancient history of nations?" The boatman shook his head in ignorance. "Then half of your life is completely wasted!" said the scholar with disdain.

Suddenly, dark storm clouds engulfed the sky. Fierce gales whipped across the river, generating towering waves that violently tossed the small wooden boat. Within moments, a giant swell struck the vessel, cracking its wooden hull. Water rushed in rapidly, and the boat began to capsize in the middle of the turbulent river.

The boatman stripped off his shirt and turned to the trembling scholar, whose face was pale with terror. "Sir!" shouted the boatman above the roar of the tempest. "Do you know how to swim?"

"No! No! I never learned to swim! Please save me!" cried the helpless scholar.

The boatman dived into the surging water, shouting back: "Then, respected scholar, your entire life is lost!" Practical survival skills proved far more valuable than academic arrogance."""
    },
    30: {
        "moral": "Idleness brings bitter misery; industry today secures tomorrow.",
        "continuation": """All through the warm, sunny days of summer and autumn, the carefree grasshopper hopped from blade to blade, singing merry songs and mocking the tiny ants who marched tirelessly back and forth under the scorching heat, carrying heavy grains of wheat into their underground storehouses.

"Why waste your precious youth toiling so hard?" the grasshopper laughed. "The world is full of green leaves and sweet sunshine! Come, sing and dance with me!" The wise ants ignored his banter and continued their diligent labor.

Soon, harsh winter arrived. Bitter frost covered the meadows, freezing snow buried every plant, and an icy wind swept through the leafless forest. The grasshopper found himself shivering with cold and starving with hunger. He searched desperately, but could not find a single leaf or grain.

Perishing from exhaustion, he crawled to the warm ant colony and knocked on the door, begging for a few crumbs to save his life.

An ant peered out from the cozy burrow and asked, "What were you doing during the long, bountiful months of summer when food was abundant?"

"I was too busy singing and enjoying the music," admitted the weeping grasshopper.

"Well," the ant replied sternly, "since you sang and danced all summer, you may go and dance the winter away!" and shut the door. The grasshopper learned too late that foresight and hard work are the only guarantees against ruin."""
    },
    31: {
        "moral": "Honesty and moral integrity in poverty are the true marks of nobility.",
        "continuation": """Sumona picked up the sleek, expensive smartphone lying on the pavement near the bus stop. As she held the high-end device, her classmates urged her to sell it in the market, pointing out that the money could buy new school uniforms and pay off several months of overdue school tuition fees.

However, Sumona's upright conscience refused to entertain such dishonesty. She navigated the lock screen and dialed the emergency contact labeled "Home".

A tearful, anxious voice answered. It was the owner, a senior university professor who had dropped the phone containing irreplaceable research manuscripts and international conference data. He gave her his address, and Sumona immediately traveled across town to return the device personally.

When the professor inspected the phone and found everything intact, he was moved to tears by the young girl's uncompromising integrity. Learning about her impoverished family background and her stellar academic record, the professor did not merely hand her a cash reward. Instead, he formally established an educational sponsorship that covered all her high school and college expenses through university graduation. Sumona's honesty transformed her future and inspired her entire community."""
    },
    32: {
        "moral": "Heroic courage and compassion recognize no barrier of age.",
        "continuation": """Fourteen-year-old Ripon was walking along the river embankment when a sudden winter gale capsized an old boatman's skiff in the freezing, turbulent waters. The elderly man was thrashing helplessly in the icy current, his strength rapidly failing as hypothermia set in.

Several adults stood on the bank shouting in panic, but none dared to plunge into the freezing river.

Without a second thought, Ripon kicked off his shoes, tore off his jacket, and dived headfirst into the icy depths. The freezing water felt like thousands of needles piercing his flesh, but his focus remained entirely on the drowning boatman.

Swimming with ferocious determination against the powerful current, Ripon reached the sinking man just as his head went under. Gripping the old man securely under his arm, Ripon paddled with all his might toward the embankment.

The onlookers leaned down from the pier, caught their hands, and pulled both safely onto dry land. Villagers wrapped them in blankets and lit a warm fire. Ripon's fearless selflessness saved a human life and earned him widespread admiration and a national bravery commendation."""
    },
    33: {
        "moral": "Self-reliance is the true foundation of human dignity and lasting success.",
        "continuation": """Kamal refused to join the crowds of unemployed graduates wandering aimlessly through city streets chasing elusive clerical jobs. Recognizing that modern technology creates immense practical demand, he enrolled in a six-month government technical training program in electronics, smartphone servicing, and solar panel installation.

He studied with relentless dedication, mastered hardware diagnostics, and returned to his village. With a modest loan from a rural cooperative bank, he rented a tiny corner stall in the village bazaar and opened a repair workshop named "Kamal Technical Services."

His punctuality, transparent pricing, and polite behavior quickly won the trust of local villagers. Within two years, his small stall expanded into a full-fledged technical training center where he employed and trained five other disadvantaged youths from his neighborhood.

Kamal cleared his debts, built a brick home for his aging parents, and established himself as a respected entrepreneur in the upazila. His life proved that dignity lies not in waiting for handouts, but in developing practical skills and building one's own destiny through self-reliance."""
    },
    34: {
        "moral": "Wealth is a fleeting test; wisdom, charity, and foresight turn it into eternal blessing.",
        "continuation": MODEL_STORY_LUCKY_TICKET["full_story"]
    }
}

# Complete 32 Dialogues with full 8-12 turn scripts mapped by ID
DIALOGUES_EXTRAS = {
    1: {
        "script": """Sadi: Assalamu Alaikum, Rafi. How are you doing today?
Rafi: Wa Alaikum Assalam, Sadi. I am fine, but I am feeling quite depressed about my English test results.
Sadi: What happened? Did you get lower marks than you expected?
Rafi: Yes, my score was very disappointing. I find English extremely challenging, especially grammar and free-hand writing.
Sadi: Don't lose heart, my friend. English is a language, not a monster. If you follow a methodical approach, you can easily master it.
Rafi: That sounds encouraging! Could you please guide me on how to improve?
Sadi: Certainly. You must focus on developing all four basic language skills simultaneously: listening, speaking, reading, and writing.
Rafi: How can I improve my listening and speaking skills at home?
Sadi: You can listen to English news on BBC or watch educational podcasts. And most importantly, let us practice speaking English together every day for at least twenty minutes.
Rafi: But what if I make grammatical mistakes while speaking?
Sadi: Making mistakes is an essential part of learning. Never feel shy. To enrich your vocabulary and writing, read English newspapers daily and write a short paragraph every evening.
Rafi: That is a very practical and structured plan, Sadi! I will start implementing it from today.
Sadi: Excellent! Consistency is the key to fluency. You will surely achieve an A+ in no time."""
    },
    2: {
        "script": """Shafi: Hello Nafi, how are you?
Nafi: Hello Shafi. I'm good, thanks. Were you able to attend today's online English class?
Shafi: Yes, I attended through Zoom. Our teacher explained the grammar rules very clearly using interactive slides.
Nafi: Online education has certainly revolutionized learning. What do you consider its greatest benefits?
Shafi: The biggest advantage is flexibility and safety. Students can attend lectures from the comfort of their homes, saving valuable commuting time and transport expenses.
Nafi: That's true. Moreover, recorded lectures allow students to review difficult topics multiple times before exams.
Shafi: Exactly. But we must also acknowledge its serious drawbacks. What challenges do you face?
Nafi: Poor internet connectivity and high data costs in rural areas create a digital divide. Many poor students cannot afford expensive smartphones.
Shafi: Furthermore, continuous staring at screens causes eye strain, headaches, and physical lethargy among students.
Nafi: Also, the real interactive environment and discipline of a physical classroom cannot be entirely replaced by a virtual screen.
Shafi: I completely agree with you. A blended approach combining physical classes with digital resources is ideal for our education system.
Nafi: Well said, Shafi. Thank you for sharing such balanced thoughts."""
    },
    3: {
        "script": """Rashed: Assalamu Alaikum, Fahim. What are you reading so intently?
Fahim: Wa Alaikum Assalam, Rashed. I am reading today's issue of 'The Daily Star'.
Rashed: Do you read English newspapers every single day?
Fahim: Yes, I do. Reading newspapers has become a daily habit for me.
Rashed: Why do you attach so much importance to reading newspapers? Isn't our textbook syllabus enough?
Fahim: Textbooks provide theoretical knowledge, but newspapers provide practical and current knowledge of the entire globe.
Rashed: How does it help a secondary school student specifically?
Fahim: It keeps us informed about international politics, scientific breakthroughs, sports, commerce, and national policies.
Rashed: Does it also assist in learning English language skills?
Fahim: Immensely! Reading standard articles enriches our vocabulary, exposes us to modern idioms, and improves our sentence construction.
Rashed: I realize now how much I have been missing by neglecting the daily news.
Fahim: A person who does not read newspapers remains like a frog in a well, completely ignorant of the world outside.
Rashed: Thank you, Fahim, for opening my eyes. I will subscribe to a good English daily from this very week."""
    },
    4: {
        "script": """Amin: Hello Masum, how is your preparation going for the upcoming SSC examination?
Masum: Hello Amin. My preparation is fairly good, but with exams knocking at the door, I am feeling a bit nervous.
Amin: Feeling slightly anxious is quite natural, but you must not let panic overwhelm your confidence. How far have you completed your syllabus?
Masum: I have revised Bengali, Science, and Mathematics thoroughly. However, I still feel somewhat weak in English 1st and 2nd Paper.
Amin: Which specific areas in English are causing you difficulty?
Masum: Completing stories, rearranging sentences, and remembering right forms of verbs.
Amin: For completing stories, memorize the standard plots and focus on writing clean, grammatically correct continuations with suitable titles. And for grammar, solve board question papers from 2020 to 2026 daily.
Masum: That is a wonderful suggestion! How many hours are you studying every day?
Amin: I study around eight hours daily, following a disciplined routine with adequate breaks. I also practice writing answers within the exam time limit.
Masum: Time management during the exam is indeed crucial. I will follow your revision strategy and practice previous board papers.
Amin: Best of luck, Masum. Let us pray for each other so we can both secure GPA 5.00 brilliantly!
Masum: Thank you, Amin. Best of luck to you too!"""
    },
    5: {
        "script": """Two Friends:
Fahad: Assalamu Alaikum, Tanvir. Did you read the alarming medical report on tobacco consumption in today's newspaper?
Tanvir: Wa Alaikum Assalam. Yes, Fahad, it states that smoking kills thousands of citizens in Bangladesh every single month.
Fahad: It is heartbreaking to see so many young teenagers taking up smoking out of peer pressure or curiosity.
Tanvir: Absolutely. They fail to realize that cigarette smoke contains over four thousand toxic chemicals, including lethal nicotine, carbon monoxide, and tar.
Fahad: What fatal health hazards does smoking cause to human organs?
Tanvir: Smoking directly damages the lungs, causing lung cancer, chronic bronchitis, and emphysema. It also increases the risk of heart attacks and brain strokes tenfold.
Fahad: What about passive smoking? Non-smokers suffer just as severely when exposed to secondhand smoke in public places.
Tanvir: Exactly! Pregnant women, infants, and elderly people are victimized without having ever touched a cigarette.
Fahad: Don't you think the government should strictly enforce a nationwide ban on public smoking and tobacco advertisements?
Tanvir: Definitely! Sale of cigarettes near educational institutions must be outlawed with heavy fines, and massive public awareness campaigns must be launched.
Fahad: Furthermore, high taxation should be imposed on tobacco products to discourage young buyers.
Tanvir: Let us raise our voices and counsel our peers to make our campus completely smoke-free. Thank you for this vital talk, Fahad."""
    },
    6: {
        "script": """Nazrul: Assalamu Alaikum, brother.
Bookseller: Wa Alaikum Assalam, young man. Welcome to our bookshop. How can I assist you today?
Nazrul: I am looking for a communicative English guide and model test book for the SSC Examination 2027.
Bookseller: We have several reputed publications in stock. Are you looking for any specific author or publication?
Nazrul: I need a book that covers the revised national curriculum, contains chapter-wise explanations, and includes solved board question papers from recent years.
Bookseller: Here is the latest edition of 'Dakhil & SSC Communicative English with Exclusive Model Tests'. It is highly recommended by experienced teachers.
Nazrul: May I examine the book for a few moments?
Bookseller: Certainly, take your time and check the table of contents and question patterns.
Nazrul: The layout looks very structured and comprehensive. It includes all 34 completing stories and 32 dialogues. What is the printed price?
Bookseller: The printed price is 450 Taka, but we offer a special student discount of twenty percent. So it will cost you 360 Taka only.
Nazrul: That is very fair. Please pack this book for me along with a good ballpoint pen.
Bookseller: Here is your book and the memo, brother.
Nazrul: Thank you very much for your courteous service.
Bookseller: You are most welcome. Wish you brilliant success in your exams!"""
    },
    7: {
        "script": """Sakib: Hello Tahmid, what are you doing with those small saplings in your garden?
Tahmid: Hello Sakib! I am planting fruit and timber saplings around our courtyard.
Sakib: That is wonderful! But why are people emphasizing tree plantation so urgently nowadays?
Tahmid: Because trees are our greatest life-savers. Without trees, human existence on Earth would be entirely impossible.
Sakib: Could you elaborate on how trees maintain our ecological balance?
Tahmid: Trees absorb poisonous carbon dioxide from the atmosphere and release pure oxygen, which we breathe every second.
Sakib: They also provide us with food, timber, and medicinal herbs, don't they?
Tahmid: Yes! Beyond that, trees prevent soil erosion, shield our coastal belt from deadly cyclones, and induce rainfall to prevent droughts.
Sakib: Yet reckless deforestation is destroying our forests at an alarming rate across the globe.
Tahmid: That is why global warming, erratic weather, and rising sea levels are threatening our country so severely.
Sakib: What should we do as responsible students to counter this disaster?
Tahmid: We must observe tree plantation weeks, plant trees in every empty space around our homes and schools, and motivate our community.
Sakib: I will join you right now and plant three saplings in my backyard as well!
Tahmid: Wonderful decision, Sakib. Let us make our Mother Earth green again."""
    },
    8: {
        "script": """Kamal: Hello Jamal, where are you rushing off to in such a hurry?
Jamal: Hello Kamal. I am heading to my spoken English club.
Kamal: Spoken English? Why are you dedicating so much extra time to English when we already study it at school?
Jamal: Because English is not merely an academic examination subject; it is the universal international language of the modern world.
Kamal: In what ways is English indispensable for our future career?
Jamal: English is the global passport. More than eighty percent of the world's scientific, technological, and medical research is published in English.
Kamal: What about higher education and overseas employment?
Jamal: If you wish to pursue higher degrees at prestigious domestic or foreign universities, proficiency in English is an absolute prerequisite.
Kamal: Furthermore, in multinational corporations, IT sectors, and international commerce, English is the primary medium of communication.
Jamal: Exactly! Even online freelancing and international outsourcing require fluent English communication skills.
Kamal: Without a solid command of English, a person remains isolated from the modern global knowledge economy.
Jamal: You have summarized it perfectly. Would you like to join our spoken English practice session today?
Kamal: Yes, I would love to! Let us walk together toward the club."""
    },
    9: {
        "script": """Rana: Hello Ripon, what were you discussing with our headmaster earlier today?
Ripon: Hello Rana. We were discussing the problem of illiteracy in our neighboring village and how we can organize a youth campaign to eradicate it.
Rana: Illiteracy is indeed one of the gravest curses holding our country back from true development.
Ripon: You are completely right. An illiterate person is like a blind individual in a civilized society, unable to read basic notices or understand civic rights.
Rana: How does illiteracy directly impede our economic progress?
Ripon: Illiterate citizens struggle to adopt modern agricultural technology, hygiene practices, and vocational training, keeping poverty alive.
Rana: What practical measures should we undertake to eradicate this curse?
Ripon: First, primary education must be enforced strictly so that no child drops out of school due to poverty.
Rana: What about adults who missed schooling in their childhood?
Ripon: We should set up free night schools in village primary school buildings where educated youths like us can teach them basic reading, writing, and arithmetic.
Rana: That is a noble initiative! We can also distribute free books and conduct community awareness meetings.
Ripon: The government, non-governmental organizations, and students must unite like an army to wipe out illiteracy.
Rana: Count me in, Ripon. I will gladly volunteer my evenings to teach at the night school!"""
    },
    10: {
        "script": """Farhan: Assalamu Alaikum, Nayeem. I noticed you recently bought a new smartphone.
Nayeem: Wa Alaikum Assalam, Farhan. Yes, my father purchased it for my online classes and educational research.
Farhan: Modern mobile phones are truly marvelous technological inventions. What useful purposes do you use it for?
Nayeem: It acts like a portable computer. I can access dictionary apps, watch educational YouTube tutorials, read PDFs, and stay connected with teachers via study groups.
Farhan: It also enables instant communication with family members during emergencies from any corner of the globe.
Nayeem: However, I have noticed many of our classmates misusing their phones terribly.
Farhan: That is the dangerous abuse of technology. Excessive mobile gaming and social media scrolling consume valuable study hours and disrupt healthy sleep.
Nayeem: Furthermore, continuous screen exposure causes serious eye damage, finger joint strain, and mental anxiety.
Farhan: Some youngsters even fall victim to cybercrime, inappropriate content, and digital addiction.
Nayeem: Mobile phones are great servants, but terrible masters. Everything depends on how wisely we utilize them.
Farhan: True words. We must maintain strict digital discipline and limit our screen time to productive educational tasks only.
Nayeem: I completely agree with your wise advice, Farhan."""
    },
    11: {
        "script": """Sabbir: Hello Tanvir, why do you look so disturbed today?
Tanvir: Hello Sabbir. During today's test, two students in our hall were expelled for copying from unauthorized notes.
Sabbir: It is deeply shameful. Copying in the examination has become an infectious moral disease among certain students.
Tanvir: Why do students resort to such shameful unfair means instead of studying honestly?
Sabbir: Mainly due to laziness, lack of consistent preparation throughout the year, and an unhealthy obsession with marks rather than real learning.
Tanvir: What disastrous consequences does copying bring upon a student's future?
Sabbir: An unfair certificate obtained by copying is completely worthless. Such a student possesses no genuine knowledge and fails miserably in job interviews and practical life.
Tanvir: Moreover, it destroys their personal integrity, self-respect, and moral character.
Sabbir: Exactly! A nation whose students cheat in exams can never produce competent doctors, honest engineers, or capable leaders.
Tanvir: What steps should be taken to eliminate copying entirely from our examination centers?
Sabbir: Exam halls must be monitored strictly with CCTV surveillance, invigilators must remain incorruptible, and strict legal penalties must be enforced.
Tanvir: Most importantly, students must be taught that an honest failure is a thousand times more honorable than a dishonest pass.
Sabbir: Brilliantly stated, Tanvir. Let us always uphold honesty in every exam we write."""
    },
    12: {
        "script": """Asif: Hello Nabil, our SSC examination will be over next month. Have you thought about your future plan of life?
Nabil: Hello Asif! Yes, I have been contemplating my future goals very seriously.
Asif: What career path have you decided to pursue after completing school?
Nabil: I intend to get admitted into a reputed college in the Science group and eventually prepare for medical admission. My cherished dream is to become a doctor.
Asif: That is a remarkably noble profession! Why did you choose the medical profession specifically?
Nabil: Most of our rural villagers suffer terribly from lack of proper medical care and cannot afford costly private clinics in big cities. I want to establish a free clinic in my village and serve impoverished patients.
Asif: That reflects your deep patriotism and compassion, Nabil. What about you, Asif? What is your ambition?
Asif: My aim is to become an agricultural scientist. Bangladesh is an agrarian country, and developing climate-resilient crops is essential to ensure our national food security.
Nabil: That is an equally vital and patriotic goal! Both our ambitions are dedicated to the welfare of our country.
Asif: To achieve these dreams, we must first secure outstanding GPA 5.00 results in our SSC exams.
Nabil: Absolutely. Let us work with supreme dedication and turn our aspirations into reality."""
    },
    13: {
        "script": MODEL_TEST_DIALOGUE["dialogue_text"]
    },
    14: {
        "script": """Arman: Hello Joy, you look exceptionally energetic and refreshed this morning! What is the secret?
Joy: Hello Arman! The secret is very simple: I have made regular physical exercise an unbreakable part of my daily morning routine.
Arman: Do you exercise every single day? Isn't our busy study schedule exhausting enough?
Joy: On the contrary, physical exercise relieves study fatigue and recharges both body and mind.
Arman: In what ways does exercise benefit our health?
Joy: There is a famous proverb: 'A sound mind in a sound body.' Exercise improves blood circulation, strengthens our heart and muscles, and boosts our immune system against illnesses.
Arman: Does it also have a positive effect on academic performance?
Joy: Absolutely! Regular exercise stimulates brain cells, enhances concentration, improves memory retention, and relieves exam stress.
Arman: What kind of exercises do you practice?
Joy: I do twenty minutes of brisk jogging, light stretching, and play badminton or football in the afternoon.
Arman: I spend all my spare time sitting at my desk or looking at my mobile phone, which often leaves me feeling sluggish.
Joy: That sedentary lifestyle will ruin your health in the long run. Come join me for morning jogging tomorrow!
Arman: I definitely will! Thank you for motivating me toward a healthier life, Joy."""
    },
    15: {
        "script": """Hasib: Assalamu Alaikum, Maruf. What are you browsing on your laptop?
Maruf: Wa Alaikum Assalam, Hasib. I am searching for academic reference articles on the internet for my science project.
Hasib: The internet is undoubtedly the greatest milestone of modern information technology.
Maruf: Indeed. It has transformed the entire world into a global village. Any information you desire is available at the click of a button.
Hasib: What do you consider the primary advantages of the internet for students?
Maruf: We can access world-class digital libraries, watch free university lectures, learn foreign languages, and communicate instantly across continents.
Hasib: E-commerce, online banking, and remote work opportunities have also made human life incredibly convenient.
Maruf: Yet, the internet has many dark and destructive aspects if not used cautiously.
Hasib: What demerits are you referring to?
Maruf: Wasting hours on addictive video games, exposure to cyberbullying, theft of private data by hackers, and the rapid spread of toxic fake news.
Hasib: Continuous internet browsing also isolates youth from real-life social relationships and physical outdoor activities.
Maruf: Therefore, self-control and cyber awareness are mandatory. We should harness the internet as a tool for intellectual growth rather than a source of moral decay.
Hasib: True wisdom, Maruf. Technology should serve human progress, not human destruction."""
    },
    16: {
        "script": """Customer: Good morning, Sir. May I come in?
Bank Manager: Good morning! Please take a seat. How can I assist you today?
Customer: Thank you, Sir. I am an SSC student, and I wish to open a savings account with your bank to manage my scholarship money.
Bank Manager: That is a commendable initiative! Cultivating a savings habit at a young age is very wise. Opening a student savings account is quite simple.
Customer: What official documents will I need to submit with the application form?
Bank Manager: You will need two passport-sized photographs of yourself, a copy of your student ID card or birth registration certificate, and your school recommendation letter.
Customer: Do I also need to provide information about a nominee?
Bank Manager: Yes, certainly. You must designate a nominee—usually your father or mother—and submit one passport-sized photograph along with a copy of their National ID card.
Customer: What is the initial minimum deposit required to activate the account?
Bank Manager: For student accounts, the initial deposit is only five hundred Taka, and there are no hidden ledger maintenance fees.
Customer: Here is the filled application form along with all the required photocopies and photographs.
Bank Manager: Excellent. Everything is in order. Sign here at the bottom, please. Your account will be active by this afternoon, and we will issue your passbook and debit card.
Customer: Thank you very much for your kind cooperation, Sir!
Bank Manager: You are most welcome. Have a wonderful day!"""
    },
    17: {
        "script": """Patient: Good evening, Doctor. May I come in?
Doctor: Good evening. Please have a seat. What seems to be the problem?
Patient: Doctor, I have been suffering from a sudden high fever and shivering since yesterday evening.
Doctor: Let me check your temperature and pulse. Yes, your temperature is 103 degrees Fahrenheit. Are you experiencing any other symptoms?
Patient: I have an excruciating headache behind my eyes and severe pain in all my joints and muscles. My entire body feels broken.
Doctor: These symptoms of high fever, retro-orbital eye pain, and acute joint aches strongly suggest viral dengue fever. Have you noticed any red rashes on your skin?
Patient: No rashes yet, but I feel mild nausea and extreme physical weakness.
Doctor: Do not worry, but we must act vigilantly. I am prescribing an immediate Complete Blood Count (CBC) and Dengue NS1 Antigen test to check your platelet count.
Patient: Is it dangerous, Doctor?
Doctor: If detected early and managed properly, it is not dangerous. For now, take Paracetamol for the fever. Never take Aspirin or painkiller tablets, as they cause internal bleeding.
Patient: What should my diet be during this illness?
Doctor: Drink plenty of oral saline, green coconut water, fresh fruit juices, and clear soup to stay thoroughly hydrated. Complete bed rest is mandatory.
Patient: Thank you, Doctor. I will get the blood tests done immediately and report back with the results."""
    },
    18: {
        "script": """Helal: Assalamu Alaikum, Belal. You are up very early today!
Belal: Wa Alaikum Assalam, Helal. I always wake up before dawn. Early rising is my daily habit.
Helal: I find it terribly difficult to leave my warm bed early in the morning. What makes early rising so valuable to you?
Belal: There is an ancient and timeless rhyme: 'Early to bed and early to rise makes a man healthy, wealthy, and wise.'
Helal: How does it improve physical health?
Belal: In the early morning, the air is clean, fresh, and free from vehicle smoke and dust. Breathing that pure oxygen revitalizes our lungs and blood.
Helal: Does an early riser also get more productive study time?
Belal: Absolutely! The early morning atmosphere is remarkably peaceful and quiet. Whatever we memorize at that time registers permanently in our memory.
Helal: Moreover, an early riser has plenty of time to organize his entire day without rushing in panic.
Belal: Exactly. A late riser, on the other hand, wakes up hurried, misses breakfast, runs late for school, and remains tired and disorganized all day long.
Helal: I realize now why I always felt rushed and stressed. From tonight, I will sleep early so that I can rise at dawn.
Belal: That is a wonderful decision, Helal. You will experience the transformative magic of early rising within a single week."""
    },
    19: {
        "script": """Riyad: Hello Fahim, why are you sitting here looking so gloomy?
Fahim: Hello Riyad. The terminal exam is only two weeks away, and half my syllabus remains unstudied. I don't know how I will cover everything!
Riyad: You spent the entire term postponing your studies, playing video games, and idling away your days. Now you are paying the price.
Fahim: I deeply regret my laziness now. I never realized how fast time slips away.
Riyad: Remember the ancient proverb: 'Time and tide wait for none.' You can recover lost wealth through hard work, but lost time is gone forever.
Fahim: What should I do now to rescue my results?
Riyad: Stop wasting even a single second from this very moment. Prepare a realistic, hourly study routine for the next two weeks.
Fahim: How should I allocate my daily hours?
Riyad: Dedicate six hours to deep, focused study in the morning and evening, one hour for light revision, seven hours for restful sleep, and eliminate social media completely.
Fahim: Do you think punctuality and disciplined time management can still save my grades?
Riyad: Punctuality is the backbone of all great achievements. If you adhere strictly to your routine without procrastination, you can still achieve a respectable score.
Fahim: Thank you for your wake-up call, Riyad. I will respect every minute of my time from today onwards."""
    },
    20: {
        "script": """Sajib: Hello Munir, look at the thick blanket of grey smog hanging over the city today. Breathing has become so uncomfortable!
Munir: Hello Sajib. It is the tragic outcome of unchecked environmental pollution. Our environment is in grave peril.
Sajib: What are the primary forms of environmental pollution choking our country?
Munir: Air pollution, water pollution, and sound pollution are the three deadly demons destroying public health.
Sajib: What is causing this catastrophic air pollution?
Munir: Black exhaust fumes from defective vehicles, unregulated brick kilns, industrial chimneys, and burning piles of municipal plastic waste.
Sajib: And our rivers and water bodies are being turned into toxic drains by industrial chemical dumping and untreated sewage.
Munir: Exactly! Millions of people suffer from asthma, lung cancer, waterborne diseases, and hearing loss as a direct result.
Sajib: What urgent measures must be undertaken to check this environmental catastrophe?
Munir: First, brick kilns must adopt green technology, polluting vehicles must be banned, and industrial effluent treatment plants (ETP) must be enforced strictly.
Sajib: We must also ban single-use polythene bags completely, switch to solar and renewable energy, and carry out massive nationwide tree plantation drives.
Munir: Every citizen must take personal responsibility. Protecting our environment is safeguarding the survival of our future generations."""
    },
    21: {
        "script": """Shuvo: Assalamu Alaikum, Mizan. What book are you reading?
Mizan: Wa Alaikum Assalam, Shuvo. I am reading a collection of essays on women's empowerment and national development.
Shuvo: That is a very timely topic. Why is female education considered so critical for a developing nation like Bangladesh?
Mizan: Half of our total population consists of women. How can a nation hope to march forward if half of its citizens remain uneducated and backward?
Shuvo: That is a profound point. A bird cannot fly properly with only one wing.
Mizan: Exactly. Napoleon Bonaparte famously said: 'Give me an educated mother, and I will give you an educated nation.'
Shuvo: How does educating women directly benefit the entire household?
Mizan: An educated mother manages her family's nutrition, healthcare, and budget far more intelligently. She takes active care of her children's schooling and character.
Shuvo: It also enables women to become financially independent and contribute directly to the national economy through employment and entrepreneurship.
Mizan: Yes, in education, healthcare, administration, and the garment industry, our educated women are performing with outstanding excellence.
Shuvo: Therefore, eradicating child marriage and ensuring free higher secondary education for all girls must remain our top national priority.
Mizan: Well spoken, Shuvo. Female education is not a privilege; it is the cornerstone of national progress."""
    },
    22: {
        "script": """Tanvir: Hello Zubair, did you hear about the unfortunate youth from our neighborhood who was arrested yesterday?
Zubair: Hello Tanvir. Yes, it was heartbreaking to learn that he had become a helpless victim of drug addiction.
Tanvir: Drug addiction is a devastating curse that is silently ruining thousands of promising young lives across our society.
Zubair: Why do young people fall into the deadly trap of drugs like Yaba, heroin, and synthetic narcotics?
Tanvir: Often out of frustration, unemployment, broken family relationships, or dangerous peer pressure from bad companions.
Zubair: What terrible damage does drug addiction inflict on the human body and mind?
Tanvir: It completely destroys brain cells, causes kidney and liver failure, and leads to severe psychological disorders and depression.
Zubair: Not only that, an addict loses all moral judgment and often resorts to theft, robbery, and violence to pay for daily drugs, destroying family peace.
Tanvir: What comprehensive steps must be taken to defeat this deadly menace?
Zubair: The government must smash international drug trafficking cartels with an iron hand and enforce the death penalty for kingpins.
Tanvir: Furthermore, we need specialized, compassionate rehabilitation centers to treat addicted youth and reintegrate them into society.
Zubair: Families and community leaders must also provide emotional support to youth and promote healthy sports and cultural activities.
Tanvir: Let us unite our voices and declare: 'Say No to Drugs, and Yes to Life!'"""
    },
    23: {
        "script": """Rimon: Hello Sadik, our final exams will conclude next week. How about planning an educational study tour with our classmates?
Sadik: Hello Rimon! That is a brilliant idea. We have worked hard all year, and a refreshing excursion will broaden our minds.
Rimon: Which historical location would you propose for our destination?
Sadik: I strongly propose visiting the historical city of Bagerhat. It is a UNESCO World Heritage site and rich in medieval Islamic architecture.
Rimon: That is an exceptional choice! We can explore the magnificent Sixty Dome Mosque (Shat Gombuj Masjid) and the shrine of Hazrat Khan Jahan Ali.
Sadik: We will also learn about medieval drainage systems, ancient terracotta art, and the history of southern Bengal.
Rimon: How many students do you think will join the excursion?
Sadik: At least thirty classmates are eager to participate. We should also invite our English and History teachers to guide us.
Rimon: What will be the estimated budget per student?
Sadik: If we hire a comfortable tourist bus and arrange home-cooked meals, around one thousand Taka per head will cover all transport, food, and entry tickets.
Rimon: Let us draft a formal written application today and submit it to our Headmaster for official permission.
Sadik: Excellent! Let's meet in the library during tiffin break to finalize the tour schedule."""
    },
    24: {
        "script": """First Citizen: Good morning, neighbor. What are you looking at so suspiciously in the market?
Second Citizen: Good morning. I am inspecting these apples and fish. I fear they have been treated with toxic formalin and chemicals.
First Citizen: Food adulteration has truly become an invisible, silent killer in our country.
Second Citizen: It is terrifying! Greedy, unscrupulous traders mix deadly carbide to ripen bananas and mangoes artificially, and spray toxic chemicals on fish and meat to keep them looking fresh.
First Citizen: Even milk, spices, mustard oil, and sweetmeats are adulterated with poisonous industrial dyes, brick dust, and urea.
Second Citizen: What catastrophic medical consequences are people suffering as a result?
First Citizen: Doctors report that the alarming surge in kidney failure, liver cirrhosis, stomach cancer, and heart disease across Bangladesh is directly linked to adulterated food.
Second Citizen: Pregnant women and innocent children are the most vulnerable victims of this heartless commercial greed.
First Citizen: What must the authorities do to eradicate this crime against humanity?
Second Citizen: Mobile courts must operate continuously throughout the year, conducting random laboratory tests in wholesale and retail bazaars.
First Citizen: Corrupt hoarders and adulterators must be sentenced to rigorous life imprisonment, and their businesses permanently confiscated.
Second Citizen: The public must also become vigilant, boycott suspicious markets, and support certified organic farming.
First Citizen: Human life is precious; no one should be allowed to poison our nation for temporary profit."""
    },
    25: {
        "script": """First Customer: Assalamu Alaikum, brother. Look at the price list in the grocery market today! It is shocking.
Second Customer: Wa Alaikum Assalam. It is completely unbearable! The prices of essential commodities like rice, lentils, edible oil, and vegetables are skyrocketing every single day.
First Customer: A poor laborer earning five hundred Taka a day cannot even afford basic rice and potatoes for his family.
Second Customer: How can low-income and fixed-salary families survive in the face of such relentless inflation?
First Customer: What is causing this unnatural, continuous price hike?
Second Customer: While global fuel prices and transport costs have contributed, the primary culprit is illegal market syndicates and artificial hoarding by greedy wholesalers.
First Customer: Exactly! Middlemen hoard essential food stocks in secret warehouses, create artificial shortages, and fleece helpless consumers.
Second Customer: Extortion along transport highways also inflates the cost of vegetables before they even reach city markets.
First Customer: What steps should the government take immediately to bring relief to the common people?
Second Customer: The Trading Corporation of Bangladesh (TCB) must expand open-market truck sales of subsidized food in every ward and village.
First Customer: Furthermore, consumer rights protection directorates must conduct strict daily raids to smash corrupt trading cartels and enforce fair retail prices.
Second Customer: If the syndicates are broken, prices will return to normal, and the poor can breathe a sigh of relief."""
    },
    26: {
        "script": """Tahsin: Hello Siam, did you follow the proceedings of the recent United Nations Climate Change Conference?
Siam: Hello Tahsin. Yes, I followed the news closely. The reports on global warming and rising sea levels are deeply alarming for Bangladesh.
Tahsin: Our country contributes less than one percent of global carbon emissions, yet we are among the most severely affected victims of climate change.
Siam: That is the cruel injustice of global climate crisis. How is Bangladesh currently experiencing these impacts?
Tahsin: Rising sea levels are submerging low-lying coastal areas in Khulna, Satkhira, and Barishal, pushing saline water into freshwater agricultural lands and drinking wells.
Siam: Furthermore, the frequency and ferocity of devastating cyclones, river erosion, and flash floods have intensified dramatically.
Tahsin: Millions of coastal farmers and fishermen are losing their ancestral homesteads, becoming helpless climate refugees in city slums.
Siam: What must the international community do to fulfill their climate obligations?
Tahsin: Developed industrialized nations must drastically slash their carbon emissions and fulfill their promised billions in climate adaptation funds to vulnerable nations.
Siam: What domestic resilience measures should Bangladesh implement?
Tahsin: We must build stronger coastal embankments, preserve the mangrove barrier of the Sundarbans, and innovate saline-tolerant and flood-resistant rice varieties.
Siam: Protecting our planet is an urgent collective moral duty for all mankind."""
    },
    27: {
        "script": """Antora: Hi Shanta, I was reading an article about our country's growth.
Shanta: That is interesting, Antora. What did it say?
Antora: It said that education is the key to our national development.
Shanta: I agree. No nation can prosper without an educated population.
Antora: Exactly. Education is often called the "backbone" of a nation.
Shanta: Why do you think it is so important for a country?
Antora: It removes the darkness of ignorance and makes people aware.
Shanta: It also helps people learn new skills to work in modern industries.
Antora: Yes. An educated person can contribute more to the economy.
Shanta: And it's not just about money. Education improves our character.
Antora: True. It teaches us about our rights and our duties as citizens.
Shanta: It also helps in reducing poverty and controlling the population.
Antora: Without education, we cannot use our natural resources properly.
Shanta: You are right. Science and technology depend entirely on education.
Antora: Look at developed countries; they all have very high literacy rates.
Shanta: So, we must ensure that every child in our country goes to school.
Antora: Government and wealthy people should work together on this.
Shanta: Education is not a luxury; it is a basic human right.
Antora: If we educate our women, the whole nation will move forward faster.
Shanta: I hope our country becomes 100% literate very soon!"""
    },
    28: {
        "script": MODEL_DIALOGUES_VERBATIM["dialogue_28"]["dialogue_text"]
    },
    29: {
        "script": MODEL_DIALOGUES_VERBATIM["dialogue_29"]["dialogue_text"]
    },
    30: {
        "script": MODEL_DIALOGUES_VERBATIM["dialogue_30"]["dialogue_text"]
    },
    31: {
        "script": MODEL_DIALOGUES_VERBATIM["dialogue_31"]["dialogue_text"]
    },
    32: {
        "script": MODEL_DIALOGUES_VERBATIM["dialogue_32"]["dialogue_text"]
    }
}

def main():
    stories_data = []
    for s in COMPLETING_STORIES_34:
        sid = s["id"]
        extra = STORIES_EXTRAS.get(sid, {})
        story_obj = {
            "id": sid,
            "title": s["title"],
            "prompt": s["prompt"],
            "moral": extra.get("moral", "Honesty and hard work always triumph."),
            "story": extra.get("continuation", s["prompt"] + "\n\n" + extra.get("moral", "")),
            "boards": s["boards"],
            "priority": s["priority"]
        }
        stories_data.append(story_obj)

    dialogues_data = []
    for d in DIALOGUES_32:
        did = d["id"]
        extra = DIALOGUES_EXTRAS.get(did, {})
        d_obj = {
            "id": did,
            "title": d["title"],
            "characters": d["characters"],
            "scenario": d["scenario"],
            "dialogue_text": extra.get("script", f"{d['characters']}: Discussing {d['title']}."),
            "boards": d["boards"],
            "priority": d["priority"]
        }
        dialogues_data.append(d_obj)

    code = f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/pdf_to_post/data_ssc_2027_writing_full.py
Complete 34 Stories and 32 Dialogues with full texts for SSC 2027 English 1st Paper.
Generated automatically by generate_full_writing_data.py
"""

STORIES_FULL_34 = {repr(stories_data)}

DIALOGUES_FULL_32 = {repr(dialogues_data)}
'''

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(code)

    print(f"Generated {OUTPUT_FILE} successfully!")
    print(f"Total Stories: {len(stories_data)}, Total Dialogues: {len(dialogues_data)}")

if __name__ == "__main__":
    main()
