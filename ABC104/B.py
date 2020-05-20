S = input()
count = 0
flag = False
if S[0] == "A":
    # print(S[2:-1]) #指定部分獲得できる
    tmp = S[2:-1]
    lower = S[1:]
    for i in range(len(tmp)):
        if tmp[i] == "C":
            count += 1
    if count == 1:
        tmpS = S.replace("A","a")
        tmpSS = tmpS.replace("C","c")
        if tmpSS.islower():
            flag = True

if flag:
    print("AC")
else:
    print("WA")
        
   