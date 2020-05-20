A = input()

#alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
plain = ""
for i in range(1,27,1):
    for char in list(A):
        ASCII = ord(char)
        num = ASCII - 65 #大文字AのASCIIコードとの差
        num = (num - i) % 26
        ASCII = num + 65
        plain += chr(ASCII)
        
    print("K="+str(i))
    print(plain)
    plain=""
