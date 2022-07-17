import sys
from bisect import bisect_left,bisect_right
c=0
m=int(sys.stdin.readline())
m_r=list(map(int,sys.stdin.readline().split(' ')))
n=int(sys.stdin.readline())
n_r=list(map(int,sys.stdin.readline().split(' ')))
m_r.sort()
for _ in range(len(n_r)):
    a=bisect_left(m_r,n_r[_])
    b=bisect_right(m_r,n_r[_])
    rst=a-b
    if(rst==0):
        print(0, end=" ")
    else:
        print(abs(rst), end=" ")

