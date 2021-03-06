# MORUPEKO RENSA

[勇者ヌルポコ](https://omocoro.jp/nurupoko/)のお題をマルコフ連鎖で作ろうという試み。

...だったが筆者がヌルポコをモルペコと思い違いしていたためこんな名前になった。

結局マルコフ連鎖では微妙だったので、品詞分解->word2vecで似た単語に置換するという単純な方法を使用。

## TODO

* 変換候補から、品詞や活用が一致するものだけを抽出する機構。品詞や活用が変わると意味がわからなくなる。モデルとトークナイザが蜜結合するのが嫌

## REF

[Pythonを使いマルコフ連鎖で文章を自動生成する - 頑張らないために頑張る](https://ysko909.github.io/posts/how-to-use-markovify/)
[学習済みWord2Vec モデルをサクッと使ってみる | cedro-blog](http://cedro3.com/ai/word2vec-gensim/#google_vignette)

## 準備

* python
* pyenv
* pipenv

```sh
pipenv install [--dev]
```

## 辞書の変更

```sh
# to small
sudachipy link -t small

# to full
sudachipy link -t full

# to core(defalut)
sudachipy link -u
```

## word2vec

[東北大の](http://www.cl.ecei.tohoku.ac.jp/~m-suzuki/jawiki_vector/)を解凍し、`./input/entity_vector/entity_vector.model.bin`に配置する。

## 単語生成

```sh
./pekorace.py 入力を一行ごとに書いたテキスト 新たに生成する単語数
```
