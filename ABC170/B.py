X,Y = map(int,input().split())
ans = "No"
for i in range(101):
    for j in range(101):
        if 2*i+4*j == Y:
            if i+j == X:
                ans = "Yes"
print(ans)

