from lib.googleapi import GoogleAPILib
import constants
from utils import Utils


class AgentsRepository:

    def __init__(self):
        self.api = GoogleAPILib()
        self.sheet_name = 'agent'
        self.sheet = constants.sheet_dic[self.sheet_name]
        self.utils = Utils()

    # エージェントの情報を取得する
    def get(self):
        values = self.api.get_values(
            range_name=self.sheet_name + '!' + self.sheet['range'])
        return self.utils.formatted_spreadsheet_value(values, self.sheet['map'])
