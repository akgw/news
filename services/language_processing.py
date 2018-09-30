import MeCab
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class LanguageProcessingService:

    @staticmethod
    def split(text, to_stem=False):
        tagger = MeCab.Tagger(
            '-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
        mecab_result = tagger.parse(text)
        info_of_words = mecab_result.split('\n')
        words = []
        for info in info_of_words:
            if info == 'EOS' or info == '':
                break

            # 句読点が入ると処理が不正になるのでスキップする
            if info[0] == ',':
                continue

            info_elems = info.split(',')

            # 名詞だけに絞る
            word, part = info_elems[0].split("\t")
            if part != "名詞":
                continue

            # 数字は除外
            if word.isnumeric():
                continue

            # 非自立は除外
            if info_elems[1] == '非自立':
                continue

            if info_elems[6] == '*':
                words.append(info_elems[0][:-3])
                continue

            if to_stem:
                words.append(info_elems[6])
                continue

            words.append(info_elems[0][:-3])
        return words

    def to_stem(self, text):
        return self.split(text=text, to_stem=True)

    def tfidf(self, text_list):
        for column_index, text in text_list.items():
            vectorizer = TfidfVectorizer(
                analyzer=self.to_stem, min_df=1, max_df=50)
            tfidf_list = vectorizer.fit_transform([text['full_text']])
            text_list[column_index]['vectorizer'] = vectorizer
            text_list[column_index]['tfidf'] = tfidf_list.toarray()

            # continue
            #
            # # 単語ごとのtfidf値出力
            # print('対象URL:' + str(url))
            # tfidfs = tfidf_list.toarray()[0]
            # terms = vectorizer.get_feature_names()
            #
            # for term in terms:
            #     tfidf = tfidfs[terms.index(term)]
            #     if tfidf > 0:
            #         print(term + ':' + str(tfidf))

        return text_list

    @staticmethod
    def cos_similarity(text_list, agent_list):
        agent_text_list = []
        agent_name_list = []
        for agent_text in agent_list.values():
            agent_text_list.append(agent_text['full_text'])
            agent_name_list.append(agent_text['name'])

        for column_index, text in text_list.items():
            agent_tfidf = text['vectorizer'].transform(agent_text_list)
            cos = cosine_similarity(text['tfidf'], agent_tfidf)
            # 類似順に取得
            news_rank = []
            for index in cos.argsort()[0][::-1]:
                news_rank.append(agent_name_list[index])
            text_list[column_index]['news_rank'] = news_rank

        return text_list
