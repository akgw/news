import requests
from bs4 import BeautifulSoup
import re
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)


class CrawlLib:
    def execute(self, url):
        resp = requests.get(url, verify=False)
        if resp.status_code != 200:
            return

        soup = BeautifulSoup(resp.content, 'html.parser')
        self.__extract_tag(soup, 'script')
        self.__extract_tag(soup, 'style')

        body = soup.find('body').get_text()
        text = ' '.join(body.splitlines())
        text = re.split(" +", text)

        return ''.join(
            [s for s in text if ('。' in s)])

    @staticmethod
    def __extract_tag(soup, tag_name):
        script = soup(tag_name)
        for tag in script:
            tag.extract()
