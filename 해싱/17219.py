import sys
n,m=map(int,sys.stdin.readline().split(' '))
x={}
for i in range(n):
    w,pwd=list(map(str,sys.stdin.readline().rstrip().split(' ')))
    x[w]=pwd
for j in range(m):
    print(x[input()])