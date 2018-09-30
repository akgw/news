from lib.googleapi import GoogleAPI


class AgentsRepository:
    def __init__(self):
        self.api = GoogleAPI()

    # エージェントの情報を取得する
    def get(self):
        return self.api.get_values('agent')
