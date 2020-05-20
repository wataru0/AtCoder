# import functools
N = int(input())

#for i in range(N+1):
# @functools.lru_cache()
# def L(i):
#     if i == 0:
#         return 2
#     if i == 1:
#         return 1
#     else:
#         return L(i-1) + L(i-2)
# print(L(N))


#上はfunctoolを使うもの下がいい
# 再起的に書くより前の値をキャッシュのように保存していく方が早いし，計算量的にも優れている！！

LL = [2,1] # リュカ数保存するリスト

for i in range(2,N+1):
    LL.append(LL[i-1] + LL[i-2])

print(LL[N])


