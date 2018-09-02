from crawl import Crawl
from googleapi import GoogleAPI

api = GoogleAPI()
rows = api.get_values()

crawl = Crawl(rows)
test_list = crawl.get_text()


print(test_list)
