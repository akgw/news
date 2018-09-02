import requests
from bs4 import BeautifulSoup
import re


class Crawl:
    def __init__(self, rows):
        self.rows = rows

    def get_text(self):
        text_list = {}
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
            text = ' '.join(text.splitlines())
            text = re.split(" +", text)
            text_list[url] = ' '.join([s for s in text if ('。' in s)])

        return text_list

    @staticmethod
    def extract_tag(soup, tag_name):
        script = soup(tag_name)
        for tag in script:
            tag.extract()
