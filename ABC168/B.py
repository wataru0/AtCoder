K = int(input())
S = input()

if len(S) <= K:
    print(S)

else:
    SS = S[0:K]
    print(SS + "...")