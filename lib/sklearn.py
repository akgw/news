import MeCab
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class SklearnLib:

    def __init__(self):
        self.vectorizer = TfidfVectorizer(
            analyzer=self.__to_stem, min_df=1, max_df=50)
        self.tagger = MeCab.Tagger(
            '-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')

    def __to_stem(self, text):
        return self.__split(text=text, to_stem=True)

    def __split(self, text, to_stem=False):
        mecab_result = self.tagger.parse(text)
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

    # 対象textのtfidf値を取得
    def calc_tfidf(self, text):
        return self.vectorizer.fit_transform([text]).toarray()

    # agent_text_listと対象のtextのcos類似度を取得
    def calc_cos_similarity(self, agent_text_list, tfidf):
        agent_tfidf = self.vectorizer.transform(agent_text_list)
        return cosine_similarity(tfidf, agent_tfidf)
