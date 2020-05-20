N = int(input())
# リストの初期化
T = [0] * (N+1)
X = [0] * (N+1)
Y = [0] * (N+1)
sX = [0]
sY = [0]
for i in range(N):
    T[i+1], X[i+1], Y[i+1] = list(map(int,input().split()))

#print(T)

ans = False

for i in range(N):
    dt = T[i+1] - T[i]
    dist = abs(X[i+1]-X[i]) + abs(Y[i+1]-Y[i])
    #if T[i] >= X[i] + Y[i] and (X[i]+Y[i]%2 == T[i]%2):
    if dt >= dist and (dist%2 == dt%2):
        #print(T[i],X[i],Y[i])
        ans = True
    else:
        ans = False

if ans:
    print("Yes")
else:
    print("No")