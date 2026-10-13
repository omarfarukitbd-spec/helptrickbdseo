import urllib.request
import urllib.error
import urllib.parse
import json
import re
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import ssl

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 AuditBot/1.0'
}

def fetch(url):
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=12, context=ssl_context) as resp:
            content = resp.read()
            charset = resp.headers.get_content_charset() or 'utf-8'
            try:
                html = content.decode(charset, errors='replace')
            except:
                html = content.decode('utf-8', errors='replace')
            return resp.status, dict(resp.headers), html
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers), ''
    except Exception as e:
        return 0, {}, str(e)

print("Starting Comprehensive Website Audit for https://www.helptrickbd.com...")
results = {
    "homepage": {},
    "posts": [],
    "categories": [],
    "pages": {},
    "broken_links": [],
    "sitemap": {},
    "robots": {},
    "security_headers": {},
    "schema_markup": {}
}

# 1. Robots.txt
code, headers, body = fetch("https://www.helptrickbd.com/robots.txt")
results["robots"] = {
    "status": code,
    "has_sitemap": "sitemap" in body.lower(),
    "disallows": [line for line in body.splitlines() if line.lower().startswith("disallow")]
}

# 2. Sitemap
code, headers, body = fetch("https://www.helptrickbd.com/sitemap_index.xml")
sitemaps = re.findall(r'<loc>(https?://[^<]+)</loc>', body)
results["sitemap"] = {
    "status": code,
    "sub_sitemaps": sitemaps
}

# 3. Homepage Audit
code, headers, html = fetch("https://www.helptrickbd.com/")
soup = BeautifulSoup(html, 'html.parser')
h1s = [h.get_text(strip=True) for h in soup.find_all('h1')]
h2s = [h.get_text(strip=True) for h in soup.find_all('h2')]
title = soup.find('title')
meta_desc = soup.find('meta', attrs={'name': 'description'})
canonical = soup.find('link', attrs={'rel': 'canonical'})
meta_robots = soup.find('meta', attrs={'name': 'robots'})
images = soup.find_all('img')
imgs_no_alt = [img.get('src') for img in images if not img.get('alt')]
imgs_no_dim = [img.get('src') for img in images if not img.get('width') or not img.get('height')]

results["security_headers"] = {
    "HSTS": headers.get('Strict-Transport-Security', 'MISSING'),
    "X-Content-Type-Options": headers.get('X-Content-Type-Options', 'MISSING'),
    "X-Frame-Options": headers.get('X-Frame-Options', 'MISSING'),
    "Content-Security-Policy": 'PRESENT' if 'Content-Security-Policy' in headers else 'MISSING',
    "Cache-Control": headers.get('Cache-Control', 'MISSING'),
    "X-LiteSpeed-Cache": headers.get('X-LiteSpeed-Cache', 'MISSING')
}

results["homepage"] = {
    "status": code,
    "title": title.get_text(strip=True) if title else None,
    "meta_description": meta_desc.get('content') if meta_desc else None,
    "canonical": canonical.get('href') if canonical else None,
    "robots": meta_robots.get('content') if meta_robots else None,
    "h1_count": len(h1s),
    "h1_tags": h1s,
    "h2_count": len(h2s),
    "total_images": len(images),
    "images_without_alt": len(imgs_no_alt),
    "images_without_dimensions": len(imgs_no_dim)
}

# Extract all internal links from homepage
all_links = set()
for a in soup.find_all('a', href=True):
    href = a['href']
    if href.startswith('https://www.helptrickbd.com') or href.startswith('/'):
        full_url = urllib.parse.urljoin('https://www.helptrickbd.com', href)
        # exclude hash and wp-admin
        if '#' in full_url:
            full_url = full_url.split('#')[0]
        if 'wp-admin' not in full_url and 'wp-login' not in full_url:
            all_links.add(full_url)

print(f"Discovered {len(all_links)} internal links on homepage.")

# 4. Check essential policy pages
policy_pages = [
    "https://www.helptrickbd.com/about-us/",
    "https://www.helptrickbd.com/about/",
    "https://www.helptrickbd.com/contact-us/",
    "https://www.helptrickbd.com/contact/",
    "https://www.helptrickbd.com/privacy-policy/",
    "https://www.helptrickbd.com/terms-and-conditions/",
    "https://www.helptrickbd.com/terms-of-service/",
    "https://www.helptrickbd.com/disclaimer/"
]

for p in policy_pages:
    p_code, p_headers, p_html = fetch(p)
    results["pages"][p] = {
        "status": p_code,
        "length": len(p_html) if p_code == 200 else 0
    }

# 5. Check sample posts
post_links = [l for l in all_links if l != 'https://www.helptrickbd.com/' and '/category/' not in l and '/page/' not in l and not any(k in l for k in ['feed', 'about', 'contact', 'privacy', 'terms', 'disclaimer'])][:10]

for pl in post_links:
    pl_code, pl_headers, pl_html = fetch(pl)
    if pl_code != 200:
        results["broken_links"].append({"url": pl, "status": pl_code})
        continue
    p_soup = BeautifulSoup(pl_html, 'html.parser')
    p_h1 = [h.get_text(strip=True) for h in p_soup.find_all('h1')]
    p_h2 = [h.get_text(strip=True) for h in p_soup.find_all('h2')]
    p_desc = p_soup.find('meta', attrs={'name': 'description'})
    p_canon = p_soup.find('link', attrs={'rel': 'canonical'})
    
    # Check JSON-LD
    json_lds = p_soup.find_all('script', type='application/ld+json')
    schemas = []
    for j in json_lds:
        try:
            data = json.loads(j.string)
            if isinstance(data, dict):
                schemas.append(data.get('@type', 'Graph' if '@graph' in data else 'Unknown'))
            elif isinstance(data, list):
                schemas.extend([item.get('@type') for item in data if isinstance(item, dict)])
        except:
            pass
            
    results["posts"].append({
        "url": pl,
        "h1_count": len(p_h1),
        "h1": p_h1[0] if p_h1 else None,
        "h2_count": len(p_h2),
        "has_meta_desc": bool(p_desc),
        "has_canonical": bool(p_canon),
        "schema_types": schemas
    })

# 6. Check categories
cat_links = [l for l in all_links if '/category/' in l][:5]
for cl in cat_links:
    cl_code, cl_headers, cl_html = fetch(cl)
    c_soup = BeautifulSoup(cl_html, 'html.parser')
    c_h1 = [h.get_text(strip=True) for h in c_soup.find_all('h1')]
    results["categories"].append({
        "url": cl,
        "status": cl_code,
        "h1": c_h1[0] if c_h1 else None
    })

# 7. Check all other links for 404s
print("Testing remaining internal links for 404s...")
for link in list(all_links)[:50]:
    if link not in [p["url"] for p in results["posts"]] and link not in [c["url"] for c in results["categories"]] and link not in results["pages"]:
        l_code, _, _ = fetch(link)
        if l_code != 200:
            results["broken_links"].append({"url": link, "status": l_code})

with open("d:/android/Project/Helptrickbd Wp/audit_result.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("Comprehensive Audit Complete. Saved to audit_result.json")
