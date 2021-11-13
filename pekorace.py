#!/usr/bin/env python
from gensim.models import KeyedVectors
import sys


def loadmodel(modelpath):
    return KeyedVectors.load_word2vec_format(modelpath, binary=True)


def main():
    model = loadmodel(sys.argv[1])
    sims = model.most_similar(sys.argv[2])
    print(sims)


if __name__ == "__main__":
    main()
