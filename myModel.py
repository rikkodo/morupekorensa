#!/usr/bin/env python

"""
gensimのword2Vec利用ラッパー
"""
import random
import re
import myTokenizer
from typing import List

from gensim.models import KeyedVectors

MODEL_PATH = './input/entity_vector/entity_vector.model.bin'
MODEL = KeyedVectors.load_word2vec_format(MODEL_PATH, binary=True)


class TzPair:
    def __init__(self, tz, trans: str):
        self.tz = tz
        self.trans = trans

    def getToken(self):
        return self.tz

    def getTrans(self) -> str:
        return self.trans


def similars(word: str) -> List[str]:
    """
    単語に似た単語のリストを返す

    Parameters:
        word:
            判定対象の文字列

    Returns:
        類似文字列のリスト
        辞書内に対象の単語がない場合は引数の単語のみが含まれるリストを返す
    """
    ret = []
    if word in MODEL:
        sims = MODEL.most_similar(word)
        ret.extend([x[0] for x in sims])
    if len(ret) == 0:
        ret.append(word)
    return ret


def genRandom(tz, isReplace) -> TzPair:
    """
    トークン列を基に、ランダム変換したトークンを取得する

    Parameters:
        tz:
            変換元トークン

    Returns:
        変換後トークン + 変換経緯
    """
    ERASE = r'[（）「」『』｛｝【】＜＞＠”’！？｜～・()<>\[\]{}@\'\"!?|~-]'

    rets = ""
    trans: List[str] = []
    for t in tz:
        ts = str(t)
        if isReplace(t):
            sims = similars(ts)
            simts = random.choice(sims)

            # wikipedia辞書特化の話
            simts = simts.split('_')[0]  # _<補足>を切り取る
            if 'Category:' in sims:
                sims = sims.split('Category:')[1]

            simts = re.sub(ERASE, '', simts)

            trans.append("({}: {})".format(ts, simts))
            rets += simts
        else:
            trans.append(ts)
            rets += ts

    return TzPair(myTokenizer.tokenize(rets), " ".join(trans))
