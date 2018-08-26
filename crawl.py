import requests
from bs4 import BeautifulSoup
import re


class Crawl:
    def __init__(self, rows):
        self.rows = rows

    def get_text(self):
        for row in self.rows:
            [url] = row
            resp = requests.get(url)
            if resp.status_code != 200:
                print('指定したURLが存在しません url=' + url)
                continue
            soup = BeautifulSoup(resp.text, 'html.parser')
            self.extract_tag(soup, 'script')
            self.extract_tag(soup, 'style')

            text = soup.find('body').get_text()
            print(re.sub(r"\s+", " ", text))

    @staticmethod
    def extract_tag(soup, tag_name):
        script = soup(tag_name)
        for tag in script:
            tag.extract()
