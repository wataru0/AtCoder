N,M = map(int,input().split())
A = [0]*M
B = [0]*M
G = [[] for _ in range(N+1)] # 探索するためのグラフ行列
for i in range(M):
    #A[i] , B[i] = map(int,input().split())
    a,b = map(int,input().split())
    # こうすることでインデックスが各部屋に，その要素が繋がっている部屋になる！
    G[a].append(b)
    G[b].append(a)

# あとは探索するだけ，時間内にできるかなぁ
#print(G) #[[], [2], [1, 3, 4], [2, 4], [3, 2]]

flag = True
dir = [0]*(N-1) # 道標の値
for i in range(1,N+1):
    #print(G[i])
    # if i == 1:#1と直接繋がっている部屋は１回いでいける
    #     dir[i-2] = 1
    if 1 in G[i]:#G内に1があったら，部屋１への道ある
        dir[i-2] = 1

        for j in range(len(G[i])):
            dir[G[i][j]-2] = 2
    

for k in dir: #dirのなかに０あったら道しるべおけない
    #print(dir)
    if k == 0:
        flag = False
        print(dir)
    

        

if flag:
    print("Yes")
    for i in range(len(dir)):
        print(dir[i])
else:
    print("No")