import sys
import fractions
n=int(sys.stdin.readline())
num=list(map(int,sys.stdin.readline().split(' ')))
for i in range(1,len(num)):
    a=fractions.Fraction(num[0],num[i])
    print(str(a.numerator)+'/'+str(a.denominator))