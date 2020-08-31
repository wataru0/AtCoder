N = int(input())
ans = ''

for i in range(1,99):
    if N <= 26**i: #名前の長さが分かる
        N-=1
        for j in range(i):
            ans += chr(ord('a')+ N%26)
            # ord()の引数に文字を指定するとそのユニコードがintで帰ってくる，
            # chr()に整数を指定すると文字がstrで返ってくる
            N //= 26
        break
    else:
        N -= 26 **i


print(ans[::-1]) #stepが-1つまり後ろから表示
print(chr(ord('a')+18))