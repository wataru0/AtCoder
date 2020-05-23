
#import numpy as np
N,M,Q = map(int,input().split())

s = [[0 for i in range(3)] for j in range(Q)]

#point = [0] * N
for i in range(Q):
    s[i] = list(map(int,input().split()))
    
#nm = np.zeros((N,M))
nm = [[0 for _ in range(M)] for _ in range(N)]
point = [N] * M
for i in range(Q):
    if s[i][0] == 2: # nが問題mを解いた
        nm[s[i][1]-1][s[i][2]-1] = 1
        #clear = np.sum(nm,axis=0)
        point[s[i][2]-1] -= 1
    else:
        #clear = np.sum(nm,axis=0)

        # clear = [0]*M
        # for j in range(M):
        #     clear[j] = nm[:][j].count(1)

        # for j in range(N):
        #     for k in range(M):
        #         clear[k] += nm[j][k]
        ans = 0 
        for j in range(M): # とりあえずの全ての問題の得点をscoreに入れる
            if nm[s[i][1]-1][j] == 1:
                # ans += N - int(clear[j])
                ans += point[j]
                #ans += 1

        
        print(int(ans))
# print(nm)
#print("CC:",clear)

    



