# 環境構築
## pyenvのインストール  
```
brew install pyenv
```

## pathを通すように設定する
```
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

## pyenvでのpythonのインストール
```
pyenv install 3.6.5
pyenv global 3.6.5
```

## pipenvのインストール
```
brew install pipenv
```

## 各種packageのインストール
```
pipenv install
```

## mecabのインストール
 `https://www.saintsouth.net/blog/morphological-analysis-by-mecab-and-mecab-ipadic-neologd-and-python3/`
```
$ GITHOME="${HOME}/git"
$ mkdir -p ${GITHOME}
$ cd ${GITHOME}
$ git clone https://github.com/taku910/mecab.git
  
$ cd ${GITHOME}/mecab/mecab
$ ./configure --enable-utf8-only
$ make
$ make check
$ sudo make install
```

## mecab-ipadic-NEologd のインストール
```
$ cd ${GITHOME}
$ git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
  
$ cd ${GITHOME}/mecab-ipadic-neologd
$ ./bin/install-mecab-ipadic-neologd
```

## インストール状況確認
```
$ where mecab
> /usr/local/bin/mecab
  
$ ls /usr/local/lib/mecab/dic/
> mecab-ipadic-neologd/
```
※neologdのpathが異なる場合、utils.pyのファイルパスを変更してください

## client_secret.jsonの配置
[こちらを参考](https://www.kumilog.net/entry/2018/03/22/090000)に、client_secret.jsonを取得、
リポジトリ直下に配置してください。

## Googleフォームの集計スプレットシートを編集
集計シートとは別に新規でシートを作成して、`agent`と名付けてください。
ヘッダ行を以下として、マッチング対象となりえるエージェントの情報を記載してください。
```
名前	紹介URL	性別	年齢	直近の業界	直近の職種	現年収	転職する際に興味がある働き方
```

## シートIDの編集
集計スプレットシートを編集したら、プログラム内で指定しているシートIDを編集する必要があります。
`news/lib/googleapi.py`の`SPREAD_SHEET_ID`を適切な値に変更してください。
([シートIDの確認方法](http://amehal.blogspot.com/2015/10/id.html))

## 実行
1. Googleフォームから求職者の情報を入力し、集計スプレットシートに値が入力されていることを確認
2. コンソールから`pipenv run start`
3. 集計スプレットシートの最右にエージェントごとの評価点数が入力されていることを確認

# Tips
## 各種パラメータについて
`constants.py`の`points_dic`変数が項目ごとの配点です。完全一致した場合に配点されるようになっています。
内部ロジックで「気になるニュース」と「エージェントの紹介文」の類似度を計算し、順位付けしています。
`points_news_dic`は順位ごとの配点を設定しています。

## ファイル構造
```
.
├── Pipfile
├── Pipfile.lock
├── README.md
├── client_secret.json
├── constants.py
├── lib
│   ├── crawl.py
│   ├── googleapi.py
│   └── sklearn.py
├── main.py
├── repositories
│   ├── agents.py
│   └── job_seekers.py
├── services
│   ├── agents.py
│   ├── crawl.py
│   ├── job_seekers.py
│   ├── language_processing.py
│   └── matching.py
└── utils.py
```

| ファイル名 | ファイル説明 |  
|:-----------|------------:|  
| Pipfile       | 各種パッケージやスクリプト設定        |  
| Pipfile.lock       | 各種パッケージのバージョン管理        |  
| README.md       | 本書        |  
| client_secret.json       | googleapiを使用するための設定ファイル        |  
| constants.py       | パラメータ設定ファイル        |  
| lib/       | 外部ライブラリ使用系ファイル        |  
| main.py       | メイン実行ロジック        |  
| repositories/       | DBやスプレットシートへ永続化する責務をもつファイル群        |  
| services/       | サービス全般の責務をもつファイル群        |  
| utils.py       | 汎用系処理ファイル        |  

