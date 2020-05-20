N = int(input())
#D = list(map(int,input().split())) # 一行に複数の整数を入力するとき
D = []
for _ in range(N):
    D.append(int(input()))

# バブルソート
for i in range(N):
    for j in range(N-1,i,-1):
        if D[j] > D[j-1]:
            D[j],D[j-1] = D[j-1],D[j]
# こんなことしなくても，sortD = sorted(D,revers=True)とすれば一行でできる

ans = 0
for i in range(N):
    if i == 0:
        tmp = D[0]
        ans += 1
    elif D[i] != tmp:
        ans += 1
        tmp = D[i]
    else:
        continue

print(ans)