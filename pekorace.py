#!/usr/bin/env python
import sys
import random
import html

import myUtil
import myTokenizer
import myModel


def main():
    if (len(sys.argv) < 3):
        print("Usage {} inputpath size", file=sys.stderr)
        exit(1)

    # ファイルの読み込み
    inputPath = sys.argv[1]
    strlist = myUtil.initList(inputPath)
    wordlist = myTokenizer.toMorphemeList(strlist)

    # ランダム部の作成/出力
    size = int(sys.argv[2])
    for _ in range(size):
        idx = random.randint(0, len(wordlist)-1)
        tzp = myModel.genRandom(wordlist[idx], myTokenizer.isReplace)

        tz = tzp.getToken()
        tzs = myTokenizer.token2Str(tz)
        tzs = html.escape(tzs)
        trans = tzp.getTrans()
        trans = html.escape(trans)

        print("{}  <!-- {} -->".format(tzs, trans))
        wordlist.append(tz)


if __name__ == "__main__":
    main()
