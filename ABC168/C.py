import math
A,B,H,M = map(int,input().split())

#各針の回転角を求める
omega = H*60+M
tanshin = omega*0.5
choshin = omega*6 % 360
#print(tanshin,choshin)#それぞれの，その時間での角度も止まる
#print(max(tanshin,choshin)-min(tanshin,choshin)) 

shita = max(tanshin,choshin)-min(tanshin,choshin)
if shita > 180:
    shita = 360 - shita

#print(shita)
ans = math.sqrt(A**2+B**2-2*A*B*math.cos(math.radians(shita)))
print(ans)