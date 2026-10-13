import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from tools.wp_publisher.publisher import WordPressPublisher

sys.stdout.reconfigure(encoding='utf-8')
pub = WordPressPublisher()
for pid in [1, 28, 37, 132]:
    r = pub.client.get(f'posts/{pid}')
    if r.status_code == 200:
        d = r.json()
        kw = d.get("meta", {}).get("rank_math_focus_keyword", "")
        t = d.get("title", {}).get("rendered", "")
        print(f"ID {pid} -> Focus KW: '{kw}' | Title: '{t[:60]}'")
