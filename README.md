# 環境構築
pyenvのインストール  
```
brew install pyenv
```

pathを通すように設定
```
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

pyenvでのpythonのインストール
```
pyenv install 3.6.5
pyenv global 3.6.5
```

pipenvのインストール
```
brew install pipenv
```

packageの追加
```
pipenv install beautifulsoup4
```

mecabのインストール
```
https://www.saintsouth.net/blog/morphological-analysis-by-mecab-and-mecab-ipadic-neologd-and-python3/
```
