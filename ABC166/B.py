N,K = map(int,input().split())
A = [[0]* N for i in range(K)]
d = [0] * K
for i in range(K):
    d[i] = int(input())
    A[i][:] = map(int,input().split())
     
#print("d",d)
#print("A:",A)
ans = 0
count = [0] * (N+1)
for i in range(K):
    for j in range(d[i]):
        #print(A[i][j])
        count[A[i][j]]=1 # お菓子持っていたら1にする

#print(count)
for i in range(1,len(count)):
    if count[i]==0:
        ans +=1

print(ans)
