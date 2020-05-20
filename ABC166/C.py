N,M = map(int,input().split())
H = list(map(int,input().split()))
A = [0]*M
B = [0]*M
Gab = [] # グラフ
g = [[] for _ in range(N+1)]
for i in range(M):
    #A[i],B[i] = map(int,input().split())
    #Gab.append(list(map(int,input().split()))) #グラフを表現する時こう書く

    #各ノードiがどのノードと繋がっているかをリストに格納する処理！！！
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

#print(A,B)
ans = 0

for i in range(1,N+1):#i番目のノードについて
    for j in g[i]: #i番目のノードと繋がっているノードとの高さを比較
        if H[i-1] <= H[j-1]:
            break
    else:
        ans+=1




#print(g)
print(ans)
#print(Gab)


