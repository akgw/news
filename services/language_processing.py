from lib.sklearn import SklearnLib


class LanguageProcessingService:

    def __init__(self):
        self.sklearn = SklearnLib()

    # tfidf値を取得
    def append_tfidf(self, text_list):
        for column_index, text in text_list.items():
            if text['full_text'] == '':
                continue

            result = self.sklearn.calc_tfidf(
                text=text['full_text'])
            text_list[column_index]['tfidf'] = result['tfidf']
            text_list[column_index]['vectorizer'] = result['vectorizer']

        return text_list

    # cos類似度を取得
    def append_cos_similarity(self, text_list, agent_list):
        agent_text_list = []
        agent_name_list = []
        for agent_text in agent_list.values():
            agent_text_list.append(agent_text['full_text'])
            agent_name_list.append(agent_text['name'])

        for column_index, text in text_list.items():
            if 'tfidf' not in text:
                continue

            cos = self.sklearn.calc_cos_similarity(
                agent_text_list=agent_text_list, tfidf=text['tfidf'], vectorizer=text['vectorizer'])

            # 類似順に取得
            news_rank = []
            for index in cos.argsort()[0][::-1]:
                news_rank.append(agent_name_list[index])
            text_list[column_index]['news_rank'] = news_rank

        return text_list
