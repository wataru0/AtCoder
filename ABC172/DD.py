N = int(input())

ans = 0
# kaito
# for i in range(N+1):
#     for j in range(N+1):
#         if i % j == 0:
#             ans += 1

# print(ans)

# teian1
# F = [0]*(N+1)#約数の個数を入れるリスト
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         if j%i==0:
#             F[j]+=1 #jの倍数のところ（約数を）インクリメンとしていく
#     ans += i*F[i]
# #print(F)

#kaitou
for i in range(1,N+1):
    for j in range(1,N+1):
        if i%j==0:
            ans+=i

print(ans)