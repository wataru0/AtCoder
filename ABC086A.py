# 標準入力を複数受け取る
a,b = (int(x) for x in input().split()) # split()で文字を区切る

c = a*b
if c % 2 == 0:
    print("Even")
else:
    print("Odd")