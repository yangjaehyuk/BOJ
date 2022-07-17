from math import gcd
from itertools import combinations
n=int(input())
for i in range(n):
    su=0
    a=list(map(int,input().split(' ')))
    x=a[0]
    b=list(combinations(a[1:x+1],2))
    for k in b:
            k=list(k)
            if(len(k)==2):
                su+=gcd(k[0],k[1])
    print(su)