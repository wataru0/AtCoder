import math
A,B = map(float,input().split())
ans = 0
# if A > 100:
#     B *= 100
#     ans = int(A) * int(B)
#     ans = ans//100
#     print(ans)
# else:
#     ans = A*B
#     # print(ans)
#     print(int(ans))

B *= 1000
ans = int(A) * int(B)
ans = ans//1000
print(ans)