#!/usr/bin/env python
import sys
import random
import html
import re

from typing import List
from sudachipy.sudachipy import MorphemeList


import myTokenizer
import myModel


class TzPair:
    def __init__(self, tz: MorphemeList, trans: str):
        self.tz = tz
        self.trans = trans

    def getToken(self) -> MorphemeList:
        return self.tz

    def getTrans(self) -> str:
        return self.trans


def initList(inputpath: str) -> List[TzPair]:
    """
    ファイルからトークンのリストを作成する

    Parameters:
        inputpath:
            入力ファイルパス

    Returns:
        ファイル各行をトークン化したリスト
    """
    ret: List[TzPair] = []
    with open(inputpath, 'r') as f:
        for w in f:
            ws = w.strip()
            tz = myTokenizer.tokenize(ws)
            ret.append(TzPair(tz, ''))

    return ret


def genRandom(tz: MorphemeList) -> TzPair:
    """
    トークン列を基に、ランダム変換したトークンを取得する

    Parameters:
        tz:
            変換元トークン

    Returns:
        変換後トークン + 変換経緯
    """
    CHANGE = ['副詞', '名詞', '補助記号', '形状詞', '形容詞', '動詞']
    ERASE = r'[（）「」『』｛｝【】＜＞＠”’！？｜～・()<>\[\]{}@\'\"!?|~-]'

    rets = ""
    trans: List[str] = []
    for t in tz:
        ts = t.surface()
        if t.part_of_speech()[0] in CHANGE:
            sims = myModel.similars(ts)
            simts = random.choice(sims)
            simts = re.sub(ERASE, '', simts)

            trans.append("({}: {})".format(ts, simts))
            rets += simts
        else:
            trans.append(ts)
            rets += ts

    return TzPair(myTokenizer.tokenize(rets), " ".join(trans))


def main():
    if (len(sys.argv) < 3):
        print("Usage {} inputpath size", file=sys.stderr)
        exit(1)

    # ファイルの読み込み
    inputPath = sys.argv[1]
    wordlist = initList(inputPath)

    # ランダム部の作成
    size = int(sys.argv[2])
    for _ in range(size):
        idx = random.randint(0, len(wordlist)-1)
        tzp = genRandom(wordlist[idx].getToken())
        wordlist.append(tzp)

    # 出力
    for idx, tzp in enumerate(wordlist):
        tz = tzp.getToken()
        trans = tzp.getTrans()
        trans = html.escape(trans)
        sTz = myTokenizer.token2Str(tz)
        sTz = html.escape(sTz)
        print("{} <!-- {}: {} -->".format(sTz, idx, trans))


if __name__ == "__main__":
    main()
