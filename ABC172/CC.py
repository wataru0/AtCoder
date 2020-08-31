N,M,K = map(int,input().split())
A = [0]*N
B = [0]*M
A = list(map(int,input().split()))
B = list(map(int,input().split()))

b = []
b.append(0)
tmp = 0
for i in range(M):
    b.append(tmp+B[i])
    tmp = tmp+B[i]# M冊全部呼んだとする
a = [0]
for i in range(N):
    a.append(a[i]+A[i])
#print(b)
ans,j = 0,M
for i in range(N+1):
    if a[i]>K:
        break
    while b[j] > K - a[i]:#Kを超えてたらこの冊数読むの諦める
        j -= 1
    ans = max(ans,i+j)#最大冊数を更新していく

print(ans)
