import math
N,D = map(int,input().split())
X = [0] * N
Y = [0] * N
for i in range(N):
    X[i],Y[i] = map(int,input().split())

ans = 0
tmp = 0
for i in range(N):
    tmp = math.sqrt(X[i]**2+Y[i]**2)
    if tmp <= D:
        ans +=1
    tmp = 0
print(ans)