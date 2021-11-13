#!/usr/bin/env python

from typing import List
import sys
from glob import iglob

from sudachipy import tokenizer, dictionary
import markovify

STATE_SIZE = 2
MAX_CHARS = 140


def loadFile(inputpaths: List[str]) -> str:
    """
    パス一覧に含まれるファイル全体を結合した文字列を返す

    Args:
        inputpaths:
            入力とするファイルのパス一覧

    Returns:
        ファイル全体を結合した文字列
    """
    text = ""

    for inputpath in inputpaths:
        for path in iglob(inputpath):
            with open(path, 'r') as f:
                text += f.read().strip()

    return text


def splitText(texts: str) -> str:
    """
    文字列を分かち書きテキストに変換する。改行コードは維持し、記号は考えない。

    Args:
        texts:
            分かち書き対象の文字列

    """

    torknizer_obj = dictionary.Dictionary().create()
    mode = tokenizer.Tokenizer.SplitMode.C

    words = [m.surface() for m in torknizer_obj.tokenize(texts, mode)]
    s_text = ' '.join(words)
    return s_text


def main(inputpaths: List[str], count: int) -> None:
    text = loadFile(inputpaths)
    splited_text = splitText(text)

    text_model = markovify.NewlineText(splited_text, state_size=STATE_SIZE)

    gened_texts: List[str] = []

    for _ in range(count):
        gened_text = text_model.make_short_sentence(MAX_CHARS, tries=100)
        gened_texts.append(gened_text)

    print("\n".join(gened_texts))


if __name__ == "__main__":
    if (len(sys.argv) < 3):
        print("Usage {} count [inputs]".format(sys.argv[0]), file=sys.stderr)
        exit(1)
    main(sys.argv[2:], int(sys.argv[1]))
