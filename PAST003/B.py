import numpy as np
N,M,Q = map(int,input().split())
#s = np.zeros((Q,3))
s = [[0 for i in range(3)] for j in range(Q)]
for i in range(Q):
    s[i] = list(map(int,input().split()))

# print(s)
# print(s[0][0])
#score = [0]*N #nの点数->解いた問題数
#clear = [0]*M #mを解いた人の人数
#nm = [[0 for _ in range(M)]for _ in range(N)] #nがmを解けたかどうか判定する行列
nm = np.zeros((N,M))
#print(nm)

for i in range(Q):
    if s[i][0] == 2: # nが問題mを解いた
        # clear[s[i][2]] += 1
        # score[s[i][1]] += 1
        nm[s[i][1]-1][s[i][2]-1] = 1
        #clear[s[i][2]-1] += 1
    #elif s[i][0] == 1: # nの点数を出力
    else:
        #ans = N - np.sum(nm,axis=0)
        #score = [0]*M
        clear = np.sum(nm,axis=0)
        ans = 0 
        for j in range(M): # とりあえずの全ての問題の得点をscoreに入れる
            #score[j] = N - clear[j]
            if nm[s[i][1]-1][j] == 1:
                #ans += score[j]
                ans += N - clear[j]
        
        print(int(ans))

#print(nm)
#print(np.sum(nm,axis=0)) # 列ごとに要素の合計値を出す
#print(score)

