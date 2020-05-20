A,B,C,D = map(int,input().split())
ans = 0

# if B >= C:
#     if D >= A:
#         if A <= C:
#             ans = B-C
#         if A > C:
#             ans = B-A
    

# elif B >= D:
#     if D >= A:
#         if A <= C :
#             ans = D-C
#         if A > C:
#             ans = D-A

# BとDのうち小さい方-AとCのうち大きい方　で求まる
if min(B,D)>=max(A,C):
    ans = min(B,D)-max(A,C)

    


print(ans)