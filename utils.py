import MeCab
from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity


class Utils:

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
        for url, text in text_list.items():
            vectorizer = TfidfVectorizer(
                analyzer=self.to_stem, min_df=1, max_df=50)
            tfidf_list = vectorizer.fit_transform(text['full_text'])
            text_list[url]['tfidf'] = tfidf_list.toarray()[0]

            # 単語ごとのtfidf値出力
            print('対象URL:' + str(url))
            tfidfs = tfidf_list.toarray()[0]
            terms = vectorizer.get_feature_names()

            for term in terms:
                tfidf = tfidfs[terms.index(term)]
                if tfidf > 0:
                    print(term + ':' + str(tfidf))

        return text_list

    # def cos_similarity(self, text_list):
    #     documents = self.tfidf(text_list)
    #
    #     tag = list(text_list.keys())
    #
    #     cs_array = cosine_similarity(documents, documents)

        # for i, cs_item in enumerate(cs_array):
        #     print("[" + tag[i] + "]")
        #     cs_dic = {}
        #     for j, cs in enumerate(cs_item):
        #         print(j)
        #     if round(cs - 1.0, 5) != 0:
        #         cs_dic[tag[j]] = cs
        #
        # for k, v in sorted(cs_dic.items(), key=lambda x:x[1], reverse=True):
        #     print("\t" + k + " : " + str(v))
