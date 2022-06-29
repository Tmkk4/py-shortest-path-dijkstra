# -*- coding:utf-8 -*-
"""
    2022/06/28
    System Development A Work No.05 on Python 3.8
    制作物 No.05 「ダイクストラ法による最短経路問題の実装」
    # 基本仕様
        - 最短距離を求める最短経路問題をダイクストラ法を用いて実装する
        - 全部で10地点に対して, 2次元配列で各地点の距離データ与えられたときに,
          任意の2点間の最短距離を求める

    # 技術仕様
        - 経路をテキストで表示させる
            e.g.) 1-4-7
        - 距離を示すデータは浮動小数点数に対応させる
        - 単独動作アプリ
        - 大部分のコードを他からコピーしない
    # refs:
        - dijkstra法 : https://nw.tsuda.ac.jp/lec/dijkstra/ ,

"""
N = 10  # the number of cities / points(default:10)
dst =
def dijkstra(dst):
    """
    与えられた都市(地点)間距離mapから 任意の2点間の最短路(距離)を返す
    :param dst: 
    :return: 
    """"""