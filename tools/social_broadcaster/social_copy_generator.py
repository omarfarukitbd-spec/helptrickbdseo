#!/usr/bin/env python3
"""
tools/social_broadcaster/social_copy_generator.py
HelpTrickBD Human-Feel Social Copy Generator.

Generates authentic, high-converting, platform-tailored social media copy
for Facebook, Telegram, and WhatsApp without robotic or repetitive AI clichés.
Strictly zero-emoji compliant.
"""

import re
import random
from typing import Dict, List, Optional
from bs4 import BeautifulSoup


class SocialCopyGenerator:
    """Generates authentic, human-sounding social media copy from blog post content."""

    # Curated category-specific hashtags
    HASHTAG_MAP = {
        "ssc": ["#HelpTrickBD", "#SSC2026", "#SSCPreparation", "#BoardExam", "#StudyTipsBD"],
        "class9": ["#HelpTrickBD", "#Class9Guide", "#NewCurriculum", "#StudyNotes", "#EducationBD"],
        "class10": ["#HelpTrickBD", "#Class10Guide", "#BoardExam", "#SSCPreparation", "#StudyTipsBD"],
        "islamic": ["#HelpTrickBD", "#IslamShikkha", "#IslamicStudies", "#BoardExamPrep", "#StudyGuide"],
        "bcs": ["#HelpTrickBD", "#BCSPreparation", "#GovtJobBD", "#JobCircular", "#CareerTipsBD"],
        "primary": ["#HelpTrickBD", "#PrimaryTeacher", "#DPEJob", "#JobPreparation", "#CareerBD"],
        "political": ["#HelpTrickBD", "#NationalUniversity", "#MastersHandnote", "#PoliticalScience", "#NUExam"],
        "tech": ["#HelpTrickBD", "#TechTips", "#BanglaTutorial", "#HowToGuide", "#DigitalSkills"],
        "general": ["#HelpTrickBD", "#EducationBD", "#BanglaArticle", "#StudyGuide", "#ExamTips"]
    }

    # Archetype opening hooks (conversational, authentic, zero robotic clichés)
    ACADEMIC_HOOKS = [
        "পরীক্ষার প্রস্তুতি গোছাতে গিয়ে অনেকেই বিশেষ কিছু অধ্যায় বা প্রশ্নের গঠন নিয়ে সংশয়ে ভোগে। এই সমস্যার কার্যকর সমাধান তুলে ধরা হয়েছে আজকের পূর্ণাঙ্গ গাইডে।",
        "পরীক্ষার জন্য শুধু মুখস্থ করা যথেষ্ট নয়, প্রশ্নের ধরন বুঝে সঠিক পয়েন্ট অনুযায়ী উত্তর লিখতে পারাটাই ভালো নম্বরের মূল চাবিকাঠি।",
        "তোমাদের অনেকেই নিয়মিত জানতে চেয়েছিলে কীভাবে এই বিষয়ের কঠিন টপিকগুলো সহজে রিভিশন দেওয়া যায়। সেই ধারাবাহিকতায় তৈরি করা হয়েছে এই স্টাডি গাইড।",
        "বোর্ড পরীক্ষার খাতার মূল্যায়ন সাধারণ পরীক্ষার চেয়ে আলাদা। তাই প্রতিটি প্রশ্নের আদর্শ মডেল উত্তর জানা থাকলে আত্মবিশ্বাস বহুগুণ বেড়ে যায়।"
    ]

    JOB_HOOKS = [
        "সরকারি ও প্রতিযোগিতামূলক পরীক্ষায় সফল হতে হলে সিলেবাসের খুঁটিনাটি এবং বিগত বছরের প্রশ্ন বিশ্লেষণ জানা অপরিহার্য।",
        "চাকরির প্রস্তুতিতে প্রতিটি নম্বর মূল্যবান। সাধারণ ভুলের কারণে যাতে পিছিয়ে পড়তে না হয়, সেজন্য বিশেষ কিছু কৌশল আয়ত্তে রাখা জরুরি।",
        "যাঁরা এই নিয়োগ পরীক্ষার প্রস্তুতি নিচ্ছেন, তাঁদের জন্য সময় ব্যবস্থাপনা এবং বিষয়ভিত্তিক প্রশ্ন সমাধানের পূর্ণাঙ্গ গাইডলাইন তৈরি করা হয়েছে।"
    ]

    TECH_HOOKS = [
        "কোনো প্রয়োজনীয় অনলাইন সেবা বা ডিজিটাল সেটিংস নিয়ে কাজ করার সময় ছোটখাটো জটিলতায় সময় নষ্ট হওয়া স্বাভাবিক। এই সহজ নির্দেশিকায় সম্পূর্ণ সমাধান তুলে ধরা হলো।",
        "সঠিক নিয়ম না জানার কারণে অনেকেই জরুরি প্রক্রিয়ায় ভুলের শিকার হন। প্রতিটি ধাপ ধারাবাহিকভাবে অনুসরণ করলে ঘরে বসেই কাজটি নিরাপদে সম্পন্ন করা সম্ভব।"
    ]

    GENERAL_HOOKS = [
        "যাঁরা এই বিষয়ে বিস্তারিত ও নির্ভরযোগ্য তথ্য খুঁজছিলেন, তাঁদের জন্য প্রয়োজনীয় সব পয়েন্ট একত্রিত করে এই বিশেষ আর্টিকেলটি প্রকাশ করা হলো।"
    ]

    def __init__(self):
        pass

    def detect_archetype(self, title: str, labels: List[str], text_content: str) -> str:
        """Detects the content archetype for conversational tone selection."""
        combined = f"{title} {' '.join(labels)} {text_content[:600]}".lower()
        if any(w in combined for w in ["bcs", "চাকরি", "নিয়োগ", "প্রাইমারি", "শিক্ষক", "সার্কুলার", "বেতন"]):
            return "job"
        elif any(w in combined for w in ["টিউটোরিয়াল", "আবেদন", "অনলাইন", "সেটিংস", "পাসপোর্ট", "কার্ড", "সফটওয়্যার", "পদ্ধতি"]):
            return "tech"
        elif any(w in combined for w in ["ক্লাস", "দাখিল", "নবম", "দশম", "এসএসসি", "অনার্স", "মাস্টার্স", "সাজেশন", "নোট", "গাইড", "অধ্যায়", "বোর্ড"]):
            return "academic"
        return "general"

    def get_hashtags(self, title: str, labels: List[str]) -> List[str]:
        """Selects relevant hashtags based on title and labels."""
        combined = f"{title} {' '.join(labels)}".lower()
        tags = set()
        tags.add("#HelpTrickBD")

        if "ইসলাম" in combined or "islam" in combined:
            tags.update(self.HASHTAG_MAP["islamic"])
        if "ssc" in combined or "এসএসসি" in combined:
            tags.update(self.HASHTAG_MAP["ssc"])
        if "৯ম" in combined or "নবম" in combined or "class 9" in combined:
            tags.update(self.HASHTAG_MAP["class9"])
        if "১০ম" in combined or "দশম" in combined or "class 10" in combined:
            tags.update(self.HASHTAG_MAP["class10"])
        if "bcs" in combined or "বিসিএস" in combined:
            tags.update(self.HASHTAG_MAP["bcs"])
        if any(w in combined for w in ["চাকরি", "নিয়োগ", "বিজ্ঞপ্তি", "সার্কুলার", "job"]):
            tags.update(self.HASHTAG_MAP["bcs"])
        if "প্রাইমারি" in combined or "primary" in combined:
            tags.update(self.HASHTAG_MAP["primary"])
        if "মাস্টার্স" in combined or "রাষ্ট্রবিজ্ঞান" in combined:
            tags.update(self.HASHTAG_MAP["political"])
        if "টিউটোরিয়াল" in combined or "অনলাইন" in combined:
            tags.update(self.HASHTAG_MAP["tech"])

        if len(tags) <= 1:
            tags.update(self.HASHTAG_MAP["general"])

        return list(tags)[:5]

    def extract_highlights(self, html_content: str) -> List[str]:
        """Extracts 3-4 natural value highlights from post headings and text."""
        soup = BeautifulSoup(html_content, "html.parser")
        headings = []
        for h in soup.find_all(["h2", "h3"]):
            txt = h.get_text(strip=True)
            # Remove numbering or punctuation
            clean_txt = re.sub(r"^[০-৯0-9\.\:\-\s]+", "", txt).strip()
            if clean_txt and len(clean_txt) > 8 and len(clean_txt) < 80:
                if not any(skip in clean_txt.lower() for skip in ["সূচিপত্র", "সারসংক্ষেপ", "প্রশ্নোত্তর", "faq"]):
                    headings.append(clean_txt)

        highlights = []
        for h in headings[:4]:
            highlights.append(h)

        # Fallback if headings are missing or sparse
        if len(highlights) < 2:
            highlights = [
                "বোর্ড পরীক্ষার মানদণ্ডে প্রতিটি অধ্যায়ের নির্ভুল মডেল বিশ্লেষণ",
                "পরীক্ষার খাতায় সর্বোচ্চ নম্বর পাওয়ার কার্যকরী প্রেজেন্টেশন টেকনিক",
                "সহজে রিভিশন দেওয়ার জন্য গুরুত্বপূর্ণ পয়েন্ট ও হ্যান্ডনোটস"
            ]

        return highlights[:4]

    def generate_all(self, title: str, post_url: str, html_content: str, labels: Optional[List[str]] = None, hero_image: Optional[str] = None) -> Dict[str, str]:
        """Generates tailored copy for Telegram, Facebook, and WhatsApp."""
        labels = labels or []
        soup = BeautifulSoup(html_content, "html.parser")
        plain_text = soup.get_text(" ", strip=True)

        archetype = self.detect_archetype(title, labels, plain_text)
        if archetype == "job":
            hook = random.choice(self.JOB_HOOKS)
        elif archetype == "tech":
            hook = random.choice(self.TECH_HOOKS)
        elif archetype == "academic":
            hook = random.choice(self.ACADEMIC_HOOKS)
        else:
            hook = random.choice(self.GENERAL_HOOKS)

        highlights = self.extract_highlights(html_content)
        hashtags = self.get_hashtags(title, labels)
        hashtag_str = " ".join(hashtags)

        # Dynamic Call-To-Action based on archetype
        if archetype == "job":
            cta_text = "নিয়োগ পরীক্ষার সঠিক প্রস্তুতি নিতে এবং সম্পূর্ণ তথ্য জানতে ভিজিট করুন:"
            tg_cta = "সম্পূর্ণ চাকরির সার্কুলার ও গাইড দেখুন"
            wa_cta = "সম্পূর্ণ তথ্য ও আবেদন নির্দেশিকা দেখতে লিংকে প্রবেশ করুন:"
        elif archetype == "tech":
            cta_text = "ধাপগুলো বিস্তারিতভাবে বুঝতে এবং সঠিকভাবে সম্পন্ন করতে সম্পূর্ণ গাইডটি দেখুন:"
            tg_cta = "সম্পূর্ণ টিউটোরিয়াল ও স্টেপ গাইড পড়ুন"
            wa_cta = "সম্পূর্ণ স্টেপ-বাই-স্টেপ টিউটোরিয়াল দেখতে লিংকে প্রবেশ করুন:"
        elif archetype == "academic":
            cta_text = "পরীক্ষার সর্বোচ্চ প্রস্তুতি নিশ্চিত করতে এবং পুরো নির্দেশিকা এক নজরে দেখতে ভিজিট করুন:"
            tg_cta = "সম্পূর্ণ স্টাডি গাইড ও নোটস পড়ুন"
            wa_cta = "সম্পূর্ণ নির্দেশিকা ও প্রয়োজনীয় ফাইল দেখতে লিংকে প্রবেশ করুন:"
        else:
            cta_text = "এই বিষয়ে আরও গভীর ও বিস্তারিত তথ্য জানতে সম্পূর্ণ আর্টিকেলটি ভিজিট করুন:"
            tg_cta = "সম্পূর্ণ আর্টিকেল পড়ুন"
            wa_cta = "সম্পূর্ণ বিবরণ ও মূল ভাবার্থ পড়তে লিংকে প্রবেশ করুন:"

        # 1. Telegram Copy (HTML markup)
        tg_bullets = "\n".join([f"• {item}" for item in highlights])
        telegram_text = (
            f"<b>{title}</b>\n\n"
            f"{hook}\n\n"
            f"<b>মূল বিষয়বস্তু ও বিশেষ অংশসমূহ:</b>\n"
            f"{tg_bullets}\n\n"
            f"{cta_text}\n"
            f"<a href=\"{post_url}\">{tg_cta}</a>\n\n"
            f"{hashtag_str}"
        )

        # 2. Facebook Copy (Natural paragraphs, high engagement)
        fb_bullets = "\n".join([f"- {item}" for item in highlights])
        facebook_text = (
            f"{title}\n\n"
            f"{hook}\n\n"
            f"কনটেন্টের মূল আকর্ষণ ও গুরুত্বপূর্ণ অংশসমূহ:\n"
            f"{fb_bullets}\n\n"
            f"{cta_text}\n"
            f"{post_url}\n\n"
            f"{hashtag_str}"
        )

        # 3. WhatsApp Copy (WhatsApp Markdown)
        wa_bullets = "\n".join([f"• {item}" for item in highlights])
        whatsapp_text = (
            f"*{title}*\n\n"
            f"{hook}\n\n"
            f"*গুরুত্বপূর্ণ বিষয়সমূহ:*\n"
            f"{wa_bullets}\n\n"
            f"{wa_cta}\n"
            f"{post_url}\n\n"
            f"{hashtag_str}"
        )

        return {
            "title": title,
            "post_url": post_url,
            "hero_image": hero_image or "",
            "archetype": archetype,
            "telegram": telegram_text,
            "facebook": facebook_text,
            "whatsapp": whatsapp_text,
            "hashtags": hashtags
        }
