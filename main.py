from crawl import Crawl
from googleapi import GoogleAPI
from utils import Utils

if __name__ == '__main__':

    api = GoogleAPI()
    rows = api.get_values()

    crawl = Crawl(rows)
    text_list = crawl.get_text()

    utils = Utils()
    text_list = utils.to_words(text_list=text_list)
    print(text_list)
