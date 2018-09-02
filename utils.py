import MeCab


class Utils:

    @staticmethod
    def split(text, to_stem=False):
        tagger = MeCab.Tagger()  # 別のTaggerを使ってもいい
        mecab_result = tagger.parse(text)
        info_of_words = mecab_result.split('\n')
        words = []
        for info in info_of_words:
            # macabで分けると、文の最後に’’が、その手前に'EOS'が来る
            if info == 'EOS' or info == '':
                break
                # info => 'な\t助詞,終助詞,*,*,*,*,な,ナ,ナ'
            info_elems = info.split(',')
            # 6番目に、無活用系の単語が入る。もし6番目が'*'だったら0番目を入れる
            if info_elems[6] == '*':
                # info_elems[0] => 'ヴァンロッサム\t名詞'
                words.append(info_elems[0][:-3])
                continue
            if to_stem:
                # 語幹に変換
                words.append(info_elems[6])
                continue
            # 語をそのまま
            words.append(info_elems[0][:-3])
        return words

    def to_words(self, text_list):
        # to_stemは調査必要
        for url, text in text_list.items():
            words = self.split(text=text, to_stem=False)
            text_list[url] = words

        return text_list
