# MORUPEKO RENSA

[勇者ヌルポコ](https://omocoro.jp/nurupoko/)のお題をマルコフ連鎖で作ろうという試み。

...だったが筆者がヌルポコをモルペコと思い違いしていたためこんな名前になった。

## REF

[Pythonを使いマルコフ連鎖で文章を自動生成する - 頑張らないために頑張る](https://ysko909.github.io/posts/how-to-use-markovify/)

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
