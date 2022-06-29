# -*- coding:utf-8 -*-
"""
    2022/06/28
    System Development A Work No.05 on Python 3.8
    制作物 No.05 「ダイクストラ法による最短経路問題の実装」
    # 基本仕様
        - 最短距離を求める最短経路問題をダイクストラ法を用いて実装する
        - 全部で10地点に対して, 2次元配列(隣接行列)で各地点の距離データ与えられたときに,
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
# globals

"""
W = [[-1.0] * 10 for i in range(10)]  # init distances of all points as infinity
for j in N:
    for k in N:
        if j == k:
            W[j][k] = 0  # 同一点間の距離は0
"""
W = [[0.0, 1.0, 7.0, 2.0, -1.0, -1.0, -1.0, 9.0, -1.0, -1.0],
       [1.0, 0.0, -1.0, -1.0, 2.0, 4.0, -1.0, -1.0, 8.0, -1.0],
       [7.0, -1.0, 0.0, -1.0, -1.0, 2.0, 3.0, -1.0, 7.0, -1.0],
       [2.0, -1.0, -1.0, 0.0, -1.0, -1.0, 5.0, -1.0, 5.0, -1.0],
       [-1.0, 2.0, -1.0, -1.0, 0.0, 1.0, -1.0, -1.0, 4.0, 1.0],
       [-1.0, 4.0, 2.0, -1.0, 1.0, 0.0, -1.0, 6.0, 4.0, -1.0],
       [-1.0, -1.0, 3.0, 5.0, -1.0, -1.0, 0.0, 2.0, 2.0, 2.5],
       [-1.0, -1.0, -1.0, -1.0, -1.0, 6.0, 2.0, 0.0, 1.5, 0.5],
       [-1.0, -1.0, -1.0, -1.0, -1.0, 2.7, 1.0, 1.0, 0.0, 1.9],
       [-1.0, -1.0, -1.0, -1.0, -1.0, 2.2, 1.0, 2.0, 1.0, 0.0]]
# distances of between cities (10 cities) :: [[float,...*10]*10]
N = len(W)  # the number of cities / points(default:10) :: int
def findMin(dst, isFixed):
    """
    最短距離未確定な都市集合にて, 最近傍都市を探索して返す(都市index:0-9)
    :param dst:都市間距離データ集合
    :param isFixed:最短距離確定フラグ  :: list[bool,...*10]; (1:確定済み, 0:未確定)
    :return:最近傍都市の都市index or ステータスコード:: int
    """

def dijkstra(W, s, g):

    """
    与えられた都市(地点)間距離mapから 任意の2点間の最短路(距離)を返す
    :param dst: 都市間距離データ集合 :: list[[float],...]; '-'(pathなし(無限大)) : -1
    :param s: 求める最短経路の始点の都市index :: int
    :param g: 求める最短路の終点の都市index :: int
    :return: dijkstra法によって得られた最良最短経路 :: list[int(都市番号),int,...]
    """
    isFixed = [0 for i in range(N)]  # 最短距離確定フラグ :: list[bool,...*10] (0:未確定, 1:確定); 未確定で初期化
    dst = [-1 for j in range(N)] # 全都市の最短距離を無限遠(-1)に 初期化

    dst[s] = 0  # initialize the distance to start point as 0
    return best


if __name__ == '__main__':
    # main()
    #dst = [[]]
    print(f"cities:{N},dst:{dst}")
    s = input('start point:')
    g = input('goal point:')
    result = dijkstra(dst, s, g)
    print(f"best solution path : "{result})