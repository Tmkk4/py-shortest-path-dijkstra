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
import sys

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
def findProxima(dst, isFixed):
    """
    最短距離未確定な都市集合にて, 最近傍都市を探索して返す(都市index:0-9)
    :param dst:都市間距離データ集合
    :param isFixed:最短距離確定フラグ  :: list[bool,...*10]; (1:確定済み, 0:未確定)
    :return:最近傍都市の都市index(0-9) or ステータスコード(-1:全都市最短路確定済み):: int
    """
    i = 0
    for i in range(len(isFixed)):
        # 確定フラグを確認
        if isFixed[i] is True:
            # 最短距離 確定済みの場合
            pass
        else:
            if (not isFixed[i+1]) and (dst[isFixed.index(i+1)] < dst[i]):
                # 都市i,i+1が最短路未確定 かつ 始点から都市i+1までの距離が始点から都市iまでの距離よりも短い場合
                i = i+1

    if i is isFixed[:-1]:
        # 全都市の最短距離が確定済みの場合 ステータスコード:-1 を返す
        return -1
    else:
        return i






def dijkstra(MAP, s, g):

    """
    与えられた都市(地点)間距離mapから 任意の2点間の最短路(距離)を返す
    :param dst: 都市間距離データ集合 :: list[[float],...]; '-'(pathなし(無限大)) : -1
    :param s: 求める最短経路の始点の都市index :: int
    :param g: 求める最短路の終点の都市index :: int
    :return: dijkstra法によって得られた最良最短経路とその距離 :: list[int(都市番号),int,...]
    """
    isFixed = [0 for i in range(N)]  # 最短距離確定フラグ :: list[bool,...*10] (0:未確定, 1:確定); 未確定で初期化
    dst = [-1 for j in range(N)] # 全都市の最短距離を無限遠(-1)に 初期化
    route = []  # 始点から終点までの最短経路ログ :: list[list[int(都市番号),...],float(最良最短路の距離)]

    dst[s] = 0  # initialize the distance to start point as 0
    route.append(s)  # 最短経路ログに始点都市sを追加
    while 1:
        # 最短距離未確定都市集合から最近傍都市を探索
        pinned = findProxima(dst, isFixed)
        if pinned == -1:
            # 全都市の最短路が確定済みの場合
            return
        if dst[pinned] >= sys.maxsize:
            # 距離がPy_ssize_t型変数のMAX (64bit:2**63-1)以上の場合 非連結グラフ→解なし
            return
        isFixed[pinned] = 1  # 都市pinnedまでの最短距離は確定
        route.append(pinned) # 最短経路ログに都市pinnedを追加
        for i in range(N):
            # 都市pinnedの隣の都市にて
            if (W[pinned][i] > 0) and (not isFixed[i]):
                # 道が繋がっている かつ 最短距離未確定の場合
                _dst= dst[pinned]+W[pinned][i]  # 始点-都市pinned-隣の都市iまでの距離

                if _dst < dst[i]:
                    # 既知の 都市iまでの距離より短い場合 都市iについての最短路を更新
                    dst[i] = _dst
                    route.append(i)  # 最短経路ログに都市iを追加
            if i == g:
                # 指定された終点へ到達した場合
                best = [route, dst[g]]
                return best


if __name__ == '__main__':
    # main()
    print(f"cities:{N},dst:{W}")
    s = input('start point(0-9):')
    g = input('goal point(0-9):')
    result = dijkstra(W, s, g)

    route = result[0]  # 始点から終点までの最短路訪問順列 :: list[int,...]
    dst_g = result[1]  # 始点から終点までの最短路距離 :: float

    if dst_g >= sys.maxsize:
        print("解なし:非連結グラフ")

    print(f"best solution path : {result}")
    print('-'*10)
    print(f"都市{s}から都市{g}まで...")
    print(f"経路:{str(route).replace(',','-').replace('[').replace(']')}")
    print(f"距離:{dst_g}")
    print('-' * 10)