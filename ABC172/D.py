N = int(input())



ans = 0
for K in range(1,N+1):
    fx = 0
    for i in range(1,K+1):
        if K%i==0:
            fx += 1
    ans += K * fx

print(ans)

