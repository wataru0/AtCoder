N,M = map(int,input().split())
S = [0]*M
C = [0]*M
for i in range(M):
    S[i],C[i] = map(int,input().split())

flag = False
for num in range(1000):
    NUM = str(num)
    for i in range(M):
        if len(NUM) == N and NUM[S[i]-1]==C[i]:
            ans = NUM
            flag = True
    

if flag:
    print(ans)
else:
    print(-1)
