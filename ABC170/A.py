X = list(map(int,input().split()))
ans = 0
for i in range(len(X)):
    if X[i]==0:
        ans=i
        break

print(ans+1)