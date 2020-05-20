# 500 A
# 100 B
# 50  C

A = int(input())
B = int(input())
C = int(input())
X = int(input())

total = 0
result = 0


# for i in range(A):
#     if X - 500 > 0:
for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            total=500*i+100*j+50*k
            if X == total:
                result += 1

print(result)
         