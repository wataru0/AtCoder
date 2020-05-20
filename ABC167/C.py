import numpy as np
N,M,X = map(int,input().split())
CA = np.zeros((N,M+1))
C = [0] * N
A = np.zeros((N,M))
# C = [0]*N
# A = []
# CA = []
for i in range(N):
    # C[i] = map(int,input().split())
    # for j range(M):
    #     CA[i][j] = map(int,input().split())

    CA[i][:] = list(map(int,input().split())) # --これ正解
    #C[i],A[i][:] = list(map(int,input().split())) # できない


#print(CA)
# print(np.min(CA,axis=0)) # これで一番安い参考書情報取得できる
# print(CA[:,0]) #これで列取得
C = CA[:,0] # これで縦のN次元リスト取得できる
AA = CA[:,1:] # これでAの部分の行列（二次元配列）が取得できる
#print(AA)
#print(C)
#print(min(C))

# -- ans---
# 全探索でできる

# for i in range(N):
#     bit = bin(1<<i) # 取りうる全てのパターン
#     print(bin(1<<i))

INF = int(1001001001)
ans = INF
for i in range(2**len(C)): # 2**nパターン考えられる
    buy = []
    cost = 0
    d = [0]*M #理解度を格納するリスト
    for j in range(N):
        # 順に右シフトさせ最下位bitのチェックを行う
        # 10進のまま書いてもビット演算すると2進として計算してくれる！
        if ((i>>j) & 1): 
            buy.append(C[j])
            cost += C[j] # 価格を足す
            for k in range(M): # 買った参考書の理解度を足す
                d[k] += AA[j][k]
    #print(buy) # 上手く全パターン取得できた
    # 理解度の合計を計算
    flag = True
    for l in range(M):
        #print(d[l])
        if d[l] < X:
            flag = False
        if flag:
            ans = min(ans,cost)

if ans == INF :
    print("-1")
else:
    print(int(ans))


    

