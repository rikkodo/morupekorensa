#!/usr/bin/env python

from typing import List


def initList(inputpath: str) -> List[str]:
    """
    ファイルから文字列のリストを作成する

    Parameters:
        inputpath:
            入力ファイルパス

    Returns:
        ファイル各行の文字列リスト
    """
    with open(inputpath, 'r') as f:
        ret = f.read().splitlines()

    return ret
