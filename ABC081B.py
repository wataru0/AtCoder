N = int(input()) # 標準入力int

A = list(map(int,input().split())) # map(関数，リスト)：リスト全ての要素に関数を適用する　
#A = list((int(x) for x in input().split()))　リストで受け取る，リスト内包表記で書くと[int(x) for x in input().split()]
#A = input().split() # str型で受け取る　複数の時配列になる

#print(A[0]) -> 1番目の数字表示

# tmp = list(map(lambda x: x%2,A))
# print(tmp)
gusuCount = 0
sunukeCount = 0

while True:
    tmp = list(map(lambda x: x%2,A)) # tmpリストに２で割ったあまりを入れる
    for i in range(N):
       if tmp[i] == 0 : #各要素が偶数かどうか確認
           gusuCount += 1

    #要素が全て2で割れたら操作できるのでインクリメント
    if gusuCount == N :
        sunukeCount += 1
        A = list(map(lambda x:x/2,A))
        #print("A:",A)
        gusuCount = 0
    else :
        break

print(sunukeCount)



        

