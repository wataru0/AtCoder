N,A,B = map(int,input().split()) #入力を三つ N A B として受け取る
#print(N,A,B)
strN = str(N) #str型にして配列のようにして扱う
# print(len(strN))
ans = 0

# for i in range(-len(strN),-1):
#     int(strN[i])

# for i in range(1,N+1): # 1 <= i < N+1 の繰り返し
#     L=len(str(i))
#     if L == 1:
#         if i >= A and i <= B:
#             #print("l1:",i)
#             sum += i
#     elif L == 2:
#         #zyu = i / 10 # 10の位
#         #iti = i % 10 # 1の位
#         iti = int(str(i)[-1])
#         zyu =  int(str(i)[-2])
#         tmp = iti + zyu
#         if tmp >= A and tmp <= B:
#             #print("l2:",i)
#             sum += i
#     elif L == 3:
#         iti = int(str(i)[-1])
#         zyu =  int(str(i)[-2])
#         hyaku = int(str(i)[-3])
#         tmp = iti + zyu + hyaku
#         if tmp >= A and tmp <= B:
#             sum += i
#     elif L == 4:
#         iti = int(str(i)[-1])
#         zyu =  int(str(i)[-2])
#         hyaku = int(str(i)[-3])
#         sen = int(str(i)[-4])
#         tmp = iti + zyu + hyaku + sen
#         if tmp >= A and tmp <= B:
#             sum += i

for i in range(1,N+1):
    # sum():リスト要素の合計を計算する，
    # 各桁の和を計算する
    if A <= sum(map(int,list(str(i)))) <= B: # str(i)で文字列化し，list(...)によって各文字を要素とする配列に変換し，map(...)によって再度整数型にした後，sum(...)で合計を計算しています．
        ans +=i

print(ans)



