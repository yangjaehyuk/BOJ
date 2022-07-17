import math
n=str(input())
ln=list(map(int,n))
ln=sorted(ln,reverse=False)
sn=list(set(ln))
n=list(n.replace('6','9'))
b=[]
if(ln==sn):
    print(1)
else:
    x=math.ceil(n.count('9')/2)
    b.append(x)
    for i in range(0,9):
        if(str(i) in n):
            b.append(n.count(str(i)))
    print(max(b))