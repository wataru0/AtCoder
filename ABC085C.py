N, Y = map(int,input().split())
x=0
y=0
z=0
sum=0
flag=0

# 三重ループは計算量が多すぎる
# for i in range(N+1):
#     for j in range(N+1):
#         for k in range(N+1):
#             sum = 10000*i+5000*j+1000*k
#             if Y==sum and i+j+k == N:
#                 x=i
#                 y=j
#                 z=k
#                 flag = 1
#                 print(x,y,z)

for i in range(N+1):
    for j in range(N+1):
        k = N - i - j #他の二枚の枚数が決まれば1000円札は計算できる
        if k >= 0:
            sum = 10000*i+5000*j+1000*k
            if Y==sum and i+j+k == N and flag==0:
                x=i
                y=j
                z=k
                flag = 1
                print(x,y,z)
                break
            
if flag == 0:
    print(-1,-1,-1)

# while True:
#     sum = Y - 10000
    
#     if sum >= 0:
#         x += 1
#         Y = sum
#         continue
#     else:
#         break

# while True:
#     sum = Y - 5000
    
#     if sum >= 0:
#         y += 1
#         Y = sum
#         continue
#     else:
#         break

# while True:
#     sum = Y - 1000
    
#     if sum >= 0:
#         z += 1
#         Y = sum
#         continue
#     else:
#         break

# if x+y+z == N:
#     print(x,y,z)
# else:
#     x=y=z=-1
#     print(x,y,z)
