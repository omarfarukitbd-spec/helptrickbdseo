import urllib.request

def check_live():
    req = urllib.request.Request('https://www.helptrickbd.com/?m=1', headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Mobile)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
        print("Fetched live HTML length:", len(html))
        print("1. Has Google Fonts async comment:", "Google Fonts Async Non-blocking" in html)
        print("2. Has media='print':", "media='print'" in html or 'media="print"' in html)
        print("3. Has SolaimanLipi:", "SolaimanLipi" in html)
        print("4. Has Table Responsive:", "table-responsive" in html)
        print("5. Has jQuery 3.7.1:", "3.7.1" in html)
        print("6. Has jQuery 3.5.1:", "3.5.1" in html)
        print("7. Has AdSense optimized comment:", "Google AdSense Official Script Optimized" in html)
    except Exception as e:
        print("Fetch error:", e)

if __name__ == '__main__':
    check_live()
