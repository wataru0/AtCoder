H, W = map(int,input().split())
S = []
# for i in range(H):
#     for j in range(W):
#         input()

for i in range(H):
    S.append(input())

S_ans = []
for row in S:
    S_ans.append(list(row))
#print(S) #['.....', '.#.#.', '.....']
#print(S[1][1]) # #と表示される．二次元配列のように扱える！
count = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            if i == j == 0:
                if S[i][j+1] == "#":
                    count += 1
                if S[i+1][j] == "#":
                    count += 1
                if S[i+1][j+1] == "#":
                    count += 1
            elif i==0 and j == (W-1):
                if S[i][j-1] == "#":
                    count += 1
                if S[i+1][j] == "#":
                    count += 1
                if S[i+1][j-1] == "#":
                    count += 1
            elif i == (H-1) and j == 0:
                if S[i][j+1] == "#":
                    count += 1
                if S[i-1][j] == "#":
                    count += 1
                if S[i-1][j+1] == "#":
                    count += 1
            elif i == (H-1) and j == (W-1):
                if S[i][j-1] == "#":
                    count += 1
                if S[i-1][j] == "#":
                    count += 1
                if S[i-1][j-1] == "#":
                    count += 1
            elif i == (H-1):
                if S[i][j+1] == "#":
                    count += 1
                if S[i-1][j+1] == "#":
                    count += 1
                if S[i-1][j] == "#":
                    count += 1
                if S[i-1][j-1] == "#":
                    count += 1
                if S[i][j-1] == "#":
                    count += 1
            elif j == (W-1):
                if S[i-1][j] == "#":
                    count += 1
                if S[i-1][j-1] == "#":
                    count += 1
                if S[i][j-1] == "#":
                    count += 1
                if S[i+1][j-1] == "#":
                    count += 1
                if S[i+1][j] == "#":
                    count += 1
            else: #端じゃない所
                if S[i][j+1] == "#":
                    count += 1
                if S[i+1][j] == "#":
                    count += 1
                if S[i+1][j+1] == "#":
                    count += 1
                if S[i+1][j-1] == "#":
                    count += 1
                if S[i][j-1] == "#":
                    count += 1
                if S[i-1][j-1] == "#":
                    count += 1
                if S[i-1][j] == "#":
                    count += 1
                if S[i-1][j+1] == "#":
                    count += 1
            S_ans[i][j]=str(count)
            count = 0
                
        # if S[i][j] == "#":
        #     S[i][j+1]
        #     S[i+1][j]
        #     S[i+1][j+1]
for row in S_ans:
    print(''.join(list(map(str,row))))




    