N = int(input())
S = input()

ans = 0

# for i in range(N):
#     for j in range(i+1,N):
#         for k in range(j+1,N):
#             if S[i] != S[j] and S[i] != S[k] and S[j] != S[k] and j-i != k-j:
#                 ans += 1
r=0
g=0
b=0   
for s in S:
    if s == "R":
        r += 1
    if s == "G":
        g += 1
    if s == "B":
        b += 1
ans = r*b*b
count = 0
for i in range(N):
    for j in range(i+1,N):
        k = j - i + j
        if j - i != k - j:
            count += 1 

print(ans-count)