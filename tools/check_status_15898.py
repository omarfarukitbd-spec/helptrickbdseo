import requests
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('tools/wp_publisher/config.json', 'r', encoding='utf-8') as f:
    cfg = json.load(f)

auth = (cfg['wp_user'], cfg['wp_app_password'])
base_url = cfg['wp_url'].rstrip('/')

res = requests.get(base_url + '/wp-json/wp/v2/posts/15898?context=edit', auth=auth)
if res.status_code == 200:
    p = res.json()
    print('ID:', p.get('id'))
    print('Modified:', p.get('modified'))
    c = p.get('content', {}).get('raw', '')
    print('Content Length:', len(c))
    print('Has wp:rank-math/toc-block:', 'wp:rank-math/toc-block' in c)
    print('Has id="rank-math-toc":', 'id="rank-math-toc"' in c)
else:
    print('Error getting 15898:', res.status_code)

ares = requests.get(base_url + '/wp-json/wp/v2/posts/15898/autosaves', auth=auth)
if ares.status_code == 200:
    print('Autosaves count:', len(ares.json()))
