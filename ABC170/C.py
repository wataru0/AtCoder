X,N = map(int,input().split())
#p = [0]*N
p = list(map(int,input().split()))
ans = 0
tmp = []
tmpans = 0

for i in range(102):
    if i in p:
        continue
    else:
        if abs(X-ans)>abs(X-i):
            ans = i
            tmp.append(i)
            # if i < tmpans:
            #     ans = i
            # tmpans = ans
            # if ans == 0:
            #     ans = i
            # else:
            #     if ans > i:
            #         ans = i




print(ans)
#print(tmp)