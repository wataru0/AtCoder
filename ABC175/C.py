X,K,D = map(int,input().split())

ans = 10**15 
K = False
tmpK = False
for i in range(K):
    if X>=0:
        X-=D
        if abs(X) < abs(ans):
            ans = abs(X)
            K = False
        else:
            K = True
            print(12)
    else:
        X+=D
        if abs(X) < abs(ans):
            ans = abs(X)
            K = False
        else:
            K = True
    if K and tmpK:
        break
    tmpK = K

print(ans)

