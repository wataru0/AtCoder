K,N = map(int,input().split())
A = list(map(int,input().split()))
base = 0
ans = 0

maxdis = 0
for i in range(N):
    if i == N-1:
        maxdis = max(maxdis,K-A[i]+A[0])
    else:
        maxdis = max(maxdis,A[i+1]-A[i])
ans = K- maxdis
print(ans)
