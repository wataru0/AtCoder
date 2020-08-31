import copy
N,M,K = map(int,input().split())
A = [0]*N
B = [0]*M
A = list(map(int,input().split()))
B = list(map(int,input().split()))
a = 0
b = 0

tmp = 0
ans = 0
# for i in range(200000):
#     if A[a] < B[b]:
#         if tmp <= K:
#             tmp += A[a]
#             ans += 1
#             a += 1
#     elif A[a] > B[b]:
#         if tmp <= K:
#             tmp += B[b]
#             ans += 1
#             b += 1
#     if a > len(A)-1 or b > len(B)-1:
#         break
fa = False
fb = False
flag = False
if sum(A)+sum(B)<=K:
    print(len(A)+len(B))
else:
    while len(A) > 0 or len(B) > 0:
        AA = copy.copy(A)
        BB = copy.copy(B)
        if len(AA) != 0:
            a = AA.pop(0)
            fa = True
        if len(BB) != 0:
            b = BB.pop(0)
            fb = True
        if fa and fb:
            if a<=b:
                tmp += a
                ans += 1
                A = AA
            else:
                tmp += b
                ans += 1
                B = BB
        else:
            if fa:
                tmp += a
                ans += 1
                A = AA
            if fb:
                tmp += b
                ans += 1
                B = BB

        if tmp > K:
            if len(A) == 0 and len(B)==0:
                flag = True
            break
        if len(A) == 0 and len(B)==0:
            flag = True
        fa = False
        fb = False
        
        #print(tmp,A,B)
        
    if flag:
        print(ans)
    else:
        print(ans-1)
