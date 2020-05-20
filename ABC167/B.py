A,B,C,K = map(int,input().split())
ans = 0
count = 0
# for i in range(A):
#     ans += 1
#     if i 

# while count != K:
#     if count <= A:
#         ans +=1
#         count+=1
#     elif count <= B:
#         count+=1
#     else:
#         ans -= 1
#         count+=1

if A+B>=K:
    if A >= K:
        ans += K
    else:
        ans += A
else:
    ans += A
    
    count = K-(A+B) # 残り枚数
    ans-=count

        
    
print(ans)
        