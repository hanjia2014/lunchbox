import urllib.request
import time

url = "https://read.douban.com/reader/column/77988011/chapter/784966825/?dcs=column&dcm=chapter-list"
count = 100

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}

for i in range(count):
    try:
        req = urllib.request.Request(url, headers=headers)
        urllib.request.urlopen(req)
        print(f"Visit {i+1} - OK")
    except Exception as e:
        print(f"Visit {i+1} - Error: {e}")
    time.sleep(0.5)