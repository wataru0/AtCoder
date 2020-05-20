

if __name__ == '__main__':

    N = int(input())
    A = list(map(int,input().split()))

    #print(A[1])
    #バブルソートでリスト内を降順にソートする
    for i in range(N):# 0<=i<N
        for j in range(N-1,i,-1): # jはリストの一番後ろから前に探索していく
            if A[j] > A[j-1]:
                tmp = A[j]
                A[j] = A[j-1]
                A[j-1] = tmp
    #print(A)
    alice = 0
    bob = 0

    for i in range(N):
        if i%2==0:
            alice += A[i]
        else:
            bob += A[i]

    ans = alice - bob
    print(ans)