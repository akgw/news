from crawl import Crawl
from googleapi import GoogleAPI
from utils import Utils

if __name__ == '__main__':

    api = GoogleAPI()
    rows = api.get_values('form')

    agent = api.get_values('agent')

    crawl = Crawl(rows)
    text_list = crawl.get_text()

    utils = Utils()
    text_list = utils.tfidf(text_list=text_list)

    # text_list = utils.cos_similarity(text_list=text_list)
