A = ['']*3
for i in range(3):
    A[i] = list(map(int,input().split()))
N = int(input())
B = [0]*N
for i in range(N):
    B[i] = int(input())

# print(A)
# print(A[0][0])
# print(A[0].index(66))
for b in B:
    for i in range(3):
        if b in A[i]:
            # print(b)
            A[i][A[i].index(b)] = 0
        


flag = False
for i in range(3):
    if A[i][0] == A[i][1] == A[i][2] == 0:
        flag = True
    if A[0][i] == A[1][i] == A[2][i] == 0:
        flag = True
if A[0][0] == A[1][1] == A[2][2] == 0:
    flag = True
if A[0][2] == A[1][1] == A[2][0] == 0:
    flag = True
if flag:
    print('Yes')
else:
    print('No')