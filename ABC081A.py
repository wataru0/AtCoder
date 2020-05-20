#s1,s2,s3 = (int(x) for x in input().split()) #標準入力複数をintにする処理
# s = map(int(),input().split()) #標準入力複数をintにする処理
S = input()
count = 0
# S = str(s)
# print(S[-1])
if S[-1] == "1":
    count +=1 
if S[-2] == "1":
    count +=1 
if S[-3] == "1":
    count +=1 

# if s1 == 1:
#     count +=1
# if s2 == 1:
#     count+=1
# if s3 == 1:
#     count+=1

print(count)
