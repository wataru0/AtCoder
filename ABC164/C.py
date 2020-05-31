N = int(input())
S = [0]*N
for i in range(N):
    S[i] = input()

ans = 0

# set()は重複する要素が削除される
#print(set(S))
ans = len(set(S))
print(ans)