import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')
doc = fitz.open('assets/pdf/nu/nu_degree_1st_year_rescheduled_routine_notice.pdf')
hits = []
for i in range(len(doc)):
    txt = doc[i].get_text()
    if any(w in txt for w in ['১৮/১০/২০২৬', '১৯/১০/২০২৬', 'পরীক্ষা সংক্রান্ত জরুরি বিজ্ঞপ্তি', 'সংশোধিত']):
        hits.append((i, txt[:120].strip().replace('\n', ' ')))

print(f"Total hits: {len(hits)}")
for h in hits:
    print(h)
