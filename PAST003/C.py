A,R,N = map(int,input().split())

# ansH = A*(1-R**N)/(1-R)
# ansL = A*(1-R**(N-1))/(1-R)
# if ansH-ansL > 10**9:
#     print('large')
# else:
#     print(int(ansH-ansL))

ans = A
border = 1000000000
flag = True
for i in range(N-1):
    ans *= R
    if ans > border:
        flag = False
        break
    

if flag:
    print(ans)
else:
    print('large')

# ans = A*R**(N-1)
# sikii = 10**9
# if ans > sikii:
#     print('large')
# else:
#     print(ans)