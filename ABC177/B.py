S = input()
T = input()

tmpT = ""
# for i in range(len(S)):
#     for j in range(len(T)):
#         if S[i] == T[j]:
#             tmp += 1
#             if i < len(S) - 1:
#                 if S[i+1]
ans = len(T)
# for i in range(len(T)):
#     tmpT = T[i]
#     if tmpT in S:
#         ans -= 1
#         tmpT += T[i]

tmp = 0
# for i in range(len(T)):
#     if T[i] in S:
#         tmp = 1
#         tmpT = T[i]
#         for j in range(i+1,len(T)):
#             tmpT+=T[j]
#             if tmpT in S:
#                 tmp += 1
#             else:
#                 break
def a(s,t):
    if t in s:
        return ans - 1
    else:
        return ans
for i in range(len(T)):
    if T[i] in S:
        tmp = 1
        tmpT = T[i]
        for j in range(i+1,len(T)):
            tmpT+=T[j]
            if tmpT in S:
                tmp += 1
            else:
                break

print(ans)