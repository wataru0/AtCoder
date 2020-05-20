S = input()
T = input()
flag = False
tmpT = T[:-1]

#print(tmpT)

if S == tmpT:
    flag = True

if flag:
    print("Yes")
else:
    print("No")