N,M = map(int,input().split())
S = [0] * M
C = [0] * M
for i in range(M):
    S[i],C[i] = map(int,input().split())


ans = [0,0,0]
# print(ans[0])
flag = True
if len(list(set(S))) == len(S) or len(list(set(S))) == len(list(set(C))):
    for i in range(M):
        ans[S[i]-1] = C[i]

    A =''
    for i in range(len(ans)):
        A += str(ans[i])
    if A[0]=='0':
        print(-1)
    else:
        print(A)
else:
    print(-1)