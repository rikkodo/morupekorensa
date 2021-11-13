#!/usr/bin/env python
"""
sudachipyのトークナイザーラッパー
"""

from sudachipy import tokenizer, dictionary

DICTTYPE = "full"

DICTOBJECT = dictionary.Dictionary(dict_type=DICTTYPE).create()
SPLITMODE = tokenizer.Tokenizer.SplitMode.C


def tokenize(word):
    return DICTOBJECT.tokenize(word, SPLITMODE)


def list(word):
    tz = tokenize(word)
    for t in tz:
        print(t.surface(), t.part_of_speech(),
              t.reading_form(), t.normalized_form())
