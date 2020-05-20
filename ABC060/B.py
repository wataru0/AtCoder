A,B,C = map(int,input().split())
flag = False
for i in range(B):
    tmp = i*A%B
    if tmp == C:
        flag = True

if flag:
    print("YES")
else:
    print("NO")

