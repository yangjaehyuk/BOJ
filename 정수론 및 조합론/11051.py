from math import factorial
import sys
n,k=map(int,sys.stdin.readline().split(' '))
rst=factorial(n)//(factorial(k)*factorial(n-k))
print(rst%10007)