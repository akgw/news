from lib.googleapi import GoogleAPI


class JobSeekersRepository:
    def __init__(self):
        self.api = GoogleAPI()

    # 求職者の情報を取得する
    def get(self):
        return self.api.get_values('form')

    # 求職者の情報を更新する
    def update(self, values):
        return self.api.set_values('form', values)
