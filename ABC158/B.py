N,A,B = map(int,input().split())
R = ''
# for i in range(N):
i = 0
a = 0
b = 0
while i <= N:
    while a <= A:
        R += 'b'
        i += 1
        a += 1
    while b <= B:
        R += 'r'
        i += 1
        b += 1
        
print(R)