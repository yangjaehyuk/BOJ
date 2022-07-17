"""from fractions import Fraction
a,b=list(map(int,input().split(' ')))
c,d=list(map(int,input().split(' ')))
rst=Fraction(a,b)+Fraction(c,d)"""
from math import gcd
a,b=list(map(int,input().split(' ')))
c,d=list(map(int,input().split(' ')))
bunmo=gcd(b,d)*b//gcd(b,d)*d//gcd(b,d)
bunja=a*d//gcd(b,d)+c*b//gcd(b,d)
if(gcd(bunja,bunmo)==1):
    print(bunja,bunmo)
else:
    print(bunja//gcd(bunja,bunmo),bunmo//gcd(bunja,bunmo))