K = int(input())
A,B = map(int,input().split())
flag = False

# if A==B:
#     if A % K ==0:
#         flag = True
for i in range(A,B+1,1):
    #print(i)
    if i % K == 0:
        flag = True

if flag:
    print("OK")
else:
    print("NG")