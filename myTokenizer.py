#!/usr/bin/env python
"""
sudachipyのトークナイザーラッパー
"""

from types import ModuleType
from typing import List

from sudachipy import tokenizer, dictionary
from sudachipy.sudachipy import MorphemeList

DICTTYPE = "full"

DICTOBJECT = dictionary.Dictionary(dict_type=DICTTYPE).create()
SPLITMODE = tokenizer.Tokenizer.SplitMode.C

CHANGE = ['副詞', '名詞', '補助記号', '形状詞', '形容詞', '動詞']


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
        word:
            トークン化対象の文字列

    Returns:
        トークン化したword
    """
    return "".join([t.surface() for t in token])


def toMorphemeList(slist: List[str]) -> List[MorphemeList]:
    """
    文字列リストをトークンリストに変換する

    Parameters:
        slist:
            トークン化対象の文字列集合

    Returns:
        トークン化したリスト

    """
    return [tokenize(w) for w in slist]


def isReplace(t: ModuleType) -> bool:
    """
    変換対象の品詞かを判定する
    """
    return t.part_of_speech()[0] in CHANGE


def getHinshiList(ml: List[MorphemeList]) -> List[str]:
    s = set()

    for tz in ml:
        for t in tz:
            s.add(t.part_of_speech()[0])

    return sorted(list(s))
