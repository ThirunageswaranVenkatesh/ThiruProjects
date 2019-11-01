
a=[17,28,30]
b=[99,16,8]
l=len(a)
_a=0
_b=0

for i in range(0,l):
    if(a[i]>b[i]):
        _a=_a+1
    elif(a[i]<b[i]):
        _b=_b+1

print(_a,_b)