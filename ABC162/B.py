N = int(input())
ans = 0
for a in range(N+1):
    if a % 3 == 0 and a % 5 == 0:
        continue
    elif a % 3 == 0:
        continue
    elif a % 5 == 0:
        continue
    else:
        ans += a
print(ans)