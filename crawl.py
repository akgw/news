import requests
from bs4 import BeautifulSoup
import re
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class Crawl:
    def get_text(self, rows):
        text_list = {}
        for row in rows:
            url = row['url']
            resp = requests.get(row['url'], verify=False)
            if resp.status_code != 200:
                print('指定したURLが存在しません url=' + url)
                continue
            soup = BeautifulSoup(resp.content, 'html.parser')
            self.extract_tag(soup, 'script')
            self.extract_tag(soup, 'style')

            text = soup.find('body').get_text()
            text = ' '.join(text.splitlines())
            text = re.split(" +", text)

            row['full_text'] = ''.join(
                [s for s in text if ('。' in s)])

            text_list[row['column_index']] = row

        return text_list

    @staticmethod
    def extract_tag(soup, tag_name):
        script = soup(tag_name)
        for tag in script:
            tag.extract()
