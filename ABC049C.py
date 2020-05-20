import random
S = input()
SS = ""
T = ""
words = ["dream","dreamer","erase","eraser"]
Rwords = ["maerd","remaerd","esare","resare"]

# T += words[1]
# T += words[2]
# print(T)

# for i in range(len(words)):
#     if S

#print(S[0])
# if S[0] == "d":
#     T += words[0]

#後ろから読んでいくと簡単に見分けがつく
for i in range(-1,-(len(S)+1),-1): #入力された文字列を後ろから格納していく
    SS += S[i]
    if SS == Rwords[0]:
        SS = ""
    elif SS ==Rwords[1]:
        SS = ""
    elif SS ==Rwords[2]:
        SS = ""
    elif SS ==Rwords[3]:
        SS = ""

if SS == "":
    print("YES")
else:
    print("NO")
#print(SS)

