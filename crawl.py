import requests
from bs4 import BeautifulSoup


class Crawl:
    def __init__(self):
        self.url = "https://www.google.co.jp/search?q=python+no+module+named&oq=python&aqs=chrome.0.69i59l3j69i57j69i65l2.869j0j7&sourceid=chrome&ie=UTF-8"

    def get_text(self):
        resp = requests.get(self.url)
        soup = BeautifulSoup(resp.text)
        return soup.find('body').get_text()


crawl = Crawl()
print(crawl.get_text())
