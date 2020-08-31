C = list(map(int,input().split()))
A = list(input().split())
ans = 0
for i in range(len(C)):
    if A[i] == 'Alice':
        ans += C[i]

print(ans)