a,b,x = map(int,input().split())
ans = 0
# for i in range(a,b+1):
#     if i%x==0:
#         ans += 1

def f(n):
    count = 0
    if n == -1:
        return 0
    else:
        count = n//x + 1 #切り捨て除算　あまりを求める時のチップスtip
        # n以下の整数でxで割り切れるものは，整数nの中にxが何個入るか？という問題に置き換えられる．
        return count

ans = f(b)-f(a-1)

print(ans)