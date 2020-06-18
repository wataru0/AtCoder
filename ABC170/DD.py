# エラトステネスの篩を使う！O(nlogn)
N = int(input())
A = list(map(int,input().split()))

listA = [0] * (10**6+10)
ans = 0
for i in A:
    if listA[i] != 0:
            listA[i] = 2
            continue
    for j in range(i,10**6+10,i):
        listA[j] += 1

for i in A:
    if listA[i] == 1:
        ans += 1

print(ans)
