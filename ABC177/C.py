N = int(input())
A = [0] * N
A = list(map(int,input().split()))

ans = 0
mod = 10**9+7
# for i in range(N-1):
#     for j in range(i+1,N):
#         ans += (A[i]%mod) * (A[j]%mod)
#         ans %= mod

A = list(map(lambda x: x %mod,A))
for i in range(N-1):
    for j in range(i+1,N):
        ans += A[i] * A[j]
        ans %= mod
print(ans)