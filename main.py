from crawl import Crawl
from googleapi import GoogleAPI
from utils import Utils
from matching import Matching


if __name__ == '__main__':

    api = GoogleAPI()
    crawl = Crawl()
    utils = Utils()
    matching = Matching()

    text_list = crawl.get_text(api.get_values('form'))
    agent_list = crawl.get_text(api.get_values('agent'))

    text_list = utils.tfidf(text_list=text_list)
    agent_list = utils.tfidf(text_list=agent_list)

    text_list = utils.cos_similarity(
        text_list=text_list, agent_list=agent_list)

    text_list = matching.execute(
        text_list=text_list, agent_list=agent_list)

    api.set_values(sheet_name='form', text_list=text_list)
