N = int(input())
ans = ''

num2alhp = lambda c :chr(c+97)
n = N
# N -= 1
#print(num2alhp(1)) # a
amari = 0
ans = []
i = 0
if n < 26:
    amari = n
    ans.append(num2alhp(amari))
else:
    while True:
        amari = N % 26
        #print(amari)
        
        ans.append(num2alhp(amari))
        
        N = N // 26
        i += 1

        if N == 0:
            break

ANS = ''
for i in range(len(ans)-1,-1,-1):
    ANS += ans[i]
print(ANS)
# #文字列反転
# ans = ''
# for i in range(len(amari)-1,-1,-1):
#     ans += amari[i]
# print(amari)
# print(ans)
# ANS=''
# for i in range(len(ans)):
#     ANS += num2alhp(int(ans[i]))
# print(ANS)