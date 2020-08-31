N,M = map(int,input().split())
# ue,sita,uee,sitaa = 0,0,0,0
# tmpN,tmpM = 0,0
# if N != 2:
#     for i in range(N+1):
#         ue *= N-i
#         sita *= N-2-i
#     tmpN = ue/sita
# if M != 2:
#     for i in range(M+1):
#         uee *= N-i
#         sitaa *= N-2-i
#     tmpM = uee/sitaa

# print(tmpN+tmpM)

ans = N*(N-1)/2 + M*(M-1)/2

print(int(ans))