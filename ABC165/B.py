X = int(input())
m = 100
ans = 0
while X > m:
    m += int(m*0.01)
    ans += 1

print(ans)

