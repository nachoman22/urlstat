import time
import urllib3
import logging

logging.basicConfig(filename='urlstat.log', level=logging.INFO)

#main logic
http = urllib3.PoolManager()
urls = ["http://google.com", "http://github.com"]

for url in urls:
    r = http.request('GET', url)
    out1 = r.status
    out2 = r.reason
    print(url, out1, out2)
