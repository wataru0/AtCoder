N = int(input())
L =list(map(int,input().split()))
ans = 0
for i in range(N):
    for j in range(i,N):
        for k in range(j,N):
            if L[i] != L[j] and L[i] != L[k] and L[j] != L[k]:
                # print(L[i],L[j],L[k])
                if L[i]+L[j]>L[k] and L[j]+L[k]>L[i] and L[k]+L[i]>L[j]:
                    ans += 1
print(ans)
