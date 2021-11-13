#!/usr/bin/env python

"""
gensimのword2Vec利用ラッパー
"""

from gensim.models import KeyedVectors

MODEL_PATH = './input/entity_vector/entity_vector.model.bin'
MODEL = KeyedVectors.load_word2vec_format(MODEL_PATH, binary=True)


def similars(word):
    """
    単語に似た単語のリストを返す

    Parameters:
        word:
            判定対象の文字列

    Returns:
        類似文字列のリスト
        辞書内に対象の単語がない場合は引数の単語のみが含まれるリストを返す
    """
    if word not in MODEL:
        return [word]
    sims = MODEL.most_similar(word)
    return [x[0] for x in sims]
