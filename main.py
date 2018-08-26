from crawl import Crawl
from googleapi import GoogleAPI

api = GoogleAPI()
rows = api.get_values()

crawl = Crawl(rows)
crawl.get_text()
