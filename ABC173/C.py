H,W,K = map(int,input().split())
C = ['']*H
for i in range(H):
    C[i] = input()

numK = 0
ans = 0

# print(C)
# print(C[:,2])
tmpC = C
for h in range(-1,H):
    for w in range(-1,W):
        if h == -1 or w == -1:
            if h != -1:
                tmpC[h] = 'r'
            if w != -1:
                for i in range(H):
                    tmpC[i][w] = 'r'
        print(tmpC)
