S = input()

ans = 0
tmp = ''
for i in range(len(S)):
    if S[i]=='R':
        tmp += '1'
    if S[i]=='S':
        tmp += '0'

if tmp == '111':
    print(3)
elif tmp == '110':
    print(2)
elif tmp == '101':
    print(1)
elif tmp == '011':
    print(2)
elif tmp == '100':
    print(1)
elif tmp == '010':
    print(1)       
elif tmp == '001':
    print(1)
else:
    print(0)