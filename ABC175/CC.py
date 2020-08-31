X,K,D = map(int,input().split())
ans = 10**15
K = False
tmpK = False
tmpX = X
for i in range(K):
    if X>=0:
        X-=D
        if abs(X) < abs(tmpX):
            print(89)
            tmpX = abs(X)
            K = False
        else:
            print(2)
            K = True
    else:
        X+=D
        if abs(X) < abs(tmpX):
            print(1)
            tmpX = abs(X)
            K = False
        else:
            print(4)
            K = True
    if K and tmpK:
        break
    tmpK = K

print(tmpX)

