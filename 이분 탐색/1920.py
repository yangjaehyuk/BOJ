import sys
import bisect
num=int(sys.stdin.readline())
r=list(map(int,sys.stdin.readline().split(' ')))
num1=int(sys.stdin.readline())
r1=list(map(int,sys.stdin.readline().split(' ')))
r.sort()
for _ in range(len(r1)):
    bisect.bisect(r,r1[_])
    if(r1[_] in r):
        print(1)
    else:
        print(0)