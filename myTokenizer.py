#!/usr/bin/env python
"""
sudachipyのトークナイザーラッパー
"""

from sudachipy import tokenizer, dictionary
from sudachipy.sudachipy import MorphemeList

DICTTYPE = "full"

DICTOBJECT = dictionary.Dictionary(dict_type=DICTTYPE).create()
SPLITMODE = tokenizer.Tokenizer.SplitMode.C


def tokenize(word: str) -> MorphemeList:
    """
    トークン化処理

    Parameters:
        word:
            トークン化対象の文字列

    Returns:
        トークン化したword
    """
    return DICTOBJECT.tokenize(word, SPLITMODE)


def listToken(token: MorphemeList) -> None:
    """
    トークンを出力する

    Parameters:
        token:
            出力対象のトークン
    """
    for t in token:
        print(t.surface(), t.part_of_speech(),
              t.reading_form(), t.normalized_form())


def listWord(word: str) -> None:
    """
    単語をトークン化し結果を出力する

    Parameters:
        word:
            出力対象の文字列
    """
    listToken(tokenize(word))


def token2Str(token: MorphemeList) -> str:
    """
    トークンを文字列に逆変換する

    Parameters:
        word str:
            トークン化対象の文字列

    Returns:
        トークン化したword
    """
    return "".join([t.surface() for t in token])
