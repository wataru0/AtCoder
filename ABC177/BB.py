S=input()
T=input()

ans = len(T)
for s in range(len(S)-len(T)+1):
    # SとTの違いをスライドさせながら計算する
    diff = 0
    # Tを一文字目から順番に照らし合わせていく
    for t in range(len(T)):
        if T[t] != S[s+t]:
            diff += 1
    ans = min(diff,ans)
print(ans)