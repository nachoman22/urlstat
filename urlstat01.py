import time
import urllib.request
from threading import Thread

class GetUrlThread(Thread):
    def __init__(self, url):
        self.url = url
        super(GetUrlThread, self).__init__()

    def run(self):
        resp = urllib.request.urlopen(self.url)
        print(self.url, resp.getcode())

def get_responses():
    urls = ['https://google.com', "https://github.com"]
    start = time.time()
    threads = []
    for url in urls:
        t = GetUrlThread(url)
        threads.append(t)
        t.start()
        for s in threads:
            s.join()
            print("Elapsed time: %s" % (time.time()-start))

get_responses()
