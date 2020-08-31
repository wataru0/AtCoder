X = int(input())
go = 0
gohyaku = 0

while X >= 500:
    gohyaku += 1
    X -= 500
    
    
while X >= 5:
    go += 1
    X -= 5
    

ans = (gohyaku * 1000) + (go * 5)
print(ans)
