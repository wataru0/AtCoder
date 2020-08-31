S = input()
a=''
b=''
c=''
d=''
# for i in range(0,int((len(S)-1)/2)):
#     a+=S[i]
# for i in range(int((len(S)-1)/2)-1,-1,-1):
#     b+=S[i]
# for j in range(int((len(S)+3)/2)-1,len(S)):
#     c+=S[j]
# for j in range(len(S)-1,int((len(S)+3)/2)-2,-1):
#     d+=S[j]

# # print(a)
# # print(b)
# # print(c)
# # print(d)
# if a == b and c==d:
#     print('Yes')
# else:
#     print('No')

mae = ''
usiro = ''
N = len(S)
mae = S[0:int((N-1)/2)]
# eam = S[-int((N-1)/2):]
usiro = S[int((N+3)/2)-1:]
# orisu = S[-int(((N+3)/2))+2:]
print(mae)
# print(eam)
print(usiro)
# print(orisu)
# for i in range(len(mae)-1,-1,-1):
#     a += mae[i]
# # print(a)
# for i in range(len(usiro)-1,-1,-1):
#     b += usiro[i]
# # print(b)

for i in reversed(mae):
    a += i
# print(a)
for i in reversed(usiro):
    b += i

if mae == a and usiro == b:
    print('Yes')
else:
    print('No')
