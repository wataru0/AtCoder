S = input()
# a = '1'
# b = '5'
# print(a+b)
ans = 0
for i in range(len(S)):
    tmp = S[i]
    for j in range(i+1,len(S)):
        tmp += S[j]
        # print(tmp)
        if int(tmp)%2019 == 0 :
            ans += 1

    tmp = ""

print(ans)
