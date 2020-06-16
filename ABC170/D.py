N = int(input())
A = list(map(int,input().split()))
ans = 0
tmp = []
flag = [0]*N
for i in range(N):
    f = 0
    for j in range(N):
        if i == j:
            continue
        else:
            if A[i]%A[j]==0:
                f=1
                break
    if f == 0:
        ans += 1
    

print(ans)
# print(tmp)
# print(flag)