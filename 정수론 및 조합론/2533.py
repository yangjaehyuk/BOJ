import sys
from math import factorial
n=int(sys.stdin.readline())
rst=factorial(n)
rst=list(map(int,str(rst)))
for i in reversed(range(len(rst))):
    if(rst[i]!=0):
        print(rst[i])
        break