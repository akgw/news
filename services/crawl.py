from lib.crawl import CrawlLib


class CrawlService:
    def __init__(self):
        self.crawl = CrawlLib()

    def execute(self, rows):
        text_list = {}
        for row in rows:
            if row['url'] == '':
                row['full_text'] = ''
                text_list[row['column_index']] = row
                continue

            text = self.crawl.execute(row['url'])
            if text is None:
                print('指定したURLが存在しません url=' + row['url'])
                continue

            row['full_text'] = text
            text_list[row['column_index']] = row

        return text_list
