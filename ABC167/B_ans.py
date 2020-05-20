a,b,c,k = map(int,input().split())

xa = min(k,a)
k -= xa
xb = min(k,b)
k -= xb
xc = k

ans = xa-xc
print(ans)