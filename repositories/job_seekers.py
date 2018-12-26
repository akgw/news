from lib.googleapi import GoogleAPILib
import constants
from utils import Utils


class JobSeekersRepository:

    def __init__(self):
        self.api = GoogleAPILib()
        self.sheet_name = 'form'
        self.sheet = constants.sheet_dic[self.sheet_name]
        self.utils = Utils()

    # 求職者の情報を取得する
    def get(self):
        range_name = self.sheet_name + '!' + self.sheet['range']
        values = self.api.get_values(range_name=range_name)

        return self.utils.formatted_spreadsheet_value(values, self.sheet['map'])

    # 求職者の情報を更新する
    def update(self, job_seekers):
        for value in job_seekers.values():
            evaluation_target = self.sheet_name + '!' + \
                self.sheet['output_range'] + str(value['column_index'])

            evaluation_body = {
                'values': [
                    [
                        str(sorted(value['point'].items(),
                                   key=lambda x: -x[1]))
                    ],
                ]
            }

            self.api.update_values(evaluation_target, evaluation_body)

    # 求職者の指定したニュースのTFIDFが高い単語を付加
    def update_tfidf_words(self, job_seekers):
        for value in job_seekers.values():
            tfidf_words_target = self.sheet_name + '!' + \
                self.sheet['tfidf_words_range'] + str(value['column_index'])

            tfidf_words_body = {
                'values': [
                    [
                         str(value['tfidf_words'])
                    ],
                ]
            }

            self.api.update_values(tfidf_words_target, tfidf_words_body)
