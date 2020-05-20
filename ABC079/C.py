#abcd = list(map(int,input().split()))
abcd = input()
ans = ""
#print(abcd[0])

# tmp = int(abcd[0]) + int(abcd[1])
# print(tmp)

if int(abcd[0]) + int(abcd[1]) + int(abcd[2]) + int(abcd[3]) == 7:
    ans = abcd[0] + "+" + abcd[1] + "+" + abcd[2] + "+" + abcd[3] + "=7"
elif int(abcd[0]) + int(abcd[1]) + int(abcd[2]) - int(abcd[3]) == 7:
    ans = abcd[0] + "+" + abcd[1] + "+" + abcd[2] + "-" + abcd[3] + "=7"
elif int(abcd[0]) + int(abcd[1]) - int(abcd[2]) + int(abcd[3]) == 7:
    ans = abcd[0] + "+" + abcd[1] + "-" + abcd[2] + "+" + abcd[3] + "=7"
elif int(abcd[0]) + int(abcd[1]) - int(abcd[2]) - int(abcd[3]) == 7:
    ans = abcd[0] + "+" + abcd[1] + "-" + abcd[2] + "-" + abcd[3] + "=7"
elif int(abcd[0]) - int(abcd[1]) + int(abcd[2]) + int(abcd[3]) == 7:
    ans = abcd[0] + "-" + abcd[1] + "+" + abcd[2] + "+" + abcd[3] + "=7"
elif int(abcd[0]) - int(abcd[1]) + int(abcd[2]) - int(abcd[3]) == 7:
    ans = abcd[0] + "-" + abcd[1] + "+" + abcd[2] + "-" + abcd[3] + "=7"
elif int(abcd[0]) - int(abcd[1]) - int(abcd[2]) + int(abcd[3]) == 7:
    ans = abcd[0] + "-" + abcd[1] + "-" + abcd[2] + "+" + abcd[3] + "=7"
elif int(abcd[0]) - int(abcd[1]) - int(abcd[2]) - int(abcd[3]) == 7:
    ans = abcd[0] + "-" + abcd[1] + "-" + abcd[2] + "-" + abcd[3] + "=7"

print(ans)


# for i in range(2):
#     for j in range(2):
#         for k in range(2):
#             if k == 0:
#                 tmp = int(abcd[0]) + int(abcd[1]) + int(abcd[2]) + int(abcd[3])
#                 if tmp == 7:
#                     ans = abcd[0] + "+" + abcd[1] + "+" + abcd[2] + "+" + abcd[3] + "=7"
#             if k == 1:
#                 tmp = int(abcd[0]) + int(abcd[1]) + int(abcd[2]) - int(abcd[3])
#                 if tmp == 7:
#                     ans = abcd[0] + "+" + abcd[1] + "+" + abcd[2] + "-" + abcd[3] + "=7"