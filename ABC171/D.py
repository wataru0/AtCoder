N = int(input())
A = [0]*N
A = list(map(int,input().split()))
Q = int(input())
B = [0]*Q
C = [0]*Q
for i in range(Q):
    B[i],C[i] = map(int,input().split())


S = [0]*Q
# for i in range(Q):
#     for j in range(N):
#         if A[j] == B[i]:
#             A[j] = C[i]
#     for k in range(N):
#         S[i] += A[k] 
# for i in range(Q):
#     print(S[i])

cnt = [0] * 100005 # Aの数字の数を格納する，カウント配列
for i in A:
    cnt[i]+=1 

tot = sum(A)
for i in range(Q):
    #合計値の変動
    tot -= B[i]*cnt[B[i]]
    tot -= C[i]*cnt[C[i]]
    #カウント配列の変動
    cnt[C[i]] += cnt[B[i]]
    cnt[B[i]] = 0
    #合計値の変動
    tot += B[i]*cnt[B[i]]
    tot += C[i]*cnt[C[i]]
    print(tot)

