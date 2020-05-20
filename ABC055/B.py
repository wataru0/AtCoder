N = int(input())
power = 1
C = 10**9+7
# そのままN!を求めていくとforの中の値がデカくなっていく
for i in range(1,N+1):
    power *= i
    power %= C

# power = power % (10**9+7)
print(power)