from math import gcd
a,b=list(map(int,input().split(':')))
rst=gcd(a,b)
a=a//rst
b=b//rst
a=str(a)
b=str(b)
print(a+':'+b)