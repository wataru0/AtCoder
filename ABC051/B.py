K,S = map(int, input().split())
count = 0
# 計算量大きすぎる
# for x in range(K+1):
#     for y in range(K+1):
#         for z in range(K+1):
#             if x+y+z == S:
#                 count += 1

for x in range(K+1):
    for y in range(K+1):
        z = S - x - y
        if 0 <= z <= K:
            count += 1
            
print(count)
